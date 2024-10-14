#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import re, math
import maya.OpenMayaUI as omui
import maya.api.OpenMaya as oma
import maya.api.OpenMayaUI as omuia
mel.eval('source "dagMenuProc"')


def X23():
    getVexList = cmds.filterExpand(ex=1, sm=31)
    getEdgeList = cmds.filterExpand(ex=1, sm=32)
    tokens = ''
    if getVexList:    
        for g in getVexList:
            cmds.select(g)
            X43('')
        cmds.select(getVexList) 
        tokens = getVexList[0].split(".")
        cmd  = 'doMenuComponentSelectionExt("' + tokens[0] + '", "vertex", 0);'
        mel.eval(cmd)
    if getEdgeList and len(getEdgeList) == 2:  
        X56()
        currentSet = cmds.ls(sl=1,fl=1)
        tokens = currentSet[0].split(".")
        cmd  = 'doMenuComponentSelectionExt("' + tokens[0] + '", "edge", 0);'
        mel.eval(cmd)
        cmds.select(currentSet,r=1)
    elif getEdgeList and len(getEdgeList) == 1: 
        listVtx = cmds.ls(cmds.polyListComponentConversion(getEdgeList, tv=1),fl=1)
        for g in listVtx:
            cmds.select(g)
            X43(getEdgeList[0])
        cmds.select(getEdgeList) 
        tokens = getEdgeList[0].split(".")
        cmd  = 'doMenuComponentSelectionExt("' + tokens[0] + '", "edge", 0);'
        mel.eval(cmd)
        cmds.select(getEdgeList)
    
def X56():
    selEdges = cmds.ls(sl=1,fl=1)
    cmds.polyBridgeEdge(ch=1, divisions=1, twist=0, taper=1, curveType=0, smoothingAngle=30, direction=0, sourceDirection=0, targetDirection=0)
    selEdges = cmds.ls(sl=1,fl=1)
    rings = cmds.polySelectSp(ring=1)
    cmds.select(selEdges, d=1)
    midEdge = cmds.ls(sl=1,fl=1)
    listVtx = cmds.ls(cmds.polyListComponentConversion(midEdge, tv=1),fl=1)
    for i in listVtx:
        cmds.select(i)
        X43('')
    cmds.select(midEdge)

def X43(unwantEdges):
    selPoint = cmds.ls(sl=1,fl=1)
    cmds.ConvertSelectionToEdges()
    if unwantEdges:
        unwantLoop = cmds.ls(cmds.polySelectSp(unwantEdges,loop=1,q=1),fl=1)
        cmds.select(unwantLoop,d=1)
    selEdgeCheck = cmds.ls(sl=1,fl=1)
    findA = ''
    findB = ''
    goSharp = 0
    if len(selEdgeCheck) == 3:
        cmds.polySelectConstraint(m=2,w=1,t=0x8000)
        cmds.polySelectConstraint(disable=True)
        selEdge = cmds.ls(sl=1,fl=1)
        findA = selEdge[0]
        findB = selEdge[1]
        goSharp = 1
    elif len(selEdgeCheck) == 2:
        findA = selEdgeCheck[0]
        findB = selEdgeCheck[1]
        goSharp = 1
    elif len(selEdgeCheck) > 3:
        cmds.select(selPoint)
    if goSharp == 1:
        #selEdgeCheck.remove(findA)
        #selEdgeCheck.remove(findB)
        #cmds.select(selEdgeCheck)
        #X32()
        #X32()
        #unwantRing = cmds.ls(sl=1,fl=1)    
        cmds.select(findA,findB )
        XI9("plus")
        XI9("plus")
        #cmds.polySelectConstraint(type=0x8000, propagate=4, m2a=180, m3a=180, ed=2)
        loopACheck = cmds.ls(sl=1,fl=1)
        cmds.select(findA,findB)
        edgelist = []
        vertexAB = cmds.ls(cmds.polyListComponentConversion(findA,findB, tv=1),fl=1)
        for a in loopACheck:
            checkVex = cmds.ls(cmds.polyListComponentConversion(a, tv=1),fl=1)
            for c in checkVex:
                if c in vertexAB:
                    edgelist.append(a)
        #cmds.select(edgelist)
        listVtx = X8I(edgelist)
        checkA = X79(listVtx[1],listVtx[0],listVtx[-1])
        angleA = math.degrees(checkA)
        checkB = X79(listVtx[-2],listVtx[-1],listVtx[0])
        angleB = math.degrees(checkB)
        angleC = 180 - angleA -angleB
        distanceC = X3o(listVtx[0],listVtx[-1])
        distanceA = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleA))
        distanceB = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleB))
        oldDistA = X3o(listVtx[-2],listVtx[-1])
        oldDistB = X3o(listVtx[0],listVtx[1])
        scalarB = distanceB / oldDistB 
        pA = cmds.pointPosition(listVtx[0], w =1)
        pB = cmds.pointPosition(listVtx[1], w =1)
        newP = [0,0,0]
        newP[0] = ((pB[0]-pA[0])*scalarB) + pA[0]
        newP[1] = ((pB[1]-pA[1])*scalarB) + pA[1]
        newP[2] = ((pB[2]-pA[2])*scalarB) + pA[2]
        cmds.move(newP[0],newP[1],newP[2],selPoint[0], absolute = 1 )
        cmds.select(selPoint)


def XoI():
    number = cmds.floatField("refInsertLength", q=1, v = 1)
    selEdge = cmds.ls(sl=True, fl=True)
    
    if len(selEdge) == 1:
        PD_points = cmds.ls(cmds.polyListComponentConversion(selEdge, tv=True),fl=1)
        PD_coord1 = cmds.pointPosition(PD_points[0])
        PD_coord2 = cmds.pointPosition(PD_points[1])
        PD_distance = ((PD_coord1[0] - PD_coord2[0])**2 + (PD_coord1[1] - PD_coord2[1])**2 + (PD_coord1[2] - PD_coord2[2])**2)**0.5
        n = int(PD_distance / number)
        if n > 0:
            cmds.polySelectSp(selEdge[0], ring=True)
            cmds.polySplitRing(ch=True, splitType=2, divisions=n, useEqualMultiplier=True, smoothingAngle=30, fixQuads=False)
    
    elif len(selEdge) > 1:
        confirmString = cmds.confirmDialog(title="Confirm", message="Warning!! More than one edge selected?", button=["Continues", "Abort"], defaultButton="Abort", cancelButton="Abort", dismissString="Abort")
        if confirmString == "Continues":
            for s in selEdge:
                PD_points = cmds.ls(cmds.polyListComponentConversion(s, tv=True),fl=1)
                PD_coord1 = cmds.pointPosition(PD_points[0])
                PD_coord2 = cmds.pointPosition(PD_points[1])
                PD_distance = ((PD_coord1[0] - PD_coord2[0])**2 + (PD_coord1[1] - PD_coord2[1])**2 + (PD_coord1[2] - PD_coord2[2])**2)**0.5
                n = int(PD_distance / number)
                if n > 0:
                    cmds.polySelectSp(s, ring=True)
                    cmds.polySplitRing(ch=True, splitType=2, divisions=n, useEqualMultiplier=True, smoothingAngle=30, fixQuads=False)
                cmds.BakeNonDefHistory()

def X92():
    global selInitialGeo
    global storeAllEdges
    selInitialGeo = []
    storeAllEdges = []
    testAnySel = cmds.ls(sl=1)
    if testAnySel:
        checkCurrentSelEdge = cmds.filterExpand(sm=32)
        checkCurrentSelPoly = cmds.filterExpand(sm=12)
        checkCurrentSelOther =cmds.filterExpand(sm=(31,34,35) )
        if checkCurrentSelEdge:
            checkEdgeLoopGrp =  XlO(checkCurrentSelEdge)
            if len(checkEdgeLoopGrp) == 1:
                listAAA = ''
                try:
                    listAAA = X8I(checkCurrentSelEdge)
                except:
                    pass
                if listAAA:
                    storeAllEdges = checkCurrentSelEdge
                    checkCurrentSelPoly = cmds.ls(hl=1)
                    selInitialGeo.append(checkCurrentSelPoly[0])
                    if not cmds.attributeQuery('start', node = selInitialGeo[0], ex=True ):
                        cmds.addAttr(selInitialGeo[0], at = 'long', ln='start') 
                    if not cmds.attributeQuery('end', node = selInitialGeo[0], ex=True ):
                        cmds.addAttr(selInitialGeo[0], at = 'long',ln='end') 
                    if not cmds.attributeQuery('nearest', node = selInitialGeo[0], ex=True ):
                        cmds.addAttr(selInitialGeo[0], at = 'long',ln='nearest') 
                    if not cmds.attributeQuery('closeTo', node = selInitialGeo[0], ex=True ):
                        cmds.addAttr(selInitialGeo[0], at = 'long',ln='closeTo') 
                    if not cmds.attributeQuery('firstRun', node = selInitialGeo[0], ex=True ):
                        cmds.addAttr(selInitialGeo[0], at = 'long',ln='firstRun') 
                    cmds.setAttr((selInitialGeo[0]+'.firstRun'),0)
                    X67()
                else:
                    cmds.select(checkCurrentSelEdge)
            else:
                cmds.select(checkCurrentSelEdge)
        else:
            if checkCurrentSelOther:
                checkCurrentSelPoly = cmds.ls(hl=1)
            selInitialGeo.append(checkCurrentSelPoly[0])
            CMD = 'doMenuComponentSelectionExt("' + str(checkCurrentSelPoly[0])+ '", "edge", 0);'
            mel.eval(CMD)
            cmds.select(cl=1)
            cmds.polyCrease((checkCurrentSelPoly[0]+'.e[*]'), value=0)
            if not cmds.attributeQuery('start', node = selInitialGeo[0], ex=True ):
                cmds.addAttr(selInitialGeo[0], at = 'long', ln='start') 
            if not cmds.attributeQuery('end', node = selInitialGeo[0], ex=True ):
                cmds.addAttr(selInitialGeo[0], at = 'long',ln='end') 
            if not cmds.attributeQuery('nearest', node = selInitialGeo[0], ex=True ):
                cmds.addAttr(selInitialGeo[0], at = 'long',ln='nearest') 
            if not cmds.attributeQuery('closeTo', node = selInitialGeo[0], ex=True ):
                cmds.addAttr(selInitialGeo[0], at = 'long',ln='closeTo') 
            if not cmds.attributeQuery('firstRun', node = selInitialGeo[0], ex=True ):
                cmds.addAttr(selInitialGeo[0], at = 'long',ln='firstRun') 
            cmds.setAttr((selInitialGeo[0]+'.firstRun'),0)
            cmds.scriptJob ( runOnce=True, event = ["SelectionChanged", selShortestLoop])
    else:
        print('no selection')
def X67():
    global ctx
    global storeAllEdges
    global selInitialGeo
    global storeCameraPosition
    global initialList
    initialList = []
    storeAllEdges = cmds.ls(sl=1,fl=1)
    listVtx = X8I(storeAllEdges)
    initialList = listVtx
    startID = listVtx[0].split('[')[-1].split(']')[0]
    endID = listVtx[-1].split('[')[-1].split(']')[0]
    cmds.setAttr((selInitialGeo[0]+'.start'),int(startID))
    cmds.setAttr((selInitialGeo[0]+'.end'),int(endID))
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
    storeCameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)
    if cmds.objExists('preSelDisp')==0:
        cmds.createNode("creaseSet")
        cmds.rename("preSelDisp")
    cmds.sets((selInitialGeo[0]+".e[*]"),remove="preSelDisp")
    cmds.sets(storeAllEdges,forceElement="preSelDisp")
    cmds.setAttr("preSelDisp.creaseLevel", 1)
    cmds.polyOptions(dce=1)
    ctx = 'Click2dTo3dCtx'
    if cmds.draggerContext(ctx, exists=True):
        cmds.deleteUI(ctx)
    cmds.draggerContext(ctx, ppc= X46 ,rc = X46, dragCommand = X8l, fnz = X4I ,name=ctx, cursor='crossHair',undoMode='step')
    cmds.setToolTo(ctx)

def X8l():
    global selInitialGeo
    global ctx
    global screenX,screenY
    global storeCameraPosition
    global storeAllEdges
    modifiers = cmds.getModifiers()
    if selInitialGeo:
        vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
        pos = om.MPoint()
        dir = om.MVector()
        hitpoint = om.MFloatPoint()
        omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
        pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
        checkHit = 0
        finalMesh = []
        finalX = 0
        finalY = 0
        finalZ = 0
        shortDistance = 10000000000
        distanceBetween = 1000000000
        hitFacePtr = om.MScriptUtil().asIntPtr()
        hitFace = []
        for mesh in selInitialGeo:
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
                finalX = x
                finalY = y
                finalZ = z
                hitFace = om.MScriptUtil(hitFacePtr).asInt()
                hitFaceName = (selInitialGeo[0] + '.f[' + str(hitFace) +']')
                cpX,cpY,cpZ = Xl5(hitFaceName)
                shortDistanceCheck = 10000
                checkCVDistance = 10000
                cvList = (cmds.polyInfo(hitFaceName , fv=True )[0]).split(':')[-1].split('  ')
                cvListX = [x for x in cvList if x.strip()]

                for v in cvListX:
                    checkNumber = ''.join([n for n in v.split('|')[-1] if n.isdigit()])
                    if len(checkNumber) > 0:
                        cvPoint = (selInitialGeo[0] + '.vtx[' + str(checkNumber) +']')
                        cvPosition = cmds.pointPosition(cvPoint)
                        checkCVDistance = math.sqrt( ((float(cvPosition[0]) - finalX)**2)  + ((float(cvPosition[1]) - finalY)**2) + ((float(cvPosition[2]) - finalZ)**2))
                        if checkCVDistance < shortDistanceCheck:
                            shortDistanceCheck = checkCVDistance
                            mostCloseCVPoint = cvPoint
                            mostCloseCVPointPos = cvPosition
                
                newID = mostCloseCVPoint.split('[')[-1].split(']')[0]
                cmds.setAttr((selInitialGeo[0]+'.nearest'),int(newID))
                checkRun = cmds.getAttr(selInitialGeo[0]+'.firstRun')

                if checkRun == 1:
                    checkCloseTo = cmds.getAttr(selInitialGeo[0]+'.nearest')
                    checkStart = cmds.getAttr(selInitialGeo[0]+'.start')
                    checkEnd = cmds.getAttr(selInitialGeo[0]+'.end')
                    
                    startPosition = cmds.pointPosition( (selInitialGeo[0] + '.vtx[' + str(checkStart) +']'))
                    endPosition = cmds.pointPosition( (selInitialGeo[0] + '.vtx[' + str(checkEnd) +']'))
                    nearPosition = cmds.pointPosition( (selInitialGeo[0] + '.vtx[' + str(checkCloseTo) +']'))

                    distA = math.sqrt( ((float(nearPosition[0]) - startPosition[0])**2)  + ((float(nearPosition[1]) - startPosition[1])**2) + ((float(nearPosition[2]) - startPosition[2])**2))
                    distB = math.sqrt( ((float(nearPosition[0]) - endPosition[0])**2)  + ((float(nearPosition[1]) - endPosition[1])**2) + ((float(nearPosition[2]) - endPosition[2])**2))
                    if distA > distB:
                        cmds.setAttr((selInitialGeo[0]+'.end'),checkEnd)
                        cmds.setAttr((selInitialGeo[0]+'.start'),checkStart)
                    else:
                        cmds.setAttr((selInitialGeo[0]+'.end'),checkStart)
                        cmds.setAttr((selInitialGeo[0]+'.start'),checkEnd)
                checkStart = cmds.getAttr(selInitialGeo[0]+'.start')
                checkEnd = cmds.getAttr(selInitialGeo[0]+'.end')
                checkNearest =  cmds.getAttr(selInitialGeo[0]+'.nearest')
                #get shortest
                cmds.select(cl=1)
                cmds.sets((selInitialGeo[0]+".e[*]"),remove="preSelDisp")
                sortList = []
                if modifiers == 4: # "press Ctrl"
                    PA = (selInitialGeo[0] + '.vtx[' + str(checkEnd) +']')
                    PB = (selInitialGeo[0] + '.vtx[' + str(checkNearest) +']')
                    UVA = cmds.polyListComponentConversion(PA,fv =1 ,tuv=1)
                    UVB = cmds.polyListComponentConversion(PB,fv =1 ,tuv=1)
                    startUVID = UVA[0].split('[')[-1].split(']')[0]
                    endUVID = UVB[0].split('[')[-1].split(']')[0]
                    #cmds.polySelect(selInitialGeo[0] , shortestEdgePathUV=(int(startUVID), int(endUVID)))
                    listShort = cmds.polySelect(selInitialGeo[0] ,q=1, shortestEdgePathUV=(int(startUVID), int(endUVID)))
                    if listShort:
                        for l in listShort:
                            sortList.append(selInitialGeo[0]+'.e['+ str(l) +']' )
                else:
                    #cmds.polySelect(selInitialGeo[0] , shortestEdgePath=(int(checkEnd), int(checkNearest)))
                    #maya run faster without select
                    listShort = cmds.polySelect(selInitialGeo[0] ,q=1, shortestEdgePath=(int(checkEnd), int(checkNearest)))
                    if listShort:
                        for l in listShort:
                            sortList.append(selInitialGeo[0]+'.e['+ str(l) +']' )
                getC = storeAllEdges + sortList
                cmds.select(getC)
                cmds.sets(getC,forceElement="preSelDisp")
                if modifiers == 1: # "press Shelf"
                    liveList = cmds.sets("preSelDisp",q=1)
                    liveList = cmds.ls(liveList,fl=1)
                    listVtx = X8I(liveList)
                    checkEndID = listVtx[-1].split('[')[-1].split(']')[0]
                    extEdgeA = []
                    extEdgeB = []
                    if int(checkEndID) == checkNearest:
                        extEdgeA = cmds.polyListComponentConversion(listVtx[-1],fv =1 ,te=1)
                        extEdgeB = cmds.polyListComponentConversion(listVtx[-2],fv =1 ,te=1)
                    else:
                        extEdgeA = cmds.polyListComponentConversion(listVtx[0],fv =1 ,te=1)
                        extEdgeB = cmds.polyListComponentConversion(listVtx[1],fv =1 ,te=1)
                    extEdgeA = cmds.ls(extEdgeA,fl=1)
                    extEdgeB = cmds.ls(extEdgeB,fl=1)  
                    extEdge = list(set(extEdgeA) - (set(extEdgeA)-set(extEdgeB)))
                    checkExtLoop = cmds.polySelectSp(extEdge,q=1, loop=1)
                    checkExtLoop = cmds.ls(checkExtLoop,fl=1)
                    otherList = list(set(checkExtLoop) - set(liveList))
                    checkEdgeLoopGrp =  XlO(otherList)
                    if checkEdgeLoopGrp:
                        if len(checkEdgeLoopGrp) > 0:
                            if len(checkEdgeLoopGrp) == 1:
                                cmds.sets(otherList,forceElement="preSelDisp")
                            elif  len(checkEdgeLoopGrp)> 1:
                                for c in checkEdgeLoopGrp:
                                    cvList = cmds.polyListComponentConversion (c,fe=1,tv=1)
                                    cvList = cmds.ls(cvList,fl=1)
                                    if (selInitialGeo[0]+'.vtx['+ str(checkNearest) +']' ) in cvList:
                                        cmds.sets(c,forceElement="preSelDisp")
                            cmds.select("preSelDisp", add=1)
                cmds.refresh(cv=True,f=True)
