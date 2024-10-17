##--------------------------------------------------------------------------
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
import mtoa.core as core
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

WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])


# ******************************************
#           PARAMS
# ******************************************
iconFixeSize = 32
iconButtonSize = 30
class MyCustomBtn_Widget(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == QtCore.Qt.RightButton:
          # emit the signal, we can grab the pos directly from the event, no need to get cursor position anymore
          self.customContextMenuRequested.emit(event.pos())
          # make a call to mouseRelease event to restore button back to its original state
          self.mouseReleaseEvent(event)



class SHADING_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


        SECTION_SHADING_LAYOUT = QtWidgets.QVBoxLayout()  #_______ MAIN
        SECTION_SHADING_LAYOUT.setContentsMargins(0, 0, 0, 0)
        SECTION_SHADING_LAYOUT.setSpacing(0)
        self.setLayout(SECTION_SHADING_LAYOUT)

        TOOLBAR_Hlyt = QtWidgets.QHBoxLayout() #_______ TOOLBAR
        TOOLBAR_Hlyt.setContentsMargins(0,0,0,0)
        TOOLBAR_Hlyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(TOOLBAR_Hlyt)



        ##----------------------------------------------------------------------------------------   T O O L B A R
        ##----------------------------------------------------------------------- LIGHTING
        TOOLBAR_Hlyt.addSpacing(5)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,26)
        self.Separator.setStyleSheet("background-color:#fba636;")
        TOOLBAR_Hlyt.addWidget(self.Separator)
        TOOLBAR_Hlyt.addSpacing(5)


        self.Hdri_btn = MyCustomBtn_Widget()
        self.Hdri_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.Hdri_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Hdri_btn.setIcon(QtGui.QIcon(IconPath + "VP_Hdri.png"))
        self.Hdri_btn.setToolTip(" Import an HDR Viewport Lighting Preset / Shift+Click : Select HDR ")
        self.Hdri_btn.clicked.connect(partial(self.loadHDR, 1))
        TOOLBAR_Hlyt.addWidget(self.Hdri_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.Hdri_btn.customContextMenuRequested.connect(self.showPopupHDR)
        #   CUBE M E N U   I T E M S
        self.popupMenuHDR = QtWidgets.QMenu()
        HDRI_1 = self.popupMenuHDR.addAction("HDR 1 -  LookDev")
        HDRI_1.triggered.connect(partial(self.loadHDR, 1))
        HDRI_2 = self.popupMenuHDR.addAction("HDR 2 -  Studio")
        HDRI_2.triggered.connect(partial(self.loadHDR, 2))
        HDRI_3 = self.popupMenuHDR.addAction("HDR 3 -  Studio SpotLights")
        HDRI_3.triggered.connect(partial(self.loadHDR, 3))
        HDRI_4 = self.popupMenuHDR.addAction("HDR 4 -  Garden")
        HDRI_4.triggered.connect(partial(self.loadHDR, 4))
        HDRI_5 = self.popupMenuHDR.addAction("HDR 5 -  Parking")
        HDRI_5.triggered.connect(partial(self.loadHDR, 5))
        HDRI_6 = self.popupMenuHDR.addAction("HDR 6 -  Exterior")
        HDRI_6.triggered.connect(partial(self.loadHDR, 6))





        self.LightsOff_btn = MyCustomBtn_Widget()
        self.LightsOff_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.LightsOff_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.LightsOff_btn.setIcon(QtGui.QIcon(IconPath + "VP_Lights.png"))
        self.LightsOff_btn.setToolTip("  Turn ON / OFF Viewport Lighting  ")
        self.LightsOff_btn.clicked.connect(self.lightONOFF)
        TOOLBAR_Hlyt.addWidget(self.LightsOff_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.LightsOff_btn.customContextMenuRequested.connect(self.showPopupLight)
        #   CUBE M E N U   I T E M S
        self.popupMenuLight = QtWidgets.QMenu()
        GroundShadow = self.popupMenuLight.addAction(" Import Ground Shadow")
        GroundShadow.triggered.connect(self.importShadowsGround)


        ##----------------------------------------------------------------------- UVS
        TOOLBAR_Hlyt.addSpacing(5)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,26)
        self.Separator.setStyleSheet("background-color:#53c48d;")
        TOOLBAR_Hlyt.addWidget(self.Separator)
        TOOLBAR_Hlyt.addSpacing(5)

        self.UvShader_btn = QtWidgets.QPushButton()
        self.UvShader_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.UvShader_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.UvShader_btn.setIcon(QtGui.QIcon(IconPath + "VP_UvShader.png"))
        self.UvShader_btn.setToolTip("  UVs Shader / Shift+Click = Tiled Attributs  ")
        self.UvShader_btn.clicked.connect(self.UVShader)
        TOOLBAR_Hlyt.addWidget(self.UvShader_btn)



        self.UvAuto_btn = QtWidgets.QPushButton()
        self.UvAuto_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.UvAuto_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.UvAuto_btn.setIcon(QtGui.QIcon(IconPath + "VP_Auto.png"))
        self.UvAuto_btn.setToolTip(" Automatic UVs on selected meshes ")
        self.UvAuto_btn.clicked.connect(self.AutoUv)
        TOOLBAR_Hlyt.addWidget(self.UvAuto_btn)

        self.UvPlanar_btn = MyCustomBtn_Widget()
        self.UvPlanar_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.UvPlanar_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.UvPlanar_btn.setIcon(QtGui.QIcon(IconPath + "VP_Planar.png"))
        self.UvPlanar_btn.setToolTip(" Planar UV Projection - Camera  ")
        self.UvPlanar_btn.clicked.connect(partial(self.PlanarUV, 0))
        TOOLBAR_Hlyt.addWidget(self.UvPlanar_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.UvPlanar_btn.customContextMenuRequested.connect(self.showPopupPlanar)
        #   CUBE M E N U   I T E M S
        self.popupMenuPlanar = QtWidgets.QMenu()
        Planar_Entry_X = self.popupMenuPlanar.addAction(" Planar Proj -   X")
        Planar_Entry_X.triggered.connect(partial(self.PlanarUV, 1))
        Planar_Entry_Y = self.popupMenuPlanar.addAction(" Planar Proj -   Y")
        Planar_Entry_Y.triggered.connect(partial(self.PlanarUV, 2))
        Planar_Entry_Z = self.popupMenuPlanar.addAction(" Planar Proj -   Z")
        Planar_Entry_Z.triggered.connect(partial(self.PlanarUV, 3))




        ##----------------------------------------------------------------------- SHADER
        TOOLBAR_Hlyt.addSpacing(5)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,26)
        self.Separator.setStyleSheet("background-color:#3fa6c5;")
        TOOLBAR_Hlyt.addWidget(self.Separator)
        TOOLBAR_Hlyt.addSpacing(5)


        self.ShaderAttribut_btn = QtWidgets.QPushButton()
        self.ShaderAttribut_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ShaderAttribut_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ShaderAttribut_btn.setIcon(QtGui.QIcon(IconPath + "VP_GetShader.png"))
        self.ShaderAttribut_btn.setToolTip("  Get Shader Attributs from Selected Mesh  ")
        self.ShaderAttribut_btn.clicked.connect(self.Get_ShaderAttributs)
        TOOLBAR_Hlyt.addWidget(self.ShaderAttribut_btn)








        ##--------------------------------------------------------------------------------------------------   S H A D E R S
        ##-----------------------------------------------------------------------  S I M P L E - Title
        SECTION_SHADING_LAYOUT.addSpacing(8)
        Simple_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SHADING_LAYOUT.addLayout(Simple_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Simple_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" S I M P L E ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            MODELING_label.setFont(QtGui.QFont('Candara', 8))
        else:
            MODELING_label.setFont(QtGui.QFont('Candara', 7))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Simple_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Simple_Title_Hlyt.addWidget(separator)
        SECTION_SHADING_LAYOUT.addSpacing(6)

        ##----------------------------------------------------------------------- S I M P L E - Shaders
        Simple_PNGList = []
        gridIconContainerSize = 44
        gridIconSize = 46

        Simple_Base_path = RessourcePath + "Shader/Simple"
        listAllInFolder = os.listdir(Simple_Base_path)

        for each in listAllInFolder:
            full_Simple_filePath = Simple_Base_path + "/" + each
            #Find and keep only .png files
            if full_Simple_filePath.endswith(".png"):
                Simple_PNGList.append(full_Simple_filePath)

        grid_Lyt = QtWidgets.QGridLayout()
        grid_Lyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(grid_Lyt)


        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Simple_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Simple_PNGList.index(each)]
            yPos = positions[Simple_PNGList.index(each)]
            self.SimpleShd_btn = QtWidgets.QPushButton()
            self.SimpleShd_btn.setFixedSize(gridIconContainerSize, gridIconContainerSize)
            self.SimpleShd_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.SimpleShd_btn.setIcon(QtGui.QIcon(each))
            self.SimpleShd_btn.setToolTip(" Shift + Click : Shader Attibuts")
            self.SimpleShd_btn.clicked.connect(partial(self.Import_Shader, Asset_ma_path))

            grid_Lyt.addWidget(self.SimpleShd_btn, xPos[0], yPos[1])


        ##----------------------------------------------------------------------- P L A S T I C - Title
        SECTION_SHADING_LAYOUT.addSpacing(8)
        Plastic_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SHADING_LAYOUT.addLayout(Plastic_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Plastic_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" P L A S T I C ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            MODELING_label.setFont(QtGui.QFont('Candara', 8))
        else:
            MODELING_label.setFont(QtGui.QFont('Candara', 7))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Plastic_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Plastic_Title_Hlyt.addWidget(separator)
        SECTION_SHADING_LAYOUT.addSpacing(6)
        ##----------------------------------------------------------------------- P L A S T I C - Shaders
        gridIconContainerSize = 44
        gridIconSize = 46

        Plastic_PNGList = []
        Plastic_Base_path = RessourcePath + "Shader/Plastic"
        listAllInFolder = os.listdir(Plastic_Base_path)

        for each in listAllInFolder:
            full_Plastic_filePath = Plastic_Base_path + "/" + each
            #Find and keep only .png files
            if full_Plastic_filePath.endswith(".png"):
                Plastic_PNGList.append(full_Plastic_filePath)

        Simple_Grid_Lyt = QtWidgets.QGridLayout()
        Simple_Grid_Lyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(Simple_Grid_Lyt)

        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Plastic_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Plastic_PNGList.index(each)]
            yPos = positions[Plastic_PNGList.index(each)]
            self.Asset_btn = QtWidgets.QPushButton()
            self.Asset_btn.setFixedSize(gridIconContainerSize, gridIconContainerSize)
            self.Asset_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.Asset_btn.setIcon(QtGui.QIcon(each))
            self.Asset_btn.setToolTip(" Shift + Click : Shader Attibuts")
            self.Asset_btn.clicked.connect(partial(self.Import_Shader, Asset_ma_path))
            Simple_Grid_Lyt.addWidget(self.Asset_btn, xPos[0], yPos[1])




        ##----------------------------------------------------------------------- M E T A L - Title
        SECTION_SHADING_LAYOUT.addSpacing(8)
        Metal_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SHADING_LAYOUT.addLayout(Metal_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Metal_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" M E T A L ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            MODELING_label.setFont(QtGui.QFont('Candara', 8))
        else:
            MODELING_label.setFont(QtGui.QFont('Candara', 7))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Metal_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Metal_Title_Hlyt.addWidget(separator)
        SECTION_SHADING_LAYOUT.addSpacing(6)
        ##----------------------------------------------------------------------- M E T A L - Shaders
        Metal_PNGList = []

        Metal_Base_path = RessourcePath + "Shader/Metal"
        listAllInFolder = os.listdir(Metal_Base_path)

        for each in listAllInFolder:
            full_Metal_filePath = Metal_Base_path + "/" + each
            #Find and keep only .png files
            if full_Metal_filePath.endswith(".png"):
                Metal_PNGList.append(full_Metal_filePath)

        Metal_Grid_Lyt = QtWidgets.QGridLayout()
        Metal_Grid_Lyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(Metal_Grid_Lyt)


        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Metal_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Metal_PNGList.index(each)]
            yPos = positions[Metal_PNGList.index(each)]
            self.MetalShd_btn = QtWidgets.QPushButton()
            self.MetalShd_btn.setFixedSize(gridIconContainerSize, gridIconContainerSize)
            self.MetalShd_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.MetalShd_btn.setIcon(QtGui.QIcon(each))
            self.MetalShd_btn.setToolTip(" Shift + Click : Shader Attibuts")
            self.MetalShd_btn.clicked.connect(partial(self.Import_Shader, Asset_ma_path))

            Metal_Grid_Lyt.addWidget(self.MetalShd_btn, xPos[0], yPos[1])



        ##----------------------------------------------------------------------- G L A S S - Title
        SECTION_SHADING_LAYOUT.addSpacing(8)
        Glass_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SHADING_LAYOUT.addLayout(Glass_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Glass_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" G L A S S ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            MODELING_label.setFont(QtGui.QFont('Candara', 8))
        else:
            MODELING_label.setFont(QtGui.QFont('Candara', 7))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Glass_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Glass_Title_Hlyt.addWidget(separator)
        SECTION_SHADING_LAYOUT.addSpacing(6)

        ##----------------------------------------------------------------------- G L A S S - Shaders
        Glass_PNGList = []

        Glass_Base_path = RessourcePath + "Shader/Glass"
        listAllInFolder = os.listdir(Glass_Base_path)

        for each in listAllInFolder:
            full_Glass_filePath = Glass_Base_path + "/" + each
            #Find and keep only .png files
            if full_Glass_filePath.endswith(".png"):
                Glass_PNGList.append(full_Glass_filePath)

        Glass_Grid_Lyt = QtWidgets.QGridLayout()
        Glass_Grid_Lyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(Glass_Grid_Lyt)

        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Glass_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Glass_PNGList.index(each)]
            yPos = positions[Glass_PNGList.index(each)]
            self.GlassShd_btn = QtWidgets.QPushButton()
            self.GlassShd_btn.setFixedSize(gridIconContainerSize, gridIconContainerSize)
            self.GlassShd_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.GlassShd_btn.setIcon(QtGui.QIcon(each))
            self.GlassShd_btn.setToolTip(" Shift + Click : Shader Attibuts")
            self.GlassShd_btn.clicked.connect(partial(self.Import_Shader, Asset_ma_path))
            Glass_Grid_Lyt.addWidget(self.GlassShd_btn, xPos[0], yPos[1])


        ##----------------------------------------------------------------------- P L A T E - Title
        SECTION_SHADING_LAYOUT.addSpacing(8)
        Plate_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SHADING_LAYOUT.addLayout(Plate_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Plate_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" P L A T E ")
        if WIN_DISPLAY_SIZE == 0:  # 125
            MODELING_label.setFont(QtGui.QFont('Candara', 8))
        else:
            MODELING_label.setFont(QtGui.QFont('Candara', 7))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Plate_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Plate_Title_Hlyt.addWidget(separator)
        SECTION_SHADING_LAYOUT.addSpacing(6)
        ##----------------------------------------------------------------------- P L A T E - Shaders
        Plate_PNGList = []

        Plate_Base_path = RessourcePath + "Shader/Plate"
        listAllInFolder = os.listdir(Plate_Base_path)

        for each in listAllInFolder:
            full_Plate_filePath = Plate_Base_path + "/" + each
            #Find and keep only .png files
            if full_Plate_filePath.endswith(".png"):
                Plate_PNGList.append(full_Plate_filePath)

        Plate_Grid_Lyt = QtWidgets.QGridLayout()
        Plate_Grid_Lyt.setSpacing(0)
        SECTION_SHADING_LAYOUT.addLayout(Plate_Grid_Lyt)


        positions = [(x, y) for x in range(10) for y in range(6)]
        for each in Plate_PNGList:
            Asset_ma_path = each.replace(".png", ".ma")
            xPos = positions[Plate_PNGList.index(each)]
            yPos = positions[Plate_PNGList.index(each)]
            self.PlateShd_btn = QtWidgets.QPushButton()
            self.PlateShd_btn.setFixedSize(gridIconContainerSize, gridIconContainerSize)
            self.PlateShd_btn.setIconSize(QtCore.QSize(gridIconSize, gridIconSize))
            self.PlateShd_btn.setIcon(QtGui.QIcon(each))
            self.PlateShd_btn.setToolTip( " Shift + Click : Shader Attibuts")
            self.PlateShd_btn.clicked.connect(partial(self.Import_Shader, Asset_ma_path))

            Plate_Grid_Lyt.addWidget(self.PlateShd_btn, xPos[0], yPos[1])

    #----------------------------------------------------------------
    ##------------------------------------------------------------------------------------   D E F I N I T I O N
    #----------------------------------------------------------------


    def BAM(self, name):
        print("BAMMM  " + name)

    
    def Import_Shader(self, shdPath):
        shaderName = str(shdPath.split("/")[-1].replace(".ma", ""))
        selection = mc.ls(sl = True)
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        shaderAttributPopUp = (json.load(open(PreferencePath + 'ShaderAttributs.json', "r"))['VALUE'])

        # Turn ON Texture VP
        panel = cmds.getPanel(withFocus=True)
        # This happens when last focus was on panel
        # that got deleted (e.g. `capture()` then `parse_active_view()`)
        if not panel or "modelPanel" not in panel:
            raise RuntimeError("No active model panel found")
        mc.modelEditor(panel, e=1, displayTextures=1)
        mc.modelEditor(panel, e=1, udm=0)

        if selection == []:
            if mc.objExists(shaderName):
                #mc.select(shaderName)
                mel.eval('commitAENotes($gAECurrentTab);showEditorExact"' +  shaderName + '";')
                if shaderAttributPopUp == 1:
                    mel.eval("commitAENotes($gAECurrentTab);copyAEWindow;")
            else:
                ModIt_Global.WarningWindow(" You should select a Mesh first.", 300)
                return
        else:
            if modifiers == QtCore.Qt.ShiftModifier:
                if mc.objExists(shaderName):
                    # mc.select(shaderName)
                    mel.eval('commitAENotes($gAECurrentTab);showEditorExact"' + shaderName + '";')
                    if shaderAttributPopUp == 1:
                        mel.eval("commitAENotes($gAECurrentTab);copyAEWindow;")
                else:
                    mc.file(shdPath, i=True)
                    mc.select(selection)
                    mc.hyperShade(a=shaderName)
                    mel.eval('commitAENotes($gAECurrentTab);showEditorExact"' + shaderName + '";')
                    if shaderAttributPopUp == 1:
                        mel.eval("commitAENotes($gAECurrentTab);copyAEWindow;")
            else:
                if mc.objExists(shaderName):
                    mc.hyperShade(a= shaderName)

                else:
                    mc.file(shdPath, i=True)
                    mc.select(selection)
                    mc.hyperShade(a=shaderName)


    def Get_ShaderAttributs(self):
        theNodes = mc.ls(sl=True, dag=True, s=True)
        if theNodes == []:
            ModIt_Global.WarningWindow(" You should select a Mesh first.", 300)
            return
        else:
            shadeEng = mc.listConnections(theNodes, type="shadingEngine")
            materials = mc.ls(mc.listConnections(shadeEng), materials=True, hd=1)
            mc.select(materials)
            print("MATERAIL = "  + str(materials))
            mel.eval('commitAENotes($gAECurrentTab);showEditorExact"' + str(materials[0]) + '";')
            shaderAttributPopUp = (json.load(open(PreferencePath + 'ShaderAttributs.json', "r"))['VALUE'])
            if shaderAttributPopUp == 1:
                mel.eval("commitAENotes($gAECurrentTab);copyAEWindow;")


    def UVShader(self):
        shaderPath = RessourcePath + "/Shader/ModIt_UVs_shd.ma"
        shaderName = "ModIt_Uvs_shd"
        selection = mc.ls(sl=True, fl=True, dag=True)
        modifiers = QtWidgets.QApplication.keyboardModifiers()

        # Turn ON Texture VP
        panel = cmds.getPanel(withFocus=True)
        # This happens when last focus was on panel
        # that got deleted (e.g. `capture()` then `parse_active_view()`)
        if not panel or "modelPanel" not in panel:
            raise RuntimeError("No active model panel found")
        mc.modelEditor(panel, e=1, displayTextures=1)
        mc.modelEditor(panel, e=1, udm=0)

        if selection == []:
            if mc.objExists(shaderName):
                if mc.window("UvShader_Edit_FloatWindows", exists=True):
                    mc.deleteUI("UvShader_Edit_FloatWindows")

                get_U_value = mc.getAttr("ModIt_Uvs_scale.repeatU")
                get_V_value = mc.getAttr("ModIt_Uvs_scale.repeatV")

                mc.window("UvShader_Edit_FloatWindows", title='UV Shader Tile', s=True, w=500)
                mc.columnLayout(adj=True, w=400)
                mc.separator(h=5, style='none')
                mc.floatSliderGrp('Slider_U_Tile', l= " U Tile ", minValue=0.1, max=10, po=True, field=True, dc= self.set_U_value, v=get_U_value, adj=0, cat=[1, "left", 3], cw=[1, 45])
                mc.floatSliderGrp('Slider_V_Tile', l= " V Tile ", minValue=0.1, max=10, po=True, field=True, dc= self.set_V_value, v=get_V_value, adj=0, cat=[1, "left", 3], cw=[1, 45])
                mc.separator(h=5, style='none')
                mc.showWindow()

            else:
                ModIt_Global.WarningWindow(" You should select a Mesh first.", 300)
                return

        else:
            if modifiers == QtCore.Qt.ShiftModifier:
                if mc.objExists(shaderName):
                    if mc.window("UvShader_Edit_FloatWindows", exists=True):
                        mc.deleteUI("UvShader_Edit_FloatWindows")

                    get_U_value = mc.getAttr("ModIt_Uvs_scale.repeatU")
                    get_V_value = mc.getAttr("ModIt_Uvs_scale.repeatV")

                    mc.window("UvShader_Edit_FloatWindows", title='UV Shader Tile', s=True, w=500)
                    mc.columnLayout(adj=True, w=400)
                    mc.separator(h=5, style='none')
                    mc.floatSliderGrp('Slider_U_Tile', l="- U Tile ", minValue=0.1, maxValue=10, po=True, field=True, dc=self.set_U_value,
                                    v=get_U_value, adj=0, cat=[1, "left", 3], cw=[1, 45])
                    mc.floatSliderGrp('Slider_V_Tile', l="- V Tile ", minValue=0.1, maxValue=10, po=True, field=True, dc=self.set_V_value,
                                    v=get_V_value, adj=0, cat=[1, "left", 3], cw=[1, 45])
                    mc.separator(h=5, style='none')
                    mc.showWindow()
                else:
                    pass
            else:
                if mc.objExists(shaderName):
                    mc.hyperShade(a=shaderName)
                else:
                    mc.file(shaderPath, i=True)
                    mc.select(selection)
                    mc.hyperShade(a=shaderName)



    def set_U_value(self, *args):
        myValueWidght = mc.floatSliderGrp("Slider_U_Tile", q=True, value=True)
        mc.setAttr("ModIt_Uvs_scale.repeatU", myValueWidght )

    def set_V_value(self, *args):
        myValueWidght = mc.floatSliderGrp("Slider_V_Tile", q=True, value=True)
        mc.setAttr("ModIt_Uvs_scale.repeatV", myValueWidght)



    def AutoUv(self):
        selection = mc.ls(sl=True, fl=True, dag=True)
        mc.undoInfo(openChunk=True, infinity=True)

        if selection == []:
            print("Warning : You should select a mesh.")
        else:

            mc.FreezeTransformations()
            mc.UVAutomaticProjection()

            mc.select(selection)
            mc.DeleteHistory()
            mc.SelectVertexMask()
            mc.SelectToggleMode()
            mc.setToolTo('moveSuperContext')

        mc.undoInfo(closeChunk=True)

    def PlanarUV(self, modeValue):
        mc.undoInfo(openChunk=True, infinity=True)

        selection = mc.ls(sl=True, fl=True, dag=True, type='mesh')

        if modeValue == 0:
            mode = "c"
        if modeValue == 1:
            mode = "x"
        if modeValue == 2:
            mode = "y"
        if modeValue == 3:
            mode = "z"


        for each in selection:
            mc.DeleteHistory()
            mc.polyProjection(each + '.f[*]', ch=1, type="planar", ibd=True, kir=True, md= mode)
            mc.polyEditUV(pu=0.5, pv=0.5, su=0.5, sv=0.5, u=-0.25, v=0.25)
            mc.select(each)
            mc.DeleteHistory()
            print("Planar UV Done")

        mc.undoInfo(closeChunk=True)


    def showPopupPlanar(self, position):
        self.popupMenuPlanar.exec_(self.UvPlanar_btn.mapToGlobal(position))
        self.UvPlanar_btn.update()

    def showPopupHDR(self, position):
        self.popupMenuHDR.exec_(self.Hdri_btn.mapToGlobal(position))
        self.Hdri_btn.update()

    def showPopupLight(self, position):
        self.popupMenuLight.exec_(self.LightsOff_btn.mapToGlobal(position))
        self.LightsOff_btn.update()


    def lightONOFF(self):
        allPanels = mc.getPanel(type='modelPanel')
        getLightVal = mc.modelEditor(allPanels[-1], q=True, lights=1)
        for each in allPanels:
            if getLightVal == True:
                mc.modelEditor(each, e=1, lights=0)
            else:
                mc.modelEditor(each, e=1, lights=1)

    def importShadowsGround(self):
        groundPath = RessourcePath + "/HDR/Ground_Shadows.ma"
        mc.file(groundPath, i=True)

        # Turn ON Texture VP
        panel = cmds.getPanel(withFocus=True)
        # This happens when last focus was on panel
        # that got deleted (e.g. `capture()` then `parse_active_view()`)
        if not panel or "modelPanel" not in panel:
            raise RuntimeError("No active model panel found")
        mc.modelEditor(panel, e=1, displayTextures=1)
        mc.modelEditor(panel, e=1, udm=0)



    def loadHDR(self, number):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            if mc.objExists('ModIt_HDR_*'):
                mc.select('ModIt_HDR_*')
        else:
            #Turn ON Light and Shadows VP
            panel = cmds.getPanel(withFocus=True)
            # This happens when last focus was on panel
            # that got deleted (e.g. `capture()` then `parse_active_view()`)
            if not panel or "modelPanel" not in panel:
                raise RuntimeError("No active model panel found")
            mc.DisplayLight()
            mc.modelEditor(panel, e=1, shadows=1)


            if mc.objExists('ModIt_HDR_*'):
                mc.delete("ModIt_HDR_*")
            if number == 1:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_1_LookDev.ma"
            elif number == 2:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_2_Studio.ma"
            elif number == 3:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_3_StudioSpotLights.ma"
            elif number == 4:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_4_Garden.ma"
            elif number == 5:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_5_Parking.ma"
            elif number == 6:
                hdrPath = RessourcePath + "/HDR/ModIt_HDR_6_Exterior.ma"


            mc.file(hdrPath, i=True)



