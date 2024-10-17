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


##GLOBAL VAR
WindowsTitle = " - AssetIt -"


#________________//
#___________________________________________
#________________//
class AssetItPromo_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AssetItPromo_UI, self).__init__()
        self.setMinimumSize(1420, 950)
        self.buildUI()

    def buildUI(self):
        UILayout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(ModIt_CSS.ModIt_CSS)
        ##UI - Preferences
        iconButtonSize = 22

        #############################################



        ## SCATTER TAB Banner
        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(IconPath + "AssetIt_Presa_Img.jpg")
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignTop)
        UILayout.addWidget(label)

        ## TEXT
        LandscapeTitle = QtWidgets.QLabel(self)
        LandscapeTitle.setFont(QtGui.QFont('Candara', 10))
        LandscapeTitle.setStyleSheet("QLabel {color : #65BEF1; }")
        LandscapeTitle.setText(""" Allow users to create custom Bolts would mean the need to : set a user folder path, creation thumbnail, pivot placement setting, allow any type of mesh possible... 

> Which is so called an Asset Manager and for that I created AssetIt script. 

- So if you need more control about Bold and you want to create your own, I invited you to take a look at AssetIt script. -""")
        LandscapeTitle.setAlignment(QtCore.Qt.AlignCenter)
        UILayout.addWidget(LandscapeTitle)



        BoutonsLayout = QtWidgets.QHBoxLayout()
        UILayout.addLayout(BoutonsLayout)
        
        GetAssetIt_btn = QtWidgets.QPushButton("-  G e t   A s s e t I t  -")
        GetAssetIt_btn.setFont(QtGui.QFont('Candara', 10))
        GetAssetIt_btn.setObjectName("AssetIt")
        GetAssetIt_btn.setFixedHeight(22)
        GetAssetIt_btn.setShortcut(QtGui.QKeySequence("Return"))
        GetAssetIt_btn.clicked.connect(self.GetAssetIt)
        BoutonsLayout.addWidget(GetAssetIt_btn)






    def GetAssetIt(self):
        cmds.deleteUI(WindowsTitle)

        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("https://wzx.gumroad.com/l/AssetIt"))




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
    ui = Dock(AssetItPromo_UI)
    ui.show()

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "ModIt_Window_Ico.png")
    # Assign the icon
    widget.setWindowIcon(icon)


    return ui

