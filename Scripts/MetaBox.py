#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds # type: ignore
import maya.mel as mel # type: ignore
import sys
import os
import importlib
import traceback

metabox_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
sys.path.append(metabox_path)
print(f"Current directory: {metabox_path}")


from Modeling.Manage import Rename
from Modeling.Edit import SpeedCut
from Modeling.Edit import EvenEdgeLoop
from Modeling.Edit import SpeedBend
from Modeling.Edit import PolyFold
from Modeling.Edit import ArcDeformer
from Modeling.Edit import InstantDrag
from Modeling.Edit import UnBevel
from Modeling.Edit import RoundInset
from Modeling.Edit import CreasePlus
importlib.reload(CreasePlus)
from Modeling.Edit import EdgeSensei
from Modeling.Edit import gs_curvetools
importlib.reload(gs_curvetools)
from Modeling.Edit import AlignEdge
from Modeling.Select import EdgeLoopSmartSelect
from Modeling.Select import SamePositionSelector
from Modeling.Select import IntervalSelectEdge
from Modeling.UV import UVSetEditor
from Metahuman.Custom import BodyPrep
from Metahuman.Custom import BatchImport
from Animation.Blendshape import MorphShape
from Animation import UniversalRigAdapter
import sys
import os

class MetaBox:
    def __init__(self):
        self.window_name = "MetaBoxWindow"
        self.window_title = "MetaBox Dev 1.0"

    def create_button_row(self, labels, commands):
        num_buttons = len(labels)
        form = cmds.formLayout(numberOfDivisions=100)
        buttons = []
        for i, (label, command) in enumerate(zip(labels, commands)):
            button = cmds.button(label=label, command=command, parent=form)
            buttons.append(button)
        
        for i, button in enumerate(buttons):
            if i == 0:
                cmds.formLayout(form, edit=True, attachForm=[(button, 'left', 0), (button, 'top', 0), (button, 'bottom', 0)])
                if num_buttons == 1:
                    cmds.formLayout(form, edit=True, attachForm=[(button, 'right', 0)])
                else:
                    cmds.formLayout(form, edit=True, attachPosition=[(button, 'right', 0, 100 // num_buttons)])
            elif i == num_buttons - 1:
                cmds.formLayout(form, edit=True, attachForm=[(button, 'right', 0), (button, 'top', 0), (button, 'bottom', 0)])
                cmds.formLayout(form, edit=True, attachControl=[(button, 'left', 0, buttons[i-1])])
            else:
                cmds.formLayout(form, edit=True, attachControl=[(button, 'left', 0, buttons[i-1])])
                cmds.formLayout(form, edit=True, attachForm=[(button, 'top', 0), (button, 'bottom', 0)])
                cmds.formLayout(form, edit=True, attachPosition=[(button, 'right', 0, (i + 1) * 100 // num_buttons)])
        
        cmds.setParent('..')

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Create window
    def show(self):
        # Check if the window exists, if so, delete it
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
        if cmds.dockControl(self.window_name + "Dock", exists=True):
            cmds.deleteUI(self.window_name + "Dock")

        # Create main window
        self.window = cmds.window(self.window_name, title=self.window_title, widthHeight=(400, 300), menuBar=True, backgroundColor=(0.2,0.2,0.2), resizeToFitChildren=True)
        main_layout = cmds.columnLayout(adjustableColumn=True)
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent=main_layout)
        # Modeling tab
        modeling_tab = cmds.columnLayout(adjustableColumn=True, parent=tabs)
        modeling_sub_tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent=modeling_tab)
        self.create_modeling_sub_tabs(modeling_sub_tabs)
        # Metahuman tab
        metahuman_tab = cmds.columnLayout(adjustableColumn=True, parent=tabs)
        metahuman_sub_tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent=metahuman_tab)
        self.create_metahuman_sub_tabs(metahuman_sub_tabs)
        # Rigging tab
        rigging_tab = cmds.columnLayout(adjustableColumn=True, parent=tabs)
        rigging_sub_tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent=rigging_tab)
        self.create_rigging_sub_tabs(rigging_sub_tabs)
        # Animation tab
        animation_tab = cmds.columnLayout(adjustableColumn=True, parent=tabs)
        animation_sub_tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent=animation_tab)
        self.create_animation_sub_tabs(animation_sub_tabs)
        # Set tab labels
        cmds.tabLayout(tabs, edit=True, tabLabel=(
            (modeling_tab, "Modeling"),
            (metahuman_tab, "Metahuman"),
            (rigging_tab, "Rigging"),
            (animation_tab, "Animation")
        ))
        cmds.showWindow(self.window)
        cmds.dockControl(self.window_name + "Dock", label=self.window_title, area='right', content=self.window, allowedArea='all')

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Modeling tab
    def create_modeling_sub_tabs(self, parent):
        self.create_modeling_edit_tab(parent)

    def create_modeling_edit_tab(self, parent):
        sub_tab = cmds.columnLayout(adjustableColumn=True, parent=parent)
        cmds.tabLayout(parent, edit=True, tabLabel=((sub_tab, "Edit")))
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close sub_tab
        display_frame = cmds.frameLayout(label="Display", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=display_frame)
        self.create_button_row(["Xray", "Xray Joint"], [self.run_xray, self.run_joint_xray])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        manage_frame = cmds.frameLayout(label="Manage", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=manage_frame)
        self.create_button_row(["Rename", "Batch Import"], [self.run_rename, self.run_batch_import])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        selector_frame = cmds.frameLayout(label="Selector", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=selector_frame)
        self.create_button_row(["Interval Select Edge"], [self.run_select_edge])
        self.create_button_row(["Same Position Selector"], [self.run_same_position_selector])
        self.create_button_row(["Edge Loop Smart Select"], [self.run_edge_loop_smart_select])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        tools_frame = cmds.frameLayout(label="Tools", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=tools_frame)
        self.create_button_row(["Crease Plus", "Speed Cut"], [self.run_crease_plus, self.run_speed_cut])
        self.create_button_row(["ModIt", "PlugIt"], [self.run_modit, self.run_plugit])
<<<<<<< HEAD
        self.create_button_row(["Extra Curve","GS Curve Tools"], [self.run_extra_curve,self.run_gs_curve_tools])
=======
>>>>>>> 7863e4b (Updated Grooms Tools)
        self.create_button_row(["Edge Sensei", "Even Edge Loop"], [self.run_edge_sensei, self.run_even_edge_loop])
        self.create_button_row(["Speed Bend", "Poly Fold"], [self.run_speed_bend, self.run_poly_fold])
        self.create_button_row(["Round Inset", "Arc Deformer"], [self.run_round_inset, self.run_arc_deformer])
        self.create_button_row(["Instant Drag", "Un Bevel"], [ self.run_instant_drag, self.run_unbevel])
        self.create_button_row(["Align Edge", "Extra Curve"], [self.run_align_edge, self.run_extra_curve])
        self.create_button_row(["GS Curve Tools", "Groomer`s Tool"], [self.run_gs_curve_tools, self.run_xgtools])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        uv_frame = cmds.frameLayout(label="UV", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=uv_frame)
        self.create_button_row(["UV Set Editor", "UVDeluxe"], [self.run_uv_set_editor, self.run_uvdeluxe])
        self.create_button_row(["RizomUV Bridge"], [self.run_rizom_uv_bridge])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        cmds.setParent('..')  # Close sub_tab

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Metahuman tab
    def create_metahuman_sub_tabs(self, parent):
        self.create_metahuman_custom_tab(parent)

    def create_metahuman_custom_tab(self, parent):
        sub_tab = cmds.columnLayout(adjustableColumn=True, parent=parent)
        cmds.tabLayout(parent, edit=True, tabLabel=((sub_tab, "Custom")))
        display_frame = cmds.frameLayout(label="Display", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=display_frame)
        self.create_button_row(["Xray","Joint Xray"], [self.run_xray, self.run_joint_xray])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        select_frame = cmds.frameLayout(label="Select", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=select_frame)
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        preparation_frame = cmds.frameLayout(label="Preparation", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=preparation_frame)
        self.create_button_row(["Body Prepare"], [self.run_body_prepare])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        import_frame = cmds.frameLayout(label="Import", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=import_frame)
        self.create_button_row(["Batch Import"], [self.run_batch_import])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        custom_mesh_frame = cmds.frameLayout(label="Custom Mesh", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=custom_mesh_frame)
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        dna_frame = cmds.frameLayout(label="DNA", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=dna_frame)
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        export_frame = cmds.frameLayout(label="Export", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=export_frame)
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        cmds.setParent('..')  # Close sub_tab

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Rigging tab
    def create_rigging_sub_tabs(self, parent):
        self.create_rigging_setup_tab(parent)

    def create_rigging_setup_tab(self, parent):
        sub_tab = cmds.columnLayout(adjustableColumn=True, parent=parent)
        cmds.tabLayout(parent, edit=True, tabLabel=((sub_tab, "Setup")))
        display_frame = cmds.frameLayout(label="Display", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=display_frame)
        self.create_button_row(["Xray", "Xray Joint"], [self.run_xray, self.run_joint_xray])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        select_frame = cmds.frameLayout(label="Select", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=select_frame)
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        setup_frame = cmds.frameLayout(label="Setup", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=setup_frame)
        self.create_button_row(["Advanced Skeleton"], [self.run_advanced_skeleton])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        cmds.setParent('..')  # Close sub_tab

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Animation tab
    def create_animation_sub_tabs(self, parent):
        self.create_animation_edit_tab(parent)
        
    def create_animation_edit_tab(self, parent):
        sub_tab = cmds.columnLayout(adjustableColumn=True, parent=parent)
        cmds.tabLayout(parent, edit=True, tabLabel=((sub_tab, "Edit")))
        display_frame = cmds.frameLayout(label="Display", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=display_frame)
        self.create_button_row(["Xray", "Xray Joint"], [self.run_xray, self.run_joint_xray])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        select_frame = cmds.frameLayout(label="Select", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=select_frame)
        self.create_button_row(["Anim School Picker"], [self.run_anim_school_picker])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        key_frame = cmds.frameLayout(label="Key", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=key_frame)
        self.create_button_row(["bhGhost", "IK/FK Switch"], [self.run_bhghost, self.run_ik_fk_switch])
        self.create_button_row(["aTools", "Keyframe Pro"], [self.open_aTools, self.open_keyframe_pro])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        pose_frame = cmds.frameLayout(label="Pose", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=pose_frame)
        self.create_button_row(["Studio Library"], [self.open_studio_library])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        blendshape_frame = cmds.frameLayout(label="Blendshape", collapsable=True, parent=sub_tab, backgroundColor=(0.15,0.15,0.15))
        cmds.columnLayout(adjustableColumn=True, parent=blendshape_frame)
        self.create_button_row(["Epic Pose Wrangler"], [self.open_epic_pose_wrangler])
        self.create_button_row(["Morph Shape"], [self.run_morph_shape])
        self.create_button_row(["Universal Rig Adapter"], [self.run_universal_rig_adapter])
        cmds.setParent('..')  # Close columnLayout
        cmds.setParent('..')  # Close frameLayout
        cmds.setParent('..')  # Close sub_tab

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Define button functionalities

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Modeling Functions
    # ****************************************************************************************************************
    # Display
    def run_xray(self, *args):
        try:
            result = cmds.modelEditor('modelPanel4', q=True, xr=True)
            cmds.modelEditor('modelPanel4', e=True, xr=not result)
        except Exception as e:
            error_message = f"Error occurred while running Xray: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK') 
    
    def run_joint_xray(self, *args):
        try:
            result = cmds.modelEditor('modelPanel4', q=True, jx=True)
            cmds.modelEditor('modelPanel4', e=True, jx=not result)
        except Exception as e:
            error_message = f"Error occurred while running XrayJoint: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK') 

    # Manage
    def run_rename(self, *args):
        try:
            Rename_Path = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'Manage', 'Rename.py')).replace('\\', '/')
            sys.path.append(Rename_Path)
            Rename.UI()
        except Exception as e:
            error_message = f"Error occurred while running Rename: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_batch_import(self, *args):
        try:
            BatchImport.run()
        except Exception as e:
            error_message = f"Error occurred while running Batch Import: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    # Edit
    def run_crease_plus(self, *args):
        try:
            crease_plus_dir = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'Edit', 'CreasePlus')).replace('\\', '/')
            print(f"CreasePlus directory: {crease_plus_dir}")
            if crease_plus_dir not in sys.path:
                sys.path.append(crease_plus_dir)
            from Modeling.Edit.CreasePlus import CreasePlusMain
            CreasePlusMain.start()
            print("CreasePlus loaded successfully")
        except Exception as e:
            error_message = f"Error occurred while running Crease Plus: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def run_speed_cut(self, *args):
        try:
            SpeedCut.run()
        except Exception as e:
            error_message = f"Error occurred while running Speed Cut: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_gs_curve_tools(self, *args):
        try:
            gs_curvetools_path = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'Edit', 'gs_curvetools')).replace('\\', '/')
            if gs_curvetools_path not in sys.path:
                sys.path.insert(0, gs_curvetools_path)

            # Import the sub modules
            gs_curve_tools_subpaths = [
                os.path.join(gs_curvetools_path, 'core').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'constants').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'ui').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'uv_editor').replace('\\', '/'),
            ]
            for path in gs_curve_tools_subpaths:
                if path not in sys.path:
                    sys.path.insert(0, path)

            # Import the main module
            from Modeling.Edit.gs_curvetools import main as ct_main
            # Run the main function
            ct_main.main()

            # If windows exists, refresh it
            if cmds.pluginInfo('gs_curvetools', query=True, loaded=True):
                from importlib import reload
                from Modeling.Edit.gs_curvetools.utils import utils as ct_ut
                reload(ct_ut)
                ct_ut.resetUI()
                print("GS Curve Tools refreshed successfully")

        except Exception as e:
            error_message = f"Error occurred while running GS Curve Tools: {str(e)}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def run_modit(self, *args):
        try:
            modit_path = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'Edit', 'ModIt')).replace('\\', '/')
            modlit_sub_paths = [
                os.path.join(modit_path, 'Classes'),
                os.path.join(modit_path, 'Icons'),
                os.path.join(modit_path, 'Mesh'),
                os.path.join(modit_path, 'Preferences'),
                os.path.join(modit_path, 'Shaders'),
                os.path.join(modit_path, 'Tools')
            ]
            for path in modlit_sub_paths:
                if path not in sys.path:
                    sys.path.append(path)
            # Add modit_icon_paths to MAYA_PLUG_IN_PATH
            os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join(modlit_sub_paths)
            modit_ui_path = os.path.join(modit_path, 'ModIt_UI.py').replace('\\', '/')
            if modit_ui_path not in sys.path:
                sys.path.append(os.path.dirname(modit_ui_path))
            from Modeling.Edit.ModIt import ModIt_UI
            importlib.reload(ModIt_UI)
            ModIt_UI
        except Exception as e:
            error_message = f"Error occurred while running ModIt: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_plugit(self, *args):
        try:
