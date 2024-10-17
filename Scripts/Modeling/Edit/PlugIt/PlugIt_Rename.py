
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
WindowsTitle = "Rename Asset"
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH
FIRSTTAB_NAME = ""

REMOVE_END = ""
ITEM_FOLDER_PATH =""

# ________________//
# ___________________________________________
# ________________//

def SEND_INFO(removeEnd, ItemFolderPath):
    global REMOVE_END
    global ITEM_FOLDER_PATH

    REMOVE_END = removeEnd
    ITEM_FOLDER_PATH = ItemFolderPath


class RenameAsset_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(RenameAsset_UI, self).__init__()
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
        MainNewTab_Label.setText("New Name :   ")
        MainNewTab_HLyt.addWidget(MainNewTab_Label)

        self.MainNewTab_Field = QtWidgets.QLineEdit()
        self.MainNewTab_Field.setObjectName("UserLibPathField")
        MainNewTab_HLyt.addWidget(self.MainNewTab_Field)





        ##________________________________________// CREATE BTN
        CreateBTN = QtWidgets.QPushButton()
        CreateBTN.setText("RENAME")
        CreateBTN.setObjectName("AddAsset")
        CreateBTN.setFixedHeight(25)
        CreateBTN.clicked.connect(self.RENAME)
        CreateBTN.setShortcut(QtGui.QKeySequence("Return"))
        CreateBTN.setToolTip("Rename Asset")
        NEWTABS_MAIN_Layout.addWidget(CreateBTN)


        NEWTABS_MAIN_Layout.addStretch()






    def RENAME(self):
        NEW_NAME = self.MainNewTab_Field.text()

        CHECK_FOLDER = REMOVE_END + "/" + NEW_NAME
        LIST_DIR = os.listdir(REMOVE_END)

        # 1 - Verif Item Name Already Exist
        if NEW_NAME in LIST_DIR:
            PlugIt_Global.WarningWindow(" Asset name already exist in this folder. Delete it first. ", 290)
            return

        #2 - Rename Files
        for filename in os.listdir(ITEM_FOLDER_PATH):
            if filename.endswith(".json"):
                print ("File Names List are = " + str(filename))
                os.rename(ITEM_FOLDER_PATH + "/" + filename, ITEM_FOLDER_PATH + "/" +  NEW_NAME + ".json")
            if filename.endswith(".ma"):
                print ("File Names List are = " + str(filename))
                os.rename(ITEM_FOLDER_PATH + "/" + filename, ITEM_FOLDER_PATH + "/" +  NEW_NAME + ".ma")
            if filename.endswith(".png"):
                print ("File Names List are = " + str(filename))
                os.rename(ITEM_FOLDER_PATH + "/" + filename, ITEM_FOLDER_PATH + "/" +  NEW_NAME + ".png")

        #3 - THEN : Rename the Folder
        os.rename(ITEM_FOLDER_PATH, REMOVE_END + "/" + NEW_NAME)






        #4 -  FAV CLEAN List
        renameOld = (ITEM_FOLDER_PATH.split("/")[-1]).replace(".png", "")
        renameNew = NEW_NAME
        favouriteFilePath = ASSET_FAVOURITES_PATH
        with open(favouriteFilePath, 'r+') as file:
            fileContent = file.read()
            FAVLIST = json.loads(fileContent)

        for each in FAVLIST:
            nameInList = (each.split("/")[-1]).replace(".png", "")

            if nameInList == renameOld:
                rootName = each.replace(nameInList + "/" + nameInList + ".png", "")
                newFAV = str(FAVLIST).replace(str(each), str(rootName) + str(renameNew) + "/" + str(renameNew) + ".png")
                newFAVtoWritte = newFAV.replace("'", '"')

                # update favourite json file for saving
                with open(favouriteFilePath, 'w+') as file:
                    file.write(newFAVtoWritte)






        #5 - UPDATE
        mc.deleteUI(WindowsTitle)

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
    ui = Dock(RenameAsset_UI)
    ui.show()

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "Windows_Ico2.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    return ui
