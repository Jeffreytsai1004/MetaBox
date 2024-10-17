#!/usr/bin/env python
# -*- coding: utf-8 -*-

##GLOBAL VARIABLEs
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

from . import ModIt_CSS


##_____________________________________________PATH
ModItPath = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
PlugInsPath = ModItPath
IconsPathThemeClassic = os.path.join(ModItPath+'/Icons/Theme_Classic/')
ToolPath = os.path.join(ModItPath+'/Tools/')
PreferencePath = os.path.join(ModItPath+'/Preferences/')
PrefIcons = os.path.join(ModItPath+'/Icons/')
RessourcePath = os.path.join(ModItPath+'/Ressources/')



##_____________________________________________PREFERENCES
ModItTitle = "ModIt"


##_____________________________________________UI
#_____________#Theme
Theme_pref = json.load(open(PreferencePath + 'Pref_Theme.json', "r"))
PREF_THEME = (Theme_pref['THEME'])

if PREF_THEME == 0:
    Theme = ModIt_CSS.ModIt_CSS
    IconPath = IconsPathThemeClassic
elif PREF_THEME == 1:
    Theme = ModIt_CSS.Maya_CSS
    IconPath = IconsPathThemeClassic

#_____________#IconSize
IconSize_pref = json.load(open(PreferencePath + 'Pref_IconSize.json', "r"))
PREF_ICONSIZE = (IconSize_pref['ICONSIZE'])

IconButtonSize = PREF_ICONSIZE

# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 30
iconButtonSize = 30
separatorWidth = 1


##_____________________________________________WARNING POP UP
def WarningWindow(message, size, *args):
    BackgroundColor = 0.16
    # ________________//
    if cmds.window("WarningWindow", exists=True):
        cmds.deleteUI("WarningWindow")
    cmds.window("WarningWindow", title=' Warning ', s=False, vis=True, rtf=False)
    cmds.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
    cmds.separator(h=8, style='none')
    cmds.text(l="  " + message + "  ", al="center")
    cmds.separator(h=8, style='none')
    cmds.button(l="OK", c=WarningOKButton)
    cmds.window("WarningWindow", e=True, wh=(size, 80))

    qw = omui.MQtUtil.findWindow("WarningWindow")
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(IconPath + "Windows_Ico_Warning.png")
    widget.setWindowIcon(icon)

    cmds.showWindow()

def WarningOKButton(*args):
    cmds.deleteUI("WarningWindow")



def LoadingWindow(message, size, *args):
    BackgroundColor = 0.110
    # ________________//
    if cmds.window("LoadingWindow", exists=True):
        cmds.deleteUI("LoadingWindow")
    cmds.window("LoadingWindow", title='Loading Asset', s=False, vis=True, rtf=False)
    cmds.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
    cmds.separator(h=5, style='none')
    cmds.text(l=" " + message + " ", al="center")
    cmds.iconTextButton(image1= IconPath + "Refresh_Button.png")
    cmds.window("LoadingWindow", e=True, wh=(size, 70))

    qw = omui.MQtUtil.findWindow("LoadingWindow")
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(IconPath + "Windows_Ico2.png")
    widget.setWindowIcon(icon)

    cmds.showWindow()

