<<<<<<< HEAD
            PlugIt_Path = os.path.normpath(os.path.join(current_dir, 'Modeling', 'Edit', 'PlugIt')).replace('\\', '/')
=======
            PlugIt_Path = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'Edit', 'PlugIt')).replace('\\', '/')
>>>>>>> 7863e4b (Updated Grooms Tools)
            plugIt_sub_paths = [
                os.path.join(PlugIt_Path, 'Icons'),
                os.path.join(PlugIt_Path, 'LIBRARY'),
                os.path.join(PlugIt_Path, 'PlugIt_Creation'),
                os.path.join(PlugIt_Path, 'Preferences'),
                os.path.join(PlugIt_Path, 'Tools'),
            ]
            for path in plugIt_sub_paths:
                if path not in sys.path:
                    sys.path.append(path)
            os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join(plugIt_sub_paths)
            plugIt_ui_path = os.path.join(PlugIt_Path, 'PlugIt_UI.py').replace('\\', '/')
            if plugIt_ui_path not in sys.path:
                sys.path.append(os.path.dirname(plugIt_ui_path))
            from Modeling.Edit.PlugIt import PlugIt_UI
            importlib.reload(PlugIt_UI)
            PlugIt_UI.showUI()
        except Exception as e:
            error_message = f"Error occurred while running PlugIt: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

