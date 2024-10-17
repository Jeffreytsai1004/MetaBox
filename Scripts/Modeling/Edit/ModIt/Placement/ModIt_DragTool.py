import maya.cmds as cmds
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

from .. import ModIt_Global
import importlib
importlib.reload(ModIt_Global)

##_______________________________________________ GLOBALS VAR
sampleFileChoice = []
PreferencePath = ModIt_Global.PreferencePath
##______________________________ PLACE TOOL


def goPress(fileMA): #_________________________________________LA DEF QUI LANCE LE PLACE TOOL
    SaveSize_pref = json.load(open(PreferencePath + 'MultiSize.json', "r"))
    MULTISIZEVALUE = (SaveSize_pref['MULTISIZEVALUE'])

    sampleMesh = str(fileMA) #GET THE ASSET CLICK FULL PATH MA


    global selAnyList
    selAnyList = cmds.ls(sl=1,fl=1,l=1)
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
    cmds.CreateEmptyGroup()
    cmds.rename(sampleName + '_Ctrl') ##__________________________________________CREATION DU GROUPE QUI CONTIENT LE MESH
    checkName=cmds.ls(sl=True)
    ##__________________________________________IMPORT ASSET
    #____ Alembic
    #command = 'AbcImport -mode import -reparent '+ checkName[0] + ' ' + '"' + sampleMesh + '"'
    #newNode = mel.eval(command)
    #print ("command = " + str(command))

    # ____ .MA
    before = set(cmds.ls(assemblies=True, l= True))

    cmds.file(sampleMesh, i=True)

    after = set(cmds.ls(assemblies=True, l= True))
    imported = after.difference(before)
    cmds.select(imported)

    cmds.parent(imported, checkName[0])
    cmds.select(checkName[0])


    cmds.setAttr(checkName[0] + ".scaleX", MULTISIZEVALUE)
    cmds.setAttr(checkName[0] + ".scaleY", MULTISIZEVALUE)
    cmds.setAttr(checkName[0] + ".scaleZ", MULTISIZEVALUE)

    cmds.makeIdentity(apply=True)

    cmds.xform(ws=1, a=1 ,piv =[0, 0, 0])
    cmds.pickWalk(d="down")
    tempSel = cmds.ls(sl=True,type='transform',l=True)
    folderName = (sampleMesh.split('/')[-2])

    cmds.select(tempSel)

    
    tempSel = cmds.ls(sl=True,type='transform',l=True)
    cmds.select(tempSel[0])
    sampleFileChoice = checkName
    cmds.setAttr((sampleFileChoice[0]+'.scaleX'),0)
    cmds.setAttr((sampleFileChoice[0]+'.scaleY'),0)
    cmds.setAttr((sampleFileChoice[0]+'.scaleZ'),0)
    
    runIt()

    if sampleFileChoice:
        if cmds.objExists(sampleFileChoice[0]):
            childNode =   cmds.listRelatives(sampleFileChoice[0],type='transform',ad=True,f=True)
            for c in childNode:
                if not cmds.attributeQuery('targetGeo', node = c, ex=True ):
                    cmds.addAttr(c, ln='targetGeo',  dt= 'string')
                    cmds.setAttr((c+'.targetGeo'),e=True, keyable=True)

def runIt():
    global ctx
    ctx = 'Click2dTo3dCtx'
    # Delete dragger context if it already exists
    if cmds.draggerContext(ctx, exists=True):
        cmds.deleteUI(ctx)
    # Create dragger context and set it to the active tool
    cmds.draggerContext(ctx, pressCommand = onPressPlace, rc = offPressPlace, dragCommand = onDragPlace, fnz = finishTool, name=ctx, cursor='crossHair',undoMode='step')
    cmds.setToolTo(ctx)

