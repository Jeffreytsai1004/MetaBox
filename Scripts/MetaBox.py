#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=====================================IMPORT=====================================
from PySide2 import QtWidgets, QtCore, QtGui
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
import maya.cmds as cmds # type: ignore
import maya.mel as mel # type: ignore
import maya.utils as utils # type: ignore
import importlib
import traceback
import subprocess
import webbrowser
import locale
import sys
import os

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
from Animation.Blendshape import MorphShape
from Animation import UniversalRigAdapter
from Dev import mayaiconview
#=====================================VARIABLES=====================================
METABOX_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
sys.path.append(METABOX_PATH)

TOOLBOX_NAME = "MetaBox"

TOOLBOX_VERSION = "Beta v1.0.0"

TOOLBOX_AUTHOR = "VIRTUOS"

CURRENT_LANG = 'en_US'

WKSP_CTRL_NAME = "ToolBoxWorkSpaceControl"

TOOLBOX_HELP = f"https://ac.virtuosgames.com:8443/display/TK/{TOOLBOX_NAME}"

TOOLBOX_ICON = os.path.join(METABOX_PATH, "Icons", "MetaBox.png").replace('\\', '/')

#=====================================UI BUTTONS COMPONENTS=====================================
class RoundedButton(QtWidgets.QPushButton):
    """
    Custom rounded button class

    Features:
    - Rounded design
    - Custom color and hover effect
    - Bold text
    """
    def __init__(self, text="", icon=None, color="#D0D0D0", hover_color="#E0E0E0", pressed_color="#C0C0C0"):
        super(RoundedButton, self).__init__(text)
        if icon:
            self.setIcon(icon)
            self.setIconSize(QtCore.QSize(24, 24))
        self.setMinimumHeight(30) # Set minimum height
        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {color}; 
                color: #303030; 
                border-radius: 10px; 
                padding: 5px;
                font-weight: bold;
                text-align: center;
            }}
            QPushButton:hover {{
                background-color: {hover_color}; 
            }}
            QPushButton:pressed {{
                background-color: {pressed_color}; 
            }}
            """
        )

#=====================================GLOBAL FUNCTIONS=====================================

def get_system_encoding():
    encoding = sys.getdefaultencoding()
    if encoding.lower() == 'ascii':
        encoding = locale.getpreferredencoding()
    return encoding

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

LANG = {
    'en_US': {
        "DOCUMENT": "DOCUMENT",
        "Help": "Help",
        "EN": "EN",
        "ZH": "ZH",
        "zh_CN": "zh_CN",
        "Switch Language": "Switch Language",
        "Modeling": "Modeling",
        "Metahuman": "Metahuman",
        "Rigging": "Rigging",
        "Animation": "Animation",
        "Display": "Display",
        "Xray": "Xray",
        "Joint Xray": "Joint Xray",
        "Manage": "Manage",
        "Rename": "Rename",
        "Batch Import": "Batch Import",
        "Select": "Select",
        "Interval Select Edge": "Interval Select Edge",
        "Same Position Selector": "Same Position Selector",
        "Edge Loop Smart Select": "Edge Loop Smart Select",
        "Even Edge Loop": "Even Edge Loop",
        "Tools": "Tools",
        "Crease Plus": "Crease Plus",
        "Speed Cut": "Speed Cut",
        "ModIt": "ModIt",
        "PlugIt": "PlugIt",
        "Zirail": "Zirail",
        "Groomer`s Tool": "Groomer`s Tool",
        "Edge Sensei": "Edge Sensei",
        "Round Inset": "Round Inset",
        "Arc Deformer": "Arc Deformer", 
        "Instant Drag": "Instant Drag",
        "Un Bevel": "Un Bevel",
        "Align Edge": "Align Edge",
        "Extra Curve": "Extra Curve",
        "Speed Bend": "Speed Bend",
        "GS Curve Tools": "GS Curve Tools",
        "GS Curve Tools Reset": "GS Curve Tools Reset", 
        "GS Curve Tools Close": "GS Curve Tools Close",
        "UV": "UV",
        "UVDeluxe": "UVDeluxe",
        "RizomUV Bridge": "RizomUV Bridge",
        "UV Set Editor": "UV Set Editor",
        "Preparation": "Preparation",   
        "Body Prepare": "Body Prepare",
        "Setup": "Setup",
        "Advanced Skeleton": "Advanced Skeleton",
        "Select": "Select",
        "Anim School Picker": "Anim School Picker",
        "DWPicker": "DWPicker",
        "Tools": "Tools",
        "bhGhost": "bhGhost",   
        "IK/FK Switch": "IK/FK Switch",
        "aTools": "aTools",
        "Keyframe Pro": "Keyframe Pro",
        "Studio Library": "Studio Library",
        "Pose Tools": "Pose Tools",
        "Epic Pose Wrangler": "Epic Pose Wrangler",
        "Morph Shape": "Morph Shape",
        "Universal Rig Adapter": "Universal Rig Adapter",
        "Dev": "Dev",
        "Dev Tool": "Dev Tool",
        "Icon Viewer": "Icon Viewer"
    },
    'zh_CN': {
        "DOCUMENT": "说明文档",
        "Help": "帮助",
        "EN": "EN",
        "ZH": "ZH",
        "zh_CN": "zh_CN",
        "Switch Language": "切换语言",
        "Modeling": "建模",
        "Metahuman": "Metahuman",
        "Rigging": "绑定",
        "Animation": "动画",
        "Display": "显示",
        "Xray": "X光显示",
        "Joint Xray": "关节X光显示",
        "Manage": "管理",
        "Rename": "重命名",
        "Batch Import": "批量导入",
        "Select": "选择",
        "Interval Select Edge": "间隔选择边",
        "Same Position Selector": "相同位置物体选择器",
        "Edge Loop Smart Select": "边缘循环智能选择",
        "Even Edge Loop": "等边循环",
        "Tools": "工具",
        "Crease Plus": "Crease ++",
        "Speed Cut": "快速切割",
        "ModIt": "ModIt",
        "PlugIt": "PlugIt",
        "Zirail": "Zirail 拓扑工具",
        "Groomer`s Tool": "Groomer 工具",
        "Edge Sensei": "边线大师",
        "Round Inset": "圆角插入",
        "Arc Deformer": "弧形变形器", 
        "Instant Drag": "吸附放置",
        "Un Bevel": "去除倒角",
        "Align Edge": "对齐到边",
        "Extra Curve": "提取曲线",
        "Speed Bend": "快速弯曲",
        "GS Curve Tools": "GS曲线工具",
        "GS Curve Tools Reset": "重置", 
        "GS Curve Tools Close": "关闭",
        "UV": "UV",
        "UVDeluxe": "UVDeluxe",
        "RizomUV Bridge": "RizomUV Bridge",
        "UV Set Editor": "UV 编辑器",
        "Preparation": "准备",   
        "Body Prepare": "身体准备",
        "Setup": "设置",
        "Advanced Skeleton": "高级骨骼",
        "Select": "选择",
        "Anim School Picker": "Anim School 拾取器",
        "DWPicker": "DW 拾取器",
        "Tools": "工具",
        "bhGhost": "洋葱皮",   
        "IK/FK Switch": "IK/FK 切换",
        "aTools": "aTools",
        "Keyframe Pro": "关键帧大师",
        "Studio Library": "工作室库",
        "Pose Tools": "姿势工具",
        "Epic Pose Wrangler": "Epic 姿势变形器",
        "Morph Shape": "变形工具",
        "Universal Rig Adapter": "通用绑定适配器",
        "Dev": "开发",
        "Dev Tool": "开发工具",
        "Icon Viewer": "图标查看器"
    }
}
#=====================================UI MAIN WINDOW COMPONENTS=====================================
class MetaBox(QtWidgets.QWidget):
    def __init__(self, parent=maya_main_window()):
        super(MetaBox, self).__init__(parent)
        self.setWindowTitle(TOOLBOX_NAME)
        self.setObjectName('MetaBoxWindow')
        self.setWindowFlags(QtCore.Qt.Window)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #Main UI components
        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        #Set window icon
        if os.path.exists(TOOLBOX_ICON):
            self.setWindowIcon(QtGui.QIcon(TOOLBOX_ICON))
        else:
            print(f"WARNING: Icon file not found: {TOOLBOX_ICON}")

    #Dock to Maya
    def dock_to_maya(self):
        if cmds.workspaceControl(WKSP_CTRL_NAME, exists=True):
            cmds.deleteUI(WKSP_CTRL_NAME)
        def create_control():
            try:
                workspace_control = cmds.workspaceControl(
                    WKSP_CTRL_NAME,
                    label="MetaBox",
                    floating=True,
                    retain=True,
                    uiScript="from MetaBox import MetaBox; MetaBox()"
                )
                cmds.control(self.objectName(), e=True, p=workspace_control, width=300)
            except Exception as e:
                print(f"Error creating workspace control: {e}")
        cmds.evalDeferred(create_control)
#===================================== UI COMPONENTS =====================================
    def create_widgets(self):
        # Create help button
        self.help_btn = QtWidgets.QPushButton(LANG[CURRENT_LANG]["DOCUMENT"])
        self.help_btn.setToolTip(LANG[CURRENT_LANG]["Help"])
        self.help_btn.setFixedSize(100, 20)
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
        self.lang_btn = QtWidgets.QPushButton("EN" if CURRENT_LANG == 'zh_CN' else "ZH")
        self.lang_btn.setToolTip(LANG[CURRENT_LANG]["Switch Language"])
        self.lang_btn.setFixedSize(30, 20)
        self.lang_btn.setStyleSheet("""
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
        self.modeling_tab_btn = RoundedButton(LANG[CURRENT_LANG]["Modeling"])
        self.metahuman_tab_btn = RoundedButton(LANG[CURRENT_LANG]["Metahuman"])
        self.rigging_tab_btn = RoundedButton(LANG[CURRENT_LANG]["Rigging"])
        self.animation_tab_btn = RoundedButton(LANG[CURRENT_LANG]["Animation"])
        self.dev_tab_btn = RoundedButton(LANG[CURRENT_LANG]["Dev"])

        # Modeling group widgets
        self.modeling_display_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Display"] )
        self.modeling_xray_btn = RoundedButton(LANG[CURRENT_LANG]["Xray"], color="#FFB3BA", hover_color="#FF9DAF", pressed_color="#FF6F61")
        self.modeling_joint_xray_btn = RoundedButton(LANG[CURRENT_LANG]["Joint Xray"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")
        self.modeling_manage_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Manage"])
        self.modeling_rename_btn = RoundedButton(LANG[CURRENT_LANG]["Rename"], color="#A4D7E1", hover_color="#A0D8D0", pressed_color="#8CC8C5")
        self.modeling_batch_import_btn = RoundedButton(LANG[CURRENT_LANG]["Batch Import"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        self.modeling_select_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Select"])
        self.modeling_interval_select_edge_btn = RoundedButton(LANG[CURRENT_LANG]["Interval Select Edge"], color="#FFEBA1", hover_color="#FFF5B3", pressed_color="#FFE68A")
        self.modeling_same_position_selector_btn = RoundedButton(LANG[CURRENT_LANG]["Same Position Selector"], color="#FFABAB", hover_color="#FFC3C3", pressed_color="#FF8C8C")
        self.modeling_edge_loop_smart_select_btn = RoundedButton(LANG[CURRENT_LANG]["Edge Loop Smart Select"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        self.modeling_even_edge_loop_btn = RoundedButton(LANG[CURRENT_LANG]["Even Edge Loop"], color="#FF8C94", hover_color="#FFB3B8", pressed_color="#FF6F7D")
        self.modeling_tools_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Tools"])
        self.modeling_crease_plus_btn = RoundedButton(LANG[CURRENT_LANG]["Crease Plus"], color="#FFB74D", hover_color="#FFD54F", pressed_color="#FFA726")
        self.modeling_speed_cut_btn = RoundedButton(LANG[CURRENT_LANG]["Speed Cut"], color="#FFEBA1", hover_color="#FFF5B3", pressed_color="#FFE68A")
        self.modeling_modit_btn = RoundedButton(LANG[CURRENT_LANG]["ModIt"], color="#A4D7E1", hover_color="#A0D8D0", pressed_color="#8CC8C5")
        self.modeling_plugit_btn = RoundedButton(LANG[CURRENT_LANG]["PlugIt"], color="#B39DDB", hover_color="#D1C4E9", pressed_color="#9575CD")
        self.modeling_zirail_btn = RoundedButton(LANG[CURRENT_LANG]["Zirail"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        self.modeling_xgtools_btn = RoundedButton(LANG[CURRENT_LANG]["Groomer`s Tool"], color="#FFAB40", hover_color="#FFB74D", pressed_color="#FF8F00")
        self.modeling_edge_sensei_btn = RoundedButton(LANG[CURRENT_LANG]["Edge Sensei"], color="#B2E0B2", hover_color="#C6E6C6", pressed_color="#99D699")
        self.modeling_round_inset_btn = RoundedButton(LANG[CURRENT_LANG]["Round Inset"], color="#FF8C94", hover_color="#FFB3B8", pressed_color="#FF6F7D")
        self.modeling_arc_deformer_btn = RoundedButton(LANG[CURRENT_LANG]["Arc Deformer"], color="#E1BEE7", hover_color="#EAB8E4", pressed_color="#D81B60")
        self.modeling_speed_bend_btn = RoundedButton(LANG[CURRENT_LANG]["Speed Bend"], color="#FFABAB", hover_color="#FF8C8C", pressed_color="#FF6F61")
        self.modeling_instant_drag_btn = RoundedButton(LANG[CURRENT_LANG]["Instant Drag"], color="#BBDEFB", hover_color="#90CAF9", pressed_color="#64B5F6")
        self.modeling_unbevel_btn = RoundedButton(LANG[CURRENT_LANG]["Un Bevel"], color="#C8E6C9", hover_color="#A5D6A7", pressed_color="#81C784")
        self.modeling_align_edge_btn = RoundedButton(LANG[CURRENT_LANG]["Align Edge"], color="#FFCCBC", hover_color="#FFAB91", pressed_color="#FF8A65")
        self.modeling_extra_curve_btn = RoundedButton(LANG[CURRENT_LANG]["Extra Curve"], color="#E1BEE7", hover_color="#D1C4E9", pressed_color="#BA68C8")
        self.modeling_gs_curve_tools_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["GS Curve Tools"])
        self.modeling_gs_curve_tools_btn = RoundedButton(LANG[CURRENT_LANG]["GS Curve Tools"], color="#C8E6C9", hover_color="#A5D6A7", pressed_color="#81C784")
        self.modeling_reset_gs_curve_tools_btn = RoundedButton(LANG[CURRENT_LANG]["GS Curve Tools Reset"], color="#FFEBA1", hover_color="#FFF5B3", pressed_color="#FFE68A")
        self.modeling_close_gs_curve_tools_btn = RoundedButton(LANG[CURRENT_LANG]["GS Curve Tools Close"], color="#FFCCBC", hover_color="#FFAB91", pressed_color="#FF8A65")
        self.modeling_uv_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["UV"]) 
        self.modeling_uvdeluxe_btn = RoundedButton(LANG[CURRENT_LANG]["UVDeluxe"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        self.modeling_rizom_uv_bridge_btn = RoundedButton(LANG[CURRENT_LANG]["RizomUV Bridge"], color="#FFABAB", hover_color="#FFC3C3", pressed_color="#FF8C8C")
        self.modeling_uv_set_editor_btn = RoundedButton(LANG[CURRENT_LANG]["UV Set Editor"], color="#FFEBA1", hover_color="#FFF5B3", pressed_color="#FFE68A")

        # Metahuman group widgets
        self.metahuman_preparation_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Preparation"])
        self.metahuman_body_prepare_btn = RoundedButton(LANG[CURRENT_LANG]["Body Prepare"], color="#FFABAB", hover_color="#FF6F6F", pressed_color="#FF8C8C")

        # Rigging group widgets
        self.rigging_setup_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Setup"])
        self.rigging_advanced_skeleton_btn = RoundedButton(LANG[CURRENT_LANG]["Advanced Skeleton"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")

        # Animation group widgets
        self.animation_select_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Select"])
        self.animation_animschool_picker_btn = RoundedButton(LANG[CURRENT_LANG]["Anim School Picker"], color="#FFB3BA", hover_color="#FF9DAF", pressed_color="#FF8C94")
        self.animation_dwpicker_btn = RoundedButton(LANG[CURRENT_LANG]["DWPicker"], color="#A0D8D0", hover_color="#8CC8C5", pressed_color="#7FBFBF")
        self.animation_tools_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Tools"])
        self.animation_bhghost_btn = RoundedButton(LANG[CURRENT_LANG]["bhGhost"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")
        self.animation_ikfk_switch_btn = RoundedButton(LANG[CURRENT_LANG]["IK/FK Switch"], color="#B2E1D4", hover_color="#A0D8D0", pressed_color="#8CC8C5")
        self.animation_atools_btn = RoundedButton(LANG[CURRENT_LANG]["aTools"], color="#FFB3BA", hover_color="#FF9DAF", pressed_color="#FF8C94")
        self.animation_keyframepro_btn = RoundedButton(LANG[CURRENT_LANG]["Keyframe Pro"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")
        self.animation_studiolibrary_btn = RoundedButton(LANG[CURRENT_LANG]["Studio Library"], color="#A0D8D0", hover_color="#8CC8C5", pressed_color="#7FBFBF")
        self.animation_pose_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Pose Tools"])
        self.animation_epic_pose_wrangler_btn = RoundedButton(LANG[CURRENT_LANG]["Epic Pose Wrangler"], color="#FFB3BA", hover_color="#FF9DAF", pressed_color="#FF8C94")
        self.animation_morph_shape_btn = RoundedButton(LANG[CURRENT_LANG]["Morph Shape"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")
        self.animation_universal_rig_adapter_btn = RoundedButton(LANG[CURRENT_LANG]["Universal Rig Adapter"], color="#A0D8D0", hover_color="#8CC8C5", pressed_color="#7FBFBF")

        # Dev group widgets
        self.dev_tools_group = QtWidgets.QGroupBox(LANG[CURRENT_LANG]["Dev Tool"])
        self.dev_icon_viewer_btn = RoundedButton(LANG[CURRENT_LANG]["Icon Viewer"], color="#FFDAA5", hover_color="#FFC78C", pressed_color="#FFC0A1")

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        # Resizable by dragging
        main_layout.setStretch(0, 1)

        # Tabs Layout
        tabs_layout = QtWidgets.QTabWidget(self)

        main_layout.addWidget(tabs_layout)

        #===================================MODELING TAB===================================
        modeling_tab = QtWidgets.QWidget()
        modeling_layout = QtWidgets.QHBoxLayout(modeling_tab)  # Use a horizontal layout
        # Scroll area
        modeling_scroll_area = QtWidgets.QScrollArea()
        modeling_scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        modeling_scroll_area_content = QtWidgets.QWidget()  # Create a content widget
        modeling_scroll_area_layout = QtWidgets.QVBoxLayout(modeling_scroll_area_content)  # Create a vertical layout
        modeling_scroll_area.setWidget(modeling_scroll_area_content)  # Set the content widget as the scroll area's widget
        # Add all buttons and groups to the scroll area
        # Display
        modeling_scroll_area_layout.addWidget(self.modeling_display_group)
        modeling_display_layout = QtWidgets.QGridLayout(self.modeling_display_group)
        modeling_display_layout.addWidget(self.modeling_xray_btn, 0, 0)
        modeling_display_layout.addWidget(self.modeling_joint_xray_btn, 0, 1)
        # Manage
        modeling_scroll_area_layout.addWidget(self.modeling_manage_group)
        modeling_manage_layout = QtWidgets.QVBoxLayout(self.modeling_manage_group)
        modeling_manage_layout.addWidget(self.modeling_rename_btn)
        modeling_manage_layout.addWidget(self.modeling_batch_import_btn)
        # Select
        modeling_scroll_area_layout.addWidget(self.modeling_select_group)
        modeling_select_layout = QtWidgets.QVBoxLayout(self.modeling_select_group)
        modeling_select_layout.addWidget(self.modeling_interval_select_edge_btn)
        modeling_select_layout.addWidget(self.modeling_same_position_selector_btn)
        modeling_select_layout.addWidget(self.modeling_edge_loop_smart_select_btn)
        modeling_select_layout.addWidget(self.modeling_even_edge_loop_btn)
        # Tools
        modeling_scroll_area_layout.addWidget(self.modeling_tools_group)
        modeling_tools_layout = QtWidgets.QGridLayout(self.modeling_tools_group)
        modeling_tools_layout.addWidget(self.modeling_crease_plus_btn, 0, 0)
        modeling_tools_layout.addWidget(self.modeling_speed_cut_btn, 0, 1)
        modeling_tools_layout.addWidget(self.modeling_modit_btn, 1, 0)
        modeling_tools_layout.addWidget(self.modeling_plugit_btn, 1, 1)
        modeling_tools_layout.addWidget(self.modeling_zirail_btn, 2, 0)
        modeling_tools_layout.addWidget(self.modeling_xgtools_btn, 2, 1)
        modeling_tools_layout.addWidget(self.modeling_edge_sensei_btn, 3, 0)
        modeling_tools_layout.addWidget(self.modeling_round_inset_btn, 3, 1)
        modeling_tools_layout.addWidget(self.modeling_arc_deformer_btn, 4, 0)
        modeling_tools_layout.addWidget(self.modeling_speed_bend_btn, 4, 1)
        modeling_tools_layout.addWidget(self.modeling_instant_drag_btn, 5, 0)
        modeling_tools_layout.addWidget(self.modeling_unbevel_btn, 5, 1)
        modeling_tools_layout.addWidget(self.modeling_align_edge_btn, 6, 0)
        modeling_tools_layout.addWidget(self.modeling_extra_curve_btn, 6, 1)
        # GS Curve Tools
        modeling_scroll_area_layout.addWidget(self.modeling_gs_curve_tools_group)
        modeling_gs_curve_tools_layout = QtWidgets.QVBoxLayout(self.modeling_gs_curve_tools_group)
        modeling_gs_curve_tools_layout.addWidget(self.modeling_gs_curve_tools_btn)
        modeling_gs_curve_tools_layout.addWidget(self.modeling_reset_gs_curve_tools_btn)
        modeling_gs_curve_tools_layout.addWidget(self.modeling_close_gs_curve_tools_btn)
        # UV
        modeling_scroll_area_layout.addWidget(self.modeling_uv_group)
        modeling_uv_layout = QtWidgets.QVBoxLayout(self.modeling_uv_group)
        modeling_uv_layout.addWidget(self.modeling_uv_set_editor_btn)
        modeling_uv_layout.addWidget(self.modeling_uvdeluxe_btn)
        modeling_uv_layout.addWidget(self.modeling_rizom_uv_bridge_btn)
        # Add the scroll area to the main layout
        modeling_layout.addWidget(modeling_scroll_area)  # Add the scroll area to the tab layout
        tabs_layout.addTab(modeling_tab, "Modeling")

        #===================================METAHUMAN TAB===================================
        metahuman_tab = QtWidgets.QWidget()
        metahuman_layout = QtWidgets.QVBoxLayout(metahuman_tab)
        # Scroll area
        metahuman_scroll_area = QtWidgets.QScrollArea()
        metahuman_scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        metahuman_scroll_area_content = QtWidgets.QWidget()  # Create a content widget
        metahuman_scroll_area_layout = QtWidgets.QVBoxLayout(metahuman_scroll_area_content)  # Create a vertical layout
        metahuman_scroll_area.setWidget(metahuman_scroll_area_content)  # Set the content widget as the scroll area's widget
        # Add all buttons and groups to the scroll area
        metahuman_scroll_area_layout.addWidget(self.metahuman_preparation_group)
        metahuman_preparation_layout = QtWidgets.QVBoxLayout(self.metahuman_preparation_group)
        metahuman_preparation_layout.addWidget(self.metahuman_body_prepare_btn)
        # Add the scroll area to the main layout
        metahuman_layout.addWidget(metahuman_scroll_area)  # Add the scroll area to the tab layout
        tabs_layout.addTab(metahuman_tab, "Metahuman")

        #===================================RIGGING TAB===================================
        rigging_tab = QtWidgets.QWidget()
        rigging_layout = QtWidgets.QVBoxLayout(rigging_tab)
        # Scroll area   
        rigging_scroll_area = QtWidgets.QScrollArea()
        rigging_scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        rigging_scroll_area_content = QtWidgets.QWidget()  # Create a content widget
        rigging_scroll_area_layout = QtWidgets.QVBoxLayout(rigging_scroll_area_content)  # Create a vertical layout
        rigging_scroll_area.setWidget(rigging_scroll_area_content)  # Set the content widget as the scroll area's widget
        # Add all buttons and groups to the scroll area
        rigging_scroll_area_layout.addWidget(self.rigging_setup_group)
        rigging_setup_layout = QtWidgets.QVBoxLayout(self.rigging_setup_group)
        rigging_setup_layout.addWidget(self.rigging_advanced_skeleton_btn)
        # Add the scroll area to the main layout
        rigging_layout.addWidget(rigging_scroll_area)  # Add the scroll area to the tab layout
        tabs_layout.addTab(rigging_tab, "Rigging")

        #===================================A   
        animation_tab = QtWidgets.QWidget()
        animation_layout = QtWidgets.QVBoxLayout(animation_tab)
        # Scroll area
        animation_scroll_area = QtWidgets.QScrollArea()
        animation_scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        animation_scroll_area_content = QtWidgets.QWidget()  # Create a content widget
        animation_scroll_area_layout = QtWidgets.QVBoxLayout(animation_scroll_area_content)  # Create a vertical layout
        animation_scroll_area.setWidget(animation_scroll_area_content)  # Set the content widget as the scroll area's widget
        # Add all buttons and groups to the scroll area
        animation_scroll_area_layout.addWidget(self.animation_select_group)
        animation_select_layout = QtWidgets.QVBoxLayout(self.animation_select_group)
        animation_select_layout.addWidget(self.animation_animschool_picker_btn)
        animation_select_layout.addWidget(self.animation_dwpicker_btn)
        animation_scroll_area_layout.addWidget(self.animation_tools_group)
        animation_tools_layout = QtWidgets.QGridLayout(self.animation_tools_group)
        animation_tools_layout.addWidget(self.animation_bhghost_btn, 0, 0)
        animation_tools_layout.addWidget(self.animation_ikfk_switch_btn, 0, 1)
        animation_tools_layout.addWidget(self.animation_atools_btn, 1, 0)
        animation_tools_layout.addWidget(self.animation_keyframepro_btn, 1, 1)
        animation_tools_layout.addWidget(self.animation_studiolibrary_btn, 2, 0)
        animation_scroll_area_layout.addWidget(self.animation_pose_group)
        animation_pose_layout = QtWidgets.QVBoxLayout(self.animation_pose_group)
        animation_pose_layout.addWidget(self.animation_epic_pose_wrangler_btn)
        animation_pose_layout.addWidget(self.animation_morph_shape_btn)
        animation_pose_layout.addWidget(self.animation_universal_rig_adapter_btn)
        # Add the scroll area to the main layout
        animation_layout.addWidget(animation_scroll_area)  # Add the scroll area to the tab layout
        tabs_layout.addTab(animation_tab, "Animation")

        #===================================DEV TAB===================================
        dev_tab = QtWidgets.QWidget()
        dev_layout = QtWidgets.QVBoxLayout(dev_tab)
        # Scroll area
        dev_scroll_area = QtWidgets.QScrollArea()
        dev_scroll_area.setWidgetResizable(True)  # Make the scroll area resizable
        dev_scroll_area_content = QtWidgets.QWidget()  # Create a content widget
        dev_scroll_area_layout = QtWidgets.QVBoxLayout(dev_scroll_area_content)  # Create a vertical layout
        dev_scroll_area.setWidget(dev_scroll_area_content)  # Set the content widget as the scroll area's widget
        # Add all buttons and groups to the scroll area
        dev_scroll_area_layout.addWidget(self.dev_tools_group)
        dev_tools_layout = QtWidgets.QVBoxLayout(self.dev_tools_group)
        dev_tools_layout.addWidget(self.dev_icon_viewer_btn)
        # Add the scroll area to the main layout
        dev_layout.addWidget(dev_scroll_area)  # Add the scroll area to the tab layout
        tabs_layout.addTab(dev_tab, "Dev")

        # change bottom layout
        bottom_layout = QtWidgets.QHBoxLayout()

        # create icon label
        icon_label = QtWidgets.QLabel()

        if os.path.exists(TOOLBOX_ICON):
            icon = QtGui.QPixmap(TOOLBOX_ICON).scaled(24, 24, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            icon_label.setPixmap(icon)
        else:
            print(f"Warning: Icon file '{TOOLBOX_ICON}' does not exist.")
        
        # add icon label to bottom layout
        bottom_layout.addWidget(icon_label)
        
        # add version information label
        version_label = QtWidgets.QLabel(f"{TOOLBOX_VERSION}")
        version_label.setStyleSheet("color: gray; font-size: 12px;")
        bottom_layout.addWidget(version_label)
        
        # add a stretchable space to push the help and language buttons to the right
        bottom_layout.addStretch()
        
        # add help and language buttons
        bottom_layout.addWidget(self.help_btn)
        bottom_layout.addWidget(self.lang_btn)

        # add bottom layout to main layout
        main_layout.addLayout(bottom_layout)

    def create_connections(self):
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
        self.modeling_edge_sensei_btn.clicked.connect(self.run_edge_sensei)
        self.modeling_round_inset_btn.clicked.connect(self.run_round_inset)
        self.modeling_arc_deformer_btn.clicked.connect(self.run_arc_deformer)
        self.modeling_instant_drag_btn.clicked.connect(self.run_instant_drag)
        self.modeling_unbevel_btn.clicked.connect(self.run_unbevel)
        self.modeling_speed_bend_btn.clicked.connect(self.run_speed_bend)
        self.modeling_align_edge_btn.clicked.connect(self.run_align_edge)
        self.modeling_extra_curve_btn.clicked.connect(self.run_extra_curve)
        self.modeling_gs_curve_tools_btn.clicked.connect(self.run_gs_curve_tools)
        self.modeling_reset_gs_curve_tools_btn.clicked.connect(self.reset_gs_curve_tools)
        self.modeling_close_gs_curve_tools_btn.clicked.connect(self.stop_gs_curve_tools)
        self.modeling_uv_set_editor_btn.clicked.connect(self.run_uv_set_editor)
        self.modeling_uvdeluxe_btn.clicked.connect(self.run_uvdeluxe)
        self.modeling_rizom_uv_bridge_btn.clicked.connect(self.run_rizom_uv_bridge)
        # Metahuman tab connections
        self.metahuman_body_prepare_btn.clicked.connect(self.run_body_prepare)
        # Rigging tab connections
        self.rigging_advanced_skeleton_btn.clicked.connect(self.run_advanced_skeleton)
        # Animation tab connections
        self.animation_animschool_picker_btn.clicked.connect(self.run_anim_school_picker)
        self.animation_dwpicker_btn.clicked.connect(self.run_dwpicker)
        self.animation_bhghost_btn.clicked.connect(self.run_bhghost)
        self.animation_ikfk_switch_btn.clicked.connect(self.run_ik_fk_switch)
        self.animation_atools_btn.clicked.connect(self.open_aTools)
        self.animation_keyframepro_btn.clicked.connect(self.open_keyframe_pro)
        self.animation_studiolibrary_btn.clicked.connect(self.open_studio_library)
        self.animation_epic_pose_wrangler_btn.clicked.connect(self.open_epic_pose_wrangler)
        self.animation_morph_shape_btn.clicked.connect(self.run_morph_shape)
        self.animation_universal_rig_adapter_btn.clicked.connect(self.run_universal_rig_adapter)
        # Dev tab connections
        self.dev_icon_viewer_btn.clicked.connect(self.run_icon_viewer)
        # connect help button
        self.help_btn.clicked.connect(self.show_help)
        # connect language switch button
        self.lang_btn.clicked.connect(self.toggle_language)


#========================================================================== FUNCTIONS ==========================================================================

    
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
            BatchImport_Path = os.path.normpath(os.path.join(METABOX_PATH, 'Metahuman', 'Custom', 'BatchImport.py')).replace('\\', '/')
            if BatchImport_Path not in sys.path:
                sys.path.append(BatchImport_Path)
            from Metahuman.Custom import BatchImport
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

            gs_curvetools_sub_path = [
                os.path.join(gs_curvetools_path, 'fonts').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'icons').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'plugins').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'utils').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'constants').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'core').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'main').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'ui').replace('\\', '/'),
                os.path.join(gs_curvetools_path, 'uv_editor').replace('\\', '/')
            ]
            for path in gs_curvetools_sub_path:
                if path not in sys.path:
                    sys.path.insert(0, path)

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

    def run_dwpicker(self, *args):
        try:
            DWPICKER_PATH = os.path.normpath(os.path.join(METABOX_PATH, 'Animation', 'dwpicker')).replace('\\', '/')
            if DWPICKER_PATH not in sys.path:
                sys.path.insert(0, DWPICKER_PATH)
            DWPICKER_SUB_PATHS = [
                os.path.join(DWPICKER_PATH, 'scripts'),
                os.path.join(DWPICKER_PATH, 'dwpicker')
            ]
            for path in DWPICKER_SUB_PATHS:
                if path not in sys.path:
                    sys.path.insert(0, path)
            for path in sys.path:
                print("Added the dwpicker submoudle path: ", path)
            from Animation.dwpicker import dwpicker
            dwpicker.show()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running dwpicker: {e}"
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
            
    def run_icon_viewer(self, *args):
        try:
            from Dev.mayaiconview import create_icon_viewer
            create_icon_viewer()
        except Exception as e:
            ERROR_MESSAGE = f"Error occurred while running Icon Viewer: {e}"
            cmds.warning(ERROR_MESSAGE)
            cmds.confirmDialog(title='Error', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK')
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Help and Language
# ****************************************************************************************************************
    def show_help(self):
        # Specify the URL of the website you want to open
        webbrowser.open(TOOLBOX_HELP)

    def toggle_language(self):
        global CURRENT_LANG
        CURRENT_LANG = 'en_US' if CURRENT_LANG == 'zh_CN' else 'zh_CN'
        self.lang_btn.setText("EN" if CURRENT_LANG == 'zh_CN' else "CN")
        self.retranslate_ui()
        
        QtWidgets.QToolTip.showText(
            self.lang_btn.mapToGlobal(QtCore.QPoint(0, -30)),
            "Language switched" if CURRENT_LANG == 'en_US' else "语言已切换",
            self.lang_btn
        )

    def retranslate_ui(self):
        # Update all UI elements
        self.setWindowTitle("MetaBox")
        self.help_btn.setText(LANG[CURRENT_LANG]["DOCUMENT"])
        self.help_btn.setFont(QtGui.QFont("Microsoft YaHei", 10))
        self.help_btn.setToolTip(LANG[CURRENT_LANG]["Help"])
        self.lang_btn.setFont(QtGui.QFont("Microsoft YaHei", 10))
        self.lang_btn.setToolTip(LANG[CURRENT_LANG]["Switch Language"])
        self.modeling_tab_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_tab_btn.setText(LANG[CURRENT_LANG]["Modeling"])
        self.metahuman_tab_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.metahuman_tab_btn.setText(LANG[CURRENT_LANG]["Metahuman"])
        self.rigging_tab_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.rigging_tab_btn.setText(LANG[CURRENT_LANG]["Rigging"])
        self.animation_tab_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_tab_btn.setText(LANG[CURRENT_LANG]["Animation"])
        self.animation_tab_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_display_group.setTitle(LANG[CURRENT_LANG]["Display"] )
        self.modeling_display_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_xray_btn.setText(LANG[CURRENT_LANG]["Xray"])
        self.modeling_xray_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_joint_xray_btn.setText(LANG[CURRENT_LANG]["Joint Xray"])
        self.modeling_joint_xray_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_manage_group.setTitle(LANG[CURRENT_LANG]["Manage"])
        self.modeling_manage_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_rename_btn.setText(LANG[CURRENT_LANG]["Rename"])
        self.modeling_rename_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_batch_import_btn.setText(LANG[CURRENT_LANG]["Batch Import"])
        self.modeling_batch_import_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_select_group.setTitle(LANG[CURRENT_LANG]["Select"])
        self.modeling_select_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_interval_select_edge_btn.setText(LANG[CURRENT_LANG]["Interval Select Edge"])
        self.modeling_interval_select_edge_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_same_position_selector_btn.setText(LANG[CURRENT_LANG]["Same Position Selector"])
        self.modeling_same_position_selector_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_edge_loop_smart_select_btn.setText(LANG[CURRENT_LANG]["Edge Loop Smart Select"])
        self.modeling_edge_loop_smart_select_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_even_edge_loop_btn.setText(LANG[CURRENT_LANG]["Even Edge Loop"])
        self.modeling_even_edge_loop_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_tools_group.setTitle(LANG[CURRENT_LANG]["Tools"])
        self.modeling_tools_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_crease_plus_btn.setText(LANG[CURRENT_LANG]["Crease Plus"])
        self.modeling_crease_plus_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_speed_cut_btn.setText(LANG[CURRENT_LANG]["Speed Cut"])
        self.modeling_speed_cut_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_modit_btn.setText(LANG[CURRENT_LANG]["ModIt"])
        self.modeling_modit_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_plugit_btn.setText(LANG[CURRENT_LANG]["PlugIt"])
        self.modeling_plugit_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_zirail_btn.setText(LANG[CURRENT_LANG]["Zirail"])
        self.modeling_zirail_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_xgtools_btn.setText(LANG[CURRENT_LANG]["Groomer`s Tool"])
        self.modeling_xgtools_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_edge_sensei_btn.setText(LANG[CURRENT_LANG]["Edge Sensei"])
        self.modeling_edge_sensei_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_round_inset_btn.setText(LANG[CURRENT_LANG]["Round Inset"])
        self.modeling_round_inset_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_arc_deformer_btn.setText(LANG[CURRENT_LANG]["Arc Deformer"])
        self.modeling_arc_deformer_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_instant_drag_btn.setText(LANG[CURRENT_LANG]["Instant Drag"])
        self.modeling_instant_drag_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_unbevel_btn.setText(LANG[CURRENT_LANG]["Un Bevel"])
        self.modeling_unbevel_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_align_edge_btn.setText(LANG[CURRENT_LANG]["Align Edge"])
        self.modeling_align_edge_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_extra_curve_btn.setText(LANG[CURRENT_LANG]["Extra Curve"])
        self.modeling_extra_curve_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_speed_bend_btn.setText(LANG[CURRENT_LANG]["Speed Bend"])
        self.modeling_speed_bend_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_gs_curve_tools_group.setTitle(LANG[CURRENT_LANG]["GS Curve Tools"])
        self.modeling_gs_curve_tools_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_gs_curve_tools_btn.setText(LANG[CURRENT_LANG]["GS Curve Tools"])
        self.modeling_gs_curve_tools_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_reset_gs_curve_tools_btn.setText(LANG[CURRENT_LANG]["GS Curve Tools Reset"])
        self.modeling_reset_gs_curve_tools_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_close_gs_curve_tools_btn.setText(LANG[CURRENT_LANG]["GS Curve Tools Close"])
        self.modeling_close_gs_curve_tools_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_uv_group.setTitle(LANG[CURRENT_LANG]["UV"])
        self.modeling_uv_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_uvdeluxe_btn.setText(LANG[CURRENT_LANG]["UVDeluxe"])
        self.modeling_uvdeluxe_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_rizom_uv_bridge_btn.setText(LANG[CURRENT_LANG]["RizomUV Bridge"])
        self.modeling_rizom_uv_bridge_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.modeling_uv_set_editor_btn.setText(LANG[CURRENT_LANG]["UV Set Editor"])
        self.modeling_uv_set_editor_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.metahuman_preparation_group.setTitle(LANG[CURRENT_LANG]["Preparation"])
        self.metahuman_preparation_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.metahuman_body_prepare_btn.setText(LANG[CURRENT_LANG]["Body Prepare"])
        self.metahuman_body_prepare_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.rigging_setup_group.setTitle(LANG[CURRENT_LANG]["Setup"])
        self.rigging_setup_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.rigging_advanced_skeleton_btn.setText(LANG[CURRENT_LANG]["Advanced Skeleton"])
        self.rigging_advanced_skeleton_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_select_group.setTitle(LANG[CURRENT_LANG]["Select"])
        self.animation_select_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_animschool_picker_btn.setText(LANG[CURRENT_LANG]["Anim School Picker"])
        self.animation_animschool_picker_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_dwpicker_btn.setText(LANG[CURRENT_LANG]["DWPicker"])
        self.animation_dwpicker_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_tools_group.setTitle(LANG[CURRENT_LANG]["Tools"])
        self.animation_tools_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_bhghost_btn.setText(LANG[CURRENT_LANG]["bhGhost"])
        self.animation_bhghost_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_ikfk_switch_btn.setText(LANG[CURRENT_LANG]["IK/FK Switch"])
        self.animation_ikfk_switch_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_atools_btn.setText(LANG[CURRENT_LANG]["aTools"])
        self.animation_atools_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_keyframepro_btn.setText(LANG[CURRENT_LANG]["Keyframe Pro"])
        self.animation_keyframepro_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_studiolibrary_btn.setText(LANG[CURRENT_LANG]["Studio Library"])
        self.animation_studiolibrary_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_pose_group.setTitle(LANG[CURRENT_LANG]["Pose Tools"])
        self.animation_pose_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_epic_pose_wrangler_btn.setText(LANG[CURRENT_LANG]["Epic Pose Wrangler"])
        self.animation_epic_pose_wrangler_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_morph_shape_btn.setText(LANG[CURRENT_LANG]["Morph Shape"])
        self.animation_morph_shape_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.animation_universal_rig_adapter_btn.setText(LANG[CURRENT_LANG]["Universal Rig Adapter"])
        self.animation_universal_rig_adapter_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.dev_tools_group.setTitle(LANG[CURRENT_LANG]["Dev Tool"])
        self.dev_tools_group.setFont(QtGui.QFont("Microsoft YaHei", 8))
        self.dev_icon_viewer_btn.setText(LANG[CURRENT_LANG]["Icon Viewer"])
        self.dev_icon_viewer_btn.setFont(QtGui.QFont("Microsoft YaHei", 8))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Show Window
# ************************************************************************************************************************************************************************************************************
def show():
    global main_window
    try:
        if cmds.workspaceControl(WKSP_CTRL_NAME, exists=True):
            cmds.deleteUI(WKSP_CTRL_NAME, control=True)
        elif main_window:
            main_window.close()
            main_window.deleteLater()
    except:
        pass
    
    def create_ui(retry_count=0):
        global main_window
        try:
            main_window = MetaBox()
            main_window.dock_to_maya()
        except Exception as e:
            if retry_count < 3:
                print(f"MetaBox creation failed, retrying... (Attempt {retry_count + 1})")
                utils.executeDeferred(lambda: create_ui(retry_count + 1))
            else:
                print(f"Failed to create MetaBox after 3 attempts: {str(e)}")

    utils.executeDeferred(create_ui)

    # Create a new window instance and dock it to Maya
    main_window = MetaBox()
    cmds.evalDeferred(lambda *args: main_window.dock_to_maya())

def load_metabox():
    from MetaBox import show
    show()

utils.executeDeferred(load_metabox)

if __name__ == "__main__":
    show()