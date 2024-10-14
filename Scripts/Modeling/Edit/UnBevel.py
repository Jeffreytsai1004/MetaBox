#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import math
import re

def run():
    selEdge = cmds.filterExpand(expand=True ,sm=32)
    if selEdge:
        #cmds.ConvertSelectionToVertices()
        #cmds.ConvertSelectionToEdges()
        #cmds.select(selEdge,d=1)
        if cmds.objExists('saveSel'):
            cmds.delete('saveSel')
        cmds.sets(name="saveSel", text= "saveSel")
        sortGrp =  getEdgeRingGroup()
        for e in sortGrp:
            cmds.select(e)
            unBevelEdgeLoop()    
        cmds.select(selEdge)
        cmds.ConvertSelectionToVertices()
        cmds.polyMergeVertex(d=0.001, am=0, ch=1)
        cmds.select('saveSel')
        cmds.delete('saveSel')

def unBevelEdgeLoop():
    listVtx = vtxLoopOrder()
    #get angles
    checkA = angleBetweenThreeP(listVtx[1],listVtx[0],listVtx[-1])
    angleA = math.degrees(checkA)
    checkB = angleBetweenThreeP(listVtx[-2],listVtx[-1],listVtx[0])
    angleB = math.degrees(checkB)
    angleC = 180 - angleA -angleB
    distanceC = distanceBetween(listVtx[0],listVtx[-1])
    #solve distanceA and distanceB
    distanceA = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleA))
    distanceB = distanceC / math.sin(math.radians(angleC)) * math.sin(math.radians(angleB))
    oldDistA = distanceBetween(listVtx[-2],listVtx[-1])
    oldDistB = distanceBetween(listVtx[0],listVtx[1])
    #scalarA = distanceA / oldDistA 
    scalarB = distanceB / oldDistB 
    pA = cmds.pointPosition(listVtx[0], w =1)
    pB = cmds.pointPosition(listVtx[1], w =1)
    newP = [0,0,0]
    newP[0] = ((pB[0]-pA[0])*scalarB) + pA[0]
    newP[1] = ((pB[1]-pA[1])*scalarB) + pA[1]
    newP[2] = ((pB[2]-pA[2])*scalarB) + pA[2]
    for i in range(1,len(listVtx)-1):
    #for i in range(len(listVtx)):
        cmds.move(newP[0],newP[1],newP[2],listVtx[i],absolute = 1)

def distanceBetween(p1,p2):
    pA = cmds.pointPosition(p1, w =1)
    pB = cmds.pointPosition(p2, w =1)
    dist = math.sqrt( ((pA[0] - pB[0])**2)  + ((pA[1] - pB[1])**2)  + ((pA[2] - pB[2])**2) )
    return dist
    
def angleBetweenThreeP(pA, pB, pC):
    a = cmds.pointPosition(pA, w =1)
    b = cmds.pointPosition(pB, w =1)
    c = cmds.pointPosition(pC, w =1)
    # Create vectors from points
    ba = [ aa-bb for aa,bb in zip(a,b) ]
    bc = [ cc-bb for cc,bb in zip(c,b) ]
    # Normalize vector
    nba = math.sqrt ( sum ( (x**2.0 for x in ba) ) )
    ba = [ x/nba for x in ba ]
    nbc = math.sqrt ( sum ( (x**2.0 for x in bc) ) )
    bc = [ x/nbc for x in bc ]
    # Calculate scalar from normalized vectors
    scalar = sum ( (aa*bb for aa,bb in zip(ba,bc)) )
    # calculate the angle in radian
    angle = math.acos(scalar)
    return angle

def vtxLoopOrder():
    selEdges = cmds.ls(sl=1,fl=1)
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
        dup.remove(gotNextVtx)
        vftOrder.append(gotNextVtx)
        count +=  1
    vftOrder.append(getHeadTail[1])
    finalList = []
    for v in vftOrder:
        finalList.append(transformNode[0]+'.vtx['+ v + ']' )
    return finalList

def getEdgeRingGroup():
    selEdges = cmds.ls(sl=1,fl=1)
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
        f= map(lambda x: (trans +".e["+ str(x) +"]"), f)
        retEdges.append(f)
    return retEdges