def X46():
    global storeAllEdges
    global selInitialGeo
    global initialList
    checkRun = cmds.getAttr(selInitialGeo[0]+'.firstRun')
    if checkRun == 0:
         cmds.setAttr((selInitialGeo[0]+'.firstRun'),1)
    else:
        cmds.setAttr((selInitialGeo[0]+'.firstRun'),2)
        getEdgeList = cmds.ls(sl=1,fl=1)
        storeAllEdges = getEdgeList
        listVtx = X8I(getEdgeList)
        if len(listVtx)>0:
            listHead = listVtx[0]
            listEnd = listVtx[-1]
            if listHead in initialList:
                cmds.setAttr((selInitialGeo[0]+'.start'),int(listVtx[0].split('[')[-1].split(']')[0]))
                cmds.setAttr((selInitialGeo[0]+'.end'),int(listVtx[-1].split('[')[-1].split(']')[0]))

            else:
                cmds.setAttr((selInitialGeo[0]+'.start'),int(listVtx[-1].split('[')[-1].split(']')[0]))
                cmds.setAttr((selInitialGeo[0]+'.end'),int(listVtx[0].split('[')[-1].split(']')[0]))
        else:
            X4I()
def X4I():
    cmds.setToolTo("moveSuperContext")
    cmds.polyOptions(dce=0)
    if cmds.objExists('preSelDisp'):
        cmds.setAttr("preSelDisp.creaseLevel", 0)
        cmds.delete('preSelDisp')
def Xl5(faceName):
    meshFaceName = faceName.split('.')[0]
    findVtx = cmds.polyInfo(faceName, fv=1)
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
        x,y,z = cmds.pointPosition((meshFaceName + '.vtx['+g + ']'),w=1)
        centerX = centerX + x
        centerY = centerY + y
        centerZ = centerZ + z

    centerX = centerX/len(getNumber)
    centerY = centerY/len(getNumber)
    centerZ = centerZ/len(getNumber)
    return centerX,centerY,centerZ
    
def X98():
    global storeEdge
    global currentArcCurve
    if cmds.objExists('arcCurve*'):
        arcCurveList = cmds.ls( "arcCurve*", transforms =1  )
        a = arcCurveList[0]
        for a in arcCurveList:
            if 'BaseWire' not in a:
                shapeNode = cmds.listRelatives(a, fullPath=True )
                hist = cmds.listConnections(cmds.listConnections(shapeNode[0],sh=1, d=1 ) ,d=1 ,sh=1)
                cmds.delete(hist,ch=1)
        cmds.delete('arcCurve*')
    if len(currentArcCurve)>0:
        if cmds.objExists(currentArcCurve):
            shapeNode = cmds.listRelatives(currentArcCurve, fullPath=True )
            hist = cmds.listConnections(cmds.listConnections(shapeNode[0],sh=1, d=1 ) ,d=1 ,sh=1)
            cmds.delete(hist,ch=1)
    if cmds.objExists(currentArcCurve):
        cmds.select(currentArcCurve)
    cmds.select(storeEdge,add=1)
    if cmds.objExists(currentArcCurve + 'BaseWire'):
        cmds.delete(currentArcCurve + 'BaseWire')

def XI4():
    global storeEdge
    global currentArcCurve
    currentDropOff = cmds.floatSliderGrp('dropOffSlider' ,q=1,v=1)
    snapCheck = cmds.checkBox('snapCurve',q = 1 ,v = 1)
    goEven = cmds.checkBox('evenSpace', q=1 ,v = 1)
    conP = cmds.intSliderGrp('CPSlider',q=1 , v = True )
    curveT = cmds.radioButtonGrp('curveType', q=1, sl=1)
    goArc = cmds.checkBox('makeArc', q=1 ,v = 1)
    cClean = cmds.checkBox('cleanCurve', q=1 ,v = 1)
    selEdge = cmds.filterExpand(expand=True ,sm=32)
    selCurve = cmds.filterExpand(expand=True ,sm=9)
    if selCurve:
        if len(selEdge)>0 and len(selCurve)== 1:
            storeEdge = selEdge
            cmds.select(selCurve,d=1)
            selMeshForDeformer = cmds.ls(sl=1,o=1)
            getCircleState,listVtx = Xll()
            newCurve = cmds.duplicate(selCurve[0], rr=1)
            cmds.rename(newCurve[0],'newsnapCurve')
            currentArcCurve = 'newsnapCurve'
            cmds.rebuildCurve(currentArcCurve,ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = 100, d=1, tol=0.01)
            #check tip order
            curveTip = cmds.pointOnCurve(currentArcCurve , pr = 0, p=1)
            tipA = cmds.pointPosition(listVtx[0],w=1)
            tipB = cmds.pointPosition(listVtx[-1],w=1)
            distA = math.sqrt( ((tipA[0] - curveTip[0])**2)  + ((tipA[1] - curveTip[1])**2)  + ((tipA[2] - curveTip[2])**2) )
            distB = math.sqrt( ((tipB[0] - curveTip[0])**2)  + ((tipB[1] - curveTip[1])**2)  + ((tipB[2] - curveTip[2])**2) )
            if distA > distB:
                listVtx.reverse()
            #snap to curve
            if goEven == 1:
                for q in range(len(selEdge)+1):
                    if q == 0:
                        pp = cmds.pointOnCurve(currentArcCurve , pr = 0, p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[q] , a =True, ws=True)
                    else:
                        pp = cmds.pointOnCurve(currentArcCurve , pr = (1.0/len(selEdge)*q), p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[q] , a =True, ws=True)
            else:
                sum = 0
                totalEdgeLoopLength = 0
                Llist = []
                uList = []
                pList = []
                for i in range(len(listVtx)-1):
                    pA = cmds.pointPosition(listVtx[i], w =1)
                    pB = cmds.pointPosition(listVtx[i+1], w =1)
                    checkDistance = math.sqrt( ((pA[0] - pB[0])**2)  + ((pA[1] - pB[1])**2)  + ((pA[2] - pB[2])**2) )
                    Llist.append(checkDistance)
                    totalEdgeLoopLength = totalEdgeLoopLength + checkDistance

                for j in Llist:
                    sum = sum + j
                    uList.append(sum)
                for k in uList:
                    p = k / totalEdgeLoopLength
                    pList.append(p)

                for q in range(len(selEdge)+1):
                    if q == 0:
                        pp = cmds.pointOnCurve(currentArcCurve , pr = 0, p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[q] , a =True, ws=True)
                    else:
                        pp = cmds.pointOnCurve(currentArcCurve , pr = pList[q-1], p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[q] , a =True, ws=True)
            cmds.delete('newsnapCurve')
            deformerNames  = cmds.wire(selMeshForDeformer, gw=0, en = 1, ce = 0, li= 0, dds = [(0,1)], dt=1, w = selCurve[0])
            cmds.connectControl("dropOffSlider", (deformerNames[0]+".dropoffDistance[0]"))
            if snapCheck == 0:
                cmds.setAttr((deformerNames[0] + '.dropoffDistance[0]'),1)
            else:
                cmds.setAttr((deformerNames[0] + '.dropoffDistance[0]'),currentDropOff)
            currentArcCurve = selCurve[0]
            cmds.select(selCurve[0])
    else:
        if selEdge:
            storeEdge = selEdge
            if cClean == 0:
                if cmds.objExists('arcCurve*'):
                    X98()
            selMeshForDeformer = cmds.ls(sl=1,o=1)
            getCircleState,listVtx = Xll()
            deformerNames = []
            #make nurbs curve
            if getCircleState == 0: #Arc
                if goArc == 1:
                    midP = int(len(listVtx)/2)
                    cmds.move(0.01, 0, 0,selEdge[midP],r=1, cs=1 ,ls=1, wd =1)
                    p1 = cmds.pointPosition(listVtx[0], w =1)
                    p2 = cmds.pointPosition(listVtx[midP], w =1)
                    p3 = cmds.pointPosition(listVtx[-1], w =1)
                    newNode = cmds.createNode('makeThreePointCircularArc')
                    cmds.setAttr((newNode + '.pt1'), p1[0],  p1[1] , p1[2])
                    cmds.setAttr((newNode + '.pt2'), p2[0],  p2[1] , p2[2])
                    cmds.setAttr((newNode + '.pt3'), p3[0],  p3[1] , p3[2])
                    cmds.setAttr((newNode + '.d'), 3)
                    cmds.setAttr((newNode + '.s'), len(listVtx))
                    newCurve = cmds.createNode('nurbsCurve')
                    cmds.connectAttr((newNode+'.oc'), (newCurve+'.cr'))
                    cmds.delete(ch=1)
                    transformNode = cmds.listRelatives(newCurve, fullPath=True , parent=True )
                    cmds.select(transformNode)
                    cmds.rename(transformNode,'arcCurve0')
                    getNewNode = cmds.ls(sl=1)
                    currentArcCurve = getNewNode[0]
                    numberP = 0
                    if curveT == 2:#nubs curve
                        numberP = int(conP) - 3
                        if numberP < 1:
                            numberP = 1
                    else:
                        numberP = int(conP) -1
                    cmds.rebuildCurve(currentArcCurve,ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s= numberP, d=3, tol=0.01)
                else:
                    p1 = cmds.pointPosition(listVtx[0], w =1)
                    cmds.curve(d= 1, p=p1)
                    cmds.rename('arcCurve0')
                    getNewNode = cmds.ls(sl=1)
                    currentArcCurve = getNewNode[0]
                    for l in range(1,len(listVtx)):
                        p2 = cmds.pointPosition(listVtx[l], w =1)
                        cmds.curve(currentArcCurve, a= 1, d= 1, p=p2)
                    numberP = int(conP) -1
                    cmds.rebuildCurve(currentArcCurve,ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s= numberP, d=1, tol=0.01)
            else: #circle
                p1 = cmds.pointPosition(listVtx[0], w =1)
                cmds.curve(d= 1, p=p1)
                cmds.rename('arcCurve0')
                getNewNode = cmds.ls(sl=1)
                currentArcCurve = getNewNode[0]
                for l in range(1,len(listVtx)):
                    p2 = cmds.pointPosition(listVtx[l], w =1)
                    cmds.curve(currentArcCurve, a= 1, d= 1, p=p2)
                cmds.curve(currentArcCurve, a= 1, d= 1, p=p1)
                cmds.closeCurve(currentArcCurve,ch=0, ps=2, rpo=1, bb= 0.5, bki=0, p=0.1)
                conP = cmds.intSliderGrp('CPSlider',q=1 , v = True )
                numberP = int(conP)
                if numberP < 4:
                    numberP = 4
                    cmds.intSliderGrp('CPSlider',e=1 , v = 4 )
                cmds.rebuildCurve(currentArcCurve,ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = numberP, d=3, tol=0.01)
                ###########################################################################
            cmds.delete(currentArcCurve ,ch=1)
            totalEdgeLoopLength = 0;
            sum = 0
            Llist = []
            uList = []
            pList = []
            #cmds.select(selEdge)
            for i in range(len(listVtx)-1):
                pA = cmds.pointPosition(listVtx[i], w =1)
                pB = cmds.pointPosition(listVtx[i+1], w =1)
                checkDistance = math.sqrt( ((pA[0] - pB[0])**2)  + ((pA[1] - pB[1])**2)  + ((pA[2] - pB[2])**2) )
                Llist.append(checkDistance)
                totalEdgeLoopLength = totalEdgeLoopLength + checkDistance
            if goEven == 1:
                avg = totalEdgeLoopLength / (len(selEdge))
                for j in range(len(selEdge)):
                    sum = ((j+1)*avg)
                    uList.append(sum)
            else:
                for j in Llist:
                    sum = sum + j
                    uList.append(sum)
            for k in uList:
                p = k / totalEdgeLoopLength
                pList.append(p)
            #snap to curve
            if snapCheck == 1:
                for q in range(len(pList)):
                    if q+1 == len(listVtx):
                        pp = cmds.pointOnCurve(currentArcCurve, pr = 0, p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[0] , a =True, ws=True)
                    else:
                        pp = cmds.pointOnCurve(currentArcCurve , pr = pList[q], p=1)
                        cmds.move( pp[0], pp[1], pp[2],listVtx[q+1] , a =True, ws=True)
            #convert to Bezier Curve
            cmds.delete(currentArcCurve ,ch=1)
            cmds.select(currentArcCurve)
            if curveT == 1:
                cmds.nurbsCurveToBezier()
                if getCircleState == 1: #circle need to fix bug
                    cmds.closeCurve(currentArcCurve,ch=0, ps=2, rpo=1, bb= 0.5, bki=0, p=0.1)
                    cmds.closeCurve(currentArcCurve,ch=0, ps=2, rpo=1, bb= 0.5, bki=0, p=0.1)
            #wireWrap
            deformerNames  = cmds.wire( selMeshForDeformer, gw=0, en = 1, ce = 0, li= 0, dds = [(0,1)], dt=1, w = currentArcCurve)
            #select controllers
            if getCircleState == 0:
                cmds.setToolTo('moveSuperContext')
                degree = cmds.getAttr(currentArcCurve + '.degree')
                spans = cmds.getAttr(currentArcCurve + '.spans')
                numberCVs = degree + spans
                collect = []
                for x in range(int(numberCVs/3)-1):
                    g = currentArcCurve + '.cv[' + str((x+1)*3) + ']'
                    collect.append(g)
                cmds.select(collect ,r=1)

            else:
                cmds.select(currentArcCurve + '.cv[*]')
            cmd = 'doMenuNURBComponentSelection("' + currentArcCurve + '", "controlVertex");'
            mel.eval(cmd)
            cmds.connectControl("dropOffSlider", (deformerNames[0]+".dropoffDistance[0]"))
            if snapCheck == 0:
                cmds.setAttr((deformerNames[0] + '.dropoffDistance[0]'),1)
            else:
                cmds.setAttr((deformerNames[0] + '.dropoffDistance[0]'),currentDropOff)
            #add to viewport even in isolate mode
            for x in range(1,5):
                cmds.isolateSelect(('modelPanel' + str(x)), ado= currentArcCurve )

def X9I():# min point for Nurbs are 4 point
    goArc = cmds.checkBox('makeArc', q=1 ,v = 1)
    curveT = cmds.radioButtonGrp('curveType', q=1, sl=1)
    if goArc == 0:
        cmds.intSliderGrp('CPSlider', e=1, min= 4, v = 4 , fmx = 500)
    else:
        if curveT == 1:
            cmds.intSliderGrp('CPSlider', e=1, min= 2, v = 3, fmx = 500)
        else:
            cmds.intSliderGrp('CPSlider', e=1, min= 4, v = 4, fmx = 500)

def X77():
    snapCheck = cmds.checkBox('snapCurve',q = 1 ,v = 1)
    if snapCheck == 0 :
        cmds.checkBox('evenSpace', e=1 ,en=0)
    else:
        cmds.checkBox('evenSpace', e=1 ,en=1)

def X45():# min point for Nurbs are 4 point
    curveT = cmds.radioButtonGrp('curveType', q=1, sl=1)
    getCurrentV = cmds.intSliderGrp('CPSlider', q=1 ,v = 1 )
    if curveT == 2:
        cmds.intSliderGrp('CPSlider', e=1, min= 4 )
        if getCurrentV < 4:
            cmds.intSliderGrp('CPSlider', e=1, v= 4 )
    else:
        cmds.intSliderGrp('CPSlider', e=1, min= 2 )
        
def Xl2():
    check  = cmds.checkBox("evenRoundPivotSnap", q=1, value=1)
    if check == 1:
        cmds.radioButtonGrp("PivotSnapType", e=1, en=1)
    else:
        cmds.radioButtonGrp("PivotSnapType", e=1, en=0)
def X75(type):
    edgeRingList = cmds.ls(sl=1,fl=1)
    targetL = cmds.floatField('equalizerLength', q=1, value = 1)
    unwantRing = cmds.ls(cmds.polySelectSp(edgeRingList, q=1,ring=1),fl=1)
    cmds.ConvertSelectionToFaces()
    cmds.ConvertSelectionToEdgePerimeter()
    cmds.select(unwantRing,d=1)
    testLoopAB = X69()
    if len(testLoopAB) == 2:
        ringPA = cmds.ls(cmds.polyListComponentConversion(testLoopAB[0], tv=1),fl=1)
        ringPB = cmds.ls(cmds.polyListComponentConversion(testLoopAB[1], tv=1),fl=1)  
        for d in edgeRingList:
            listVtx = cmds.ls(cmds.polyListComponentConversion(d, tv=1),fl=1)
            pACheck = listVtx[0]
            pBCheck = listVtx[1]
            if pACheck in ringPA:
                pass
            else:
                pACheck = listVtx[1]
                pBCheck = listVtx[0]
            pA = cmds.pointPosition(pACheck, w=1)
            pB = cmds.pointPosition(pBCheck, w=1)
            checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
            if type == "A":
                cmds.scale((targetL/checkDistance) ,(targetL/checkDistance),(targetL/checkDistance), listVtx[0], p=[pA[0],pA[1],pA[2]],r=1)
            elif type == "B":
                cmds.scale((targetL/checkDistance) ,(targetL/checkDistance),(targetL/checkDistance), listVtx[1], p=[pB[0],pB[1],pB[2]],r=1)
            else:
                cmds.scale((targetL/checkDistance) ,(targetL/checkDistance),(targetL/checkDistance), listVtx[0], p=[((pA[0]+pB[0])/2),((pA[1]+pB[1])/2),((pA[2]+pB[2])/2)],r=1)
                cmds.scale((targetL/checkDistance) ,(targetL/checkDistance),(targetL/checkDistance), listVtx[1], p=[((pA[0]+pB[0])/2),((pA[1]+pB[1])/2),((pA[2]+pB[2])/2)],r=1)
            cmds.select(edgeRingList)     
def X76(Where):
    selEdge = cmds.ls(sl=1,fl=1)
    length = X52(selEdge[0])
    output = round(length, 3)
    if Where == 'RE':
        cmds.floatField('equalizerLength', e=True, v=output)
    elif Where == 'IbL':
        cmds.floatField('refInsertLength', e=True, v=output)
    
def X58():
    if cmds.objExists('edgeSave'):
        cmds.delete('edgeSav*')
    currentV = cmds.floatSliderGrp('lockEdgeSlider', q=True, v=True)
    type = cmds.radioButtonGrp('lockEdgeType', q=True, sl=True)
    if type == 1:
        X73()
    else:
        XOI()
    cmds.floatSliderGrp('lockEdgeSlider', e=True, v=currentV)

def X25():
    if cmds.objExists('edgeSave'):
        cmds.delete('edgeSav*')
    currentV = cmds.floatSliderGrp('lockEdgeSlider', q=True, v=True)
    type = cmds.radioButtonGrp('lockEdgeType', q=True, sl=True)
    if type == 1:
        X85()
    else:
        X27()
    cmds.floatSliderGrp('lockEdgeSlider', e=True, v=currentV)

def X73():
    lockLength = cmds.floatField('lastLockEdgelength', q=True, v=True)
    X85()
    X65(lockLength)
    cmds.select(d=True)

def X65(targetEdgeLength):
    global polySRA
    global polySRB
    global AEdge
    global BEdge
    ADis = X52(AEdge[0])
    currentW = cmds.getAttr(polySRA[0] +" .weight")
    newW = currentW * targetEdgeLength / ADis
    cmds.floatSliderGrp('lockEdgeSlider', e=True, v=currentW)
    cmds.setAttr( (polySRA[0] + ".weight"), newW)
    ADis = X52(AEdge[0])
    BDis = X52(BEdge[0])
    currentW = cmds.getAttr(polySRB[0]+".weight")
    newW = 1 - (ADis * (1.0 - currentW) / BDis)
    cmds.setAttr( (polySRB[0] + ".weight"), newW)
    cmds.floatField('lastLockEdgelength', e=True, v = targetEdgeLength)


