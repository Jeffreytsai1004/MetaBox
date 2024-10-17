##--------------------------------------------------------------------------
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
# import mtoa.core as core
from functools import partial

# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget

import importlib
from .. import ModIt_Global

importlib.reload(ModIt_Global)

from .. import ModIt_CSS
importlib.reload(ModIt_CSS)




##______________________GLOBAL VAR
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath
RessourcePath = ModIt_Global.RessourcePath


# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 20
iconButtonSize = 20
separatorWidth = ModIt_Global.separatorWidth

##JSON PREF DATA
SCREW_MODE =(json.load(open(PreferencePath + 'Screw_Mode.json',"r"))['VALUE'])
SCREW_SIZE =(json.load(open(PreferencePath + 'MultiSize.json',"r"))['MULTISIZEVALUE'])

WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])


class PLACEMENT_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_PLACEMENT_LAYOUT = QtWidgets.QVBoxLayout()  # MAIN
        self.setLayout(SECTION_PLACEMENT_LAYOUT)
        SECTION_PLACEMENT_LAYOUT.setContentsMargins(0,0,0,0)


        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   M O D E L I N G
        ###------------------------------------------------------------------------------------// SCREW
        SCREW_Label = QtWidgets.QLabel(self)
        SCREW_Label.setText(" -  S C R E W   /   B O L T  - ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            SCREW_Label.setFont(QtGui.QFont('Candara', 8))
        else:
            SCREW_Label.setFont(QtGui.QFont('Candara', 7))

        SCREW_Label.setAlignment(QtCore.Qt.AlignCenter)
        SECTION_PLACEMENT_LAYOUT.addWidget(SCREW_Label)
        SECTION_PLACEMENT_LAYOUT.addSpacing(5)

        ###---------------------------------------------------- H LAYOUT
        Parameters_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_PLACEMENT_LAYOUT.addLayout(Parameters_Hlyt)



        ###-------------------------------------------------------------------------------------------------- DRAG MODE
        self.ImportDrag_btn = QtWidgets.QPushButton()
        self.ImportDrag_btn.setObjectName("TABSBTN")
        self.ImportDrag_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ImportDrag_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ImportDrag_btn.clicked.connect(self.set_DragMode)
        Parameters_Hlyt.addWidget(self.ImportDrag_btn)


        ###-------------------------------------------------------------------------------------------------- FACE MODE
        self.ImportComponent_btn = QtWidgets.QPushButton()
        self.ImportComponent_btn.setObjectName("TABSBTN")
        self.ImportComponent_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ImportComponent_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ImportComponent_btn.clicked.connect(self.set_FaceMode)
        Parameters_Hlyt.addWidget(self.ImportComponent_btn)

        if SCREW_MODE == 1:
            self.ImportDrag_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Drag.png"))
            self.ImportComponent_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Selection_OFF.png"))
        else:
            self.ImportDrag_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Drag_OFF.png"))
            self.ImportComponent_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Selection.png"))




        #####---------------------------------------------------- / SEPARATOR /
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(26, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        Parameters_Hlyt.addWidget(self.Separator)



        ###-------------------------------------------------------------------------------------------------- SIZE SLIDER
        Size_Title = QtWidgets.QLabel("Size ")
        Parameters_Hlyt.addWidget(Size_Title)

        self.Size_Slider = QtWidgets.QSlider()
        self.Size_Slider.setMinimum(0.01)
        self.Size_Slider.setMaximum(100)
        self.Size_Slider.setProperty("value", SCREW_SIZE)
        self.Size_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Size_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Size_Slider.setTickInterval(1)
        self.Size_Slider.setFixedHeight(22)
        self.Size_Slider.valueChanged.connect(self.set_MultiSize_Slider)
        Parameters_Hlyt.addWidget(self.Size_Slider)


        self.Size_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Size_SpinBox.setDecimals(2)
        self.Size_SpinBox.setFixedWidth(40)
        self.Size_SpinBox.setFixedHeight(18)
        self.Size_SpinBox.setRange(0.01, 1000)
        self.Size_SpinBox.setValue(SCREW_SIZE)
        self.Size_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Size_SpinBox.editingFinished.connect(self.set_MultiSize_SpinBox)
        Parameters_Hlyt.addWidget(self.Size_SpinBox)

        SECTION_PLACEMENT_LAYOUT.addSpacing(5)


        ##---------------------------------------------------- Separator
        SECTION_PLACEMENT_LAYOUT.addSpacing(3)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #282828;}")
        separator.setMaximumHeight(2)
        SECTION_PLACEMENT_LAYOUT.addWidget(separator)
        SECTION_PLACEMENT_LAYOUT.addSpacing(3)




        ##--------------------------------------------------
        ##----------------------------------------------------------/ S C R E W   /  B O L T S
        ##--------------------------------------------------
        separatorSpacingValue = 3

        Screw_PNGList = []
        Bolt_PNGList = []
        Special_PNGList = []
        SciFi_PNGList = []

        ##----------------------------------------------------------/  S C R E W
        Screw_Base_path = RessourcePath + "Mesh/Screw"
        listAllInFolder = os.listdir(Screw_Base_path)

        for each in listAllInFolder:
            full_screw_filePath = Screw_Base_path + "/" + each
            #Find and keep only .png files
            if full_screw_filePath.endswith(".png"):
                Screw_PNGList.append(full_screw_filePath)

        grid_Lyt = QtWidgets.QGridLayout()
        SECTION_PLACEMENT_LAYOUT.addLayout(grid_Lyt)

        gridIconSize = 40
        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Screw_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Screw_PNGList.index(each)]
            yPos = positions[Screw_PNGList.index(each)]
            self.Asset_btn = QtWidgets.QPushButton()
            self.Asset_btn.setFixedSize(gridIconSize, gridIconSize)
            self.Asset_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.Asset_btn.setIcon(QtGui.QIcon(each))
            self.Asset_btn.clicked.connect(partial(self.set_Import, Asset_ma_path))
            grid_Lyt.addWidget(self.Asset_btn, xPos[0], yPos[1])


        ##---------------------------------------------------- Separator
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #666; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        SECTION_PLACEMENT_LAYOUT.addWidget(separator)
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)

        ##----------------------------------------------------------/  B O L T S
        Bolt_Base_path = RessourcePath + "Mesh/Bolt"
        listAllInFolder = os.listdir(Bolt_Base_path)

        for each in listAllInFolder:
            full_Bolt_filePath = Bolt_Base_path + "/" + each
            #Find and keep only .png files
            if full_Bolt_filePath.endswith(".png"):
                Bolt_PNGList.append(full_Bolt_filePath)

        grid_Lyt = QtWidgets.QGridLayout()
        SECTION_PLACEMENT_LAYOUT.addLayout(grid_Lyt)

        gridIconSize = 40
        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Bolt_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Bolt_PNGList.index(each)]
            yPos = positions[Bolt_PNGList.index(each)]
            self.Asset_btn = QtWidgets.QPushButton()
            self.Asset_btn.setFixedSize(gridIconSize, gridIconSize)
            self.Asset_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.Asset_btn.setIcon(QtGui.QIcon(each))
            self.Asset_btn.clicked.connect(partial(self.set_Import, Asset_ma_path))
            grid_Lyt.addWidget(self.Asset_btn, xPos[0], yPos[1])

        ##---------------------------------------------------- Separator
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #666; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        SECTION_PLACEMENT_LAYOUT.addWidget(separator)
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)



        ##----------------------------------------------------------/  S C I - F I
        SciFi_Base_path = RessourcePath + "Mesh/SciFi"
        listAllInFolder = os.listdir(SciFi_Base_path)

        for each in listAllInFolder:
            full_SciFi_filePath = SciFi_Base_path + "/" + each
            #Find and keep only .png files
            if full_SciFi_filePath.endswith(".png"):
                SciFi_PNGList.append(full_SciFi_filePath)

        grid_Lyt = QtWidgets.QGridLayout()
        SECTION_PLACEMENT_LAYOUT.addLayout(grid_Lyt)

        gridIconSize = 40
        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in SciFi_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[SciFi_PNGList.index(each)]
            yPos = positions[SciFi_PNGList.index(each)]
            self.Asset_btn = QtWidgets.QPushButton()
            self.Asset_btn.setFixedSize(gridIconSize, gridIconSize)
            self.Asset_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.Asset_btn.setIcon(QtGui.QIcon(each))
            self.Asset_btn.clicked.connect(partial(self.set_Import, Asset_ma_path))
            grid_Lyt.addWidget(self.Asset_btn, xPos[0], yPos[1])


        ##---------------------------------------------------- Separator
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #666; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        SECTION_PLACEMENT_LAYOUT.addWidget(separator)
        SECTION_PLACEMENT_LAYOUT.addSpacing(separatorSpacingValue)


        ##----------------------------------------------------------/  S P E C I A L S
        Special_Base_path = RessourcePath + "Mesh/Special"
        listAllInFolder = os.listdir(Special_Base_path)

        for each in listAllInFolder:
            full_Special_filePath = Special_Base_path + "/" + each
            #Find and keep only .png files
            if full_Special_filePath.endswith(".png"):
                Special_PNGList.append(full_Special_filePath)

        grid_Lyt = QtWidgets.QGridLayout()
        SECTION_PLACEMENT_LAYOUT.addLayout(grid_Lyt)

        gridIconSize = 40
        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Special_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Special_PNGList.index(each)]
            yPos = positions[Special_PNGList.index(each)]
            self.Asset_btn = QtWidgets.QPushButton()
            self.Asset_btn.setFixedSize(gridIconSize, gridIconSize)
            self.Asset_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.Asset_btn.setIcon(QtGui.QIcon(each))
            self.Asset_btn.clicked.connect(partial(self.set_Import, Asset_ma_path))
            grid_Lyt.addWidget(self.Asset_btn, xPos[0], yPos[1])






        self.AssetItPromo_btn = QtWidgets.QPushButton("-  C u s t o m   B o l t  -")
        self.AssetItPromo_btn.setObjectName("StoreSet")
        self.AssetItPromo_btn.setFixedHeight(18)
        self.AssetItPromo_btn.setStyleSheet("color:#808080;")
        if WIN_DISPLAY_SIZE == 1: #150
            self.AssetItPromo_btn.setFont(QtGui.QFont('Calibri', 6))
        self.AssetItPromo_btn.clicked.connect(self.AssetItPromo)
        SECTION_PLACEMENT_LAYOUT.addWidget(self.AssetItPromo_btn)






    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------
    def AssetItPromo(self):
        from . import ModIt_AssetIt
        importlib.reload(ModIt_AssetIt)
        ModIt_AssetIt.showUI()


    def set_DragMode(self):
        self.ImportDrag_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Drag.png"))
        self.ImportComponent_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Selection_OFF.png"))
        open(PreferencePath + 'Screw_Mode.json', "w").write(json.dumps({"VALUE": 1}))

    def set_FaceMode(self):
        self.ImportDrag_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Drag_OFF.png"))
        self.ImportComponent_btn.setIcon(QtGui.QIcon(IconPath + "Placement_Selection.png"))
        open(PreferencePath + 'Screw_Mode.json', "w").write(json.dumps({"VALUE": 2}))






    def set_MultiSize_Slider(self):
        SliderValue = self.Size_Slider.value()
        self.Size_SpinBox.setValue(SliderValue)


    def set_MultiSize_SpinBox(self):
        SpinBoxAValue = self.Size_SpinBox.value()
        self.Size_Slider.setValue(SpinBoxAValue)
        self.Size_SpinBox.clearFocus()
        open(PreferencePath + 'MultiSize.json', "w").write(json.dumps({"MULTISIZEVALUE": SpinBoxAValue}))





    def set_Import(self, maPath):
        SCREW_MODE = (json.load(open(PreferencePath + 'Screw_Mode.json', "r"))['VALUE'])

        if SCREW_MODE == 1:
            #VERIF THERE IS A MESH
            listAllGeometrieScene = cmds.ls(type="mesh")
            if listAllGeometrieScene == []:
                ModIt_Global.WarningWindow("Drag Placement mode need at least one mesh in the scene.", 350)
                return

            from . import ModIt_DragTool
            importlib.reload(ModIt_DragTool)
            ModIt_DragTool.goPress(maPath)

        else:
            SaveSize_pref = json.load(open(PreferencePath + 'MultiSize.json', "r"))
            MULTISIZEVALUE = (SaveSize_pref['MULTISIZEVALUE'])


            selectionCheck = cmds.ls(sl=True)
            if selectionCheck == []:
                ModIt_Global.WarningWindow("On 'Place at Selection' mode : you should select component first.", 350)
                return

            cmds.setToolTo('moveSuperContext')
            pos = cmds.manipMoveContext('Move', query=True, position=True)
            selection = cmds.ls(selection=True, l=True)

            ##_________________IMPORT L'ASSET
            before = set(cmds.ls(assemblies=True))
            cmds.file(maPath , i=True)

            after = set(cmds.ls(assemblies=True))
            imported = after.difference(before)
            cmds.select(imported)
            objImported = cmds.ls(sl=True)[0]


            cmds.setAttr(objImported + ".scaleX", MULTISIZEVALUE)
            cmds.setAttr(objImported + ".scaleY", MULTISIZEVALUE)
            cmds.setAttr(objImported + ".scaleZ", MULTISIZEVALUE)
            cmds.select(objImported)
            cmds.makeIdentity(apply=True)

            cmds.select(objImported)
            cmds.makeIdentity(apply=True)
            cmds.xform(ws=1, a=1, piv=[0, 0, 0])

            cmds.move(pos[0], pos[1], pos[2], objImported)
            constr = cmds.normalConstraint(selection, objImported, aimVector=(0, 1, 0), worldUpType=0)
            cmds.delete(constr)

            cmds.select(objImported)
            cmds.setToolTo('moveSuperContext')




