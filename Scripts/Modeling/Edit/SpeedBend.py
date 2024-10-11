#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import math
import re
import maya.mel as mel
from collections import defaultdict

def sBFillHole():
    checkHole = cmds.filterExpand(ex=1, sm=(34))
    checkHoleEdge = cmds.ls(cmds.polyListComponentConversion(checkHole, te=1),fl=1)
    cmds.polySelectConstraint(mode=3, type=0x8000, where=1)
    selected_edge = cmds.ls(sl=1,fl=1)
    cmds.polySelectConstraint(disable=True)
    foundHole = list(set(selected_edge)&set(checkHoleEdge))
    if foundHole:
        cmds.select(foundHole)
        cmds.FillHole()
        cmds.ConvertSelectionToFaces()
        cmds.select(checkHole,add=1)
    else:
        cmds.select(checkHole)

def isFlat(sel):
    normals = defaultdict(list)
    for face in sel:
        normal = cmds.polyInfo(face, faceNormals=True)[0].split()[2:]
        normal = [float(x) for x in normal]
        normals[tuple(normal)].append(face)
    most_common_normal = max(normals, key=lambda x: len(normals[x]))
    facesFlat = 1
    for normal, faces in normals.items():
        if normal == most_common_normal:
            continue
        dot = sum([a*b for a,b in zip(normal, most_common_normal)])
        mag1 = math.sqrt(sum([a*a for a in normal]))
        mag2 = math.sqrt(sum([a*a for a in most_common_normal]))
        cos_angle = dot / (mag1 * mag2)
        angle = math.acos(cos_angle)
        if math.degrees(angle) > 1:
            facesFlat = 0
    return facesFlat

def speedBendExtrudeGO():
    global passSelection
    passSelection = []
    toBlendFace = cmds.filterExpand(ex=1, sm=(34))
    if toBlendFace:
        beforeBendClean()
        toBlendFace = cmds.filterExpand(ex=1, sm=(34))
        checkFlat = isFlat(toBlendFace)
        if checkFlat == 1:
            singleFaceRecord = cmds.filterExpand(ex=1, sm=(34))
            toBlendEdge = cmds.ls(cmds.polyListComponentConversion(singleFaceRecord, te=1),fl=1)
            totalDistance = 0
            for b in toBlendEdge:
                listVtx = cmds.ls(cmds.polyListComponentConversion(b, tv=1),fl=1)
                pA = cmds.pointPosition(listVtx[0], w=1)
                pB = cmds.pointPosition(listVtx[1], w=1)
                checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
                totalDistance = totalDistance + checkDistance
            diameterA = totalDistance / 3.14159
            bendLength = totalDistance / 2
            cmds.polyExtrudeFacet(constructionHistory=0, keepFacesTogether=1, divisions=1, twist=0, taper=0, off=0 , thickness = bendLength , smoothingAngle=30)
        finishBendClean()

def speedBendLinkUI():
    checkSetting = cmds.checkBox('speedBendSetting',q=1, v= 1)
    checkDivSetting = cmds.checkBox('speedBendNoDiv',q=1, v= 1)
    bendV = cmds.floatSliderGrp("speedBendBend",q=1,v=1)
    rollV = cmds.floatSliderGrp("speedBendRoll",q=1,v=1)
    offsetV = cmds.floatSliderGrp('speedBendOffset',q=1,v=1)
    cmds.iconTextButton("speedBendGOGO", e=1, en=0 ,bgc=[0.28,0.28,0.28],l='')
    cmds.iconTextButton("speedBendExtrude", e=1, en=0 ,bgc=[0.28,0.28,0.28],l='')
    if checkDivSetting == 0:
        divV = cmds.intSliderGrp("speedBendDiv",q=1,v=1)
    cmds.connectControl( 'speedBendBend', 'speedBend.curvature' )
    cmds.connectControl( 'speedBendRoll', 'bendOffsetRot.rotateY' )
    cmds.connectControl( 'speedBendOffset', 'speedBendHandle.translateX' )
    if checkDivSetting == 0:
        cmds.connectControl( 'speedBendDiv', 'speedBendBridge.divisions' )
    if checkSetting == 1:
        cmds.setAttr('speedBend.curvature',bendV)
        cmds.setAttr('bendOffsetRot.rotateY',rollV)
        cmds.setAttr('speedBendHandle.translateX',offsetV)
        if checkDivSetting == 1:
            cmds.setAttr('speedBendBridge.divisions',divV)
            cmds.iconTextButton("speedBendExtrude", e=1, en=0 ,bgc=[0.28,0.28,0.28],l='')
    cmds.scriptJob (ro=1, event = ["SelectionChanged", finishBendClean])
    cmds.scriptJob(uiDeleted=["speedBendUI", finishBendClean])

