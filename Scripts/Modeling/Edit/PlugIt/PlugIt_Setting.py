
##                                         SETTING
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui

# Special cases for different Maya versions
try:
    from shiboken2 import wrapInstance
except ImportError:
    from shiboken import wrapInstance

try:
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import QWidget
except ImportError:
    from PySide.QtGui import QIcon, QWidget

import importlib

from . import PlugIt_Global
importlib.reload(PlugIt_Global)

from . import PlugIt_CSS
importlib.reload(PlugIt_CSS)

##PATH_SET
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath

##GLOBAL VAR
WindowsTitle = "Settings"
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH


##UI INFO
Theme_pref = json.load(open(PreferencePath + 'Pref_Theme.json', "r"))
PREF_THEME = (Theme_pref['THEME'])
if PREF_THEME == 0:
    ThemeIndex = 0
if PREF_THEME == 1:
    ThemeIndex = 1
if PREF_THEME == 2:
    ThemeIndex = 2

Icon_pref = json.load(open(PreferencePath + 'Pref_IconSize.json', "r"))
PREF_ICON = (Icon_pref['ICONSIZE'])
if PREF_ICON == 18:
    IconIndex = 0
if PREF_ICON == 22:
    IconIndex = 1
if PREF_ICON == 30:
    IconIndex = 2


Click_pref = json.load(open(PreferencePath + 'Pref_Click.json', "r"))
PREF_CLICK = (Click_pref['CLICK'])
if PREF_CLICK == 0:
    ClickIndex = 0
if PREF_CLICK == 1:
    ClickIndex = 1

# ________________//
# ___________________________________________
# ________________//


