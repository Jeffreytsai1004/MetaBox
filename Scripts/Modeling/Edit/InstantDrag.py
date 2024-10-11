#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from maya.OpenMaya import MGlobal
import math
import maya.api.OpenMaya as oma
import re



def run():
    cleanList = ('instPicker','instRot')
    for c in cleanList:
        if mc.objExists(c):
            mc.delete(c)
    global ctx
    ctx = 'Click2dTo3dCtx'
    global storeHitFace
    storeHitFace =''
    if mc.draggerContext(ctx, exists=True):
        mc.deleteUI(ctx)
    mc.draggerContext(ctx, pressCommand = instDragPick, rc = instDragClean, dragCommand = instDragMove, name=ctx, cursor='crossHair',undoMode='step')
    mc.setToolTo(ctx)



def instDragPick():
    preSelect = mc.ls(sl=1,fl=1,l=1)
    global ctx
    global screenX,screenY
    global checkScreenMeshList
    global storeCameraPosition
    global storeMeshNode
    global parentDir
    global targetMeshName
    global instDul
    global storeHitFace
    global cameraFarClip
    global storeRotCount
    global lockCount
    global edgeAlignRecord
    edgeAlignRecord = 0
    storeRotCount = 0
    vpX, vpY, _ = mc.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    pos = om.MPoint()
    dir = om.MVector()
    omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = mc.listRelatives(camPath,type='transform',p=True)
    cameraFarClip = mc.getAttr(cameraTrans[0]+'.farClipPlane')
    storeCameraPosition = mc.xform(cameraTrans,q=1,ws=1,rp=1)
    ##########################################################
    storeMeshNode=[]
    instDul = 0
    checkHit = 0
    finalMesh = []
    shortDistance = cameraFarClip
    distanceBetween = cameraFarClip
    hitpoint = om.MFloatPoint()
    hitFace = om.MScriptUtil()
    hitFace.createFromInt(0)
    hitFacePtr = hitFace.asIntPtr()
    ##########################################################
    checkScreenMeshList = screenVisPoly()
    for mesh in checkScreenMeshList:
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
        cameraFarClip,
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
            distanceBetween = math.sqrt( ((float(storeCameraPosition[0]) - x)**2)  + ((float(storeCameraPosition[1]) - y)**2) + ((float(storeCameraPosition[2]) - z)**2))
            if distanceBetween < shortDistance:
                shortDistance = distanceBetween
                finalMesh = mesh
    if preSelect:
        checkShape = mc.listRelatives(preSelect, shapes=True, fullPath=True)
        finalMesh = checkShape
    
    if len(finalMesh) > 0:
        #preSelect = mc.ls(sl=1,fl=1,l=1)
        #checkShape = mc.listRelatives(preSelect, shapes=True, fullPath=True)
        #finalMesh = checkShape
        storeMeshNode=mc.listRelatives(finalMesh,type='transform',p=True,f=True)
        shapeNode = mc.listRelatives(storeMeshNode[0], fullPath=True,ad=True )
        parentDir = '|'.join(storeMeshNode[0].split('|')[0:-1])
        targetMeshName = storeMeshNode[0].split('|')[-1]
        #move pivot to bbox base
        rotSave = mc.getAttr(targetMeshName + '.rotate')
        posSave = mc.xform(targetMeshName, q=True, ws=True, piv=True)[:3]
        mc.setAttr(targetMeshName + '.rotate',0,0,0)
        bbox = mc.exactWorldBoundingBox(targetMeshName)
        base_position = bbox[1]
        mc.move(posSave[0], base_position, posSave[2] , (targetMeshName+ '.scalePivot'), (targetMeshName + '.rotatePivot'), ws=True)
        
        ##########################################################
        mc.group(empty=1,n ='instPicker')
        mc.duplicate('instPicker')
        mc.rename('instRot')
        mc.parent('instRot','instPicker')
        mc.select('instPicker',storeMeshNode[0])
        mc.matchTransform(pos=1,rot=1)
        mc.parent(storeMeshNode[0],'instRot')
        mc.select('instPicker|instRot|'+targetMeshName)
        mc.setAttr('instPicker.rotate',rotSave[0][0],rotSave[0][1],rotSave[0][2])
        mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        mc.delete(constructionHistory=True)
        ##########################################################
        for s in shapeNode:
            if s in checkScreenMeshList:
                checkScreenMeshList.remove(s)
        currentRoteY = mc.getAttr('instRot.rotateY')
        lockCount = int(currentRoteY / 15)*15

