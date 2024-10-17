
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
WindowsTitle = "Add New Sub Tab"
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH
FIRSTTAB_NAME = ""

# ________________//
# ___________________________________________
# ________________//
class NewSecondTab_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewSecondTab_UI, self).__init__()
        self.setMinimumSize(400, 80)
        self.buildUI()


    def buildUI(self):
        NEWTABS_MAIN_Layout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(PlugIt_Global.Theme)
        iconButtonSize = PlugIt_Global.IconButtonSize

        #############################################
        ##________________________________________// MAIN TAB
        ## MAIN TAB LAYOUT
        MainNewTab_HLyt = QtWidgets.QHBoxLayout()
        NEWTABS_MAIN_Layout.addLayout(MainNewTab_HLyt)
        MainNewTab_HLyt.setAlignment(QtCore.Qt.AlignCenter)

        ## MAIN TAB LABEL
        MainNewTab_Label = QtWidgets.QLabel(self)
        MainNewTab_Label.setText("SUB Tab Name :   ")
        MainNewTab_HLyt.addWidget(MainNewTab_Label)

        self.MainNewTab_Field = QtWidgets.QLineEdit()
        self.MainNewTab_Field.setObjectName("UserLibPathField")
        MainNewTab_HLyt.addWidget(self.MainNewTab_Field)





        ##________________________________________// CREATE BTN
        CreateBTN = QtWidgets.QPushButton()
        CreateBTN.setText("CREATE TABS")
        CreateBTN.setObjectName("AddAsset")
        CreateBTN.setFixedHeight(25)
        CreateBTN.clicked.connect(self.CREATETABS)
        CreateBTN.setShortcut(QtGui.QKeySequence("Return"))
        CreateBTN.setToolTip("Create Tabs")
        NEWTABS_MAIN_Layout.addWidget(CreateBTN)


        NEWTABS_MAIN_Layout.addStretch()




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


    def CREATETABS(self):
        SUB_TAB_NAME = self.MainNewTab_Field.text()

        #SECURE WARNING
        if SUB_TAB_NAME == "":
            PlugIt_Global.WarningWindow("You should give a MAIN Tab Name", 250)
            return


       #CREATE SUB TAB*
        try:
            SECOND_TAB_PATH = LIBRARY_PATH + "/" +FIRSTTAB_NAME + "/" + SUB_TAB_NAME
            print ("SECOND_TAB_PATH = " + str(SECOND_TAB_PATH))
            os.mkdir(SECOND_TAB_PATH)
        except:
            PlugIt_Global.WarningWindow("SECOND Tab Name already exist, delete it first", 250)
            return



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


    return child


def showUI(FirstTabName):
    ui = Dock(NewSecondTab_UI)
    ui.show()
    if mc.window("Add New Tab", exists=True):
        mc.deleteUI("Add New Tab")

    global FIRSTTAB_NAME
    FIRSTTAB_NAME = FirstTabName

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "Windows_Ico2.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    return ui

