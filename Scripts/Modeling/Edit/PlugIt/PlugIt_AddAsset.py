##                                         PLUG CREATION
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
import sys
from mtoa.cmds.arnoldRender import arnoldRender


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
from .PlugIt_Creation import PlugIt_CameraThumb
importlib.reload(PlugIt_CameraThumb)

##PATH_SET
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath
PlugIt_Creation_PATH = PlugIt_Global.AssetCreationPath
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH

##GLOBAL VAR
WindowsTitle = "Plug Creation"
ACTIVEMAINTAB = "USER"
ACTIVESUBTAB_NAME = ""
RENDERDONE = False
RENDERERCHOICE = "Arnold"
PLUGNAME = "Plug Name"
HOLE_SET = 0

def SEND_INFO(SecondTabActiveName):
    global ACTIVESUBTAB_NAME
    ACTIVESUBTAB_NAME = SecondTabActiveName
    return ACTIVESUBTAB_NAME

class AddAsset_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddAsset_UI, self).__init__()
        self.setMinimumSize(360, 350)
        self.buildUI()

    def buildUI(self):
        #if mc.objExists("PlugIt_ThumbScene"):
            #    pass
            #else:
            #######_______________________________________________//  I M P O R T   S C E N E
        mc.file(PlugIt_Creation_PATH + "Thumb_Creation/Plug_Creation_Scene_Init.ma", rnn=True, o=True, ignoreVersion=True, force = True)
        mc.file(rename= PlugIt_Creation_PATH + "Thumb_Creation/Plug_Creation_Scene.ma")
        mc.file(save=True, type="mayaAscii", force = True)

        PLUG_MAINLyt = QtWidgets.QVBoxLayout(self)
        PLUG_MAINLyt.setSpacing(10)
        self.setStyleSheet(PlugIt_Global.Theme)
        ##UI - Preferences
        iconButtonSize = PlugIt_Global.IconButtonSize

        #######_______________________________________________// T I T L E
        Title_Lbl = QtWidgets.QLabel(self)
        Title_Lbl.setText(" -  P L U G   C R E A T I O N  - ")
        Title_Lbl.setFont(QtGui.QFont('Candara', 8))
        Title_Lbl.setAlignment(QtCore.Qt.AlignCenter)
        PLUG_MAINLyt.addWidget(Title_Lbl)
        
        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)


        #######_______________________________________________// T U T O
        Tuto_Lyt = QtWidgets.QHBoxLayout()
        PLUG_MAINLyt.addLayout(Tuto_Lyt)

        self.Tuto_Btn = QtWidgets.QPushButton()
        self.Tuto_Btn.setObjectName("MasterBtn")
        self.Tuto_Btn.setText("H O W   T O   C R E A T E   P L U G  ?")
        self.Tuto_Btn.setStyleSheet("QPushButton {color: #65BEF1; border-color: #65BEF1; }" )
        self.Tuto_Btn.setFixedHeight(30)
        self.Tuto_Btn.clicked.connect(self.link_Tuto)
        self.Tuto_Btn.setToolTip("Link to tutorial on how to create your custom Plug")
        Tuto_Lyt.addWidget(self.Tuto_Btn)

        Tuto_Lyt.addSpacing(10)


        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet(
            "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)

        #######_______________________________________________// N A M E
        PlugName_Lyt = QtWidgets.QHBoxLayout()
        PLUG_MAINLyt.addLayout(PlugName_Lyt)

        self.PlugNameField = QtWidgets.QLineEdit()
        self.PlugNameField.setObjectName("AssetNameField")
        self.PlugNameField.setAlignment(QtCore.Qt.AlignCenter)
        self.PlugNameField.setText(PLUGNAME)
        self.PlugNameField.setFont(QtGui.QFont('Calibri', 9))
        #self.PlugNameField.setStyleSheet("QLineEdit{color: #71CCFF;}")
        self.PlugNameField.setFixedHeight(25)
        PlugName_Lyt.addWidget(self.PlugNameField)

        #AssetName Empty
        if self.PlugNameField.text() == "Plug Name":
            self.PlugNameField.clear()
            self.PlugNameField.setPlaceholderText("Plug Name")

        self.PlugNameFieldEnterBtn = QtWidgets.QPushButton()
        self.PlugNameFieldEnterBtn.setFixedSize(0,0)
        self.PlugNameFieldEnterBtn.setIconSize(QtCore.QSize(0, 0))
        self.PlugNameFieldEnterBtn.setIcon(QtGui.QIcon(IconPath + "Apply.png"))
        self.PlugNameFieldEnterBtn.setToolTip("  Validate Asset Name  ")
        self.PlugNameFieldEnterBtn.clicked.connect(self.AssetNameValidate)
        self.PlugNameFieldEnterBtn.setShortcut(QtGui.QKeySequence("Return"))
        PlugName_Lyt.addWidget(self.PlugNameFieldEnterBtn)


        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)


        #######_______________________________________________// T A B  C H O I C E
        ##FOLDER COMBO
        self.secondLevelFolderList = os.listdir(LIBRARY_PATH + "/" + ACTIVEMAINTAB)
        Folder_HLyt = QtWidgets.QHBoxLayout()
        Folder_HLyt.setSpacing(6)
        PLUG_MAINLyt.addLayout(Folder_HLyt)

        try:
            FoundIndex = self.secondLevelFolderList.index(str(ACTIVESUBTAB_NAME))
        except:
            FoundIndex = 0

        Folder_Lbl = QtWidgets.QLabel(self)
        Folder_Lbl.setText(" F o l d e r :  ")
        Folder_Lbl.setFont(QtGui.QFont('Candara', 7))
        Folder_Lbl.setFixedWidth(59)
        Folder_HLyt.addWidget(Folder_Lbl)

        self.Folder_Combo = QtWidgets.QComboBox()
        self.Folder_Combo.addItems(self.secondLevelFolderList)
        self.Folder_Combo.setFixedHeight(25)
        #self.Folder_Combo.setEditable(True)
        #self.Folder_Combo.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        #self.Folder_Combo.lineEdit().setFont(QtGui.QFont('Calibri', 9))
        #self.Folder_Combo.lineEdit().setReadOnly(True)
        #self.Folder_Combo.currentIndexChanged.connect(self.SET_Theme)
        self.Folder_Combo.setCurrentIndex(FoundIndex)
        Folder_HLyt.addWidget(self.Folder_Combo)

        Folder_HLyt.addSpacing(10)

        ## BTN ADD
        #self.Folder_Btn = QtWidgets.QPushButton()
        #self.Folder_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        #self.Folder_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        #self.Folder_Btn.setIcon(QtGui.QIcon(IconPath + "AddAsset2.png"))
        #self.Folder_Btn.clicked.connect(self.OpenLibFolder)
        #self.Folder_Btn.setToolTip("  Open Library Folder  ")
        #Folder_HLyt.addWidget(self.Folder_Btn)


        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)

        #######_______________________________________________// S E T  H O L E
        SetHole_Lyt = QtWidgets.QHBoxLayout()
        SetHole_Lyt.setSpacing(5)
        PLUG_MAINLyt.addLayout(SetHole_Lyt)


        self.SetHole_Btn = QtWidgets.QPushButton()
        self.SetHole_Btn.setObjectName("MasterBtn")
        self.SetHole_Btn.setText("SET HOLE")
        if HOLE_SET == 1:
            self.SetHole_Btn.setStyleSheet("QPushButton {color: #65BEF1; border-color: #65BEF1; }" )
        self.SetHole_Btn.setFixedHeight(30)
        self.SetHole_Btn.clicked.connect(self.set_Hole)
        self.SetHole_Btn.setToolTip("Create and Add asset to Library")
        SetHole_Lyt.addWidget(self.SetHole_Btn)

        ## BTN LIBRARY FOLDER
        self.HoldeDel_Btn = QtWidgets.QPushButton()
        self.HoldeDel_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.HoldeDel_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.HoldeDel_Btn.setIcon(QtGui.QIcon(IconPath + "delete_ON.png"))
        self.HoldeDel_Btn.clicked.connect(self.set_Hole_Delete)
        self.HoldeDel_Btn.setToolTip("  Open Library Folder  ")
        SetHole_Lyt.addWidget(self.HoldeDel_Btn)

        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)


        #######_______________________________________________// C O N C A V E
        ##FOLDER COMBO
        Concave_HLyt = QtWidgets.QHBoxLayout()
        Concave_HLyt.setSpacing(6)
        PLUG_MAINLyt.addLayout(Concave_HLyt)

        Concave_HLyt.addSpacing(25)


        ## BTN LIBRARY FOLDER
        self.Concave_Btn = QtWidgets.QPushButton()
        self.Concave_Btn.setFixedSize(iconButtonSize, iconButtonSize)
        self.Concave_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Concave_Btn.setIcon(QtGui.QIcon(IconPath + "Concave.png"))
        #self.Concave_Btn.clicked.connect(self.set_Hole_Delete)
        self.Concave_Btn.setToolTip("  Open Library Folder  ")
        Concave_HLyt.addWidget(self.Concave_Btn)



        Concave_Lbl = QtWidgets.QLabel(self)
        Concave_Lbl.setText(" Does the mesh have Concave borders?    Yes ")
        #Concave_Lbl.setFont(QtGui.QFont('Candara', 7))
        #Concave_Lbl.setFixedWidth(300)
        Concave_HLyt.addWidget(Concave_Lbl, alignment=QtCore.Qt.AlignRight)



        self.ClayRenderBTN = QtWidgets.QCheckBox()
        self.ClayRenderBTN.setFixedSize(iconButtonSize, iconButtonSize)
        self.ClayRenderBTN.setCheckable(1)
        #self.ClayRenderBTN.setChecked(CLAYRENDER)
        #self.ClayRenderBTN.toggled.connect(self.set_ClayRenderBTN)
        Concave_HLyt.addWidget(self.ClayRenderBTN)


        Concave_HLyt.addStretch()






        ##---------------------------------------------------- SEPARATOR : Horizontal
        PLUG_MAINLyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        PLUG_MAINLyt.addWidget(separator)
        PLUG_MAINLyt.addSpacing(2)

        ##_______________________________________ CREATE ASSET BTN
        CreateAssetBtn = QtWidgets.QPushButton()
        CreateAssetBtn.setObjectName("MasterBtn")
        CreateAssetBtn.setText(" - CREATE PLUG - ")
        CreateAssetBtn.setFixedHeight(30)
        CreateAssetBtn.clicked.connect(self.CREATE_PLUG)
        CreateAssetBtn.setToolTip("Create and Add asset to Library")
        PLUG_MAINLyt.addWidget(CreateAssetBtn)


        PLUG_MAINLyt.addStretch()
        #Folder_HLyt.addStretch()


    def set_Hole(self):
        self.SetHole_Btn.setStyleSheet("QPushButton {color: #65BEF1; border-color: #65BEF1; }")
        mc.sets(n = "Plug_Hole_set")
        mc.select(d = True)

    def set_Hole_Delete(self):
        self.SetHole_Btn.setStyleSheet("")

    def AssetNameValidate(self):
        AssetName = self.PlugNameField.text()
        if ":" in AssetName:
            PlugIt_Global.WarningWindow("You can't use ' : ' character in Asset Name", 250)
            return
        else:
            self.PlugNameField.clearFocus()

    def link_Tuto(self):
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("https://www.youtube.com/watch?v=ZSYQKoUaja4"))


    def GetComboTAB1(self):
        content = self.TAB1_Combo.currentText()
        self.secondLevelFolderList = os.listdir(LIBRARY_PATH + "/" + content)
        self.Folder_Combo.clear()
        self.Folder_Combo.addItems(self.secondLevelFolderList)

    def updatingProgressBar(self):
        self.step += 1
        self.progress_dialog.setLabelText("{0} : {1}(of {2})".format(self.opName,self.step, self.number_of_operations))
        self.progress_dialog.setValue(self.step)
        QtCore.QCoreApplication.processEvents()


    def CREATE_PLUG(self):
        #__________________________ V A R I A B L E S
        USER_PATH = PlugIt_Global.LIBRARY_PATH + "/USER/"
        get_PlugName = self.PlugNameField.text()
        get_FolderName = self.Folder_Combo.currentText()



        #__________________________U I  I N F O  V E R I F I C A T I O N S
        if get_PlugName == "":
            PlugIt_Global.WarningWindow("You should enter a Plug name", 250)
            return
        else:
            self.PlugNameField.clearFocus()

        if ":" in get_PlugName:
            PlugIt_Global.WarningWindow("You can't use ' : ' character in Plug Name", 250)
            return
        #try:  ## Check if Asset Already EXIST
        #    os.mkdir(PLUG_PATH)
        #except:
            #    PlugIt_Global.WarningWindow("A Plug with this name already exist in this folder", 400)
        #    return

        # __________________________P L U G  V E R I F I C A T I O N S
        # ______________________________ WARNINGS  -  SELECTION VERIF
        meshSelection = mc.ls(sl=True)
        if meshSelection == []:
            PlugIt_Global.WarningWindow("You should select your Plug Mesh", 400)
            return
        if len(meshSelection) > 1:
            PlugIt_Global.WarningWindow("Plug should be 1 mesh only", 300)
            return

        # ______________________________ MESH VERIF
        # Verif ExteriorBorder and InnerBorder
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.ConvertSelectionToEdgePerimeter()
        if len(mc.filterExpand(sm=32)) != 8:
            print("STOP - Borders Compromise")
            PlugIt_Global.WarningWindow("STOP - Borders Compromise. Verify there no extra vertex on red faces", 300)
            return

        #__________________________ P R O G R E S S B A R
        self.number_of_operations = 3
        self.step = 0
        self.opName = "Plug Creation Process Starting"
        self.progress_dialog = QtWidgets.QProgressDialog("Batch Process", "", 0, self.number_of_operations, self)
        self.progress_dialog.setWindowTitle("Plug Creation...")
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.setValue(0)
        self.progress_dialog.setMinimumSize(550, 80)
        self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        self.progress_dialog.show()



        # PROGRESBAR UPDATING
        self.updatingProgressBar()
        self.opName = "Arnold Thumb Render Start"

        # ______________________________ CLEAN MESH
        mc.move(0, 0, 0, meshSelection[0] + ".scalePivot", meshSelection[0] + ".rotatePivot", rpr=True)
        mc.makeIdentity(meshSelection, apply=True)
        mc.select(meshSelection)
        mc.delete(ch=True)
        mc.rename(meshSelection[0], "Plug_Mesh")
        mc.parent("Plug_controler", "Plug_Mesh")
        mc.delete("Plug_Mesh_grp")

        # ______________________________ SET CREATION
        # PROGRESBAR UPDATING
        self.updatingProgressBar()
        self.opName = "Arnold Thumb Render Start"

        # Plug_AllFaces_set
        mc.select("Plug_Mesh")
        mc.ConvertSelectionToFaces()
        mc.sets(n="Plug_AllFaces_set")

        # Plug_Selection_set
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.InvertSelection()
        mc.sets(n="Plug_Selection_set")

        # Plug_ExtraSecure_set
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.ConvertSelectionToEdgePerimeter()
        mc.sets(n="Plug_ExtraSecure_set")
        mc.select("Plug_EdgeBorder_set")
        mc.sets(rm="Plug_ExtraSecure_set")

        # ______________________________ COUNT NUMBER
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.GrowPolygonSelectionRegion()
        mc.ConvertSelectionToEdgePerimeter()
        mc.sets(n="Plug_borderCount_set")
        mc.select("Plug_EdgeBorder_set")
        mc.sets(rm="Plug_borderCount_set")
        mc.select("Plug_borderCount_set")
        plugBorderCount = len(mc.filterExpand(sm=32))
        mc.delete("Plug_borderCount_set")
        mc.createNode('transform', n='PlugIt_PlugCountNumber_' + str(plugBorderCount))

        # __________________ A R N O L D   T H U M B   R E N D E R


        mc.select("Plug_Mesh")
        mc.hyperShade(assign="PlugIt_Thumb_shd")
        mc.delete("BorderVerif_shd")

        PLUG_PATH = USER_PATH + get_FolderName + "/" + get_PlugName
        DESTPATH = PLUG_PATH + '/' + get_PlugName
        imgSize = 268

        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')  # Set curent render
        mc.setAttr('defaultArnoldDriver.aiTranslator', 'png', type='string')  # Set the TIF image format
        mc.setAttr('defaultArnoldDriver.prefix', DESTPATH, type='string')  # TO SAVE IMG TO DESTINATION PATH
        mc.setAttr('defaultArnoldRenderOptions.renderDevice', 0)  # CPU rendering

        mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)  # SAMPLING
        mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 2)
        mc.setAttr('defaultArnoldRenderOptions.GISpecularSamples', 2)
        mc.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', 0)
        mc.setAttr('defaultArnoldRenderOptions.GISssSamples', 0)
        mc.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 0)
        mc.setAttr('defaultArnoldRenderOptions.GIDiffuseDepth', 2)
        mc.setAttr("defaultResolution.width", imgSize)
        mc.setAttr("defaultResolution.height", imgSize)
        mc.setAttr("defaultResolution.deviceAspectRatio", 1)
        mc.setAttr("defaultResolution.pixelAspect", 1)

        mc.colorManagementPrefs(e=True, outputTransformEnabled=True, outputUseViewTransform=True)  # Color Management Prefs
        mc.arnoldRender(width=imgSize, height=imgSize, camera="PlugIt_RenderThumbCam")  # render and save the image

        # FIX "_1" naming :
        old_name = DESTPATH + '_1.png'
        new_name = DESTPATH + '.png'

        if os.path.exists(new_name):
            os.remove(new_name)
        os.rename(old_name, new_name)

        # ______________________________ ASSIGN SHADER
        mc.select("Plug_Mesh")
        mc.hyperShade(assign="PlugIt_Plug_Shd")

        # ______________________________ S A V E  P L U G
        mc.select("Plug_Mesh", "PlugIt_PlugCountNumber_*")
        mc.file(DESTPATH + ".ma", force=True, options="v = 0", type="mayaAscii", exportSelected=True)


        # __________________________ E N D I N G
        # PROGRESBAR UPDATING
        self.updatingProgressBar()
        self.opName = "Plug Created."
        self.progress_dialog.close()

        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        ui = PlugIt_UI.showUI()
        mc.flushUndo()






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

def atClose():
    if mc.window("Thumbnail Framing", exists=True):
        mc.deleteUI("Thumbnail Framing")


def showUI():
    ui = Dock(AddAsset_UI)
    ui.show()

    if mc.window("Thumbnail Framing", exists=True):
        mc.deleteUI("Thumbnail Framing")


    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "Windows_Ico2.png")
    # Assign the icon
    widget.setWindowIcon(icon)
    mc.scriptJob(uiDeleted=[WindowsTitle, atClose])

    return ui

