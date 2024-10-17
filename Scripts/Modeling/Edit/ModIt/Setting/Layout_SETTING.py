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

# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 20
iconButtonSize = 20
separatorWidth = ModIt_Global.separatorWidth

##JSON PREF DATA
PRIM_MODE =(json.load(open(PreferencePath + 'Setting_Primitives_Placement.json',"r"))['PRIM_MODE'])
PRIM_SIZE =(json.load(open(PreferencePath + 'Setting_Primitives_Size.json',"r"))['PRIM_SIZE'])
SHADER_ATTRIBUTS = (json.load(open(PreferencePath + 'ShaderAttributs.json',"r"))['VALUE'])
INSTANCE_MODE = (json.load(open(PreferencePath + 'InstanceMode.json',"r"))['VALUE'])
AUTOLOAD = (json.load(open(PreferencePath + 'Autoload.json',"r"))['VALUE'])
LOCATOR_SIZE =(json.load(open(PreferencePath + 'Locator_Size.json',"r"))['VALUE'])
PRIM_TOPOF =(json.load(open(PreferencePath + 'Setting_Primitives_OnTopOf.json',"r"))['VALUE'])

WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])
if WIN_DISPLAY_SIZE == 0:  # 125
    Title_Text_Size = 8
    Text_Size = 7
else: #150
    Title_Text_Size = 7
    Text_Size = 7

DOCK =(json.load(open(PreferencePath + 'Dockable.json',"r"))['VALUE'])