def XOI():
    global myLockEdge
    myLockEdge = []
    selectedgelock = cmds.ls(sl=True)
    selectGeo = cmds.ls(hl=True)
    cmds.bakePartialHistory(all=True)
    lockLength = cmds.floatField('lastLockEdgelength', q=True, v=True)
    length = X52(selectedgelock[0])
    halfL = length / 2.0
    checkN = lockLength / halfL
    lockL = 1.0 - checkN
    if lockL > 0:
        cmds.sets(name="edgeSave", text="edgeSave")
        cmds.select(selectedgelock[0], r=True)
        cmds.polySelectSp(ring=True)
        cmds.polySplitRing(ch=0, splitType=2, divisions=1)
        locknodeLst = cmds.polyDuplicateEdge(of=lockL, ch=True)
        cmds.rename(locknodeLst[0], "lockEdges")
        cmds.polyDelEdge(cv=True)
        cmds.select('edgeSave', r=True)
        X82('min')
        myLockEdge = cmds.ls(sl=True, fl=True)
        cmds.delete('edgeSave')
        cmds.select(d=True)
        cmds.connectControl('lockEdgeSlider', 'lockEdges.of')
    else:
        cmds.select(selectedgelock[0], r=True)
        X6l()
        print("length longer than current egde!") 

def X85():
    cmds.floatSliderGrp('lockEdgeSlider', e=True, en=1)
    global myLockEdge
    global polySRA
    global polySRB
    global AEdge
    global BEdge
    myLockEdge = []
    polySRA = []
    polySRB = []
    AEdge = []
    BEdge = []
    cmds.bakePartialHistory(all=True) 
    cmds.polySelectSp(ring=True)
    X82('min')
    cmds.sets(name="edgeSave", text="edgeSave")
    edgeData = XI2()
    cmds.polySelectSp(ring=True)
    polySRA = cmds.polySplitRing(ch=True, splitType=0, weight=0.01, smoothingAngle=30, fixQuads=True, insertWithEdgeFlow=False, direction=1, rootEdge=int(edgeData[1]))
    cmds.select('edgeSave', r=True)
    X82('max')
    edgeData = XI2()
    cmds.polySelectSp(ring=True)
    polySRB = cmds.polySplitRing(ch=True, splitType=0, weight=0.99, smoothingAngle=30, fixQuads=True, insertWithEdgeFlow=False, direction=0, rootEdge=int(edgeData[1]))
    cmds.select('edgeSave', r=True)
    X82('max')
    midEdge = cmds.ls(sl=True, fl=True)
    cmds.select('edgeSave', r=True)
    cmds.select(midEdge, d=True)
    X82('max')
    AEdge = cmds.ls(sl=True, fl=True)
    myLockEdge = cmds.ls(sl=True, fl=True)
    cmds.select('edgeSave', r=True)
    cmds.select(midEdge, d=True)
    cmds.select(AEdge, d=True)
    BEdge = cmds.ls(sl=True, fl=True)
    cmds.delete('edgeSave')
    cmds.select(d=True)
    X36()


def X6l():
    cmds.ConvertSelectionToEdges()
    current = cmds.ls(sl=True)
    if current:
        tokens = current[0].split(".")
        cmds.selectType(edge=True)
        cmds.select(tokens[0], r=True, ne=True)
        cmds.select(current, r=True)
        cmd  = 'doMenuComponentSelectionExt("' + tokens[0] + '", "edge", 0);'
        mel.eval(cmd)

def X27():
    global myLockEdge
    myLockEdge = []
    selectedgelock = cmds.ls(sl=True)
    selectGeo = cmds.ls(hl=True)
    cmds.sets(name="edgeSave", text="edgeSave")
    cmds.bakePartialHistory(all=True)
    Lock = cmds.floatSliderGrp('lockEdgeSlider', q=True, v=True)
    length = X52(selectedgelock[0])
    cmds.polySelectSp(ring=True)
    cmds.polySplitRing(ch=0, splitType=2, divisions=1)
    locknodeLst = cmds.polyDuplicateEdge(of=Lock, ch=True)
    cmds.rename(locknodeLst[0], "lockEdges")
    cmds.polyDelEdge(cv=True)
    cmds.select(selectGeo[0], r=True)
    X6l()
    cmds.InvertSelection()
    cmds.select('edgeSave', r=True)
    X82('min')
    myLockEdge = cmds.ls(sl=True, fl=True)
    cmds.delete('edgeSave')
    cmds.select(d=True)
    cmds.connectControl('lockEdgeSlider', 'lockEdges.of')
    
def X24():
    global myLockEdge
    length = X52(myLockEdge[0])
    output = round(length, 3)
    cmds.floatField('lastLockEdgelength', e=True, v=output)

def XI2():
    startEdge = cmds.ls(sl=True, fl=True)
    buffer = startEdge[0].split(".")
    Edgebuffer = buffer[1].split("[")
    getNumber = Edgebuffer[1].split("]")
    return buffer[0], getNumber[0]

def X36():
    type = cmds.radioButtonGrp('lockEdgeType', q=True, sl=True)
    if type == 1:
        Lock = cmds.floatSliderGrp('lockEdgeSlider', q=True, v=True)
        global polySRA
        global polySRB
        global AEdge
        global BEdge
        errorCheck = (1 - Lock) / 2.0
        if 0.001 < errorCheck < 0.4999:
            cmds.setAttr((polySRA[0] +".weight"), errorCheck)
            currentW = cmds.getAttr(polySRB[0]+".weight")
            ADis = X52(AEdge[0])
            BDis = X52(BEdge[0])
            newW = 1 - (ADis * (1.0 - currentW) / BDis)
            cmds.setAttr((polySRB[0] + ".weight"), newW)
    X24()

def X82(minmax):
    value = 0 if minmax == "max" else float('inf')
    selection = cmds.ls(sl=True, fl=True)
    edges = cmds.filterExpand(selection, ex=True, sm=32)
    if not edges:
        raise ValueError("No valid Edges selected!")
    targetEdge = None
    for edge in edges:
        checkEdgeLength = X52(edge)
        if minmax == "max" and checkEdgeLength > value:
            value = checkEdgeLength
            targetEdge = edge
        elif minmax == "min" and checkEdgeLength < value:
            value = checkEdgeLength
            targetEdge = edge
    
    if targetEdge:
        cmds.select(targetEdge)
    else:
        raise ValueError("No edge found matching the criteria.")

def X52(edge):
    vertices = cmds.polyListComponentConversion(edge, toVertex=True)
    vertices = cmds.filterExpand(vertices, sm=31)
    length = X89(vertices[0], vertices[1])
    return length

def X89(vertex1, vertex2):
    v1 = cmds.pointPosition(vertex1, w=True)
    v2 = cmds.pointPosition(vertex2, w=True)
    distance = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2)
    return distance

def XO3():
    keepCheckBox = cmds.checkBox('keepSpliteNumber', q=True, v=True)
    keepInsertNumber = cmds.floatSliderGrp('multiInsertNo', q=True, v=True)
    selectedEdges = cmds.ls(sl=True, fl=True)
    polySplitRingNodes = cmds.ls(type='polySplitRing')
    cmds.floatSliderGrp('multiInsertNo', e=True, v=1)
    polySRList = []
    obj = cmds.ls(hl=True)
    if polySplitRingNodes:
        cmds.select(obj)
        cmds.delete(ch=True)
    if len(selectedEdges) == 1:
        cmds.select(selectedEdges)
        cmds.polySelectSp(ring=True)
        nodeLst = cmds.polySplitRing(ch=True, splitType=2, divisions=1, useEqualMultiplier=True, smoothingAngle=30, fixQuads=False)
        cmds.connectControl('multiInsertNo', nodeLst[0] + ".div")
        if keepCheckBox:
            cmds.setAttr(nodeLst[0] + ".div", keepInsertNumber)
            cmds.floatSliderGrp('multiInsertNo', e=True, v=keepInsertNumber)
    elif len(selectedEdges) > 1:
        confirmString = cmds.confirmDialog(title="Confirm", message="Warning!! More than one edge selected?", button=["Continues", "Abort"], defaultButton="Abort", cancelButton="Abort", dismissString="Abort")
        if confirmString == "Continues":
            for s in selectedEdges:
                cmds.select(s)
                cmds.polySelectSp(ring=True)
                nodeLst = cmds.polySplitRing(ch=True, splitType=2, divisions=1, useEqualMultiplier=True, smoothingAngle=30, fixQuads=False)
                polySRList.append(nodeLst[0] + ".div")
            collectList = ['"{}"'.format(p) for p in polySRList]
            getList = ','.join(collectList)
            cmd = "cmds.connectControl('multiInsertNo', {})".format(getList)
            eval(cmd)
            if keepCheckBox:
                cmds.floatSliderGrp('multiInsertNo', e=True, v=keepInsertNumber)
                for p in polySRList:
                    cmds.setAttr(p, keepInsertNumber)
        cmds.select(cl=True)
    if obj:
        cmd = 'doMenuComponentSelection("' + obj[0]  +'", "edge");'
        mel.eval(cmd)
        
def X2l(location, curveObject):
    curve = curveObject
    tempList = om.MSelectionList()
    tempList.add(curve)
    curveObj = om.MObject()
    tempList.getDependNode(0, curveObj)
    dagpath = om.MDagPath()
    tempList.getDagPath(0, dagpath)
    curveMF = om.MFnNurbsCurve(dagpath)
    point = om.MPoint( location[0], location[1], location[2])
    prm = om.MScriptUtil()
    pointer = prm.asDoublePtr()
    om.MScriptUtil.setDouble (pointer, 0.0)
    tolerance = .001
    space = om.MSpace.kObject
    result = om.MPoint()
    result = curveMF.closestPoint (point, pointer,  0.0, space)
    parameter = om.MScriptUtil.getDouble (pointer)
    return [parameter, (result.x), (result.y), (result.z)]
    
def X39(SX, SY):
    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()
    omui.M3dView().active3dView().viewToWorld(int(SX), int(SY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    checkCam = X68()
    finalX = []
    finalY = []
    finalZ = []
    checkList = []
    checkList.append('refPlane')
    for mesh in checkList:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)
        intersection = fnMesh.closestIntersection(om.MFloatPoint(pos2), om.MFloatVector(dir), None, None, False, om.MSpace.kWorld, 99999, False, None, hitpoint, None, None, None, None, None)
        if intersection:
            finalX = hitpoint.x
            finalY = hitpoint.y
            finalZ = hitpoint.z
    return (finalX, finalY, finalZ)
    
def X49(pointName):
    view = omuia.M3dView.active3dView()
    posInView = []
    ppos = cmds.pointPosition(pointName, w=1)
    posInView.append(view.worldToView(oma.MPoint(ppos)))
    vpos = view.worldToView(oma.MPoint(ppos))
    wx, wy, wz = X39(vpos[0], vpos[1])
    return (wx, wy, wz)
    
def Xl3(cameraName, worldPoint):
    resWidth, resHeight = X34()
    selList = om.MSelectionList()
    selList.add(cameraName)
    dagPath = om.MDagPath()
    selList.getDagPath(0, dagPath)
    dagPath.extendToShape()
    camInvMtx = dagPath.inclusiveMatrix().inverse()
    fnCam = om.MFnCamera(dagPath)
    mFloatMtx = fnCam.projectionMatrix()
    projMtx = om.MMatrix(mFloatMtx.matrix)
    mPoint = om.MPoint(worldPoint[0], worldPoint[1], worldPoint[2]) * camInvMtx * projMtx
    x = (mPoint[0] / mPoint[3] / 2 + 0.5) * resWidth
    y = (mPoint[1] / mPoint[3] / 2 + 0.5) * resHeight
    return [x, y]
    
def X34():
    windowUnder = cmds.getPanel(withFocus=True)
    if 'modelPanel' not in windowUnder:
        windowUnder = 'modelPanel4'
    viewNow = omui.M3dView.active3dView()
    omui.M3dView.getM3dViewFromModelEditor(windowUnder, viewNow)
    screenW = omui.M3dView.portWidth(viewNow)
    screenH = omui.M3dView.portHeight(viewNow)
    return (screenW, screenH)
    
def X55(tX, tY, tZ):
    checkCam = X68()
    resWidth, resHeight = X34()
    ratio = cmds.getAttr('defaultResolution.deviceAspectRatio')
    cmds.polyPlane(w=ratio, h=1, sx=40, sy=20, ax=(0, 0, 1), cuv=2, ch=1)
    cmds.rename('refPlane')
    cmds.setAttr('refPlane.visibility', 0)
    cmds.parentConstraint(checkCam, 'refPlane', weight=1)
    cmds.delete(constraints=True)
    cmds.setAttr('refPlane.translateX', tX)
    cmds.setAttr('refPlane.translateY', tY)
    cmds.setAttr('refPlane.translateZ', tZ)
    head3d = cmds.pointPosition('refPlane.vtx[0]')
    tail3d = cmds.pointPosition('refPlane.vtx[860]')
    head2D = Xl3(checkCam, (head3d[0], head3d[1], head3d[2]))
    tail2d = Xl3(checkCam, (tail3d[0], tail3d[1], tail3d[2]))
    distanceX = tail2d[0] - head2D[0]
    distanceY = tail2d[1] - head2D[1]
    cmds.setAttr('refPlane.scaleX', resWidth / distanceX * 2)
    cmds.setAttr('refPlane.scaleY', resHeight / distanceY * 2)
    
def X68():
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath, type='transform', p=True)
    cameraPosition = cmds.xform(cameraTrans, q=1, ws=1, rp=1)
    return cameraTrans[0]
    
def Xo7(edgeList):
    listEvenVtx = X8I(edgeList)
    if cmds.objExists('tempEvenCurve'):
        cmds.delete('tempEvenCurve')
    cmds.select(edgeList)
    cmds.polyToCurve(form=2, degree=1, conformToSmoothMeshPreview=1)
    cmds.rename('tempEvenCurve')
    curveCVs =cmds.ls('tempEvenCurve.cv[*]',fl=1)
    posCurve = cmds.xform(curveCVs[0], a=1,ws=1, q=1, t=1)
    posEdge = cmds.xform(listEvenVtx[0], a=1,ws=1, q=1, t=1)
    if posCurve == posEdge:
        pass
    else:
        listEvenVtx = listEvenVtx[::-1]
    cmds.rebuildCurve('tempEvenCurve',ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = 0 , d=1, tol=0)
    cmds.rebuildCurve('tempEvenCurve',ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = 0 , d=1, tol=0)
    if len(curveCVs)< 4:
        cmds.delete( 'tempEvenCurve.cv[1]', 'tempEvenCurve.cv[3]')
        curveCVs =cmds.ls('tempEvenCurve.cv[*]',fl=1)
    for i in range(len(curveCVs)):
        pos = cmds.xform(curveCVs[i], a=1,ws=1, q=1, t=1)
        cmds.xform(listEvenVtx[i], a=1, ws=1, t = (pos[0],pos[1],pos[2]) )
    cmds.delete('tempEvenCurve')
    
def X94():
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        X29(e)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)

def X29(flatList):
    X2I()
    listVtx = X8I(flatList)
    cmds.select(flatList)
    cmds.polyToCurve(form=0, degree=1, conformToSmoothMeshPreview=1,)
    cmds.rename('newguildcurve')
    cmds.delete('newguildcurve',  e=1, ch=1)
    cmd = 'modifySelectedCurves smooth 1 0;'
    mel.eval(cmd)
    xA, yA, zA = cmds.pointPosition(listVtx[0], w=1)
    xA =  round(xA,3)
    yA =  round(yA,3)
    zA =  round(zA,3)
    xC, yC, zC = cmds.pointPosition('newguildcurve.cv[0]',w=1)
    xC =  round(xC,3)
    yC =  round(yC,3)
    zC =  round(zC,3)
    if xA == xC and yA == yC and zA == zC:
       pass
    else:
        listVtx.reverse()
    for i in range(1,len(listVtx)-1):
        xD, yD, zD = cmds.pointPosition('newguildcurve.cv['+str(i)+']',w=1)
        cmds.move(xD, yD, zD,listVtx[i] , a =True, ws=True)
    X2I()

def X47(mode):
    if mode == 3:
        cmds.iconTextButton('button2DIcon' ,e=1 ,bgc =  [0.18,0.18,0.18] )
        cmds.iconTextButton('button3DIcon' ,e=1 ,bgc =  [0.5, 0.21, 0] )
    elif mode ==2:
        cmds.iconTextButton('button2DIcon' ,e=1 ,bgc =  [0.5, 0.21, 0] )
        cmds.iconTextButton('button3DIcon' ,e=1 ,bgc =  [0.18,0.18,0.18] )

def Xoo(level):
    checkMode = cmds.iconTextButton('button2DIcon' ,q=1 ,bgc = 1 )
    if checkMode[2] > 0:
        X9l(level)
    else:
        Xl8(level)

def Xl8(level):
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        X63(e,level)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)

def X63(flatList,level):
    numberPoint = level
    X2I()
    listVtx = X8I(flatList)
    checkCam = X68()
    closetP2Cam = []
    shortDistance = 10000000000
    cameraPosition = cmds.xform(checkCam, q=1, ws=1, rp=1)
    for g in listVtx:
        x, y, z = cmds.pointPosition(g, w=1)
        distanceBetween = math.sqrt((float(cameraPosition[0]) - x) ** 2 + (float(cameraPosition[1]) - y) ** 2 + (float(cameraPosition[2]) - z) ** 2)
        if distanceBetween < shortDistance:
            shortDistance = distanceBetween
            closetP2Cam = g
    tX, tY, tZ = cmds.pointPosition(closetP2Cam, w=1)
    X55(tX, tY, tZ)
    pointDict = []
    for g in listVtx:
        pos = X49(g)
        pointDict.append(pos)
    cmds.curve(d=1, p=[(pointDict[0][0], pointDict[0][1], pointDict[0][2]), (pointDict[-1][0], pointDict[-1][1], pointDict[-1][2])])
    cmds.rename('newguildcurve')
    if numberPoint == 1:
        cmds.rebuildCurve('newguildcurve', ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=1, d=3, tol=0)
        gap = int(len(listVtx) * 0.5)
        cmds.select('newguildcurve.cv[1]', 'newguildcurve.cv[2]')
        nodeCluster = cmds.cluster(n= 'midGrp')
        cmds.move(pointDict[gap][0], pointDict[gap][1], pointDict[gap][2], nodeCluster[1], rpr=True)
    elif numberPoint == 2:
        cmds.rebuildCurve('newguildcurve', ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=2, d=2, tol=0)
        gapA = int(len(listVtx) * 0.33333)
        gapB = int(len(listVtx) * 0.66666)
        cmds.move(pointDict[gapA][0], pointDict[gapA][1], pointDict[gapA][2], 'newguildcurve.cv[1]', rpr=True)
        cmds.move(pointDict[gapB][0], pointDict[gapB][1], pointDict[gapB][2], 'newguildcurve.cv[2]', rpr=True)
    elif numberPoint == 3:
        cmds.rebuildCurve('newguildcurve', ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=3, d=2, tol=0)
        gapA = int(len(listVtx) * 0.25)
        gapB = int(len(listVtx) * 0.5)
        gapC = int(len(listVtx) * 0.75)
        cmds.move(pointDict[gapA][0], pointDict[gapA][1], pointDict[gapA][2], 'newguildcurve.cv[1]', rpr=True)
        cmds.move(pointDict[gapB][0], pointDict[gapB][1], pointDict[gapB][2], 'newguildcurve.cv[2]', rpr=True)
        cmds.move(pointDict[gapC][0], pointDict[gapC][1], pointDict[gapC][2], 'newguildcurve.cv[3]', rpr=True)
    cmds.delete('newguildcurve', ch=1)
    cmds.move(cameraPosition[0], cameraPosition[1], cameraPosition[2], 'newguildcurve.scalePivot', 'newguildcurve.rotatePivot')
    cmds.duplicate('newguildcurve')
    cmds.setAttr('newguildcurve.scaleX', 0.5)
    cmds.setAttr('newguildcurve.scaleY', 0.5)
    cmds.setAttr('newguildcurve.scaleZ', 0.5)
    cmds.setAttr('newguildcurve1.scaleX', 2)
    cmds.setAttr('newguildcurve1.scaleY', 2)
    cmds.setAttr('newguildcurve1.scaleZ', 2)
    cmds.nurbsToPolygonsPref(polyType=1, format=3, uType=3, uNumber=1, vType=3, vNumber=1)
    loftNode = cmds.loft('newguildcurve1', 'newguildcurve', ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=1, rsn=True)
    cmds.rename('guildMesh')
    cmds.polySmooth('guildMesh', mth=0, sdt=2, ovb=1, ofb=3, ofc=0, ost=0, ocr=0, dv=2, bnr=1, c=1, kb=1, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=0)
    cmds.transferAttributes('guildMesh', listVtx, transferPositions=1, searchMethod=3)
    shapesNode = cmds.listRelatives(listVtx[0], shapes=True, ap=True)
    cmds.delete(shapesNode, ch=1)
    X2I()
