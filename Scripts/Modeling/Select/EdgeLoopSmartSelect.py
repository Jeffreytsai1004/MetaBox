#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from maya.OpenMaya import MGlobal
import math
import re
import maya.mel as mel

def run():
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
            checkEdgeLoopGrp =  getEdgeRingGroup(checkCurrentSelEdge)
            if len(checkEdgeLoopGrp) == 1:
                listAAA = ''
                try:
                    listAAA = vtxLoopOrder(checkCurrentSelEdge)
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
                    selShortestLoop()
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

def selShortestLoop():
    global ctx
    global storeAllEdges
    global selInitialGeo
    global storeCameraPosition
    global initialList
    initialList = []
    storeAllEdges = cmds.ls(sl=1,fl=1)
    listVtx = vtxLoopOrder(storeAllEdges)
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
    cmds.draggerContext(ctx, ppc= liveShortPause ,rc = liveShortPause, dragCommand = liveShortMove, fnz = liveShortStop ,name=ctx, cursor='crossHair',undoMode='step')
    cmds.setToolTo(ctx)



def liveShortMove():
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
                cpX,cpY,cpZ = getPolyFaceCenter(hitFaceName)
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
                    listVtx = vtxLoopOrder(liveList)
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
                    checkEdgeLoopGrp =  getEdgeRingGroup(otherList)
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


def liveShortPause():
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
        listVtx = vtxLoopOrder(getEdgeList)
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
            liveShortStop()
        

def liveShortStop():
    cmds.setToolTo("moveSuperContext")
    cmds.polyOptions(dce=0)
    if cmds.objExists('preSelDisp'):
        cmds.setAttr("preSelDisp.creaseLevel", 0)
        cmds.delete('preSelDisp')
    
    
def getPolyFaceCenter(faceName):
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

def vtxLoopOrder(edgelist):
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

def getEdgeRingGroup(selEdges):
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

run()