class SETTING_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_SETTING_LAYOUT = QtWidgets.QVBoxLayout()  # MAIN
        self.setLayout(SECTION_SETTING_LAYOUT)
        SECTION_SETTING_LAYOUT.setContentsMargins(0,0,0,0)

        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   G E N E R A L
        ##------------------------------------------------------------------------------------//
        General_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(General_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        General_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" G E N E R A L ")
        MODELING_label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        General_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        General_Title_Hlyt.addWidget(separator)


        ###------------------------------------------------------------------------------------// DOCK FLOATING MODE
        ###---------------------------------------------------- H LAYOUT
        DockMode_Hlyt = QtWidgets.QHBoxLayout()
        DockMode_Hlyt.setSpacing(0)
        SECTION_SETTING_LAYOUT.addLayout(DockMode_Hlyt)

        ###---------------------------------------------------- ICON
        Autosave_img = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "WinDock.png")
        Autosave_img.setPixmap(pixmap)
        DockMode_Hlyt.addWidget(Autosave_img)
        DockMode_Hlyt.addSpacing(5)

        ###---------------------------------------------------- LABEL
        label = QtWidgets.QLabel(self)
        label.setText(" ModIt Mode : ")
        if WIN_DISPLAY_SIZE == 1:  # 125
            label.setFont(QtGui.QFont('Candara', Text_Size))
        DockMode_Hlyt.addWidget(label)
        DockMode_Hlyt.addSpacing(15)

        ###---------------------------------------------------- FLOATING BTN
        DockMode_Btn = QtWidgets.QPushButton()
        DockMode_Btn.setText("Floating")
        DockMode_Btn.clicked.connect(self.set_Floating)

        if DOCK == 0:
            DockMode_Btn.setStyleSheet("QPushButton {color : #29b1ea;}")
            DockMode_Btn.setEnabled(0)
        else:
            DockMode_Btn.setStyleSheet("QPushButton {color : #404040;}")
        DockMode_Hlyt.addWidget(DockMode_Btn)
        DockMode_Hlyt.addSpacing(15)

        ###---------------------------------------------------- DOCK BTN
        FloatingMode_Btn = QtWidgets.QPushButton()
        FloatingMode_Btn.setText("Dockable")
        FloatingMode_Btn.clicked.connect(self.set_Dockable)

        if DOCK == 1:
            FloatingMode_Btn.setStyleSheet("QPushButton {color : #29b1ea;}")
            FloatingMode_Btn.setEnabled(0)
        else:
            FloatingMode_Btn.setStyleSheet("QPushButton {color : #404040;}")

        DockMode_Hlyt.addWidget(FloatingMode_Btn)





        ###------------------------------------------------------------------------------------// DISPLAY SIZE
        ###---------------------------------------------------- H LAYOUT
        DisplaySize_Hlyt = QtWidgets.QHBoxLayout()
        DisplaySize_Hlyt.setSpacing(0)
        SECTION_SETTING_LAYOUT.addLayout(DisplaySize_Hlyt)

        ###---------------------------------------------------- ICON
        Autosave_img = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "WinSize.png")
        Autosave_img.setPixmap(pixmap)
        DisplaySize_Hlyt.addWidget(Autosave_img)
        DisplaySize_Hlyt.addSpacing(5)

        ###---------------------------------------------------- LABEL
        label = QtWidgets.QLabel(self)
        label.setText(" Windows Display Size : ")
        if WIN_DISPLAY_SIZE == 1:  # 125
            label.setFont(QtGui.QFont('Candara', Text_Size))
        DisplaySize_Hlyt.addWidget(label)

        ###---------------------------------------------------- 100% BTN
        Display100_Btn = QtWidgets.QPushButton()
        Display100_Btn.setText("100%")
        Display100_Btn.setFixedWidth(50)
        Display100_Btn.clicked.connect(self.set_WinSize100)
        if WIN_DISPLAY_SIZE == 1:
            Display100_Btn.setStyleSheet( "QPushButton {color : #404040;}")
        else:
            Display100_Btn.setStyleSheet("QPushButton {color : #29b1ea;}")
            Display100_Btn.setEnabled(0)
        DisplaySize_Hlyt.addWidget(Display100_Btn)

        ###---------------------------------------------------- 150% BTN
        Display150_Btn = QtWidgets.QPushButton()
        Display150_Btn.setText("150%")
        Display150_Btn.setFixedWidth(50)
        Display150_Btn.clicked.connect(self.set_WinSize150)
        if WIN_DISPLAY_SIZE == 1:
            Display150_Btn.setStyleSheet( "QPushButton {color : #29b1ea;}")
            Display150_Btn.setEnabled(0)
        else:
            Display150_Btn.setStyleSheet("QPushButton {color : #404040;}")
        DisplaySize_Hlyt.addWidget(Display150_Btn)









        DisplaySize_Hlyt.addStretch()
        DockMode_Hlyt.addStretch()


        ###------------------------------------------------------------------------------------// Attributs PopUp
        ###---------------------------------------------------- H LAYOUT
        Autosave_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Autosave_Hlyt)

        ###---------------------------------------------------- ICON
        Autosave_img = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "saveDisk.png")
        Autosave_img.setPixmap(pixmap)
        Autosave_Hlyt.addWidget(Autosave_img)

        ###---------------------------------------------------- MODE LABEL
        Autosave_label = QtWidgets.QLabel(self)
        Autosave_label.setText(" Open ModIt at launch :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            Autosave_label.setFont(QtGui.QFont('Candara', Text_Size))
        #Autosave_label.setFixedHeight(19)
        Autosave_Hlyt.addWidget(Autosave_label)

        ###---------------------------------------------------- CHECKBOX
        self.Autosave_Cbx = QtWidgets.QCheckBox()
        self.Autosave_Cbx.setFixedSize(20, 20)
        if AUTOLOAD == 0:
            self.Autosave_Cbx.setChecked(0)
        else:
            self.Autosave_Cbx.setChecked(1)
        self.Autosave_Cbx.toggled.connect(self.Autoload_ON_OFF)
        Autosave_Hlyt.addWidget(self.Autosave_Cbx)
        Autosave_Hlyt.addStretch()













        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   M O D E L I N G
        ##------------------------------------------------------------------------------------//
        SECTION_SETTING_LAYOUT.addSpacing(5)
        Modeling_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Modeling_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Modeling_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" M O D E L I N G ")
        MODELING_label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Modeling_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Modeling_Title_Hlyt.addWidget(separator)

        ###------------------------------------------------------------------------------------// Primitives

        Primitive_label = QtWidgets.QLabel(self)
        Primitive_label.setText(" / P r i m i t i v e s ")
        Primitive_label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        #Primitive_label.setAlignment(QtCore.Qt.AlignCenter)
        SECTION_SETTING_LAYOUT.addWidget(Primitive_label)

        ###---------------------------------------------------- INTERACTIVE MODE
        ###---------------------------------------------------- H LAYOUT
        Modeling_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Modeling_Hlyt)

        ###---------------------------------------------------- ICON
        GlobalScaleImg = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "Placement_Drag.png")
        GlobalScaleImg.setPixmap(pixmap)
        Modeling_Hlyt.addWidget(GlobalScaleImg)

        ###---------------------------------------------------- MODE LABEL
        InteractiveMode_label = QtWidgets.QLabel(self)
        InteractiveMode_label.setText("Interactive Mode :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            InteractiveMode_label.setFont(QtGui.QFont('Candara', Text_Size))
        #InteractiveMode_label.setFixedHeight(19)
        Modeling_Hlyt.addWidget(InteractiveMode_label)

        ###---------------------------------------------------- CHECKBOX
        self.InteractivePlacementCbx = QtWidgets.QCheckBox()
        self.InteractivePlacementCbx.setFixedSize(20, 20)
        self.InteractivePlacementCbx.toggled.connect(self.PrimMode_Interactive)
        if PRIM_MODE == 0:
            self.InteractivePlacementCbx.setChecked(0)
        else:
            self.InteractivePlacementCbx.setChecked(1)
        Modeling_Hlyt.addWidget(self.InteractivePlacementCbx)






        ###---------------------------------------------------- ON TOP OF MODE
        ###---------------------------------------------------- H LAYOUT
        OnTopOf_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(OnTopOf_Hlyt)

        ###---------------------------------------------------- ICON
        GlobalScaleImg = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "Prim_OnTopOf.png")
        GlobalScaleImg.setPixmap(pixmap)
        OnTopOf_Hlyt.addWidget(GlobalScaleImg)

        ###---------------------------------------------------- MODE LABEL
        OnTopOf_label = QtWidgets.QLabel(self)
        OnTopOf_label.setText("On Top of Selection :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            OnTopOf_label.setFont(QtGui.QFont('Candara', Text_Size))
        #OnTopOf_label.setFixedHeight(19)
        OnTopOf_Hlyt.addWidget(OnTopOf_label)

        ###---------------------------------------------------- CHECKBOX
        self.OnTopOf_Cbx = QtWidgets.QCheckBox()
        self.OnTopOf_Cbx.setFixedSize(20, 20)
        self.OnTopOf_Cbx.toggled.connect(self.Prim_TopOF)
        if PRIM_TOPOF == 0:
            self.OnTopOf_Cbx.setChecked(0)
        else:
            self.OnTopOf_Cbx.setChecked(1)
        OnTopOf_Hlyt.addWidget(self.OnTopOf_Cbx)
        OnTopOf_Hlyt.addStretch()







        #####---------------------------------------------------- / SEPARATOR /
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(26, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        Modeling_Hlyt.addWidget(self.Separator)


        ## COMBO UNIT // HIDE
        self.UnitComboList = [
            'cm',
            'inch',
        ]

        self.UnitCombo = QtWidgets.QComboBox()
        self.UnitCombo.addItems(self.UnitComboList)
        self.UnitCombo.setFixedWidth(50)
        self.UnitCombo.setFixedHeight(20)
        #self.UnitCombo.currentIndexChanged.connect(self.SET_Theme)
        self.UnitCombo.setCurrentIndex(1)
        #Modeling_Hlyt.addWidget(self.UnitCombo)



        ###---------------------------------------------------- SIZE MULTIPLICATEUR
        SizeM_label = QtWidgets.QLabel(self)
        SizeM_label.setText("Size X :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            SizeM_label.setFont(QtGui.QFont('Candara', Text_Size))
        #SizeM_label.setFixedHeight(19)
        Modeling_Hlyt.addWidget(SizeM_label)

        self.SizeSpinBox = QtWidgets.QDoubleSpinBox()
        self.SizeSpinBox.setDecimals(1)


        self.SizeSpinBox.setFixedWidth(40)
        self.SizeSpinBox.setFixedHeight(23)

        self.SizeSpinBox.setRange(0, 10000)
        self.SizeSpinBox.setValue(PRIM_SIZE)
        self.SizeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.SizeSpinBox.editingFinished.connect(self.set_MultiSize)
        Modeling_Hlyt.addWidget(self.SizeSpinBox)


        SECTION_SETTING_LAYOUT.addSpacing(2)
        Modeling_Hlyt.addStretch()
        Modeling_Hlyt.setSpacing(6)



        ###------------------------------------------------------------------------------------// MESH
        ###---------------------------------------------------- TITLE
        Sym_Label = QtWidgets.QLabel(self)
        Sym_Label.setText(" / M e s h ")
        Sym_Label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        #Sym_Label.setAlignment(QtCore.Qt.AlignCenter)
        SECTION_SETTING_LAYOUT.addWidget(Sym_Label)

        ###---------------------------------------------------- H LAYOUT
        Symmetry_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Symmetry_Hlyt)

        ###---------------------------------------------------- ICON
        GlobalScaleImg = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "Sym_Setting.png")
        GlobalScaleImg.setPixmap(pixmap)
        Symmetry_Hlyt.addWidget(GlobalScaleImg)

        ###---------------------------------------------------- SYM LABEL
        SymetryDefault_label = QtWidgets.QLabel(self)
        SymetryDefault_label.setText("Symmetry Default Axis :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            SymetryDefault_label.setFont(QtGui.QFont('Candara', Text_Size))
        SymetryDefault_label.setFixedHeight(22)
        Symmetry_Hlyt.addWidget(SymetryDefault_label)

        ###---------------------------------------------------- SYM AXIS
        AXIS = (json.load(open(PreferencePath + 'Pref_SymAxis.json', "r"))['VALUE'])

        itemsList = [" X", " Y", " Z"]
        self.SymAxisChoice_combo = QtWidgets.QComboBox(self)
        self.SymAxisChoice_combo.setFixedWidth(35)
        self.SymAxisChoice_combo.setFixedHeight(22)
        self.SymAxisChoice_combo.addItems(itemsList)
        self.SymAxisChoice_combo.setCurrentIndex(AXIS)
        self.SymAxisChoice_combo.currentIndexChanged.connect(self.set_SymAxisChoice)
        Symmetry_Hlyt.addWidget(self.SymAxisChoice_combo)



        ###---------------------------------------------------- INSTANCE BTNcheckable
        self.InstanceMode_btn = QtWidgets.QPushButton("    I N S T A N C E    ")
        self.InstanceMode_btn.setObjectName("StoreSet")
        self.InstanceMode_btn.setFixedHeight(18)
        if INSTANCE_MODE == 0:
            self.InstanceMode_btn.setStyleSheet("color:#808080;")
        else:
            self.InstanceMode_btn.setStyleSheet("color:#29b1ea;")




        if WIN_DISPLAY_SIZE == 1: #150
            self.InstanceMode_btn.setFont(QtGui.QFont('Calibri', 6))
        self.InstanceMode_btn.clicked.connect(self.set_InstanceMode)
        Symmetry_Hlyt.addWidget(self.InstanceMode_btn)








        Symmetry_Hlyt.addStretch()
        SECTION_SETTING_LAYOUT.addSpacing(4)









        ###------------------------------------------------------------------------------------// TOOL
        ###---------------------------------------------------- TITLE
        Tool_Label = QtWidgets.QLabel(self)
        Tool_Label.setText(" / T o o l ")
        Tool_Label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        SECTION_SETTING_LAYOUT.addWidget(Tool_Label)

        ###---------------------------------------------------- H LAYOUT
        Tool_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Tool_Hlyt)

        ###---------------------------------------------------- ICON
        LocatorImg = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "Locator_cible_setting.png")
        LocatorImg.setPixmap(pixmap)
        Tool_Hlyt.addWidget(LocatorImg)

        ###---------------------------------------------------- SIZE MULTIPLICATEUR
        Locator_label = QtWidgets.QLabel(self)
        Locator_label.setText("Size Locators :")
        if WIN_DISPLAY_SIZE == 1:  # 125
            Locator_label.setFont(QtGui.QFont('Candara', Text_Size))
        Tool_Hlyt.addWidget(Locator_label)

        self.LocatorSpinBox = QtWidgets.QDoubleSpinBox()
        self.LocatorSpinBox.setDecimals(1)
        self.LocatorSpinBox.setFixedWidth(40)
        self.LocatorSpinBox.setFixedHeight(23)
        self.LocatorSpinBox.setRange(1, 1000)
        self.LocatorSpinBox.setValue(LOCATOR_SIZE)
        self.LocatorSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.LocatorSpinBox.editingFinished.connect(self.set_LocatorSize)
        Tool_Hlyt.addWidget(self.LocatorSpinBox)


        SECTION_SETTING_LAYOUT.addSpacing(2)
        Tool_Hlyt.addStretch()
        Tool_Hlyt.setSpacing(6)

















        ##------------------------------------------------------------------------------------//
        ##------------------------------------------------------------------------------------------------------//  T A B   S H A D I N G
        ##------------------------------------------------------------------------------------//
        SECTION_SETTING_LAYOUT.addSpacing(5)
        Shading_Title_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Shading_Title_Hlyt)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Shading_Title_Hlyt.addWidget(separator)

        MODELING_label = QtWidgets.QLabel(self)
        MODELING_label.setText(" S H A D I N G ")
        MODELING_label.setFont(QtGui.QFont('Candara', Title_Text_Size))
        MODELING_label.setAlignment(QtCore.Qt.AlignCenter)
        Shading_Title_Hlyt.addWidget(MODELING_label)

        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        Shading_Title_Hlyt.addWidget(separator)

        ###------------------------------------------------------------------------------------// Attributs PopUp
        ###---------------------------------------------------- H LAYOUT
        AE_Hlyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(AE_Hlyt)

        ###---------------------------------------------------- ICON
        ShaderAttrib_img = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(IconPath + "ShaderAttributs.png")
        ShaderAttrib_img.setPixmap(pixmap)
        AE_Hlyt.addWidget(ShaderAttrib_img)

        ###---------------------------------------------------- MODE LABEL
        ShaderAttrib_label = QtWidgets.QLabel(self)
        ShaderAttrib_label.setText("Shader Attributs in Floating Window")
        if WIN_DISPLAY_SIZE == 1:  # 125
            ShaderAttrib_label.setFont(QtGui.QFont('Candara', Text_Size))
        #ShaderAttrib_label.setFixedHeight(19)
        AE_Hlyt.addWidget(ShaderAttrib_label)

        ###---------------------------------------------------- CHECKBOX
        self.ShaderAttrib_Cbx = QtWidgets.QCheckBox()
        self.ShaderAttrib_Cbx.setFixedSize(20, 20)
        self.ShaderAttrib_Cbx.toggled.connect(self.ShaderAttributs_mode)
        if SHADER_ATTRIBUTS == 0:
            self.ShaderAttrib_Cbx.setChecked(0)
        else:
            self.ShaderAttrib_Cbx.setChecked(1)
        AE_Hlyt.addWidget(self.ShaderAttrib_Cbx)


        AE_Hlyt.addStretch()



        ###------------------------------------------------------------------------------------// LINKS
        SECTION_SETTING_LAYOUT.addSpacing(4)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #3e3e3e; padding: 0; margin: 0; border-bottom: 1 solid #848484; border-top: 1 solid #2a2a2a;}")
        separator.setMaximumHeight(2)
        SECTION_SETTING_LAYOUT.addWidget(separator)
        SECTION_SETTING_LAYOUT.addSpacing(4)
        ###---------------------------------------------------- H LAYOUT
        Link_HLyt = QtWidgets.QHBoxLayout()
        SECTION_SETTING_LAYOUT.addLayout(Link_HLyt)

        icoSize = 26


        DiscordBtn = QtWidgets.QPushButton()
        DiscordBtn.setFixedSize(icoSize, icoSize)
        DiscordBtn.setIconSize(QtCore.QSize(icoSize, icoSize))
        DiscordBtn.setIcon(QtGui.QIcon(IconPath + "Discord_ico.png"))
        DiscordBtn.setToolTip("  WZX Discord Link  ")
        DiscordBtn.clicked.connect(self.Link_Discord)
        Link_HLyt.addWidget(DiscordBtn)


        WzxStoreBtn = QtWidgets.QPushButton()
        WzxStoreBtn.setFixedSize(icoSize, icoSize)
        WzxStoreBtn.setIconSize(QtCore.QSize(icoSize, icoSize))
        WzxStoreBtn.setIcon(QtGui.QIcon(IconPath + "WzxStore_ico.png"))
        WzxStoreBtn.setToolTip("  WZXStore Link  ")
        WzxStoreBtn.clicked.connect(self.Link_WzxStore)
        Link_HLyt.addWidget(WzxStoreBtn)















    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------
    def Link_Discord(self):
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("https://discord.com/invite/KpkrvrU"))

    def Link_WzxStore(self):
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("https://www.wzxstore.com/"))




    def set_SymAxisChoice(self):
        AxisChoice = self.SymAxisChoice_combo.currentIndex()
        print(AxisChoice)


        self.SymAxisChoice_combo.clearFocus()
        open(PreferencePath + 'Pref_SymAxis.json', "w").write(json.dumps({"VALUE": AxisChoice}))


    def set_MultiSize(self):
        getSpinValue = self.SizeSpinBox.value()
        self.SizeSpinBox.clearFocus()
        open(PreferencePath + 'Setting_Primitives_Size.json', "w").write(json.dumps({"PRIM_SIZE": getSpinValue}))

    def set_LocatorSize(self):
        getSpinValue = self.LocatorSpinBox.value()
        self.LocatorSpinBox.clearFocus()
        open(PreferencePath + 'Locator_Size.json', "w").write(json.dumps({"VALUE": getSpinValue}))

    def set_WinSize100(self):
        open(PreferencePath + 'WinSize.json', "w").write(json.dumps({"VALUE": 0}))
        from .. import ModIt_LAUNCH
        import importlib
        importlib.reload(ModIt_LAUNCH)


    def set_WinSize150(self):
        open(PreferencePath + 'WinSize.json', "w").write(json.dumps({"VALUE": 1}))
        from .. import ModIt_LAUNCH
        import importlib
        importlib.reload(ModIt_LAUNCH)


    def set_Floating(self):
        open(PreferencePath + 'Dockable.json', "w").write(json.dumps({"VALUE": 0}))
        from .. import ModIt_LAUNCH
        import importlib
        importlib.reload(ModIt_LAUNCH)


    def set_Dockable(self):
        open(PreferencePath + 'Dockable.json', "w").write(json.dumps({"VALUE": 1}))
        from .. import ModIt_LAUNCH
        import importlib
        importlib.reload(ModIt_LAUNCH)

    def set_InstanceMode(self):
        INSTANCE_MODE = (json.load(open(PreferencePath + 'InstanceMode.json', "r"))['VALUE'])

        if INSTANCE_MODE ==0:
            open(PreferencePath + 'InstanceMode.json', "w").write(json.dumps({"VALUE": 1}))
            self.InstanceMode_btn.setStyleSheet("color:#29b1ea;")
        else:
            open(PreferencePath + 'InstanceMode.json', "w").write(json.dumps({"VALUE": 0}))
            self.InstanceMode_btn.setStyleSheet("color:#606060;")


    #------------------------------------------------PRIM MODE

    def PrimMode_Interactive(self, checked):
        if checked == True:
            open(PreferencePath + 'Setting_Primitives_Placement.json', "w").write(json.dumps({"PRIM_MODE": 1}))
        else:
            open(PreferencePath + 'Setting_Primitives_Placement.json', "w").write(json.dumps({"PRIM_MODE": 0}))
            if mc.optionVar(q="createPolyPrimitiveAsTool") == 1:
                mc.ToggleCreatePolyPrimitivesAsTool()
            if mc.optionVar(q="polyPrimitiveAsToolExitOnComplete") == 1:
                mc.TogglePolyPrimitivesAsToolExitOnComplete()

    def Prim_TopOF(self, checked):
        if checked == True:
            open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "w").write(json.dumps({"VALUE": 1}))
        else:
            open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "w").write(json.dumps({"VALUE": 0}))





    def ShaderAttributs_mode(self, checked):
        if checked == True:
            open(PreferencePath + 'ShaderAttributs.json', "w").write(json.dumps({"VALUE": 1}))
        else:
            open(PreferencePath + 'ShaderAttributs.json', "w").write(json.dumps({"VALUE": 0}))





    def Autoload_ON_OFF(self, checked):
        if checked == True:
            open(PreferencePath + 'Autoload.json', "w").write(json.dumps({"VALUE": 1}))

            UserSetupPath = ModIt_Global.UserScriptFolder + "/userSetup.py"

            # Open a file with access mode 'a'
            file_object = open(UserSetupPath, 'a')
            # Append 'hello' at the end of file
            file_object.write("""
import maya.cmds as cmds
def ModItAutoLoad ():
    from ModIt import ModIt_UI
    import importlib
    importlib.reload(ModIt_UI)
    ModIt_UI

cmds.evalDeferred(ModItAutoLoad, lowestPriority=True)""")
            # Close the file
            file_object.close()

        else:
            open(PreferencePath + 'Autoload.json', "w").write(json.dumps({"VALUE": 0}))

            UserSetupPath = ModIt_Global.UserScriptFolder + "/userSetup.py"
            TempFilePAth = ModIt_Global.UserScriptFolder + "/modItTemp.py"
            import os

            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "def ModItAutoLoad ():":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)


            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "cmds.evalDeferred(ModItAutoLoad, lowestPriority=True)":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)


            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "    from ModIt import ModIt_UI":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)



            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "    import importlib":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)


            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "    ModIt_UI":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)


            with open(UserSetupPath, "r") as input:
                with open(TempFilePAth, "w") as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip("\n") != "    importlib.reload(ModIt_UI)":
                            output.write(line)
            # replace file with original name
            os.replace(TempFilePAth, UserSetupPath)

