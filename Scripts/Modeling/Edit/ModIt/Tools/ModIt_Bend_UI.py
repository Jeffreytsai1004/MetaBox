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

WindowsTitle = "Bend"

Bend = ""
ObjectPath = ""

##UI INFO
# ________________//
# ___________________________________________
# ________________//
def SEND_INFO(Bend_node, Obj):
    global Bend
    Bend = Bend_node
    global ObjectPath
    ObjectPath = Obj

    return Bend + ObjectPath


class Bevel2_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Bevel2_UI, self).__init__()
        self.setMinimumSize(420, 80)
        self.buildUI()



    def buildUI(self):
        ##UI - Preferences
        iconButtonSize = 10

        # ________________//
        # ___________________________________________## UI
        # ________________//
        BEND_MLyt = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(ModIt_Global.Theme)


        Title = QtWidgets.QLabel(" -  B e n d    T o o l  -  ")
        Title.setAlignment(QtCore.Qt.AlignCenter)
        BEND_MLyt.addWidget(Title)
        BEND_MLyt.addSpacing(10)



        # ___________________________________________## BEVEL A
        SliderA_HLyt = QtWidgets.QHBoxLayout(self)
        BEND_MLyt.addLayout(SliderA_HLyt)

        Bend_Title = QtWidgets.QLabel(" - Curvature ")
        SliderA_HLyt.addWidget(Bend_Title)

        self.Bend_Slider = QtWidgets.QSlider()
        self.Bend_Slider.setMinimum(-180)
        self.Bend_Slider.setMaximum(180)
        self.Bend_Slider.setProperty("value", 0)
        self.Bend_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Bend_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Bend_Slider.setTickInterval(1)
        self.Bend_Slider.setFixedHeight(22)
        self.Bend_Slider.valueChanged.connect(self.SliderA_Action)
        SliderA_HLyt.addWidget(self.Bend_Slider)


        self.Bend_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Bend_SpinBox.setDecimals(1)
        self.Bend_SpinBox.setFixedWidth(40)
        self.Bend_SpinBox.setFixedHeight(18)
        self.Bend_SpinBox.setRange(-180, 180)
        self.Bend_SpinBox.setValue(0)
        self.Bend_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Bend_SpinBox.editingFinished.connect(self.SpinBoxA_Action)
        SliderA_HLyt.addWidget(self.Bend_SpinBox)



        #---------------------------------
        BEND_MLyt.addSpacing(6)
        self.BakeButton = QtWidgets.QPushButton()
        self.BakeButton.setText(" B A K E ")
        self.BakeButton.setFixedHeight(22)
        self.BakeButton.setObjectName("StoreSet")
        #self.BakeButton.clicked.connect(self.Bake)
        #BEND_MLyt.addWidget(self.BakeButton)




        BEND_MLyt.addStretch()










    def SliderA_Action(self):
        BendValue = self.Bend_Slider.value()
        self.Bend_SpinBox.setValue(BendValue)
        mc.setAttr(str(Bend) + ".curvature", BendValue)


    def SpinBoxA_Action(self):
        SpinBoxAValue = self.Bend_SpinBox.value()
        self.Bend_Slider.setValue(SpinBoxAValue)
        self.Bend_SpinBox.clearFocus()

    #def Bake(self):
        #objectName = mc.ls(sl=True, l=True)
        #allNode = mc.listHistory(Bend)
        #getShape = mc.ls(allNode, type="shape")[0]
       # mc.delete(ch = 1)




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