def speedBendOffsetReset():
    currentV = cmds.floatSliderGrp("speedBendOffset",e=1,v=0)
    if cmds.objExists('speedBendHandle'):
        cmds.setAttr('speedBendHandle.translateX' ,0)

def speedBendOffsetMore(more):
    currentV = cmds.floatSliderGrp("speedBendOffset",q=1,max=1)
    if currentV ==  100:
        if (more == -1):
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 0, min = -1, max = 10, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.34, 0.34, 0.34])
            cmds.button('sBOffsetPlus',e=1,en=1,l='+')
    if currentV ==  10:
        if (more == 1):
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 0, min = -10, max = 100, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.44, 0.44, 0.44])
            cmds.button('sBOffsetPlus',e=1,en=0,l='')
        else:
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 1, min = -1.0, max = 1, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.24, 0.24, 0.24])
    elif currentV ==  1:
        if (more == 1):
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 0, min = -1, max = 10, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.34, 0.34, 0.34])
        else:
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 3, min = -1.0, max = 0.1, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.14, 0.14, 0.14])
    elif currentV ==  0.1:
        if (more == 1):
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 2, min = -1.0, max = 1, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.24, 0.24, 0.24])
        else:
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 4, min = -1.0, max = 0.01, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.04, 0.04, 0.04])
            cmds.button('sBOffsetMinus',e=1,en=0,l='')
    elif currentV ==  0.01:
        if (more == 1):
            cmds.floatSliderGrp('speedBendOffset',e=1, pre = 2, min = -1.0, max = 1, v=0)
            cmds.button("speedBendOffsetV", e=1 , bgc=[0.24, 0.24, 0.24])
            cmds.button('sBOffsetMinus',e=1,en=1,l='-')

def speedBendDivReset():
    currentV = cmds.intSliderGrp("speedBendDiv",e=1,v=8)
    if cmds.objExists('speedBendBridge'):
        cmds.setAttr('speedBendBridge.divisions',8)

def speedBendBendMore(more):
    currentV = cmds.floatSliderGrp("speedBendBend", q=1 , v=1)
    currentGap = cmds.intField('speedBendBendV', q=1,v =1)
    maxV = cmds.floatSliderGrp("speedBendBend", q=1, max=1)
    minV = cmds.floatSliderGrp("speedBendBend", q=1, min=1)
    nextCloseV = (int(currentV / currentGap) + int(more)) * currentGap
    if nextCloseV > maxV:
        nextCloseV = maxV
    elif nextCloseV < minV:
        nextCloseV = minV
    cmds.floatSliderGrp("speedBendBend", e=1 , v=nextCloseV)
    if cmds.objExists('speedBend'):
        cmds.setAttr('speedBend.curvature',nextCloseV)

def speedBendBendReset():
    cmds.floatSliderGrp("speedBendBend", e=1 , v=90)
    if cmds.objExists('speedBend'):
        cmds.setAttr('speedBend.curvature',90)

def speedBendBendUpdate():
    currentV = cmds.floatSliderGrp("speedBendBend", q=1 , v=1)
    if cmds.objExists('speedBendBend'):
        cmds.setAttr('speedBend.curvature',currentV)