##______________________________ PLACE TOOL - DRAGGER VAR
def getPosition(SX, SY):
    global betweenListShape
    global checkVisList

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

    cameraTrans = cmds.listRelatives(camPath, type='transform', p=True)
    cameraPosition = cmds.xform(cameraTrans, q=1, ws=1, rp=1)

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
        shapesList = cmds.listRelatives(betweenListShape, ad=True, f=True)
        shapesNodestOnly = cmds.ls(shapesList, type='shape', l=1, fl=1)
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


    return finalX, finalY, finalZ, finalMesh, hitFace
    cmds.refresh(cv=True, f=True)

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

    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
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
            cmds.select(newChoice)

        else:
            newNodeA = []
            randomNumber = random.randint(0, (len(combineSelPool) - 1))
            newChoiceA = combineSelPool[randomNumber]

            if meshTypeState == 2:
                # only instance mesh not tranform node
                newNodeA = cmds.duplicate(newChoiceA, rr=True)
                cmds.select(newNodeA)
                cmds.pickWalk(d='Down')
                meshNode = cmds.ls(sl=True, l=True)
                cmds.select(newChoiceA)
                cmds.pickWalk(d='Down')
                cmds.instance()
                cmds.delete(meshNode)
                intNode = cmds.ls(sl=True, l=True)
                cmds.parent(intNode, newNodeA)
                cmds.rename(meshNode[0].split('|')[-1])
                cmds.pickWalk(d='up')
            else:
                newNodeA = cmds.duplicate(newChoiceA, rr=True)
            cmds.select(newNodeA)

        tempSel = cmds.ls(sl=1, type='transform')


        wx, wy, wz, hitmesh, hitFace = getPosition(screenX, screenY)
        lastSnapMesh = hitmesh
        cmds.setAttr((tempSel[0] + '.translateX'), wx)
        cmds.setAttr((tempSel[0] + '.translateY'), wy)
        cmds.setAttr((tempSel[0] + '.translateZ'), wz)
        hitFaceName = (hitmesh + '.f[' + str(hitFace) + ']')

        if checkSnapState == 1:
            rx, ry, rz = checkFaceAngle(hitFaceName)
            cmds.setAttr((tempSel[0] + '.rotateX'), rx)
            cmds.setAttr((tempSel[0] + '.rotateY'), ry)
            cmds.setAttr((tempSel[0] + '.rotateZ'), rz)

        cmds.setAttr((tempSel[0] + '.scaleX'), 1)
        cmds.setAttr((tempSel[0] + '.scaleY'), 1)
        cmds.setAttr((tempSel[0] + '.scaleZ'), 1)


        ##__________________________# Initialement Valeur de Slider
        currentScaleX = 1.0
        currnetRotY = 0.0
        currentDepth = 0.0
        randomY = 0.0
        silderScale = 1.0
        randomScale = 0.0
        randomSwing = 0.0

        cmds.pickWalk(tempSel[0], direction='down')
        meshNode = cmds.ls(sl=1, type='transform', l=1)
        # meshNode = cmds.listRelatives(tempSel[0],c=True, typ = 'transform',f=True)
        SycList.append(meshNode[0])
        cmds.setAttr((meshNode[0] + '.scaleX'), currentScaleX)
        cmds.setAttr((meshNode[0] + '.scaleY'), currentScaleX)
        cmds.setAttr((meshNode[0] + '.scaleZ'), currentScaleX)

        currentScaleRecord = currentScaleX
        cmds.setAttr((meshNode[0] + '.rotateY'), currnetRotY)
        currentRotRecord = currnetRotY
        cmds.setAttr((meshNode[0] + '.translateY'), currentDepth)

        if (randomY > 0):
            randomNumber = random.uniform(0, randomY)
            cmds.setAttr((meshNode[0] + '.rotateY'), int(randomNumber))
            currentRotRecord = int(randomNumber)

        if (randomScale > 0):
            randomNumber = random.uniform((-1 * randomScale), randomScale)
            cmds.setAttr((meshNode[0] + '.scaleX'), (randomNumber + silderScale))
            cmds.setAttr((meshNode[0] + '.scaleY'), (randomNumber + silderScale))
            cmds.setAttr((meshNode[0] + '.scaleZ'), (randomNumber + silderScale))
            currentScaleRecord = (randomNumber + silderScale)

        if randomSwing > 0:
            offsetNode = cmds.listRelatives(meshNode[0], type='transform', p=True)
            randomNumberX = random.uniform(-1 * randomSwing, randomSwing)
            cmds.setAttr((offsetNode[0] + '.rotateX'), int(randomNumberX))
            randomNumberZ = random.uniform(-1 * randomSwing, randomSwing)
            cmds.setAttr((offsetNode[0] + '.rotateZ'), int(randomNumberZ))

        cmds.select(tempSel)


        #######################################################################

        transNode = cmds.listRelatives(lastSnapMesh, type='transform', p=True, f=True)
        cmds.setAttr((meshNode[0] + '.targetGeo'), transNode[0], type="string")

    #########################################################################
    except:
        pass

    cmds.refresh(cv=True, f=True)

