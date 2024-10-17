##--------------------------------------------------------------------------
## ScriptName : PlugIt
## Author     : Wizix
## LastUpdate : 13/02/23
## Version    : 3.0.2
##--------------------------------------------------------------------------
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
from . import PlugIt_Widgets
import importlib
importlib.reload(PlugIt_Widgets)
from . import PlugIt_Setting
importlib.reload(PlugIt_Setting)
from . import PlugIt_AddAsset
importlib.reload(PlugIt_AddAsset)
from . import PlugIt_NewTab
importlib.reload(PlugIt_NewTab)
from . import PlugIt_NewSecondTab
importlib.reload(PlugIt_NewSecondTab)
from . import PlugIt_SavePopUp
importlib.reload(PlugIt_SavePopUp)


##---------------------------------------------------------------------------------------------------------------- G L O B A L   V A R I A B L E S
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH
ACTIVESUBTAB = 0
ACTIVESUBTAB_NAME = ""
MAYA_VERSION = mc.about(v=True)
MAIN_TAB_OPEN =(json.load(open(PreferencePath + 'TAB_MAIN_ID.json',"r"))['VALUE'])
if MAIN_TAB_OPEN ==0:
    TAB_OPEN_SECOND = (json.load(open(PreferencePath + 'TAB_PLUGIT_SECOND_ID.json',"r"))['VALUE'])
else:
    TAB_OPEN_SECOND = (json.load(open(PreferencePath + 'TAB_USER_SECOND_ID.json',"r"))['VALUE'])

