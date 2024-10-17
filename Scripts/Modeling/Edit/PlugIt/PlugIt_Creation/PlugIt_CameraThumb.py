from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
import importlib

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



#PATHS
USERAPPDIR = mc.internalVar(userAppDir=True)
VERSION = mc.about(v=True)


from .. import PlugIt_Global
importlib.reload(PlugIt_Global)

from .. import PlugIt_CSS
importlib.reload(PlugIt_CSS)



##THEME_SET
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath

##GLOBAL VAR
WindowsTitle = "Thumbnail Framing"


SELECTION = []
WRESOLUTION = 0
HRESOLUTION = 0
ASPECTRATION = 1

def SEND_INFO(Selection):
    global SELECTION
    SELECTION = Selection
    print ("SELECTION in ADD ASSET = " + str(SELECTION))
    return SELECTION



#________________//
#___________________________________________
#________________//
class Thumb_Framing(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Thumb_Framing, self).__init__()
        self.setMinimumSize(410, 45)
        self.buildUI()


    def buildUI(self):
        THUMBFRAMINGLayout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(PlugIt_CSS.PlugIt_CSS)
        iconButtonSize = PlugIt_Global.IconButtonSize

        global WRESOLUTION
        WRESOLUTION = mc.getAttr("defaultResolution.width")
        global HRESOLUTION
        HRESOLUTION = mc.getAttr("defaultResolution.height")
        global ASPECTRATION
        ASPECTRATION = mc.getAttr("defaultResolution.deviceAspectRatio")



        mc.setAttr("defaultResolution.width", 400)
        mc.setAttr("defaultResolution.height", 400)
        mc.setAttr("defaultResolution.deviceAspectRatio", 1)


        mc.select(SELECTION)
        self.FramingViewport = mc.modelEditor(camera="RenderThumbCamShape", vs=True, addSelected=True, ca= False, dim= True, da ="smoothShaded", dl= "all", dtx= True, gr= False, hud= True, lt= False, sdw= True, swf= False, th= True, tx= True, wos = False)
        mc.viewFit("RenderThumbCamShape", all= False, f=1)
        mc.select(SELECTION, d=True)

        mel.eval("setCameraNamesVisibility 0;")
        mel.eval("setViewAxisVisibility 0;")




        #############################################
        ## TOOLBAR
        TOOLBARLayout = QtWidgets.QHBoxLayout(self)
        THUMBFRAMINGLayout.addLayout(TOOLBARLayout)

        ## CAMERA BTN
        CameraFitBtn = QtWidgets.QPushButton()
        CameraFitBtn.setFixedSize(iconButtonSize,iconButtonSize)
        CameraFitBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        CameraFitBtn.setIcon(QtGui.QIcon(IconPath + "Camera2.png"))
        CameraFitBtn.setToolTip("  Fit Object  ")
        CameraFitBtn.setShortcut(QtGui.QKeySequence("F"))
        CameraFitBtn.clicked.connect(self.FitObject)
        TOOLBARLayout.addWidget(CameraFitBtn)


        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setObjectName("Separator")
        self.Separator.setFixedSize(iconButtonSize,iconButtonSize)
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        TOOLBARLayout.addWidget(self.Separator)

        ## LIGHTON BTN
        LightOn = QtWidgets.QPushButton()
        LightOn.setFixedSize(iconButtonSize,iconButtonSize)
        LightOn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        LightOn.setIcon(QtGui.QIcon(IconPath + "LightOn.png"))
        LightOn.setToolTip("  Light On  ")
        LightOn.clicked.connect(self.LightOn)
        TOOLBARLayout.addWidget(LightOn)

        ## LIGHTOFF BTN
        LightOff = QtWidgets.QPushButton()
        LightOff.setFixedSize(iconButtonSize,iconButtonSize)
        LightOff.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        LightOff.setIcon(QtGui.QIcon(IconPath + "LightOff.png"))
        LightOff.setToolTip("  Light Off  ")
        LightOff.clicked.connect(self.LightOff)
        TOOLBARLayout.addWidget(LightOff)


        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setObjectName("Separator")
        self.Separator.setFixedSize(iconButtonSize,iconButtonSize)
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        TOOLBARLayout.addWidget(self.Separator)


        ## WIRE BTN
        WireBtn = QtWidgets.QPushButton()
        WireBtn.setFixedSize(iconButtonSize,iconButtonSize)
        WireBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        WireBtn.setIcon(QtGui.QIcon(IconPath + "Wireframe.png"))
        WireBtn.setToolTip("  Wireframe Override  ")
        WireBtn.clicked.connect(self.Wireframe)
        TOOLBARLayout.addWidget(WireBtn)



        ## SHADE BTN
        ShadeBtn = QtWidgets.QPushButton()
        ShadeBtn.setFixedSize(iconButtonSize,iconButtonSize)
        ShadeBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        ShadeBtn.setIcon(QtGui.QIcon(IconPath + "Shade2.png"))
        ShadeBtn.setToolTip("  Shade Only  ")
        ShadeBtn.clicked.connect(self.Shade)
        TOOLBARLayout.addWidget(ShadeBtn)

        ## TEXTURE BTN
        TextureBtn = QtWidgets.QPushButton()
        TextureBtn.setFixedSize(iconButtonSize,iconButtonSize)
        TextureBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        TextureBtn.setIcon(QtGui.QIcon(IconPath + "TextureOn.png"))
        TextureBtn.setToolTip("  Display Texture On  ")
        TextureBtn.clicked.connect(self.Texture)
        TOOLBARLayout.addWidget(TextureBtn)



        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setObjectName("Separator")
        self.Separator.setFixedSize(iconButtonSize,iconButtonSize)
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        TOOLBARLayout.addWidget(self.Separator)

        ## CALIDATE BTN
        ValidateBtn = QtWidgets.QPushButton()
        ValidateBtn.setFixedSize(iconButtonSize,iconButtonSize)
        ValidateBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        ValidateBtn.setIcon(QtGui.QIcon(IconPath + "Apply.png"))
        ValidateBtn.setToolTip("  Validate Framing  ")
        ValidateBtn.setShortcut(QtGui.QKeySequence("Return"))
        ValidateBtn.clicked.connect(self.Validate)
        TOOLBARLayout.addWidget(ValidateBtn)



        #TOOLBARLayout.addStretch()

    def FitObject(self):
        print ("Fit OBJECT")
        mc.select(SELECTION)
        mc.viewFit("RenderThumbCam", all= False, f=1)
        mc.select(SELECTION, d=True)


    def LightOn(self):
        mc.modelEditor(self.FramingViewport, edit=True, dl= "all")

    def LightOff(self):
        mc.modelEditor(self.FramingViewport, edit=True, dl= "default")

    def Wireframe(self):
        mc.modelEditor(self.FramingViewport, edit=True, wos= True)

    def Shade(self):
        mc.modelEditor(self.FramingViewport, edit=True, displayAppearance='smoothShaded')
        mc.modelEditor(self.FramingViewport, edit=True, displayTextures=False)
        mc.modelEditor(self.FramingViewport, edit=True, wos= False)

    def Texture(self):
        mc.modelEditor(self.FramingViewport, edit=True, displayAppearance='smoothShaded')
        mc.modelEditor(self.FramingViewport, edit=True, displayTextures=True)

    def Validate(self):
        mc.deleteUI("Thumbnail Framing")


def Dock(Widget, width=200, height=200, hp="fixed", show=True):
    label = getattr(Widget, "label", WindowsTitle)

    try:
        cmds.deleteUI(WindowsTitle)
    except RuntimeError:
        pass

    dockControl = cmds.workspaceControl(
        WindowsTitle,
        initialWidth=width,
        minimumWidth=False,
        initialHeight = height,
        minimumHeight=False,
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
    mel.eval("setCameraNamesVisibility 1;")
    mel.eval("setViewAxisVisibility 1;")
    mc.setAttr("defaultResolution.width", WRESOLUTION)
    mc.setAttr("defaultResolution.height", HRESOLUTION)
    mc.setAttr("defaultResolution.deviceAspectRatio", ASPECTRATION)


def showUI():
    ui = Dock(Thumb_Framing)
    ui.show()

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "Windows_Ico2.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    mc.scriptJob(uiDeleted=['Thumbnail Framing', atClose])

    return ui

