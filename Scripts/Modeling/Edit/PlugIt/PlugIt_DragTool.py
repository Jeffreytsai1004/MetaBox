import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from maya.OpenMaya import MGlobal
import math
import os
import os, json
import random
import re
from pymel.core.datatypes import Vector, Matrix, Point
import pymel.core as pm
import shutil
from . import PlugIt_UI
from . import PlugIt_Global
import importlib
importlib.reload(PlugIt_Global)

##_______________________________________________ GLOBALS VAR
sampleFileChoice = []
PreferencePath = PlugIt_Global.PreferencePath
##______________________________ VAR
finalMeshName = "noFinalMesh"


def goPress(fileMA): #_________________________________________LA DEF QUI LANCE LE PLACE TOOL
    SaveSize_pref = json.load(open(PreferencePath + 'DRAGMODE_Size.json', "r"))
    MULTISIZEVALUE = (SaveSize_pref['VALUE'])

    sampleMesh = str(fileMA) #GET THE ASSET CLICK FULL PATH MA


    global selAnyList
    selAnyList = mc.ls(sl=1,fl=1,l=1)
    global sampleFileChoice
    global pressFirstTime
    global betweenFirstTime
    global screenX,screenY
    global betweenList
    global betweenListShape
    global checkVisList
    global selectionPool
    global combineSelPool

    screenX = 0
    screenY = 0
    betweenList = []
    betweenListShape = []
    betweenFirstTime = 1
    pressFirstTime = 1
    selectionPool = []
    combineSelPool = []
    checkVisList = screenVisPoly()

       
    sampleName = (sampleMesh.split('/')[-1]).split('.')[0]
    mc.CreateEmptyGroup()
    mc.rename(sampleName + '_Ctrl') ##__________________________________________CREATION DU GROUPE QUI CONTIENT LE MESH
    checkName = mc.ls(sl=True)
    ##__________________________________________IMPORT ASSET
    # ____ .MA
    before = set(mc.ls(assemblies=True, l= True))

    mc.file(sampleMesh, i=True)

    after = set(mc.ls(assemblies=True, l= True))
    imported = after.difference(before)

    # ____ Clean ExtraSecure
    mc.select("Plug_ExtraSecure_set")
    mc.DeleteEdge()
    mc.delete("Plug_ExtraSecure_set")


    # ____ FLIP OPTION
    # mc.select(imported)
    # plugMesh = mc.ls(sl=True)
    # mc.setAttr(plugMesh[0] + ".scaleY", -1)
    # mc.select(imported)
    # mc.ReversePolygonNormals()




    mc.parent(imported, checkName[0])


    #PLUG IT INIT PROCEDURES
    #Del the Curve Controler don't need
    mc.delete("Plug_controler")

    mc.select(checkName[0])

    if MULTISIZEVALUE != 1.0:
        mc.setAttr(checkName[0] + ".scaleX", MULTISIZEVALUE)
        mc.setAttr(checkName[0] + ".scaleY", MULTISIZEVALUE)
        mc.setAttr(checkName[0] + ".scaleZ", MULTISIZEVALUE)

    mc.makeIdentity(apply=True)

    mc.xform(ws=1, a=1 ,piv =[0, 0, 0])
    mc.pickWalk(d="down")
    tempSel = mc.ls(sl=True,type='transform',l=True)
    folderName = (sampleMesh.split('/')[-2])

    mc.select(tempSel)

    
    tempSel = mc.ls(sl=True,type='transform',l=True)
    mc.select(tempSel[0])
    sampleFileChoice = checkName
    mc.setAttr((sampleFileChoice[0]+'.scaleX'),0)
    mc.setAttr((sampleFileChoice[0]+'.scaleY'),0)
    mc.setAttr((sampleFileChoice[0]+'.scaleZ'),0)
    
    runIt()

    if sampleFileChoice:
        if mc.objExists(sampleFileChoice[0]):
            childNode =   mc.listRelatives(sampleFileChoice[0],type='transform',ad=True,f=True)
            for c in childNode:
                if not mc.attributeQuery('targetGeo', node = c, ex=True ):
                    mc.addAttr(c, ln='targetGeo',  dt= 'string')
                    mc.setAttr((c+'.targetGeo'),e=True, keyable=True)




def runIt():
    global ctx
    ctx = 'Click2dTo3dCtx'
    # Delete dragger context if it already exists
    if mc.draggerContext(ctx, exists=True):
        mc.deleteUI(ctx)
    # Create dragger context and set it to the active tool
    mc.draggerContext(ctx, pressCommand = onPressPlace, rc = offPressPlace, dragCommand = onDragPlace, fnz = finishTool, name=ctx, cursor='crossHair',undoMode='step')
    mc.setToolTo(ctx)