##---------------------------------------------------------------------------------------------------------------- B U I L D   U I
class PlugIt_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PlugIt_UI, self).__init__()
        self.allListWidets = []
        self.setMinimumSize(300, 400)
        self.buildUI()
        self.firstTab.setCurrentIndex(MAIN_TAB_OPEN)
        self.secondTab.setCurrentIndex(TAB_OPEN_SECOND)
        open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": 1111}))

    def buildUI(self):
        ##_________________________________________________________________________________ UI VALUE
        self.setStyleSheet(PlugIt_Global.Theme)
        iconButtonSize = PlugIt_Global.IconButtonSize
        separatorWidth = 1

        ##_________________________________________________________________________________ LAYOUTS
        self.MAIN_Lyt = QtWidgets.QVBoxLayout()
        self.setLayout(self.MAIN_Lyt)
        self.MAIN_Lyt.setContentsMargins(6, 6, 6, 6)
        self.TOOLBAR_HLyt = QtWidgets.QHBoxLayout()
        self.MAIN_Lyt.addLayout(self.TOOLBAR_HLyt)

        ##_________________________________________________________________________________ TOOLBAR
        ## BTN SETTING
        self.SettingBTN = QtWidgets.QPushButton()
        self.SettingBTN.setFixedSize(iconButtonSize,iconButtonSize)
        self.SettingBTN.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.SettingBTN.setIcon(QtGui.QIcon(IconPath + "BatchProcess.png"))
        self.SettingBTN.clicked.connect(self.Setting_Window)
        self.SettingBTN.setToolTip("  Setting Window  ")
        self.TOOLBAR_HLyt.addWidget(self.SettingBTN)

        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        self.TOOLBAR_HLyt.addWidget(self.Separator)

        ## BTN UNDO PLUG
        self.UndoPlug_Btn = QtWidgets.QPushButton()
        self.UndoPlug_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.UndoPlug_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.UndoPlug_Btn.setIcon(QtGui.QIcon(IconPath + "Undo_ON.png"))
        self.UndoPlug_Btn.clicked.connect(self.UndoPlug)
        self.UndoPlug_Btn.setToolTip("  Undo last Plug  ")
        self.TOOLBAR_HLyt.addWidget(self.UndoPlug_Btn)


        ## BTN LIBRARY FOLDER
        self.LibFolderBTN = QtWidgets.QPushButton()
        self.LibFolderBTN.setFixedSize(iconButtonSize,iconButtonSize)
        self.LibFolderBTN.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.LibFolderBTN.setIcon(QtGui.QIcon(IconPath + "Folder2.png"))
        self.LibFolderBTN.clicked.connect(self.OpenLibFolder)
        self.LibFolderBTN.setToolTip("  Open Library Folder  ")
        self.TOOLBAR_HLyt.addWidget(self.LibFolderBTN)



        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        self.TOOLBAR_HLyt.addWidget(self.Separator)

        PLUG_MODE = (json.load(open(PreferencePath + 'PLUG_MODE.json', "r"))['VALUE'])
        ## MODE  :  CLASSIC
        self.ModeClassic_Btn = QtWidgets.QPushButton()
        self.ModeClassic_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.ModeClassic_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        if PLUG_MODE == 0:
            self.ModeClassic_Btn.setIcon(QtGui.QIcon(IconPath + "Plug_Mode_ON.png"))
        else:
            self.ModeClassic_Btn.setIcon(QtGui.QIcon(IconPath + "Plug_Mode_OFF.png"))
        self.ModeClassic_Btn.clicked.connect(self.set_ModeClassic)
        self.ModeClassic_Btn.setToolTip("  Classic Mode : Insert Plugs on clean mesh with options  ")
        self.TOOLBAR_HLyt.addWidget(self.ModeClassic_Btn)

        ## MODE  :  x1
        self.ModeX1_Btn = QtWidgets.QPushButton()
        self.ModeX1_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.ModeX1_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        if PLUG_MODE == 1:
            self.ModeX1_Btn.setIcon(QtGui.QIcon(IconPath + "x1Mode_ON.png"))
        else:
            self.ModeX1_Btn.setIcon(QtGui.QIcon(IconPath + "x1Mode_OFF.png"))
        self.ModeX1_Btn.clicked.connect(self.set_ModeX1)
        self.ModeX1_Btn.setToolTip("  x1 Mode : Quick one click insert Plugs on one face ")
        self.TOOLBAR_HLyt.addWidget(self.ModeX1_Btn)

        ## MODE  :  DRAG
        self.ModeDrag_Btn = QtWidgets.QPushButton()
        self.ModeDrag_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.ModeDrag_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        if PLUG_MODE == 2:
            self.ModeDrag_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_ON.png"))
        else:
            self.ModeDrag_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_OFF.png"))
        self.ModeDrag_Btn.clicked.connect(self.set_ModeDrag)
        self.ModeDrag_Btn.setToolTip("  Drag Mode : Drag Plug placement on NGon face // SHIFT = Scale // CTRL = Rotate  ")
        
        VERSION = mc.about(v=True)  #WAITING FOR PYMEL 2024 SUPPORT
        if VERSION == "2024":
            pass
        else:
            self.TOOLBAR_HLyt.addWidget(self.ModeDrag_Btn)



        ## SEPARATOR
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        self.TOOLBAR_HLyt.addWidget(self.Separator)

        ## BTN CREATE PLUG
        self.CreatePlugBTN = QtWidgets.QPushButton()
        self.CreatePlugBTN.setFixedSize(iconButtonSize,iconButtonSize)
        self.CreatePlugBTN.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.CreatePlugBTN.setIcon(QtGui.QIcon(IconPath + "AddAsset2.png"))
        self.CreatePlugBTN.setToolTip("  Create Plug  ")
        self.CreatePlugBTN.clicked.connect(self.SavedBefore_PlugCreation)
        self.TOOLBAR_HLyt.addWidget(self.CreatePlugBTN, alignment=QtCore.Qt.AlignRight)

        ##---------------------------------------------------- SEPARATOR : Horizontal
        self.MAIN_Lyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(1)
        self.MAIN_Lyt.addWidget(separator)
        self.MAIN_Lyt.addSpacing(2)

        ##----------------------------------------------------------------------------------------/  D R A G  M O D E  :  O P T I O N  B A R
        self.DragMode_WIDGET = QtWidgets.QWidget()
        self.MAIN_Lyt.addWidget(self.DragMode_WIDGET)

        self.DragMode_VMAINLyt = QtWidgets.QVBoxLayout(self.DragMode_WIDGET)
        self.DragMode_VMAINLyt.setContentsMargins(0, 0, 0, 0)

        self.DragMode_HLyt = QtWidgets.QHBoxLayout()
        self.DragMode_VMAINLyt.addLayout(self.DragMode_HLyt)


        self.DragMode_HLyt.setContentsMargins(0, 0, 0, 0)
        self.DragMode_HLyt.setSpacing(5)#          BETWEEN SECTIONS
        self.DragMode_HLyt.setAlignment(QtCore.Qt.AlignTop)

        ## BTN FLIP
        DRAGMODE_FLIP = (json.load(open(PreferencePath + 'DRAGMODE_Flip.json', "r"))['VALUE'])
        self.DragOption_Flip_Btn = QtWidgets.QPushButton()
        self.DragOption_Flip_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.DragOption_Flip_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        if DRAGMODE_FLIP == 0:
            self.DragOption_Flip_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_FlipOption_OFF.png"))
        else:
            self.DragOption_Flip_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_FlipOption_ON.png"))
        self.DragOption_Flip_Btn.clicked.connect(self.set_ModeDrag_Flip)
        self.DragOption_Flip_Btn.setToolTip("  Positive or Negative Plug  ")
        self.DragMode_HLyt.addWidget(self.DragOption_Flip_Btn)



        ## Separator : Vertical
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        self.DragMode_HLyt.addWidget(self.Separator)



        ##_________________________________________________________________________________ ## SCALE SLIDER
        DRAGMODE_SIZE = (json.load(open(PreferencePath + 'DRAGMODE_Size.json', "r"))['VALUE'])
        ##------------------------------------------------------------: LABEL
        Scale_Label = QtWidgets.QLabel("Size : ")
        Scale_Label.setStyleSheet("color:#909090;")
        Scale_Label.setFont(QtGui.QFont('Calibri', 9))
        self.DragMode_HLyt.addWidget(Scale_Label)
        ##------------------------------------------------------------: SLIDER
        self.Scale_Slider = QtWidgets.QSlider()
        self.Scale_Slider.setMinimum(10)
        self.Scale_Slider.setMaximum(1000)
        self.Scale_Slider.setProperty("value", DRAGMODE_SIZE*100)
        self.Scale_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Scale_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Scale_Slider.setTickInterval(1)
        self.Scale_Slider.setFixedHeight(22)
        self.Scale_Slider.valueChanged.connect(self.set_Slider)
        self.DragMode_HLyt.addWidget(self.Scale_Slider)
        ##------------------------------------------------------------: SPINBOX
        self.Scale_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Scale_SpinBox.setDecimals(2)
        self.Scale_SpinBox.setFixedWidth(45)
        self.Scale_SpinBox.setFixedHeight(18)
        self.Scale_SpinBox.setRange(0.1, 1000)
        self.Scale_SpinBox.setValue(DRAGMODE_SIZE)
        self.Scale_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Scale_SpinBox.editingFinished.connect(self.set_SpinBox)
        self.DragMode_HLyt.addWidget(self.Scale_SpinBox)



        ##_________________________________________________________________________________ ROTATE LINE
        self.DragMode_HLyt2 = QtWidgets.QHBoxLayout()
        self.DragMode_VMAINLyt.addLayout(self.DragMode_HLyt2)

        self.DragMode_HLyt2.setContentsMargins(0, 0, 0, 0)
        self.DragMode_HLyt2.setSpacing(5)#          BETWEEN SECTIONS
        self.DragMode_HLyt2.setAlignment(QtCore.Qt.AlignTop)

        ## BTN ROTATE STEP
        self.DragOption_Rotate_Btn = QtWidgets.QPushButton()
        self.DragOption_Rotate_Btn.setFixedSize(iconButtonSize,iconButtonSize)
        self.DragOption_Rotate_Btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.DragOption_Rotate_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_RotateStep_ON.png"))
        self.DragOption_Rotate_Btn.clicked.connect(self.set_Defualt15Rotate)
        self.DragOption_Rotate_Btn.setToolTip("  Set Rotate Step to Default 15°  ")
        self.DragMode_HLyt2.addWidget(self.DragOption_Rotate_Btn)

        ## Separator : Vertical
        self.Separator = QtWidgets.QPushButton()
        self.Separator.setFixedSize(separatorWidth,iconButtonSize)
        self.Separator.setObjectName("Separator")
        self.Separator.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Separator.setIcon(QtGui.QIcon(IconPath + "SeparatorBtn.png"))
        self.Separator.setEnabled(0)
        self.DragMode_HLyt2.addWidget(self.Separator)

        DRAGMODE_ROTATE = (json.load(open(PreferencePath + 'DRAGMODE_Rotate.json', "r"))['VALUE'])
        ##------------------------------------------------------------: LABEL
        Rotation_Label = QtWidgets.QLabel("Rotation Step : ")
        Rotation_Label.setStyleSheet("color:#909090;")
        Rotation_Label.setFont(QtGui.QFont('Calibri', 9))
        self.DragMode_HLyt2.addWidget(Rotation_Label)
        ##------------------------------------------------------------: SLIDER
        self.Rotation_Slider = QtWidgets.QSlider()
        self.Rotation_Slider.setMinimum(1)
        self.Rotation_Slider.setMaximum(9000)
        self.Rotation_Slider.setProperty("value", DRAGMODE_ROTATE*100)
        self.Rotation_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Rotation_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Rotation_Slider.setTickInterval(1)
        self.Rotation_Slider.setFixedHeight(22)
        self.Rotation_Slider.valueChanged.connect(self.set_Slider_Rotate)
        self.DragMode_HLyt2.addWidget(self.Rotation_Slider)
        ##------------------------------------------------------------: SPINBOX
        self.Rotation_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Rotation_SpinBox.setDecimals(0)
        self.Rotation_SpinBox.setFixedWidth(45)
        self.Rotation_SpinBox.setFixedHeight(18)
        self.Rotation_SpinBox.setRange(1, 9000)
        self.Rotation_SpinBox.setValue(DRAGMODE_ROTATE)
        self.Rotation_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Rotation_SpinBox.editingFinished.connect(self.set_SpinBox_Rotate)
        self.DragMode_HLyt2.addWidget(self.Rotation_SpinBox)









        ##_________________________________________________________________________________ OPTION HIDE/SHOW
        DRAGMODE_VISIBILITY = (json.load(open(PreferencePath + 'DRAGMODE_Widget.json', "r"))['VALUE'])
        if DRAGMODE_VISIBILITY == 0:
            self.DragMode_WIDGET.hide()
        else:
            self.DragMode_WIDGET.show()




        

        ##_________________________________________________________________________________ TABS
        self.firstTab = QtWidgets.QTabWidget(self)
        try:
            self.firstLevelFolderList = os.listdir(LIBRARY_PATH)
        except:
            os.mkdir(str(LIBRARY_PATH))
            os.mkdir(str(LIBRARY_PATH) + "/MAINTAB")
            os.mkdir(str(LIBRARY_PATH) + "/MAINTAB" + "/SecondTab")
            self.firstLevelFolderList = os.listdir(LIBRARY_PATH)
            PlugIt_Global.WarningWindow("The Script lost link to your Asset Library folder. A default new one is create.", 500)

        #EMPTY FOLDER CHOOSEN
        if self.firstLevelFolderList == [] :
            os.mkdir(str(LIBRARY_PATH) + "/MAINTAB")
            os.mkdir(str(LIBRARY_PATH) + "/MAINTAB" + "/SecondTab")
            from . import PlugIt_UI
            import importlib
            importlib.reload(PlugIt_UI)
            PlugIt_UI.showUI()

        #FIRST LEVEL TABS
        for i in self.firstLevelFolderList:
            firstTab_path = LIBRARY_PATH + "/" + i
            try:
                self.secondLevelFolderList = os.listdir(firstTab_path)
                self.secondTab = QtWidgets.QTabWidget(self)
                if self.secondLevelFolderList == []:
                    os.mkdir(str(firstTab_path) + "/SecondTab")
                    from . import PlugIt_UI
                    import importlib
                    importlib.reload(PlugIt_UI)
                    PlugIt_UI.showUI()
                #SECOND LEVEL TABS
                for j in self.secondLevelFolderList:
                    secondTab_path = firstTab_path + "/" + j
                    os.listdir(secondTab_path)
                    widget = PlugIt_Widgets.PlugIt_ListWidget(path=secondTab_path, parent=self)
                    self.allListWidets.append(widget)
                    self.addTabAuto(parentTabWidget=self.secondTab, childWidget=widget, tabName=j)
                    self.secondTab.setCurrentIndex(TAB_OPEN_SECOND)

                #ADD TABS BUTTON SECOND TAB
                plus_lb2 = QtWidgets.QLabel("")
                self.secondTab.addTab(plus_lb2, "+")
                plus_index2 = self.secondTab.indexOf(plus_lb2)
                self.secondTab.setTabEnabled(plus_index2, True)
                self.addTabAuto(parentTabWidget=self.firstTab, childWidget=self.secondTab, tabName=i)
                self.secondTab.currentChanged.connect(partial(self.get_SubTabIndex, self.secondTab))
                self.secondTab.currentChanged.connect(self.SaveTabChange)
                self.secondTab.currentChanged.connect(self.Add_New_Second_Tabs)

            except:
                widget = PlugIt_Widgets.PlugIt_ListWidget(path=firstTab_path, parent=self)
                self.allListWidets.append(widget)
                self.addTabAuto(parentTabWidget=self.firstTab, childWidget=widget, tabName=i)


        ##TABS SETTING
        self.firstTab.currentChanged.connect(self.SaveTabChange)
        self.secondTab.currentChanged.connect(self.Add_New_Tabs)
        self.MAIN_Lyt.addWidget(self.firstTab)

        ##_________________________________________________________________________________ TAB FAVOURITE
        favouriteFilePath = ASSET_FAVOURITES_PATH
        with open(favouriteFilePath, 'r+') as file:
            pathString = file.read()
        self.favouritesWidget = PlugIt_Widgets.PlugIt_ListWidget(path=pathString, parent=self)
        self.allListWidets.append(self.favouritesWidget)
        self.firstTab.addTab(self.favouritesWidget, "❤")

        ##_________________________________________________________________________________ SLIDER
        SliderUserPref = open(PreferencePath + 'SliderUserPref.json', "r")
        SliderUserValue_pref = json.load(SliderUserPref)
        SLIDER_VALUE = (SliderUserValue_pref['SLIDER_VALUE'])

        self.sizeSlider = QtWidgets.QSlider()
        self.sizeSlider.setMaximum(18)#18
        self.sizeSlider.setMinimum(5)#6
        self.sizeSlider.setProperty("value", SLIDER_VALUE)
        self.sizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sizeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sizeSlider.setTickInterval(1)
        self.sizeSlider.valueChanged.connect(self.adjustIconSize)
        self.adjustIconSize()
        self.MAIN_Lyt.addWidget(self.sizeSlider)




