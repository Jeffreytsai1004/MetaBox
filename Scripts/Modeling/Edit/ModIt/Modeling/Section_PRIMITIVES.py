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
iconFixeSize = ModIt_Global.iconFixeSize
iconButtonSize = ModIt_Global.iconButtonSize
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




class PRIMITIVES_LAYOUT(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        SECTION_PRIMITIVES_LAYOUT = QtWidgets.QHBoxLayout()  # MAIN
        SECTION_PRIMITIVES_LAYOUT.setContentsMargins(0,0,0,0)
        self.setLayout(SECTION_PRIMITIVES_LAYOUT)

        ##---------------------------------------------------- PRIMITIVES - CUBE
        #self.CubeBtn = QtWidgets.QPushButton()
        self.CubeBtn = MyCustomBtn_Widget()
        self.CubeBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.CubeBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.CubeBtn.setIcon(QtGui.QIcon(IconPath + "Prim_CUBE.png"))
        self.CubeBtn.clicked.connect(partial(self.Create_Cube, 1))

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        #self.CubeBtn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.CubeBtn.customContextMenuRequested.connect(self.showPopupCube)
        #   CUBE M E N U   I T E M S
        self.popupMenuCube = QtWidgets.QMenu()
        CubeMenu_Entry_1 = self.popupMenuCube.addAction("Cube sbdv 1")
        CubeMenu_Entry_2 = self.popupMenuCube.addAction("Cube sbdv 2")
        CubeMenu_Entry_3 = self.popupMenuCube.addAction("Cube sbdv 3")
        CubeMenu_Entry_4 = self.popupMenuCube.addAction("Cube sbdv 4")
        CubeMenu_Entry_1.triggered.connect(partial(self.Create_Cube, 1))
        CubeMenu_Entry_2.triggered.connect(partial(self.Create_Cube, 2))
        CubeMenu_Entry_3.triggered.connect(partial(self.Create_Cube, 3))
        CubeMenu_Entry_4.triggered.connect(partial(self.Create_Cube, 4))


        ##---------------------------------------------------- PRIMITIVES - SPHERE
        self.SphereBtn = MyCustomBtn_Widget()
        self.SphereBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.SphereBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.SphereBtn.setIcon(QtGui.QIcon(IconPath + "Prim_SPHERE.png"))
        self.SphereBtn.clicked.connect(partial(self.Create_Sphere, 16, 10))

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.SphereBtn.customContextMenuRequested.connect(self.showPopupSphere)
        #   CUBE M E N U   I T E M S
        self.popupMenuSphere = QtWidgets.QMenu()
        SphereMenu_Entry_1 = self.popupMenuSphere.addAction("Sphere sbdv 12")
        SphereMenu_Entry_2 = self.popupMenuSphere.addAction("Sphere sbdv 14")
        SphereMenu_Entry_3 = self.popupMenuSphere.addAction("Sphere sbdv 16")
        SphereMenu_Entry_4 = self.popupMenuSphere.addAction("Sphere sbdv 18")
        SphereMenu_Entry_5 = self.popupMenuSphere.addAction("Sphere sbdv 20")
        SphereMenu_Entry_6 = self.popupMenuSphere.addAction("Sphere sbdv 22")
        SphereMenu_Entry_1.triggered.connect(partial(self.Create_Sphere, 12, 6))
        SphereMenu_Entry_2.triggered.connect(partial(self.Create_Sphere, 14, 8))
        SphereMenu_Entry_3.triggered.connect(partial(self.Create_Sphere, 16, 10))
        SphereMenu_Entry_4.triggered.connect(partial(self.Create_Sphere, 18, 10))
        SphereMenu_Entry_5.triggered.connect(partial(self.Create_Sphere, 20, 12))
        SphereMenu_Entry_6.triggered.connect(partial(self.Create_Sphere, 22, 12))

        ##---------------------------------------------------- PRIMITIVES - CYLINDER
        self.CylinderBtn = MyCustomBtn_Widget()
        self.CylinderBtn.setObjectName("TABSBTN")
        self.CylinderBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.CylinderBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.CylinderBtn.setIcon(QtGui.QIcon(IconPath + "Prim_CYLINDRE.png"))
        self.CylinderBtn.clicked.connect(partial(self.Create_Cylinder, 2, 16))

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.CylinderBtn.customContextMenuRequested.connect(self.showPopupCylinder)
        #   CUBE M E N U   I T E M S
        self.popupMenuCylinder = QtWidgets.QMenu()
        CylinderMenu_Entry_0 = self.popupMenuCylinder.addAction("------------X")
        CylinderMenu_Entry_1 = self.popupMenuCylinder.addAction("Cylinder 8")
        CylinderMenu_Entry_2 = self.popupMenuCylinder.addAction("Cylinder 12")
        CylinderMenu_Entry_3 = self.popupMenuCylinder.addAction("Cylinder 16")
        CylinderMenu_Entry_4 = self.popupMenuCylinder.addAction("Cylinder  28")
        CylinderMenu_Entry_00 = self.popupMenuCylinder.addAction("------------Y")
        CylinderMenu_Entry_5 = self.popupMenuCylinder.addAction("Cylinder 8")
        CylinderMenu_Entry_6 = self.popupMenuCylinder.addAction("Cylinder 12")
        CylinderMenu_Entry_7 = self.popupMenuCylinder.addAction("Cylinder 16")
        CylinderMenu_Entry_8 = self.popupMenuCylinder.addAction("Cylinder  28")
        CylinderMenu_Entry_000 = self.popupMenuCylinder.addAction("------------Z")
        CylinderMenu_Entry_9 = self.popupMenuCylinder.addAction("Cylinder 8")
        CylinderMenu_Entry_10 = self.popupMenuCylinder.addAction("Cylinder 12")
        CylinderMenu_Entry_11 = self.popupMenuCylinder.addAction("Cylinder 16")
        CylinderMenu_Entry_12 = self.popupMenuCylinder.addAction("Cylinder  28")
        CylinderMenu_Entry_1.triggered.connect(partial(self.Create_Cylinder, 1, 8))
        CylinderMenu_Entry_2.triggered.connect(partial(self.Create_Cylinder, 1, 12))
        CylinderMenu_Entry_3.triggered.connect(partial(self.Create_Cylinder, 1, 16))
        CylinderMenu_Entry_4.triggered.connect(partial(self.Create_Cylinder, 1, 28))

        CylinderMenu_Entry_5.triggered.connect(partial(self.Create_Cylinder, 2, 8))
        CylinderMenu_Entry_6.triggered.connect(partial(self.Create_Cylinder, 2, 12))
        CylinderMenu_Entry_7.triggered.connect(partial(self.Create_Cylinder, 2, 16))
        CylinderMenu_Entry_8.triggered.connect(partial(self.Create_Cylinder, 2, 28))

        CylinderMenu_Entry_9.triggered.connect(partial(self.Create_Cylinder, 3, 8))
        CylinderMenu_Entry_10.triggered.connect(partial(self.Create_Cylinder, 3, 12))
        CylinderMenu_Entry_11.triggered.connect(partial(self.Create_Cylinder, 3, 16))
        CylinderMenu_Entry_12.triggered.connect(partial(self.Create_Cylinder, 3, 28))



        ##---------------------------------------------------- PRIMITIVES - PLANE
        self.PlaneBtn = MyCustomBtn_Widget()
        self.PlaneBtn.setObjectName("TABSBTN")
        self.PlaneBtn.setFixedSize(iconFixeSize, iconFixeSize)
        self.PlaneBtn.setIconSize(QtCore.QSize(iconButtonSize, iconButtonSize))
        self.PlaneBtn.setIcon(QtGui.QIcon(IconPath + "Prim_PLANE.png"))
        self.PlaneBtn.clicked.connect(partial(self.Create_Plane, 2))

        #   C O N N E C T   P O P U P   M E N U   T O   O U R   B U T T O N
        self.PlaneBtn.customContextMenuRequested.connect(self.showPopupPlane)
        #   CUBE M E N U   I T E M S
        self.popupMenuPlane = QtWidgets.QMenu()
        PlaneMenu_Entry_1 = self.popupMenuPlane.addAction("Plane X")
        PlaneMenu_Entry_2 = self.popupMenuPlane.addAction("Plane Y")
        PlaneMenu_Entry_3 = self.popupMenuPlane.addAction("Plane Z")
        PlaneMenu_Entry_1.triggered.connect(partial(self.Create_Plane, 1))
        PlaneMenu_Entry_2.triggered.connect(partial(self.Create_Plane, 2))
        PlaneMenu_Entry_3.triggered.connect(partial(self.Create_Plane, 3))


        ##---------------------------------------------------- Add to Layout
        SECTION_PRIMITIVES_LAYOUT.addWidget(self.CubeBtn)
        SECTION_PRIMITIVES_LAYOUT.addWidget(self.SphereBtn)
        SECTION_PRIMITIVES_LAYOUT.addWidget(self.CylinderBtn)
        SECTION_PRIMITIVES_LAYOUT.addWidget(self.PlaneBtn)
    #------------------------------------------------
    ##----------------------------------------------------   D E F I N I T I O N
    #------------------------------------------------
    def BAM(self):
        print("BAMMM")


        # Data to be written
        dictionary = {
            "name": "Wizix",
            "Age": 32,
            "Tag": "wzx",
        }

        open(PreferencePath + 'TestFile.json', "w").write(json.dumps(dictionary, indent=3))
    def BAM2(self):
        print("BAMMM2")

        # Data to be written
        entry = {"Age": 36}

        filename = PreferencePath + 'TestFile.json'
        lst = [{'alice': 24, 'bob': 27}]

        with open(filename, mode='w') as f:
            lst.append({'carl': 33})
            json.dump(lst, f)


    def Create_Cube(self, subdiv):
        #_______________VAR
        MultiScale = (json.load(open(PreferencePath + 'Setting_Primitives_Size.json', "r"))['PRIM_SIZE'])
        InteractionMode = (json.load(open(PreferencePath + 'Setting_Primitives_Placement.json', "r"))['PRIM_MODE'])
        PRIM_TOPOF = (json.load(open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "r"))['VALUE'])

        self.CubeBtn.update()
        RenameName = "Cube_001"


        if InteractionMode == 0:
            selection = mc.ls(sl=True)
            createCubePrim = mc.polyCube(w=10 * MultiScale, h=10 * MultiScale, d=10 * MultiScale, sx=subdiv, sy=subdiv,   sz=subdiv, ax=[0, 1, 0], cuv=4, ch=1)

            if selection == []: #GRID MODE
                createCubePrim
                mc.select(createCubePrim)
                mc.CenterPivot()
                myObj = mc.rename(RenameName)
                mc.polySoftEdge(a=45, ch=1)
                mc.makeIdentity(apply=True)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')

            elif mc.objectType(selection[0]) == "mesh": #COMPONENT MODE
                mc.select(selection)
                mc.setToolTo('moveSuperContext')
                pos = mc.manipMoveContext('Move', query=True, position=True)
                createCubePrim
                mc.select(createCubePrim)
                # 1 - Place at component position
                mc.move(pos[0], pos[1], pos[2])
                constr = mc.normalConstraint(selection, createCubePrim, aimVector=(0, 1, 0), worldUpType=0)
                mc.delete(constr)
                myObj = mc.rename(RenameName)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')


            else: #ON TOP OF MODE
                if PRIM_TOPOF == 1:
                    createCubePrim
                    mc.select(createCubePrim)
                    mc.xform(ws=1, a=1, piv=[0, 0, 0])
                    mc.makeIdentity(apply=True)

                    ##_______________Get Selection BBOX
                    bbox = mc.exactWorldBoundingBox(selection)
                    Ymin = bbox[1]
                    YMax = bbox[4]

                    # 0 - Init Freeze at Origin asset
                    bbox = mc.exactWorldBoundingBox(createCubePrim)
                    bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
                    mc.xform(createCubePrim, piv=bottom, ws=True)
                    mc.move(0, 0, 0, createCubePrim, rpr=True)
                    mc.select(createCubePrim)
                    mc.makeIdentity(apply=True, t=1, r=1, s=1)


                    # 1 - Place at obj posion
                    mc.matchTransform(createCubePrim, selection, pos=True)

                    # 2 - Up to Top
                    mc.move(YMax, createCubePrim, y=True, a=True)


                    mc.select(createCubePrim[0])
                    mc.CenterPivot()
                    myObj = mc.rename(RenameName)
                    mc.polySoftEdge(a=45, ch=1)
                    mc.makeIdentity(apply=True)
                    mc.select(cl= True)
                    mc.select(myObj)
                    mc.setToolTo('moveSuperContext')
                else:
                    pass

        else:
            #VERIF SELECTION
            SELECTION = mc.ls(sl=True)
            if SELECTION == []:
                ModIt_Global.WarningWindow("You should select a mesh", 250)
                return

            mc.SelectVertexMask()
            mc.SelectToggleMode()

            #ACTIVATE INTERACTIVE CREATION USER
            if mc.optionVar(q="createPolyPrimitiveAsTool") == 0:
                mc.ToggleCreatePolyPrimitivesAsTool()
            if mc.optionVar(q="polyPrimitiveAsToolExitOnComplete") == 0:
                mc.TogglePolyPrimitivesAsToolExitOnComplete()


            #ADD TO SNAP OBJECT
            ##KILL INTERACTIVE PRIM SCRIPT JOB
            JOB_NUMBER = (json.load(open(PreferencePath + 'JobNumber.json', "r"))['JOB_NUMBER'])

            try:
                mc.scriptJob(kill=JOB_NUMBER, force=True)
            except:
                pass

            mc.makeLive()
            #ACTIVATE INTERACTIVE et EXIT
            InteractiveModeScriptJob = mel.eval('int $jobNum = `scriptJob -ct "SomethingSelected" "makeLive -none;" -protected`;')

            open(PreferencePath + 'JobNumber.json', "w").write(json.dumps({"JOB_NUMBER": InteractiveModeScriptJob}))


            mc.createPolyCubeCtx("CreatePolyCubeCtx", e=True, w=10*MultiScale, h=10*MultiScale, d=10*MultiScale, sh=subdiv, sd=subdiv, sw=subdiv)
            mc.setToolTo("CreatePolyCubeCtx")




    def Create_Sphere(self, subdivA, subdivH):
        # _______________VAR
        MultiScale = (json.load(open(PreferencePath + 'Setting_Primitives_Size.json', "r"))['PRIM_SIZE'])
        InteractionMode = (json.load(open(PreferencePath + 'Setting_Primitives_Placement.json', "r"))['PRIM_MODE'])
        PRIM_TOPOF = (json.load(open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "r"))['VALUE'])
        self.SphereBtn.update()
        RenameName = "Sphere_001"

        if InteractionMode == 0:
            selection = mc.ls(sl=True)
            createSpherePrim = mc.polySphere(r=5*MultiScale, sx=subdivA, sy=subdivH, ax=[0, 1, 0], cuv=2,ch=1)

            if selection == []:  # GRID MODE
                createSpherePrim
                mc.select(createSpherePrim)
                mc.CenterPivot()
                myObj = mc.rename(RenameName)
                mc.polySoftEdge(a=45, ch=1)
                mc.makeIdentity(apply=True)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')

            elif mc.objectType(selection[0]) == "mesh":  # COMPONENT MODE
                mc.select(selection)
                mc.setToolTo('moveSuperContext')
                pos = mc.manipMoveContext('Move', query=True, position=True)
                createSpherePrim
                mc.select(createSpherePrim)
                # 1 - Place at component position
                mc.move(pos[0], pos[1], pos[2])
                constr = mc.normalConstraint(selection, createSpherePrim, aimVector=(0, 1, 0), worldUpType=0)
                mc.delete(constr)
                myObj = mc.rename(RenameName)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')


            else:  # ON TOP OF MODE
                if PRIM_TOPOF == 1:
                    createSpherePrim
                    mc.select(createSpherePrim)
                    mc.xform(ws=1, a=1, piv=[0, 0, 0])
                    mc.makeIdentity(apply=True)

                    ##_______________Get Selection BBOX
                    bbox = mc.exactWorldBoundingBox(selection)
                    Ymin = bbox[1]
                    YMax = bbox[4]

                    # 0 - Init Freeze at Origin asset
                    bbox = mc.exactWorldBoundingBox(createSpherePrim)
                    bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
                    mc.xform(createSpherePrim, piv=bottom, ws=True)
                    mc.move(0, 0, 0, createSpherePrim, rpr=True)
                    mc.select(createSpherePrim)
                    mc.makeIdentity(apply=True, t=1, r=1, s=1)

                    # 1 - Place at obj posion
                    mc.matchTransform(createSpherePrim, selection, pos=True)

                    # 2 - Up to Top
                    mc.move(YMax, createSpherePrim, y=True, a=True)

                    mc.select(createSpherePrim[0])
                    mc.CenterPivot()
                    myObj = mc.rename(RenameName)
                    mc.polySoftEdge(a=45, ch=1)
                    mc.makeIdentity(apply=True)
                    mc.select(cl= True)
                    mc.select(myObj)
                    mc.setToolTo('moveSuperContext')
                else:
                    pass
        else:
            # VERIF SELECTION
            SELECTION = mc.ls(sl=True)
            if SELECTION == []:
                ModIt_Global.WarningWindow("You should select a mesh", 250)
                return

            mc.SelectVertexMask()
            mc.SelectToggleMode()

            # ACTIVATE INTERACTIVE CREATION USER
            if mc.optionVar(q="createPolyPrimitiveAsTool") == 0:
                mc.ToggleCreatePolyPrimitivesAsTool()
            if mc.optionVar(q="polyPrimitiveAsToolExitOnComplete") == 0:
                mc.TogglePolyPrimitivesAsToolExitOnComplete()

            # ADD TO SNAP OBJECT
            ##KILL INTERACTIVE PRIM SCRIPT JOB
            JOB_NUMBER = (json.load(open(PreferencePath + 'JobNumber.json', "r"))['JOB_NUMBER'])

            try:
                mc.scriptJob(kill=JOB_NUMBER, force=True)
            except:
                pass

            mc.makeLive()
            # ACTIVATE INTERACTIVE et EXIT
            InteractiveModeScriptJob = mel.eval(
                'int $jobNum = `scriptJob -ct "SomethingSelected" "makeLive -none;" -protected`;')

            open(PreferencePath + 'JobNumber.json', "w").write(json.dumps({"JOB_NUMBER": InteractiveModeScriptJob}))

            mc.createPolySphereCtx("CreatePolySphereCtx", e=True, radius=5 * MultiScale, sh=subdivA, sw=subdivH)
            mc.setToolTo("CreatePolySphereCtx")
            mc.polySoftEdge(a=45, ch=1)

    def Create_Cylinder(self, axe, subdiv):
        # _______________VAR
        MultiScale = (json.load(open(PreferencePath + 'Setting_Primitives_Size.json', "r"))['PRIM_SIZE'])
        InteractionMode = (json.load(open(PreferencePath + 'Setting_Primitives_Placement.json', "r"))['PRIM_MODE'])
        PRIM_TOPOF = (json.load(open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "r"))['VALUE'])
        self.CylinderBtn.update()
        RenameName = "Cylinder_001"

        if axe == 1:
            axValue = [1, 0, 0]
        elif axe == 2:
            axValue = [0, 1, 0]
        elif axe == 3:
            axValue = [0, 0, 1]

        if InteractionMode == 0:
            selection = mc.ls(sl=True)
            createCylinderPrim = mc.polyCylinder(r=5 * MultiScale, h=10* MultiScale, sy=1, sz=0, ax= axValue, sc=0, cuv=4, ch=1, sa=subdiv)

            if selection == []:  # GRID MODE
                createCylinderPrim
                mc.select(createCylinderPrim)
                mc.CenterPivot()
                myObj = mc.rename(RenameName)
                mc.polySoftEdge(a=45, ch=1)
                mc.makeIdentity(apply=True)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')


            elif mc.objectType(selection[0]) == "mesh":  # COMPONENT MODE
                mc.select(selection)
                mc.setToolTo('moveSuperContext')
                pos = mc.manipMoveContext('Move', query=True, position=True)
                createCylinderPrim
                mc.select(createCylinderPrim)
                # 1 - Place at component position
                mc.move(pos[0], pos[1], pos[2])
                constr = mc.normalConstraint(selection, createCylinderPrim, aimVector=(0, 1, 0), worldUpType=0)
                mc.delete(constr)
                myObj = mc.rename(RenameName)
                mc.select(cl= True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')


            else:  # ON TOP OF MODE
                if PRIM_TOPOF == 1:
                    createCylinderPrim
                    mc.select(createCylinderPrim)
                    mc.xform(ws=1, a=1, piv=[0, 0, 0])
                    mc.makeIdentity(apply=True)

                    ##_______________Get Selection BBOX
                    bbox = mc.exactWorldBoundingBox(selection)
                    Ymin = bbox[1]
                    YMax = bbox[4]

                    # 0 - Init Freeze at Origin asset
                    bbox = mc.exactWorldBoundingBox(createCylinderPrim)
                    bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
                    mc.xform(createCylinderPrim, piv=bottom, ws=True)
                    mc.move(0, 0, 0, createCylinderPrim, rpr=True)
                    mc.select(createCylinderPrim)
                    mc.makeIdentity(apply=True, t=1, r=1, s=1)

                    # 1 - Place at obj posion
                    mc.matchTransform(createCylinderPrim, selection, pos=True)

                    # 2 - Up to Top
                    mc.move(YMax, createCylinderPrim, y=True, a=True)

                    mc.select(createCylinderPrim[0])
                    mc.CenterPivot()
                    myObj = mc.rename(RenameName)
                    mc.polySoftEdge(a=45, ch=1)
                    mc.makeIdentity(apply=True)
                    mc.select(cl= True)
                    mc.select(myObj)
                    mc.setToolTo('moveSuperContext')
                else:
                    pass
        else:
            # VERIF SELECTION
            SELECTION = mc.ls(sl=True)
            if SELECTION == []:
                ModIt_Global.WarningWindow("You should select a mesh", 250)
                return

            mc.SelectVertexMask()
            mc.SelectToggleMode()

            # ACTIVATE INTERACTIVE CREATION USER
            if mc.optionVar(q="createPolyPrimitiveAsTool") == 0:
                mc.ToggleCreatePolyPrimitivesAsTool()
            if mc.optionVar(q="polyPrimitiveAsToolExitOnComplete") == 0:
                mc.TogglePolyPrimitivesAsToolExitOnComplete()

            # ADD TO SNAP OBJECT
            ##KILL INTERACTIVE PRIM SCRIPT JOB
            JOB_NUMBER = (json.load(open(PreferencePath + 'JobNumber.json', "r"))['JOB_NUMBER'])

            try:
                mc.scriptJob(kill=JOB_NUMBER, force=True)
            except:
                pass

            mc.makeLive()
            # ACTIVATE INTERACTIVE et EXIT
            InteractiveModeScriptJob = mel.eval(
                'int $jobNum = `scriptJob -ct "SomethingSelected" "makeLive -none;" -protected`;')

            open(PreferencePath + 'JobNumber.json', "w").write(json.dumps({"JOB_NUMBER": InteractiveModeScriptJob}))

            mc.createPolyCylinderCtx("CreatePolyCylinderCtx", e=True, radius=5 * MultiScale, height=10 * MultiScale , sa =subdiv)
            mc.setToolTo("CreatePolyCylinderCtx")
            mc.polySoftEdge(a=45, ch=1)


    def Create_Plane(self, axe):
        # _______________VAR
        MultiScale = (json.load(open(PreferencePath + 'Setting_Primitives_Size.json', "r"))['PRIM_SIZE'])
        InteractionMode = (json.load(open(PreferencePath + 'Setting_Primitives_Placement.json', "r"))['PRIM_MODE'])
        PRIM_TOPOF = (json.load(open(PreferencePath + 'Setting_Primitives_OnTopOf.json', "r"))['VALUE'])
        self.CubeBtn.update()
        RenameName = "Plane_001"

        if axe == 1:
            axValue = [1, 0, 0]
        elif axe == 2:
            axValue = [0, 1, 0]
        elif axe == 3:
            axValue = [0, 0, 1]

        if InteractionMode == 0:
            selection = mc.ls(sl=True)
            createPlanePrim =  mc.polyPlane(w=10 * MultiScale, h=10 * MultiScale, sx=1, sy=1, ax=axValue, cuv=2, ch=1)

            if selection == []:  # GRID MODE
                createPlanePrim
                mc.select(createPlanePrim)
                mc.CenterPivot()
                myObj = mc.rename(RenameName)
                mc.polySoftEdge(a=45, ch=1)
                mc.makeIdentity(apply=True)
                mc.select(cl=True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')

            elif mc.objectType(selection[0]) == "mesh":  # COMPONENT MODE
                mc.select(selection)
                mc.setToolTo('moveSuperContext')
                pos = mc.manipMoveContext('Move', query=True, position=True)
                createPlanePrim
                mc.select(createPlanePrim)
                # 1 - Place at component position
                mc.move(pos[0], pos[1], pos[2])
                constr = mc.normalConstraint(selection, createPlanePrim, aimVector=(0, 1, 0), worldUpType=0)
                mc.delete(constr)
                myObj = mc.rename(RenameName)
                mc.select(cl=True)
                mc.select(myObj)
                mc.setToolTo('moveSuperContext')


            else:  # ON TOP OF MODE
                if PRIM_TOPOF == 1:
                    createPlanePrim
                    mc.select(createPlanePrim)
                    mc.xform(ws=1, a=1, piv=[0, 0, 0])
                    mc.makeIdentity(apply=True)

                    ##_______________Get Selection BBOX
                    bbox = mc.exactWorldBoundingBox(selection)
                    Ymin = bbox[1]
                    YMax = bbox[4]

                    # 0 - Init Freeze at Origin asset
                    bbox = mc.exactWorldBoundingBox(createPlanePrim)
                    bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
                    mc.xform(createPlanePrim, piv=bottom, ws=True)
                    mc.move(0, 0, 0, createPlanePrim, rpr=True)
                    mc.select(createPlanePrim)
                    mc.makeIdentity(apply=True, t=1, r=1, s=1)

                    # 1 - Place at obj posion
                    mc.matchTransform(createPlanePrim, selection, pos=True)

                    # 2 - Up to Top
                    mc.move(YMax, createPlanePrim, y=True, a=True)

                    mc.select(createPlanePrim[0])
                    mc.CenterPivot()
                    myObj = mc.rename(RenameName)
                    mc.polySoftEdge(a=45, ch=1)
                    mc.makeIdentity(apply=True)
                    mc.select(cl=True)
                    mc.select(myObj)
                    mc.setToolTo('moveSuperContext')
                else:
                    pass



        else:
            # VERIF SELECTION
            SELECTION = mc.ls(sl=True)
            if SELECTION == []:
                ModIt_Global.WarningWindow("You should select a mesh", 250)
                return

            mc.SelectVertexMask()
            mc.SelectToggleMode()

            # ACTIVATE INTERACTIVE CREATION USER
            if mc.optionVar(q="createPolyPrimitiveAsTool") == 0:
                mc.ToggleCreatePolyPrimitivesAsTool()
            if mc.optionVar(q="polyPrimitiveAsToolExitOnComplete") == 0:
                mc.TogglePolyPrimitivesAsToolExitOnComplete()

            # ADD TO SNAP OBJECT
            ##KILL INTERACTIVE PRIM SCRIPT JOB
            JOB_NUMBER = (json.load(open(PreferencePath + 'JobNumber.json', "r"))['JOB_NUMBER'])

            try:
                mc.scriptJob(kill=JOB_NUMBER, force=True)
            except:
                pass

            mc.makeLive()
            # ACTIVATE INTERACTIVE et EXIT
            InteractiveModeScriptJob = mel.eval(
                'int $jobNum = `scriptJob -ct "SomethingSelected" "makeLive -none;" -protected`;')

            open(PreferencePath + 'JobNumber.json', "w").write(json.dumps({"JOB_NUMBER": InteractiveModeScriptJob}))

            mc.createPolyPlaneCtx("CreatePolyPlaneCtx", e=True, w=10 * MultiScale, h=10 * MultiScale,  sh=1, sw=1)
            mc.setToolTo("CreatePolyPlaneCtx")


    def showPopupCube(self, position):
        self.popupMenuCube.exec_(self.CubeBtn.mapToGlobal(position))
        self.CubeBtn.update()

    def showPopupSphere(self, position):
        self.popupMenuSphere.exec_(self.SphereBtn.mapToGlobal(position))
        self.SphereBtn.update()

    def showPopupCylinder(self, position):
        self.popupMenuCylinder.exec_(self.CylinderBtn.mapToGlobal(position))
        self.CylinderBtn.update()

    def showPopupPlane(self, position):
        self.popupMenuPlane.exec_(self.PlaneBtn.mapToGlobal(position))
        self.PlaneBtn.update()