##______________________________ PLACE TOOL - DRAGGER VAR
def getPosition(SX, SY):
    global betweenListShape
    global checkVisList
    global finalMeshName




    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()
    omui.M3dView().active3dView().viewToWorld(int(SX), int(SY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    # current camera
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()

    cameraTrans = mc.listRelatives(camPath, type='transform', p=True)
    cameraPosition = mc.xform(cameraTrans, q=1, ws=1, rp=1)

    checkHit = 0
    finalMesh = []
    finalX = []
    finalY = []
    finalZ = []

    shortDistance = 10000000000
    distanceBetween = 1000000000

    hitFacePtr = om.MScriptUtil().asIntPtr()
    hitFace = []
    checkList = []

    checkStackMode = 1
    shapesNodestOnly = []
    try:
        shapesList = mc.listRelatives(betweenListShape, ad=True, f=True)
        shapesNodestOnly = mc.ls(shapesList, type='shape', l=1, fl=1)
    except:
        pass
    if checkStackMode == 1:
        checkList = checkVisList
        try:
            checkList = list(set(checkVisList) - set(shapesNodestOnly))
        except:
            pass
    else:
        checkList = screenVisPoly()
        checkList = list(set(checkList) - set(shapesNodestOnly))

    for mesh in checkList:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)

        intersection = fnMesh.closestIntersection(
            om.MFloatPoint(pos2),
            om.MFloatVector(dir),
            None,
            None,
            False,
            om.MSpace.kWorld,
            99999,
            False,
            None,
            hitpoint,
            None,
            hitFacePtr,
            None,
            None,
            None)

        if intersection:
            x = hitpoint.x
            y = hitpoint.y
            z = hitpoint.z
            distanceBetween = math.sqrt(
                ((float(cameraPosition[0]) - x) ** 2) + ((float(cameraPosition[1]) - y) ** 2) + (
                            (float(cameraPosition[2]) - z) ** 2))
            if distanceBetween < shortDistance:
                shortDistance = distanceBetween
                finalMesh = mesh
                finalX = x
                finalY = y
                finalZ = z
                hitFace = om.MScriptUtil(hitFacePtr).asInt()


    print("FINAL MESH = " + str(finalMesh))
    finalMeshName = finalMesh





    return finalX, finalY, finalZ, finalMesh, hitFace
    mc.refresh(cv=True, f=True)

def onPressPlace():
    global ctx
    global betweenListShape
    betweenListShape = []
    global SycList
    SycList = []
    global sampleFileChoice
    global selectionPool
    global combineSelPool
    global pressFirstTime
    global betweenFirstTime
    betweenFirstTime = 1
    global screenX, screenY
    global headMesh
    headMesh = []
    global tailMesh
    global lastSnapMesh
    global currentScaleRecord
    global currentRotRecord
    tailMesh = []
    checkSnapState = 1

    vpX, vpY, _ = mc.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY

    meshTypeState = 1  # 1 = MESH / 2 = INSTANCE

    try:
        if pressFirstTime == 1:
            # check samplePool still item, if yes random select one
            # multiMode
            newChoice = []
            if len(sampleFileChoice) > 1:
                randomNumber = random.randint(0, (len(sampleFileChoice) - 1))
                newChoice = sampleFileChoice[randomNumber]
                sampleFileChoice.remove(newChoice)
                selectionPool.append(newChoice)

            else:
                newChoice = sampleFileChoice[0]
                sampleFileChoice.remove(newChoice)
                selectionPool.append(newChoice)
                pressFirstTime = 0

            # combine two list for selection###bug
            combineSelPool = list(set(sampleFileChoice + selectionPool))
            mc.select(newChoice)

        else:
            newNodeA = []
            randomNumber = random.randint(0, (len(combineSelPool) - 1))
            newChoiceA = combineSelPool[randomNumber]

            if meshTypeState == 2:
                # only instance mesh not tranform node
                newNodeA = mc.duplicate(newChoiceA, rr=True)
                mc.select(newNodeA)
                mc.pickWalk(d='Down')
                meshNode = mc.ls(sl=True, l=True)
                mc.select(newChoiceA)
                mc.pickWalk(d='Down')
                mc.instance()
                mc.delete(meshNode)
                intNode = mc.ls(sl=True, l=True)
                mc.parent(intNode, newNodeA)
                mc.rename(meshNode[0].split('|')[-1])
                mc.pickWalk(d='up')
            else:
                newNodeA = mc.duplicate(newChoiceA, rr=True)
            mc.select(newNodeA)

        tempSel = mc.ls(sl=1, type='transform')


        wx, wy, wz, hitmesh, hitFace = getPosition(screenX, screenY)
        lastSnapMesh = hitmesh







        mc.setAttr((tempSel[0] + '.translateX'), wx)
        mc.setAttr((tempSel[0] + '.translateY'), wy)
        mc.setAttr((tempSel[0] + '.translateZ'), wz)
        hitFaceName = (hitmesh + '.f[' + str(hitFace) + ']')

        if checkSnapState == 1:
            rx, ry, rz = checkFaceAngle(hitFaceName)
            mc.setAttr((tempSel[0] + '.rotateX'), rx)
            mc.setAttr((tempSel[0] + '.rotateY'), ry)
            mc.setAttr((tempSel[0] + '.rotateZ'), rz)

        mc.setAttr((tempSel[0] + '.scaleX'), 1)
        mc.setAttr((tempSel[0] + '.scaleY'), 1)
        mc.setAttr((tempSel[0] + '.scaleZ'), 1)


        ##__________________________# Initialement Valeur de Slider
        currentScaleX = 1.0
        currnetRotY = 0.0
        currentDepth = 0.0
        randomY = 0.0
        silderScale = 1.0
        randomScale = 0.0
        randomSwing = 0.0

        mc.pickWalk(tempSel[0], direction='down')
        meshNode = mc.ls(sl=1, type='transform', l=1)
        # meshNode = mc.listRelatives(tempSel[0],c=True, typ = 'transform',f=True)
        SycList.append(meshNode[0])
        mc.setAttr((meshNode[0] + '.scaleX'), currentScaleX)
        mc.setAttr((meshNode[0] + '.scaleY'), currentScaleX)
        mc.setAttr((meshNode[0] + '.scaleZ'), currentScaleX)

        currentScaleRecord = currentScaleX
        mc.setAttr((meshNode[0] + '.rotateY'), currnetRotY)
        currentRotRecord = currnetRotY
        mc.setAttr((meshNode[0] + '.translateY'), currentDepth)

        if (randomY > 0):
            randomNumber = random.uniform(0, randomY)
            mc.setAttr((meshNode[0] + '.rotateY'), int(randomNumber))
            currentRotRecord = int(randomNumber)

        if (randomScale > 0):
            randomNumber = random.uniform((-1 * randomScale), randomScale)
            mc.setAttr((meshNode[0] + '.scaleX'), (randomNumber + silderScale))
            mc.setAttr((meshNode[0] + '.scaleY'), (randomNumber + silderScale))
            mc.setAttr((meshNode[0] + '.scaleZ'), (randomNumber + silderScale))
            currentScaleRecord = (randomNumber + silderScale)

        if randomSwing > 0:
            offsetNode = mc.listRelatives(meshNode[0], type='transform', p=True)
            randomNumberX = random.uniform(-1 * randomSwing, randomSwing)
            mc.setAttr((offsetNode[0] + '.rotateX'), int(randomNumberX))
            randomNumberZ = random.uniform(-1 * randomSwing, randomSwing)
            mc.setAttr((offsetNode[0] + '.rotateZ'), int(randomNumberZ))

        mc.select(tempSel)


        #######################################################################

        transNode = mc.listRelatives(lastSnapMesh, type='transform', p=True, f=True)
        mc.setAttr((meshNode[0] + '.targetGeo'), transNode[0], type="string")

    #########################################################################
    except:
        pass

    mc.refresh(cv=True, f=True)

def offPressPlace():

    global tempCmd
    global betweenList
    global betweenList3DPos
    global finalMeshName
    betweenList3DPos = []

    for e in betweenList:
        attList = ['translateX','translateY','translateZ']
        attListRecord =['ptX','ptY','ptZ']
        for a in range(len(attList)):
            attListRecord[a] = mc.getAttr(e +'.'+attList[a])
        pos3D = (attListRecord[0],attListRecord[1],attListRecord[2])
        betweenList3DPos.append(pos3D )
    mc.refresh(cv=True,f=True)
    deSelect()

    #Get Active Sel Mode
    activeSelMode = mc.selectMode(q=True, root=True)
    if activeSelMode == False:
        mc.selectMode(root=True)

    else:
        mc.selectMode(object=True)

    # Get ShapeNodeName
    mc.select(finalMeshName)
    OriginShapesName = mc.ls(sl=True)[0]

    #Get Material of TargetMesh
    mc.select(finalMeshName)
    theNodes = mc.ls(sl=True, dag=True, s=True)
    shadeEng = mc.listConnections(theNodes, type="shadingEngine")
    getMaterial = mc.ls(mc.listConnections(shadeEng), materials=True)[0]
    mc.select(cl= True)

    ######################################################## S T A R T
    FLIP = (json.load(open(PreferencePath + 'DRAGMODE_Flip.json', "r"))['VALUE'])

    # ______________________________/ UNDO SAVED
    if mc.objExists("PlugItDupSave_*"):
        mc.select("PlugItDupSave_*")
        mc.delete()

    mc.duplicate(finalMeshName, n= "UndoMeshTemp")
    mc.select("UndoMeshTemp")
    mc.Unparent()
    mc.HideSelectedObjects()
    mc.setAttr("UndoMeshTemp.hiddenInOutliner", 1)
    try:
        mel.eval("AEdagNodeCommonRefreshOutliners();")
    except:
        pass

    # ______________________________/ PIVOT SAVED
    mc.spaceLocator(n="PlugIt_OrignMesh_PivotSave")
    mc.select("PlugIt_OrignMesh_PivotSave", finalMeshName)
    mc.MatchTransform()






    # ______________________________/ FLIP OPTION
    if FLIP == 1:
        mc.setAttr("Plug_Mesh.scaleY", -1)
        mc.polyNormal("Plug_Mesh", normalMode=0, userNormalMode=0, ch=1)
        mc.select("Plug_Mesh")
        mc.FreezeTransformations()
        mc.delete("Plug_Mesh", ch=True)

    # ______________________________/ DUPLICATE PLUG
    mc.duplicate("Plug_Mesh", n="Plug_Mesh_Dup")
    mc.select("Plug_Mesh_Dup")
    mc.ConvertSelectionToFaces()
    mc.sets(rm="Plug_AllFaces_set")
    # Get Material of TargetMesh
    mc.select(finalMeshName)
    theNodes = mc.ls(sl=True, dag=True, s=True)
    shadeEng = mc.listConnections(theNodes, type="shadingEngine")
    getMaterial = mc.ls(mc.listConnections(shadeEng), materials=True)[0]
    mc.select(cl=True)
    mc.select("Plug_Mesh_Dup")
    mc.hyperShade(a=getMaterial)

    # ______________________________/ BBOX CAGE
    CageShd = mc.shadingNode('lambert', asShader=True, n="PlugIt_BBoxCage_shd")
    mc.setAttr("PlugIt_BBoxCage_shd.color", 0, 1, 0)
    mc.select("Plug_Mesh")
    mc.geomToBBox(name='Plug_Mesh', keepOriginal=0)
    mc.hyperShade(assign=CageShd)

    # ______________________________/ BOOL
    mc.polyCBoolOp(finalMeshName, 'Plug_Mesh', op=2, n="PlugIt_Bool")
    mc.delete("PlugIt_Bool", ch=True)
    mc.hyperShade(objects = CageShd)
    mc.delete()



    #Get Plug_Mesh_Dup Parent Name
    parentName = mc.listRelatives("Plug_Mesh_Dup", parent=True)

    # COMBINE
    mc.select("PlugIt_Bool", "Plug_Mesh_Dup")
    mc.polyUnite(ch=1, mergeUVSets=1, centerPivot=True, name="PlugIt_Drag_Combine")
    mc.select("PlugIt_Drag_Combine")
    mc.polyMergeVertex(d=0.01, am=1, ch=1)


    mc.delete("PlugIt_Drag_Combine", ch=True)
    if mc.objExists("Plug_EdgeBorder_set*"):
        mc.delete("Plug_EdgeBorder_set")
    if mc.objExists("Plug_Selection_set*"):
        mc.delete("Plug_Selection_set")
    if mc.objExists("PlugIt_BBoxCage_shd*"):
        mc.delete("PlugIt_BBoxCage_shd")


    # PivotBack
    mc.matchTransform('PlugIt_Drag_Combine', 'PlugIt_OrignMesh_PivotSave', piv=True)
    mc.delete("PlugIt_OrignMesh_PivotSave")


    if mc.objExists("PlugIt_Plug_Shd"):
        mc.delete("PlugIt_Plug_Shd")
    if mc.objExists("BBoxSG*"):
        mc.delete("BBoxSG*")
    if mc.objExists("PlugIt_BBoxCage_shdSG*"):
        mc.delete("PlugIt_BBoxCage_shdSG*")
    if mc.objExists("Plug_Hole_set"):
        mc.delete("Plug_Hole_set")

    # CLEAN
    mc.delete(parentName[0])




    ######################################################## E N D
    FinalMeshName = finalMeshName.split("|")[1]


    #finishTool()
    getame = mc.rename("PlugIt_Drag_Combine", str(FinalMeshName))
    mc.select(getame)
    transformName = mc.ls(sl=True)
    shapeNode = mc.listRelatives(transformName, shapes=True)[0]
    mc.rename(shapeNode, OriginShapesName)


    mc.rename("UndoMeshTemp", "PlugItDupSave_" + str(FinalMeshName))
    mc.MoveTool() #TO KEEP DRAG WORKING or OFF:
    mc.delete(str(getame), constructionHistory=True)
    mc.flushUndo()


def onDragPlace():

    global tempCmd
    tempCmd = []
    global ctx
    global pressFirstTime
    global betweenFirstTime
    global screenX,screenY
    global betweenList
    global betweenListShape
    global checkVisList
    global combineSelPool
    global SycList
    global headMesh
    global tailMesh
    global lastPanelActive
    global lastSnapMesh
    global currentScaleRecord
    global currentRotRecord
    
    
    checkSnapState = 1
    lastPanelActive = mc.getPanel(underPointer=True)
    currentSX = 0
    currnetSY = 0
    goStrightLine = 0.0
    randomY = 0.0
    meshTypeState = 1
    selSample = []
    selSample = mc.ls(sl=True,fl=True,l=True)
    headMesh = selSample[0]



    if len(selSample)>0:
        if (goStrightLine > 0):
            if betweenFirstTime == 1:
                #need to give one sample to first position
                attList = ['translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ']
                attListRecord =['ptX','ptY','ptZ','prX','prY','prZ','psX','psY','psZ']
                for a in range(len(attList)):
                    attListRecord[a] = mc.getAttr(selSample[0]+'.'+attList[a])
                #pick up sample if multiMode
                if len(combineSelPool)>1:
                        randomNumber = random.randint(0,(len(combineSelPool)-1))
                        mc.select(combineSelPool[randomNumber])
                else:
                    mc.select(selSample[0])
                keepItMesh = mc.ls(sl=1,fl=1)
                #make a copy
                if meshTypeState == 2:
                    #only instance mesh not tranform node
                    newKeepNode = mc.duplicate(keepItMesh[0],rr=True)
                    mc.select(newKeepNode)
                    mc.pickWalk(d='Down')
                    meshKeepNode = mc.ls(sl=True,l=True)
                    mc.select(keepItMesh[0])
                    mc.pickWalk(d='Down')
                    mc.instance()
                    mc.delete(meshKeepNode)
                    intKeepNode = mc.ls(sl=True,l=True)
                    mc.parent(intKeepNode,newKeepNode)
                    intKeepNode = mc.ls(sl=True,l=True)
                    mc.rename(meshKeepNode[0].split('|')[-1])
                    mc.pickWalk(d='up')
                else:
                    mc.duplicate(keepItMesh[0])
                #restore position
                checkKeepNode = mc.ls(sl=1,fl=1)
                for b in range(len(attList)):
                    mc.setAttr((checkKeepNode[0]+'.'+attList[b]),attListRecord[b])
                checkKeepNodeChild = mc.listRelatives(checkKeepNode[0],c=True, typ = 'transform',f=True)
                SycList.append(checkKeepNodeChild[0])

                meshNodeA = mc.listRelatives(selSample[0],c=True, typ = 'transform',f=True)

                SycList.append(meshNodeA[0])
                if randomY > 0:
                    randomNumber = random.uniform(0,randomY)
                    mc.setAttr((meshNodeA[0]+'.rotateY'),int(randomNumber))

                tailMesh = checkKeepNode[0]
                betweenList = []
                betweenListShape = []
                #get in between element
                for i in range(int(goStrightLine)):
                    if len(combineSelPool)>1:
                        randomNumber = random.randint(0,(len(combineSelPool)-1))
                        mc.select(combineSelPool[randomNumber])
                    else:
                        mc.select(selSample[0])

                    newBetweenDulpi = mc.ls(sl=True,fl=True,l=True)
                    if meshTypeState == 2:
                        #only instance mesh not tranform node
                        newNode = mc.duplicate(newBetweenDulpi[0],rr=True)
                        mc.select(newNode)
                        mc.pickWalk(d='Down')
                        meshNode = mc.ls(sl=True,l=True)
                        mc.select(newBetweenDulpi[0])
                        mc.pickWalk(d='Down')
                        mc.instance()
                        mc.delete(meshNode)
                        intNode = mc.ls(sl=True,l=True)
                        mc.parent(intNode,newNode)
                        intNode = mc.ls(sl=True,l=True)
                        mc.rename(meshNode[0].split('|')[-1])
                        mc.pickWalk(d='up')
                    else:
                        mc.duplicate(newBetweenDulpi[0])

                    selBetween = mc.ls(sl=True,fl=True,l=True)
                    meshNodeB = mc.listRelatives(selBetween[0],c=True, typ = 'transform',f=True)
                    
                    silderScale = 1.0
                    randomScale = 0.0
                    randomSwing = 0.0
                    
                    if (randomScale > 0):
                        randomNumber = random.uniform((-1*randomScale),randomScale)
                        newScale = (randomNumber+silderScale)
                        #bug calucation done but update not fast enough to show, evalDeferred works but not great
                        cmdx = 'mc.setAttr("' + meshNodeB[0] +'.scaleX",' + str(newScale) + ')'
                        mc.evalDeferred(cmdx)
                        cmdy = 'mc.setAttr("' + meshNodeB[0] +'.scaleY",' + str(newScale) + ')'
                        mc.evalDeferred(cmdy)
                        cmdz = 'mc.setAttr("' + meshNodeB[0] +'.scaleZ",' + str(newScale) + ')'
                        mc.evalDeferred(cmdz)


                    if randomY > 0:
                        randomNumber = random.uniform(0,randomY)
                        mc.setAttr((meshNodeB[0]+'.rotateY'),int(randomNumber))

                    if randomSwing > 0:
                        offsetNode = mc.listRelatives(meshNodeB[0],type='transform',p=True)
                        randomNumberX = random.uniform(-1*randomSwing,randomSwing)
                        mc.setAttr((offsetNode[0]+'.rotateX'),int(randomNumberX))
                        randomNumberZ = random.uniform(-1*randomSwing,randomSwing)
                        mc.setAttr((offsetNode[0]+'.rotateZ'),int(randomNumberZ))

                    SycList.append(meshNodeB[0])
                    betweenShape = mc.listRelatives(selBetween[0], fullPath=True ,c=True)
                    betweenList.append(selBetween[0])
                    betweenListShape.append(betweenShape[0])
                    betweenFirstTime = 0
        else:
            betweenListShape = []

        modifiers = mc.getModifiers()
        SycList = list(set(SycList))
        if (modifiers == 4):
            #print 'ctrl Press'
            DRAGMODE_ROTATE = (json.load(open(PreferencePath + 'DRAGMODE_Rotate.json', "r"))['VALUE'])

            vpX, vpY, _ = mc.draggerContext(ctx, query=True, dragPoint=True)
            distanceA = (vpX - screenX)
            rotateCheck = (distanceA)
            rotateRun = currentRotRecord + rotateCheck

            if rotateRun > 360 :
                rotateRun = 360
            elif rotateRun < -360 :
                rotateRun = -360
            getR = int(rotateRun / DRAGMODE_ROTATE)*DRAGMODE_ROTATE #ROTATE STEP
            if rotateRun != getR:
                rotateRun = getR
            #mc.floatSliderGrp( 'meshRotSlide', e=1 ,v = rotateRun )
            mc.setAttr((selSample[0]+'.rotateAxisY'),rotateRun)
            #mc.refresh(f=True)

        elif(modifiers == 1):

            #print 'shift selSample'
            vpX, vpY, _ = mc.draggerContext(ctx, query=True, dragPoint=True)
            distanceB = vpX - screenX
            scaleCheck = distanceB / 100
            scaleRun = currentScaleRecord + scaleCheck
            if scaleRun > 5:
                scaleRun = 5
            elif scaleRun < 0:
                scaleRun = 0.1

            #mc.floatSliderGrp( 'meshScaleSlide', e=1 ,v = scaleRun )
            if len(SycList)>0:
                    mc.setAttr((selSample[0] + '.scaleX'),scaleRun)
                    mc.setAttr((selSample[0] + '.scaleY'),scaleRun)
                    mc.setAttr((selSample[0] + '.scaleZ'),scaleRun)
            #mc.refresh(cv=True,f=True)
        else:
            vpX, vpY, _ = mc.draggerContext(ctx, query=True, dragPoint=True)
            currentSX = vpX
            currentSY = vpY
            pos = om.MPoint()
            dir = om.MVector()
            hitpoint = om.MFloatPoint()
            omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
            pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)

            #current camera
            view = omui.M3dView.active3dView()
            cam = om.MDagPath()
            view.getCamera(cam)
            camPath = cam.fullPathName()

            cameraTrans = mc.listRelatives(camPath,type='transform',p=True)
            cameraPosition = mc.xform(cameraTrans,q=1,ws=1,rp=1)

            checkHit = 0
            finalMesh = []
            finalX = 0
            finalY = 0
            finalZ = 0
            shortDistance = 10000000000
            distanceBetween = 1000000000

            checkList=[]
            meshNode = mc.listRelatives(selSample, fullPath=True ,c=True)
            myShape = mc.listRelatives(meshNode, shapes=True,f=True)

            shapesList = mc.listRelatives(betweenListShape,ad=True,f=True)
            shapesNodestOnly =  mc.ls(shapesList,type='shape',l=1,fl=1)


            if myShape == None:#gpu
                checkList =  list(set(checkVisList))
            else:
                checkStackMode  = 1
                if checkStackMode == 1:
                    checkList =  list(set(checkVisList)-set(myShape)-set(shapesNodestOnly))
                else:
                    checkList = screenVisPoly()
                    checkList.remove(myShape[0])
                    SycListShape = mc.listRelatives(SycList, shapes=True,f=True)
                    checkList = list(set(checkList) - set(shapesNodestOnly)- set(SycListShape))
            hitFacePtr = om.MScriptUtil().asIntPtr()
            hitFace = []
            for mesh in checkList:
                selectionList = om.MSelectionList()
                selectionList.add(mesh)
                dagPath = om.MDagPath()
                selectionList.getDagPath(0, dagPath)
                fnMesh = om.MFnMesh(dagPath)
                intersection = fnMesh.closestIntersection(
                om.MFloatPoint(pos2),
                om.MFloatVector(dir),
                None,
                None,
                False,
                om.MSpace.kWorld,
                99999,
                False,
                None,
                hitpoint,
                None,
                hitFacePtr,
                None,
                None,
                None)
                if intersection:
                    x = hitpoint.x
                    y = hitpoint.y
                    z = hitpoint.z
                    distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
                    if distanceBetween < shortDistance:
                        shortDistance = distanceBetween
                        finalMesh = mesh
                        hitFace = om.MScriptUtil(hitFacePtr).asInt()
                        hitFaceName = (finalMesh + '.f[' + str(hitFace) +']')
                        #buggy when this is done after it return incorrect information
                        if checkSnapState == 1:
                            rx, ry, rz = checkFaceAngle(hitFaceName)
                            mc.setAttr((selSample[0] + '.rotateX'), rx)
                            mc.setAttr((selSample[0] + '.rotateY'), ry)
                            mc.setAttr((selSample[0] + '.rotateZ'), rz)
                        finalX = x
                        finalY = y
                        finalZ = z
                    lastSnapMesh = finalMesh
                    #######################################################################
                    childNode =   mc.listRelatives(selSample[0],type='transform',ad=True,f=True)
                    transNode=mc.listRelatives(lastSnapMesh,type='transform',p=True,f=True)
                    for c in childNode:
                        mc.setAttr((c + '.targetGeo'),transNode[0],type="string")
                   #########################################################################
                    mc.setAttr((selSample[0] + '.translateX'), finalX)
                    mc.setAttr((selSample[0] + '.translateY'), finalY)
                    mc.setAttr((selSample[0] + '.translateZ'), finalZ)
                    hitFaceName = (finalMesh + '.f[' + str(hitFace) +']')

                    lockVtxCheck = 0.0
                    if (lockVtxCheck > 0):
                        cvX = 0
                        cvY = 0
                        cvZ = 0
                        shortDistanceCheck = 10000
                        checkCVDistance = 10000
                        mostCloseDist = lockVtxCheck
                        hitFaceName = (finalMesh + '.f[' + str(hitFace) +']')
                        cvList = (mc.polyInfo(hitFaceName , fv=True )[0]).split(':')[-1].split('    ')
                        cvList = [x for x in cvList if x.strip()]
                        mostCloseCVPoint = []
                        for v in cvList:
                            checkNumber = ''.join([n for n in v.split('|')[-1] if n.isdigit()])
                            if len(checkNumber) > 0:
                                cvPoint = (finalMesh + '.vtx[' + str(checkNumber) +']')
                                cvPosition = mc.pointPosition(cvPoint)
                                checkCVDistance = math.sqrt( ((float(cvPosition[0]) - finalX)**2)  + ((float(cvPosition[1]) - finalY)**2) + ((float(cvPosition[2]) - finalZ)**2))
                                if checkCVDistance < shortDistanceCheck:
                                    shortDistanceCheck = checkCVDistance
                                    cvX = float(cvPosition[0])
                                    cvY = float(cvPosition[1])
                                    cvZ = float(cvPosition[2])
                                    mostCloseCVPoint = cvPoint
                        if shortDistanceCheck < mostCloseDist:
                            mc.setAttr((selSample[0] + '.translateX'), cvX)
                            mc.setAttr((selSample[0] + '.translateY'), cvY)
                            mc.setAttr((selSample[0] + '.translateZ'), cvZ)
                            #get average normal angle from suround faces
                            if checkSnapState == 1:
                                rX,rY,rZ = avgVertexNormalAngle(cvPoint)
                                mc.setAttr(selSample[0]+'.rotateX', rX)
                                mc.setAttr(selSample[0]+'.rotateY', rY)
                                mc.setAttr(selSample[0]+'.rotateZ', rZ)

                    silderRandomPos = 0.0
                    # caculate new inBetween position
                    for a in range(int(goStrightLine)):
                        disX = (screenX - currentSX)/(goStrightLine+1)
                        disY = (screenY - currentSY)/(goStrightLine+1)
                        nextX = 0
                        nextY = 0
                        if silderRandomPos > 0:
                            randomNumberX = random.uniform((-1*silderRandomPos),silderRandomPos)
                            randomNumberY = random.uniform((-1*silderRandomPos),silderRandomPos)
                            nextX =   (screenX -(disX*(a+1) ))*(1+(randomNumberX*0.1))
                            nextY =   (screenY -(disY*(a+1))) *(1+(randomNumberY*0.1))

                        else:
                            nextX =   screenX -(disX*(a+1))
                            nextY =   screenY -(disY*(a+1))
                        wx,wy,wz,hitmesh,hitFace = getPosition(nextX,nextY)
                        if wx != []:
                            #######################################################################
                            childNode =   mc.listRelatives(betweenList[a],type='transform',ad=True,f=True)
                            transNode=mc.listRelatives(hitmesh,type='transform',p=True,f=True)
                            for c in childNode:
                                mc.setAttr((c + '.targetGeo'),transNode[0],type="string")
                            #########################################################################
                            mc.setAttr((betweenList[a] + '.translateX'), wx)
                            mc.setAttr((betweenList[a] + '.translateY'), wy)
                            mc.setAttr((betweenList[a] + '.translateZ'), wz)
                            if checkSnapState == 1:
                                hitFaceName = (hitmesh + '.f[' + str(hitFace) +']')
                                rx, ry, rz = checkFaceAngle(hitFaceName)
                                mc.setAttr((betweenList[a] + '.rotateX'), rx)
                                mc.setAttr((betweenList[a] + '.rotateY'), ry)
                                mc.setAttr((betweenList[a] + '.rotateZ'), rz)

        mc.select(selSample[0])
        mc.refresh(cv=True,f=True)