def speedBendRollMore(more):
    currentV = cmds.floatSliderGrp("speedBendRoll", q=1 , v=1)
    currentGap = cmds.intField('speedBendRollV', q=1,v =1)
    maxV = cmds.floatSliderGrp("speedBendRoll", q=1, max=1)
    minV = cmds.floatSliderGrp("speedBendRoll", q=1, min=1)
    nextCloseV = (int(currentV / currentGap) + int(more)) * currentGap
    if nextCloseV > maxV:
        nextCloseV = maxV
    elif nextCloseV < minV:
        nextCloseV = minV
    cmds.floatSliderGrp("speedBendRoll", e=1 , v=nextCloseV)
    if cmds.objExists('bendOffsetRot'):
        cmds.setAttr('bendOffsetRot.rotateY',nextCloseV)

def speedBendRollUpdate():
    currentV = cmds.floatSliderGrp("speedBendRoll", q=1 , v=1)
    if cmds.objExists('bendOffsetRot'):
        cmds.setAttr('bendOffsetRot.rotateY',currentV)

def speedBendRollReset():
    cmds.floatSliderGrp("speedBendRoll", e=1 , v=0)
    if cmds.objExists('bendOffsetRot'):
        cmds.setAttr('bendOffsetRot.rotateY',0)

def speedBendGo():
    global passSelection
    passSelection = []
    checkButton = cmds.iconTextButton("speedBendGOGO", q=1, en=1)
    checkDivSetting = cmds.checkBox('speedBendNoDiv',q=1, v= 1)
    if checkButton == 1:
        sBFillHole()
        global toBlendMesh
        lockFaceList = []
        beforeBendClean()
        toBlendFace = cmds.filterExpand(ex=1, sm=(34))
        if toBlendFace:
            toBlendMesh = toBlendFace[0].split('.')[0]
            toBlendShape = cmds.listRelatives(toBlendMesh,f=1, s=1)
            singleFace = 0
            cmds.sets(name="toBlendCut", text="toBlendCut")
            if len(toBlendFace) > 0:
                checkFlat = isFlat(toBlendFace)
                if checkFlat == 1:
                    singleFaceRecord = cmds.filterExpand(ex=1, sm=(34))
                    toBlendEdgeAll = cmds.ls(cmds.polyListComponentConversion(singleFaceRecord, te=1),fl=1)
                    toBlendEdgeInside = cmds.ls(cmds.polyListComponentConversion(singleFaceRecord, te=1,internal=1),fl=1)
                    toBlendEdge = list(set(toBlendEdgeAll)-set(toBlendEdgeInside))
                    totalDistance = 0
                    for b in toBlendEdge:
                        listVtx = cmds.ls(cmds.polyListComponentConversion(b, tv=1),fl=1)
                        pA = cmds.pointPosition(listVtx[0], w=1)
                        pB = cmds.pointPosition(listVtx[1], w=1)
                        checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
                        totalDistance = totalDistance + checkDistance
                    diameterA = totalDistance / 3.14159
                    bendLength = totalDistance / 2
                    cmds.polyExtrudeFacet(constructionHistory=0, keepFacesTogether=1, divisions=1, twist=0, taper=0, off=0 , thickness = bendLength , smoothingAngle=30)
                    addCapFace = cmds.ls(sl=1,fl=1)
                    addCapEdge = cmds.ls(cmds.polyListComponentConversion(addCapFace, te=1),fl=1)
                    cmds.sets(toBlendEdge,name="toBlendCut", text="toBlendCut")
                    cmds.sets(addCapEdge, add= 'toBlendCut')
                    toBlendFace = cmds.ls(cmds.polyListComponentConversion(addCapEdge, tf=1),fl=1)
                    singleFace = 1
            if len(toBlendFace) > 1 :
                convert2EdgeInternal = cmds.ls(cmds.polyListComponentConversion(toBlendFace, te=1, internal=1),fl=1)
                convert2Edge = cmds.ls(cmds.polyListComponentConversion(toBlendFace, te=1),fl=1)
                toBlendEdge = list(set(convert2Edge)-set(convert2EdgeInternal))
                cmds.sets(toBlendEdge, add= 'toBlendCut')
                fullFace =  cmds.ls( (toBlendMesh+'.f[*]'),fl=1)
                lockFaceList = list(set(fullFace)-set(toBlendFace))
                cmds.sets(lockFaceList,name="lockFaces", text="lockFaces")
                ringVtx = cmds.polyListComponentConversion(toBlendEdge, tv=1)
                ringVtx = cmds.ls(ringVtx,fl=1)
                cv_positions = [cmds.pointPosition(x,w=1) for x in ringVtx]
                center_position = [sum(axis) / len(ringVtx) for axis in zip(*cv_positions)]
                grp = cmds.group(empty=True, name='bendPointA')
                cmds.move(center_position[0], center_position[1], center_position[2], grp, absolute=True)
                findFace = cmds.polyListComponentConversion(toBlendEdge, tf=1)
                findFace = cmds.ls(findFace,fl=1)
                getFaceList = list(set(findFace) & set(toBlendFace))
                ringEdgeList = cmds.ls(cmds.polyListComponentConversion(getFaceList,te=1,internal=1),fl=1)
                capEdgeLoop = cmds.ls(cmds.polyListComponentConversion(getFaceList,te=1),fl=1)
                ringB = list(set(capEdgeLoop) - set(ringEdgeList) - set(toBlendEdge))
                ringVtxB = cmds.ls(cmds.polyListComponentConversion(ringB, tv=1),fl=1)
                cv_positionsB = [cmds.pointPosition(x,w=1) for x in ringVtxB]
                center_positionB = [sum(axis) / len(ringVtxB) for axis in zip(*cv_positionsB)]
                grpB = cmds.group(empty=True, name='bendPointB')
                cmds.move(center_positionB[0], center_positionB[1], center_positionB[2], grpB, absolute=True)
                consNodeA = cmds.aimConstraint('bendPointB','bendPointA',offset=[0,0,0], weight=1, aimVector=[0,1,0], upVector=[1,0,0], worldUpType='vector')
                rotationRecord = cmds.getAttr('bendPointA.rotate')
                if singleFace == 0:
                    totalDistance = 0
                    for b in toBlendEdge:
                        listVtx = cmds.ls(cmds.polyListComponentConversion(b, tv=1),fl=1)
                        pA = cmds.pointPosition(listVtx[0], w=1)
                        pB = cmds.pointPosition(listVtx[1], w=1)
                        checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
                        totalDistance = totalDistance + checkDistance
                    diameterA = totalDistance / 3.14159
                    bendLength = totalDistance / 2
                    cmds.polySplitRing(ringEdgeList)
                    newSplitRing = cmds.ls(sl=1,fl=1)
                    findNewVerticleFaceA = cmds.ls(cmds.polyListComponentConversion(newSplitRing , tf=1),fl=1)
                    findNewVerticleFaceB = cmds.ls(cmds.polyListComponentConversion(toBlendEdge , tf=1),fl=1)
                    findNewVerticleFace = list(set(findNewVerticleFaceA) & set(findNewVerticleFaceB))
                    findNewVerticleVerticleEdge = cmds.ls(cmds.polyListComponentConversion(findNewVerticleFace,te=1,internal=1),fl=1)
                    cmds.sets(newSplitRing, add = 'toBlendCut' )
                    if checkDivSetting == 0:
                        listVtx = cmds.ls(cmds.polyListComponentConversion(findNewVerticleVerticleEdge[0], tv=1),fl=1)
                        pA = cmds.pointPosition(listVtx[0], w=1)
                        pB = cmds.pointPosition(listVtx[1], w=1)
                        oldEdgeDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
                        distanceScaleV = bendLength /oldEdgeDistance
                        for v in findNewVerticleVerticleEdge:
                            listVtx = cmds.ls(cmds.polyListComponentConversion(v, tv=1),fl=1)
                            getBaseCV = list(set(listVtx) & set(ringVtx))
                            pA = cmds.pointPosition(getBaseCV, w=1)
                            cmds.scale(distanceScaleV,distanceScaleV,distanceScaleV, v, cs=1, r=1, p= (pA[0],pA[1],pA[2]))
                        cmds.delete(findNewVerticleFace)
                        cmds.delete(toBlendMesh,ch=1)
                        cmds.select('toBlendCut',add=1)
                else:
                    if checkDivSetting == 0:
                        toDeleteFace = list(set(toBlendFace)-set(singleFaceRecord))
                        cmds.delete(toDeleteFace)
                        cmds.delete(toBlendMesh,ch=1)
                if checkDivSetting == 0:
                    membersLockFaces = cmds.ls(cmds.sets('lockFaces', query=True),fl=1)
                    cmds.polyBridgeEdge('toBlendCut',ch=1, divisions=20, twist=0, taper=1, curveType=0, smoothingAngle=30, direction=0, sourceDirection=0, targetDirection=0)
                    history_nodes = cmds.listHistory(toBlendMesh)
                    polyBridgeNode= cmds.ls(history_nodes,type='polyBridgeEdge')
                    cmds.rename(polyBridgeNode[0],'speedBendBridge')
                    cmds.createNode('mesh')
                    cmds.rename('toBlendOutShape')
                    unWantTransNode = cmds.listRelatives('toBlendOutShape', parent=True)[0]
                    cmds.connectAttr((toBlendShape[0] + '.outMesh'), ('toBlendOutShape.inMesh'),f=1)
                    cmds.parent('toBlendOutShape',toBlendMesh, relative=True, shape=True)
                    cmds.delete(unWantTransNode)
                    shading_group = cmds.listConnections(toBlendShape[0], type='shadingEngine')[0]
                    cmds.sets('toBlendOutShape', e=1, forceElement=shading_group)
                    cmds.HideSelectedObjects(toBlendShape[0])
                    cmds.polySoftEdge(toBlendMesh, a=30, ch=1)
                cmds.select(toBlendMesh)
                cmds.Bend()
                bendHandleNode = cmds.ls(sl=1,fl=1,transforms=1)
                cmds.rename(bendHandleNode[0],'speedBendHandle')
                history_nodes = cmds.listHistory(toBlendMesh)
                bendNode = cmds.ls(history_nodes,type='nonLinear')
                cmds.rename(bendNode[0],'speedBend')
                cmds.setAttr(('speedBendHandle.rotate'),rotationRecord[0][0],rotationRecord[0][1],rotationRecord[0][2])
                cmds.setAttr(('speedBendHandle.translate'),center_position[0],center_position[1],center_position[2])
                cmds.setAttr(('speedBendHandle.scale'),bendLength,bendLength,bendLength)
                cmds.setAttr('speedBend.lowBound',0)
                cmds.setAttr('speedBend.curvature',90)
                cmds.parent('speedBendHandle',toBlendMesh)
                offSetGrp = cmds.group(empty=True, name="bendOffset")
                offSetRotGrp = cmds.group(empty=True, name="bendOffsetRot")
                cmds.parent(offSetRotGrp,offSetGrp)
                cmds.parent(offSetGrp,'speedBendHandle')
                cmds.setAttr('bendOffset.translate',0,0,0)
                cmds.setAttr('bendOffset.rotate',0,0,0)
                cmds.setAttr('bendOffset.scale',1,1,1)
                cmds.parent('bendOffset',toBlendMesh)
                cmds.parent('speedBendHandle','bendOffsetRot')
                weightZeroList = cmds.ls(cmds.polyListComponentConversion(membersLockFaces, tv=1),fl=1)
                for f in weightZeroList:
                    cmds.percent('speedBend',f , v=0)
                if checkDivSetting == 0:
                    toBlendFaceList  = cmds.ls(cmds.polyListComponentConversion('toBlendOutShape',tf=1),fl=1)
                    convertList = []
                    for e in lockFaceList:
                        newN =  'toBlendOutShape.' + e.split('.')[-1]
                        convertList.append(newN)
                    selBendArea = list(set(toBlendFaceList) - set(convertList))
                    if singleFace == 1:
                        passSelection = addCapFace
                    else:
                        passSelection = selBendArea
                    cmds.hide(toBlendShape)
                    cmds.select(cl=1)
                    cmds.showHidden('toBlendOutShape')
                cmds.select(toBlendMesh)
                cleanList = ('bendPoint*','lockFaces','toBlendCut')
                for c in cleanList:
                    if cmds.objExists(c):
                        cmds.delete(c)
                cmds.setAttr(('speedBendHandle.hiddenInOutliner'),0)
                cmds.setAttr(('speedBendHandle.visibility'),0)
                if checkDivSetting == 0:
                    cmds.setAttr("speedBendBridge.divisions",8)
                speedBendLinkUI()