def X2I():
    cleanSceneList = {'refPlan*','newguildcurv*','newguildcurv*','guildMes*','baseLo*','newDeformcurv*'}
    for c in cleanSceneList:
        if cmds.objExists(c):
            cmds.delete(c)
def X9l(level):
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        X54(e,level)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
def X54(flatList,level):
    checkEven = cmds.checkBox('evenCurveEdgeLength', q=1,v=1)
    X2I()
    listVtx = X8I(flatList)
    numberPoint = level
    distList = []
    totalDist = 0
    xA, yA, zA = cmds.pointPosition(listVtx[0], w=1)
    xB, yB, zB = cmds.pointPosition(listVtx[-1], w=1)
    cmds.curve(d=1, p=[(xA, yA, zA),(xB, yB, zB)])
    cmds.rename('newguildcurve')
    for i in range(len(listVtx)-1):
        xA, yA, zA = cmds.pointPosition(listVtx[i], w=1)
        xB, yB, zB = cmds.pointPosition(listVtx[i+1], w=1)
        distanceBetween = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB) + (zA - zB) * (zA - zB))
        distList.append(distanceBetween)
        totalDist = totalDist + distanceBetween
    if numberPoint == 1:
        cmds.rebuildCurve('newguildcurve', ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=1, d=3, tol=0)
        gapA = int(len(listVtx) * 0.5)
        xA, yA, zA = cmds.pointPosition(listVtx[gapA], w=1)
        cmds.select('newguildcurve.cv[1]','newguildcurve.cv[2]')
        nodeCluster = cmds.cluster(n= 'midGrp')
        cmds.spaceLocator(n='baseLoc')
        cmds.select('baseLoc',nodeCluster[1])
        cmds.matchTransform()
        cmds.move( xA, yA, zA, nodeCluster[1], rpr =1)
        cmds.select(nodeCluster[1],'baseLoc')
        cmds.parent()
        cmds.setAttr("baseLoc.scale", 1.33, 1.33, 1.33)
    elif numberPoint == 2:
        cmds.rebuildCurve('newguildcurve', ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=2, d=2, tol=0)
        gapA = int(len(listVtx) * 0.33333)
        gapB = int(len(listVtx) * 0.66666)
        xA, yA, zA = cmds.pointPosition(listVtx[gapA], w=1)
        xB, yB, zB = cmds.pointPosition(listVtx[gapB ], w=1)
        cmds.move( xA, yA, zA, 'newguildcurve.cv[1]', a =True, ws=True)
        cmds.move( xB, yB, zB, 'newguildcurve.cv[2]', a =True, ws=True)
    elif numberPoint == 3:
        cmds.rebuildCurve('newguildcurve', ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=3, d=2, tol=0)
        gapA = int(len(listVtx) * 0.25)
        gapB = int(len(listVtx) * 0.5)
        gapC = int(len(listVtx) * 0.75)
        xA, yA, zA = cmds.pointPosition(listVtx[gapA], w=1)
        xB, yB, zB = cmds.pointPosition(listVtx[gapB ], w=1)
        xC, yC, zC = cmds.pointPosition(listVtx[gapC ], w=1)
        cmds.move( xA, yA, zA, 'newguildcurve.cv[1]', a =True, ws=True)
        cmds.move( xB, yB, zB, 'newguildcurve.cv[2]', a =True, ws=True)
        cmds.move( xC, yC, zC, 'newguildcurve.cv[3]', a =True, ws=True)
    cmds.rebuildCurve('newguildcurve', ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=100, d=3, tol=0)
    currentU = 0
    prV = 0
    gapDist = 1.0/(len(listVtx)-1)
    scaleV = 1/totalDist
    for j in range(len(listVtx)-2):
        if checkEven == 1:
            prV = currentU + gapDist
        else:
            prV = currentU + (scaleV * distList[j])
        currentU = prV
        xj, yj, zj = cmds.pointOnCurve('newguildcurve', pr= currentU, p=1)
        cmds.move(xj, yj, zj,listVtx[j+1] , a =True, ws=True)

    X2I()

def X3l(dir,startMode):
    global edgeCurlRunMoveCV
    global edgeCurlRunSel
    global edgeCurlRunDistList
    global startModeRecord
    startModeRecord = startMode
    modifiers = 0
    if startMode == 0:
        modifiers = cmds.getModifiers()
    elif startMode == 1:
        modifiers = 1
    elif startMode == 4:
        modifiers = 4
    elif startMode == 100:
        modifiers = 0
    edgeCurlRunDistList = []
    edgeCurlRunSel = []
    edgeCurlRunMoveCV = []
    checkEndCV = []
    distList = []
    edgeSel = cmds.ls(sl=1,fl=1)
    if len(edgeSel) == 1:
        cmds.ConvertSelectionToVertices()
        selectsCV = cmds.ls(sl=1,fl=1)
        cmds.select(edgeSel)
        cmds.SelectEdgeLoopSp()
        cmds.ConvertSelectionToVertices()
        loopCVList = cmds.ls(sl=1,fl=1)
        cmds.select(selectsCV)
        cmds.ConvertSelectionToEdges()
        cmds.ConvertSelectionToVertices()
        surroundCV = cmds.ls(sl=1,fl=1)
        commonList = list(set(surroundCV) & set(loopCVList))
        cmds.select(commonList)
        cmds.ConvertSelectionToContainedEdges()
        checkConnerEdge = cmds.ls(sl=1,fl=1)
        if len(checkConnerEdge) == 3:
            cmds.ConvertSelectionToFaces()
            checkConnerFace = cmds.ls(sl=1,fl=1)
            if len(checkConnerFace)==2:
                cmds.select(edgeSel)
                cmds.GrowLoopPolygonSelectionRegion()
            elif len(checkConnerFace) > 2:
                cmds.select(checkConnerEdge)
    else:
        cmds.setToolTo( 'moveSuperContext' )
    getCircleState,listVtx = Xll()
    if getCircleState == 0:
        edgeCurlRunSel = edgeSel
        cleanList = ('tempGuid*','arcCurv*','upperLo*','aimLo*','baseLo*','makeThreePointCircularAr*','tempGuideLin*')
        for c in cleanList:
            if cmds.objExists(c):
                cmds.delete(c)
        leftCV = ''
        rightCV = ''
        view = omui.M3dView.active3dView()
        cam = om.MDagPath()
        view.getCamera(cam)
        camPath = cam.fullPathName()
        cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
        CurrentCam = cameraTrans[0]
        xA, yA, zA = cmds.pointPosition(listVtx[0], w=1)
        A2D = Xl3(cameraTrans[0], (xA,yA,zA))
        xB, yB, zB = cmds.pointPosition(listVtx[-1], w=1)
        B2D = Xl3(cameraTrans[0], (xB,yB,zB))
        if A2D[0] < B2D[0]:
            leftCV = listVtx[0]
            rightCV = listVtx[-1]
        else:
            rightCV = listVtx[0]
            leftCV = listVtx[-1]
        if leftCV == listVtx[-1]:
            listVtx.reverse()
        if dir == 'L':
            listVtx.reverse()
        if len(edgeSel) == 1:
            xA, yA, zA = cmds.pointPosition(listVtx[-1], w=1)
            xB, yB, zB = cmds.pointPosition(listVtx[-2], w=1)
            distanceBetween = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB) + (zA - zB) * (zA - zB))
            distList.append(distanceBetween)
        elif len(edgeSel) > 2:
            distList = []
            for i in range(len(listVtx)-1):
                xA, yA, zA = cmds.pointPosition(listVtx[i], w=1)
                xB, yB, zB = cmds.pointPosition(listVtx[i+1], w=1)
                distanceBetween = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB) + (zA - zB) * (zA - zB))
                distList.append(distanceBetween)
        edgeCurlRunDistList = distList
        firstCV = listVtx[0]
        secCV = listVtx[1]
        thirdCV = ''
        if len(edgeSel) == 1:
            thirdCV = listVtx[2]
        else:
            thirdCV = listVtx[-1]
        edgeCurlRunMoveCV = listVtx
        if startMode != 100:
            p1 = cmds.pointPosition(firstCV, w=1)
            p2 = cmds.pointPosition(secCV, w=1)
            p3 = cmds.pointPosition(thirdCV, w=1)
            newNode = cmds.createNode('makeThreePointCircularArc')
            cmds.setAttr(newNode + '.pt1', p1[0], p1[1], p1[2])
            cmds.setAttr(newNode + '.pt2', p2[0], p2[1], p2[2])
            cmds.setAttr(newNode + '.pt3', p3[0], p3[1], p3[2])
            cmds.setAttr(newNode + '.d', 3)
            cmds.setAttr(newNode + '.s', 4)
            newCurve = cmds.createNode('nurbsCurve')
            cmds.select(cl=1)
            cmds.connectAttr(newNode + '.oc', newCurve + '.cr')
            transformNode = cmds.listRelatives(newCurve, fullPath=True, parent=True)
            cmds.rename(transformNode, 'arcCurve')
            cmd = 'doMenuComponentSelection("' + edgeCurlRunMoveCV[0].split('.')[0] +'", "edge");'
            mel.eval(cmd)
            cmds.select(edgeSel)
            cmds.refresh(f=True)
            cPos = cmds.getAttr( newNode +'.center')
            cmds.move( cPos[0][0],  cPos[0][1],  cPos[0][2],'arcCurve.scalePivot' ,'arcCurve.rotatePivot' , a =True, ws=True)
            cmds.delete(ch=1)
            circleR =  math.sqrt((p1[0] - cPos[0][0]) * (p1[0]  - cPos[0][0]) + (p1[1]  - cPos[0][1]) * (p1[1]  - cPos[0][1]) + (p1[2]  - cPos[0][2]) * (p1[2]  - cPos[0][2]))
            cmds.spaceLocator(n='upperLoc')
            cmds.spaceLocator(n='aimLoc')
            cmds.spaceLocator(n='baseLoc')
            cmds.select('upperLoc','aimLoc','baseLoc')
            cmds.CenterPivot()
            cmds.setAttr(('upperLoc.scale'),0.01,0.01,0.01)
            cmds.setAttr(('aimLoc.scale'),0.01,0.01,0.01)
            cmds.setAttr(('aimLoc.translate'),0, 1,-1)
            cmds.setAttr(('upperLoc.translate'),0, 1,1)
            consNode = cmds.aimConstraint('aimLoc','baseLoc',offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType='object', worldUpObject='upperLoc')
            cmds.setAttr(('baseLoc.translate'),cPos[0][0], cPos[0][1], cPos[0][2])
            cmds.setAttr(('aimLoc.translate'),p3[0], p3[1], p3[2])
            cmds.setAttr(('upperLoc.translate'),p1[0], p1[1], p1[2])
            cmds.circle( nr=(0, 0, 1), c=(0, 0, 0),r= circleR,n='tempGuide')
            cmds.displaySmoothness(divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3)
            cmds.setAttr("tempGuideShape.overrideEnabled", 1)
            cmds.setAttr("tempGuideShape.overrideColor",31)
            cmds.select('tempGuide','baseLoc')
            cmds.matchTransform()
            cmds.select('baseLoc',d=1)
            cmds.makeIdentity('tempGuide', apply=1, t=1,r=1,s=1)
            cmds.ReverseCurve()
            cmds.delete(ch=1)
            cmds.move(  p2[0],   p2[1],   p2[2],'tempGuide.scalePivot' ,'tempGuide.rotatePivot' , a =True, ws=True)
        else:
            if len(edgeSel) == 1:
                cmds.select(edgeSel)
            else:
                cmds.select(edgeCurlRunMoveCV[0],edgeCurlRunMoveCV[1])
                cmds.ConvertSelectionToContainedEdges()
            cmds.polyToCurve(form=0, degree=1, conformToSmoothMeshPreview=1)
            cmds.rename('tempGuide')
            cmds.CenterPivot()
            cmds.ReverseCurve()
            cmds.delete(ch=1)
            cmds.setAttr("tempGuide.scale",50,50,50)
            cmds.makeIdentity('tempGuide', apply=1, t=1,r=1,s=1)
        checkLock = cmds.checkBox('lockCurveEdgeLength', q=1,v=1)
        checkEven = cmds.checkBox('evenCurveEdgeLength', q=1,v=1)
        if startMode == 100:
            xA, yA, zA = cmds.pointPosition('tempGuide.cv[0]', w=1)
            A2D = Xl3(cameraTrans[0], (xA,yA,zA))
            xB, yB, zB = cmds.pointPosition('tempGuide.cv[1]', w=1)
            B2D = Xl3(cameraTrans[0], (xB,yB,zB))
            if A2D[0] > B2D[0]:
                cmds.select('tempGuide')
                cmds.ReverseCurve()
            if dir == 'L':
                cmds.select('tempGuide')
                cmds.ReverseCurve()
            if checkEven == 1 and len(edgeSel) > 1:
                Xo7(edgeSel)
            if checkLock == 0:
                selectionList = om.MSelectionList()
                selectionList.add('tempGuide')
                dagPath = om.MDagPath()
                selectionList.getDagPath(0, dagPath)
                omCurveOut = om.MFnNurbsCurve(dagPath)
                for m in range(1,len(edgeCurlRunMoveCV)) :
                    xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m], w=1)
                    pointInSpace = om.MPoint(xK,yK,zK)
                    closestPoint = om.MPoint()
                    closestPoint = omCurveOut.closestPoint(pointInSpace)
                    cmds.move( closestPoint[0], closestPoint[1], closestPoint[2],edgeCurlRunMoveCV[m] , a =True, ws=True)
            else:
                circleLength = cmds.arclen( 'tempGuide' )
                maxU = cmds.getAttr('tempGuide.maxValue')
                UScaleV = circleLength  / maxU
                if len(edgeSel) == 1:
                    xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[-2], w=1)
                    getU = X2l([xK, yK, zK], 'tempGuide')[0]
                    movingDist = distList[0]
                    moveV = movingDist / UScaleV
                    newU = getU + moveV
                    xj, yj, zj = cmds.pointOnCurve('tempGuide', pr= newU, p=1)
                    cmds.move(xj, yj, zj, edgeCurlRunMoveCV[-1] , a =True, ws=True)
                else:
                    for m in range(1,len(edgeCurlRunMoveCV)) :
                        xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m-1], w=1)
                        getU = X2l([xK, yK, zK], 'tempGuide')[0]
                        movingDist = distList[m-1]
                        moveV = movingDist / UScaleV
                        newU = getU + moveV
                        xj, yj, zj = cmds.pointOnCurve('tempGuide', pr= newU, p=1)
                        cmds.move(xj, yj, zj, edgeCurlRunMoveCV[m] , a =True, ws=True)
        else:
            if checkLock == 0:
                selectionList = om.MSelectionList()
                selectionList.add('tempGuide')
                dagPath = om.MDagPath()
                selectionList.getDagPath(0, dagPath)
                omCurveOut = om.MFnNurbsCurve(dagPath)
                if checkEven == 1:
                    Xo7(edgeSel)
                for m in range(1,len(edgeCurlRunMoveCV)) :
                    xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m], w=1)
                    pointInSpace = om.MPoint(xK,yK,zK)
                    closestPoint = om.MPoint()
                    closestPoint = omCurveOut.closestPoint(pointInSpace)
                    cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], edgeCurlRunMoveCV[m] , a =True, ws=True)
            else:
                circleLength = cmds.arclen( 'tempGuide' )
                maxU = cmds.getAttr('tempGuide.maxValue')
                UScaleV = circleLength  / maxU
                if len(edgeSel) == 1:
                    xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[-2], w=1)
                    getU = X2l([xK, yK, zK], 'tempGuide')[0]
                    movingDist = distList[0]
                    moveV = movingDist / UScaleV
                    newU = getU + moveV
                    xj, yj, zj = cmds.pointOnCurve('tempGuide', pr= newU, p=1)
                    cmds.move(xj, yj, zj, edgeCurlRunMoveCV[-1] , a =True, ws=True)
                else:
                    for m in range(1,len(edgeCurlRunMoveCV)) :
                        xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m-1], w=1)
                        getU = X2l([xK, yK, zK], 'tempGuide')[0]
                        movingDist = distList[m-1]
                        moveV = movingDist / UScaleV
                        newU = getU + moveV
                        xj, yj, zj = cmds.pointOnCurve('tempGuide', pr= newU, p=1)
                        cmds.move(xj, yj, zj, edgeCurlRunMoveCV[m] , a =True, ws=True)
        cleanList = []
        if len(edgeSel) == 1:
            cmds.select(edgeCurlRunMoveCV[-2],edgeCurlRunMoveCV[-1])
            cmds.ConvertSelectionToContainedEdges()
            selNew=cmds.ls(sl=1)
            cmd = 'doMenuComponentSelection("' + edgeSel[0].split('.')[0] +'", "edge");'
            mel.eval(cmd)
            cmds.select(selNew)
            cleanList = ('tempGuid*','arcCurv*','upperLo*','aimLo*','baseLo*','makeThreePointCircularAr*','tempGuideLin*')
        else:
            if startMode!= 100:
                global ctx
                ctx = 'edgeCurlRun'
                if cmds.draggerContext(ctx, exists=True):
                    cmds.deleteUI(ctx)
                cmds.draggerContext(ctx, pressCommand = X78, rc = Xo6, dragCommand = XOl, fnz = X3I, name=ctx, cursor='crossHair',undoMode='step')
                cmds.setToolTo(ctx)
                cleanList = ('arcCurv*','upperLo*','aimLo*','baseLo*','makeThreePointCircularAr*','tempGuideLin*')
            else:
                cleanList = ('tempGuid*','arcCurv*','upperLo*','aimLo*','baseLo*','makeThreePointCircularAr*','tempGuideLin*')
            cmds.select(edgeSel)
            cmd = 'doMenuComponentSelection("' + edgeSel[0].split('.')[0] +'", "edge");'
            mel.eval(cmd)
            cmds.select(edgeCurlRunSel)
        for c in cleanList:
            if cmds.objExists(c):
                cmds.delete(c)

