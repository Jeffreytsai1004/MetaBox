#!/usr/bin/env python
# -*- coding: utf-8 -*-

##--------------------------------------------------------------------------
## ScriptName : ModIt 3.0
## Author     : Wizix
## StartDate : 2022/09/09
## LastUpdate : 2022/13/09
## Version    : 0.0.1
##-------------------------------------------------------------------------- I M P O R T
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.cmds as cmds
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
from maya import OpenMayaUI as omui
from functools import partial
# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
##---------------------------------------- Import Modules
import importlib
from . import ModIt_Global
importlib.reload(ModIt_Global)
from . import ModIt_CSS
importlib.reload(ModIt_CSS)

##---------------------------------------- Import Classes
from .Class import Collapsible
importlib.reload(Collapsible)
from .Modeling import Section_PRIMITIVES
importlib.reload(Section_PRIMITIVES)
from .Modeling import Section_COLORS
importlib.reload(Section_COLORS)
from .Modeling import Section_SETS
importlib.reload(Section_SETS)
from .Modeling import Section_SELECTIONS
importlib.reload(Section_SELECTIONS)
from .Modeling import Section_MESH
importlib.reload(Section_MESH)
from .Modeling import Section_TOOLS
importlib.reload(Section_TOOLS)
from .Modeling import Section_UTILITIES
importlib.reload(Section_UTILITIES)

from .Placement import Layout_PLACEMENT
importlib.reload(Layout_PLACEMENT)

from .Setting import Layout_SETTING
importlib.reload(Layout_SETTING)
from .Shading import Layout_SHADING
importlib.reload(Layout_SHADING)



##-------------------------------------------------------------------------- G L O B A L   V A R
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath
RessourcePath = ModIt_Global.RessourcePath

#GLOBAR VAR UI
WINDOW_TITLE = ModIt_Global.ModItTitle


##JSON PREF DATA
ADAP_HEIGHT = (json.load(open(PreferencePath + 'UI_Adapt_Height.json',"r"))['VALUE'])
TAB_OPEN =(json.load(open(PreferencePath + 'TabOpen.json',"r"))['TAB_OPEN'])

S_UTILITIES_VALUE =(json.load(open(PreferencePath + 'Section_Utilities.json',"r"))['VALUE'])
S_PRIMITIVES_VALUE =(json.load(open(PreferencePath + 'Section_Primitives.json',"r"))['VALUE'])
S_COLORS_VALUE =(json.load(open(PreferencePath + 'Section_Colors.json',"r"))['VALUE'])
S_SELECTIONS_VALUE =(json.load(open(PreferencePath + 'Section_Selections.json',"r"))['VALUE'])
S_MESH_VALUE =(json.load(open(PreferencePath + 'Section_Mesh.json',"r"))['VALUE'])
S_SETS_VALUE =(json.load(open(PreferencePath + 'Section_Sets.json',"r"))['VALUE'])
S_TOOLS_VALUE =(json.load(open(PreferencePath + 'Section_Tools.json',"r"))['VALUE'])

WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])

DOCK =(json.load(open(PreferencePath + 'Dockable.json',"r"))['VALUE'])



