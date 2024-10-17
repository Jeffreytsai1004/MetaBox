##--------------------------------------------------------------------------
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
import mtoa.core as core
from functools import partial

# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget

import importlib
from .. import ModIt_Global

importlib.reload(ModIt_Global)

from .. import ModIt_CSS



##______________________GLOBAL VAR
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath

# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 26
iconButtonSize = 26
separatorWidth = ModIt_Global.separatorWidth

##JSON PREF DATA
PRIM_MODE =(json.load(open(PreferencePath + 'Setting_Primitives_Placement.json',"r"))['PRIM_MODE'])
PRIM_SIZE =(json.load(open(PreferencePath + 'Setting_Primitives_Size.json',"r"))['PRIM_SIZE'])


class MyCustomBtn_Widget(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == QtCore.Qt.RightButton:
          # emit the signal, we can grab the pos directly from the event, no need to get cursor position anymore
          self.customContextMenuRequested.emit(event.pos())
          # make a call to mouseRelease event to restore button back to its original state
          self.mouseReleaseEvent(event)




class COLORS_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        SECTION_COLORS_LAYOUT = QtWidgets.QHBoxLayout()# MAIN
        SECTION_COLORS_LAYOUT.setContentsMargins(10,5,5,10)
        self.setLayout(SECTION_COLORS_LAYOUT)

        ##-------------------------------------------------------------------------------- COLOR : GREY
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Grey"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Grey.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(150, 150, 150)
        self.imgGrey = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgGrey)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgGrey.rect())


        self.ColorGreyBtn = MyCustomBtn_Widget()
        self.ColorGreyBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorGreyBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorGreyBtn.setIcon(QtGui.QIcon(self.imgGrey))
        self.ColorGreyBtn.clicked.connect(partial(self.ApplyColor, "Grey", 0.5, 0.5, 0.5))

        # C O N T E X T   M E N U
        self.ColorGreyBtn.customContextMenuRequested.connect(self.showPopup_Grey)
        self.popupMenuGrey = QtWidgets.QMenu()
        ColorGreyMenu_Entry_Select = self.popupMenuGrey.addAction("Select")
        ColorGreyMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Grey"))
        ColorGreyMenu_Entry_Attributes = self.popupMenuGrey.addAction("Attributes")
        ColorGreyMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Grey"))

        ##-------------------------------------------------------------------------------- COLOR#2 : YELLOW
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Yellow"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Yellow.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(229, 153, 0)
        self.imgYellow = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgYellow)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgYellow.rect())

        # BUTTON ICON COLOR
        self.ColorYellowBtn = MyCustomBtn_Widget()
        self.ColorYellowBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorYellowBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorYellowBtn.setIcon(QtGui.QIcon(self.imgYellow))
        self.ColorYellowBtn.clicked.connect(partial(self.ApplyColor, "Yellow", 0.9, 0.6, 0.0))


        # C O N T E X T   M E N U
        self.ColorYellowBtn.customContextMenuRequested.connect(self.showPopup_Yellow)
        self.popupMenuYellow = QtWidgets.QMenu()
        ColorYellowMenu_Entry_Select = self.popupMenuYellow.addAction("Select")
        ColorYellowMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Yellow"))
        ColorYellowMenu_Entry_Attributes = self.popupMenuYellow.addAction("Attributes")
        ColorYellowMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Yellow"))

        ##-------------------------------------------------------------------------------- COLOR : ORANGE
        #QT PAINTER
        if mc.objExists("ModItColor_" + "ORange"):
            colorRGB_0to1 = mc.getAttr("ModItColor_ORange.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(229, 89, 0)
        self.imgORange = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgORange)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgORange.rect())


        self.ColorORangeBtn = MyCustomBtn_Widget()
        self.ColorORangeBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorORangeBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorORangeBtn.setIcon(QtGui.QIcon(self.imgORange))
        self.ColorORangeBtn.clicked.connect(partial(self.ApplyColor, "ORange", 0.9, 0.35, 0.0))
        # C O N T E X T   M E N U
        self.ColorORangeBtn.customContextMenuRequested.connect(self.showPopup_ORange)
        self.popupMenuORange = QtWidgets.QMenu()
        ColorORangeMenu_Entry_Select = self.popupMenuORange.addAction("Select")
        ColorORangeMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "ORange"))
        ColorORangeMenu_Entry_Attributes = self.popupMenuORange.addAction("Attributes")
        ColorORangeMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "ORange"))

        ##-------------------------------------------------------------------------------- COLOR : RED
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Red"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Red.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(178, 3, 3)
        self.imgRed = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgRed)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgRed.rect())

        self.ColorRedBtn = MyCustomBtn_Widget()
        self.ColorRedBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorRedBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorRedBtn.setIcon(QtGui.QIcon(self.imgRed))
        self.ColorRedBtn.clicked.connect(partial(self.ApplyColor, "Red", 0.7, 0.011, 0.011))
        # C O N T E X T   M E N U
        self.ColorRedBtn.customContextMenuRequested.connect(self.showPopup_Red)
        self.popupMenuRed = QtWidgets.QMenu()
        ColorRedMenu_Entry_Select = self.popupMenuRed.addAction("Select")
        ColorRedMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Red"))
        ColorRedMenu_Entry_Attributes = self.popupMenuRed.addAction("Attributes")
        ColorRedMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Red"))

        ##-------------------------------------------------------------------------------- COLOR : GREEN
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Green"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Green.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(0, 203, 74)
        self.imgGreen = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgGreen)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgGreen.rect())

        self.ColorGreenBtn = MyCustomBtn_Widget()
        self.ColorGreenBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorGreenBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorGreenBtn.setIcon(QtGui.QIcon(self.imgGreen))
        self.ColorGreenBtn.clicked.connect(partial(self.ApplyColor, "Green", 0.0, 0.798, 0.292))
        # C O N T E X T   M E N U
        self.ColorGreenBtn.customContextMenuRequested.connect(self.showPopup_Green)
        self.popupMenuGreen = QtWidgets.QMenu()
        ColorGreenMenu_Entry_Select = self.popupMenuGreen.addAction("Select")
        ColorGreenMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Green"))
        ColorGreenMenu_Entry_Attributes = self.popupMenuGreen.addAction("Attributes")
        ColorGreenMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Green"))

        ##-------------------------------------------------------------------------------- COLOR : CYAN
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Cyan"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Cyan.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(0, 170, 227)
        self.imgCyan = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgCyan)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgCyan.rect())

        self.ColorCyanBtn = MyCustomBtn_Widget()
        self.ColorCyanBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorCyanBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorCyanBtn.setIcon(QtGui.QIcon(self.imgCyan))
        self.ColorCyanBtn.clicked.connect(partial(self.ApplyColor, "Cyan", 0.0, 0.6684, 0.894))
        # C O N T E X T   M E N U
        self.ColorCyanBtn.customContextMenuRequested.connect(self.showPopup_Cyan)
        self.popupMenuCyan = QtWidgets.QMenu()
        ColorCyanMenu_Entry_Select = self.popupMenuCyan.addAction("Select")
        ColorCyanMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Cyan"))
        ColorCyanMenu_Entry_Attributes = self.popupMenuCyan.addAction("Attributes")
        ColorCyanMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Cyan"))

        ##-------------------------------------------------------------------------------- COLOR : BLUE
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Blue"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Blue.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(0, 110, 178)
        self.imgBlue = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgBlue)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgBlue.rect())


        self.ColorBlueBtn = MyCustomBtn_Widget()
        self.ColorBlueBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorBlueBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorBlueBtn.setIcon(QtGui.QIcon(self.imgBlue))
        self.ColorBlueBtn.clicked.connect(partial(self.ApplyColor, "Blue", 0, 0.432, 0.7))
        # C O N T E X T   M E N U
        self.ColorBlueBtn.customContextMenuRequested.connect(self.showPopup_Blue)
        self.popupMenuBlue = QtWidgets.QMenu()
        ColorBlueMenu_Entry_Select = self.popupMenuBlue.addAction("Select")
        ColorBlueMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Blue"))
        ColorBlueMenu_Entry_Attributes = self.popupMenuBlue.addAction("Attributes")
        ColorBlueMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Blue"))

        ##-------------------------------------------------------------------------------- COLOR : BLACK
        #QT PAINTER
        if mc.objExists("ModItColor_" + "Black"):
            colorRGB_0to1 = mc.getAttr("ModItColor_Black.baseColor")[0]
            color = QtGui.QColor(colorRGB_0to1[0]*255, colorRGB_0to1[1]*255, colorRGB_0to1[2]*255)
        else:
            color = QtGui.QColor(15, 15, 15)
        self.imgBlack = QtGui.QPixmap(IconPath + "Color_Default_Icon.png")
        painter = QtGui.QPainter(self.imgBlack)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(self.imgBlack.rect())


        self.ColorBlackBtn = MyCustomBtn_Widget()
        self.ColorBlackBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorBlackBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorBlackBtn.setIcon(QtGui.QIcon(self.imgBlack))
        self.ColorBlackBtn.clicked.connect(partial(self.ApplyColor, "Black", 0.05, 0.05, 0.05))
        # C O N T E X T   M E N U
        self.ColorBlackBtn.customContextMenuRequested.connect(self.showPopup_Black)
        self.popupMenuBlack = QtWidgets.QMenu()
        ColorBlackMenu_Entry_Select = self.popupMenuBlack.addAction("Select")
        ColorBlackMenu_Entry_Select.triggered.connect(partial(self.SelectColor, "Black"))
        ColorBlackMenu_Entry_Attributes = self.popupMenuBlack.addAction("Attributes")
        ColorBlackMenu_Entry_Attributes.triggered.connect(partial(self.AttributColor, "Black"))



        ##---------------------------------------------------- Add to Layout
        SECTION_COLORS_LAYOUT.addWidget(self.ColorGreyBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorYellowBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorORangeBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorRedBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorGreenBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorCyanBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorBlueBtn)
        SECTION_COLORS_LAYOUT.addWidget(self.ColorBlackBtn)

    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N

    def ApplyColor(self, color, num1, num2, num3):
        mc.undoInfo(openChunk=True, infinity=True)
        selection = mc.ls(sl=True)
        if mc.objExists("ModItColor_" + color):
            mc.hyperShade(assign="ModItColor_" + color)
        else:
            ModItColor_StandarSurface = mc.shadingNode("standardSurface", asShader=True)
            mc.setAttr(ModItColor_StandarSurface + ".baseColor", num1, num2, num3, type='double3')
            mc.setAttr(ModItColor_StandarSurface + ".specularRoughness", 0.5)
            mc.setAttr(ModItColor_StandarSurface + ".specularRoughness", 0.5)
            mc.setAttr(ModItColor_StandarSurface + ".specular", 0.5)
            mc.rename("ModItColor_" + color)
            mc.select(selection)
            mc.hyperShade(assign="ModItColor_" + color)
        mc.undoInfo(closeChunk=True)

    def SelectColor(self, color):
        mc.undoInfo(openChunk=True, infinity=True)
        if mc.objExists("ModItColor_" + color):
            mc.hyperShade(objects="ModItColor_" + color)
        else:
            print("Please First Create this FaceColor Shader")
        mc.undoInfo(closeChunk=True)




    def AttributColor(self, color):
        if mc.objExists('ModItColor_' + color):
            mc.select('ModItColor_' + color)
        else:
            print("Please First Create this FaceColor Shader")



    def lambert1(self):
        mc.hyperShade(assign="lambert1")

    def SelectLambert(self):
        if mc.objExists('lambert1'):
            mc.hyperShade(objects="lambert1")
        else:
            print("Please First Create this FaceColor Shader")

    def TransLambert(self):
        if mc.objExists('lambert1'):
            mc.window(title='Lambert Transparancy')
            mc.columnLayout()
            mc.attrColorSliderGrp(at='lambert1.transparency')
            mc.showWindow()
        else:
            print("Please First Create this FaceColor Shader")

    def AttributLambert(self):
        if mc.objExists('lambert1'):
            mc.select('lambert1')
        else:
            print("Please First Create this FaceColor Shader")



    def showPopup_Grey(self, position):
        self.popupMenuGrey.exec_(self.ColorGreyBtn.mapToGlobal(position))
        self.ColorBlackBtn.update()

    def showPopup_Yellow(self, position):
        self.popupMenuYellow.exec_(self.ColorYellowBtn.mapToGlobal(position))
        self.ColorYellowBtn.update()

    def showPopup_ORange(self, position):
        self.popupMenuORange.exec_(self.ColorORangeBtn.mapToGlobal(position))
        self.ColorORangeBtn.update()

    def showPopup_Red(self, position):
        self.popupMenuRed.exec_(self.ColorRedBtn.mapToGlobal(position))
        self.ColorRedBtn.update()

    def showPopup_Green(self, position):
        self.popupMenuGreen.exec_(self.ColorGreenBtn.mapToGlobal(position))
        self.ColorGreenBtn.update()

    def showPopup_Cyan(self, position):
        self.popupMenuCyan.exec_(self.ColorCyanBtn.mapToGlobal(position))
        self.ColorCyanBtn.update()

    def showPopup_Black(self, position):
        self.popupMenuBlack.exec_(self.ColorBlackBtn.mapToGlobal(position))
        self.ColorBlackBtn.update()

    def showPopup_Blue(self, position):
        self.popupMenuBlue.exec_(self.ColorBlueBtn.mapToGlobal(position))
        self.ColorBlueBtn.update()