def beforeBendClean():
    speedBendScriptJobClean()
    selection  = cmds.ls(sl=1,fl=1)
    if selection:
        top_node = selection[0]
        while cmds.listRelatives(top_node, parent=True):
            top_node = cmds.listRelatives(top_node, parent=True)[0]
        cmds.delete(top_node ,ch=1)
        toBlendShape = cmds.listRelatives(top_node, s=1)
        if toBlendShape:
            if len(toBlendShape)>1:
                if 'toBlendOutShape' in toBlendShape:
                   for s in toBlendShape:
                       if s != 'toBlendOutShape':
                           cmds.delete(s)
                else:
                    faceCount = cmds.polyEvaluate(top_node, f=True )
                    for t in toBlendShape:
                        checkFaceCount = cmds.polyEvaluate(t, f=True )
                        if checkFaceCount != faceCount:
                            cmds.delete(t)
            toBlendShape = cmds.listRelatives(top_node,f=1,s=1)[0]
            parentNode = cmds.listRelatives(toBlendShape,f=1, p=1)[0]
            cmds.rename(toBlendShape,(parentNode[1:]+'Shape'))
        cleanList = ('speedBendBridg*','bendPoint*','lockFace*','toBlendCu*','toBlendOutShap*','speedBen*','bendOffse*')
        for c in cleanList:
            if cmds.objExists(c):
                cmds.delete(c)
        cmds.showHidden(top_node)