def instDragClean():
    global parentDir
    global targetMeshName
    global instDul
    global edgeAlignRecord
    edgeAlignRecord = 0
    if mc.objExists('instPicker'):
        if len(parentDir) == 0:
            mc.select('instPicker|instRot|'+targetMeshName)
            mc.parent(w=1)
        else:
            mc.parent(('|instPicker|instRot|'+targetMeshName),(parentDir))

    cleanList = ('instPicker','instRot')
    for c in cleanList:
        if mc.objExists(c):
            mc.delete(c)
    instDul = 0
    mc.select(cl=1)
    
def instDragMove():
    global screenX
    global storeMeshNode
    global storeHitFace
    global cameraFarClip
    global storeRotCount
    global storeRotCount
    global lockCount
    global edgeAlignRecord
    if storeMeshNode:
        if mc.objExists('instPicker'):
            global ctx
            global screenX,screenY
            global storeCameraPosition
            global checkScreenMeshList
            global parentDir
            global targetMeshName
            global instDul
            
            modifiers = mc.getModifiers()
            vpX, vpY, _ = mc.draggerContext(ctx, query=True, dragPoint=True)
            
            if (modifiers == 4):
                #press Ctrl ----> rotate
                if screenX > vpX:
                    lockCount = lockCount - 2
                else: 
                    lockCount = lockCount + 2
                screenX = vpX
                if lockCount < -360:
                    lockCount = -360
                elif lockCount > 360:
                    lockCount = 360
                
                getX = int(lockCount / 15)*15
                
                if storeRotCount != getX:
                    storeRotCount = getX
                mc.setAttr('instRot.rotateY',storeRotCount)
                mc.refresh(cv=True,f=True)
            elif(modifiers == 5):
                #press Shift + Ctrl
                if edgeAlignRecord == 0:
                    alignEdge()
                    edgeAlignRecord = 1
                    mc.refresh(cv=True,f=True)
            elif(modifiers == 1):
                #press Shift -----> dulpicate current mesh
                if instDul == 0:
                    newD = mc.duplicate(('|instPicker|instRot|'+targetMeshName),rr=1)
                    if len(parentDir) == 0:
                        mc.select('instPicker|instRot|'+targetMeshName)
                        mc.parent(w=1)
                    else:
                        mc.parent(('|instPicker|instRot|'+targetMeshName),(parentDir))
                    targetMeshName = newD[0]
                    mc.select(targetMeshName)
                    instDul = 1
                mc.refresh(cv=True,f=True)
            else:
                pos = om.MPoint()
                dir = om.MVector()
                omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
                pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
                ############################################################
                checkHit = 0
                finalMesh = ''
                hitFaceName = ''
                finalX = 0
                finalY = 0
                finalZ = 0
                shortDistance = cameraFarClip
                distanceBetween = cameraFarClip
                hitpoint = om.MFloatPoint()
                hitFace = om.MScriptUtil()
                hitFace.createFromInt(0)
                hitFacePtr = hitFace.asIntPtr()
                ############################################################
                for mesh in checkScreenMeshList:
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
                    cameraFarClip,
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
                        distanceBetween = math.sqrt( ((float(storeCameraPosition[0]) - x)**2)  + ((float(storeCameraPosition[1]) - y)**2) + ((float(storeCameraPosition[2]) - z)**2))
                        if distanceBetween < shortDistance:
                            shortDistance = distanceBetween
                            finalMesh = mesh

                if finalMesh:
                    selectionList = om.MSelectionList()
                    selectionList.add(finalMesh)
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
                    cameraFarClip,
                    False,
                    None,
                    hitpoint,
                    None,
                    hitFacePtr,
                    None,
                    None,
                    None)
                    finalX = hitpoint.x
                    finalY = hitpoint.y
                    finalZ = hitpoint.z
                    hitFace = om.MScriptUtil(hitFacePtr).asInt()
                    hitFaceName = (finalMesh + '.f[' + str(hitFace) +']')
                    instDul = 0
                    mc.setAttr('instPicker.translate', finalX,finalY,finalZ)
                    if storeHitFace != hitFaceName:
                        rx, ry, rz = checkFaceAngle(hitFaceName)
                        mc.setAttr('instPicker.rotate', rx,ry,rz)
                        storeHitFace = hitFaceName
                    mc.refresh(cv=True,f=True)


