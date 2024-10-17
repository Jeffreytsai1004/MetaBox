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
importlib.reload(ModIt_CSS)


##______________________GLOBAL VAR
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath

# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 32
iconButtonSize = 32
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

    #def enterEvent(self, event):
    #   print("ENTER EVENT")
    #def leaveEvent(self, event):
    #   print("LEAVE EVENT")


class UTILITIES_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_UTILITIES_LAYOUT = QtWidgets.QHBoxLayout()  # MAIN
        SECTION_UTILITIES_LAYOUT.setContentsMargins(10,0,0,10)
        SECTION_UTILITIES_LAYOUT.setSpacing(0)
        self.setLayout(SECTION_UTILITIES_LAYOUT)

        ##-------------------------------------------------------------------------------- HISTORY
        self.DelHistory_btn = MyCustomBtn_Widget()
        self.DelHistory_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.DelHistory_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.DelHistory_btn.setIcon(QtGui.QIcon(IconPath + "Util_Historique.png"))
        self.DelHistory_btn.setToolTip("  Delete History on Selection  ")
        self.DelHistory_btn.clicked.connect(mc.DeleteHistory)
        SECTION_UTILITIES_LAYOUT.addWidget(self.DelHistory_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.DelHistory_btn.customContextMenuRequested.connect(self.showPopup_DelHisto)
        #   CUBE M E N U   I T E M S
        self.popupMenu_DelHisto = QtWidgets.QMenu()
        DelHisto_Entry_1 = self.popupMenu_DelHisto.addAction("Delete All")
        DelHisto_Entry_1.triggered.connect(mc.DeleteAllHistory)


        ##-------------------------------------------------------------------------------- FREEZE
        self.FreezeTransform_btn = MyCustomBtn_Widget()
        self.FreezeTransform_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.FreezeTransform_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.FreezeTransform_btn.setIcon(QtGui.QIcon(IconPath + "Util_FreezeT.png"))
        self.FreezeTransform_btn.setToolTip("  Freeze Transformation on Selection  ")
        self.FreezeTransform_btn.clicked.connect(mc.FreezeTransformations)
        SECTION_UTILITIES_LAYOUT.addWidget(self.FreezeTransform_btn)


        ##-------------------------------------------------------------------------------- CENTER PIVOT
        self.CenterPivot_btn = MyCustomBtn_Widget()
        self.CenterPivot_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.CenterPivot_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.CenterPivot_btn.setIcon(QtGui.QIcon(IconPath + "Util_AlignPivot.png"))
        self.CenterPivot_btn.setToolTip("  Center Pivot  ")
        self.CenterPivot_btn.clicked.connect(mc.CenterPivot)
        SECTION_UTILITIES_LAYOUT.addWidget(self.CenterPivot_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.CenterPivot_btn.customContextMenuRequested.connect(self.showPopup_CenterPivot)
        #   CUBE M E N U   I T E M S
        self.popupMenu_CenterPivot = QtWidgets.QMenu()
        CenterPivot_Entry_1 = self.popupMenu_CenterPivot.addAction("Center Pivot at Base")
        CenterPivot_Entry_1.triggered.connect(self.PivotBottom)
        CenterPivot_Entry_2 = self.popupMenu_CenterPivot.addAction("Center Pivot at Base and Grid")
        CenterPivot_Entry_2.triggered.connect(self.PivotGrid)

        ##-------------------------------------------------------------------------------- OPTIMIZE
        self.Optimize_btn = QtWidgets.QPushButton()
        self.Optimize_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.Optimize_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Optimize_btn.setIcon(QtGui.QIcon(IconPath + "Util_Optimize.png"))
        self.Optimize_btn.setToolTip("  Optimize Scene ")
        self.Optimize_btn.clicked.connect(mc.OptimizeScene)
        SECTION_UTILITIES_LAYOUT.addWidget(self.Optimize_btn)

        ##-------------------------------------------------------------------------------- BTOA
        self.BtoA_btn = MyCustomBtn_Widget()
        self.BtoA_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.BtoA_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.BtoA_btn.setIcon(QtGui.QIcon(IconPath + "Util_BtoA.png"))
        self.BtoA_btn.setToolTip(" Match Position and Rotation  ")
        self.BtoA_btn.clicked.connect(self.MatchPosRot)
        SECTION_UTILITIES_LAYOUT.addWidget(self.BtoA_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.BtoA_btn.customContextMenuRequested.connect(self.showPopup_BtoA)
        #   CUBE M E N U   I T E M S
        self.popupMenu_BtoA = QtWidgets.QMenu()
        BtoA_Entry_1 = self.popupMenu_BtoA.addAction("Match All Transforms")
        BtoA_Entry_1.triggered.connect(mc.MatchTransform)
        BtoA_Entry_2 = self.popupMenu_BtoA.addAction("Match Pivots")
        BtoA_Entry_2.triggered.connect(mc.MatchPivots)



        SECTION_UTILITIES_LAYOUT.addSpacing(4)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,30)
        self.Separator.setStyleSheet("background-color:#434343;")
        SECTION_UTILITIES_LAYOUT.addWidget(self.Separator)
        SECTION_UTILITIES_LAYOUT.addSpacing(4)



        ##-------------------------------------------------------------------------------- SHOW
        self.DisplayShow_btn = QtWidgets.QPushButton()
        self.DisplayShow_btn.setFixedSize(30, 30)
        self.DisplayShow_btn.setIconSize(QtCore.QSize(30, 30))
        self.DisplayShow_btn.setIcon(QtGui.QIcon(IconPath + "Display_Show.png"))
        self.DisplayShow_btn.setToolTip("  Show All Hidden Object  ")
        self.DisplayShow_btn.clicked.connect(mc.ShowAll)
        SECTION_UTILITIES_LAYOUT.addWidget(self.DisplayShow_btn)


        ##-------------------------------------------------------------------------------- HIDE
        self.DisplayHide_btn = QtWidgets.QPushButton()
        self.DisplayHide_btn.setFixedSize(30, 30)
        self.DisplayHide_btn.setIconSize(QtCore.QSize(30, 30))
        self.DisplayHide_btn.setIcon(QtGui.QIcon(IconPath + "Display_Hide.png"))
        self.DisplayHide_btn.setToolTip("  Hide Unselected Objects  ")
        self.DisplayHide_btn.clicked.connect(mc.HideUnselectedObjects)
        SECTION_UTILITIES_LAYOUT.addWidget(self.DisplayHide_btn)










    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------ MENU
    def showPopup_CenterPivot(self, position):
        self.popupMenu_CenterPivot.exec_(self.CenterPivot_btn.mapToGlobal(position))
        self.CenterPivot_btn.update()

    def showPopup_DelHisto(self, position):
        self.popupMenu_DelHisto.exec_(self.DelHistory_btn.mapToGlobal(position))
        self.DelHistory_btn.update()

    def showPopup_BtoA(self, position):
        self.popupMenu_BtoA.exec_(self.BtoA_btn.mapToGlobal(position))
        self.BtoA_btn.update()



    #------------------------------------------------ ACTIONS

    def BAM(self):
        print("BAMMM")

    def PivotBottom(self):
        sel = mc.ls(sl=True)
        bbox = mc.exactWorldBoundingBox(sel)
        bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
        mc.xform(sel, piv=bottom, ws=True)

    def PivotGrid(self):
        sel = mc.ls(sl=True)
        bbox = mc.exactWorldBoundingBox(sel)
        bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
        mc.xform(sel, piv=bottom, ws=True)
        mc.move(0, 0, 0, sel, rpr=True)


    def MatchPosRot(self):
        mc.undoInfo(openChunk=True, infinity=True)
        mc.MatchTranslation()
        mc.MatchRotation()
        mc.undoInfo(closeChunk=True)