def finishBendClean():
    storeSel = cmds.ls(sl=1)
    speedBendScriptJobClean()
    global toBlendMesh
    global passSelection
    if cmds.objExists(toBlendMesh):
        cmds.delete(toBlendMesh ,ch=1)
        toBlendShape = cmds.listRelatives(toBlendMesh,s=1)
        if toBlendShape:
            if len(toBlendShape)>1:
                if 'toBlendOutShape' in toBlendShape:
                   for s in toBlendShape:
                       if s != 'toBlendOutShape':
                           cmds.delete(s)
                else:
                    faceCount = cmds.polyEvaluate(toBlendMesh, f=True )
                    for t in toBlendShape:
                        checkFaceCount = cmds.polyEvaluate(t, f=True )
                        if checkFaceCount != faceCount:
                            cmds.delete(t)
            toBlendShape = cmds.listRelatives(toBlendMesh,f=1,s=1)[0]
            parentNode = cmds.listRelatives(toBlendShape,f=1, p=1)[0]
            cmds.rename(toBlendShape,(parentNode[1:]+'Shape'))
            cmds.showHidden(toBlendMesh)
            if passSelection:
                convertList = []
                for p in passSelection:
                    newN =  toBlendMesh +'.' + p.split('.')[-1]
                    convertList.append(newN)
                cmds.select(convertList)
    checkState = cmds.iconTextButton("speedBendGOGO", q=1, ex=1 )
    if checkState == 1:
        cmds.iconTextButton("speedBendGOGO", e=1, en=1, l ="Bend", bgc=[0.2, 0.2, 0.2] )
    cmds.iconTextButton("speedBendExtrude", e=1, en=1 ,bgc=[0.2,0.2,0.2],l='Extrude')

