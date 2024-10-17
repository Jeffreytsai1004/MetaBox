
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from functools import partial

# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget

from . import PlugIt_Global
import importlib
importlib.reload(PlugIt_Global)
from . import PlugIt_CSS
importlib.reload(PlugIt_CSS)
from . import PlugIt_AddAsset
importlib.reload(PlugIt_AddAsset)

##---------------------------------------------------------------------------------------------------------------- G L O B A L   V A R I A B L E S
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH

WINDOWS_TITLE = "Plug Creation - Save Scene"


##---------------------------------------------------------------------------------------------------------------- B U I L D   U I
class Save_PopUp_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Save_PopUp_UI, self).__init__()
        self.setMinimumSize(400, 90)
        self.buildUI()

    def buildUI(self):
        ##_________________________________________________________________________________ UI VALUE
        self.setStyleSheet(PlugIt_Global.Theme)
        iconButtonSize = PlugIt_Global.IconButtonSize
        separatorWidth = 1

        ##_________________//  GLOBAL LAYOUT
        GLOBAL_Lyt = QtWidgets.QVBoxLayout(self)
        GLOBAL_Lyt.setSpacing(10)
        GLOBAL_Lyt.setContentsMargins(10, 10, 10, 10)

        #######_______________________________________________ // L A B E L
        Label_Lyt = QtWidgets.QHBoxLayout(self)
        GLOBAL_Lyt.addLayout(Label_Lyt)
        Message_Lbl = QtWidgets.QLabel()
        Message_Lbl.setText("  Save changes before Plug Creation Scene opens ?  ")
        Message_Lbl.setFont(QtGui.QFont('Candara', 9))
        Message_Lbl.setStyleSheet("color:#909090;")
        Label_Lyt.addWidget(Message_Lbl, alignment=QtCore.Qt.AlignCenter)

        #######_______________________________________________ // S A V E    B T N
        Btn_Lyt = QtWidgets.QHBoxLayout(self)
        GLOBAL_Lyt.addLayout(Btn_Lyt)

        Save_Btn = QtWidgets.QPushButton()
        Save_Btn.setText("S A V E")
        Save_Btn.setObjectName("MasterBtn")
        Save_Btn.setFixedHeight(30)
        Save_Btn.clicked.connect(partial(self.set_Save, 1))
        Btn_Lyt.addWidget(Save_Btn)

        #######_______________________________________________ // D O N 'T  S A V E   B T N
        DontSave_Btn = QtWidgets.QPushButton()
        DontSave_Btn.setText("D O N 'T  S A V E")
        DontSave_Btn.setObjectName("MasterBtn")
        DontSave_Btn.setFixedHeight(30)
        DontSave_Btn.clicked.connect(partial(self.set_Save, 0))
        Btn_Lyt.addWidget(DontSave_Btn)

        #######_______________________________________________ // C A N C E L   B T N
        Cancel_Btn = QtWidgets.QPushButton()
        Cancel_Btn.setText("C A N C E L")
        Cancel_Btn.setObjectName("MasterBtn")
        Cancel_Btn.setFixedHeight(30)
        Cancel_Btn.clicked.connect(self.set_Cancel)
        Btn_Lyt.addWidget(Cancel_Btn)




    ##____________________________________________________________
    ##_________________________________________________________________________________// DEF
    ##_____________________________________________________________
    def set_Save(self, option):
        print("Save Option = " + str(option))
        if option == 1: # SAVE
            mc.SaveScene()
        else:
            pass

        ACTIVESUBTAB_NAME = "Rock"
        importlib.reload(PlugIt_AddAsset)
        PlugIt_AddAsset.SEND_INFO(str(ACTIVESUBTAB_NAME))
        PlugIt_AddAsset.showUI()

        if mc.window(WINDOWS_TITLE, exists=True):
            mc.deleteUI(WINDOWS_TITLE)


    def set_Save2(self, option):
        MainTabindex = self.firstTab.currentIndex()
        currentMainTabText = self.firstTab.tabText(MainTabindex)

        if currentMainTabText == "❤":
            currentMainTab = self.firstTab.tabText(0)

        elif currentMainTabText == "/":
            currentMainTab = self.firstTab.tabText(0)

        else:
            currentMainTab = currentMainTabText


        #GET SECOND TAB
        self.get_SubTabIndex(self.secondTab)
        #print("ACTIVESUBTAB_NAME == " + str(ACTIVESUBTAB_NAME))

        importlib.reload(PlugIt_AddAsset)
        #PlugIt_AddAsset.SEND_INFO(str(ACTIVESUBTAB_NAME))
        PlugIt_AddAsset.showUI()

    def set_Cancel(self):
        if mc.window(WINDOWS_TITLE, exists=True):
            mc.deleteUI(WINDOWS_TITLE)




def Dock(Widget, width=200, height=200, hp="free", show=True):
    name = WINDOWS_TITLE
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
    print("AT CLOSE")

def showUI():
    ui = Dock(Save_PopUp_UI)
    ui.show()


    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WINDOWS_TITLE)
    try:
        widget = wrapInstance(int(qw), QWidget)
        # Create a QIcon object
        icon = QIcon(IconPath + "PlugIt_Window_Ico.png")
        # Assign the icon
        widget.setWindowIcon(icon)
    except:
        pass #Pour si on reload alos qu'il est dock



    return ui