def screenVisPoly():
    commonList= []
    view = omui.M3dView.active3dView()
    om.MGlobal.selectFromScreen(0, 0, view.portWidth(), view.portHeight(), om.MGlobal.kReplaceList)
    objects = om.MSelectionList()
    sel = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(objects)
    om.MGlobal.setActiveSelectionList(sel, om.MGlobal.kReplaceList)
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

        
def checkFaceAngle(faceName):
    shapeNode = mc.listRelatives(faceName, fullPath=True , parent=True )
    transformNode = mc.listRelatives(shapeNode[0], fullPath=True , parent=True )
    obj_matrix = oma.MMatrix(mc.xform(transformNode, query=True, worldSpace=True, matrix=True))
    face_normals_text = mc.polyInfo(faceName, faceNormals=True)[0]
    face_normals = [float(digit) for digit in re.findall(r'-?\d*\.\d*', face_normals_text)]
    v = oma.MVector(face_normals) * obj_matrix
    upvector = oma.MVector (0,1,0)
    getHitNormal = v
    quat = oma.MQuaternion(upvector, getHitNormal)
    quatAsEuler = oma.MEulerRotation()
    quatAsEuler = quat.asEulerRotation()
    rx, ry, rz = math.degrees(quatAsEuler.x), math.degrees(quatAsEuler.y), math.degrees(quatAsEuler.z)
    return rx, ry, rz

def alignEdge():
    mesh=mc.ls(sl=1,fl=1)
    if len(mesh) == 1:
        checkLongName = mc.ls(mesh[0],l=1)
        parentNode = checkLongName[0].split('|')
        if len(parentNode) > 2:
            outParent = ''
            outParent = '|'.join(parentNode[1:-1])
            mc.parent(mesh[0],w=1)
        cleanList = ('sampleCurv*','sampleMes*','rotationPlan*')
        for c in cleanList:
            if mc.objExists(c):
                mc.delete(c)
        gface, gHitp,cEdge,cEdgePos = getClosestEdge()
        mc.select(cEdge)
        checkCVList=mc.ls( mc.polyListComponentConversion (cEdge,fe=True,tv=True),flatten=True)
        mx,my,mz = mc.pointPosition(checkCVList[0],w=1)
        mc.polyPlane(w=1, h=1, sx=1, sy=1, ax=(0,1,0), cuv=2, ch=0, n='rotationPlane')
        mc.polyCreateFacet( p=[(mx, my, mz),(cEdgePos[0], cEdgePos[1], cEdgePos[2]),(gHitp[0], gHitp[1], gHitp[2])] )
        mc.rename('sampleMesh')
        mc.select("rotationPlane.vtx[0:2]", "sampleMesh.vtx[0:2]")
        CMD = 'snap3PointsTo3Points(0);'
        mel.eval(CMD)
        mc.parent(mesh[0],'rotationPlane')
        axes = ["X", "Y", "Z"]
        for a in axes:
            val = mc.getAttr( mesh[0] + ".rotate" + a)
            valTmp = ''
            if val > 0:
                valTmp = val + 45
            else:
                valTmp = val - 45
            valNew = int (valTmp/90)
            mc.setAttr(( mesh[0] + ".rotate" + a), (valNew*90))

        mc.move(gHitp[0], gHitp[1], gHitp[2], mesh[0], rpr=True,wd=True)
        mc.select(mesh[0])
        mc.parent(w=1)
        if len(parentNode) > 2:
            mc.parent(mesh[0],outParent)
        for c in cleanList:
            if mc.objExists(c):
                mc.delete(c)