##-------------------------------------------------------------------------- B U I L D   U I
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow() ##Return the Maya main window widget as a Python object
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class ModIt_UI(QtWidgets.QDialog):
    if DOCK == 0:
        def __init__(self, parent=maya_main_window()):
            super(ModIt_UI, self).__init__(parent)
            ##__________________________________________________________________ SAVE UI POSITION
            self.settings_path = os.path.join(PreferencePath + "settingsFile.ini")


            ##__________________________________________________________________ WINDOWS SETTING
            self.setWindowTitle(WINDOW_TITLE)
            self.setFixedSize(340, ADAP_HEIGHT)
            icon = QIcon(IconPath + "ModIt_Window_Ico.png")
            self.setWindowIcon(icon)

            self.buildUI()

    else:
        def __init__(self, parent=None):
            super(ModIt_UI, self).__init__()

            ##__________________________________________________________________ SAVE UI POSITION
            self.settings_path = os.path.join(PreferencePath + "settingsFile.ini")
            self.setMinimumSize(400, 660)
            self.buildUI()



    def buildUI(self):
        open(PreferencePath + 'JobNumber.json', "w").write(json.dumps({"JOB_NUMBER": 0}))
        # ******************************************
        #           BUTTONS PARAMS
        # ******************************************
        Tab_iconFixeSize = 30
        Tab_iconButtonSize = 24
        iconFixeSize = ModIt_Global.iconFixeSize
        iconButtonSize = ModIt_Global.iconButtonSize
        separatorWidth = ModIt_Global.separatorWidth

        ##__________________// UI - Import CSS
        self.setStyleSheet(ModIt_Global.Theme)
        ##_________________//  Restore Previous Position
        settings_obj = QtCore.QSettings(self.settings_path, QtCore.QSettings.IniFormat)
        self.restoreGeometry(settings_obj.value("windowGeometry"))
        ##_________________//  GLOBAL LAYOUT
        GLOBAL_Lyt = QtWidgets.QVBoxLayout(self)
        GLOBAL_Lyt.setSpacing(0)
        GLOBAL_Lyt.setContentsMargins(0, 0, 0, 0)

        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  TABS
        ##------------------------------------------------------------------------------------//
        self.TABSBAR_Widget = QtWidgets.QWidget()
        self.TABSBAR_Widget.setStyleSheet("background-color:#222222;") #TABS BG  - Pose problem bg color
        self.TABSBAR_Lyt = QtWidgets.QHBoxLayout(self.TABSBAR_Widget)
        self.TABSBAR_Lyt.setAlignment(QtCore.Qt.AlignTop)
        self.TABSBAR_Lyt.setContentsMargins(0, 0, 0, 0)
        self.TABSBAR_Lyt.setSpacing(0)
        GLOBAL_Lyt.addWidget(self.TABSBAR_Widget)

        ##______________________________________________________/ BTN MODELING TAB
        self.ModelingTab_Btn = QtWidgets.QPushButton()
        if TAB_OPEN == 0:
            self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_ON.png"))
            self.ModelingTab_Btn.setStyleSheet("background-color:#303030;")
        else:
            self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_OFF.png"))
            self.ModelingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")
        self.ModelingTab_Btn.setFixedSize(Tab_iconFixeSize,Tab_iconFixeSize)
        self.ModelingTab_Btn.setIconSize(QtCore.QSize(Tab_iconButtonSize, Tab_iconButtonSize))
        self.ModelingTab_Btn.setToolTip("  ModIt  ")

        self.ModelingTab_Btn.clicked.connect(self.ModelingTab_ON)
        self.TABSBAR_Lyt.addWidget(self.ModelingTab_Btn)

        ##______________________________________________________/ BTN SHADING TAB
        self.ShadingTab_Btn = QtWidgets.QPushButton()
        if TAB_OPEN == 1:
            self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_ON.png"))
            self.ShadingTab_Btn.setStyleSheet("background-color:#303030;")
        else:
            self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_OFF.png"))
            self.ShadingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        self.ShadingTab_Btn.setFixedSize(Tab_iconFixeSize,Tab_iconFixeSize)
        self.ShadingTab_Btn.setIconSize(QtCore.QSize(Tab_iconButtonSize, Tab_iconButtonSize))

        self.ShadingTab_Btn.clicked.connect(self.ShadingTab_ON)
        self.ShadingTab_Btn.setToolTip("  ViewportIt  ")
        self.TABSBAR_Lyt.addWidget(self.ShadingTab_Btn)

        ##______________________________________________________/ BTN PLACEMENT TAB
        self.PlacementTab_Btn = QtWidgets.QPushButton()
        if TAB_OPEN == 2:
            self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "PLACEMENT_ON.png"))
            self.PlacementTab_Btn.setStyleSheet("background-color:#303030;")
        else:
            self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "PLACEMENT_OFF.png"))
            self.PlacementTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\QPushButton::hover{background-color : #343434;}")

        self.PlacementTab_Btn.setFixedSize(Tab_iconFixeSize,Tab_iconFixeSize)
        self.PlacementTab_Btn.setIconSize(QtCore.QSize(Tab_iconButtonSize, Tab_iconButtonSize))

        self.PlacementTab_Btn.clicked.connect(self.PlacementTab_ON)
        self.PlacementTab_Btn.setToolTip("  Placement  ")
        self.TABSBAR_Lyt.addWidget(self.PlacementTab_Btn)


        ##______________________________________________________/ BTN SETTING TAB
        self.SettingTab_Btn = QtWidgets.QPushButton()
        if TAB_OPEN == 3:
            self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_ON.png"))
            self.SettingTab_Btn.setStyleSheet("background-color:#303030;")
        else:
            self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_OFF.png"))
            self.SettingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\QPushButton::hover{background-color : #343434;}")

        self.SettingTab_Btn.setFixedSize(Tab_iconFixeSize,Tab_iconFixeSize)
        self.SettingTab_Btn.setIconSize(QtCore.QSize(Tab_iconButtonSize, Tab_iconButtonSize))

        self.SettingTab_Btn.clicked.connect(self.SettingTab_ON)
        self.SettingTab_Btn.setToolTip("  Setting  ")
        self.TABSBAR_Lyt.addWidget(self.SettingTab_Btn)

        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B    M O D E L I N G
        ##------------------------------------------------------------------------------------//
        self.TAB_MODELING_Widget = QtWidgets.QWidget()
        GLOBAL_Lyt.addWidget(self.TAB_MODELING_Widget)
        self.ALL_SECTIONS_HLyt = QtWidgets.QVBoxLayout(self.TAB_MODELING_Widget)
        self.ALL_SECTIONS_HLyt.setContentsMargins(0, 0, 0, 0)
        self.ALL_SECTIONS_HLyt.setSpacing(5)#          BETWEEN SECTIONS
        self.ALL_SECTIONS_HLyt.setAlignment(QtCore.Qt.AlignTop)




        ##_________________________________________________________________________________________________________________/   U T I L I T E S
        self.Collapsible_wdg_SETS = Collapsible.CollapsibleWidget("U T I L I T E S")
        self.Collapsible_wdg_SETS.set_expanded(S_UTILITIES_VALUE)
        self.Collapsible_wdg_SETS.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Utilities", 40))
        self.Collapsible_wdg_SETS.add_widget(Section_UTILITIES.UTILITIES_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_SETS)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)


        ##_________________________________________________________________________________________________________________/   P R I M I T I V E S
        self.Collapsible_wdg_PRIMITIVES = Collapsible.CollapsibleWidget("P R I M I T I V E S")
        self.Collapsible_wdg_PRIMITIVES.set_expanded(S_PRIMITIVES_VALUE)
        self.Collapsible_wdg_PRIMITIVES.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Primitives", 40))
        self.Collapsible_wdg_PRIMITIVES.add_widget(Section_PRIMITIVES.PRIMITIVES_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_PRIMITIVES)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)


        ##_________________________________________________________________________________________________________________/   C O L O R S
        self.Collapsible_wdg_COLORS = Collapsible.CollapsibleWidget("C O L O R S")
        self.Collapsible_wdg_COLORS.set_expanded(S_COLORS_VALUE)
        self.Collapsible_wdg_COLORS.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Colors", 40))
        self.Collapsible_wdg_COLORS.add_widget(Section_COLORS.COLORS_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_COLORS)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)


        ##_________________________________________________________________________________________________________________/   S E L E C T I O N S
        self.Collapsible_wdg_SELECTIONS = Collapsible.CollapsibleWidget("S E L E C T I O N S")
        self.Collapsible_wdg_SELECTIONS.set_expanded(S_SELECTIONS_VALUE)
        self.Collapsible_wdg_SELECTIONS.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Selections", 40))
        self.Collapsible_wdg_SELECTIONS.add_widget(Section_SELECTIONS.SELECTIONS_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_SELECTIONS)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)

        ##_________________________________________________________________________________________________________________/   M E S H
        self.Collapsible_wdg_MESH = Collapsible.CollapsibleWidget("M E S H")
        self.Collapsible_wdg_MESH.set_expanded(S_MESH_VALUE)
        self.Collapsible_wdg_MESH.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Mesh", 110))
        self.Collapsible_wdg_MESH.add_widget(Section_MESH.MESH_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_MESH)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)


        ##_________________________________________________________________________________________________________________/   S E T S
        self.Collapsible_wdg_SETS = Collapsible.CollapsibleWidget("S E T S")
        self.Collapsible_wdg_SETS.set_expanded(S_SETS_VALUE)
        self.Collapsible_wdg_SETS.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Sets", 85))
        self.Collapsible_wdg_SETS.add_widget(Section_SETS.SETS_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_SETS)
        ## _____________________________________________________/ Separator
        self.ALL_SECTIONS_HLyt.addSpacing(2)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(2000,2)
        self.Separator.setStyleSheet("background-color:#262626;")
        self.ALL_SECTIONS_HLyt.addWidget(self.Separator)



        ##_________________________________________________________________________________________________________________/   T O O L S
        self.Collapsible_wdg_TOOLS = Collapsible.CollapsibleWidget("T O O L S")
        self.Collapsible_wdg_TOOLS.set_expanded(S_TOOLS_VALUE)
        self.Collapsible_wdg_TOOLS.collapsed_signal.connect(partial(self.Section_OpenClose_btn, "Tools", 40))
        self.Collapsible_wdg_TOOLS.add_widget(Section_TOOLS.TOOLS_LAYOUT())
        self.ALL_SECTIONS_HLyt.addWidget(self.Collapsible_wdg_TOOLS)






        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   S H A D I N G
        ##------------------------------------------------------------------------------------//
        self.TAB_SHADING_Widget = QtWidgets.QWidget()
        GLOBAL_Lyt.addWidget(self.TAB_SHADING_Widget)
        self.TAB_SHADING_Lyt = QtWidgets.QVBoxLayout(self.TAB_SHADING_Widget)
        self.TAB_SHADING_Lyt.addWidget(Layout_SHADING.SHADING_LAYOUT())




        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   P L A C E M E N T
        ##------------------------------------------------------------------------------------//
        self.TAB_PLACEMENT_Widget = QtWidgets.QWidget()
        GLOBAL_Lyt.addWidget(self.TAB_PLACEMENT_Widget)
        self.TAB_PLACEMENT_Lyt = QtWidgets.QVBoxLayout(self.TAB_PLACEMENT_Widget)
        self.TAB_PLACEMENT_Lyt.addWidget(Layout_PLACEMENT.PLACEMENT_LAYOUT())





        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B    S E T T I N G
        ##------------------------------------------------------------------------------------//
        self.TAB_SETTING_Widget = QtWidgets.QWidget()
        GLOBAL_Lyt.addWidget(self.TAB_SETTING_Widget)
        self.TAB_SETTING_Lyt = QtWidgets.QVBoxLayout(self.TAB_SETTING_Widget)
        self.TAB_SETTING_Lyt.addWidget(Layout_SETTING.SETTING_LAYOUT())





        ##__________________________________________________________________// UI - END
        self.ALL_SECTIONS_HLyt.addStretch()
        self.TAB_SHADING_Lyt.addStretch()
        self.TAB_PLACEMENT_Lyt.addStretch()
        self.TAB_SETTING_Lyt.addStretch()

        ##_______________/ AT SCRIPT OPENING SET HIDE/SHOW TABS
        if TAB_OPEN == 0:
            self.ModelingTab_ON()
        if TAB_OPEN == 1:
            self.ShadingTab_ON()
        if TAB_OPEN == 2:
            self.PlacementTab_ON()
        if TAB_OPEN == 3:
            self.SettingTab_ON()



    ##_________________________________________________________________________________// ACTIONS DEF
    ##_____________________________________________________________
    ##______________________________________________________/   TABS BAR
    def ModelingTab_ON(self):
        ADAP_HEIGHT = (json.load(open(PreferencePath + 'UI_Adapt_Height.json', "r"))['VALUE'])
        self.TAB_MODELING_Widget.show()
        self.TAB_SHADING_Widget.hide()
        self.TAB_PLACEMENT_Widget.hide()
        self.TAB_SETTING_Widget.hide()

        if DOCK == 0:
            self.setFixedHeight(ADAP_HEIGHT)
            self.resize(self.width(), ADAP_HEIGHT)

        self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_ON.png"))
        self.ModelingTab_Btn.setStyleSheet("background-color:#303030;")  # TABS BTN BG  - ACTIF

        self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_OFF.png"))
        self.ShadingTab_Btn.setStyleSheet("QPushButton{background-color :#292929;}\QPushButton::hover{background-color : #343434;}")

        self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "TabScrew_OFF.png"))
        self.PlacementTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_OFF.png"))
        self.SettingTab_Btn.setStyleSheet("QPushButton{background-color :#292929;}\ QPushButton::hover{background-color : #343434;}")


        open(PreferencePath + 'TabOpen.json', "w").write(json.dumps({"TAB_OPEN" : 0}))



    def ShadingTab_ON(self):
        self.TAB_MODELING_Widget.hide()
        self.TAB_SHADING_Widget.show()
        self.TAB_PLACEMENT_Widget.hide()
        self.TAB_SETTING_Widget.hide()

        if DOCK == 0:
            if WIN_DISPLAY_SIZE == 0:  # 125
                self.setFixedHeight(535)
            else:
                self.setFixedHeight(555)
            self.resize(self.width(), 40)

        self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_ON.png"))
        self.ShadingTab_Btn.setStyleSheet("background-color:#303030;")


        self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_OFF.png"))
        self.ModelingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")

        self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "TabScrew_OFF.png"))
        self.PlacementTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_OFF.png"))
        self.SettingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")

        open(PreferencePath + 'TabOpen.json', "w").write(json.dumps({"TAB_OPEN" : 1}))

    def PlacementTab_ON(self):
        self.TAB_MODELING_Widget.hide()
        self.TAB_SHADING_Widget.hide()
        self.TAB_PLACEMENT_Widget.show()
        self.TAB_SETTING_Widget.hide()

        if DOCK == 0:
            self.setFixedHeight(680)
            self.resize(self.width(), 40)

        self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "TabScrew_ON.png"))
        self.PlacementTab_Btn.setStyleSheet("background-color:#303030;")

        self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_OFF.png"))
        self.ModelingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_OFF.png"))
        self.ShadingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")

        self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_OFF.png"))
        self.SettingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        open(PreferencePath + 'TabOpen.json', "w").write(json.dumps({"TAB_OPEN" : 2}))


    def SettingTab_ON(self):
        self.TAB_MODELING_Widget.hide()
        self.TAB_SHADING_Widget.hide()
        self.TAB_PLACEMENT_Widget.hide()
        self.TAB_SETTING_Widget.show()

        if DOCK == 0:
            if WIN_DISPLAY_SIZE == 0:  # 125
                self.setFixedHeight(440)
            else:
                self.setFixedHeight(480)


            self.resize(self.width(), 40)

        self.SettingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SETTING_ON.png"))
        self.SettingTab_Btn.setStyleSheet("background-color:#303030;")

        self.ModelingTab_Btn.setIcon(QtGui.QIcon(IconPath + "MODELING_OFF.png"))
        self.ModelingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")

        self.PlacementTab_Btn.setIcon(QtGui.QIcon(IconPath + "TabScrew_OFF.png"))
        self.PlacementTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")


        self.ShadingTab_Btn.setIcon(QtGui.QIcon(IconPath + "SHADING_OFF.png"))
        self.ShadingTab_Btn.setStyleSheet("QPushButton{background-color :#272727;}\ QPushButton::hover{background-color : #343434;}")

        open(PreferencePath + 'TabOpen.json', "w").write(json.dumps({"TAB_OPEN" : 3}))




    def Section_OpenClose_btn(self, name, size, signal):
        ADAP_HEIGHT = (json.load(open(PreferencePath + 'UI_Adapt_Height.json',"r"))['VALUE'])
        userWidht = self.width()

        if signal == 1:
            NEW_ADAP_HEIGHT = ADAP_HEIGHT + size
            self.setMinimumHeight(NEW_ADAP_HEIGHT)
            self.resize(userWidht, NEW_ADAP_HEIGHT)
            open(PreferencePath + 'Section_' + str(name) + '.json', "w").write(json.dumps({"VALUE": 1}))
            open(PreferencePath + 'UI_Adapt_Height.json', "w").write(json.dumps({"VALUE": NEW_ADAP_HEIGHT}))



        else:
            NEW_ADAP_HEIGHT = ADAP_HEIGHT - size
            self.setMinimumHeight(NEW_ADAP_HEIGHT)
            self.resize(userWidht, NEW_ADAP_HEIGHT)
            open(PreferencePath + 'Section_'+  str(name) + '.json', "w").write(json.dumps({"VALUE": 0}))
            open(PreferencePath + 'UI_Adapt_Height.json', "w").write(json.dumps({"VALUE": NEW_ADAP_HEIGHT}))







    def closeEvent(self, event):
        # Save window's geometry
        settings_obj = QtCore.QSettings(self.settings_path, QtCore.QSettings.IniFormat)
        settings_obj.setValue("windowGeometry", self.saveGeometry())

        ##KILL INTERACTIVE PRIM SCRIPT JOB
        JOB_NUMBER = (json.load(open(PreferencePath + 'JobNumber.json', "r"))['JOB_NUMBER'])
        try:
            mc.scriptJob(kill=JOB_NUMBER, force=True)
        except:
            pass

        ##DELETE PopUp UI
        if mc.window("Bevel2", exists=True):
            mc.deleteUI("Bevel2")
        if mc.window("Bend", exists=True):
            mc.deleteUI("Bend")
        if mc.window("Linear Duplication", exists=True):
            mc.deleteUI("Linear Duplication")
        if mc.window("Radial Duplication", exists=True):
            mc.deleteUI("Radial Duplication")
        if mc.window("Curve Duplication", exists=True):
            mc.deleteUI("Curve Duplication")