def Xo6():
    lineList = ('tempGuide','tempGuideLine')
    for l in lineList:
        if cmds.objExists(l):
            cmds.setAttr((l + ".visibility"),0)

def XOl():
    global edgeCurlRunMoveCV
    global edgeCurlRunSel
    global screenX,screenY
    global ctx
    global currentScaleRecord
    global edgeCurlRunDistList
    global startModeRecord
    currentRotRecord = 0
    currentEnRecord = 0
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
    screenX = vpX
    screenY = vpY
    selectionList = om.MSelectionList()
    selectionList.add('tempGuide')
    dagPath = om.MDagPath()
    selectionList.getDagPath(0, dagPath)
    omCurveOut = om.MFnNurbsCurve(dagPath)
    if currentScaleRecord > vpX:
        cmds.setAttr('tempGuide.scale',1.02,1.02,1.02)
    else:
        cmds.setAttr('tempGuide.scale',0.98,0.98,0.98)
    currentScaleRecord = vpX
    cmds.makeIdentity('tempGuide', apply=1, t=1,r=1,s=1)
    checkLock = cmds.checkBox('lockCurveEdgeLength', q=1,v=1)
    if(checkLock == 1):
        cmds.setAttr("tempGuide.visibility",1)
        circleLength = cmds.arclen( 'tempGuide' )
        maxU = cmds.getAttr('tempGuide.maxValue')
        UScaleV = circleLength  / maxU
        for m in range(1,len(edgeCurlRunMoveCV)) :
            xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m-1], w=1)
            getU = X2l([xK, yK, zK], 'tempGuide')[0]
            movingDist = edgeCurlRunDistList[m-1]
            moveV = movingDist / UScaleV
            newU = getU + moveV
            xj, yj, zj = cmds.pointOnCurve('tempGuide', pr= newU, p=1)
            cmds.move(xj, yj, zj, edgeCurlRunMoveCV[m] , a =True, ws=True)
    else:
        cmds.setAttr("tempGuide.visibility",1)
        for m in range(1,len(edgeCurlRunMoveCV)) :
            xK, yK, zK = cmds.pointPosition(edgeCurlRunMoveCV[m], w=1)
            pointInSpace = om.MPoint(xK,yK,zK)
            closestPoint = om.MPoint()
            closestPoint = omCurveOut.closestPoint(pointInSpace)
            cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], edgeCurlRunMoveCV[m] , a =True, ws=True)
    cmds.refresh(f=True)