def getClosestEdge():
    mayaMesh = mc.ls(sl=1,fl=1)
    gFace = ''
    gHitP = ''
    gFace,gHitP = getClosestMeshHit(mayaMesh[0])
    listF2E=mc.ls( mc.polyListComponentConversion (gFace,ff=True,te=True),flatten=True)
    cEdge = ''
    smallestDist = 1000000
    cEdgePos = []
    for l in listF2E:
        mc.select(l)
        mc.polyToCurve(form=2, degree=1, conformToSmoothMeshPreview=1)
        sampleCurve = mc.ls(sl=1)
        selectionList = om.MSelectionList()
        selectionList.add(sampleCurve[0])
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        omCurveOut = om.MFnNurbsCurve(dagPath)
        pointInSpace = om.MPoint(gHitP[0],gHitP[1],gHitP[2])
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        getDist = math.sqrt( ((closestPoint[0] - gHitP[0])**2)  + ((closestPoint[1]- gHitP[1])**2) + ((closestPoint[2] - gHitP[2])**2))
        if getDist < smallestDist:
            smallestDist = getDist
            cEdge = l
            cEdgePos = [closestPoint[0],closestPoint[1],closestPoint[2]]
        mc.delete(sampleCurve)
    mc.select(cEdge)
    return(gFace,gHitP,cEdge,cEdgePos)





def getClosestMeshHit(mayaMesh):
    myShape = mc.listRelatives(mayaMesh, f=True,ad =True)
    checkList = screenVisPoly()
    removeList = list(set(checkList) - set(myShape))
    checkList = removeList
    meshPos = mc.xform(mayaMesh,q=1, ws=1, a=1, piv=1)
    posXXX = [meshPos[0],meshPos[1],meshPos[2]]
    shortDistanceCheck = 10000
    resultFace = []
    resultCV =[]
    resultHitPoint = []
    for c in checkList:
        transNode = mc.listRelatives(c, p=True,f=True)
        getFaceDist,getFace,getHitPoint  = getClosestPointOnFace(transNode[0],posXXX)
        #print((getCV, getFaceDist, getFace)
        if getFaceDist < shortDistanceCheck:
            shortDistanceCheck = getFaceDist
            resultFace = getFace
            resultHitPoint = getHitPoint
    return (resultFace,resultHitPoint)



def getClosestPointOnFace(mayaMesh,pos=[0,0,0]):
    mVector = oma.MVector(pos)#using MVector type to represent position
    selectionList = oma.MSelectionList()
    selectionList.add(mayaMesh)
    dPath= selectionList.getDagPath(0)
    mMesh=oma.MFnMesh(dPath)
    ID = mMesh.getClosestPoint(oma.MPoint(mVector),space=oma.MSpace.kWorld)[1] #getting closest face ID
    closestPoint= mMesh.getClosestPoint(oma.MPoint(mVector),space=oma.MSpace.kWorld)[0]
    cpx = closestPoint[0]
    cpy = closestPoint[1]
    cpz = closestPoint[2]
    hitPointPosition = [cpx,cpy,cpz]
    hitFaceName = (mayaMesh+'.f['+str(ID)+']')
    getFaceDist = math.sqrt( ((pos[0] - cpx)**2)  + ((pos[1]- cpy)**2) + ((pos[2] - cpz)**2))
    return (getFaceDist, hitFaceName,hitPointPosition)


def getPolyFaceCenter(faceName):
    meshFaceName = faceName.split('.')[0]
    findVtx = mc.polyInfo(faceName, fv=1)
    getNumber = []
    checkNumber = ((findVtx[0].split(':')[1]).split('\n')[0]).split(' ')
    for c in checkNumber:
        findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
        if findNumber:
            getNumber.append(findNumber)
    centerX = 0
    centerY = 0
    centerZ = 0
    for g in getNumber:
        x,y,z = mc.pointPosition((meshFaceName + '.vtx['+g + ']'),w=1)
        centerX = centerX + x
        centerY = centerY + y
        centerZ = centerZ + z

    centerX = centerX/len(getNumber)
    centerY = centerY/len(getNumber)
    centerZ = centerZ/len(getNumber)
    return centerX,centerY,centerZ