##_____________________________________________________________
##_________________________________________________________________________________// UI
##_____________________________________________________________


if DOCK == 0:
    try:
        UI.close() # pylint: disable=E0601
        UI.deleteLater()
    except:
        pass

    UI = ModIt_UI()
    UI.show()

else:

    def Dock(Widget, width=200, height=200, hp="free", show=True):
        name = ModIt_Global.ModItTitle
        label = getattr(Widget, "label", name)

        try:
            cmds.deleteUI(name)
        except RuntimeError:
            pass

        dockControl = cmds.workspaceControl(
            name,
            initialWidth=width,
            minimumWidth=False,
            widthProperty=hp,
            heightProperty=hp,
            label=label
        )

        dockPtr = omui.MQtUtil.findControl(dockControl)
        dockWidget = QtCompat.wrapInstance(int(dockPtr), QtWidgets.QWidget)
        dockWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        child = Widget(dockWidget)
        dockWidget.layout().addWidget(child)

        if show:
            cmds.evalDeferred(
                lambda *args: cmds.workspaceControl(
                    dockControl,
                    edit=True,
                    widthProperty="free",
                    restore=True
                )
            )
        return child


    def atClose():
        print("At MODIT CLOSE")
        if mc.window("ModIt_Global.ModItTitle", exists=True):
            mc.deleteUI("ModIt_Global.ModItTitle")





    def showUI():
        ui = Dock(ModIt_UI)
        ui.show()



        # # Get a pointer and convert it to Qt Widget object
        # qw = omui.MQtUtil.findWindow(ModIt_Global.ModItTitle)
        # try:
        #     widget = wrapInstance(int(qw), QWidget)
        #     # Create a QIcon object
        #     icon = QIcon(IconPath + "ModIt_Window_Ico.png")
        #     # Assign the icon
        #     widget.setWindowIcon(icon)
        # except:
        #     pass  # Pour si on reload alos qu'il est dock

        # return ui