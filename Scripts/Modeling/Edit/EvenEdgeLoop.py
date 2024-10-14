#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc # type: ignore
import maya.mel as mel # type: ignore
import math
import re

def evenEdgeLoopDoitRun(smoothType):
    sel=mc.ls(sl=1,fl=1)
    if sel:
        shape = mc.listRelatives(sel,p=1 )
        mc.displaySmoothness(divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1)
        sortEdgeLoopGrp =  getEdgeRingGroup(0,'')
        for s in sortEdgeLoopGrp:
            mc.select(s)
            evenEdgeLoopDoit(smoothType)
        mc.select(sel)
        cmd = 'doMenuComponentSelection("' + shape[0] +'", "edge");'
        mel.eval(cmd)
        mc.select(sel)

def run():
    if mc.window("evenEdgeLoopDoitUI", exists = True):
        mc.deleteUI("evenEdgeLoopDoitUI")

    evenEdgeLoopDoitUI = mc.window("Even Edge Loop", w = 230, s = 1 ,mxb = False,mnb = False)
    mc.columnLayout(adj=1)
    mc.rowColumnLayout(nc= 5 ,cw=[(1,75),(2,10),(3,75),(4,10),(5,75)])
    mc.button( l= "Average", c = lambda x: evenEdgeLoopDoitRun("even") )
    mc.text(l='')
    mc.button( l= "Arc", c =  lambda x: evenEdgeLoopDoitRun("2P") )
    mc.text(l='')
    mc.button( l= "Straighten ", c =  lambda x: evenEdgeLoopDoitRun("straighten") )
    mc.showWindow(evenEdgeLoopDoitUI)

def evenEdgeLoopDoit(smoothType):
    if mc.objExists('tempEvenCurve'):
        mc.delete('tempEvenCurve')
    sel =mc.ls(sl=1,fl=1)

    getCircleState,listVtx = vtxLoopOrderCheck()
    mc.polyToCurve(form=2, degree=1, conformToSmoothMeshPreview=1)
    mc.rename('tempEvenCurve')
    curveCVs =mc.ls('tempEvenCurve.cv[*]',fl=1)
    posCurve = mc.xform(curveCVs[0], a=1,ws=1, q=1, t=1)
    posEdge = mc.xform(listVtx[0], a=1,ws=1, q=1, t=1)
    if posCurve == posEdge:
        pass
    else:
        listVtx = listVtx[::-1]
    if len(curveCVs)>2:
        if smoothType == '2P':
            if len(curveCVs)>3:
                mc.delete(curveCVs[1:-1])
                mc.rebuildCurve('tempEvenCurve',ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = 2 , d=2, tol=0)
                midA = len(listVtx)/3
                midB = len(listVtx)/3*2
                midA = int(midA)
                midB = int(midB)
                posA = mc.xform(listVtx[midA], q=1, ws=1, t=1)
                posB = mc.xform(listVtx[midB], q=1, ws=1, t=1)
                mc.xform('tempEvenCurve.cv[1]', a=1, ws=1, t = (posA[0],posA[1],posA[2]) )
                mc.xform('tempEvenCurve.cv[2]', a=1, ws=1, t = (posB[0],posB[1],posB[2]) )
                mc.rebuildCurve('tempEvenCurve',ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = (len(listVtx)-1) , d=1, tol=0)
                curveCVs =mc.ls('tempEvenCurve.cv[*]',fl=1)
        elif smoothType == 'straighten ':
            mc.delete(curveCVs[1:-1])
            newNumber = (len(listVtx)-1)
            mc.rebuildCurve('tempEvenCurve',ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = newNumber , d=1, tol=0)
            if newNumber == 2:
                mc.delete('tempEvenCurve.cv[1]','tempEvenCurve.cv[3]')
            curveCVs =mc.ls('tempEvenCurve.cv[*]',fl=1)
        else:
            mc.rebuildCurve('tempEvenCurve',ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s = 0 , d=1, tol=0)
            if len(curveCVs)< 4:
                mc.delete( 'tempEvenCurve.cv[1]', 'tempEvenCurve.cv[3]')
                curveCVs =mc.ls('tempEvenCurve.cv[*]',fl=1)
            posCurve = mc.xform(curveCVs[0], a=1,ws=1, q=1, t=1)
            posEdge = mc.xform(listVtx[0], a=1,ws=1, q=1, t=1)
            posEdge[0] = round(posEdge[0],3)
            posEdge[1] = round(posEdge[1],3)
            posEdge[2] = round(posEdge[2],3)
            posCurve[0] = round(posCurve[0],3)
            posCurve[1] = round(posCurve[1],3)
            posCurve[2] = round(posCurve[2],3)
    for i in range(len(curveCVs)):
        pos = mc.xform(curveCVs[i], a=1,ws=1, q=1, t=1)
        mc.xform(listVtx[i], a=1, ws=1, t = (pos[0],pos[1],pos[2]) )
    mc.delete('tempEvenCurve')