##_________________________________________________________
##____________________________________________________________________________________________________ DEFINITIONS
##_________________________________________________________
    def SavedBefore_PlugCreation(self):
        ArnoldIsLoad = mc.pluginInfo("mtoa.mll", query=True, loaded=True)
        if ArnoldIsLoad == False:
            PlugIt_Global.WarningWindow("Arnold Mtoa Module should be load to create Plug")
       # if mc.objExists("PlugIt_ThumbScene"):
        #    importlib.reload(PlugIt_AddAsset)
         #   PlugIt_AddAsset.showUI()
        else:
            PlugIt_SavePopUp.showUI()




    def set_ModeClassic(self):
        open(PreferencePath + 'PLUG_MODE.json', "w").write(json.dumps({"VALUE" : 0}))
        self.ModeClassic_Btn.setIcon(QtGui.QIcon(IconPath + "Plug_Mode_ON.png"))
        self.ModeX1_Btn.setIcon(QtGui.QIcon(IconPath + "x1Mode_OFF.png"))
        self.ModeDrag_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_OFF.png"))

        self.DragMode_WIDGET.hide()
        open(PreferencePath + 'DRAGMODE_Widget.json', "w").write(json.dumps({"VALUE": 0}))

        SCRIPT_JOB_PREVIOUS = (json.load(open(PreferencePath + 'ScriptJob_1x1.json', "r"))['VALUE'])
        if SCRIPT_JOB_PREVIOUS == 1111:
            pass
        else:
            mc.scriptJob(kill=SCRIPT_JOB_PREVIOUS, force=True)
            open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": 1111}))



    def set_ModeX1(self):
        #if MAYA_VERSION == "2022":
        #    PlugIt_Global.WarningWindow("The x1 mode can only works with Maya 2023 version and higher.", 500)
        #else:
        open(PreferencePath + 'PLUG_MODE.json', "w").write(json.dumps({"VALUE" : 1}))
        self.ModeClassic_Btn.setIcon(QtGui.QIcon(IconPath + "Plug_Mode_OFF.png"))
        self.ModeX1_Btn.setIcon(QtGui.QIcon(IconPath + "x1Mode_ON.png"))
        self.ModeDrag_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_OFF.png"))

        self.DragMode_WIDGET.hide()
        open(PreferencePath + 'DRAGMODE_Widget.json', "w").write(json.dumps({"VALUE": 1}))





    def set_ModeDrag(self):
        open(PreferencePath + 'PLUG_MODE.json', "w").write(json.dumps({"VALUE" : 2}))
        self.ModeClassic_Btn.setIcon(QtGui.QIcon(IconPath + "Plug_Mode_OFF.png"))
        self.ModeX1_Btn.setIcon(QtGui.QIcon(IconPath + "x1Mode_OFF.png"))
        self.ModeDrag_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_ON.png"))

        self.DragMode_WIDGET.show()
        open(PreferencePath + 'DRAGMODE_Widget.json', "w").write(json.dumps({"VALUE": 2}))

        SCRIPT_JOB_PREVIOUS = (json.load(open(PreferencePath + 'ScriptJob_1x1.json', "r"))['VALUE'])
        if SCRIPT_JOB_PREVIOUS == 1111:
            pass
        else:
            mc.scriptJob(kill=SCRIPT_JOB_PREVIOUS, force=True)
            open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": 1111}))

    def set_ModeDrag_Flip(self):
        DRAGMODE_FLIP = (json.load(open(PreferencePath + 'DRAGMODE_Flip.json', "r"))['VALUE'])

        if DRAGMODE_FLIP == 0:
            open(PreferencePath + 'DRAGMODE_Flip.json', "w").write(json.dumps({"VALUE" : 1}))
            self.DragOption_Flip_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_FlipOption_ON.png"))
        else:
            open(PreferencePath + 'DRAGMODE_Flip.json', "w").write(json.dumps({"VALUE": 0}))
            self.DragOption_Flip_Btn.setIcon(QtGui.QIcon(IconPath + "DragMode_FlipOption_OFF.png"))



    def set_Slider(self):
        SliderValue = self.Scale_Slider.value()/100
        self.Scale_SpinBox.setValue(SliderValue)
        open(PreferencePath + 'DRAGMODE_Size.json', "w").write(json.dumps({"VALUE": SliderValue}))

    def set_SpinBox(self):
        SpinBoxAValue = self.Scale_SpinBox.value()*100
        self.Scale_Slider.setValue(SpinBoxAValue)
        self.Scale_SpinBox.clearFocus()


    def set_Slider_Rotate(self):
        SliderValue = self.Rotation_Slider.value()/100
        self.Rotation_SpinBox.setValue(SliderValue)
        open(PreferencePath + 'DRAGMODE_Rotate.json', "w").write(json.dumps({"VALUE": SliderValue}))

    def set_SpinBox_Rotate(self):
        SpinBoxAValue = self.Rotation_SpinBox.value()*100
        self.Rotation_Slider.setValue(SpinBoxAValue)
        self.Rotation_SpinBox.clearFocus()

    def set_Defualt15Rotate(self):
        open(PreferencePath + 'DRAGMODE_Rotate.json', "w").write(json.dumps({"VALUE": 15}))
        self.Rotation_Slider.setProperty("value", 1500)


    def UndoPlug(self):
        mc.undoInfo(openChunk=True, infinity=True, chunkName="UndoPlug")

        if mc.objExists("PlugItDupSave_*"):

            mc.select("PlugItDupSave_*")
            meshSelect = mc.ls(sl=True)[0]
            mc.setAttr(meshSelect + ".hiddenInOutliner", 0)
            mel.eval("AEdagNodeCommonRefreshOutliners();")
            meshName = meshSelect.split("PlugItDupSave_")[1]

            mc.select(meshSelect)
            mc.FreezeTransformations()
            mc.select(meshSelect, meshName)
            mc.MatchTransform()

            mc.delete(meshName)
            mc.select(meshSelect)
            mc.ShowSelectedObjects()
            mc.rename(meshSelect, meshName)
            mc.select(d=True)

            if mc.objExists("P_Creation_Ctrl"):
                mc.delete("P_Creation_Ctrl")
            if mc.objExists("Plug_AllFaces_set"):
                mc.delete("Plug_AllFaces_set")
            if mc.objExists("Plug_EdgeBorder_set"):
                mc.delete("Plug_EdgeBorder_set")
            if mc.objExists("Plug_Selection_set"):
                mc.delete("Plug_Selection_set")
            if mc.objExists("PlugIt_Plug_Shd"):
                mc.delete("PlugIt_Plug_Shd")

        else:
            print("No Undo Possible")


        mc.undoInfo(closeChunk=True, chunkName="UndoPlug")

    def SaveTabChange(self):
        getFirstTabIndex = self.firstTab.currentIndex()
        getTabName = self.firstTab.tabText(getFirstTabIndex)

        FirstTabinfoToSave = {"VALUE" : getFirstTabIndex}
        s = json.dumps(FirstTabinfoToSave)
        open(PreferencePath + 'TAB_MAIN_ID.json', "w").write(s)

        FavTabSave = {"TAB_ACTIVE_NAME" : str(getTabName)}
        s = json.dumps(FavTabSave)
        open(PreferencePath + 'KnowFavTab.json', "w").write(s)

        if getFirstTabIndex == 0:
            getSecondTabIndex = int(ACTIVESUBTAB)
            SecondTabinfoToSave = {"VALUE" : getSecondTabIndex}
            s = json.dumps(SecondTabinfoToSave)
            open(PreferencePath + 'TAB_PLUGIT_SECOND_ID.json', "w").write(s)

        else:
            getSecondTabIndex = int(ACTIVESUBTAB)
            SecondTabinfoToSave = {"VALUE" : getSecondTabIndex}
            s = json.dumps(SecondTabinfoToSave)
            open(PreferencePath + 'TAB_USER_SECOND_ID.json', "w").write(s)

    def addTabAuto(self, parentTabWidget, childWidget, tabName, insert=False):
        if insert:
            parentTabWidget.insertTab(parentTabWidget.count()-3, childWidget, tabName)
        else:
            parentTabWidget.addTab(childWidget, tabName)
        index = parentTabWidget.indexOf(childWidget)

    def tabPlusButtonClicked(self, parentTabWidget, index):
        self.tabMenu.popup(QtGui.QCursor.pos(), None)
        self.closeAction.triggered.connect(partial(self.closeTab, parentTabWidget, index))

    def mousePressEvent(self, event):
        # Override the default Qt function to clearFocus when the clicked widget is not a QLineEdit
        focused_widget = QtWidgets.QApplication.focusWidget()
        if isinstance(focused_widget, QtWidgets.QLineEdit):
            focused_widget.clearFocus()
            QtWidgets.QMainWindow.mousePressEvent(self, event)



    def QlineEditClear(self):
        self.researchBar.clearFocus()

    def adjustIconSize(self):
        iconSize = self.sizeSlider.value() * 14
        gridSize = iconSize + 5
        for i in self.allListWidets:
            try:
                i.setGridSize(QtCore.QSize(gridSize, gridSize))
                for g in i.buttons:
                   g.setIconSize(QtCore.QSize(iconSize, iconSize))

                SliderValueInfoToSave = {"SLIDER_VALUE": self.sizeSlider.value()}
                s = json.dumps(SliderValueInfoToSave)
                open(PreferencePath + 'SliderUserPref.json', "w").write(s)
            except:
                pass


    def Setting_Window(self):
       PlugIt_Setting.showUI()

    def Refresh(self):
        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        ui = PlugIt_UI.showUI()

    def OpenLibFolder(self):
        os.startfile(LIBRARY_PATH)

    def Add_New_Tabs(self):
        NumberOfFolder = len(os.listdir(LIBRARY_PATH))
        indexValue = int(NumberOfFolder)+2
        if self.firstTab.currentIndex() == indexValue:
            self.firstTab.setCurrentIndex(0)
            PlugIt_NewTab.showUI()

    def get_SubTabIndex(self, tab, *args):
        global ACTIVESUBTAB
        global ACTIVESUBTAB_NAME

        SUBINDEX = str(tab.currentIndex())
        SUBINDEX_NAME = tab.tabText(int(SUBINDEX))

        ACTIVESUBTAB = SUBINDEX
        ACTIVESUBTAB_NAME = SUBINDEX_NAME

        return ACTIVESUBTAB + ACTIVESUBTAB_NAME

    def Add_New_Second_Tabs(self):
        FirstTabIndex = self.firstTab.currentIndex()
        FirstTabName = self.firstTab.tabText(FirstTabIndex)

        NumberOfFolder = len(os.listdir(LIBRARY_PATH + "/" + FirstTabName))
        indexValue = int(NumberOfFolder)

        if ACTIVESUBTAB_NAME == "+" :
            self.secondTab.setCurrentIndex(0)
            PlugIt_NewSecondTab.showUI(FirstTabName)


    def PLUG(self):
        from . import PlugIt_Plug
        importlib.reload(PlugIt_Plug)
        PlugIt_Plug.showUI()


