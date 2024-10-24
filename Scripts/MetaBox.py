#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=====================================IMPORT=====================================
from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds # type: ignore
import maya.mel as mel # type: ignore
import sys
import os
import importlib
import traceback
import subprocess
import webbrowser

#=====================================IMPORT FUNCTIONS=====================================
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
#=====================================PATH=====================================
METABOX_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
sys.path.append(METABOX_PATH)
print(f"Current directory: {METABOX_PATH}")
#=====================================VARIABLES=====================================
TOOLBOX_NAME = "MetaBox"
TOOLBOX_VERSION = "1.0"
TOOLBOX_AUTHOR = "VIRTUOS"
TOOLBOX_HELP = f"https://ac.virtuosgames.com:8443/display/TK/{TOOLBOX_NAME}"
ICON_PATH = os.path.join(METABOX_PATH, "Icons", TOOLBOX_NAME + ".png")
#=====================================UI BUTTONS COMPONENTS=====================================
class RoundedButton(QtWidgets.QPushButton):
    """
    Custom rounded button class

    Features:
    - Rounded design
    - Custom color and hover effect
    - Bold text
    """
    def __init__(self, text="", icon=None):
        super(RoundedButton, self).__init__(text)
        if icon:
            self.setIcon(icon)
            self.setIconSize(QtCore.QSize(24, 24))
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #D0D0D0;
                color: #303030;
                border-radius: 10px;
                padding: 5px;
                font-weight: bold;
                text-align: center;
                
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #C0C0C0;
            }
            """
        )

#=====================================UI MAIN WINDOW COMPONENTS=====================================

class MetaBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MetaBox, self).__init__(parent)
        self.setWindowTitle(TOOLBOX_NAME)
        self.setMinimumWidth(300)

        # Set up the windows icon
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        else:
            print(f"WARNING: Icon file not found: {ICON_PATH}")

        # Set the window flags always on top
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # Initialize toggle state
        self.toggle_state = False

        # Initialize language state
        self.is_chinese = False

        # Initialize translation dictionary
        self.translations = {
            'en_US': {
                "Modeling": "Modeling",
                "Metahuman": "Metahuman",
                "Rigging": "Rigging",
                "Animation": "Animation",
                "Edit":"Edit",
                "Display":"Display",
                "Manage":"Manage",
                "Select":"Select",
                "Tools":"Tools",
                "UV":"UV",
                "Custom":"Custom",
                "Setup":"Setup",
                "Animation Edit":"Animation Edit",
                "Key":"Key",
                "Pose":"Pose",
                "Blendshape":"Blendshape",
                "Xray":"Xray",
                "Joint Xray":"Joint Xray",
                "Rename":"Rename",
                "Import":"Import",
                "Batch Import":"Batch Import",
                "Interval Select Edge":"Interval Select Edge",
                "Same Position Selector":"Same Position Selector",
                "Edge Loop Smart Select":"Edge Loop Smart Select",
                "Even Edge Loop":"Even Edge Loop",
                "Speed Bend":"Speed Bend",
                "Poly Fold":"Poly Fold",
                "Round Inset":"Round Inset",
                "Arc Deformer":"Arc Deformer",
                "Instant Drag":"Instant Drag",
                "Un Bevel":"Un Bevel",
                "Align Edge":"Align Edge", 
                "Extra Curve":"Extra Curve",
                "UV Set Editor":"UV Set Editor",
                "UVDeluxe":"UVDeluxe",
                "RizomUV Bridge":"RizomUV Bridge",
                "Preparation":"Preparation",
                "Body Prep":"Body Prep",
                "Custom Mesh":"Custom Mesh",
                "DNA":"DNA",
                "Export":"Export",
                "Advanced Skeleton":"Advanced Skeleton",
                "Anim School Picker":"Anim School Picker",
                "bhGhost":"bhGhost",
                "IK/FK Switch":"IK/FK Switch",
                "aTools":"aTools",
                "Keyframe Pro":"Keyframe Pro",
                "Studio Library":"Studio Library",
                "Epic Pose Wrangler":"Epic Pose Wrangler",
                "Morph Shape":"Morph Shape",
                "Universal Rig Adapter":"Universal Rig Adapter",
                "document": "Document",
                "Help": "Help",
                "Switch Language": "Switch Language"
            },
            'zh_CN': {
                "Modeling": "建模",
                "Metahuman": "Metahuman",
                "Rigging": "绑定",
                "Animation": "动画",
                "Edit":"编辑",
                "Display":"显示",
                "Manage":"管理",
                "Select":"选择",
                "Tools":"工具",
                "UV":"UV",
                "Custom":"自定义",
                "Setup":"设置",
                "Animation Edit":"动画编辑",
                "Key":"关键帧",
                "Pose":"姿势",
                "Blendshape":"混合形状",
                "Xray":"X光",
                "Joint Xray":"关节X光",
                "Rename":"重命名",
                "Batch Import":"批量导入",
                "Import":"导入",
                "Interval Select Edge":"间隔选择边",
                "Same Position Selector":"相同位置选择器",
                "Edge Loop Smart Select":"边缘循环智能选择",
                "Even Edge Loop":"等边循环",
                "Speed Bend":"速度弯曲",
                "Poly Fold":"多边形折叠",
                "Round Inset":"圆角插入",
                "Arc Deformer":"弧形变形器",
                "Instant Drag":"瞬时拖拽",
                "Un Bevel":"Un Bevel",
                "Align Edge":"对齐边缘", 
                "Extra Curve":"额外曲线",
                "UV Set Editor":"UV集编辑器",
                "UVDeluxe":"UVDeluxe",
                "RizomUV Bridge":"RizomUV桥接",
                "Preparation":"准备",
                "Body Prep":"身体准备",
                "Custom Mesh":"自定义网格",
                "DNA":"DNA",
                "Export":"导出",
                "Advanced Skeleton":"高级骨骼",
                "Anim School Picker":"动画学校选择器",
                "bhGhost":"bhGhost",
                "IK/FK Switch":"IK/FK切换",
                "aTools":"aTools",
                "Keyframe Pro":"关键帧Pro",
                "Studio Library":"Studio Library",
                "Epic Pose Wrangler":"Epic姿势编写器",
                "Morph Shape":"混合形状",
                "Universal Rig Adapter":"通用绑定适配器",
                "document": "文档",
                "Help": "帮助",
                "Switch Language": "切换语言"
            }
        }

        self.current_language = "en_US"

        self.create_widgets()
        self.create_layouts()
        self.create_connections()
#===================================== UI COMPONENTS =====================================
    def create_widgets(self):
        # Create help button
        self.help_btn = QtWidgets.QPushButton("document")
        self.help_btn.setToolTip("帮助")
        self.help_btn.setFixedSize(60, 20)
        self.help_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: gray;
                font-weight: bold;
            }
            QPushButton:hover {
                color: black;
            }
        """)

        # Create switch language button
        self.switch_language_btn = RoundedButton("Switch Language")
        self.switch_language_btn.setToolTip("切换语言")
        self.switch_language_btn.setFixedSize(60, 20)
        self.switch_language_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: gray;
                font-weight: bold;
            }
            QPushButton:hover {
                color: black;
            }
        """)

        # Create tabs
        self.modeling_tab_btn = RoundedButton("Modeling")
        self.metahuman_tab_btn = RoundedButton("Metahuman")
        self.rigging_tab_btn = RoundedButton("Rigging")
        self.animation_tab_btn = RoundedButton("Animation")

        # Modeling group widgets
        self.modeling_display_group = QtWidgets.QGroupBox("Display")
        self.modeling_xray_btn = RoundedButton("Xray")
        self.modeling_joint_xray_btn = RoundedButton("Joint Xray")
        self.modeling_manage_group = QtWidgets.QGroupBox("Manage")
        self.modeling_rename_btn = RoundedButton("Rename")
        self.modeling_batch_import_btn = RoundedButton("Batch Import")
        self.modeling_select_group = QtWidgets.QGroupBox("Select")
        self.modeling_interval_select_edge_btn = RoundedButton("Interval Select Edge")
        self.modeling_same_position_selector_btn = RoundedButton("Same Position Selector")
        self.modeling_edge_loop_smart_select_btn = RoundedButton("Edge Loop Smart Select")
        self.modeling_even_edge_loop_btn = RoundedButton("Even Edge Loop")
        self.modeling_tools_group = QtWidgets.QGroupBox("Tools")
        self.modeling_crease_plus_btn = RoundedButton("Crease Plus")
        self.modeling_speed_cut_btn = RoundedButton("Speed Cut")
        self.modeling_modit_btn = RoundedButton("ModIt")
        self.modeling_plugit_btn = RoundedButton("PlugIt")
        self.modeling_zirail_btn = RoundedButton("Zirail")
        self.modeling_xgtools_btn = RoundedButton("Groomer`s Tool")
        self.modeling_gs_curve_tools_btn = RoundedButton("GS Curve Tools")
        self.modeling_reset_gs_curve_tools_btn = RoundedButton("GS Curve Tools Reset")
        self.modeling_close_gs_curve_tools_btn = RoundedButton("GS Curve Tools Close")
        self.modeling_edge_sensei_btn = RoundedButton("Edge Sensei")
        self.modeling_round_inset_btn = RoundedButton("Round Inset")
        self.modeling_arc_deformer_btn = RoundedButton("Arc Deformer")
        self.modeling_instant_drag_btn = RoundedButton("Instant Drag")
        self.modeling_unbevel_btn = RoundedButton("Un Bevel")
        self.modeling_align_edge_btn = RoundedButton("Align Edge")
        self.modeling_extra_curve_btn = RoundedButton("Extra Curve")
        self.modeling_uv_group = QtWidgets.QGroupBox("UV")
        self.modeling_uvdeluxe_btn = RoundedButton("UVDeluxe")
        self.modeling_rizom_uv_bridge_btn = RoundedButton("RizomUV Bridge")
        self.modeling_uv_set_editor_btn = RoundedButton("UV Set Editor")

        # Metahuman group widgets
        self.metahuman_display_group = QtWidgets.QGroupBox("Display")
        self.metahuman_xray_btn = RoundedButton("Xray")
        self.metahuman_joint_xray_btn = RoundedButton("Joint Xray")
        self.metahuman_import_group = QtWidgets.QGroupBox("Import")
        self.metahuman_select_group = QtWidgets.QGroupBox("Select")
        self.metahuman_preparation_group = QtWidgets.QGroupBox("Preparation")
        self.metahuman_body_prepare_btn = RoundedButton("Body Prepare")
        self.metahuman_custommesh_group = QtWidgets.QGroupBox("Custom Mesh")
        self.metahuman_dna_group = QtWidgets.QGroupBox("DNA")
        self.metahuman_export_group = QtWidgets.QGroupBox("Export")

        # Rigging group widgets
        self.rigging_display_group = QtWidgets.QGroupBox("Display")
        self.rigging_xray_btn = RoundedButton("Xray")
        self.rigging_joint_xray_btn = RoundedButton("Joint Xray")
        self.rigging_import_group = QtWidgets.QGroupBox("Import")
        self.rigging_select_group = QtWidgets.QGroupBox("Select")
        self.rigging_setup_group = QtWidgets.QGroupBox("Setup")
        self.rigging_advanced_skeleton_btn = RoundedButton("Advanced Skeleton")

        # Animation group widgets
        self.animation_display_group = QtWidgets.QGroupBox("Display")
        self.animation_xray_btn = RoundedButton("Xray")
        self.animation_joint_xray_btn = RoundedButton("Joint Xray")
        self.animation_import_group = QtWidgets.QGroupBox("Import")
        self.animation_select_group = QtWidgets.QGroupBox("Select")
        self.animation_key_group = QtWidgets.QGroupBox("Key")
        self.animation_pose_group = QtWidgets.QGroupBox("Pose")
        self.animation_blendshape_group = QtWidgets.QGroupBox("Blendshape")

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setSpacing(7)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Tabs Layout
        tabs_layout = QtWidgets.QTabWidget(self)
        main_layout.addWidget(tabs_layout)

        # Modeling Layout
        modeling_tab = QtWidgets.QWidget()
        modeling_layout = QtWidgets.QVBoxLayout(modeling_tab)
        modeling_layout.addWidget(self.modeling_display_group)
        display_layout = QtWidgets.QVBoxLayout(self.modeling_display_group)
        display_layout.addWidget(self.modeling_xray_btn)
        display_layout.addWidget(self.modeling_joint_xray_btn)
        modeling_layout.addWidget(self.modeling_manage_group)
        manage_layout = QtWidgets.QVBoxLayout(self.modeling_manage_group)
        manage_layout.addWidget(self.modeling_rename_btn)
        manage_layout.addWidget(self.modeling_batch_import_btn)
        modeling_layout.addWidget(self.modeling_select_group)
        select_layout = QtWidgets.QVBoxLayout(self.modeling_select_group)
        select_layout.addWidget(self.modeling_interval_select_edge_btn)
        select_layout.addWidget(self.modeling_same_position_selector_btn)
        select_layout.addWidget(self.modeling_edge_loop_smart_select_btn)
        select_layout.addWidget(self.modeling_even_edge_loop_btn)
        modeling_layout.addWidget(self.modeling_tools_group)
        tools_layout = QtWidgets.QVBoxLayout(self.modeling_tools_group)
        tools_layout.addWidget(self.modeling_crease_plus_btn)
        tools_layout.addWidget(self.modeling_speed_cut_btn)
        tools_layout.addWidget(self.modeling_modit_btn)
        tools_layout.addWidget(self.modeling_plugit_btn)
        tools_layout.addWidget(self.modeling_zirail_btn)
        tools_layout.addWidget(self.modeling_xgtools_btn)
        tools_layout.addWidget(self.modeling_gs_curve_tools_btn)
        tools_layout.addWidget(self.modeling_reset_gs_curve_tools_btn)
        tools_layout.addWidget(self.modeling_close_gs_curve_tools_btn)
        tools_layout.addWidget(self.modeling_edge_sensei_btn)
        tools_layout.addWidget(self.modeling_round_inset_btn)
        tools_layout.addWidget(self.modeling_arc_deformer_btn)
        tools_layout.addWidget(self.modeling_instant_drag_btn)
        tools_layout.addWidget(self.modeling_unbevel_btn)
        tools_layout.addWidget(self.modeling_align_edge_btn)
        tools_layout.addWidget(self.modeling_extra_curve_btn)
        modeling_layout.addWidget(self.modeling_uv_group)
        uv_layout = QtWidgets.QVBoxLayout(self.modeling_uv_group)
        uv_layout.addWidget(self.modeling_uv_set_editor_btn)
        uv_layout.addWidget(self.modeling_uvdeluxe_btn)
        uv_layout.addWidget(self.modeling_rizom_uv_bridge_btn)
        tabs_layout.addTab(modeling_tab, "Modeling")

        # Metahuman Layout
        metahuman_tab = QtWidgets.QWidget()
        metahuman_layout = QtWidgets.QVBoxLayout(metahuman_tab)
        metahuman_layout.addWidget(self.metahuman_display_group)
        metahuman_display_layout = QtWidgets.QVBoxLayout(self.metahuman_display_group)
        metahuman_display_layout.addWidget(self.metahuman_xray_btn)
        metahuman_display_layout.addWidget(self.metahuman_joint_xray_btn)
        metahuman_layout.addWidget(self.metahuman_import_group)
        metahuman_layout.addWidget(self.metahuman_select_group)
        metahuman_layout.addWidget(self.metahuman_preparation_group)
        preparation_layout = QtWidgets.QVBoxLayout(self.metahuman_preparation_group)
        preparation_layout.addWidget(self.metahuman_body_prepare_btn)
        metahuman_layout.addWidget(self.metahuman_custommesh_group)
        metahuman_layout.addWidget(self.metahuman_dna_group)
        metahuman_layout.addWidget(self.metahuman_export_group)
        tabs_layout.addTab(metahuman_tab, "Metahuman")

        # Rigging Layout
        rigging_tab = QtWidgets.QWidget()
        rigging_layout = QtWidgets.QVBoxLayout(rigging_tab)
        rigging_layout.addWidget(self.rigging_display_group)
        rigging_display_layout = QtWidgets.QVBoxLayout(self.rigging_display_group)
        rigging_display_layout.addWidget(self.rigging_xray_btn)
        rigging_display_layout.addWidget(self.rigging_joint_xray_btn)
        rigging_layout.addWidget(self.rigging_import_group)
        rigging_layout.addWidget(self.rigging_select_group)
        rigging_layout.addWidget(self.rigging_setup_group)
        setup_layout = QtWidgets.QVBoxLayout(self.rigging_setup_group)
        setup_layout.addWidget(self.rigging_advanced_skeleton_btn)
        tabs_layout.addTab(rigging_tab, "Rigging")

        # Animation Layout
        animation_tab = QtWidgets.QWidget()
        animation_layout = QtWidgets.QVBoxLayout(animation_tab)
        animation_layout.addWidget(self.animation_display_group)
        animation_display_layout = QtWidgets.QVBoxLayout(self.animation_display_group)
        animation_display_layout.addWidget(self.animation_xray_btn)
        animation_display_layout.addWidget(self.animation_joint_xray_btn)
        animation_layout.addWidget(self.animation_import_group)
        animation_layout.addWidget(self.animation_select_group)
        animation_layout.addWidget(self.animation_key_group)
        animation_layout.addWidget(self.animation_pose_group)
        animation_layout.addWidget(self.animation_blendshape_group)
        tabs_layout.addTab(animation_tab, "Animation")

    def create_connections(self):
        # Help button connection
        self.help_btn.clicked.connect(self.show_help)
        # Switch language button connection
        self.switch_language_btn.clicked.connect(self.toggle_language)
        # Modeling tab connections
        self.modeling_xray_btn.clicked.connect(self.run_xray)
        self.modeling_joint_xray_btn.clicked.connect(self.run_joint_xray)
        self.modeling_rename_btn.clicked.connect(self.run_rename)
        self.modeling_batch_import_btn.clicked.connect(self.run_batch_import)
        self.modeling_interval_select_edge_btn.clicked.connect(self.run_select_edge)
        self.modeling_same_position_selector_btn.clicked.connect(self.run_same_position_selector)
        self.modeling_edge_loop_smart_select_btn.clicked.connect(self.run_edge_loop_smart_select)
        self.modeling_even_edge_loop_btn.clicked.connect(self.run_even_edge_loop)
        self.modeling_crease_plus_btn.clicked.connect(self.run_crease_plus)
        self.modeling_speed_cut_btn.clicked.connect(self.run_speed_cut)
        self.modeling_modit_btn.clicked.connect(self.run_modit)
        self.modeling_plugit_btn.clicked.connect(self.run_plugit)
        self.modeling_zirail_btn.clicked.connect(self.run_zirail)
        self.modeling_xgtools_btn.clicked.connect(self.run_xgtools)
        self.modeling_gs_curve_tools_btn.clicked.connect(self.run_gs_curve_tools)
        self.modeling_reset_gs_curve_tools_btn.clicked.connect(self.reset_gs_curve_tools)
        self.modeling_close_gs_curve_tools_btn.clicked.connect(self.stop_gs_curve_tools)
        self.modeling_edge_sensei_btn.clicked.connect(self.run_edge_sensei)
        self.modeling_round_inset_btn.clicked.connect(self.run_round_inset)
        self.modeling_arc_deformer_btn.clicked.connect(self.run_arc_deformer)
        self.modeling_instant_drag_btn.clicked.connect(self.run_instant_drag)
        self.modeling_unbevel_btn.clicked.connect(self.run_unbevel)
        self.modeling_align_edge_btn.clicked.connect(self.run_align_edge)
        self.modeling_extra_curve_btn.clicked.connect(self.run_extra_curve)
        self.modeling_uv_set_editor_btn.clicked.connect(self.run_uv_set_editor)
        self.modeling_uvdeluxe_btn.clicked.connect(self.run_uvdeluxe)
        self.modeling_rizom_uv_bridge_btn.clicked.connect(self.run_rizom_uv_bridge)
        # Metahuman tab connections
        self.metahuman_xray_btn.clicked.connect(self.run_xray)
        self.metahuman_joint_xray_btn.clicked.connect(self.run_joint_xray)
        self.metahuman_body_prepare_btn.clicked.connect(self.run_body_prepare)
        # Rigging tab connections
        self.rigging_xray_btn.clicked.connect(self.run_xray)
        self.rigging_joint_xray_btn.clicked.connect(self.run_joint_xray)
        self.rigging_advanced_skeleton_btn.clicked.connect(self.run_advanced_skeleton)
        # Animation tab connections
        self.animation_xray_btn.clicked.connect(self.run_xray)
        self.animation_joint_xray_btn.clicked.connect(self.run_joint_xray)

#========================================================================== FUNCTIONS ==========================================================================
    # Initialization
    def show_help(self):
        webbrowser.open(TOOLBOX_HELP)

    def toggle_language(self):
        self.current_language = "en_US" if self.current_language == "zh_CN" else "zh_CN"
        self.switch_language_btn.setText(self.current_language)
    
    # Modeling Functions
    # ****************************************************************************************************************
    # Display
    def run_xray(self, *args):
        try:
            result = cmds.modelEditor('modelPanel4', q=True, xr=True)
            cmds.modelEditor('modelPanel4', e=True, xr=not result)
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Xray: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK') 
    
    def run_joint_xray(self, *args):
        try:
            result = cmds.modelEditor('modelPanel4', q=True, jx=True)
            cmds.modelEditor('modelPanel4', e=True, jx=not result)
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running XrayJoint: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK') 

    # Manage
    def run_rename(self, *args):
        try:
            Rename_Path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Manage', 'Rename.py')).replace('\\', '/')
            sys.path.append(Rename_Path)
            Rename.UI()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Rename: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_batch_import(self, *args):
        try:
            BatchImport.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Batch Import: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    # Edit
    def run_crease_plus(self, *args):
        try:
            crease_plus_dir = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'CreasePlus')).replace('\\', '/')
            print(f"CreasePlus directory: {crease_plus_dir}")
            if crease_plus_dir not in sys.path:
                sys.path.append(crease_plus_dir)
            from Modeling.Edit.CreasePlus import CreasePlusMain
            CreasePlusMain.start()
            print("CreasePlus loaded successfully")
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Crease Plus: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def run_speed_cut(self, *args):
        try:
            SpeedCut.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Speed Cut: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_gs_curve_tools(self, *args):
        try:
            gs_curvetools_path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'gs_curvetools')).replace('\\', '/')
            if gs_curvetools_path not in sys.path:
                sys.path.insert(0, gs_curvetools_path)

            from Modeling.Edit.gs_curvetools import main as ct_main
            # Run the main function
            ct_main.main()

        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running GS Curve Tools: {str(e)}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def stop_gs_curve_tools(self, *args):
        try:
            gs_curvetools_path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'gs_curvetools')).replace('\\', '/')
            if gs_curvetools_path not in sys.path:
                sys.path.insert(0, gs_curvetools_path)

            from Modeling.Edit.gs_curvetools.utils import utils as ct_ut
            # Run the main function
            ct_ut.stopUI()

        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running GS Curve Tools: {str(e)}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def reset_gs_curve_tools(self, *args):
        try:
            gs_curvetools_path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'gs_curvetools')).replace('\\', '/')
            if gs_curvetools_path not in sys.path:
                sys.path.insert(0, gs_curvetools_path)

            from Modeling.Edit.gs_curvetools.utils import utils as ct_ut

            ct_ut.resetOptionVars()

            def __getMayaOS():
                """Get Maya version and parent OS"""
                maya = str(cmds.about(api=1))[:4]
                os = str(cmds.about(os=1))
                return [int(maya), os]
            logger = ct_ut.Logger()
            MAYA_VER = __getMayaOS()[0]
            LOGGER = logger.logger
            if MAYA_VER >= 2018:
                ct_ut.stopUI(True)
            
            # Reload all files
            gs_curvetools_subpaths = [
                os.path.join(gs_curvetools_path, 'constants').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'core').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'main').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'ui').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'uv_editor').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils', 'gs_math').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils', 'style').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils', 'tooltips').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils', 'utils').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils', 'wrap').replace('\\', '/')
            ]
            for subpath in gs_curvetools_subpaths:
                if subpath not in sys.path:
                    sys.path.insert(0, subpath)
            from Modeling.Edit.gs_curvetools import main as ct_main
            # Run the main function
            ct_main.main()

        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running GS Curve Tools: {str(e)}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")


    def run_modit(self, *args):
        try:
            modit_path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'ModIt')).replace('\\', '/')
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
            ERROR_MESSAGE = f"Error occurred while running ModIt: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_plugit(self, *args):
        try:
            PlugIt_Path = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'PlugIt')).replace('\\', '/')

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
            ERROR_MESSAGE = f"Error occurred while running PlugIt: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_xgtools(self, *args):
        try:
            import maya.cmds as cmds
            print("Successfully imported maya.cmds")
            
            import sys
            import os
            import traceback
            XGTC_PARENT_PATH = os.path.join(METABOX_PATH, 'Modeling', 'Edit')
            if XGTC_PARENT_PATH not in sys.path:
                sys.path.insert(0, XGTC_PARENT_PATH)

            xgtc_path = os.path.join(XGTC_PARENT_PATH, 'xgtc').replace('\\', '/')
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
            ERROR_MESSAGE = f"Error importing modules for XGTools: {str(e)}"
            print(ERROR_MESSAGE)
            cmds.warning(ERROR_MESSAGE)
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running XGTools: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK') 
    
    def run_zirail(self, *args):
        try:
            # Get Maya version
            MAYA_VERSION = cmds.about(version=True).split()[0]
            # If Maya version is 2018~2020，set ziRail path to Scripts\Modeling\Edit\ziRail\2018_2020 and ziRail plugin path to Scripts\Modeling\Edit\ziRail\2018_2020\plug-ins
            # if Maya version is 2022~2023, set ziRail path to Scripts\Modeling\Edit\ziRail\2022_2023 and ziRail plugin path to Scripts\Modeling\Edit\ziRail\2022_2023\plug-ins
            # Else, print the error message
            if MAYA_VERSION == '2018' or MAYA_VERSION == '2019' or MAYA_VERSION == '2020':
                ZIRAIL_PATH = os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'ziRail', '2018_2020').replace('\\', '/')
                ZIRAIL_PLUGIN_PATH = os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'ziRail', '2018_2020', 'plug-ins').replace('\\', '/')
                for plugin in [f'ziRail_{MAYA_VERSION}.mll', f'ziWireframeViewport_{MAYA_VERSION}.mll']:
                    plugin_path = os.path.join(ZIRAIL_PLUGIN_PATH, plugin)
                    if os.path.exists(plugin_path):
                        if not cmds.pluginInfo(plugin_path, query=True, loaded=True):
                            cmds.loadPlugin(plugin_path)
                    else:
                        print(f"Warning: Plugin file does not exist: {plugin_path}")

            elif MAYA_VERSION == '2022' or MAYA_VERSION == '2023':
                ZIRAIL_PATH = os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'ziRail', '2022_2023').replace('\\', '/')
                ZIRAIL_PLUGIN_PATH = os.path.join(METABOX_PATH, 'Modeling', 'Edit', 'ziRail', '2022_2023', 'plug-ins').replace('\\', '/')
                for plugin in [f'ziRail_{MAYA_VERSION}.mll', f'ziWireframeViewport_{MAYA_VERSION}.mll']:
                    plugin_path = os.path.join(ZIRAIL_PLUGIN_PATH, plugin)
                    if os.path.exists(plugin_path):
                        if not cmds.pluginInfo(plugin_path, query=True, loaded=True):
                            cmds.loadPlugin(plugin_path)
                    else:
                        print(f"Warning: Plugin file does not exist: {plugin_path}")
                if os.path.exists(ZIRAIL_PLUGIN_PATH):
                    os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join([os.environ.get('MAYA_PLUG_IN_PATH', ''), ZIRAIL_PLUGIN_PATH])
            else:
                ERROR_MESSAGE = f"Error occurred while running ziRail: Maya version {MAYA_VERSION} is not supported"
                cmds.warning(ERROR_MESSAGE)
                cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
                return
            
            # Check if ZIRAIL_PATH exists before adding to sys.path
            if os.path.exists(ZIRAIL_PATH) and ZIRAIL_PATH not in sys.path:
                sys.path.insert(0, ZIRAIL_PATH)

            # Import and run the appropriate ziRail module
            if MAYA_VERSION in ['2018', '2019', '2020']:
                zi_rail = importlib.import_module(f'Modeling.Edit.ziRail.2018_2020.zi_rail')
            elif MAYA_VERSION in ['2022', '2023']:
                zi_rail = importlib.import_module(f'Modeling.Edit.ziRail.2022_2023.zi_rail')
            else:
                ERROR_MESSAGE = f"Error occurred while running ziRail: Maya version {MAYA_VERSION} is not supported"
                cmds.warning(ERROR_MESSAGE)
                cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
                return
            importlib.reload(zi_rail)

            zi_rail.main()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running ziRail: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')


    def run_edge_sensei(self, *args):
        try:
            EdgeSensei.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Edge Sensei: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_even_edge_loop(self, *args):
        try:
            EvenEdgeLoop.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Even Edge Loop: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK') 

    def run_speed_bend(self, *args):
        try:
            SpeedBend.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Speed Bend: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_poly_fold(self, *args):
        try:
            PolyFold.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Poly Fold: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_round_inset(self, *args):
        try:
            RoundInset.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Round Inset: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_arc_deformer(self, *args):
        try:
            ArcDeformer.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Arc Deformer: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_instant_drag(self, *args):
        try:
            InstantDrag.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Instant Drag: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_unbevel(self, *args):
        try:
            UnBevel.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running UnBevel: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_extra_curve(self, *args):
        try:
            mel.eval('polyToCurve -form 2 -degree 3 -conformToSmoothMeshPreview 1')
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running ExtractCurve: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    # Select
    def run_edge_loop_smart_select(self, *args):
        try:
            EdgeLoopSmartSelect.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Edge Loop Smart Select: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_select_edge(self, *args):
        try:
            IntervalSelectEdge.show()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Interval Select Edge: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_same_position_selector(self, *args):
        try:
            SamePositionSelector.show()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running SamePositionSelector: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_align_edge(self, *args):
        try:
            AlignEdge.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Align Edge: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    # UV
    def run_uv_set_editor(self, *args):
        try:
            UVSetEditor.show()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while opening UV Set Editor: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_uvdeluxe(self, *args):
        try:
            from Modeling.UV.UVDeluxe import uvdeluxe
            uvdeluxe.createUI()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while opening UVDeluxe: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_rizom_uv_bridge(self, *args):
        try:
            RIZOMUV_PATH = os.path.normpath(os.path.join(METABOX_PATH, 'Modeling', 'UV', 'RizomUVBridge')).replace('\\', '/')
            if RIZOMUV_PATH not in sys.path:
                sys.path.insert(0, RIZOMUV_PATH)
            RIZOMUV_LUA_PATH = os.path.join(RIZOMUV_PATH, 'RizomUVBridge.lua').replace('\\', '/')
            if RIZOMUV_LUA_PATH not in sys.path:
                sys.path.insert(0, RIZOMUV_LUA_PATH)
            from Modeling.UV.RizomBridge import RizomUVBridge
            RizomUVBridge.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running RizomUV Bridge: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Rigging Functions
    # ****************************************************************************************************************
    def run_advanced_skeleton(self, *args):
        try:
            adv_sub_path = [
                os.path.join(METABOX_PATH, 'Animation', 'AdvancedSkeleton').replace('\\', '/'),
                os.path.join(METABOX_PATH, 'Animation', 'AdvancedSkeleton', 'AdvancedSkeleton5Files').replace('\\', '/')
            ]
            for path in adv_sub_path:
                if path not in sys.path:
                    sys.path.insert(0, path)
            # If advancedSkeleton5Files does not exist, run the adv_install.py and the launch.py, else run the adv_launch.py directly
            if not os.path.exists(os.path.join(METABOX_PATH, 'Animation', 'AdvancedSkeleton', 'adv_install.py').replace('\\', '/')):
                from Animation.AdvancedSkeleton import adv_install
                adv_install.install()
            from Animation.AdvancedSkeleton import adv_launch
            adv_launch.launch()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Advanced Skeleton: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Metahuman Functions
    # ****************************************************************************************************************
    # Preparation
    def run_body_prepare(self, *args):
        try:
            BodyPrep.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Body Prepare: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Animation Functions
    # ****************************************************************************************************************
    # Pose
    def open_aTools(self, *args):
        try:
            # Get aTools path
            ATOOLS_PATH = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'aTools')).replace('\\', '/')
            if ATOOLS_PATH not in sys.path:
                sys.path.insert(0, ATOOLS_PATH)
            ATOOLS_PARENT_PATH = os.path.dirname(ATOOLS_PATH)
            if ATOOLS_PARENT_PATH not in sys.path:
                sys.path.insert(0, ATOOLS_PARENT_PATH)
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
            ERROR_MESSAGE = f"Error occurred while running aTools: {e}"
            print(f"Detailed error: {traceback.format_exc()}")
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def open_keyframe_pro(self, *args):
        try:
            KEYFRAME_PRO_PATH = [
                os.path.join(METABOX_PATH, 'Animation', 'keyframe_pro'),
                os.path.join(METABOX_PATH, 'Animation', 'keyframe_pro', 'keyframe_pro'),
                os.path.join(METABOX_PATH, 'Animation', 'keyframe_pro', 'keyframe_pro_maya')
            ]
            for path in KEYFRAME_PRO_PATH:
                if path not in sys.path:
                    sys.path.insert(0, path)
            for path in sys.path:
                print("Added the keyframe_Pro submoudle path: ", path)
            from Animation.keyframe_pro.keyframe_pro_maya.maya_to_keyframe_pro import MayaToKeyframePro
            MayaToKeyframePro.display()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Keyframe Pro: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def open_studio_library(self, *args):
        try:
            STUDIOLIBRARY_PATH = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'studiolibrary')).replace('\\', '/')
            STUDIOLIBRARY_SUB_PATHS = [
                os.path.join(STUDIOLIBRARY_PATH, 'src'),
                os.path.join(STUDIOLIBRARY_PATH, 'src', 'studiolibrary'),
                os.path.join(STUDIOLIBRARY_PATH, 'src', 'studiolibrarymaya'),
                os.path.join(STUDIOLIBRARY_PATH, 'src', 'studioqt'),
                os.path.join(STUDIOLIBRARY_PATH, 'src', 'mutils'),
                os.path.join(STUDIOLIBRARY_PATH, 'src', 'studiovendor')
            ]
            # Added the main path to sys.path
            if STUDIOLIBRARY_PATH not in sys.path:
                sys.path.insert(0, STUDIOLIBRARY_PATH)
            # Added the sub path to sys.path
            for path in STUDIOLIBRARY_SUB_PATHS:
                if path not in sys.path:
                    sys.path.insert(0, path.replace('\\', '/'))
            for path in sys.path:
                print("Added the studiolibrary submoudle path: ", path)
            # Import studiolibrary from the STUDIOLIBRARY_PATH with importlib
            studiolibrary = importlib.import_module('studiolibrary')
            importlib.reload(studiolibrary)
            # Run studiolibrary
            studiolibrary.main()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Studio Library: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_anim_school_picker(self, *args):
        try:
            # Added the path to the AnimSchoolPicker.mel file
            ANIMPICKER_PATH = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'AnimSchoolPicker')).replace('\\', '/')
            if ANIMPICKER_PATH not in sys.path:
                sys.path.insert(0, ANIMPICKER_PATH)

            # Get Maya Version
            MAYA_VERSION = cmds.about(version=True).split()[0]

            # Set plugin path
            ANIMPICKER_PLUGIN_PATH = os.path.join(ANIMPICKER_PATH, MAYA_VERSION).replace('\\', '/')
            # Added the plugin path to MAYA_PLUG_IN_PATH
            os.environ['MAYA_PLUG_IN_PATH'] = ANIMPICKER_PLUGIN_PATH

            # load the plugin
            animpicker_mll = os.path.join(ANIMPICKER_PLUGIN_PATH, 'AnimSchoolPicker.mll').replace('\\', '/')
            cmds.loadPlugin(animpicker_mll, quiet=True)
            cmds.AnimSchoolPicker()
            print(f"Anim School Picker loaded successfully from {animpicker_mll}")
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Anim School Picker: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
    
    def run_bhghost(self, *args):
        try:
            bhghost_path = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'bhGhost')).replace('\\', '/')
            print(bhghost_path)
            if bhghost_path not in sys.path:
                sys.path.insert(0, bhghost_path)
            bhghost_mel = os.path.join(bhghost_path, 'bhGhost.mel').replace('\\', '/')
            print(bhghost_mel)
            mel.eval(f'source "{bhghost_mel}";')
            print(f"bhGhost loaded successfully from {bhghost_mel}")
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running bhGhost: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
            print(f"Detailed error: {traceback.format_exc()}")

    def run_ik_fk_switch(self, *args):
        try:
            IK_FK_Switch_Path = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'IK_FK_Switch')).replace('\\', '/')
            if IK_FK_Switch_Path not in sys.path:
                sys.path.insert(0, IK_FK_Switch_Path)
            from Animation import IK_FK_Switcher
            IK_FK_Switcher.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running IK/FK Switch: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    # Blendshape
    def open_epic_pose_wrangler(self, *args):
        try:
            # Add Epic Pose Wrangler path
            epic_pose_wrangler_path = os.path.join(METABOX_PATH, 'Animation', 'epic_pose_wrangler').replace('\\', '/')
            sys.path.append(epic_pose_wrangler_path)
            print(epic_pose_wrangler_path)
            print(f"Attempting to import Epic Pose Wrangler from: {epic_pose_wrangler_path}")            
            # Get current Maya version
            MAYA_VERSION = cmds.about(version=True).split()[0]            
            # Load necessary plugins
            plugin_dir = os.path.join(epic_pose_wrangler_path, 'plugins', 'Windows', MAYA_VERSION)
            for plugin in ['embeddedRL4.mll', f'MayaUE4RBFPlugin{MAYA_VERSION}.mll', 'MayaUERBFPlugin.mll']:
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
            ERROR_MESSAGE = f"Error occurred while running Epic Pose Wrangler: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    def run_universal_rig_adapter(self, *args):
        try:
            UniversalRigAdapter.run()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Universal Rig Adapter: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
    
    def run_morph_shape(self, *args):
        try:
            MorphShape.show()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running MorphShape: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show():
    """
    Display the HUG Tools main window
    
    This function will close the existing window (if any) and then create and display a new window.
    Use the global variable main_window to keep a reference to the window instance.
    """
    global main_window
    try:
        # Try to close the existing window
        main_window.close()
        main_window.deleteLater()
    except:
        # If the window does not exist, ignore the error
        pass
    
    # Create a new window instance and display it
    main_window = MetaBox()
    main_window.show()


if __name__ == "__main__":
    show()