def getEdgeRingGroup(listSort,listInput):
    selEdges = mc.ls(sl=1,fl=1)
    trans = selEdges[0].split(".")[0]
    e2vInfos = mc.polyInfo(selEdges, ev=True)
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
        f= list(map(lambda x: (trans +".e["+ str(x) +"]"), f))
        retEdges.append(f)
    if listSort == 1:
        sortEdgeLoopOrder=[]
        getCircleState,listVtx = vtxLoopOrderCheck(listInput)
        for l in listVtx:
            for r in retEdges:
                checkCvList = mc.ls(mc.polyListComponentConversion( r,fe=True, tv=True), fl=True,l=True)
                if l in checkCvList:
                    sortEdgeLoopOrder.append(r)
        return sortEdgeLoopOrder
    else:
        return retEdges


def vtxLoopOrderCheck():
    selEdges = mc.ls(sl=1,fl=1)
    shapeNode = mc.listRelatives(selEdges[0], fullPath=True , parent=True )
    transformNode = mc.listRelatives(shapeNode[0], fullPath=True , parent=True )
    edgeNumberList = []
    for a in selEdges:
        checkNumber = ((a.split('.')[1]).split('\n')[0]).split(' ')
        for c in checkNumber:
            findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
            if findNumber:
                edgeNumberList.append(findNumber)
    getNumber = []
    for s in selEdges:
        evlist = mc.polyInfo(s,ev=True)
        checkNumber = ((evlist[0].split(':')[1]).split('\n')[0]).split(' ')
        for c in checkNumber:
            findNumber = ''.join([n for n in c.split('|')[-1] if n.isdigit()])
            if findNumber:
                getNumber.append(findNumber)
    dup = set([x for x in getNumber if getNumber.count(x) > 1])
    getHeadTail = list(set(getNumber) - dup)
    checkCircleState = 0
    if not getHeadTail: #close curve
        checkCircleState = 1
        getHeadTail.append(getNumber[0])
    vftOrder = []
    vftOrder.append(getHeadTail[0])
    count = 0
    while len(dup)> 0 and count < 1000:
        checkVtx = transformNode[0]+'.vtx['+ vftOrder[-1] + ']'
        velist = mc.polyInfo(checkVtx,ve=True)
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
        findVtx = mc.polyInfo(checkVtx,ev=True)
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
    if checkCircleState == 0:
        vftOrder.append(getHeadTail[1])
    else:#close curve remove connected vtx
        if vftOrder[0] == vftOrder[1]:
            vftOrder = vftOrder[1:]
        elif vftOrder[0] == vftOrder[-1]:
            vftOrder = vftOrder[0:-1]
    finalList = []
    for v in vftOrder:
        finalList.append(transformNode[0]+'.vtx['+ v + ']' )

    return checkCircleState, finalList
#edge

if __name__ == "__main__":
    run()