def finishTool():
    restoreSelVis()
    #mc.MoveTool()
    mc.select(cl=True)

    mel.eval('changeSelectMode - object;')
    mel.eval('updateSelectionModeIcons;')
    mel.eval('dR_selTypeChanged("");')

    print("FINISH")



##______________________________ PLACE TOOL - HELPERS
def restoreSelVis():
    mc.modelEditor('modelPanel1', e=True, sel=True)
    mc.modelEditor('modelPanel2', e=True, sel=True)
    mc.modelEditor('modelPanel3', e=True, sel=True)
    mc.modelEditor('modelPanel4', e=True, sel=True)

def screenVisPoly():
    commonList= []
    view = omui.M3dView.active3dView()
    om.MGlobal.selectFromScreen(0, 0, view.portWidth(), view.portHeight(), om.MGlobal.kReplaceList)
    objects = om.MSelectionList()
    sel = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(objects)
    #restore selection
    om.MGlobal.setActiveSelectionList(sel, om.MGlobal.kReplaceList)
    #return the objects as strings
    fromScreen = []
    objects.getSelectionStrings(fromScreen)
    shapesOnScreen = mc.listRelatives(fromScreen, shapes=True,f=True)
    meshList = mc.ls(type='mesh',l=True)#only polygon
    if len(meshList)>0 and shapesOnScreen is not None:
        commonList = list(set(meshList) & set(shapesOnScreen))
        return commonList
    else:
        commonList = []
        return commonList