class Setting_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Setting_UI, self).__init__()
        self.setMinimumSize(650, 210)

        self.buildUI()


    def buildUI(self):
        SETTINGLayout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(PlugIt_Global.Theme)
        ##UI - Preferences
        iconButtonSize = PlugIt_Global.IconButtonSize

        ## UI TABS
        UILabel = QtWidgets.QLabel(self)
        UILabel.setText(" - U I - ")
        UILabel.setFont(QtGui.QFont('Candara', 10))
        UILabel.setAlignment(QtCore.Qt.AlignCenter)
        SETTINGLayout.addWidget(UILabel)
        SETTINGLayout.addSpacing(5)



        ##_____________________________________________________ UI THEME
        THEMEHlyt = QtWidgets.QHBoxLayout()
        SETTINGLayout.addLayout(THEMEHlyt)
        THEMELabel = QtWidgets.QLabel(self)
        THEMELabel.setText("T h e m e : ")
        THEMELabel.setFixedWidth(58)
        THEMELabel.setFont(QtGui.QFont('Candara', 7))
        THEMEHlyt.addWidget(THEMELabel)
        self.ThemeComboList = [
            'Default Blue',
            'Maya',
        ]

        self.ThemeCombo = QtWidgets.QComboBox()
        self.ThemeCombo.addItems(self.ThemeComboList)
        self.ThemeCombo.setFixedWidth(200)
        self.ThemeCombo.currentIndexChanged.connect(self.SET_Theme)
        self.ThemeCombo.setCurrentIndex(ThemeIndex)
        THEMEHlyt.addWidget(self.ThemeCombo)

        ## UI ICONSIZE
        IconSizeLabel = QtWidgets.QLabel(self)
        IconSizeLabel.setText("        /        I c o n s  S i z e : ")
        IconSizeLabel.setFixedWidth(140)
        IconSizeLabel.setFont(QtGui.QFont('Candara', 7))
        THEMEHlyt.addWidget(IconSizeLabel)
        self.IconSizeComboList = [
            '18',
            '22',
            '30',
        ]

        self.IconSizeCombo = QtWidgets.QComboBox()
        self.IconSizeCombo.addItems(self.IconSizeComboList)
        #self.IconSizeCombo.setFixedWidth(200)
        self.IconSizeCombo.setCurrentIndex(IconIndex)
        self.IconSizeCombo.currentIndexChanged.connect(self.SET_IconSize)
        THEMEHlyt.addWidget(self.IconSizeCombo)




        ##---------------------------------------------------- SEPARATOR : Horizontal
        SETTINGLayout.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        SETTINGLayout.addWidget(separator)
        SETTINGLayout.addSpacing(2)



        ## UI TABS
        UILabel = QtWidgets.QLabel(self)
        UILabel.setText(" - P L U G   O P T I O N S - ")
        UILabel.setFont(QtGui.QFont('Candara', 10))
        UILabel.setAlignment(QtCore.Qt.AlignCenter)
        SETTINGLayout.addWidget(UILabel)



        ##_____________________________________________________ CLICK CHOICE
        CLICKHlyt = QtWidgets.QHBoxLayout()
        SETTINGLayout.addLayout(CLICKHlyt)
        CLICKLabel = QtWidgets.QLabel(self)
        CLICKLabel.setText("I m p o r t  P l u g : ")
        CLICKLabel.setFont(QtGui.QFont('Candara', 7))
        CLICKHlyt.addWidget(CLICKLabel)
        self.ClickComboList = [
            'Left Click',
            'Double-Click',
        ]

        self.ClickCombo = QtWidgets.QComboBox()
        self.ClickCombo.addItems(self.ClickComboList)
        #self.ClickCombo.setFixedWidth(150)
        self.ClickCombo.currentIndexChanged.connect(self.SET_Click)
        self.ClickCombo.setCurrentIndex(ClickIndex)
        CLICKHlyt.addWidget(self.ClickCombo)

        CLICKHlyt.addSpacing(20)

        ## CLEAN FAV BTN
        CleanFavBTN = QtWidgets.QPushButton()
        CleanFavBTN.setText("C l e a n   F a v o r i t e   T a b")
        CleanFavBTN.setFont(QtGui.QFont('Candara', 7))
        CleanFavBTN.setObjectName("CleanFav")
        CleanFavBTN.setFixedHeight(25)
        CleanFavBTN.setFixedWidth(200)
        CleanFavBTN.clicked.connect(self.CleanFav)
        CleanFavBTN.setToolTip("That will delete all Favorite tab content")
        CLICKHlyt.addWidget(CleanFavBTN)

        ## CLEAN SCENE BTN
        CleanSceneBTN = QtWidgets.QPushButton()
        CleanSceneBTN.setText("C l e a n   S c e n e")
        CleanSceneBTN.setFont(QtGui.QFont('Candara', 7))
        CleanSceneBTN.setObjectName("CleanScene")
        CleanSceneBTN.setFixedHeight(25)
        CleanSceneBTN.setFixedWidth(200)
        CleanSceneBTN.clicked.connect(self.CleanScene)
        CleanSceneBTN.setToolTip("Clean Scene Node after Problem")
        CLICKHlyt.addWidget(CleanSceneBTN)



        ##---------------------------------------------------- SEPARATOR : Horizontal
        SETTINGLayout.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet(
            "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        SETTINGLayout.addWidget(separator)
        SETTINGLayout.addSpacing(2)


        ##________________________________________// SAVE SETTING
        SaveSettingBTN = QtWidgets.QPushButton()
        SaveSettingBTN.setText("SAVE SETTING")
        SaveSettingBTN.setObjectName("SaveSetting")
        SaveSettingBTN.setFixedHeight(25)
        SaveSettingBTN.clicked.connect(self.Apply)
        SaveSettingBTN.setToolTip("Apply and Save Setting")
        SETTINGLayout.addWidget(SaveSettingBTN)


        #THEMEHlyt.addStretch()
        SETTINGLayout.addStretch()
        CLICKHlyt.addStretch()



    def CleanScene(self):
        if mc.objExists("PlugIt_TargetMesh"):
            mc.rename("PlugIt_TargetMesh", "newDebugMesh")


        listToClean = ["PlugIt_TargetMesh*", "Plug_Mesh*", "Mesh_EdgeBorder_set*", "Plug_AllFaces_set*", "Plug_EdgeBorder_set*", "Plug_Hole_set*", "Plug_Selection_set*", "PlugIt_Plug_Shd*",  "hairSystem*", "hairSystem*Follicles", "hairSystem*OutputCurves*", "nucleus*", "Mesh_EdgeBorder_set*"]

        for each in listToClean:
            if mc.objExists(each):
                mc.delete(each)


    def CleanFav(self):
        BackgroundColor = 0.16
        Message = "Are you sure you want to delete all your saved favourites?"
        # ________________//
        if mc.window("WarningWindow", exists=True):
            mc.deleteUI("WarningWindow")
        mc.window("WarningWindow", title=' Warning ', s=False, vis=True, rtf=False)
        mc.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
        mc.separator(h=8, style='none')
        mc.text(l="  " + Message + "  ", al="center")
        mc.separator(h=8, style='none')
        mc.rowColumnLayout( numberOfRows=1 )
        mc.separator(w=35, style='none')
        mc.button(l="YES", c=self.WarningDeleteLayerYES, width= 100, h=20)
        mc.separator(w=10, style='none')
        mc.button(l="NO", c=self.WarningDeleteLayerNO, width= 100, h=20)
        mc.window("WarningWindow", e=True, wh=(300, 80))

        qw = omui.MQtUtil.findWindow("WarningWindow")
        widget = wrapInstance(int(qw), QWidget)
        icon = QIcon(IconPath + "Windows_Ico_Warning.png")
        widget.setWindowIcon(icon)

        mc.showWindow()

    def WarningDeleteLayerYES(self, *args):
        favouriteFilePath = ASSET_FAVOURITES_PATH
        infoToSave = []
        s = json.dumps(infoToSave)
        open(favouriteFilePath, "w").write(s)

        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        ui = PlugIt_UI.showUI()


    def WarningDeleteLayerNO(self, *args):
        mc.deleteUI("WarningWindow")


    def SET_Theme(self):
        ChoosenValue = self.ThemeCombo.currentIndex()
        if ChoosenValue == 0:
            ThemeValue =0
        if ChoosenValue == 1:
            ThemeValue =1
        if ChoosenValue == 2:
            ThemeValue =2

        infoToSave = {"THEME": ThemeValue}
        s = json.dumps(infoToSave)
        open(PreferencePath + 'Pref_Theme.json', "w").write(s)

    def SET_IconSize(self):
        ChoosenValue = self.IconSizeCombo.currentIndex()
        if ChoosenValue == 0:
            IconValue =18
        if ChoosenValue == 1:
            IconValue =22
        if ChoosenValue == 2:
            IconValue =30

        infoToSave = {"ICONSIZE": IconValue}
        s = json.dumps(infoToSave)
        open(PreferencePath + 'Pref_IconSize.json', "w").write(s)

    def SET_Click(self):
        ChoosenValue = self.ClickCombo.currentIndex()
        if ChoosenValue == 0:
            ClickValue =0
        if ChoosenValue == 1:
            ClickValue =1

        infoToSave = {"CLICK": ClickValue}
        s = json.dumps(infoToSave)
        open(PreferencePath + 'Pref_Click.json', "w").write(s)




    def Apply(self):
        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        ui = PlugIt_UI.showUI()


def Dock(Widget, width=200, height=200, hp="free", show=True):
    label = getattr(Widget, "label", WindowsTitle)

    try:
        cmds.deleteUI(WindowsTitle)
    except RuntimeError:
        pass

    dockControl = cmds.workspaceControl(
        WindowsTitle,
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


def showUI():
    ui = Dock(Setting_UI)
    ui.show()

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "Windows_Ico2.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    return ui

