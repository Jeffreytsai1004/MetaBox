##--------------------------------------------------------------------------
## ScriptName : ModIt 3.0
## Author     : Wizix
## StartDate : 2022/09/09
## LastUpdate : 2022/13/09
## Version    : 0.0.1
##-------------------------------------------------------------------------- I M P O R T
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat
import os
from maya import OpenMayaUI as omui
from functools import partial
# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
##---------------------------------------- Import Modules
import importlib
from .. import ModIt_Global
importlib.reload(ModIt_Global)
from .. import ModIt_CSS
importlib.reload(ModIt_CSS)
##---------------------------------------- Import Classes


##-------------------------------------------------------------------------- G L O B A L   V A R
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath

WindowsTitle = "Bevel2"

BevelA = ""
BevelB = ""

##UI INFO
# ________________//
# ___________________________________________
# ________________//
def SEND_INFO(BevelA_node, BevelB_node):
    global BevelA
    BevelA = BevelA_node

    global BevelB
    BevelB = BevelB_node

    return BevelA + BevelB


class Bevel2_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Bevel2_UI, self).__init__()
        self.setMinimumSize(420, 100)
        self.buildUI()

        #Wireframe OnSHade ON
        viewport = mc.getPanel(withFocus=True)
        mc.modelEditor(viewport, edit=True, wireframeOnShaded=True)

    def buildUI(self):
        ##UI - Preferences
        iconButtonSize = 10

        # ________________//
        # ___________________________________________## UI
        # ________________//
        BEVELS2_MLyt = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(ModIt_Global.Theme)


        Title = QtWidgets.QLabel(" - M i x e d  B e v e l s  -  ")
        Title.setAlignment(QtCore.Qt.AlignCenter)
        BEVELS2_MLyt.addWidget(Title)
        BEVELS2_MLyt.addSpacing(10)



        # ___________________________________________## BEVEL A
        SliderA_HLyt = QtWidgets.QHBoxLayout(self)
        BEVELS2_MLyt.addLayout(SliderA_HLyt)

        BevA_Title = QtWidgets.QLabel(" - Bevel A ")
        SliderA_HLyt.addWidget(BevA_Title)

        self.BevelA_Slider = QtWidgets.QSlider()
        self.BevelA_Slider.setMinimum(1)
        self.BevelA_Slider.setMaximum(95)
        self.BevelA_Slider.setProperty("value", 50)
        self.BevelA_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.BevelA_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.BevelA_Slider.setTickInterval(1)
        self.BevelA_Slider.setFixedHeight(22)
        self.BevelA_Slider.valueChanged.connect(self.SliderA_Action)
        SliderA_HLyt.addWidget(self.BevelA_Slider)


        self.BevelA_SpinBox = QtWidgets.QDoubleSpinBox()
        self.BevelA_SpinBox.setDecimals(2)
        self.BevelA_SpinBox.setFixedWidth(40)
        self.BevelA_SpinBox.setFixedHeight(18)
        self.BevelA_SpinBox.setRange(0.01, 0.95)
        self.BevelA_SpinBox.setValue(0.5)
        self.BevelA_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.BevelA_SpinBox.editingFinished.connect(self.SpinBoxA_Action)
        SliderA_HLyt.addWidget(self.BevelA_SpinBox)



        BEVELS2_MLyt.addSpacing(5)

        # ___________________________________________## BEVEL B
        SliderB_HLyt = QtWidgets.QHBoxLayout(self)
        BEVELS2_MLyt.addLayout(SliderB_HLyt)

        BevB_Title = QtWidgets.QLabel(" - Bevel B ")
        SliderB_HLyt.addWidget(BevB_Title)

        self.BevelB_Slider = QtWidgets.QSlider()
        self.BevelB_Slider.setMinimum(1)
        self.BevelB_Slider.setMaximum(95)
        self.BevelB_Slider.setProperty("value", 50)
        self.BevelB_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.BevelB_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.BevelB_Slider.setTickInterval(1)
        self.BevelB_Slider.setFixedHeight(22)
        self.BevelB_Slider.valueChanged.connect(self.SliderB_Action)
        SliderB_HLyt.addWidget(self.BevelB_Slider)


        self.BevelB_SpinBox = QtWidgets.QDoubleSpinBox()
        self.BevelB_SpinBox.setDecimals(2)
        self.BevelB_SpinBox.setFixedWidth(40)
        self.BevelB_SpinBox.setFixedHeight(18)
        self.BevelB_SpinBox.setRange(0.01, 0.95)
        self.BevelB_SpinBox.setValue(0.5)
        self.BevelB_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.BevelB_SpinBox.editingFinished.connect(self.SpinBoxB_Action)
        SliderB_HLyt.addWidget(self.BevelB_SpinBox)







        BEVELS2_MLyt.addStretch()


    def Action(self):
        pass


    def SliderA_Action(self):
        BevelAValue = self.BevelA_Slider.value()/100
        self.BevelA_SpinBox.setValue(BevelAValue)
        mc.setAttr(str(BevelA) + ".fraction", BevelAValue)




    def SpinBoxA_Action(self):
        SpinBoxAValue = self.BevelA_SpinBox.value()*100
        self.BevelA_Slider.setValue(SpinBoxAValue)
        self.BevelA_SpinBox.clearFocus()






    def SliderB_Action(self):

        BevelBValue = self.BevelB_Slider.value()/100
        self.BevelB_SpinBox.setValue(BevelBValue)
        mc.setAttr(str(BevelB) + ".fraction", BevelBValue)


    def SpinBoxB_Action(self):
        SpinBoxBValue = self.BevelB_SpinBox.value()*100
        self.BevelB_Slider.setValue(SpinBoxBValue)
        self.BevelB_SpinBox.clearFocus()


def Dock(Widget, width=200, height=200, hp="free", show=True):
    label = getattr(Widget, "label", WindowsTitle)

    try:
        mc.deleteUI(WindowsTitle)
    except RuntimeError:
        pass

    dockControl = mc.workspaceControl(
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
        mc.evalDeferred(
            lambda *args: mc.workspaceControl(
                dockControl,
                edit=True,
                widthProperty="free",
                restore=True
            )
        )
    return child



def showUI():
    ui = Dock(Bevel2_UI)
    ui.show()


    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "ModIt_Window_Ico.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    return ui