<<<<<<< HEAD
=======
    def run_xgtools(self, *args):
        try:

            import maya.cmds as cmds
            print("Successfully imported maya.cmds")
            
            import sys
            import os
            import traceback

            xgtc_parent_dir = os.path.join(metabox_path, 'Modeling', 'Edit')
            if xgtc_parent_dir not in sys.path:
                sys.path.insert(0, xgtc_parent_dir)

            xgtc_path = os.path.join(xgtc_parent_dir, 'xgtc').replace('\\', '/')
            if xgtc_path not in sys.path:
                sys.path.insert(0, xgtc_path)

            xgtc_scripts_path = os.path.join(xgtc_path, 'scripts').replace('\\', '/')
            if xgtc_scripts_path not in sys.path:
                sys.path.insert(0, xgtc_scripts_path)

            xgtc_icons_path = os.path.join(xgtc_path, 'icons').replace('\\', '/')
            if xgtc_icons_path not in sys.path:
                sys.path.insert(0, xgtc_icons_path)

            from Modeling.Edit.xgtc.scripts import xgToolsUI_user_sub
            print("Successfully imported XGTools modules")

            xgToolsUI_user_sub.xgToolsUI()

        except ImportError as e:
            error_message = f"Error importing modules for XGTools: {str(e)}"
            print(error_message)
            cmds.warning(error_message)
        except Exception as e:
            error_message = f"Error occurred while running XGTools: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK') 