def offPressPlace():
    global tempCmd
    global betweenList
    global betweenList3DPos
    betweenList3DPos = []

    for e in betweenList:
        attList = ['translateX','translateY','translateZ']
        attListRecord =['ptX','ptY','ptZ']
        for a in range(len(attList)):
            attListRecord[a] = cmds.getAttr(e +'.'+attList[a])
        pos3D = (attListRecord[0],attListRecord[1],attListRecord[2])
        betweenList3DPos.append(pos3D )
    cmds.refresh(cv=True,f=True)
    deSelect()

    #Get Active Sel Mode
    activeSelMode = cmds.selectMode(q=True, root=True)
    if activeSelMode == False:
        cmds.selectMode(root=True)

    else:
        cmds.selectMode(object=True)



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
    lastPanelActive = cmds.getPanel(underPointer=True)
    currentSX = 0
    currnetSY = 0
    goStrightLine = 0.0
    randomY = 0.0
    meshTypeState = 1
    selSample = []
    selSample = cmds.ls(sl=True,fl=True,l=True)
    headMesh = selSample[0]
    


    
    if len(selSample)>0:
        if (goStrightLine > 0):
            if betweenFirstTime == 1:
                #need to give one sample to first position
                attList = ['translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ']
                attListRecord =['ptX','ptY','ptZ','prX','prY','prZ','psX','psY','psZ']
                for a in range(len(attList)):
                    attListRecord[a] = cmds.getAttr(selSample[0]+'.'+attList[a])
                #pick up sample if multiMode
                if len(combineSelPool)>1:
                        randomNumber = random.randint(0,(len(combineSelPool)-1))
                        cmds.select(combineSelPool[randomNumber])
                else:
                    cmds.select(selSample[0])
                keepItMesh = cmds.ls(sl=1,fl=1)
                #make a copy
                if meshTypeState == 2:
                    #only instance mesh not tranform node
                    newKeepNode = cmds.duplicate(keepItMesh[0],rr=True)
                    cmds.select(newKeepNode)
                    cmds.pickWalk(d='Down')
                    meshKeepNode = cmds.ls(sl=True,l=True)
                    cmds.select(keepItMesh[0])
                    cmds.pickWalk(d='Down')
                    cmds.instance()
                    cmds.delete(meshKeepNode)
                    intKeepNode = cmds.ls(sl=True,l=True)
                    cmds.parent(intKeepNode,newKeepNode)
                    intKeepNode = cmds.ls(sl=True,l=True)
                    cmds.rename(meshKeepNode[0].split('|')[-1])
                    cmds.pickWalk(d='up')
                else:
                    cmds.duplicate(keepItMesh[0])
                #restore position
                checkKeepNode = cmds.ls(sl=1,fl=1)
                for b in range(len(attList)):
                    cmds.setAttr((checkKeepNode[0]+'.'+attList[b]),attListRecord[b])
                checkKeepNodeChild = cmds.listRelatives(checkKeepNode[0],c=True, typ = 'transform',f=True)
                SycList.append(checkKeepNodeChild[0])

                meshNodeA = cmds.listRelatives(selSample[0],c=True, typ = 'transform',f=True)

                SycList.append(meshNodeA[0])
                if randomY > 0:
                    randomNumber = random.uniform(0,randomY)
                    cmds.setAttr((meshNodeA[0]+'.rotateY'),int(randomNumber))

                tailMesh = checkKeepNode[0]
                betweenList = []
                betweenListShape = []
                #get in between element
                for i in range(int(goStrightLine)):
                    if len(combineSelPool)>1:
                        randomNumber = random.randint(0,(len(combineSelPool)-1))
                        cmds.select(combineSelPool[randomNumber])
                    else:
                        cmds.select(selSample[0])

                    newBetweenDulpi = cmds.ls(sl=True,fl=True,l=True)
                    if meshTypeState == 2:
                        #only instance mesh not tranform node
                        newNode = cmds.duplicate(newBetweenDulpi[0],rr=True)
                        cmds.select(newNode)
                        cmds.pickWalk(d='Down')
                        meshNode = cmds.ls(sl=True,l=True)
                        cmds.select(newBetweenDulpi[0])
                        cmds.pickWalk(d='Down')
                        cmds.instance()
                        cmds.delete(meshNode)
                        intNode = cmds.ls(sl=True,l=True)
                        cmds.parent(intNode,newNode)
                        intNode = cmds.ls(sl=True,l=True)
                        cmds.rename(meshNode[0].split('|')[-1])
                        cmds.pickWalk(d='up')
                    else:
                        cmds.duplicate(newBetweenDulpi[0])

                    selBetween = cmds.ls(sl=True,fl=True,l=True)
                    meshNodeB = cmds.listRelatives(selBetween[0],c=True, typ = 'transform',f=True)
                    
                    silderScale = 1.0
                    randomScale = 0.0
                    randomSwing = 0.0
                    
                    if (randomScale > 0):
                        randomNumber = random.uniform((-1*randomScale),randomScale)
                        newScale = (randomNumber+silderScale)
                        #bug calucation done but update not fast enough to show, evalDeferred works but not great
                        cmdx = 'cmds.setAttr("' + meshNodeB[0] +'.scaleX",' + str(newScale) + ')'
                        cmds.evalDeferred(cmdx)
                        cmdy = 'cmds.setAttr("' + meshNodeB[0] +'.scaleY",' + str(newScale) + ')'
                        cmds.evalDeferred(cmdy)
                        cmdz = 'cmds.setAttr("' + meshNodeB[0] +'.scaleZ",' + str(newScale) + ')'
                        cmds.evalDeferred(cmdz)


                    if randomY > 0:
                        randomNumber = random.uniform(0,randomY)
                        cmds.setAttr((meshNodeB[0]+'.rotateY'),int(randomNumber))

                    if randomSwing > 0:
                        offsetNode = cmds.listRelatives(meshNodeB[0],type='transform',p=True)
                        randomNumberX = random.uniform(-1*randomSwing,randomSwing)
                        cmds.setAttr((offsetNode[0]+'.rotateX'),int(randomNumberX))
                        randomNumberZ = random.uniform(-1*randomSwing,randomSwing)
                        cmds.setAttr((offsetNode[0]+'.rotateZ'),int(randomNumberZ))

                    SycList.append(meshNodeB[0])
                    betweenShape = cmds.listRelatives(selBetween[0], fullPath=True ,c=True)
                    betweenList.append(selBetween[0])
                    betweenListShape.append(betweenShape[0])
                    betweenFirstTime = 0
        else:
            betweenListShape = []

        modifiers = cmds.getModifiers()
        SycList = list(set(SycList))
        if (modifiers == 4):
            #print 'ctrl Press'

            vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
            distanceA = (vpX - screenX)
            rotateCheck = (distanceA)
            rotateRun = currentRotRecord + rotateCheck

            if rotateRun > 360 :
                rotateRun = 360
            elif rotateRun < -360 :
                rotateRun = -360
            getR = int(rotateRun / 15)*15
            if rotateRun != getR:
                rotateRun = getR
            #cmds.floatSliderGrp( 'meshRotSlide', e=1 ,v = rotateRun )
            cmds.setAttr((selSample[0]+'.rotateAxisY'),rotateRun)
            #cmds.refresh(f=True)

        elif(modifiers == 1):

            #print 'shift selSample'
            vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
            distanceB = vpX - screenX
            scaleCheck = distanceB / 100
            scaleRun = currentScaleRecord + scaleCheck
            if scaleRun > 5:
                scaleRun = 5
            elif scaleRun < 0:
                scaleRun = 0.1

            #cmds.floatSliderGrp( 'meshScaleSlide', e=1 ,v = scaleRun )
            if len(SycList)>0:
                    cmds.setAttr((selSample[0] + '.scaleX'),scaleRun)
                    cmds.setAttr((selSample[0] + '.scaleY'),scaleRun)
                    cmds.setAttr((selSample[0] + '.scaleZ'),scaleRun)
            #cmds.refresh(cv=True,f=True)
        else:
            vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
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

            cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
            cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)

            checkHit = 0
            finalMesh = []
            finalX = 0
            finalY = 0
            finalZ = 0
            shortDistance = 10000000000
            distanceBetween = 1000000000

            checkList=[]
            meshNode = cmds.listRelatives(selSample, fullPath=True ,c=True)
            myShape = cmds.listRelatives(meshNode, shapes=True,f=True)

            shapesList = cmds.listRelatives(betweenListShape,ad=True,f=True)
            shapesNodestOnly =  cmds.ls(shapesList,type='shape',l=1,fl=1)


            if myShape == None:#gpu
                checkList =  list(set(checkVisList))
            else:
                checkStackMode  = 1
                if checkStackMode == 1:
                    checkList =  list(set(checkVisList)-set(myShape)-set(shapesNodestOnly))
                else:
                    checkList = screenVisPoly()
                    checkList.remove(myShape[0])
                    SycListShape = cmds.listRelatives(SycList, shapes=True,f=True)
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
                            cmds.setAttr((selSample[0] + '.rotateX'), rx)
                            cmds.setAttr((selSample[0] + '.rotateY'), ry)
                            cmds.setAttr((selSample[0] + '.rotateZ'), rz)
                        finalX = x
                        finalY = y
                        finalZ = z
                    lastSnapMesh = finalMesh
                    #######################################################################
                    childNode =   cmds.listRelatives(selSample[0],type='transform',ad=True,f=True)
                    transNode=cmds.listRelatives(lastSnapMesh,type='transform',p=True,f=True)
                    for c in childNode:
                        cmds.setAttr((c + '.targetGeo'),transNode[0],type="string")
                   #########################################################################
                    cmds.setAttr((selSample[0] + '.translateX'), finalX)
                    cmds.setAttr((selSample[0] + '.translateY'), finalY)
                    cmds.setAttr((selSample[0] + '.translateZ'), finalZ)
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
                        cvList = (cmds.polyInfo(hitFaceName , fv=True )[0]).split(':')[-1].split('    ')
                        cvList = [x for x in cvList if x.strip()]
                        mostCloseCVPoint = []
                        for v in cvList:
                            checkNumber = ''.join([n for n in v.split('|')[-1] if n.isdigit()])
                            if len(checkNumber) > 0:
                                cvPoint = (finalMesh + '.vtx[' + str(checkNumber) +']')
                                cvPosition = cmds.pointPosition(cvPoint)
                                checkCVDistance = math.sqrt( ((float(cvPosition[0]) - finalX)**2)  + ((float(cvPosition[1]) - finalY)**2) + ((float(cvPosition[2]) - finalZ)**2))
                                if checkCVDistance < shortDistanceCheck:
                                    shortDistanceCheck = checkCVDistance
                                    cvX = float(cvPosition[0])
                                    cvY = float(cvPosition[1])
                                    cvZ = float(cvPosition[2])
                                    mostCloseCVPoint = cvPoint
                        if shortDistanceCheck < mostCloseDist:
                            cmds.setAttr((selSample[0] + '.translateX'), cvX)
                            cmds.setAttr((selSample[0] + '.translateY'), cvY)
                            cmds.setAttr((selSample[0] + '.translateZ'), cvZ)
                            #get average normal angle from suround faces
                            if checkSnapState == 1:
                                rX,rY,rZ = avgVertexNormalAngle(cvPoint)
                                cmds.setAttr(selSample[0]+'.rotateX', rX)
                                cmds.setAttr(selSample[0]+'.rotateY', rY)
                                cmds.setAttr(selSample[0]+'.rotateZ', rZ)

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
                            childNode =   cmds.listRelatives(betweenList[a],type='transform',ad=True,f=True)
                            transNode=cmds.listRelatives(hitmesh,type='transform',p=True,f=True)
                            for c in childNode:
                                cmds.setAttr((c + '.targetGeo'),transNode[0],type="string")
                            #########################################################################
                            cmds.setAttr((betweenList[a] + '.translateX'), wx)
                            cmds.setAttr((betweenList[a] + '.translateY'), wy)
                            cmds.setAttr((betweenList[a] + '.translateZ'), wz)
                            if checkSnapState == 1:
                                hitFaceName = (hitmesh + '.f[' + str(hitFace) +']')
                                rx, ry, rz = checkFaceAngle(hitFaceName)
                                cmds.setAttr((betweenList[a] + '.rotateX'), rx)
                                cmds.setAttr((betweenList[a] + '.rotateY'), ry)
                                cmds.setAttr((betweenList[a] + '.rotateZ'), rz)

        cmds.select(selSample[0])
        cmds.refresh(cv=True,f=True)