def X3I():
    cleanList = ('tempGuid*','arcCurv*','upperLo*','aimLo*','baseLo*','makeThreePointCircularAr*','tempGuideLin*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)

def X78():
    global edgeCurlRunMoveCV
    global edgeCurlRunSel
    global screenX,screenY
    global ctx
    global currentScaleRecord
    currentScaleRecord = 0
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY

def Xl6():
    cmds.checkBox('lockCurveEdgeLength', e=1,v=1)
    cmds.checkBox('evenCurveEdgeLength', e=1,v=0)
    cmds.setToolTo( 'moveSuperContext' )

def X83():
    cmds.checkBox('lockCurveEdgeLength', e=1,v=0)
    cmds.setToolTo( 'moveSuperContext' )

def X87():
    cmds.checkBox('lockCurveEdgeLength', e=1,v=0)
    cmds.checkBox('evenCurveEdgeLength', e=1,v=1)
    cmds.setToolTo( 'moveSuperContext' )

def X9o():
    cmds.checkBox('evenCurveEdgeLength', e=1,v=0)
    cmds.setToolTo( 'moveSuperContext' )

def X48():
    global curveGrp
    global totalLenGrp
    global ctx
    global listVtxFGrp
    global radiusBestFitGrp
    global arcGrp
    global radiusGrp
    global blendNodeList
    global ulistGrp
    global sectionNumber
    listVtxFGrp = []
    totalLenGrp = []
    ulistGrp = []
    curveGrp = []
    arcGrp = []
    radiusGrp = []
    radiusBestFitGrp = []
    blendNodeList = []
    selEdge = cmds.filterExpand(expand=True, sm=32)
    if selEdge:
        if cmds.objExists('saveSelSemi'):
            cmds.delete('saveSelSemi')
        cmds.sets(name='saveSelSemi', text='saveSelSemi')
        sortGrp = X69()
        for e in sortGrp:
            listVtx = X8I(e)
            firstN = listVtx[0].split('[')[1].split(']')[0]
            secN = listVtx[1].split('[')[1].split(']')[0]
            if int(firstN) > int(secN):
                listVtx.reverse()
            listVtxFGrp.append(listVtx)
            positionListA = []
            for n in listVtx:
                getPo = cmds.pointPosition(n, w=1)
                positionListA.append(getPo)
            p1 = cmds.pointPosition(listVtx[0], w=1)
            p2 = cmds.pointPosition(listVtx[-1], w=1)
            radius = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) / 2
            p3 = cmds.pointPosition(listVtx[int(len(listVtx) / 2)], w=1)
            p4 = [(p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2, (p2[2] + p1[2]) / 2]
            distanceBC = math.sqrt((p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2 + (p4[2] - p3[2]) ** 2) / 2
            if distanceBC < 0.001:
                distanceBC = 0.001
            distanceBD = radius / 2.0
            OD = (distanceBC ** 2 + distanceBD ** 2) / (2 * distanceBC)
            newR = radius + OD
            radiusBestFitGrp.append(newR)
            radiusGrp.append(radius)
            newNode = cmds.createNode('makeTwoPointCircularArc')
            arcGrp.append(newNode)
            cmds.setAttr(newNode + '.pt1', p1[0], p1[1], p1[2])
            cmds.setAttr(newNode + '.pt2', p2[0], p2[1], p2[2])
            cmds.setAttr(newNode + '.tac', 0)
            cmds.setAttr(newNode + '.r', newR)
            cmds.setAttr(newNode + '.d', 3)
            sectionNumber = len(e)
            cmds.setAttr(newNode + '.s', sectionNumber)
            newCurve = cmds.createNode('nurbsCurve')
            cmds.connectAttr(newNode + '.oc', newCurve + '.cr')
            transformNode = cmds.listRelatives(newCurve, fullPath=True, parent=True)
            curveName = cmds.listRelatives(parent=True)
            curveGrp.append(curveName[0])
            cmds.setAttr(curveName[0] + '.visibility', 0)
            cvList = []
            cvList.append(listVtx[0])
            cvList.append(listVtx[int(len(listVtx) / 2)])
            cvList.append(listVtx[-1])
            points = []
            for cv in cvList:
                x, y, z = cmds.pointPosition(cv, w=1)
                this_point = om.MPoint(x, y, z)
                points.append(this_point)
            vectors = [ points[i + 1] - points[i] for i in range(len(points) - 1) ]
            if vectors[0] == vectors[1]:
                cmds.move(0.001, 0, 0, e[1:-1], r=1, cs=1, ls=1, wd=1)
                points = []
                for cv in cvList:
                    x, y, z = cmds.pointPosition(cv, w=1)
                    this_point = om.MPoint(x, y, z)
                    points.append(this_point)
                vectors = [ points[i + 1] - points[i] for i in range(len(points) - 1) ]
            Nx = vectors[0][1] * vectors[1][2] - vectors[0][2] * vectors[1][1]
            Ny = vectors[0][2] * vectors[1][0] - vectors[0][0] * vectors[1][2]
            Nz = vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0]
            cmds.setAttr(newNode + '.directionVectorX', Nx)
            cmds.setAttr(newNode + '.directionVectorY', Ny)
            cmds.setAttr(newNode + '.directionVectorZ', Nz)
            cmds.group(em=True, name=curveName[0] + '_offsetSemi')
            cmds.group(em=True, name=curveName[0] + '_aim')
            cmds.setAttr(curveName[0] + '_offsetSemi.translateX', p1[0])
            cmds.setAttr(curveName[0] + '_offsetSemi.translateY', p1[1])
            cmds.setAttr(curveName[0] + '_offsetSemi.translateZ', p1[2])
            cmds.setAttr(curveName[0] + '_aim.translateX', p2[0])
            cmds.setAttr(curveName[0] + '_aim.translateY', p2[1])
            cmds.setAttr(curveName[0] + '_aim.translateZ', p2[2])
            const = cmds.aimConstraint(curveName[0] + '_aim', curveName[0] + '_offsetSemi')
            cmds.delete(const, curveName[0] + '_aim')
            cmds.parent(curveName[0], curveName[0] + '_offsetSemi')
            cmds.FreezeTransformations()
            cmds.move(p1[0], p1[1], p1[2], curveName[0] + '.scalePivot', curveName[0] + '.rotatePivot', a=1)
            totalEdgeLoopLength = 0
            sum = 0
            Llist = []
            uList = []
            pList = []
            for i in range(len(listVtx) - 1):
                pA = cmds.pointPosition(listVtx[i], w=1)
                pB = cmds.pointPosition(listVtx[i + 1], w=1)
                checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
                Llist.append(checkDistance)
                totalEdgeLoopLength = totalEdgeLoopLength + checkDistance
            totalLenGrp.append(totalEdgeLoopLength)
            goEven = cmds.checkBox('evenCurveEdgeLength', q=1, v=1)
            if goEven == 1:
                avg = totalEdgeLoopLength / len(e)
                for j in range(len(e)):
                    sum = (j + 1) * avg
                    uList.append(sum)
            else:
                for j in Llist:
                    sum = sum + j
                    uList.append(sum)

            ulistGrp.append(uList)
            for k in uList:
                p = k / totalEdgeLoopLength * sectionNumber
                pList.append(p)

            for q in range(len(pList) - 1):
                pp = cmds.pointOnCurve(curveName[0], pr=pList[q], p=1)
                cmds.move(pp[0], pp[1], pp[2], listVtx[q + 1], a=True, ws=True)
            backupCurve = cmds.duplicate(curveName[0])
            p1A = cmds.pointPosition(listVtx[1], w=1)
            p2A = cmds.pointPosition(listVtx[-2], w=1)
            mid1x = (p1A[0] - p1[0]) / 2 + p1[0]
            mid1y = (p1A[1] - p1[1]) / 2 + p1[1]
            mid1z = (p1A[2] - p1[2]) / 2 + p1[2]
            mid2x = (p2A[0] - p2[0]) / 2 + p2[0]
            mid2y = (p2A[1] - p2[1]) / 2 + p2[1]
            mid2z = (p2A[2] - p2[2]) / 2 + p2[2]
            positionListA.insert(1, [mid1x, mid1y, mid1z])
            positionListA.insert(len(positionListA) - 1, [mid2x, mid2y, mid2z])
            for x in range(len(positionListA)):
                cmds.move(positionListA[x][0], positionListA[x][1], positionListA[x][2], backupCurve[0] + '.cv[' + str(x) + ']', a=1)
            blendName = cmds.blendShape(backupCurve[0], curveName[0], w=[(0, 1)], en=0)
            blendNodeList.append(blendName[0])
        meshName = selEdge[0].split('.')[0]
        cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
        mel.eval(cmd)
        cmds.select(selEdge)
        ctx = 'unBevelCtx'
        if cmds.draggerContext(ctx, exists=True):
            cmds.deleteUI(ctx)
        cmds.draggerContext(ctx, pressCommand=XO2, rc=X26, dragCommand=X38, fnz=X74, name=ctx, cursor='crossHair', undoMode='step')
        cmds.setToolTo(ctx)
def X74():
    cmds.setToolTo('selectSuperContext')
    cleanList = ('makeTwoPointCircularAr*','*Semi*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def X26():
    cmds.setToolTo('selectSuperContext')
    cleanList = ('makeTwoPointCircularAr*','*Semi*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def XO2():
    global currentRotRecord
    global currentEnRecord
    global screenX
    global screenY
    currentRotRecord = 0
    currentEnRecord = 0
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    t = radiusGrp[0] / radiusBestFitGrp[0]
    screenX = (vpX + t) / 1.9
def X38():
    global currentRotRecord
    global currentEnRecord
    modifiers = cmds.getModifiers()
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
    distanceA = (vpX - screenX) / 100
    t = distanceA
    fu = 1 / (1 + t ** 5 / 100)
    if modifiers == 4:
        for c in curveGrp:
            cmds.setAttr(c + '.rotateX', 0)
    elif modifiers == 1:
        rotateRun = cmds.getAttr(curveGrp[0] + '.rotateX')
        if currentRotRecord > vpX:
            rotateRun = rotateRun + 2
        else:
            rotateRun = rotateRun - 2
        for c in curveGrp:
            cmds.setAttr(c + '.rotateX', rotateRun)
        currentRotRecord = vpX
    elif modifiers == 8:
        evRun = cmds.getAttr(blendNodeList[0] + '.envelope')
        if currentEnRecord > vpX:
            evRun = evRun + 0.05
        else:
            evRun = evRun - 0.05
        if evRun > 1:
            evRun = 1
        elif evRun < 0:
            evRun = 0
        for f in blendNodeList:
            cmds.setAttr(f + '.envelope', evRun)
        currentEnRecord = vpX
    else:
        for f in blendNodeList:
            cmds.setAttr(f + '.envelope', 0)

        for a in range(len(arcGrp)):
            newR = radiusGrp[a] * (1 + fu * 5)
            cmds.setAttr(arcGrp[a] + '.radius', newR)
    for i in range(len(arcGrp)):
        pList = []
        uList = ulistGrp[i]
        for k in uList:
            p = k / totalLenGrp[i] * sectionNumber
            pList.append(p)
        listVtx = listVtxFGrp[i]
        for q in range(len(pList) - 1):
            pp = cmds.pointOnCurve(curveGrp[i], pr=pList[q], p=1)
            cmds.move(pp[0], pp[1], pp[2], listVtx[q + 1], a=True, ws=True)
    cmds.refresh(f=True)
def X7l():
    global selEdge
    global selMeshForDeformer
    global ctx
    selEdge = cmds.filterExpand(expand=True, sm=32)
    currentDropOff = 1
    snapCheck = 1
    goEven = cmds.checkBox('evenCurveEdgeLength', q=1, v=1)
    conP = 2
    curveT = 1
    goArc = 1
    selMeshForDeformer = cmds.ls(sl=1, o=1)
    getCircleState, listVtx = Xll()
    deformerNames = []
    midP = int(len(listVtx) / 2)
    cmds.move(0.01, 0, 0, selEdge[midP], r=1, cs=1, ls=1, wd=1)
    p1 = cmds.pointPosition(listVtx[0], w=1)
    p2 = cmds.pointPosition(listVtx[midP], w=1)
    p3 = cmds.pointPosition(listVtx[-1], w=1)
    newNode = cmds.createNode('makeThreePointCircularArc')
    cmds.setAttr(newNode + '.pt1', p1[0], p1[1], p1[2])
    cmds.setAttr(newNode + '.pt2', p2[0], p2[1], p2[2])
    cmds.setAttr(newNode + '.pt3', p3[0], p3[1], p3[2])
    cmds.setAttr(newNode + '.d', 3)
    cmds.setAttr(newNode + '.s', len(listVtx))
    newCurve = cmds.createNode('nurbsCurve')
    cmds.connectAttr(newNode + '.oc', newCurve + '.cr')
    cmds.delete(ch=1)
    transformNode = cmds.listRelatives(newCurve, fullPath=True, parent=True)
    cmds.rename(transformNode, 'arcCurve')
    numberP = 0
    numberP = int(conP) - 1
    cmds.rebuildCurve('arcCurve', ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=numberP, d=3, tol=0.01)
    cmds.delete('arcCurve', ch=1)
    totalEdgeLoopLength = 0
    sum = 0
    Llist = []
    uList = []
    pList = []
    for i in selEdge:
        e2v = cmds.polyListComponentConversion(i, fe=1, tv=1)
        e2v = cmds.ls(e2v, fl=1)
        pA = cmds.pointPosition(e2v[0], w=1)
        pB = cmds.pointPosition(e2v[1], w=1)
        checkDistance = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
        Llist.append(checkDistance)
        totalEdgeLoopLength = totalEdgeLoopLength + checkDistance
    if goEven == 1:
        avg = totalEdgeLoopLength / len(selEdge)
        for j in range(len(selEdge)):
            sum = (j + 1) * avg
            uList.append(sum)
    else:
        for j in Llist:
            sum = sum + j
            uList.append(sum)
    for k in uList:
        p = k / totalEdgeLoopLength
        pList.append(p)
    for q in range(len(pList)):
        if q + 1 == len(listVtx):
            pp = cmds.pointOnCurve('arcCurve', pr=0, p=1)
            cmds.move(pp[0], pp[1], pp[2], listVtx[0], a=True, ws=True)
        else:
            pp = cmds.pointOnCurve('arcCurve', pr=pList[q], p=1)
            cmds.move(pp[0], pp[1], pp[2], listVtx[q + 1], a=True, ws=True)
    cmds.delete('arcCurve', ch=1)
    cmds.select('arcCurve')
    cmds.nurbsCurveToBezier()
    try:
        deformerNames = cmds.wire(selMeshForDeformer, gw=0, en=1, ce=0, li=0, w='arcCurve', uct=0)
    except:
        deformerNames = cmds.wire(selMeshForDeformer, gw=0, en=1, ce=0, li=0, w='arcCurve')
    cmds.setAttr(deformerNames[0] + '.dropoffDistance[0]', 0.1)
    cA = cmds.pointPosition('arcCurve.cv[0]', w=1)
    cD = cmds.pointPosition('arcCurve.cv[3]', w=1)
    try:
        cmds.select('arcCurve.cv[1]')
        cmds.cluster(useComponentTags=0)
        checkSel = cmds.ls(sl=1)
        cmds.rename(checkSel[0], 'ccBHandle')
    except:
        cmds.cluster('arcCurve.cv[1]', name='ccB')

    cmds.move(cA[0], cA[1], cA[2], 'ccBHandle.scalePivot', 'ccBHandle.rotatePivot', a=True, ws=True)
    try:
        cmds.select('arcCurve.cv[2]')
        cmds.cluster(useComponentTags=0)
        checkSel = cmds.ls(sl=1)
        cmds.rename(checkSel[0], 'ccCHandle')
    except:
        cmds.cluster('arcCurve.cv[2]', name='ccC')
    cmds.move(cD[0], cD[1], cD[2], 'ccCHandle.scalePivot', 'ccCHandle.rotatePivot', a=True, ws=True)
    cmds.setAttr('arcCurve.visibility', 0)
    cmds.setAttr('ccBHandle.visibility', 0)
    cmds.setAttr('ccCHandle.visibility', 0)
    meshName = selEdge[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(selEdge)
    hideList = ['arcCurve','arcCurveBaseWire','ccBHandle','ccCHandle']
    for h in hideList:
        cmds.setAttr((h + '.hiddenInOutliner'), 1)
    ctx = 'tensionCtx'
    if cmds.draggerContext(ctx, exists=True):
        cmds.deleteUI(ctx)
    cmds.draggerContext(ctx, pressCommand=X22, rc=X96, dragCommand=XO6, fnz=X33, name=ctx, cursor='crossHair', undoMode='step')
    cmds.setToolTo(ctx)
def X33():
    cmds.delete(selMeshForDeformer, ch=1)
    cmds.setToolTo('selectSuperContext')
    cleanList = ('arc*','cc*Handl*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def X96():
    pass
def X22():
    global screenX
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
def XO6():
    modifiers = cmds.getModifiers()
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
    distanceA = (screenX - vpX) / 100
    t = 1 + distanceA
    if modifiers == 4:
        cmds.setAttr('ccBHandle.scaleX', t)
        cmds.setAttr('ccBHandle.scaleY', t)
        cmds.setAttr('ccBHandle.scaleZ', t)
    elif modifiers == 1:
        cmds.setAttr('ccCHandle.scaleX', t)
        cmds.setAttr('ccCHandle.scaleY', t)
        cmds.setAttr('ccCHandle.scaleZ', t)
    elif modifiers == 8:
        cmds.setAttr('ccBHandle.scaleX', 1)
        cmds.setAttr('ccBHandle.scaleY', 1)
        cmds.setAttr('ccBHandle.scaleZ', 1)
        cmds.setAttr('ccCHandle.scaleX', 1)
        cmds.setAttr('ccCHandle.scaleY', 1)
        cmds.setAttr('ccCHandle.scaleZ', 1)
    else:
        cmds.setAttr('ccBHandle.scaleX', t)
        cmds.setAttr('ccBHandle.scaleY', t)
        cmds.setAttr('ccBHandle.scaleZ', t)
        cmds.setAttr('ccCHandle.scaleX', t)
        cmds.setAttr('ccCHandle.scaleY', t)
        cmds.setAttr('ccCHandle.scaleZ', t)
    cmds.refresh(f=True)
def X8O():
    global vLData
    global cLData
    global ctx
    global ppData
    checCurrentkHUD = cmds.headsUpDisplay(lh=1)
    if checCurrentkHUD is not None:
        for t in checCurrentkHUD:
            cmds.headsUpDisplay(t, rem=1)
    ppData = []
    vLData = []
    cLData = []
    selEdge = cmds.filterExpand(expand=True, sm=32)
    if selEdge:
        if cmds.objExists('saveSel'):
            cmds.delete('saveSel')
        cmds.sets(name='saveSel', text='saveSel')
        sortGrp = X69()
        for e in sortGrp:
            pPoint, vList, cList = X35(e)
            ppData.append(pPoint)
            vLData.append(vList)
            cLData.append(cList)

        cmds.select(selEdge)
        ctx = 'unBevelCtx'
        if cmds.draggerContext(ctx, exists=True):
            cmds.deleteUI(ctx)
        cmds.draggerContext(ctx, pressCommand=X28, rc=Xo8, dragCommand=Xl7, name=ctx, cursor='crossHair', undoMode='step')
        cmds.setToolTo(ctx)
    return
def Xo8():
    cmds.headsUpDisplay('HUDunBevelStep', rem=True)
    flattenList = []
    for v in vLData:
        for x in range(len(v)):
            flattenList.append(v[x])
    cmds.polyMergeVertex(flattenList, d=0.001, am=0, ch=0)
    cmds.select('saveSel')
    meshName = flattenList[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.setToolTo('selectSuperContext')
    if cmds.objExists('saveSel'):
        cmds.delete('saveSel')
def X53():
    if viewPortCount >= 1:
        getPercent = viewPortCount / 100.0
    elif viewPortCount < 1 and viewPortCount > 0:
        getPercent = 0.1
    elif viewPortCount == 0:
        getPercent = 0
    getNumber = '%.2f' % getPercent
    return getNumber
def X28():
    global storeCount
    global screenX
    global screenY
    global viewPortCount
    global lockCount
    viewPortCount = 0
    lockCount = 50
    storeCount = 0
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    lockX = vpX
    cmds.headsUpDisplay('HUDunBevelStep', section=1, block=0, blockSize='large', label='unBevel', labelFontSize='large', command=X53, atr=1)
def Xl7():
    global storeCount
    global screenX
    global viewPortCount
    global lockCount
    movePN = 0
    modifiers = cmds.getModifiers()
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
    if modifiers == 1:
        for i in range(len(ppData)):
            cmds.scale(0, 0, 0, vLData[i], cs=1, r=1, p=(ppData[i][0], ppData[i][1], ppData[i][2]))
        viewPortCount = 0
    elif modifiers == 8:
        if screenX > vpX:
            lockCount = lockCount - 1
        else:
            lockCount = lockCount + 1
        screenX = vpX
        if lockCount > 0:
            getX = int(lockCount / 10) * 10
            if storeCount != getX:
                storeCount = getX
                for i in range(len(ppData)):
                    for v in range(len(vLData[i])):
                        moveX = ppData[i][0] - cLData[i][v][0] * lockCount
                        moveY = ppData[i][1] - cLData[i][v][1] * lockCount
                        moveZ = ppData[i][2] - cLData[i][v][2] * lockCount
                        cmds.move(moveX, moveY, moveZ, vLData[i][v], absolute=1, ws=1)
            viewPortCount = storeCount
        else:
            viewPortCount = 0.1
    else:
        if screenX > vpX:
            lockCount = lockCount - 5
        else:
            lockCount = lockCount + 5
        screenX = vpX
        if lockCount > 0:
            for i in range(len(ppData)):
                for v in range(len(vLData[i])):
                    moveX = ppData[i][0] - cLData[i][v][0] * lockCount
                    moveY = ppData[i][1] - cLData[i][v][1] * lockCount
                    moveZ = ppData[i][2] - cLData[i][v][2] * lockCount
                    cmds.move(moveX, moveY, moveZ, vLData[i][v], absolute=1, ws=1)
            viewPortCount = lockCount
        else:
            viewPortCount = 0.1
    cmds.refresh(f=True)

def XI5():
    selEdge = cmds.filterExpand(expand=True, sm=32)
    if selEdge:
        if cmds.objExists('saveSel'):
            cmds.delete('saveSel')
        cmds.sets(name='saveSel', text='saveSel')
        sortGrp = X69()
        for e in sortGrp:
            X35(e)
        cmds.select(selEdge)
        cmds.ConvertSelectionToVertices()
        cmds.polyMergeVertex(d=0.001, am=0, ch=1)
        cmds.select('saveSel')
        cmds.delete('saveSel')

def X35(edgelist):
    listVtx = X8I(edgelist)
    checkA = X79(listVtx[1], listVtx[0], listVtx[-1])
    angleA = math.degrees(checkA)
    checkB = X79(listVtx[-2], listVtx[-1], listVtx[0])
    angleB = math.degrees(checkB)
    angleC = 180 - angleA - angleB
    distanceC = X3o(listVtx[0], listVtx[-1])
    distanceA = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleA))
    distanceB = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleB))
    oldDistA = X3o(listVtx[-2], listVtx[-1])
    oldDistB = X3o(listVtx[0], listVtx[1])
    scalarB = distanceB / oldDistB
    pA = cmds.pointPosition(listVtx[0], w=1)
    pB = cmds.pointPosition(listVtx[1], w=1)
    newP = [0, 0, 0]
    newP[0] = (pB[0] - pA[0]) * scalarB + pA[0]
    newP[1] = (pB[1] - pA[1]) * scalarB + pA[1]
    newP[2] = (pB[2] - pA[2]) * scalarB + pA[2]
    listVtx = listVtx[1:-1]
    storeDist = []
    for l in listVtx:
        sotreXYZ = [0, 0, 0]
        p = cmds.xform(l, q=True, t=True, ws=True)
        sotreXYZ[0] = (newP[0] - p[0]) / 100
        sotreXYZ[1] = (newP[1] - p[1]) / 100
        sotreXYZ[2] = (newP[2] - p[2]) / 100
        storeDist.append(sotreXYZ)
    return (newP, listVtx, storeDist)
def X84():
    goEven = cmds.checkBox('evenRoundEdgeLength', q=1, v=1)
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        check = []
        check.append(e[0])
        check.append(e[-1])
        e2v = cmds.ls(cmds.polyListComponentConversion(check,tv=1),fl=1)
        if len(e2v) != 3:
            XI7(e)
            if goEven == 1:
                Xo7(e)
                XI7(e)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
def XI7(flatList):
    cleanList = ('newCircleGuid*','tempGuid*','arcCurv*','upperLo*','aimLo*','tempCircleGuide*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    edgeSel = flatList
    listVtx = X8I(edgeSel)
    pointA = listVtx[0]
    pointB = listVtx[-1]
    xA, yA, zA = cmds.pointPosition(pointA, w=1)
    xB, yB, zB = cmds.pointPosition(pointB , w=1)
    avgX = 0
    avgY = 0
    avgZ = 0
    for i in range(1, len(listVtx)-1):
        xP, yP, zP = cmds.pointPosition(listVtx[i], w=1)
        avgX = avgX + xP
        avgY = avgY + yP
        avgZ = avgZ + zP
    xMid = avgX / (len(listVtx)-2)
    yMid = avgY / (len(listVtx)-2)
    zMid = avgZ / (len(listVtx)-2)
    distanceBetween = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB) + (zA - zB) * (zA - zB))
    circleR = distanceBetween / math.sqrt( 2 )
    cmds.circle( nr=(0, 0 ,circleR), c=(0, 0, 0),r= circleR,n='tempCircleGuideA')
    cmds.spaceLocator(n='upperLoc')
    cmds.spaceLocator(n='aimLoc')
    cmds.spaceLocator(n='baseLoc')
    cmds.select('upperLoc','aimLoc','baseLoc')
    cmds.CenterPivot()
    cmds.setAttr(('upperLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.translate'),0, 1,-1)
    cmds.setAttr(('upperLoc.translate'),0, 1,1)
    consNode = cmds.aimConstraint('aimLoc','baseLoc',offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType='object', worldUpObject='upperLoc')
    cmds.setAttr(('baseLoc.translate'),xA, yA, zA)
    cmds.setAttr(('aimLoc.translate'),xB, yB, zB )
    cmds.setAttr(('upperLoc.translate'),xMid,yMid,zMid)
    cmds.select('tempCircleGuideA','baseLoc')
    cmds.matchTransform()
    cmds.duplicate('tempCircleGuideA',smartTransform=1,n='newCircleGuide')
    cmds.setAttr(('newCircleGuide.translate'),xB, yB, zB)
    intersectC = cmds.curveIntersect('tempCircleGuideA','newCircleGuide')
    sPosX, sPosY,sPosZ = cmds.pointOnCurve('tempCircleGuideA' , pr = float(intersectC[0]), p=1)
    cPosX, cPosY,cPosZ = cmds.pointOnCurve('tempCircleGuideA' , pr = float(intersectC[2]), p=1)
    distA = math.sqrt((xMid - sPosX) * (xMid - sPosX) + (yMid - sPosY) * (yMid - sPosY) + (zMid - sPosZ) * (zMid - sPosZ))
    distB = math.sqrt((xMid - cPosX) * (xMid - cPosX) + (yMid - cPosY) * (yMid - cPosY) + (zMid - cPosZ) * (zMid - cPosZ))
    newCenter = []
    if distA > distB:
        newCenter = [sPosX, sPosY,sPosZ ]
    else:
        newCenter = [cPosX, cPosY,cPosZ ]
    cmds.setAttr(('newCircleGuide.translate'),newCenter[0], newCenter[1], newCenter[2])
    cmds.makeIdentity('newCircleGuide', apply=1, t=1,r=1,s=1)
    selectionList = om.MSelectionList()
    selectionList.add('newCircleGuide')
    dagPath = om.MDagPath()
    selectionList.getDagPath(0, dagPath)
    omCurveOut = om.MFnNurbsCurve(dagPath)
    for m in range(1,len(listVtx)) :
        xK, yK, zK = cmds.pointPosition(listVtx[m], w=1)
        pointInSpace = om.MPoint(xK,yK,zK)
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], listVtx[m] , a =True, ws=True)
    cleanList = ('newCircleGuid*','tempGuid*','arcCurv*','upperLo*','aimLo*','tempCircleGuide*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def Xo9():
    goEven = cmds.checkBox('evenRoundEdgeLength', q=1, v=1)
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        check = []
        check.append(e[0])
        check.append(e[-1])
        e2v = cmds.ls(cmds.polyListComponentConversion(check,tv=1),fl=1)
        if len(e2v) != 3:
            X2o(e)
            if goEven == 1:
                Xo7(e)
                X2o(e)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
def X2o(flatList):
    cleanList = ('newCircleGuid*','tempGuid*','arcCurv*','upperLo*','aimLo*','tempCircleGuide*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    listVtx = X8I(flatList)
    pointA = listVtx[0]
    pointB = listVtx[-1]
    xA, yA, zA = cmds.pointPosition(pointA, w=1)
    xB, yB, zB = cmds.pointPosition(pointB , w=1)
    avgX = 0
    avgY = 0
    avgZ = 0
    for i in range(1, len(listVtx)-1):
        xP, yP, zP = cmds.pointPosition(listVtx[i], w=1)
        avgX = avgX + xP
        avgY = avgY + yP
        avgZ = avgZ + zP
    xMid = avgX / (len(listVtx)-2)
    yMid = avgY / (len(listVtx)-2)
    zMid = avgZ / (len(listVtx)-2)
    distanceBetween = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB) + (zA - zB) * (zA - zB))
    circleR = distanceBetween / 2
    cmds.circle( nr=(0, 0 ,circleR), c=(0, 0, 0),r= circleR,n='newCircleGuide')
    cmds.spaceLocator(n='upperLoc')
    cmds.spaceLocator(n='aimLoc')
    cmds.spaceLocator(n='baseLoc')
    cmds.select('upperLoc','aimLoc','baseLoc')
    cmds.CenterPivot()
    cmds.setAttr(('upperLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.translate'),0, 1,-1)
    cmds.setAttr(('upperLoc.translate'),0, 1,1)
    consNode = cmds.aimConstraint('aimLoc','baseLoc',offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType='object', worldUpObject='upperLoc')
    cmds.setAttr(('baseLoc.translate'),xA, yA, zA)
    cmds.setAttr(('aimLoc.translate'),xB, yB, zB )
    cmds.setAttr(('upperLoc.translate'),xMid,yMid,zMid)
    cmds.select('newCircleGuide','baseLoc')
    cmds.matchTransform()
    xC = (xA - xB)/2 + xB
    yC = (yA - yB)/2 + yB
    zC = (zA - zB)/2 + zB
    cmds.setAttr(('newCircleGuide.translate'),xC, yC, zC)
    cmds.makeIdentity('newCircleGuide', apply=1, t=1,r=1,s=1)
    selectionList = om.MSelectionList()
    selectionList.add('newCircleGuide')
    dagPath = om.MDagPath()
    selectionList.getDagPath(0, dagPath)
    omCurveOut = om.MFnNurbsCurve(dagPath)
    for m in range(1,len(listVtx)) :
        xK, yK, zK = cmds.pointPosition(listVtx[m], w=1)
        pointInSpace = om.MPoint(xK,yK,zK)
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], listVtx[m] , a =True, ws=True)
    cleanList = ('newCircleGuid*','tempGuid*','arcCurv*','upperLo*','aimLo*','tempCircleGuide*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def X5I():
    checkEven = cmds.checkBox('evenRoundEdgeLength', q=1,v=1)
    pivotSnapSwitch = cmds.checkBox('evenRoundPivotSnap', q=1,v=1)
    getFaceList = cmds.filterExpand(ex=1, sm=34)
    if getFaceList:
        cmds.ConvertSelectionToEdgePerimeter()
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    cmds.polyCircularizeEdge(constructionHistory=0, alignment=0, radialOffset=0, normalOffset=0, normalOrientation=0, smoothingAngle=30, evenlyDistribute = checkEven, divisions=0, supportingEdges=0, twist=0, relaxInterior=1)
    sortGrp = X69()
    meshName = edgeLoopSel[0].split('.')[0]
    cmds.delete(meshName,ch =1)
    if pivotSnapSwitch == 1:
        if len(sortGrp) > 1:
            X2O()
def X2O():
    pivotSnapTypeCheck = cmds.radioButtonGrp('PivotSnapType', q=1,sl=1)
    cleanList = ('baseCircleCurv*','tempCenterCurve*','xxxx','tempCircleCenterLin*','upperLo*','aimLo*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    baseLoopNumber = 0
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    curveList = []
    targetLoop = ''
    vCheck = 10000000
    if pivotSnapTypeCheck == 2:
        vCheck = 0
    for e in sortGrp:
        bbox =cmds.xform(e, q=1, ws=1, bb=1)
        xSide = (bbox[3]-bbox[0])*(bbox[4]-bbox[1])
        ySide = (bbox[5]-bbox[2])*(bbox[3]-bbox[0])
        zSide = (bbox[4]-bbox[1])*(bbox[5]-bbox[2])
        if xSide == 0:
            xSide = 1
        if ySide == 0:
            ySide = 1
        if zSide == 0:
            zSide = 1
        bboxV =  math.sqrt(xSide*ySide*zSide)
        if pivotSnapTypeCheck == 1:
            if bboxV < vCheck:
                vCheck = bboxV
                targetLoop = e
        else:
            if bboxV > vCheck:
                vCheck = bboxV
                targetLoop = e
    cmds.select(targetLoop)
    cirvleNode = cmds.polyToCurve(ch=0,form=2, degree=1, conformToSmoothMeshPreview=1,n='baseCircleCurve')
    cmds.CenterPivot()
    cmds.select(targetLoop)
    cmds.ConvertSelectionToVertices()
    edgeSel = cmds.ls(sl=1,fl=1)
    baseLoopNumber = len(edgeSel)
    pointA = edgeSel[0]
    pointB = edgeSel[-1]
    pointC = edgeSel[int(len(edgeSel)/2)]
    xA, yA, zA = cmds.pointPosition(pointA, w=1)
    xB, yB, zB = cmds.pointPosition(pointB , w=1)
    xC, yC, zC = cmds.pointPosition(pointC , w=1)
    cmds.spaceLocator(n='upperLoc')
    cmds.spaceLocator(n='aimLoc')
    cmds.spaceLocator(n='baseLoc')
    cmds.select('upperLoc','aimLoc','baseLoc')
    cmds.CenterPivot()
    cmds.setAttr(('upperLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.scale'),0.01,0.01,0.01)
    cmds.setAttr(('aimLoc.translate'),0, 1,-1)
    cmds.setAttr(('upperLoc.translate'),0, 1,1)
    consNode = cmds.aimConstraint('aimLoc','baseLoc',offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType='object', worldUpObject='upperLoc')
    cmds.setAttr(('baseLoc.translate'),xA, yA, zA)
    cmds.setAttr(('aimLoc.translate'),xB, yB, zB )
    cmds.setAttr(('upperLoc.translate'),xC, yC, zC)
    cmds.curve(d=1, p=[(0,0,0),(0,0,-10)], k=[0,1],name = 'tempCircleCenterLine')
    cmds.CenterPivot()
    cmds.select('tempCircleCenterLine','baseLoc')
    cmds.matchTransform(rot=1)
    cmds.select('tempCircleCenterLine','baseCircleCurve')
    cmds.matchTransform(pos=1)
    cmds.makeIdentity('tempCircleCenterLine', apply=1, t=1,r=1,s=1)
    selectionList = om.MSelectionList()
    selectionList.add('tempCircleCenterLine')
    dagPath = om.MDagPath()
    selectionList.getDagPath(0, dagPath)
    omCurveOut = om.MFnNurbsCurve(dagPath)
    matchList =  list(set(edgeLoopSel)-set(targetLoop))
    cmds.select(matchList)
    sortGrp = X69()
    cmds.spaceLocator(n='xxxx')
    meshName = edgeLoopSel[0].split('.')[0]
    for e in sortGrp:
        cmds.select(e)
        cirvleNode = cmds.polyToCurve(ch=0,form=2, degree=1, conformToSmoothMeshPreview=1,name='tempCenterCurve01')
        cmds.CenterPivot()
        cmds.select('baseCircleCurve',cirvleNode[0])
        cmds.matchTransform()
        cmds.makeIdentity('baseCircleCurve', apply=1, t=1,r=1,s=1)
        baseLength = cmds.arclen( 'baseCircleCurve' )
        targetLength = cmds.arclen( cirvleNode[0] )
        scaleV = targetLength / baseLength
        cmds.setAttr(('baseCircleCurve.scale'),scaleV,scaleV,scaleV)
        compareCVList = cmds.ls(('baseCircleCurve.cv[*]'),fl=1)
        bboxPiv =cmds.xform('baseCircleCurve', q=1, ws=1, piv=1)
        pointInSpace = om.MPoint(bboxPiv[0],bboxPiv[1],bboxPiv[2])
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], 'xxxx', a =True, ws=True)
        cmds.select('baseCircleCurve','xxxx')
        cmds.matchTransform(pos=1)
        cmds.select(e)
        cmds.ConvertSelectionToVertices()
        listVtx = cmds.ls(sl=1,fl=1)
        cmds.setToolTo('moveSuperContext')
        centerP = cmds.manipMoveContext("Move", q=1,p=1)
        nodeCluster = cmds.cluster(n= 'centerGrp')
        pointInSpace = om.MPoint(centerP[0],centerP[1],centerP[2])
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        cmds.move(closestPoint[0], closestPoint[1], closestPoint[2], nodeCluster[1], rpr=1)
        cmds.delete(meshName,ch =1)
        if baseLoopNumber == len(listVtx):
            for m in listVtx :
                xK, yK, zK = cmds.pointPosition(m, w=1)
                checkDist = 100000
                getCV = []
                toRemove = ''
                for c in compareCVList:
                    xN, yN, zN = cmds.pointPosition(c, w=1)
                    dist = math.sqrt((xK - xN) * (xK - xN) + (yK - yN) * (yK - yN) + (zK - zN) * (zK - zN))
                    if dist < checkDist:
                        checkDist = dist
                        getCV = [xN,yN,zN]
                        toRemove = c
                cmds.move( getCV[0], getCV[1], getCV[2], m , a =True, ws=True)
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
    cleanList = ('baseCircleCurv*','tempCenterCurve*','xxxx','tempCircleCenterLin*','upperLo*','aimLo*','baseLo*')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
