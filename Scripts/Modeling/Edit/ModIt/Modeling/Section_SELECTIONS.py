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
iconButtonSize = 30
separatorWidth = ModIt_Global.separatorWidth

##JSON PREF DATA
PRIM_MODE =(json.load(open(PreferencePath + 'Setting_Primitives_Placement.json',"r"))['PRIM_MODE'])
PRIM_SIZE =(json.load(open(PreferencePath + 'Setting_Primitives_Size.json',"r"))['PRIM_SIZE'])



class MyCustomBtn_Widget_forIcon(QtWidgets.QPushButton):
    def __init__(self, iconPath):
        super().__init__()
        #FOR ICON HOVER EFFECT
        pix_normal = QtGui.QPixmap(iconPath)
        pix_over = pix_normal.copy()
        painter = QtGui.QPainter(pix_over)
        painter.fillRect(pix_over.rect(), QtGui.QColor(250, 250, 250, 40))
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_Plus)
        painter.end()
        self._icon_normal = QIcon(pix_normal)
        self._icon_over = QIcon(pix_over)
        self.setIcon(self._icon_normal)
        #FOR CONTEXT MENU
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

    def enterEvent(self, event): #ICON
        self.setIcon(self._icon_over)
        return super(MyCustomBtn_Widget, self).enterEvent(event)
    def leaveEvent(self, event): #ICON
        self.setIcon(self._icon_normal)
        return super(MyCustomBtn_Widget, self).leaveEvent(event)

    def mousePressEvent(self, event): #CONTEXT MENUE
        super().mousePressEvent(event)
        if event.button() == QtCore.Qt.RightButton:
          # emit the signal, we can grab the pos directly from the event, no need to get cursor position anymore
          self.customContextMenuRequested.emit(event.pos())
          # make a call to mouseRelease event to restore button back to its original state
          self.mouseReleaseEvent(event)
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