>>>>>>> 7863e4b (Updated Grooms Tools)
    def run_edge_sensei(self, *args):
        try:
            EdgeSensei.run()
        except Exception as e:
            error_message = f"Error occurred while running Edge Sensei: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_even_edge_loop(self, *args):
        try:
            EvenEdgeLoop.run()
        except Exception as e:
            error_message = f"Error occurred while running Even Edge Loop: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK') 

    def run_speed_bend(self, *args):
        try:
            SpeedBend.run()
        except Exception as e:
            error_message = f"Error occurred while running Speed Bend: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_poly_fold(self, *args):
        try:
            PolyFold.run()
        except Exception as e:
            error_message = f"Error occurred while running Poly Fold: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_round_inset(self, *args):
        try:
            RoundInset.run()
        except Exception as e:
            error_message = f"Error occurred while running Round Inset: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_arc_deformer(self, *args):
        try:
            ArcDeformer.run()
        except Exception as e:
            error_message = f"Error occurred while running Arc Deformer: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_instant_drag(self, *args):
        try:
            InstantDrag.run()
        except Exception as e:
            error_message = f"Error occurred while running Instant Drag: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_unbevel(self, *args):
        try:
            UnBevel.run()
        except Exception as e:
            error_message = f"Error occurred while running UnBevel: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_extra_curve(self, *args):
        try:
            mel.eval('polyToCurve -form 2 -degree 3 -conformToSmoothMeshPreview 1')
        except Exception as e:
            error_message = f"Error occurred while running ExtractCurve: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    # Select
    def run_edge_loop_smart_select(self, *args):
        try:
            EdgeLoopSmartSelect.run()
        except Exception as e:
            error_message = f"Error occurred while running Edge Loop Smart Select: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_select_edge(self, *args):
        try:
            IntervalSelectEdge.show()
        except Exception as e:
            error_message = f"Error occurred while running Interval Select Edge: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_same_position_selector(self, *args):
        try:
            SamePositionSelector.show()
        except Exception as e:
            error_message = f"Error occurred while running SamePositionSelector: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_align_edge(self, *args):
        try:
            AlignEdge.run()
        except Exception as e:
            error_message = f"Error occurred while running Align Edge: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    # UV
    def run_uv_set_editor(self, *args):
        try:
            UVSetEditor.show()
        except Exception as e:
            error_message = f"Error occurred while opening UV Set Editor: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_uvdeluxe(self, *args):
        try:
            from Modeling.UV.UVDeluxe import uvdeluxe
            uvdeluxe.createUI()
        except Exception as e:
            error_message = f"Error occurred while opening UVDeluxe: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_rizom_uv_bridge(self, *args):
        try:
            rizomuvbridge_Path = os.path.normpath(os.path.join(metabox_path, 'Modeling', 'UV', 'RizomUVBridge')).replace('\\', '/')
            if rizomuvbridge_Path not in sys.path:
                sys.path.insert(0, rizomuvbridge_Path)
            rizomuvbridge_lua_path = os.path.join(rizomuvbridge_Path, 'RizomUVBridge.lua').replace('\\', '/')
            if rizomuvbridge_lua_path not in sys.path:
                sys.path.insert(0, rizomuvbridge_lua_path)
            from Modeling.UV.RizomBridge import RizomUVBridge
            RizomUVBridge.run()
        except Exception as e:
            error_message = f"Error occurred while running RizomUV Bridge: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Rigging Functions
    # ****************************************************************************************************************
    def run_advanced_skeleton(self, *args):
        try:
            adv_sub_path = [
                os.path.join(metabox_path, 'Animation', 'AdvancedSkeleton').replace('\\', '/'),
                os.path.join(metabox_path, 'Animation', 'AdvancedSkeleton', 'AdvancedSkeleton5Files').replace('\\', '/')
            ]
            for path in adv_sub_path:
                if path not in sys.path:
                    sys.path.insert(0, path)
            # If advancedSkeleton5Files does not exist, run the adv_install.py and the launch.py, else run the adv_launch.py directly
            if not os.path.exists(os.path.join(metabox_path, 'Animation', 'AdvancedSkeleton', 'adv_install.py').replace('\\', '/')):
                from Animation.AdvancedSkeleton import adv_install
                adv_install.install()
            from Animation.AdvancedSkeleton import adv_launch
            adv_launch.launch()
        except Exception as e:
            error_message = f"Error occurred while running Advanced Skeleton: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Metahuman Functions
    # ****************************************************************************************************************
    # Preparation
    def run_body_prepare(self, *args):
        try:
            BodyPrep.run()
        except Exception as e:
            error_message = f"Error occurred while running Body Prepare: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Animation Functions
    # ****************************************************************************************************************
    # Pose
    def open_aTools(self, *args):
        try:
            # Get aTools path
            aTools_Path = os.path.normpath(os.path.join(metabox_path, 'Animation', 'aTools')).replace('\\', '/')
            if aTools_Path not in sys.path:
                sys.path.insert(0, aTools_Path)
            parent_dir = os.path.dirname(aTools_Path)
            if parent_dir not in sys.path:
                sys.path.insert(0, parent_dir)
            atools = importlib.import_module('aTools')
            importlib.reload(atools)
            animTools = importlib.import_module('aTools.animTools')
            importlib.reload(animTools)
            animBar = importlib.import_module('aTools.animTools.animBar')
            importlib.reload(animBar)
            animBarUI = importlib.import_module('aTools.animTools.animBar.animBarUI')
            importlib.reload(animBarUI)
            animBarUI.show('refresh')
        except Exception as e:
            error_message = f"Error occurred while running aTools: {e}"
            print(f"Detailed error: {traceback.format_exc()}")
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def open_keyframe_pro(self, *args):
        try:
            keyframe_pro_paths = [
                os.path.join(metabox_path, 'Animation', 'keyframe_pro'),
                os.path.join(metabox_path, 'Animation', 'keyframe_pro', 'keyframe_pro'),
                os.path.join(metabox_path, 'Animation', 'keyframe_pro', 'keyframe_pro_maya')
            ]
            for path in keyframe_pro_paths:
                if path not in sys.path:
                    sys.path.insert(0, path)
            for path in sys.path:
                print("Added the keyframe_Pro submoudle path: ", path)
            from Animation.keyframe_pro.keyframe_pro_maya.maya_to_keyframe_pro import MayaToKeyframePro
            MayaToKeyframePro.display()
        except Exception as e:
            error_message = f"Error occurred while running Keyframe Pro: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def open_studio_library(self, *args):
        try:
            studiolibrary_path = os.path.normpath(os.path.join(metabox_path, 'Animation', 'studiolibrary')).replace('\\', '/')
            studiolibrary_sub_paths = [
                os.path.join(studiolibrary_path, 'src'),
                os.path.join(studiolibrary_path, 'src', 'studiolibrary'),
                os.path.join(studiolibrary_path, 'src', 'studiolibrarymaya'),
                os.path.join(studiolibrary_path, 'src', 'studioqt'),
                os.path.join(studiolibrary_path, 'src', 'mutils'),
                os.path.join(studiolibrary_path, 'src', 'studiovendor')
            ]
            # Added the main path to sys.path
            if studiolibrary_path not in sys.path:
                sys.path.insert(0, studiolibrary_path)
            # Added the sub path to sys.path
            for path in studiolibrary_sub_paths:
                if path not in sys.path:
                    sys.path.insert(0, path.replace('\\', '/'))
            for path in sys.path:
                print("Added the studiolibrary submoudle path: ", path)
            # Import studiolibrary from the studiolibrary_path with importlib
            studiolibrary = importlib.import_module('studiolibrary')
            importlib.reload(studiolibrary)
            # Run studiolibrary
            studiolibrary.main()
        except Exception as e:
            error_message = f"Error occurred while running Studio Library: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_anim_school_picker(self, *args):
        try:
            # Added the path to the AnimSchoolPicker.mel file
            animpicker_path = os.path.normpath(os.path.join(metabox_path, 'Animation', 'AnimSchoolPicker')).replace('\\', '/')
            if animpicker_path not in sys.path:
                sys.path.insert(0, animpicker_path)

            # Get Maya Version
            maya_version = cmds.about(version=True).split()[0]

            # Set plugin path
            animpicker_plugin_path = os.path.join(animpicker_path, maya_version).replace('\\', '/')
            # Added the plugin path to MAYA_PLUG_IN_PATH
            os.environ['MAYA_PLUG_IN_PATH'] = animpicker_plugin_path

            # load the plugin
            animpicker_mll = os.path.join(animpicker_plugin_path, 'AnimSchoolPicker.mll').replace('\\', '/')
            cmds.loadPlugin(animpicker_mll, quiet=True)
            cmds.AnimSchoolPicker()
            print(f"Anim School Picker loaded successfully from {animpicker_mll}")
        except Exception as e:
            error_message = f"Error occurred while running Anim School Picker: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
    
    def run_bhghost(self, *args):
        try:
            bhghost_path = os.path.normpath(os.path.join(metabox_path, 'Animation', 'bhGhost')).replace('\\', '/')
            print(bhghost_path)
            if bhghost_path not in sys.path:
                sys.path.insert(0, bhghost_path)
            bhghost_mel = os.path.join(bhghost_path, 'bhGhost.mel').replace('\\', '/')
            print(bhghost_mel)
            mel.eval(f'source "{bhghost_mel}";')
            print(f"bhGhost loaded successfully from {bhghost_mel}")
        except Exception as e:
            error_message = f"Error occurred while running bhGhost: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def run_ik_fk_switch(self, *args):
        try:
            IK_FK_Switch_Path = os.path.normpath(os.path.join(metabox_path, 'Animation', 'IK_FK_Switch')).replace('\\', '/')
            if IK_FK_Switch_Path not in sys.path:
                sys.path.insert(0, IK_FK_Switch_Path)
            from Animation import IK_FK_Switcher
            IK_FK_Switcher.run()
        except Exception as e:
            error_message = f"Error occurred while running IK/FK Switch: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    # Blendshape
    def open_epic_pose_wrangler(self, *args):
        try:
            # Add Epic Pose Wrangler path
            epic_pose_wrangler_path = os.path.join(metabox_path, 'Animation', 'epic_pose_wrangler').replace('\\', '/')
            sys.path.append(epic_pose_wrangler_path)
            print(epic_pose_wrangler_path)
            print(f"Attempting to import Epic Pose Wrangler from: {epic_pose_wrangler_path}")            
            # Get current Maya version
            maya_version = cmds.about(version=True).split()[0]            
            # Load necessary plugins
            plugin_dir = os.path.join(epic_pose_wrangler_path, 'plugins', 'Windows', maya_version)
            for plugin in ['embeddedRL4.mll', f'MayaUE4RBFPlugin{maya_version}.mll', 'MayaUERBFPlugin.mll']:
                plugin_path = os.path.join(plugin_dir, plugin)
                if os.path.exists(plugin_path):
                    if not cmds.pluginInfo(plugin_path, query=True, loaded=True):
                        cmds.loadPlugin(plugin_path)
                else:
                    print(f"Warning: Plugin file does not exist: {plugin_path}")

            # Import and run Epic Pose Wrangler
            sys.path.insert(0, os.path.dirname(epic_pose_wrangler_path))
            from Animation.epic_pose_wrangler import main
            pose_wrangler = main.PoseWrangler()
            
            cmds.inViewMessage(amg='Epic Pose Wrangler loaded successfully', pos='midCenter', fade=True)
        except Exception as e:
            error_message = f"Error occurred while running Epic Pose Wrangler: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    def run_universal_rig_adapter(self, *args):
        try:
            UniversalRigAdapter.run()
        except Exception as e:
            error_message = f"Error occurred while running Universal Rig Adapter: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')
    
    def run_morph_shape(self, *args):
        try:
            MorphShape.show()
        except Exception as e:
            error_message = f"Error occurred while running MorphShape: {e}"
            cmds.warning(error_message)
            cmds.confirmDialog(title='Error', message=error_message, button=['OK'], defaultButton='OK')

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show():
    MetaBox().show()

if __name__ == "__main__":
    show()