def Xo2():
    goEven = cmds.checkBox('evenCurveEdgeLength', q=1, v=1)
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        X42(e)
        if goEven == 1:
            Xo7(e)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
def X42(flatList):
    if cmds.objExists('tempCenterLin*'):
        cmds.delete('tempCenterLin*')
    edgeSel = flatList
    listVtx = X8I(edgeSel)
    xA, yA, zA = cmds.pointPosition(listVtx[0], w=1)
    xB, yB, zB = cmds.pointPosition(listVtx[-1], w=1)
    cmds.curve(d=1, p=[(xA, yA, zA),(xB, yB, zB)], k=[0,1],name = 'tempCenterLine')
    selectionList = om.MSelectionList()
    selectionList.add('tempCenterLine')
    dagPath = om.MDagPath()
    selectionList.getDagPath(0, dagPath)
    omCurveOut = om.MFnNurbsCurve(dagPath)
    for m in listVtx :
        xK, yK, zK = cmds.pointPosition(m, w=1)
        pointInSpace = om.MPoint(xK,yK,zK)
        closestPoint = om.MPoint()
        closestPoint = omCurveOut.closestPoint(pointInSpace)
        cmds.move( closestPoint[0], closestPoint[1], closestPoint[2],m, a =True, ws=True)
    if cmds.objExists('tempCenterLin*'):
        cmds.delete('tempCenterLin*')
def XO7():
    edgeLoopSel = cmds.ls(sl=1,fl=1)
    sortGrp = X69()
    for e in sortGrp:
        check = []
        check.append(e[0])
        check.append(e[-1])
        e2v = cmds.ls(cmds.polyListComponentConversion(check,tv=1),fl=1)
        if len(e2v) != 3:
            Xo7(e)
    meshName = edgeLoopSel[0].split('.')[0]
    cmd = 'doMenuNURBComponentSelection("' + meshName + '", "edge");'
    mel.eval(cmd)
    cmds.select(edgeLoopSel)
def X8I(edgelist):
    if edgelist:
        selEdges = edgelist
        shapeNode = cmds.listRelatives(selEdges[0], fullPath=True , parent=True )
        transformNode = cmds.listRelatives(shapeNode[0], fullPath=True , parent=True )
        edgeNumberList = []
        for a in selEdges:
            checkNumber = ((a.split('.')[1]).split('\n')[0]).split(' ')
            for c in checkNumber:
                findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
                if findNumber:
                    edgeNumberList.append(findNumber)
        getNumber = []
        for s in selEdges:
            evlist = cmds.polyInfo(s,ev=True)
            checkNumber = ((evlist[0].split(':')[1]).split('\n')[0]).split(' ')
            for c in checkNumber:
                findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
                if findNumber:
                    getNumber.append(findNumber)
        dup = set([x for x in getNumber if getNumber.count(x) > 1])
        getHeadTail = list(set(getNumber) - dup)
        vftOrder = []
        finalList = []
        if len(getHeadTail)>0:
            vftOrder.append(getHeadTail[0])
            count = 0
            while len(dup)> 0 and count < 100:
                checkVtx = transformNode[0]+'.vtx['+ vftOrder[-1] + ']'
                velist = cmds.polyInfo(checkVtx,ve=True)
                getNumber = []
                checkNumber = ((velist[0].split(':')[1]).split('\n')[0]).split(' ')
                for c in checkNumber:
                    findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
                    if findNumber:
                        getNumber.append(findNumber)
                findNextEdge = []
                for g in getNumber:
                    if g in edgeNumberList:
                        findNextEdge = g
                edgeNumberList.remove(findNextEdge)
                checkVtx = transformNode[0]+'.e['+ findNextEdge + ']'
                findVtx = cmds.polyInfo(checkVtx,ev=True)
                getNumber = []
                checkNumber = ((findVtx[0].split(':')[1]).split('\n')[0]).split(' ')
                for c in checkNumber:
                    findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
                    if findNumber:
                        getNumber.append(findNumber)
                gotNextVtx = []
                for g in getNumber:
                    if g in dup:
                        gotNextVtx = g
                if len(gotNextVtx)> 0:
                    dup.remove(gotNextVtx)
                    vftOrder.append(gotNextVtx)
                    count +=  1
            if len(getHeadTail)>1:
                vftOrder.append(getHeadTail[1])
                for v in vftOrder:
                    finalList.append(transformNode[0]+'.vtx['+ v + ']' )
        return finalList
def XlO(selEdges):
    if selEdges:
        trans = selEdges[0].split(".")[0]
        e2vInfos = cmds.polyInfo(selEdges, ev=True)
        e2vDict = {}
        fEdges = []
        for info in e2vInfos:
            evList = [ int(i) for i in re.findall('\\d+', info) ]
            e2vDict.update(dict([(evList[0], evList[1:])]))
        while True:
            try:
                startEdge, startVtxs = e2vDict.popitem()
            except:
                break
            edgesGrp = [startEdge]
            num = 0
            for vtx in startVtxs:
                curVtx = vtx
                while True:

                    nextEdges = []
                    for k in e2vDict:
                        if curVtx in e2vDict[k]:
                            nextEdges.append(k)
                    if nextEdges:
                        if len(nextEdges) == 1:
                            if num == 0:
                                edgesGrp.append(nextEdges[0])
                            else:
                                edgesGrp.insert(0, nextEdges[0])
                            nextVtxs = e2vDict[nextEdges[0]]
                            curVtx = [ vtx for vtx in nextVtxs if vtx != curVtx ][0]
                            e2vDict.pop(nextEdges[0])
                        else:
                            break
                    else:
                        break
                num += 1
            fEdges.append(edgesGrp)
        retEdges =[]
        for f in fEdges:
            collectList=[]
            for x in f:
                getCom= (trans +".e["+ str(x) +"]")
                collectList.append(getCom)
            retEdges.append(collectList)
        return retEdges

def Xll():
    selEdges = cmds.ls(sl=1, fl=1)
    shapeNode = cmds.listRelatives(selEdges[0], fullPath=True, parent=True)
    transformNode = cmds.listRelatives(shapeNode[0], fullPath=True, parent=True)
    edgeNumberList = []
    for a in selEdges:
        checkNumber = a.split('.')[1].split('\n')[0].split(' ')
        for c in checkNumber:
            findNumber = ''.join([ n for n in c.split('|')[-1] if n.isdigit() ])
            if findNumber:
                edgeNumberList.append(findNumber)
    getNumber = []
    for s in selEdges:
        evlist = cmds.polyInfo(s, ev=True)
        checkNumber = evlist[0].split(':')[1].split('\n')[0].split(' ')
        for c in checkNumber:
            findNumber = ''.join([ n for n in c.split('|')[-1] if n.isdigit() ])
            if findNumber:
                getNumber.append(findNumber)
    dup = set([ x for x in getNumber if getNumber.count(x) > 1 ])
    getHeadTail = list(set(getNumber) - dup)
    checkCircleState = 0
    if not getHeadTail:
        checkCircleState = 1
        getHeadTail.append(getNumber[0])
    vftOrder = []
    vftOrder.append(getHeadTail[0])
    count = 0
    while len(dup) > 0 and count < 1000:
        checkVtx = transformNode[0] + '.vtx[' + vftOrder[-1] + ']'
        velist = cmds.polyInfo(checkVtx, ve=True)
        getNumber = []
        checkNumber = velist[0].split(':')[1].split('\n')[0].split(' ')
        for c in checkNumber:
            findNumber = ''.join([ n for n in c.split('|')[-1] if n.isdigit() ])
            if findNumber:
                getNumber.append(findNumber)
        findNextEdge = []
        for g in getNumber:
            if g in edgeNumberList:
                findNextEdge = g
        edgeNumberList.remove(findNextEdge)
        checkVtx = transformNode[0] + '.e[' + findNextEdge + ']'
        findVtx = cmds.polyInfo(checkVtx, ev=True)
        getNumber = []
        checkNumber = findVtx[0].split(':')[1].split('\n')[0].split(' ')
        for c in checkNumber:
            findNumber = ''.join([ n for n in c.split('|')[-1] if n.isdigit() ])
            if findNumber:
                getNumber.append(findNumber)
        gotNextVtx = []
        for g in getNumber:
            if g in dup:
                gotNextVtx = g
        dup.remove(gotNextVtx)
        vftOrder.append(gotNextVtx)
        count += 1
    if checkCircleState == 0:
        vftOrder.append(getHeadTail[1])
    elif vftOrder[0] == vftOrder[1]:
        vftOrder = vftOrder[1:]
    elif vftOrder[0] == vftOrder[-1]:
        vftOrder = vftOrder[0:-1]
    finalList = []
    for v in vftOrder:
        finalList.append(transformNode[0] + '.vtx[' + v + ']')
    return (checkCircleState, finalList)

def X3o(p1, p2):
    pA = cmds.pointPosition(p1, w=1)
    pB = cmds.pointPosition(p2, w=1)
    dist = math.sqrt((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2)
    return dist
def X79(pA, pB, pC):
    a = cmds.pointPosition(pA, w=1)
    b = cmds.pointPosition(pB, w=1)
    c = cmds.pointPosition(pC, w=1)
    ba = [ aa - bb for aa, bb in zip(a, b) ]
    bc = [ cc - bb for cc, bb in zip(c, b) ]
    nba = math.sqrt(sum((x ** 2.0 for x in ba)))
    ba = [ x / nba for x in ba ]
    nbc = math.sqrt(sum((x ** 2.0 for x in bc)))
    bc = [ x / nbc for x in bc ]
    scalar = sum((aa * bb for aa, bb in zip(ba, bc)))
    angle = math.acos(scalar)
    return angle
def X69():
    selEdges = cmds.ls(sl=1, fl=1)
    trans = selEdges[0].split('.')[0]
    e2vInfos = cmds.polyInfo(selEdges, ev=True)
    e2vDict = {}
    fEdges = []
    for info in e2vInfos:
        evList = [ int(i) for i in re.findall('\\d+', info) ]
        e2vDict.update(dict([(evList[0], evList[1:])]))
    while True:
        try:
            startEdge, startVtxs = e2vDict.popitem()
        except:
            break
        edgesGrp = [startEdge]
        num = 0
        for vtx in startVtxs:
            curVtx = vtx
            while True:
                nextEdges = []
                for k in e2vDict:
                    if curVtx in e2vDict[k]:
                        nextEdges.append(k)

                if nextEdges:
                    if len(nextEdges) == 1:
                        if num == 0:
                            edgesGrp.append(nextEdges[0])
                        else:
                            edgesGrp.insert(0, nextEdges[0])
                        nextVtxs = e2vDict[nextEdges[0]]
                        curVtx = [ vtx for vtx in nextVtxs if vtx != curVtx ][0]
                        e2vDict.pop(nextEdges[0])
                    else:
                        break
                else:
                    break
            num += 1
        fEdges.append(edgesGrp)
    retEdges = []
    for f in fEdges:
        collectList = []
        for x in f:
            getCom = trans + '.e[' + str(x) + ']'
            collectList.append(getCom)
        retEdges.append(collectList)
    return retEdges

def X62(angle):
    currentSelp = cmds.ls(sl=True, fl=True)
    cmds.polySelectConstraint(m=2, w=1, pp=4, m3a=angle, t=0x8000)
    wholeLoop = cmds.ls(sl=True, fl=True)
    cmds.polySelectConstraint(m=2, w=2, t=0x8000)
    removeInnerEdges = cmds.ls(sl=True, fl=True)
    if len(wholeLoop) != len(removeInnerEdges):
        cmds.select(wholeLoop)
        cmds.select(removeInnerEdges, d=True)
    cmds.polySelectConstraint(m=0, w=0)
    cmds.polySelectConstraint(disable=True)
    
def X99():
    cmds.ConvertSelectionToEdges()
    cmds.polySelectConstraint(m=2, t=0x8000, w=1)
    cmds.polySelectConstraint(disable=True)

def X6o():
    cmds.polySlideEdgeCtx("polySlideEdgeContext", e=True, useSnapping=False)
    cmds.setToolTo("polySlideEdgeContext")


def XI9(PM):
    selEdge = cmds.ls(sl=True, fl=True)
    cmds.polySelectConstraint(disable=True)
    if PM == "minus":
        if len(selEdge) > 1:
            cmds.polySelectConstraint(pp=6, t=0x8000)
            cmds.polySelectConstraint(m=0, w=0) 
            cmds.polySelectConstraint(disable=True) 
    else:
        cmds.polySelectConstraint(m=2, w=2, t=0x8000)
        selInner = cmds.ls(sl=True, fl=True)
        cmds.select(selEdge, r=True)
        cmds.polySelectConstraint(m=2, w=1, t=0x8000)
        selBorder = cmds.ls(sl=True, fl=True)
        cmds.select(selEdge, r=True)
        if len(selInner) > len(selBorder):
            cmds.polySelectConstraint(pp=5, t=0x8000)
            cmds.polySelectConstraint(m=0, w=0)
            cmds.polySelectConstraint(disable=True)
        else:
            cmds.polySelectConstraint(pp=1, m=2, w=1, t=0x8000)
            cmds.polySelectConstraint(m=0, w=0)
            cmds.polySelectConstraint(disable=True)


def X32():
    firstSel = cmds.ls(sl=True, fl=True)
    cmd = 'polySelectEdgesEveryN "edgeRing" 1';
    mel.eval(cmd)
    growAll = cmds.ls(sl=True, fl=True)
    newFace = cmds.polyListComponentConversion(firstSel, fe=True, tf=True)
    newEdges = cmds.ls(cmds.polyListComponentConversion(newFace, ff=True, te=True),fl=1)
    commonItems = list(set(newEdges) & set(growAll))
    cmds.select(commonItems)

def X86():
    firstSel = cmds.ls(sl=True, fl=True)
    newVert = cmds.polyListComponentConversion(firstSel, fe=True, tv=True)
    cmds.select(newVert)
    cmds.ConvertSelectionToContainedFaces(newVert)
    cmds.ConvertSelectionToEdgePerimeter()
    newBorder = cmds.ls(sl=True, fl=True)
    diffItems = list(set(firstSel) - set(newBorder))
    cmds.select(diffItems)


def X95():
    edges = cmds.ls(fl=True, sl=True)
    cmds.polySelectConstraint(m=2, w=2, type=0x8000)
    cmds.polySelectConstraint(disable=True)
    getPoints = cmds.ls( cmds.polyListComponentConversion(edges, tv=True),fl=True)
    edgeLoopExt = cmds.ls( cmds.polySelectSp(edges, q=1, loop=1),fl=True)
    for p in getPoints:
        surEedge = cmds.ls( cmds.polyListComponentConversion(p, te=True),fl=True)
        nextTwoEdge = list(set(surEedge) - set(edgeLoopExt))
        surPoints = cmds.ls( cmds.polyListComponentConversion(nextTwoEdge, tv=True),fl=True)
        surPoints.remove(p) 
        if len(surPoints) == 2:
            ptA = cmds.xform(surPoints[0], q=True, t=True, ws=True)
            ptB = cmds.xform(surPoints[1], q=True, t=True, ws=True)
            midP = cmds.xform(p, q=True, t=True, ws=True)
            distA = math.sqrt( ((ptA[0] - midP[0])**2)  + ((ptA[1] - midP[1])**2) + ((ptA[2] - midP[2])**2))
            distB = math.sqrt( ((ptB[0] - midP[0])**2)  + ((ptB[1] - midP[1])**2) + ((ptB[2] - midP[2])**2))
            scaleBaseP = ''
            scaleDistP = 0
            if distA > distB:
                scaleBaseP = ptA
                scaleDistP = distA
            else:
                 scaleBaseP = ptB
                 scaleDistP = distB
            avgDist = ( distA + distB )/2
            magV =  avgDist /scaleDistP
            if magV < 1: 
                vectBtwPnts= ((scaleBaseP[0] -midP[0])*-1), ((scaleBaseP[1] -midP[1])*-1), ((scaleBaseP[2] -midP[2])*-1)
                vectorToFinish = om.MFloatVector(vectBtwPnts[0],vectBtwPnts[1],vectBtwPnts[2])
                raySource = om.MFloatPoint(scaleBaseP[0],scaleBaseP[1],scaleBaseP[2])
                rayDirection = vectorToFinish
                magnitude = vectorToFinish.length()
                new_magnitude = magnitude * magV
                direction_normalized = vectorToFinish.normal()
                scaled_direction = direction_normalized * new_magnitude
                new_endpoint = raySource + scaled_direction
                cmds.move(new_endpoint.x, new_endpoint.y, new_endpoint.z, p , absolute=True)

def X66():
    target = cmds.intField("collapseLoopNumber", q=1,v = 1)
    checkEdges = cmds.ls(selection=True, flatten=True)
    checkNumberA = XlO(checkEdges)
    if len(checkNumberA) == 1:
        cmds.select(checkEdges, r=True)
        if cmds.objExists("edgeGepLock"):
            cmds.delete("edgeGepLock*")
        cmds.sets(name="edgeGepLock", text="edgeGepLock")
        cvListFlat = cmds.ls(cmds.polyListComponentConversion(fromEdge=True, toVertex=True),fl=1)
        count = 0
        if len(cvListFlat) == len(checkEdges):
            while len(checkEdges) > target and count < 100:
                cmds.select("edgeGepLock", r=True)
                X82('min')
                cmds.polyCollapseEdge()
                cmds.select("edgeGepLock", r=True)
                checkEdges = cmds.ls(selection=True, flatten=True)
                count += 1
        else:
            cmds.select(checkEdges)
            XI9('minus')
            checkEdges = cmds.ls(selection=True, flatten=True)
            if cmds.objExists("edgeGepLock"):
                cmds.delete("edgeGepLock*")
            cmds.sets(name="edgeGepLock", text="edgeGepLock")
            cmds.select("edgeGepLock", r=True)
            while len(checkEdges) > (target - 2) and count < 100:
                cmds.select("edgeGepLock", r=True)
                X82('min')
                cmds.polyCollapseEdge()
                cmds.select("edgeGepLock", r=True)
                checkEdges = cmds.ls(selection=True, flatten=True)
                count += 1
            cmds.select("edgeGepLock", r=True)
            XI9('plus')
        XO7()
        if cmds.objExists("edgeGepLock"):
            cmds.delete("edgeGepLock*")
def Xl9():
    cmds.delete(all=True, e=True, ch=True)
    selEdges = cmds.filterExpand(ex=True, sm=32) or []
    selCV = cmds.filterExpand(ex=True, sm=31) or []
    if len(selCV) > 0 and len(selEdges) == 0:
        cmds.ConvertSelectionToEdges()
        #cmds.GrowPolygonSelectionRegion()
        unwantEdge = cmds.ls(sl=True, fl=True)
        cmds.select(selCV)
        cmds.ConvertSelectionToFaces()
        cmds.polySelectConstraint(mode=2, type=0x0008, size=3)
        cmds.polySelectConstraint(disable=True)
        cmds.ConvertSelectionToEdges()
        cmds.select(unwantEdge, d=True)
        X5o() 
        cmds.select(selCV, add=True)
    elif len(selCV) > 0 and len(selEdges) == 1:
        XI3()
    elif len(selCV) == 1 and len(selEdges) == 2:
        verticesA = cmds.ls(cmds.polyListComponentConversion(selEdges[0], toVertex=True),fl=1)
        verticesB = cmds.ls(cmds.polyListComponentConversion(selEdges[1], toVertex=True),fl=1)
        common_items = list(set(verticesA) & set(verticesB))
        cmds.select(common_items,selCV)
        cmds.polyConnectComponents(ch=0, insertWithEdgeFlow=0, adjustEdgeFlow=0)

def X5o():
    value = 0
    edges = cmds.filterExpand(ex=True, sm=32)
    target_edge = ''
    for edge in edges:
        vertices = cmds.ls(cmds.polyListComponentConversion(edge, toVertex=True),fl=1)
        v1 = cmds.pointPosition(vertices[0], w=True)
        v2 = cmds.pointPosition(vertices[1], w=True)
        check_edge_length = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2)
        if check_edge_length > value:
            value = check_edge_length
            target_edge = edge
    cmds.select(target_edge)