class SELECTIONS_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_SELECTIONS_LAYOUT = QtWidgets.QHBoxLayout()  # MAIN
        SECTION_SELECTIONS_LAYOUT.setContentsMargins(0,0,0,0)
        SECTION_SELECTIONS_LAYOUT.setSpacing(0)
        self.setLayout(SECTION_SELECTIONS_LAYOUT)

        ##---------------------------------------------------- ALIGN PIVOT
        self.AlignPivotFace_btn = MyCustomBtn_Widget()
        self.AlignPivotFace_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.AlignPivotFace_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.AlignPivotFace_btn.setIcon(QtGui.QIcon(IconPath + "AlignFace.png"))
        self.AlignPivotFace_btn.setToolTip("  Align and Bake Object Pivot based on Face Normals  ")
        self.AlignPivotFace_btn.clicked.connect(self.alignPivotFace)



        ##---------------------------------------------------- CONTINUS EDGE
        self.ContinusEdge_btn = MyCustomBtn_Widget()
        self.ContinusEdge_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.ContinusEdge_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.ContinusEdge_btn.setIcon(QtGui.QIcon(IconPath + "ContinusEdge.png"))
        self.ContinusEdge_btn.setToolTip("  Select All Perimeter Contiguous Edge Until +45° angle  ")
        self.ContinusEdge_btn.clicked.connect(self.continusEdges)










        ##---------------------------------------------------- SELECT INNER
        self.SelIn_btn = QtWidgets.QPushButton()
        self.SelIn_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.SelIn_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.SelIn_btn.setIcon(QtGui.QIcon(IconPath + "SelIco1b.png"))
        self.SelIn_btn.setToolTip("  Select Inner Faces ")
        self.SelIn_btn.clicked.connect(self.selInner)


        ##---------------------------------------------------- SELECT INNER + SELECTION
        self.SelInAndSel_btn = QtWidgets.QPushButton()
        self.SelInAndSel_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.SelInAndSel_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.SelInAndSel_btn.setIcon(QtGui.QIcon(IconPath + "SelIco1.png"))
        self.SelInAndSel_btn.setToolTip("  Select Inner Faces and Keep Selection  ")
        self.SelInAndSel_btn.clicked.connect(self.selInnerPlus)


        ##---------------------------------------------------- NX Edge
        self.EdgeNx_btn = MyCustomBtn_Widget()
        self.EdgeNx_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.EdgeNx_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.EdgeNx_btn.setIcon(QtGui.QIcon(IconPath + "SelIco3.png"))
        self.EdgeNx_btn.setToolTip("  Select Every X Edges  ")
        self.EdgeNx_btn.clicked.connect(partial(self.selEdgeNX, "edgeLoop", 2))

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.EdgeNx_btn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.EdgeNx_btn.customContextMenuRequested.connect(self.showPopupNedge)
        #   CUBE M E N U   I T E M S
        self.popupMenuNedge = QtWidgets.QMenu()
        Loop_2 = self.popupMenuNedge.addAction("  > Loop : Select 1 Edge each 2 Edges")
        Loop_3 = self.popupMenuNedge.addAction("  > Loop : Select 1 Edge each 3 Edges")
        Loop_4 = self.popupMenuNedge.addAction("  > Loop : Select 1 Edge each 4 Edges")
        Loop_2.triggered.connect(partial(self.selEdgeNX, "edgeLoop", 2))
        Loop_3.triggered.connect(partial(self.selEdgeNX, "edgeLoop", 3))
        Loop_4.triggered.connect(partial(self.selEdgeNX, "edgeLoop", 4))
        Ring_2 = self.popupMenuNedge.addAction("  > Ring : Select 1 Edge each 2 Edges")
        Ring_3 = self.popupMenuNedge.addAction("  > Ring : Select 1 Edge each 3 Edges")
        Ring_4 = self.popupMenuNedge.addAction("  > Ring : Select 1 Edge each 4 Edges")
        Ring_2.triggered.connect(partial(self.selEdgeNX, "edgeRing", 2))
        Ring_3.triggered.connect(partial(self.selEdgeNX, "edgeRing", 3))
        Ring_4.triggered.connect(partial(self.selEdgeNX, "edgeRing", 4))












        ##---------------------------------------------------- CHECK FACES
        self.CheckFace_btn = MyCustomBtn_Widget()
        self.CheckFace_btn.setFixedSize(iconFixeSize, iconFixeSize)
        self.CheckFace_btn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.CheckFace_btn.setIcon(QtGui.QIcon(IconPath + "SelIco2.png"))
        self.CheckFace_btn.setToolTip("  Select Object Faces By Type  ")
        self.CheckFace_btn.clicked.connect(self.checkNGon)

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.CheckFace_btn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.CheckFace_btn.customContextMenuRequested.connect(self.showPopupCheck)
        #   CUBE M E N U   I T E M S
        self.popupMenuCube = QtWidgets.QMenu()
        Ngons = self.popupMenuCube.addAction(" Select all NGons faces on the selected mesh")
        Quad = self.popupMenuCube.addAction(" Select all Quadrangles faces on the selected mesh")
        Tri = self.popupMenuCube.addAction(" Select all Triangles faces on the selected mesh")
        Concave = self.popupMenuCube.addAction(" Select all Concaves faces on the selected mesh")
        Ngons.triggered.connect(self.checkNGon)
        Quad.triggered.connect(self.checkQuad)
        Tri.triggered.connect(self.checkTri)
        Concave.triggered.connect(self.checkNConcave)





























        ##---------------------------------------------------- Add to Layout
        SECTION_SELECTIONS_LAYOUT.addWidget(self.AlignPivotFace_btn)
        SECTION_SELECTIONS_LAYOUT.addWidget(self.ContinusEdge_btn)
        SECTION_SELECTIONS_LAYOUT.addWidget(self.SelIn_btn)
        SECTION_SELECTIONS_LAYOUT.addWidget(self.SelInAndSel_btn)
        SECTION_SELECTIONS_LAYOUT.addWidget(self.EdgeNx_btn)
        SECTION_SELECTIONS_LAYOUT.addWidget(self.CheckFace_btn)








    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------
    def BAM(self):
        print("BAMMM")


    def showPopupNedge(self, position):
        self.popupMenuNedge.exec_(self.EdgeNx_btn.mapToGlobal(position))
        self.EdgeNx_btn.update()

    def showPopupCheck(self, position):
        self.popupMenuCube.exec_(self.CheckFace_btn.mapToGlobal(position))
        self.CheckFace_btn.update()



    def Clean(self):
        mc.sets(n="selInnerPlusSet1")
        mc.sets(add="selInnerPlusSet1")
        mc.SelectFacetMask()
        mc.polyUVSet(d=True, uvSet="ModIt_UvLayout")
        mc.select(clear=True)
        mc.select("selInnerPlusSet1")
        mc.delete("selInnerPlusSet1")

    def CleanPluss(self):
        mc.sets(n="selInnerPlusSet1")
        mc.sets(add="selInnerPlusSet1")
        mc.SelectFacetMask()
        mc.polyUVSet(d=True, uvSet="ModIt_UvLayout")
        mc.select(clear=True)
        mc.select("selInnerPlusSet1")
        mc.delete("selInnerPlusSet1")
        mc.GrowPolygonSelectionRegion()

    def selInner(self):
        #Verif Selection is Face
        checkSelectedComponent = mc.filterExpand(sm=34)
        if checkSelectedComponent == None:
            ModIt_Global.WarningWindow(" You should select Faces.", 300)
            return

        mc.undoInfo(openChunk=True, infinity=True)
        selFace= mc.ls(sl=True)
        selObj = cmds.ls(sl=1, fl=1, o=1)
        mc.polyProjection (selObj, ch=1, type= "Planar", ibd = False, cm= True, uvSetName = "ModIt_UvLayout", kir = True, md= "c")
        mc.polyUVSet(cuv= True, uvSet = "ModIt_UvLayout")

        selEdgePeri = mc.ConvertSelectionToEdgePerimeter()
        mc.polyMapCut()

        mc.SelectMeshUVShell()

        mc.scriptJob( runOnce=True, e = ["SelectionChanged", self.Clean])
        mc.undoInfo(closeChunk=True)


    def selInnerPlus(self):
        #Verif Selection is Face
        checkSelectedComponent = mc.filterExpand(sm=34)
        if checkSelectedComponent == None:
            ModIt_Global.WarningWindow(" You should select Faces.", 300)
            return

        mc.undoInfo(openChunk=True, infinity=True)
        selFace=mc.ls(sl=True)
        selObj = cmds.ls(sl=1, fl=1, o=1)

        mc.polyProjection (selObj, ch=1, type= "Planar", ibd = False, cm= True, uvSetName = "ModIt_UvLayout", kir = True, md= "c")
        mc.polyUVSet(cuv= True, uvSet = "ModIt_UvLayout")

        selEdgePeri = mc.ConvertSelectionToEdgePerimeter()
        mc.polyMapCut()

        mc.SelectMeshUVShell()

        mc.scriptJob( runOnce=True, e = ["SelectionChanged", self.CleanPluss])
        mc.undoInfo(closeChunk=True)


    def selEdgeNX(self, type, nbr):
        mel.eval('polySelectEdgesEveryN "%s" %s;' % (type, nbr))

    def checkNGon(self):
        mc.selectMode(q=True, co=True)
        mc.polySelectConstraint(m=3 ,t = 0x0008, sz=3)
        mc.polySelectConstraint(dis=True)
    
    def checkTri(self):
        mc.selectMode(q=True, co=True)
        mc.polySelectConstraint(m=3 ,t = 0x0008, sz=1)
        mc.polySelectConstraint(dis=True)
    
    def checkQuad(self):
        mc.selectMode(q=True, co=True)
        mc.polySelectConstraint(m=3 ,t = 0x0008, sz=2)
        mc.polySelectConstraint(dis=True)
    
    
    def checkNConcave(self):
        mc.selectMode(q=True, co=True)
        mc.polySelectConstraint(m=3 ,t = 0x0008, c=1)
        mc.polySelectConstraint(dis=True)


    def alignPivotFace(self):
        #Verif Selection is Face
        checkSelectedComponent = mc.filterExpand(sm=34)
        if checkSelectedComponent == None:
            ModIt_Global.WarningWindow(" Works on Face mode only.", 300)
            return

        else:
            mc.undoInfo(openChunk=True, infinity=True)
            mc.setToolTo('Move')
            getPivotPos = mel.eval("float $getPivotPos[] = `manipMoveContext -q -p Move`;")
            mel.eval("ConvertSelectionToVertices;")
            vtxSel = mc.ls(fl=1, sl=1)
            selectedObjectStore = mc.ls(o=1, sl=1)
            objectSelectionStore = mc.listRelatives(selectedObjectStore[0], p=1)
            if len(vtxSel) < 3:
                mc.warning("ModIt : Please select at least 3 Vertices, 2 Edges or 1 Face")

            plane = mc.polyPlane(cuv=2, sy=1, sx=1, h=1, n='rotationPlane', ch=1, w=1, ax=(0, 1, 0))
            mc.select((plane[0] + ".vtx[0:2]"), vtxSel[0], vtxSel[1], vtxSel[2])
            mel.eval("snap3PointsTo3Points(0)")
            mc.parent(objectSelectionStore, plane[0])
            mc.makeIdentity(objectSelectionStore, apply=True, s=0, r=1, t=0, n=0)
            mc.xform(ws=1, piv=(getPivotPos[0], getPivotPos[1], getPivotPos[2]))
            mc.parent(objectSelectionStore, world=1)
            mc.delete(plane)
            mc.undoInfo(closeChunk=True)



    def continusEdges(self):
        #Verif Selection is Edge
        checkSelectedComponent = mc.filterExpand(sm=32)
        if checkSelectedComponent == None:
            ModIt_Global.WarningWindow(" You should select a border edge.", 300)
            return

        else:
            mc.undoInfo(openChunk=True, infinity=True)
            # 1 - Continus Edge
            mc.SelectContiguousEdges()

            # 2 - Store Continus Set
            mc.sets(n="ModIt_SelContinus_tempSet")

            # Need to get select objectq
            mc.SelectVertexMask()
            mc.SelectToggleMode()

            objSel = mc.ls(sl=True)

            # GET ALL FACE
            list = mc.ls(sl=True)
            for item in list:
                fCount = mc.polyEvaluate(v=True)
                mc.select(cl=True)
                mc.select(item + '.f[0:' + str(fCount) + ']', add=True)

            # CONVERT IN EDGE
            mc.ConvertSelectionToContainedEdges()
            mc.sets(n="ModIt_IntEdges_tempSet")

            mc.select(mc.sets('ModIt_IntEdges_tempSet', sub="ModIt_SelContinus_tempSet"))

            mc.sets(n="ModIt_GoodSel")
            mc.select(d=True)

            obSelName = str(objSel[0])
            mel.eval('doMenuComponentSelectionExt(" ' + obSelName + '", "edge", 0);')
            mc.select("ModIt_GoodSel")

            mc.delete("ModIt_IntEdges_tempSet")
            mc.delete("ModIt_SelContinus_tempSet")
            mc.delete("ModIt_GoodSel")