def deSelect():
    obj_shape = mc.listRelatives(parent=True, f=True)
    obj = mc.listRelatives(obj_shape,parent=True, f=True)
    mc.select(obj)
    mc.selectMode(leaf=True)
    cmd = "changeSelectMode -object;"
    mel.eval(cmd)
    mc.select(clear=True)

def checkFaceAngle(faceName):
    shapeNode = mc.listRelatives(faceName, fullPath=True , parent=True )
    transformNode = mc.listRelatives(shapeNode[0], fullPath=True , parent=True )
    obj_matrix = Matrix(mc.xform(transformNode, query=True, worldSpace=True, matrix=True))
    face_normals_text = mc.polyInfo(faceName, faceNormals=True)[0]
    face_normals = [float(digit) for digit in re.findall(r'-?\d*\.\d*', face_normals_text)]
    v = Vector(face_normals) * obj_matrix
    if max(abs(v[0]), abs(v[1]), abs(v[2])) == -v[1]:
        pass
        #print face, v #if reverse, need to rotate another 180 degree
    upvector = om.MVector (0,1,0)
    getHitNormal = v
    quat = om.MQuaternion(upvector, getHitNormal)
    quatAsEuler = om.MEulerRotation()
    quatAsEuler = quat.asEulerRotation()
    rx, ry, rz = math.degrees(quatAsEuler.x), math.degrees(quatAsEuler.y), math.degrees(quatAsEuler.z)
    return rx, ry, rz

def screenVisPoly():
    commonList= []
    view = omui.M3dView.active3dView()
    om.MGlobal.selectFromScreen(0, 0, view.portWidth(), view.portHeight(), om.MGlobal.kReplaceList)
    objects = om.MSelectionList()
    sel = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(objects)
    #restore selection
    om.MGlobal.setActiveSelectionList(sel, om.MGlobal.kReplaceList)
    #return the objects as strings
    fromScreen = []
    objects.getSelectionStrings(fromScreen)
    shapesOnScreen = mc.listRelatives(fromScreen, shapes=True,f=True)
    meshList = mc.ls(type='mesh',l=True)#only polygon
    if len(meshList)>0 and shapesOnScreen is not None:
        commonList = list(set(meshList) & set(shapesOnScreen))
        return commonList
    else:
        commonList = []
        return commonList


