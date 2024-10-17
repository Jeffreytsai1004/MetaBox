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
from maya import OpenMayaUI as omui
from PySide2.QtCore import Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance


import importlib
from .. import ModIt_Global

importlib.reload(ModIt_Global)

from .. import ModIt_CSS
importlib.reload(ModIt_CSS)

from ..Tools import ModIt_Bend_UI
from ..Tools import ModIt_DupLinear_UI
from ..Tools import ModIt_DupRadial_UI
from ..Tools import ModIt_DupCurve_UI

##______________________GLOBAL VAR
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath
RessourcePath = ModIt_Global.RessourcePath

# ******************************************
#           BUTTONS PARAMS
# ******************************************
iconFixeSize = 30
iconButtonSize = 30
separatorWidth = ModIt_Global.separatorWidth

##JSON PREF DATA



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


class TOOLS_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_TOOLS_LAYOUT = QtWidgets.QHBoxLayout()  # MAIN
        SECTION_TOOLS_LAYOUT.setContentsMargins(10,0,0,10)
        SECTION_TOOLS_LAYOUT.setSpacing(0)
        self.setLayout(SECTION_TOOLS_LAYOUT)

        ##---------------------------------------------------- DUP LINEAR
        self.DupLinear_btn = MyCustomBtn_Widget()
        self.DupLinear_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.DupLinear_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.DupLinear_btn.setIcon(QtGui.QIcon(IconPath + "Dup_Offset.png"))
        self.DupLinear_btn.setToolTip(" Duplicate Linear ")
        self.DupLinear_btn.clicked.connect(self.DupLinear)
        SECTION_TOOLS_LAYOUT.addWidget(self.DupLinear_btn)


        ##---------------------------------------------------- DUP RADIAL
        self.DupRadial_btn = MyCustomBtn_Widget()
        self.DupRadial_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.DupRadial_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.DupRadial_btn.setIcon(QtGui.QIcon(IconPath + "Dup_Radial.png"))
        self.DupRadial_btn.setToolTip("  Duplicate Radial  ")
        self.DupRadial_btn.clicked.connect(self.DupRadia)
        SECTION_TOOLS_LAYOUT.addWidget(self.DupRadial_btn)


        ##---------------------------------------------------- DUP CURVE
        self.DupCurv_btn = MyCustomBtn_Widget()
        self.DupCurv_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.DupCurv_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.DupCurv_btn.setIcon(QtGui.QIcon(IconPath + "Dup_Curve.png"))
        self.DupCurv_btn.setToolTip(" Duplicate on CURVE : Select Mesh first and Curve then  ")
        self.DupCurv_btn.clicked.connect(self.DupCurve)
        SECTION_TOOLS_LAYOUT.addWidget(self.DupCurv_btn)
        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.DupCurv_btn.customContextMenuRequested.connect(self.showPopupCurve)
        #   CUBE M E N U   I T E M S
        self.popupMenuCurve = QtWidgets.QMenu()
        Curve_Entry_1 = self.popupMenuCurve.addAction("Bezier Tool")
        Curve_Entry_1.triggered.connect(self.Bezier)
        Curve_Entry_2 = self.popupMenuCurve.addAction("EPCurve Tool")
        Curve_Entry_2.triggered.connect(self.EPCurve)
        Curve_Entry_3 = self.popupMenuCurve.addAction("Pencil Curve Tool")
        Curve_Entry_3.triggered.connect(self.Pencil)
        Curve_Entry_sep = self.popupMenuCurve.addAction(" ---------------- ")
        Curve_Entry_4 = self.popupMenuCurve.addAction(" Classic Chain Sample Mesh")
        Curve_Entry_4.triggered.connect(self.ChainA)
        Curve_Entry_5 = self.popupMenuCurve.addAction(" Classic Link Sample Mesh")
        Curve_Entry_5.triggered.connect(self.ChainB)
        Curve_Entry_6 = self.popupMenuCurve.addAction(" Transmission Chain Sample Mesh")
        Curve_Entry_6.triggered.connect(self.ChainC)




        ##--------------------------------------------------------------------------------------------------------

        SECTION_TOOLS_LAYOUT.addSpacing(4)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,30)
        self.Separator.setStyleSheet("background-color:#434343;")
        SECTION_TOOLS_LAYOUT.addWidget(self.Separator)
        SECTION_TOOLS_LAYOUT.addSpacing(4)
        ##--------------------------------------------------------------------------------------------------------



        ##---------------------------------------------------- BEND
        self.Bend_btn = QtWidgets.QPushButton()
        self.Bend_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.Bend_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Bend_btn.setIcon(QtGui.QIcon(IconPath + "Deform_Bend.png"))
        self.Bend_btn.setToolTip(" Bend Deformer ")
        self.Bend_btn.clicked.connect(self.BendTool)
        SECTION_TOOLS_LAYOUT.addWidget(self.Bend_btn)

        ##---------------------------------------------------- LATTICE
        self.Lattice_btn = MyCustomBtn_Widget()
        self.Lattice_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.Lattice_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.Lattice_btn.setIcon(QtGui.QIcon(IconPath + "Deform_Lattice.png"))
        self.Lattice_btn.setToolTip("  Lattice Deformer  ")
        self.Lattice_btn.clicked.connect(partial(self.LatticeTool, 2))
        SECTION_TOOLS_LAYOUT.addWidget(self.Lattice_btn)


        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.Lattice_btn.customContextMenuRequested.connect(self.showPopupLattice)
        #   CUBE M E N U   I T E M S
        self.popupMenuLattice = QtWidgets.QMenu()
        Angle_Entry_1 = self.popupMenuLattice.addAction("Lattice Div 3")
        Angle_Entry_1.triggered.connect(partial(self.LatticeTool, 3))
        Angle_Entry_2 = self.popupMenuLattice.addAction("Lattice Div 4")
        Angle_Entry_2.triggered.connect(partial(self.LatticeTool, 4))
        Angle_Entry_3 = self.popupMenuLattice.addAction("Lattice Div 5")
        Angle_Entry_3.triggered.connect(partial(self.LatticeTool, 5))
        Angle_Entry_4 = self.popupMenuLattice.addAction("Lattice Div 6")
        Angle_Entry_4.triggered.connect(partial(self.LatticeTool, 6))
        Angle_Entry_5 = self.popupMenuLattice.addAction(" ---------------- ")
        Angle_Entry_6 = self.popupMenuLattice.addAction("Reset Lattice (Selected)")
        Angle_Entry_6.triggered.connect(mc.RemoveLatticeTweaks)


        ##--------------------------------------------------------------------------------------------------------

        SECTION_TOOLS_LAYOUT.addSpacing(4)
        self.Separator = QtWidgets.QLabel()
        self.Separator.setFixedSize(1,30)
        self.Separator.setStyleSheet("background-color:#434343;")
        SECTION_TOOLS_LAYOUT.addWidget(self.Separator)
        SECTION_TOOLS_LAYOUT.addSpacing(4)
        ##--------------------------------------------------------------------------------------------------------



        ##---------------------------------------------------- FULLSCREEN ON
        self.FullScreenOn_btn = QtWidgets.QPushButton()
        self.FullScreenOn_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.FullScreenOn_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.FullScreenOn_btn.setIcon(QtGui.QIcon(IconPath + "FullScreen_On.png"))
        self.FullScreenOn_btn.setToolTip(" Maya Full Screen Enter ")
        self.FullScreenOn_btn.clicked.connect(self.FullScreenOn)
        SECTION_TOOLS_LAYOUT.addWidget(self.FullScreenOn_btn)

        ##---------------------------------------------------- FULLSCREEN OFF
        self.FullScreenOff_btn = QtWidgets.QPushButton()
        self.FullScreenOff_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.FullScreenOff_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.FullScreenOff_btn.setIcon(QtGui.QIcon(IconPath + "FullScreen_Off.png"))
        self.FullScreenOff_btn.setToolTip(" Maya Full Screen Exit ")
        self.FullScreenOff_btn.clicked.connect(self.FullScreenOff)
        SECTION_TOOLS_LAYOUT.addWidget(self.FullScreenOff_btn)





        #SECTION_TOOLS_LAYOUT.addSpacing(4)
        #self.Separator = QtWidgets.QLabel()
        #self.Separator.setFixedSize(1,30)
        #self.Separator.setStyleSheet("background-color:#434343;")
        #SECTION_TOOLS_LAYOUT.addWidget(self.Separator)
        #SECTION_TOOLS_LAYOUT.addSpacing(4)


        ##---------------------------------------------------- SELECT INNER + SELECTION
        #self.Welder_btn = QtWidgets.QPushButton()
        #self.Welder_btn.setFixedSize(iconFixeSize, iconFixeSize)
        #self.Welder_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        #self.Welder_btn.setIcon(QtGui.QIcon(IconPath + "Welder_Paint.png"))
        #self.Welder_btn.setToolTip("  Select Inner Faces and Keep Selection  ")
        #self.Welder_btn.clicked.connect(self.BAM)
        #SECTION_TOOLS_LAYOUT.addWidget(self.Welder_btn)








        ##---------------------------------------------------- Add to Layout












    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------
    def BAM(self):
        print("BAMMM")

    def showPopupLattice(self, position):
        self.popupMenuLattice.exec_(self.Lattice_btn.mapToGlobal(position))
        self.Lattice_btn.update()

    def showPopupCurve(self, position):
        self.popupMenuCurve.exec_(self.DupCurv_btn.mapToGlobal(position))
        self.DupCurv_btn.update()


    def BendTool(self):
        objectName = mc.ls(sl=True, l=True)

        mc.Bend()

        # 1 - GET ALL BEVEL NODE
        typ = "nonLinear"
        nodes = []
        for obj in objectName:
            for node in cmds.listHistory(obj):
                if cmds.nodeType(node) == typ:
                    nodes.append(node)
        Bend_node = nodes[0]

        mc.setAttr(str(Bend_node) + ".highBound", 2)
        mc.setAttr(str(Bend_node) + ".lowBound", -2)

        # ------------------------------------------------

        # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
        if mc.window("Bend", exists=True):
            mc.deleteUI("Bend")

        importlib.reload(ModIt_Bend_UI)
        ModIt_Bend_UI.SEND_INFO(str(Bend_node), str(objectName))
        ModIt_Bend_UI.showUI()

    def LatticeTool(self, number):
        objectName = mc.ls(sl=True, l=True)

        if objectName == []:
            print("Warning : Nothing Selected")
            return
        else:
            mc.CreateLattice()
            theLatice = mc.ls(sl=True)[0]
            mc.setAttr(str(theLatice) + "Shape.sDivisions", number)
            mc.setAttr(str(theLatice) + "Shape.tDivisions", number)
            mc.setAttr(str(theLatice) + "Shape.uDivisions", number)


    def DupLinear(self):
        LOCATOR_SIZE = (json.load(open(PreferencePath + 'Locator_Size.json', "r"))['VALUE'])

        import MASH.api as mapi
        MeshSel = mc.ls(sl=True, fl=True, dag=True, hd=1)
        mc.undoInfo(openChunk=True, infinity=True)
        sel = mc.ls(sl=True)
        if sel == []:
            ModIt_Global.WarningWindow("You should select Mesh or Group with Meshes.", 300)
            return

        try:  # MODE EDIT
            getName = sel[0].split("_")
            if getName[1] == "Linear":
                print("Edit Linear Mode")
                import re
                versionNum = re.findall(r'\d+', sel[0])[0]
                print(versionNum)

            # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
            if mc.window("Linear Duplication", exists=True):
                mc.deleteUI("Linear Duplication")

            importlib.reload(ModIt_DupLinear_UI)
            ModIt_DupLinear_UI.SEND_INFO(str(versionNum))
            ModIt_DupLinear_UI.showUI()





        except:  # MODE CREATE NEW
            ## 1 - VERIF
            #That it well mesh or Group
            sel = mc.ls(sl=True)
            descendants = set(mc.ls(mc.listRelatives(sel, ad=True) or [], type='shape'))
            mesh_descendants = set(mc.ls(descendants, type='mesh'))
            is_valid = (descendants == mesh_descendants)
            if is_valid == False :
                ModIt_Global.WarningWindow("You should select Mesh or Group with Meshes only.", 300)
                return

            #MASH is loaded
            try:
                mc.loadPlugin("MASH")
            except:
                pass

            try:
                mc.parent(MeshSel, world=True)
            except:
                pass

            mc.FreezeTransformations()
            mc.CenterPivot()
            posSaveLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_PosSave_Loc")
            mc.select(posSaveLocator, MeshSel)
            mc.MatchTranslation()
            mc.move(0, 0, 0, MeshSel, rpr=True)
            mc.makeIdentity(MeshSel, apply=True)



            #Origin Locator for NumName
            orignLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_Linear_OrignLoc1")
            mc.setAttr(orignLocator[0] + ".localScaleX", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + ".localScaleY", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + ".localScaleZ", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + "Shape.overrideEnabled", 1)
            mc.setAttr(orignLocator[0] + "Shape.overrideRGBColors", 1)
            mc.setAttr(orignLocator[0] + "Shape.overrideColorRGB", 1, 0.192, 0)

            #Get num
            import re
            num = re.findall(r'\d+', orignLocator[0])[0]



            # Create a Locator, place it to mesh location and grab is name in case of name conflict to be sure to rename the MASH sysmte like him.
            myLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_Linear_Loc" + str(num))
            mc.setAttr(myLocator[0] + ".localScaleX", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + ".localScaleY", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + ".localScaleZ", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + "Shape.overrideEnabled", 1)
            mc.setAttr(myLocator[0] + "Shape.overrideRGBColors", 1)
            mc.setAttr(myLocator[0] + "Shape.overrideColorRGB", 0.01, 0.461, 1.00)

            # GET Locator Number
            myLocatorName = mc.ls(sl=True)


            mc.select(myLocatorName, MeshSel)
            mc.MatchTranslation()
            mc.FreezeTransformations()
            mc.select(MeshSel)

            # Create a new MASH network
            mashNetwork = mapi.Network()
            MashDistribute = mashNetwork.createNetwork(name="ModIt_Duplicate" + str(num), geometry="Instancer")
            mc.setAttr("ModIt_Duplicate" + str(num) + "_Distribute.arrangement", 1)  # set Linear Mode
            MashInstancer = "ModIt_Duplicate" + str(num) + "_Instancer"
            createRandomNode = mashNetwork.addNode("MASH_Random")
            mc.setAttr("ModIt_Duplicate" + str(num) + "_Random.absoluteScale", 0)
            mc.setAttr("ModIt_Duplicate" + str(num) + "_Random.positionX", 0)
            mc.setAttr("ModIt_Duplicate" + str(num) + "_Random.positionY", 0)
            mc.setAttr("ModIt_Duplicate" + str(num) + "_Random.positionZ", 0)







            # Place at selObj Pos
            mc.parent(myLocatorName, MashInstancer)
            mc.select(MashInstancer, posSaveLocator)
            mc.MatchTranslation()
            mc.delete(posSaveLocator)

            # Origin Locator Set
            mc.select(orignLocator, MashInstancer)
            mc.MatchTranslation()
            mc.parent(MashInstancer, orignLocator)

            # Link Locator
            mc.setAttr(myLocatorName[0] + ".translateX", 20)
            mc.expression(s='ModIt_Duplicate' + str(num) + '_Distribute.amplitudeX = ' + myLocatorName[0] + ".translateX")
            mc.expression(s='ModIt_Duplicate' + str(num) + '_Distribute.amplitudeY = ' + myLocatorName[0] + ".translateY")
            mc.expression(s='ModIt_Duplicate' + str(num) + '_Distribute.amplitudeZ = ' + myLocatorName[0] + ".translateZ")

            # Rename OrignObj to found it later
            mc.rename(MeshSel, "ModIt_Linear_" + str(num) + "_Mesh")

            mc.select(myLocatorName)

            # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
            if mc.window("Linear Duplication", exists=True):
                mc.deleteUI("Linear Duplication")

            importlib.reload(ModIt_DupLinear_UI)
            ModIt_DupLinear_UI.SEND_INFO(str(num))
            ModIt_DupLinear_UI.showUI()

        mc.undoInfo(closeChunk=True)

    def DupRadia(self):
        LOCATOR_SIZE = (json.load(open(PreferencePath + 'Locator_Size.json', "r"))['VALUE'])


        import MASH.api as mapi
        MeshSel = mc.ls(sl=True, fl=True, dag=True, hd=1)
        mc.undoInfo(openChunk=True, infinity=True)
        sel = mc.ls(sl=True)
        if sel == []:
            ModIt_Global.WarningWindow("You should select Mesh or Group with Meshes.", 300)
            return

        try:  # MODE EDIT
            getName = sel[0].split("_")
            if getName[1] == "Radial":
                print("Edit Radial Mode")
                import re
                versionNum = re.findall(r'\d+', sel[0])[0]
                print(versionNum)

            # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
            if mc.window("Radial Duplication", exists=True):
                mc.deleteUI("Radial Duplication")

            importlib.reload(ModIt_DupRadial_UI)
            ModIt_DupRadial_UI.SEND_INFO(str(versionNum))
            ModIt_DupRadial_UI.showUI()





        except:  # MODE CREATE NEW
            ## 1 - VERIF
            #That it well mesh or Group
            sel = mc.ls(sl=True)
            descendants = set(mc.ls(mc.listRelatives(sel, ad=True) or [], type='shape'))
            mesh_descendants = set(mc.ls(descendants, type='mesh'))
            is_valid = (descendants == mesh_descendants)
            if is_valid == False :
                ModIt_Global.WarningWindow("You should select Mesh or Group with Meshes only.", 300)
                return

            #MASH is loaded
            try:
                mc.loadPlugin("MASH")
            except:
                pass



            try:
                mc.parent(MeshSel, world=True)
            except:
                pass

            mc.FreezeTransformations()
            mc.CenterPivot()
            posSaveLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_PosSave_Loc")
            mc.select(posSaveLocator, MeshSel)
            mc.MatchTranslation()
            mc.move(0, 0, 0, MeshSel, rpr=True)
            mc.makeIdentity(MeshSel, apply=True)



            #Origin Locator for NumName
            orignLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_Radial_OrignLoc1")
            mc.setAttr(orignLocator[0] + ".localScaleX", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + ".localScaleY", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + ".localScaleZ", LOCATOR_SIZE)
            mc.setAttr(orignLocator[0] + "Shape.overrideEnabled", 1)
            mc.setAttr(orignLocator[0] + "Shape.overrideRGBColors", 1)
            mc.setAttr(orignLocator[0] + "Shape.overrideColorRGB", 1, 0.192, 0)

            #Get num
            import re
            num = re.findall(r'\d+', orignLocator[0])[0]


            # Create a Locator, place it to mesh location and grab is name in case of name conflict to be sure to rename the MASH sysmte like him.
            myLocator = mc.spaceLocator(p=[0, 0, 0], n="ModIt_Radial_Loc" + str(num))
            mc.setAttr(myLocator[0] + ".localScaleX", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + ".localScaleY", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + ".localScaleZ", LOCATOR_SIZE)
            mc.setAttr(myLocator[0] + "Shape.overrideEnabled", 1)
            mc.setAttr(myLocator[0] + "Shape.overrideRGBColors", 1)
            mc.setAttr(myLocator[0] + "Shape.overrideColorRGB", 0.01, 0.461, 1.00)

            # GET Locator Number
            myLocatorName = mc.ls(sl=True)


            mc.select(myLocatorName, MeshSel)
            mc.MatchTranslation()
            mc.FreezeTransformations()
            mc.select(MeshSel)

            # Create a new MASH network
            mashNetwork = mapi.Network()
            MashDistribute = mashNetwork.createNetwork(name="ModIt_Duplicate_Radial" + str(num), geometry="Instancer")
            mc.setAttr("ModIt_Duplicate_Radial" + str(num) + "_Distribute.arrangement", 2) #set RadialMode
            MashInstancer = "ModIt_Duplicate_Radial" + str(num) + "_Instancer"
            createRandomNode = mashNetwork.addNode("MASH_Random")
            mc.setAttr("ModIt_Duplicate_Radial" + str(num) + "_Random.absoluteScale", 0)
            mc.setAttr("ModIt_Duplicate_Radial" + str(num) + "_Random.positionX", 0)
            mc.setAttr("ModIt_Duplicate_Radial" + str(num) + "_Random.positionY", 0)
            mc.setAttr("ModIt_Duplicate_Radial" + str(num) + "_Random.positionZ", 0)




            # Place at selObj Pos
            mc.parent(myLocatorName, MashInstancer)
            mc.select(MashInstancer, posSaveLocator)
            mc.MatchTranslation()
            mc.delete(posSaveLocator)

            # Origin Locator Set
            mc.select(orignLocator, MashInstancer)
            mc.MatchTranslation()
            mc.parent(MashInstancer, orignLocator)

            # Link Locator
            mc.setAttr(myLocatorName[0] + ".translateX", 10)
            mc.expression(s='ModIt_Duplicate_Radial' + str(num) + '_Distribute.radialRadius = ' + myLocatorName[0] + ".translateX")


            # Rename OrignObj to found it later
            mc.rename(MeshSel, "ModIt_Radial_" + str(num) + "_Mesh")

            mc.select(myLocatorName)

            # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
            if mc.window("Radial Duplication", exists=True):
                mc.deleteUI("Radial Duplication")

            importlib.reload(ModIt_DupRadial_UI)
            ModIt_DupRadial_UI.SEND_INFO(str(num))
            ModIt_DupRadial_UI.showUI()

        mc.undoInfo(closeChunk=True)

    def DupCurve(self):
        import MASH.api as mapi
        MeshSel = mc.ls(sl=True, fl=True, dag=True, hd=1)
        CurveSelection = mc.ls(sl=True, fl=True, dag=True, tl=1, shapes=True)

        mc.undoInfo(openChunk=True, infinity=True)

        sel = mc.ls(sl=True)
        if sel == []: #SI RIEN ERREUR
            ModIt_Global.WarningWindow("You should select 1-Mesh and 2-Curve.", 300)
            return

        if len(sel) == 1: #VERIF EDIT MODE
            print("EditModeVerif")

            descendants = set(mc.ls(mc.listRelatives(sel, ad=True) or [], type='shape'))
            bezier_descendants = set(mc.ls(descendants, type='bezierCurve'))
            is_valid_bezier = (descendants == bezier_descendants)

            nurbsh_descendants = set(mc.ls(descendants, type='nurbsCurve'))
            is_valid_nurbs = (descendants == nurbsh_descendants)

            if is_valid_bezier == False :
                if is_valid_nurbs == False :
                    ModIt_Global.WarningWindow("You should select the Curve to edit mode.", 300)
                    return
                else:
                    curveName = CurveSelection[0]

                    if mc.window("Curve Duplication", exists=True):
                        mc.deleteUI("Curve Duplication")

                    importlib.reload(ModIt_DupCurve_UI)
                    ModIt_DupCurve_UI.SEND_INFO(str(curveName))
                    ModIt_DupCurve_UI.showUI()

            else:
                curveName = CurveSelection[0]

                if mc.window("Curve Duplication", exists=True):
                    mc.deleteUI("Curve Duplication")

                importlib.reload(ModIt_DupCurve_UI)
                ModIt_DupCurve_UI.SEND_INFO(str(curveName))
                ModIt_DupCurve_UI.showUI()


        if len(sel) == 2: #VERIF CREATION MODE
            if mc.nodeType(CurveSelection) == "nurbsCurve":
                pass
            else:
                if mc.nodeType(CurveSelection) == "bezierCurve":
                    pass
                else:
                    ModIt_Global.WarningWindow("You should select Mesh First and Curve in Second.", 300)
                    return




            #MASH is loaded
            try:
                mc.loadPlugin("MASH")
            except:
                pass

            try:
                mc.parent(MeshSel, world=True)
            except:
                pass

            mc.FreezeTransformations()
            mc.CenterPivot()
            mc.move(0, 0, 0, MeshSel, rpr=True)
            mc.makeIdentity(MeshSel, apply=True)





            #Get num qui ici est le nom de la curve
            num = CurveSelection[0]


            mc.select(MeshSel)



            # Create a new MASH network
            mashNetwork = mapi.Network()
            MashDistribute = mashNetwork.createNetwork(name="ModIt_Duplicate_Curve" + str(num), geometry="Instancer")
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Distribute.arrangement", 8) #set CurveMode
            MashInstancer = "ModIt_Duplicate_Curve" + str(num) + "_Instancer"

            # create a world node
            curveNode = mashNetwork.addNode("MASH_Curve")
            mc.connectAttr(CurveSelection[0] + ".worldSpace[0]", "ModIt_Duplicate_Curve" + str(num) + "_Curve" + ".inCurves[0]")
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Curve" +  ".parametricLength", 1)

            # create a Random node
            createRandomNode = mashNetwork.addNode("MASH_Random")
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Random.absoluteScale", 0)
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Random.positionX", 0)
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Random.positionY", 0)
            mc.setAttr("ModIt_Duplicate_Curve" + str(num) + "_Random.positionZ", 0)




            mc.select(CurveSelection)

            # Pour eviter la boucle infinie avec le atClose qui clean la THumbScene
            if mc.window("Curve Duplication", exists=True):
                mc.deleteUI("Curve Duplication")

            importlib.reload(ModIt_DupCurve_UI)
            ModIt_DupCurve_UI.SEND_INFO(str(num))
            ModIt_DupCurve_UI.showUI()

        mc.undoInfo(closeChunk=True)


    def Bezier(self):
        mc.CreateBezierCurveTool()

    def EPCurve(self):
        mc.EPCurveTool()

    def Pencil(self):
        mc.PencilCurveTool()


    def ChainA(self):
        fileO = RessourcePath + "Mesh/Chain_A.ma"
        mc.file(fileO, i=True)

    def ChainB(self):
        fileO = RessourcePath + "Mesh/Chain_B.ma"
        mc.file(fileO, i=True)

    def ChainC(self):
        fileO = RessourcePath + "Mesh/Chain_C.ma"
        mc.file(fileO, i=True)



    def FullScreenOn(self):
        mainWindowPtr = omui.MQtUtil.mainWindow()
        mainWindow = wrapInstance(int(mainWindowPtr), QMainWindow)
        mainWindow.showFullScreen()

    def FullScreenOff(self):
        mainWindowPtr = omui.MQtUtil.mainWindow()
        mainWindow = wrapInstance(int(mainWindowPtr), QMainWindow)
        mainWindow.showNormal()

















