def initSceneFirstPlugBug():
    print("LAUCHN INIT SCENE")

    mc.polyCube(n ="PlugIt_InitCube", w =10, h= 10, d= 10, sx= 4, sy= 4, sz= 4)
    mc.select ("PlugIt_InitCube.f[22]")

    from . import PlugIt_Plug
    importlib.reload(PlugIt_Plug)

    PlugIt_Plug.INIT_PERFORM_PLUG(LIBRARY_PATH + "/PLUGIT/1 - Round/Plug_Circle_01/Plug_Circle_01.ma", 1, 4)


    #CLEAN
    if mc.objExists("PlugIt_InitCube"):
        mc.delete("PlugIt_InitCube")
    if mc.objExists("Plug_Mesh"):
        mc.delete("Plug_Mesh")
    if mc.objExists("PlugIt_FlipY_info"):
        mc.delete("PlugIt_FlipY_info")


    print("LAUCHN INIT SCENE - DONE")
    return


def Dock(Widget, width=200, height=200, hp="free", show=True):
    name = PlugIt_Global.PlugItTitle
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
    if mc.window("P L U G  -  O p t i o n s", exists=True):
        mc.deleteUI("P L U G  -  O p t i o n s")

    if mc.window("Plug Creation", exists=True):
        mc.deleteUI("Plug Creation")

    if mc.objExists("PlugIt_Thumb_Group"):
        mc.delete("PlugIt_Thumb_Group")

    SCRIPT_JOB_PREVIOUS = (json.load(open(PreferencePath + 'ScriptJob_1x1.json', "r"))['VALUE'])
    if SCRIPT_JOB_PREVIOUS == 1111:
        pass
    else:
        mc.scriptJob(kill=SCRIPT_JOB_PREVIOUS, force=True)
        open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": 1111}))



