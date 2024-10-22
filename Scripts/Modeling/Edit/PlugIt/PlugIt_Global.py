##GLOBAL VARIABLEs
from maya import cmds as mc
import json
import os
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
from . import PlugIt_CSS
import importlib
importlib.reload(PlugIt_CSS)


PLUGIT_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
IconsPathThemeClassic = os.path.join(PLUGIT_PATH+'/Icons/Theme_Classic/')
PreferencePath = os.path.join(PLUGIT_PATH+'/Preferences/')
AssetCreationPath = os.path.join(PLUGIT_PATH+'/PlugIt_Creation/')
PlugInsPath = os.path.join(PLUGIT_PATH+'/Tools/')
PrefIcons = os.path.join(PLUGIT_PATH+'/Icons/')
ToolsPath = os.path.join(PLUGIT_PATH+'/Tools/')

PlugItTitle = "PlugIt"

##_____________________________________________PREFERENCES
LIBRARY_PATH = os.path.join(PLUGIT_PATH+'/LIBRARY')
ASSET_FAVOURITES_PATH = os.path.join(PLUGIT_PATH+'/Preferences/FavouritesList.json')

##_____________________________________________UI
#_____________#Theme
Theme_pref = json.load(open(PreferencePath + 'Pref_Theme.json', "r"))
PREF_THEME = (Theme_pref['THEME'])

if PREF_THEME == 0:
    Theme = PlugIt_CSS.PlugIt_CSS
    IconPath = IconsPathThemeClassic
elif PREF_THEME == 1:
    Theme = PlugIt_CSS.Maya_CSS
    IconPath = IconsPathThemeClassic

#_____________#IconSize
IconSize_pref = json.load(open(PreferencePath + 'Pref_IconSize.json', "r"))
PREF_ICONSIZE = (IconSize_pref['ICONSIZE'])

IconButtonSize = PREF_ICONSIZE



##_____________________________________________WARNING POP UP
def WarningWindow(message, size, *args):
    BackgroundColor = 0.16
    # ________________//
    if mc.window("WarningWindow", exists=True):
        mc.deleteUI("WarningWindow")
    mc.window("WarningWindow", title=' Warning ', s=False, vis=True, rtf=False)
    mc.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
    mc.separator(h=8, style='none')
    mc.text(l="  " + message + "  ", al="center")
    mc.separator(h=8, style='none')
    mc.button(l="OK", c=WarningOKButton)
    mc.window("WarningWindow", e=True, wh=(size, 80))

    qw = omui.MQtUtil.findWindow("WarningWindow")
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(IconPath + "Windows_Ico_Warning.png")
    widget.setWindowIcon(icon)

    mc.showWindow()

def WarningOKButton(*args):
    mc.deleteUI("WarningWindow")



def LoadingWindow(message, size, *args):
    BackgroundColor = 0.110
    # ________________//
    if mc.window("LoadingWindow", exists=True):
        mc.deleteUI("LoadingWindow")
    mc.window("LoadingWindow", title='Loading Asset', s=False, vis=True, rtf=False)
    mc.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
    mc.separator(h=5, style='none')
    mc.text(l=" " + message + " ", al="center")
    mc.iconTextButton(image1= IconPath + "Refresh_Button.png")
    mc.window("LoadingWindow", e=True, wh=(size, 70))

    qw = omui.MQtUtil.findWindow("LoadingWindow")
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(IconPath + "Windows_Ico2.png")
    widget.setWindowIcon(icon)

    mc.showWindow()

















