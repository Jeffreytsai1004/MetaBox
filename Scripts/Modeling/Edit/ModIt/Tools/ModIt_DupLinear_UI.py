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

WindowsTitle = "Linear Duplication"

Num = ""


##UI INFO
# ________________//
# ___________________________________________
# ________________//
def SEND_INFO(NumVersion):
    global Num
    Num = NumVersion

    return Num


class Linear_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Linear_UI, self).__init__()
        self.setMinimumSize(460, 230)
        self.buildUI()



    def buildUI(self):
        ##UI - Preferences
        iconFixeSize = 22
        iconButtonSize = 20

        # ________________//
        # ___________________________________________## UI
        # ________________//
        LINEAR_MLyt = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet(ModIt_Global.Theme)


        Title = QtWidgets.QLabel(" -  L i n e a r   D u p l i c a t i o n  -  ")
        Title.setAlignment(QtCore.Qt.AlignCenter)
        LINEAR_MLyt.addWidget(Title)
        LINEAR_MLyt.addSpacing(10)

        Linear_HLyt = QtWidgets.QHBoxLayout()
        LINEAR_MLyt.addLayout(Linear_HLyt)


        # ___________________________________________## LOCATOR ORIGN
        self.LocatorOrign_btn = QtWidgets.QPushButton()
        self.LocatorOrign_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.LocatorOrign_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.LocatorOrign_btn.setIcon(QtGui.QIcon(IconPath + "Locator_orign.png"))
        self.LocatorOrign_btn.setToolTip("  Get Origin Locator  ")
        self.LocatorOrign_btn.clicked.connect(self.get_locatorOrign)
        Linear_HLyt.addWidget(self.LocatorOrign_btn)

        # ___________________________________________## NUMBER OF INSTANCES
        # ___________________________________________##
        SliderNumber_HLyt = QtWidgets.QHBoxLayout(self)
        Linear_HLyt.addLayout(SliderNumber_HLyt)


        Number_label = QtWidgets.QLabel(" Number ")
        SliderNumber_HLyt.addWidget(Number_label)

        self.Number_Slider = QtWidgets.QSlider()
        self.Number_Slider.setMinimum(1)
        self.Number_Slider.setMaximum(100)
        try:
            getValue = mc.getAttr("ModIt_Duplicate" + str(Num) + "_Distribute.pointCount")
        except:
            getValue = 10
        self.Number_Slider.setProperty("value", getValue)
        self.Number_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Number_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Number_Slider.setTickInterval(1)
        self.Number_Slider.setFixedHeight(22)
        self.Number_Slider.valueChanged.connect(self.SliderNumber_Action)
        SliderNumber_HLyt.addWidget(self.Number_Slider)


        self.Number_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Number_SpinBox.setDecimals(1)
        self.Number_SpinBox.setFixedWidth(40)
        self.Number_SpinBox.setFixedHeight(18)
        self.Number_SpinBox.setRange(0, 1000)
        self.Number_SpinBox.setValue(getValue)
        self.Number_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Number_SpinBox.editingFinished.connect(self.SpinBoxA_Action)
        SliderNumber_HLyt.addWidget(self.Number_SpinBox)

        # ___________________________________________## LOCATOR CIBLE
        self.LocatorTarget_btn = QtWidgets.QPushButton()
        self.LocatorTarget_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.LocatorTarget_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.LocatorTarget_btn.setIcon(QtGui.QIcon(IconPath + "Locator_cible.png"))
        self.LocatorTarget_btn.setToolTip("  Get Target Locator  ")
        self.LocatorTarget_btn.clicked.connect(self.get_locatorTarget)
        Linear_HLyt.addWidget(self.LocatorTarget_btn)






        LINEAR_MLyt.addSpacing(4)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(5000,1)
        self.Separator.setStyleSheet("background-color:#434343;")
        LINEAR_MLyt.addWidget(self.Separator)
        LINEAR_MLyt.addSpacing(4)
















        TitleR = QtWidgets.QLabel(" -  R a n d o m  -  ")
        TitleR.setAlignment(QtCore.Qt.AlignCenter)
        LINEAR_MLyt.addWidget(TitleR)
        LINEAR_MLyt.addSpacing(10)
        # ___________________________________________## RANDOM POSITION
        # ___________________________________________##
        SliderRandomP_HLyt = QtWidgets.QHBoxLayout(self)
        LINEAR_MLyt.addLayout(SliderRandomP_HLyt)

        Random_label = QtWidgets.QLabel("Position XYZ ")
        SliderRandomP_HLyt.addWidget(Random_label)

        try:
            getValueP = mc.getAttr("ModIt_Duplicate" + str(Num) + "_Random.positionX")
        except:
            getValueP = 0
        self.RandomP_Slider = QtWidgets.QSlider()
        self.RandomP_Slider.setMinimum(0)
        self.RandomP_Slider.setMaximum(100)
        self.RandomP_Slider.setProperty("value", getValueP)
        self.RandomP_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.RandomP_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.RandomP_Slider.setTickInterval(1)
        self.RandomP_Slider.setFixedHeight(22)
        self.RandomP_Slider.valueChanged.connect(self.SliderPosRandom_Action)
        SliderRandomP_HLyt.addWidget(self.RandomP_Slider)


        self.RandomP_SpinBox = QtWidgets.QDoubleSpinBox()
        self.RandomP_SpinBox.setDecimals(1)
        self.RandomP_SpinBox.setFixedWidth(40)
        self.RandomP_SpinBox.setFixedHeight(18)
        self.RandomP_SpinBox.setRange(0, 1000)
        self.RandomP_SpinBox.setValue(getValueP)
        self.RandomP_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RandomP_SpinBox.editingFinished.connect(self.SpinPosRandom_Action)
        SliderRandomP_HLyt.addWidget(self.RandomP_SpinBox)



        # ___________________________________________##      RANDOM ROTATION     X
        # ___________________________________________##
        SliderRandomRx_HLyt = QtWidgets.QHBoxLayout(self)
        LINEAR_MLyt.addLayout(SliderRandomRx_HLyt)

        Random_label = QtWidgets.QLabel("Rotation   X ")
        SliderRandomRx_HLyt.addWidget(Random_label)

        try:
            getValueR = mc.getAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationX")
        except:
            getValueR = 0
            
        self.RandomRx_Slider = QtWidgets.QSlider()
        self.RandomRx_Slider.setMinimum(0)
        self.RandomRx_Slider.setMaximum(360)
        self.RandomRx_Slider.setProperty("value", getValueR)
        self.RandomRx_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.RandomRx_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.RandomRx_Slider.setTickInterval(1)
        self.RandomRx_Slider.setFixedHeight(22)
        self.RandomRx_Slider.valueChanged.connect(self.SliderRotRandomX_Action)
        SliderRandomRx_HLyt.addWidget(self.RandomRx_Slider)

        self.RandomRx_SpinBox = QtWidgets.QDoubleSpinBox()
        self.RandomRx_SpinBox.setDecimals(1)
        self.RandomRx_SpinBox.setFixedWidth(40)
        self.RandomRx_SpinBox.setFixedHeight(18)
        self.RandomRx_SpinBox.setRange(0, 1000)
        self.RandomRx_SpinBox.setValue(getValueR)
        self.RandomRx_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RandomRx_SpinBox.editingFinished.connect(self.SpinRotRandomX_Action)
        SliderRandomRx_HLyt.addWidget(self.RandomRx_SpinBox)





        # ___________________________________________##      RANDOM ROTATION     Y
        # ___________________________________________##
        SliderRandomRy_HLyt = QtWidgets.QHBoxLayout(self)
        LINEAR_MLyt.addLayout(SliderRandomRy_HLyt)

        Random_label = QtWidgets.QLabel("Rotation   Y ")
        SliderRandomRy_HLyt.addWidget(Random_label)

        try:
            getValueR = mc.getAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationY")
        except:
            getValueR = 0

        self.RandomRy_Slider = QtWidgets.QSlider()
        self.RandomRy_Slider.setMinimum(0)
        self.RandomRy_Slider.setMaximum(360)
        self.RandomRy_Slider.setProperty("value", getValueR)
        self.RandomRy_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.RandomRy_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.RandomRy_Slider.setTickInterval(1)
        self.RandomRy_Slider.setFixedHeight(22)
        self.RandomRy_Slider.valueChanged.connect(self.SliderRotRandomY_Action)
        SliderRandomRy_HLyt.addWidget(self.RandomRy_Slider)

        self.RandomRy_SpinBox = QtWidgets.QDoubleSpinBox()
        self.RandomRy_SpinBox.setDecimals(1)
        self.RandomRy_SpinBox.setFixedWidth(40)
        self.RandomRy_SpinBox.setFixedHeight(18)
        self.RandomRy_SpinBox.setRange(0, 1000)
        self.RandomRy_SpinBox.setValue(getValueR)
        self.RandomRy_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RandomRy_SpinBox.editingFinished.connect(self.SpinRotRandomY_Action)
        SliderRandomRy_HLyt.addWidget(self.RandomRy_SpinBox)



        # ___________________________________________##      RANDOM ROTATION     Z
        # ___________________________________________##
        SliderRandomRz_HLyt = QtWidgets.QHBoxLayout(self)
        LINEAR_MLyt.addLayout(SliderRandomRz_HLyt)

        Random_label = QtWidgets.QLabel("Rotation   Z ")
        SliderRandomRz_HLyt.addWidget(Random_label)

        try:
            getValueR = mc.getAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationZ")
        except:
            getValueR = 0

        self.RandomRz_Slider = QtWidgets.QSlider()
        self.RandomRz_Slider.setMinimum(0)
        self.RandomRz_Slider.setMaximum(360)
        self.RandomRz_Slider.setProperty("value", getValueR)
        self.RandomRz_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.RandomRz_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.RandomRz_Slider.setTickInterval(1)
        self.RandomRz_Slider.setFixedHeight(22)
        self.RandomRz_Slider.valueChanged.connect(self.SliderRotRandomZ_Action)
        SliderRandomRz_HLyt.addWidget(self.RandomRz_Slider)

        self.RandomRz_SpinBox = QtWidgets.QDoubleSpinBox()
        self.RandomRz_SpinBox.setDecimals(1)
        self.RandomRz_SpinBox.setFixedWidth(40)
        self.RandomRz_SpinBox.setFixedHeight(18)
        self.RandomRz_SpinBox.setRange(0, 1000)
        self.RandomRz_SpinBox.setValue(getValueR)
        self.RandomRz_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RandomRz_SpinBox.editingFinished.connect(self.SpinRotRandomZ_Action)
        SliderRandomRz_HLyt.addWidget(self.RandomRz_SpinBox)













        #---------------------------------
        LINEAR_MLyt.addSpacing(6)
        self.BakeButton = QtWidgets.QPushButton()
        self.BakeButton.setText(" B A K E ")
        self.BakeButton.setFixedHeight(22)
        self.BakeButton.setObjectName("StoreSet")
        self.BakeButton.clicked.connect(self.Bake)
        LINEAR_MLyt.addWidget(self.BakeButton)




















        LINEAR_MLyt.addStretch()










    def SliderNumber_Action(self):
        NumberValue = self.Number_Slider.value()
        self.Number_SpinBox.setValue(NumberValue)
        self.SpinBoxA_Action()

    def SpinBoxA_Action(self):
        SpinBoxAValue = self.Number_SpinBox.value()
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Distribute.pointCount", SpinBoxAValue)
        self.Number_Slider.setValue(SpinBoxAValue)
        self.Number_SpinBox.clearFocus()





    def SliderPosRandom_Action(self):
        NumberValue = self.RandomP_Slider.value()
        self.RandomP_SpinBox.setValue(NumberValue)
        self.SpinPosRandom_Action()

    def SpinPosRandom_Action(self):
        SpinBoxValue = self.RandomP_SpinBox.value()
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.positionX", SpinBoxValue)
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.positionY", SpinBoxValue)
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.positionZ", SpinBoxValue)
        self.RandomP_Slider.setValue(SpinBoxValue)
        self.RandomP_SpinBox.clearFocus()


    def SliderRotRandomX_Action(self):
        NumberValue = self.RandomRx_Slider.value()
        self.RandomRx_SpinBox.setValue(NumberValue)
        self.SpinRotRandomX_Action()

    def SpinRotRandomX_Action(self):
        SpinBoxValue = self.RandomRx_SpinBox.value()
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationX", SpinBoxValue)
        self.RandomRx_Slider.setValue(SpinBoxValue)
        self.RandomRx_SpinBox.clearFocus()

    def SliderRotRandomY_Action(self):
        NumberValue = self.RandomRy_Slider.value()
        self.RandomRy_SpinBox.setValue(NumberValue)
        self.SpinRotRandomY_Action()

    def SpinRotRandomY_Action(self):
        SpinBoxValue = self.RandomRy_SpinBox.value()
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationY", SpinBoxValue)
        self.RandomRy_Slider.setValue(SpinBoxValue)
        self.RandomRy_SpinBox.clearFocus()

    def SliderRotRandomZ_Action(self):
        NumberValue = self.RandomRz_Slider.value()
        self.RandomRz_SpinBox.setValue(NumberValue)
        self.SpinRotRandomZ_Action()

    def SpinRotRandomZ_Action(self):
        SpinBoxValue = self.RandomRz_SpinBox.value()
        mc.setAttr("ModIt_Duplicate" + str(Num) + "_Random.rotationZ", SpinBoxValue)
        self.RandomRz_Slider.setValue(SpinBoxValue)
        self.RandomRz_SpinBox.clearFocus()






    def get_locatorOrign(self):
        mc.select("ModIt_Linear_OrignLoc" + str(Num))

    def get_locatorTarget(self):
        mc.select("ModIt_Linear_Loc" + str(Num))



    def Bake(self):
        MashInstancer = "ModIt_Duplicate" + Num + "_Instancer"

        mc.select(MashInstancer)
        import maya.mel as mel
        mel.eval('MASHBakeGUI;')
        mc.select(MashInstancer)
        import MASHbakeInstancer;
        MASHbakeInstancer.MASHbakeInstancer(False)
        mc.deleteUI("mashBakeStill", window=True)

        mc.select("ModIt_Duplicate" + Num + "_Instancer")
        mc.CenterPivot()
        mc.delete(ch=True)
        mc.rename("ModIt_Linear_1")


        mc.delete("ModIt_Linear_OrignLoc" + Num)


        if mc.window("Linear Duplication", exists=True):
            mc.deleteUI("Linear Duplication")




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
    ui = Dock(Linear_UI)
    ui.show()


    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowsTitle)
    widget = wrapInstance(int(qw), QWidget)
    # Create a QIcon object
    icon = QIcon(IconPath + "ModIt_Window_Ico.png")
    # Assign the icon
    widget.setWindowIcon(icon)

    return ui