def XI3():
    cleanList = ('KeepEdge','KeepCV','NewCV')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    sel = cmds.ls(sl=1, fl=1)
    cmds.select(cl=1)
    Verts = []
    Edge = []
    newVertAddList = []
    for s in sel:
        if '.vtx[' in s:
            Verts.append(s)
        elif '.e[' in s:
            Edge.append(s)
    if len(Edge) == 1 and len(Verts) > 0:
        cmds.sets(name='KeepEdge', text='g')
        cmds.sets(Edge, add='KeepEdge')
        cmds.sets(name='KeepCV', text='g')
        cmds.sets(Verts, add='KeepCV')
        cmds.sets(name='NewCV', text='g')
        for v in Verts:
            getEdge = cmds.ls(cmds.sets('KeepEdge', query=True),fl=1)
            for g in getEdge:
                EdgeNumber = int(g.split('[')[-1].split(']')[0])
                vertList = cmds.ls(cmds.polyListComponentConversion(g, tv=True), fl=True)
                vertPA = cmds.xform(vertList[0], q=True, ws=True, translation=True)
                vertPB = cmds.xform(vertList[1], q=True, ws=True, translation=True)
                vertPC = cmds.xform(v, q=True, ws=True, translation=True)
                VA = om.MVector(vertPA[0],vertPA[1],vertPA[2])
                VB = om.MVector(vertPB[0],vertPB[1],vertPB[2])
                VC = om.MVector(vertPC[0],vertPC[1],vertPC[2])
                VAB = VB - VA
                magnitude = VAB.length()
                if magnitude != 0:
                    DA = om.MVector(VAB.x / magnitude, VAB.y / magnitude, VAB.z / magnitude)
                else:
                    DA = om.MVector(VAB)
                t = (VC - VA) * DA
                closest_point = VA + DA * t
                wPos = [closest_point.x, closest_point.y, closest_point.z]
                if wPos != vertPA and wPos != vertPB:
                    AC = closest_point - VA
                    BC = closest_point - VB
                    if AC * BC < 0:
                        print('here')
                        cmds.polySplit(g, ip=[(EdgeNumber, 0.5)], ch=0)
                        lastVert = str(v.split('.')[0]) + '.vtx[' + str(cmds.polyEvaluate(v, v=1)) + ']'
                        cmds.xform(lastVert, ws=True, t=(closest_point.x, closest_point.y, closest_point.z))
                        cmds.polyConnectComponents([v, lastVert], ch=0)
                        cmds.sets(lastVert, add='NewCV')
                else:
                    checkExistEdge = cmds.ls(cmds.polyListComponentConversion(v, te=True), fl=True)
                    if wPos == vertPA:
                        checkCurrentEdge = cmds.ls(cmds.polyListComponentConversion(vertList[0], te=True), fl=True)
                        common_elements = [element for element in checkExistEdge if element in checkCurrentEdge]
                        if len(common_elements) == 0:
                            cmds.polyConnectComponents([v, vertList[0]], ch=0)
                    else:
                        checkCurrentEdges = cmds.ls(cmds.polyListComponentConversion(vertList[1], te=True), fl=True)
                        common_elements = [element for element in checkExistEdge if element in checkCurrentEdge]
                        if len(common_elements) == 0:
                            cmds.polyConnectComponents([v, vertList[1]], ch=0)
        getNewCV = cmds.ls(cmds.sets('NewCV', query=True),fl=1)
        if 'getNewCV':
            cmds.select('NewCV')
        else:
            cmds.select(Verts,Edge)
        for c in cleanList:
            if cmds.objExists(c):
                cmds.delete(c)
        Xl9()
                           
def run():
    fColor = (0.23,0.2,0.2)
    if cmds.window("EdgeSenseiWindow", exists=True):
        cmds.deleteUI("EdgeSenseiWindow", window=True)
    if cmds.dockControl("EdgeSenseiDock", exists=True):
        cmds.deleteUI("EdgeSenseiDock", control=True)
    edge_window = cmds.window("EdgeSenseiWindow", title="Edge Sensei", widthHeight=(320, 1100),s = 1 ,mxb = False, mnb = False)
    cmds.columnLayout(adj=True)
    cmds.frameLayout(label="Quick Tools", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 50), (4, 7), (5, 50), (6, 7), (7, 50), (8, 7), (9, 65)])
    cmds.text(l=" Quick")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Split",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: cmds.SplitPolygonTool())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Insert",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: cmds.SplitEdgeRingTool())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Slide",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X6o())
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 65), (4, 7), (5, 75), (6, 7), (7, 50), (8, 7), (9, 65)])
    cmds.text(l="")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Connet 90",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: Xl9())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Sharp Corner",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X23())
    cmds.setParent("..")
    cmds.separator(height=5, style="in")
    cmds.rowColumnLayout(nc=13, cw=[(1, 50), (2, 20), (3, 50), (4, 7), (5, 70), (6, 7), (7, 50), (8, 20), (9, 50), (10, 5), (11, 20), (12, 5), (13, 20)])
    cmds.text(l=" Select")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Border",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X99())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Contiguous",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X62(30))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Shortest",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X92())
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=13, cw=[(1, 50), (2, 20), (3, 40), (4, 5), (5, 20), (6, 5), (7, 20), (8, 20), (9, 50), (10, 5), (11, 20), (12, 5), (13, 20)])
    cmds.text(l=" ")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Loop",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: cmds.SelectEdgeLoopSp())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="+", rpt=1, bgc=(0.08, 0.18, 0.38), c=lambda *args: XI9("plus"))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="-", rpt=1, bgc=(0.08, 0.38, 0.28), c=lambda *args: XI9("minus"))
    cmds.text(l=" |")
    cmds.iconTextButton(style="textOnly", label="Ring",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: cmds.SelectEdgeRingSp())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="+", rpt=1, bgc=(0.08, 0.18, 0.38), c=lambda *args: X32())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="-", rpt=1, bgc=(0.08, 0.38, 0.28), c=lambda *args: X86())
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=7, cw=[(1, 50), (2, 20), (3, 50), (4, 20), (5, 50), (6, 20), (7, 50)])
    cmds.setParent("..")
    cmds.separator(height=5, style="in")
    cmds.rowColumnLayout(nc=11, cw=[(1, 50), (2, 20), (3, 50), (4, 7), (5, 50), (6, 7), (7, 50), (8, 7), (9, 50), (10, 7), (11, 65)])
    cmds.text(l="Average")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Smooth", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X94())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Even", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: XO7())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Spread",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X95())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Flow",rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: cmds.PolyEditEdgeFlow())
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.frameLayout(label="Arc", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 50), (4, 5), (5, 50), (6, 5), (7, 50), (8, 5), (9, 50)])
    cmds.text(l="      3D")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="1", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X9l(1))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="2", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X9l(2))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="3", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X9l(3))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="--", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X9l(0))
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 50), (4, 5), (5, 50), (6, 5), (7, 50), (8, 5), (9, 50)])
    cmds.text(l="      2D")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="1", rpt=1, bgc=(0.22, 0.22, 0.18), c=lambda *args: Xl8(1))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="2", rpt=1, bgc=(0.22, 0.22, 0.18), c=lambda *args: Xl8(2))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="3", rpt=1, bgc=(0.22, 0.22, 0.18), c=lambda *args: Xl8(3))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="--", rpt=1, bgc=(0.22, 0.22, 0.18), c=lambda *args: Xl8(0))
    cmds.text(l="", h=5)
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 50), (4, 5), (5, 50), (6, 5), (7, 50), (8, 5), (9, 50)])
    cmds.text(l="      Edit")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Inflate", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X48())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Tension", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X7l())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="UnBevel", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X8O())
    cmds.text(l="")
    cmds.checkBox("evenCurveEdgeLength", label="Even", value=0)
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.frameLayout(label="Constant", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=7, cw=[(1, 50), (2, 20), (3, 50), (4, 7), (5, 50), (6, 17), (7, 90)])
    cmds.text(l="  Extend")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="L", rpt=1,bgc=(0.08, 0.18, 0.38), c=lambda *args: X3l('L',100))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="R", rpt=1,bgc=(0.08, 0.38, 0.28), c=lambda *args: X3l('R',100))
    cmds.text(l="")
    cmds.checkBox("lockCurveEdgeLength", label="Keep Length", value=0)
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=7, cw=[(1, 50), (2, 20), (3, 50), (4, 7), (5, 50), (6, 20), (7, 50)])
    cmds.text(l="     Curl")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="L", rpt=1,bgc=(0.08, 0.18, 0.38), c=lambda *args: X3l('L',4))
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="R", rpt=1,bgc=(0.08, 0.38, 0.28), c=lambda *args: X3l('R',4))
    cmds.setParent("..")
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.frameLayout(label="Round", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=9, cw=[(1, 50), (2, 20), (3, 50), (4, 5), (5, 50), (6, 5), (7, 50), (8, 5), (9, 50)])
    cmds.text(l="")
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="90", bgc=(0.18, 0.18, 0.18), c=lambda *args: X84())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="180", bgc=(0.18, 0.18, 0.18), c=lambda *args: Xo9())
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="360", bgc=(0.18, 0.18, 0.18), c=lambda *args: X5I())
    cmds.text(l="")
    cmds.checkBox("evenRoundEdgeLength", label="Even", value=1)
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=4, cw=[(1, 50), (2, 20), (3,110), (4,130)])
    cmds.text(l="")
    cmds.text(l="")
    cmds.checkBox("evenRoundPivotSnap", label="Pivot Snap Type", value=0, cc=lambda *args: Xl2())
    cmds.radioButtonGrp("PivotSnapType", en=0, nrb=2, sl=1, la2=("Small", "Big"), cw=[(1,50), (2, 60)] )
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.frameLayout(label="Insert by Number", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.floatSliderGrp("multiInsertNo", v=2, pre=0, min=2, max=50, fmn=2, fmx=100, cw3=[50, 35, 0], label="Number  ", field=True)
    cmds.rowColumnLayout(nc=5, cw=[(1, 50),(2, 20), (3, 30),(4, 9), (5, 150)])
    cmds.text(l="Repeat")
    cmds.text(l="")
    cmds.checkBox("keepSpliteNumber", l="", v=0)
    cmds.text(l="")
    cmds.iconTextButton(style="textOnly", label="Split", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: XO3())
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.text(l="",h=1)
    cmds.setParent("..")
    cmds.frameLayout(label="Insert by Length:",  bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=7, cw=[(1, 45), (2, 7), (3, 40), (4, 7),(5, 95), (6, 5),(7, 95)])
    cmds.text(label="Length:")
    cmds.text(l="", h=3)
    cmds.floatField("refInsertLength", v = 10, pre=3)
    cmds.text(l="", h=3)
    cmds.button(bgc=[0.2, 0.2, 0.2], label="Check", h=23, c=lambda *args: X76("IbL"))
    cmds.text(l="", h=3)
    cmds.button(bgc=[0.2, 0.2, 0.2], label="Split", h=23, c=lambda *args: XoI())
    cmds.setParent('..')
    cmds.text(l="",h=1)
    cmds.setParent('..')
    cmds.frameLayout(label="Edge Lock", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=3, cw=[(1, 50), (2, 50), (3, 175)])
    cmds.text(l="   Type")
    cmds.text(l="", h=3)
    cmds.radioButtonGrp("lockEdgeType", nrb=2, sl=1, la2=["Absolute", "Relative"], cw=[(1, 90), (2, 70)])
    cmds.setParent("..")
    cmds.floatSliderGrp("lockEdgeSlider", v=0.95, min=0.001, max=0.999, s=0.01, cw3=[50, 40, 0], label="Ratio   ", field=True, dc=lambda *args: X36())
    cmds.rowColumnLayout(nc=7, cw=[(1, 45), (2, 7), (3, 40), (4, 7),(5, 95), (6, 5),(7, 95)])
    cmds.text(l="Length")
    cmds.text(l="", h=3)
    cmds.floatField("lastLockEdgelength",  v = 0.02, pre=3)
    cmds.text(l="", h=3)
    cmds.iconTextButton(style="textOnly",label="Ratio", rpt=1, bgc=(0.18, 0.18, 0.18), c=lambda *args: X25())
    cmds.text(l="", h=3)
    cmds.iconTextButton(style="textOnly",label="Length", rpt=1,bgc=(0.18, 0.18, 0.18), c=lambda *args: X58())
    cmds.text(l="",h=2)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.text(l="",h=4)
    cmds.setParent("..")
    cmds.frameLayout(label="Ring Equalizer", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=11, cw=[(1, 45), (2, 7), (3, 40), (4, 7),(5, 40), (6, 30),(7, 35), (8, 3),(9, 35), (10, 3),(11, 35)])
    cmds.text(l="Length")
    cmds.text(l="",h=2)
    cmds.floatField("equalizerLength", v=1 ,pre =3 )
    cmds.text(l="",h=2)
    cmds.iconTextButton(style="textOnly", label="check", bgc=(0.18, 0.18, 0.18), c=lambda *args: X76("RE"))
    cmds.text(l="  |  ",h=2)
    cmds.iconTextButton(style="textOnly", label="A", bgc=(0.08, 0.18, 0.38), c=lambda *args: X75('A'))
    cmds.text(l="",h=2)
    cmds.iconTextButton(style="textOnly", label="Mid", bgc=(0.18, 0.18, 0.18), c=lambda *args: X75('M'))
    cmds.text(l="",h=2)
    cmds.iconTextButton(style="textOnly", label="B", bgc=(0.08, 0.38, 0.28), c=lambda *args: X75('B'))
    cmds.setParent("..")
    cmds.text(l="",h=1)
    cmds.setParent('..')
    cmds.frameLayout(label="Collapse Loop to Number:",  bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.text(l="",h=2)
    cmds.rowColumnLayout(nc=7, cw=[(1, 45), (2, 7), (3, 40), (4, 7),(5, 95), (6, 5),(7, 95)])
    cmds.text(label="Target:")
    cmds.text(l="", h=3)
    cmds.intField("collapseLoopNumber", v = 10)
    cmds.text(l="", h=3)
    cmds.button(bgc=[0.2, 0.2, 0.2], label="Collapse", h=23, c=lambda *args: X66())
    cmds.setParent('..')
    cmds.text(l="",h=1)
    cmds.setParent('..')
    cmds.frameLayout(label="Arc Deformer", bv=0, w=298, cll=1, cl=0 ,bgc = fColor)
    cmds.rowColumnLayout(nc=3 ,cw=[(1,50),(2,50),(3,175)])
    cmds.text(l ='Type')
    cmds.text(l ='')
    cmds.radioButtonGrp('curveType', nrb=2, sl=1, labelArray2=['Bezier', 'Nurbs'], cw = [(1,90),(2,70)],cc='X45()')
    cmds.setParent( '..' )
    cmds.rowColumnLayout(nc=10 ,cw=[(1,1),(2,50),(3,10),(4,50),(5,5),(6,50),(7,5),(8,50),(9,5),(10,95)])
    cmds.text(l ='')
    cmds.text(l ='Options')
    cmds.text(l ='')
    cmds.checkBox('makeArc', label= "Arc" ,v = 1, cc=lambda *args: X9I())
    cmds.text(l ='')
    cmds.checkBox('snapCurve', label= "Snap" ,v = 1, cc=lambda *args: X77())
    cmds.text(l ='')
    cmds.checkBox('evenSpace', label= "Even" ,v = 1)
    cmds.text(l ='')
    cmds.checkBox('cleanCurve', label= "Keep Curve" ,v = 1)
    cmds.setParent( '..' )
    cmds.intSliderGrp('CPSlider', cw3=[50, 30, 180], label = 'Point ',  field= 1, min= 2, max= 10, fmx = 500, v = 3 )
    cmds.floatSliderGrp('dropOffSlider' , label = 'DropOff', v = 0.01, cw3=[50, 30, 180], field=1 ,pre = 2, min= 0.01, max= 10)
    cmds.rowColumnLayout(nc=4 ,cw=[(1,99),(2,95),(3,5),(4,95)])
    cmds.text(l ='')
    cmds.iconTextButton(style="textOnly", l= 'Create',bgc=(0.18, 0.18, 0.18),  c= 'XI4()')
    cmds.text(l ='')
    cmds.iconTextButton(style="textOnly", l= 'Done', bgc=(0.18, 0.18, 0.18), c= 'X98()')
    cmds.text(l ='')
    cmds.setParent( '..' )
    cmds.text(l="",h=2)
    cmds.showWindow(edge_window)
    cmds.window("EdgeSenseiWindow", e=1, widthHeight=(320, 1100))
    #allowedAreas = ['right', 'left']
    #cmds.dockControl("EdgeSenseiDock", area="left", content = edge_window, width=360, allowedArea = allowedAreas,fl=1, label="EdgeSensei v1.0")