def finishTool():
    restoreSelVis()
    #cmds.MoveTool()
    cmds.select(cl=True)

##______________________________ PLACE TOOL - HELPERS
def restoreSelVis():
    cmds.modelEditor('modelPanel1', e=True, sel=True)
    cmds.modelEditor('modelPanel2', e=True, sel=True)
    cmds.modelEditor('modelPanel3', e=True, sel=True)
    cmds.modelEditor('modelPanel4', e=True, sel=True)

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
    shapesOnScreen = cmds.listRelatives(fromScreen, shapes=True,f=True)
    meshList = cmds.ls(type='mesh',l=True)#only polygon
    if len(meshList)>0 and shapesOnScreen is not None:
        commonList = list(set(meshList) & set(shapesOnScreen))
        return commonList
    else:
        commonList = []
        return commonList

def deSelect():
    obj_shape = cmds.listRelatives(parent=True, f=True)
    obj = cmds.listRelatives(obj_shape,parent=True, f=True)
    cmds.select(obj)
    cmds.selectMode(leaf=True)
    cmd = "changeSelectMode -object;"
    mel.eval(cmd)
    cmds.select(clear=True)

def checkFaceAngle(faceName):
    shapeNode = cmds.listRelatives(faceName, fullPath=True , parent=True )
    transformNode = cmds.listRelatives(shapeNode[0], fullPath=True , parent=True )
    obj_matrix = Matrix(cmds.xform(transformNode, query=True, worldSpace=True, matrix=True))
    face_normals_text = cmds.polyInfo(faceName, faceNormals=True)[0]
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
    shapesOnScreen = cmds.listRelatives(fromScreen, shapes=True,f=True)
    meshList = cmds.ls(type='mesh',l=True)#only polygon
    if len(meshList)>0 and shapesOnScreen is not None:
        commonList = list(set(meshList) & set(shapesOnScreen))
        return commonList
    else:
        commonList = []
        return commonList