def speedBendScriptJobClean():
    count = 0
    foundError = 1
    while foundError > 0 and count < 10:
        jobs = cmds.scriptJob( listJobs=True )
        foundError = 0
        for j in jobs:
            if "finishBendClean" in j:
                jID = j.split(':')[0]
                print(jID)
                try:
                    cmds.scriptJob (kill = int(jID),f =1 )
                except:
                    foundError = 1

        count +=  1
    
def run():
    if cmds.window("speedBendUI", exists=True):
        cmds.deleteUI("speedBendUI")
    speedBendUI = cmds.window("speedBendUI",title = "Speed Bend",w = 350,h = 150)
    cmds.frameLayout(label="Bend Extrude:",lv=0, bv=0, w=295, mw=3, mh=5)
    cmds.columnLayout(adj=1)
    cmds.rowColumnLayout(nc=5, cw=[(1, 220), (2, 30), (3, 30),(4, 30),(5, 30)])
    cmds.floatSliderGrp("speedBendBend", cw3=[50, 50, 0], label="     Bend", f=1, v=90, min=-180, max=180, pre=0, cc=speedBendBendUpdate)
    cmds.button(label="X", c=speedBendBendReset, bgc=[0.24, 0.24, 0.24])
    cmds.intField('speedBendBendV', v =45, bgc =[0.24,0.24,0.24])
    cmds.button(label="-", c=lambda x: speedBendBendMore(-1), bgc=[0.24, 0.24, 0.24])
    cmds.button(label="+", c=lambda x: speedBendBendMore(1), bgc=[0.24, 0.24, 0.24])

    cmds.floatSliderGrp("speedBendRoll", cw3=[50, 50, 0], label="    Roll", f=1, v=45, min=-180, max=180, fmx=360, pre=0, cc=speedBendRollUpdate)
    cmds.button(label="X", c=speedBendRollReset, bgc=[0.24, 0.24, 0.24])
    cmds.intField('speedBendRollV', v =45, bgc =[0.24,0.24,0.24] )
    cmds.button(label="-", c=lambda x: speedBendRollMore(-1), bgc=[0.24, 0.24, 0.24])
    cmds.button(label="+", c=lambda x: speedBendRollMore(1), bgc=[0.24, 0.24, 0.24])

    cmds.floatSliderGrp("speedBendOffset", cw3=[50, 50, 0], label="    Offset", f=1, v=0, min=-0.1, max=1, pre=1)
    cmds.button(label="X", c=speedBendOffsetReset, bgc=[0.24, 0.24, 0.24])
    cmds.button("speedBendOffsetV", en= 0,label="", bgc=[0.24, 0.24, 0.24])
    cmds.button('sBOffsetMinus',label="-", c=lambda x: speedBendOffsetMore(-1), bgc=[0.24, 0.24, 0.24])
    cmds.button('sBOffsetPlus',label="+", c=lambda x: speedBendOffsetMore(1), bgc=[0.24, 0.24, 0.24])

    cmds.intSliderGrp("speedBendDiv", cw3=[50, 50, 0], label="Divisions", v=4, f=1, min=1, max=16, fmx=36)
    cmds.button(label="X", c=speedBendDivReset, bgc=[0.24, 0.24, 0.24])
    cmds.setParent("..")

    cmds.rowColumnLayout(nc=7, cw=[(1, 18),(2, 100), (3, 100), (4, 2), (5, 58), (6, 2), (7, 58)])
    cmds.text(l ='')
    cmds.columnLayout(adj=1)
    cmds.checkBox('speedBendSetting',label="Remember", value= 0)
    cmds.checkBox('speedBendNoDiv',label="No Divisions", value= 0)
    cmds.setParent("..")
    cmds.iconTextButton("speedBendGOGO", style='textOnly', l ="Bend", c=speedBendGo, rpt=1, bgc=[0.2, 0.2, 0.2])
    cmds.text(l ='')
    cmds.iconTextButton("speedBendExtrude", style='textOnly', l ="Extrude", c=speedBendExtrudeGO, rpt=1, bgc=[0.2, 0.2, 0.2])
    cmds.text(l ='')
    cmds.iconTextButton(style='textOnly', l ="Done", c=finishBendClean, bgc=[0.3, 0.2, 0.2])
    cmds.showWindow(speedBendUI)

if __name__ == "__main__":
    run()