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
WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])
DOCK =(json.load(open(PreferencePath + 'Dockable.json',"r"))['VALUE'])


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

class SETS_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        SECTION_SETS_LAYOUT = QtWidgets.QVBoxLayout()# MAIN
        SECTION_SETS_LAYOUT.setContentsMargins(25, 2, 2, 2)
        self.setLayout(SECTION_SETS_LAYOUT)

        setBtnClickZone = 16
        setBtnIconSize = 14
        SetBoutonWidht = 80

        ##---------------------------------------
        ##----------------------------------------------------------------------------------------------------------------------------------------------- STORE SETS
        ##--------------------------------------- SET - LIGNE 1
        SET_A_LYT = QtWidgets.QHBoxLayout()
        SET_A_LYT.setSpacing(7)
        SECTION_SETS_LAYOUT.addLayout(SET_A_LYT)
        SECTION_SETS_LAYOUT.setSpacing(0)

        ##----------------------------------------------------------------- -
        self.Set_1_Min_Btn = QtWidgets.QPushButton()
        self.Set_1_Min_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_1_Min_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set_1_Min_Btn.setIcon(QtGui.QIcon(IconPath + "Moins.png"))
        self.Set_1_Min_Btn.clicked.connect(partial(self.Sub_Set, 1))
        SET_A_LYT.addWidget(self.Set_1_Min_Btn)

        ##----------------------------------------------------------------------------------------------------------------------------------------- STORE SET 1
        self.Set_1_Store_Btn = QtWidgets.QPushButton()
        self.Set_1_Store_Btn.setFixedSize(SetBoutonWidht, 20)
        self.Set_1_Store_Btn.setObjectName("StoreSet")
        self.Set_1_Store_Btn.setText("S E T  -  2")
        if WIN_DISPLAY_SIZE == 1: #150
            self.Set_1_Store_Btn.setFont(QtGui.QFont('Calibri', 6))
        self.Set_1_Store_Btn.clicked.connect(partial(self.Store_Set, 1))
        SET_A_LYT.addWidget(self.Set_1_Store_Btn)

        ##----------------------------------------------------------------- +
        self.Set_1_Plus_Btn = QtWidgets.QPushButton()
        self.Set_1_Plus_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_1_Plus_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set_1_Plus_Btn.setIcon(QtGui.QIcon(IconPath + "Plus.png"))
        self.Set_1_Plus_Btn.clicked.connect(partial(self.Add_Set, 1))
        SET_A_LYT.addWidget(self.Set_1_Plus_Btn)

        SET_A_LYT.addSpacing(12)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,20)
        self.Separator.setStyleSheet("background-color:#404040;")
        SET_A_LYT.addWidget(self.Separator)
        SET_A_LYT.addSpacing(12)

        ##----------------------------------------------------------------- -
        self.Set_2_Min_Btn = QtWidgets.QPushButton()
        self.Set_2_Min_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_2_Min_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set_2_Min_Btn.setIcon(QtGui.QIcon(IconPath + "Moins.png"))
        self.Set_2_Min_Btn.clicked.connect(partial(self.Sub_Set, 2))
        SET_A_LYT.addWidget(self.Set_2_Min_Btn)

        ##----------------------------------------------------------------- STORE SET 2
        self.Set_2_Store_Btn = QtWidgets.QPushButton()
        self.Set_2_Store_Btn.setFixedSize(SetBoutonWidht, 20)
        self.Set_2_Store_Btn.setObjectName("StoreSet")
        self.Set_2_Store_Btn.setText("S E T  -  2")
        if WIN_DISPLAY_SIZE == 1: #150%
            self.Set_2_Store_Btn.setFont(QtGui.QFont('Calibri', 6))
        self.Set_2_Store_Btn.clicked.connect(partial(self.Store_Set, 2))
        SET_A_LYT.addWidget(self.Set_2_Store_Btn)

        ##----------------------------------------------------------------- +
        self.Set_2_Plus_Btn = QtWidgets.QPushButton()
        self.Set_2_Plus_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_2_Plus_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set_2_Plus_Btn.setIcon(QtGui.QIcon(IconPath + "Plus.png"))
        self.Set_2_Plus_Btn.clicked.connect(partial(self.Add_Set, 2))
        SET_A_LYT.addWidget(self.Set_2_Plus_Btn)




        ##______________________________________________________________/ UNDER LAYOUT
        SET_A_UNDER_LYT = QtWidgets.QHBoxLayout()
        SET_A_UNDER_LYT.setSpacing(10)
        SECTION_SETS_LAYOUT.addLayout(SET_A_UNDER_LYT)
        SET_A_UNDER_LYT.addSpacing(38)

        ##----------------------------------------------------------------- DEL
        self.Set_A_1_Del_btn = QtWidgets.QPushButton()
        self.Set_A_1_Del_btn.setFixedSize(20, 14)
        self.Set_A_1_Del_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_A_1_Del_btn.setIcon(QtGui.QIcon(IconPath + "setDel.png"))
        self.Set_A_1_Del_btn.clicked.connect(partial(self.Del_Set, 1))
        SET_A_UNDER_LYT.addWidget(self.Set_A_1_Del_btn)
        if mc.objExists("ModIt_Set_1"):
            self.Set_A_1_Del_btn.setEnabled(1)
        else:
            self.Set_A_1_Del_btn.setEnabled(0)



        ##----------------------------------------------------------------- GET
        self.Set_A_1_Get_btn = QtWidgets.QPushButton()
        self.Set_A_1_Get_btn.setFixedSize(20, 14)
        self.Set_A_1_Get_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_A_1_Get_btn.setIcon(QtGui.QIcon(IconPath + "setGet.png"))
        self.Set_A_1_Get_btn.clicked.connect(partial(self.Get_Set, 1))
        SET_A_UNDER_LYT.addWidget(self.Set_A_1_Get_btn)
        if mc.objExists("ModIt_Set_1"):
            self.Set_A_1_Get_btn.setEnabled(1)
        else:
            self.Set_A_1_Get_btn.setEnabled(0)


        SET_A_UNDER_LYT.addSpacing(106)

        ##----------------------------------------------------------------- DEL
        self.Set_A_2_Del_btn = QtWidgets.QPushButton()
        self.Set_A_2_Del_btn.setFixedSize(20, 14)
        self.Set_A_2_Del_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_A_2_Del_btn.setIcon(QtGui.QIcon(IconPath + "setDel.png"))
        self.Set_A_2_Del_btn.clicked.connect(partial(self.Del_Set, 2))
        SET_A_UNDER_LYT.addWidget(self.Set_A_2_Del_btn)
        if mc.objExists("ModIt_Set_2"):
            self.Set_A_2_Del_btn.setEnabled(1)
        else:
            self.Set_A_2_Del_btn.setEnabled(0)


        ##----------------------------------------------------------------- GET
        self.Set_A_2_Get_btn = QtWidgets.QPushButton()
        self.Set_A_2_Get_btn.setFixedSize(20, 14)
        self.Set_A_2_Get_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_A_2_Get_btn.setIcon(QtGui.QIcon(IconPath + "setGet.png"))
        self.Set_A_2_Get_btn.clicked.connect(partial(self.Get_Set, 2))
        SET_A_UNDER_LYT.addWidget(self.Set_A_2_Get_btn)
        if mc.objExists("ModIt_Set_2"):
            self.Set_A_2_Get_btn.setEnabled(1)
        else:
            self.Set_A_2_Get_btn.setEnabled(0)



        SECTION_SETS_LAYOUT.addSpacing(4)



        ##--------------------------------------- SET - LIGNE 2
        SET_B_LYT = QtWidgets.QHBoxLayout()
        SET_B_LYT.setSpacing(7)
        SECTION_SETS_LAYOUT.addLayout(SET_B_LYT)
        SECTION_SETS_LAYOUT.setSpacing(0)

        ##----------------------------------------------------------------- -
        self.Set_3_Min_Btn = QtWidgets.QPushButton()
        self.Set_3_Min_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_3_Min_Btn.setIconSize(QtCore.QSize(18, 18))
        self.Set_3_Min_Btn.setIcon(QtGui.QIcon(IconPath + "Moins.png"))
        self.Set_3_Min_Btn.clicked.connect(partial(self.Sub_Set, 3))
        SET_B_LYT.addWidget(self.Set_3_Min_Btn)

        ##----------------------------------------------------------------------------------------------------------------------------------------- STORE SET 1
        self.Set_3_Store_Btn = QtWidgets.QPushButton()
        self.Set_3_Store_Btn.setFixedSize(SetBoutonWidht, 20)
        self.Set_3_Store_Btn.setObjectName("StoreSet")
        self.Set_3_Store_Btn.setText("S E T  -  3")
        if WIN_DISPLAY_SIZE == 1: #150%
            self.Set_3_Store_Btn.setFont(QtGui.QFont('Calibri', 6))
        self.Set_3_Store_Btn.clicked.connect(partial(self.Store_Set, 3))
        SET_B_LYT.addWidget(self.Set_3_Store_Btn)

        ##----------------------------------------------------------------- +
        self.Set_3_Plus_Btn = QtWidgets.QPushButton()
        self.Set_3_Plus_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set_3_Plus_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set_3_Plus_Btn.setIcon(QtGui.QIcon(IconPath + "Plus.png"))
        self.Set_3_Plus_Btn.clicked.connect(partial(self.Add_Set, 3))
        SET_B_LYT.addWidget(self.Set_3_Plus_Btn)




        ##----------------------------------------------------------------- INTERSECT
        SET_B_LYT.addSpacing(2)
        self.Set_Int_Min_Btn = QtWidgets.QPushButton()
        self.Set_Int_Min_Btn.setFixedSize(20, 20)
        self.Set_Int_Min_Btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_Int_Min_Btn.setIcon(QtGui.QIcon(IconPath + "setIntersect.png"))
        self.Set_Int_Min_Btn.setToolTip(" Get Components that are both on Set-3 and Set-4  ")
        self.Set_Int_Min_Btn.clicked.connect(self.BoolIntersect_Set)
        SET_B_LYT.addWidget(self.Set_Int_Min_Btn)
        SET_B_LYT.addSpacing(3)




        ##----------------------------------------------------------------- -
        self.Set__Min_Btn = QtWidgets.QPushButton()
        self.Set__Min_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set__Min_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set__Min_Btn.setIcon(QtGui.QIcon(IconPath + "Moins.png"))
        self.Set__Min_Btn.clicked.connect(partial(self.Sub_Set, 4))
        SET_B_LYT.addWidget(self.Set__Min_Btn)

        ##----------------------------------------------------------------- STORE SET 2
        self.Set__Store_Btn = QtWidgets.QPushButton()
        self.Set__Store_Btn.setFixedSize(SetBoutonWidht, 20)
        self.Set__Store_Btn.setObjectName("StoreSet")
        self.Set__Store_Btn.setText("S E T  -  4")
        if WIN_DISPLAY_SIZE == 1:  # 150%
            self.Set__Store_Btn.setFont(QtGui.QFont('Calibri', 6))
        self.Set__Store_Btn.clicked.connect(partial(self.Store_Set, 4))
        SET_B_LYT.addWidget(self.Set__Store_Btn)

        ##----------------------------------------------------------------- +
        self.Set__Plus_Btn = QtWidgets.QPushButton()
        self.Set__Plus_Btn.setFixedSize(setBtnClickZone, setBtnClickZone)
        self.Set__Plus_Btn.setIconSize(QtCore.QSize(setBtnIconSize, setBtnIconSize))
        self.Set__Plus_Btn.setIcon(QtGui.QIcon(IconPath + "Plus.png"))
        self.Set__Plus_Btn.clicked.connect(partial(self.Add_Set, 4))
        SET_B_LYT.addWidget(self.Set__Plus_Btn)


        ##______________________________________________________________/ UNDER LAYOUT
        SET_B_UNDER_LYT = QtWidgets.QHBoxLayout()
        SET_B_UNDER_LYT.setSpacing(10)
        SECTION_SETS_LAYOUT.addLayout(SET_B_UNDER_LYT)
        SET_B_UNDER_LYT.addSpacing(38)

        ##----------------------------------------------------------------- DEL
        self.Set_B_1_Del_btn = QtWidgets.QPushButton()
        self.Set_B_1_Del_btn.setFixedSize(20, 14)
        self.Set_B_1_Del_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_B_1_Del_btn.setIcon(QtGui.QIcon(IconPath + "setDel.png"))
        self.Set_B_1_Del_btn.clicked.connect(partial(self.Del_Set, 3))
        SET_B_UNDER_LYT.addWidget(self.Set_B_1_Del_btn)
        if mc.objExists("ModIt_Set_3"):
            self.Set_B_1_Del_btn.setEnabled(1)
        else:
            self.Set_B_1_Del_btn.setEnabled(0)


        ##----------------------------------------------------------------- GET
        self.Set_B_1_Get_btn = QtWidgets.QPushButton()
        self.Set_B_1_Get_btn.setFixedSize(20, 14)
        self.Set_B_1_Get_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_B_1_Get_btn.setIcon(QtGui.QIcon(IconPath + "setGet.png"))
        self.Set_B_1_Get_btn.clicked.connect(partial(self.Get_Set, 3))
        SET_B_UNDER_LYT.addWidget(self.Set_B_1_Get_btn)
        if mc.objExists("ModIt_Set_3"):
            self.Set_B_1_Get_btn.setEnabled(1)
        else:
            self.Set_B_1_Get_btn.setEnabled(0)

        SET_B_UNDER_LYT.addSpacing(106)

        ##----------------------------------------------------------------- DEL
        self.Set_B_2_Del_btn = QtWidgets.QPushButton()
        self.Set_B_2_Del_btn.setFixedSize(20, 14)
        self.Set_B_2_Del_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_B_2_Del_btn.setIcon(QtGui.QIcon(IconPath + "setDel.png"))
        self.Set_B_2_Del_btn.clicked.connect(partial(self.Del_Set, 4))
        SET_B_UNDER_LYT.addWidget(self.Set_B_2_Del_btn)
        if mc.objExists("ModIt_Set_4"):
            self.Set_B_2_Del_btn.setEnabled(1)
        else:
            self.Set_B_2_Del_btn.setEnabled(0)


        ##----------------------------------------------------------------- GET
        self.Set_B_2_Get_btn = QtWidgets.QPushButton()
        self.Set_B_2_Get_btn.setFixedSize(20, 14)
        self.Set_B_2_Get_btn.setIconSize(QtCore.QSize(20, 20))
        self.Set_B_2_Get_btn.setIcon(QtGui.QIcon(IconPath + "setGet.png"))
        self.Set_B_2_Get_btn.clicked.connect(partial(self.Get_Set, 4))
        SET_B_UNDER_LYT.addWidget(self.Set_B_2_Get_btn)
        if mc.objExists("ModIt_Set_4"):
            self.Set_B_2_Get_btn.setEnabled(1)
        else:
            self.Set_B_2_Get_btn.setEnabled(0)




        self.ColorGreyBtn = MyCustomBtn_Widget()
        self.ColorGreyBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ColorGreyBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ColorGreyBtn.setIcon(QtGui.QIcon(IconPath + "ColorLambert.png"))
        self.ColorGreyBtn.clicked.connect(self.Action)
        # C O N T E X T   M E N U
        self.ColorGreyBtn.customContextMenuRequested.connect(self.showPopup_Lambert)
        self.popupMenuGrey = QtWidgets.QMenu()
        ColorGreyMenu_Entry_Select = self.popupMenuGrey.addAction("Select")
        ColorGreyMenu_Entry_Select.triggered.connect(self.Action)
        #ColorGreyMenu_Entry_Attributes.triggered.connect(self.AttributLambert)


        if DOCK == 0:
            SET_A_LYT.addStretch()
            SET_B_LYT.addStretch()
            SET_A_UNDER_LYT.addStretch()
            SET_B_UNDER_LYT.addStretch()
            SECTION_SETS_LAYOUT.addStretch()




    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N

    def Action(self):
        pass


    def Store_Set(self, number):
        if mc.objExists('ModIt_Set_' + str(number)):
            mc.sets(add='ModIt_Set_' + str(number))
        else:
            createNewSet = mc.sets(n= 'ModIt_Set_' + str(number))

        if number == 1:
            self.Set_A_1_Get_btn.setEnabled(1)
            self.Set_A_1_Del_btn.setEnabled(1)
        elif number == 2:
            self.Set_A_2_Get_btn.setEnabled(1)
            self.Set_A_2_Del_btn.setEnabled(1)
        elif number == 3:
            self.Set_B_1_Get_btn.setEnabled(1)
            self.Set_B_1_Del_btn.setEnabled(1)
        elif number == 4:
            self.Set_B_2_Get_btn.setEnabled(1)
            self.Set_B_2_Del_btn.setEnabled(1)


    def Add_Set(self, number):
        try:
            mc.sets(add='ModIt_Set_' + str(number))

        except:
            print("ModIt Error : Create a set first")

    def Sub_Set(self, number):
        try:
            mc.sets(rm='ModIt_Set_' + str(number))
        except:
            print("ModIt Error : Create a set first")


    def Del_Set(self, number):
        try:
            mc.delete('ModIt_Set_' + str(number))
        except:
            print("ModIt Error : Create a set first")

        if number == 1:
            self.Set_A_1_Get_btn.setEnabled(0)
            self.Set_A_1_Del_btn.setEnabled(0)
        elif number == 2:
            self.Set_A_2_Get_btn.setEnabled(0)
            self.Set_A_2_Del_btn.setEnabled(0)
        elif number == 3:
            self.Set_B_1_Get_btn.setEnabled(0)
            self.Set_B_1_Del_btn.setEnabled(0)
        elif number == 4:
            self.Set_B_2_Get_btn.setEnabled(0)
            self.Set_B_2_Del_btn.setEnabled(0)

    def Get_Set(self, number):
        try:
            mc.select('ModIt_Set_' + str(number))

            #obSelName = str(objSel[0])
            #mel.eval('doMenuComponentSelectionExt(" ' + obSelName + '", "edge", 0);')
        except:
            print("ModIt Error : Create a set first")


    def DelIntersect_Set(self):
        try:
            mc.delete('ModIt_Set_A')
            mc.delete('ModIt_Set_B')
        except:
            print("ModIt Error : Create a set first")

    def BoolIntersect_Set(self):
        if mc.objExists('ModIt_Set_3'):
            if mc.objExists('ModIt_Set_4'):
                mc.select(mc.sets( 'ModIt_Set_3', intersection = "ModIt_Set_4"))
            else:
                ModIt_Global.WarningWindow("ModIt Warning : You should store Set-3 and Set-4 first.", 350)
                return
        else:
            ModIt_Global.WarningWindow("ModIt Warning : You should store Set-3 and Set-4 first.", 350)
            return


    def showPopup_Lambert(self, position):
        self.popupMenuGrey.exec_(self.ColorGreyBtn.mapToGlobal(position))

