def showUI():
    ui = Dock(PlugIt_UI)
    ui.show()

    #FirstLaunch = (json.load(open(PreferencePath + 'FirstLaunch.json', "r"))['VALUE'])
    #if FirstLaunch == 0:
        #open(PreferencePath + 'FirstLaunch.json', "w").write(json.dumps({"VALUE": 1}))
        #PyMel Test
        #try:
            #import pymel.core as pm
            #pm.sphere(n="PlugIt_PyMel_Check")
            #pm.delete("PlugIt_PyMel_Check")
        #except:
            #WarningWindow("You don't have PyMel install. You should install PyMel using this link : ", 450)
            #return



    ##DELETE PopUp UI
    if mc.window("P L U G  -  O p t i o n s", exists=True):
        mc.deleteUI("P L U G  -  O p t i o n s")

    ##CLEAN Scene
    if mc.objExists("PlugIt_Thumb_Group"):
        mc.delete("PlugIt_Thumb_Group")

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(PlugIt_Global.PlugItTitle)
    try:
        widget = wrapInstance(int(qw), QWidget)
        # Create a QIcon object
        icon = QIcon(IconPath + "PlugIt_Window_Ico.png")
        # Assign the icon
        widget.setWindowIcon(icon)
    except:
        pass #Pour si on reload alos qu'il est dock


    mc.setToolTo("Move")
    mc.scriptJob(uiDeleted=[PlugIt_Global.PlugItTitle, atClose])

    return ui





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
    mc.button(l="Install PyMel", c= PyMelLink)
    mc.window("WarningWindow", e=True, wh=(size, 80))

    qw = omui.MQtUtil.findWindow("WarningWindow")
    widget = wrapInstance(int(qw), QWidget)
    icon = QIcon(IconPath + "Windows_Ico_Warning.png")
    widget.setWindowIcon(icon)

    mc.showWindow()

def PyMelLink(*args):
    QtGui.QDesktopServices.openUrl(
        QtCore.QUrl("https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2022/ENU/Maya-Scripting/files/GUID-2AA5EFCE-53B1-46A0-8E43-4CD0B2C72FB4-htm.html"))



initSceneFirstPlugBug()
