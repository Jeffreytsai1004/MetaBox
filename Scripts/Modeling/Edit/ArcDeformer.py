#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel
import math

# set currentArcCurve and storeEdge as global variables
global currentArcCurve
global storeEdge
currentArcCurve = ""
storeEdge = []

def run():
    if cmds.window("arcDeformerUI", exists = True):
        cmds.deleteUI("arcDeformerUI")
    arcDeformerUI = cmds.window("arcDeformerUI",title = "Arc Deformer", w=320)
    cmds.frameLayout(labelVisible= False)
    cmds.rowColumnLayout(nc=4 ,cw=[(1,5),(2,60),(3,20),(4,180)])
    cmds.text(l ='')
    cmds.text(l ='Curve Type')
    cmds.text(l ='')
    cmds.radioButtonGrp('curveType', nrb=2, sl=1, labelArray2=['Bezier', 'Nurbs'], cw = [(1,100),(2,100)],cc=lambda x: controlNumberSwitch())
    cmds.setParent( '..' )
    cmds.rowColumnLayout(nc=10 ,cw=[(1,10),(2,60),(3,20),(4,50),(5,10),(6,50),(7,10),(8,50),(9,10),(10,95)])
    cmds.text(l ='')
    cmds.text(l ='Options')
    cmds.text(l ='')
    cmds.checkBox('makeArc', label= "Arc" ,v = 1, cc= lambda x: makeArcSwitch())
    cmds.text(l ='')
    cmds.checkBox('snapCurve', label= "Snap" ,v = 1, cc= lambda x: disableEvenSpaceCheckBox())
    cmds.text(l ='')
    cmds.checkBox('evenSpace', label= "Even" ,v = 1)
    cmds.text(l ='')
    cmds.checkBox('cleanCurve', label= "Keep Curve" ,v = 1)
    cmds.setParent( '..' )
    cmds.intSliderGrp('CPSlider', cw3=[80, 30, 180], label = 'Control Point ',  field= 1, min= 2, max= 10, fmx = 500, v = 3 )
    cmds.floatSliderGrp('dropOffSlider' , label = 'DropOff', v = 0.01, cw3=[80, 30, 180], field=1 ,pre = 2, min= 0.01, max= 10)
    cmds.rowColumnLayout(nc=4 ,cw=[(1,120),(2,80),(3,10),(4,80)])
    cmds.text(l ='')
    cmds.button( l= 'Run',  c = lambda x: arcEdgeLoop())
    cmds.text(l ='')
    cmds.button( l= 'Done',  c = lambda x: arcDone())
    cmds.text(l ='')
    cmds.setParent( '..' )
    cmds.showWindow(arcDeformerUI)

def arcDone():
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

def arcEdgeLoop():
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
            getCircleState,listVtx = vtxLoopOrderCheck()
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
                    arcDone()
            selMeshForDeformer = cmds.ls(sl=1,o=1)
            getCircleState,listVtx = vtxLoopOrderCheck()
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

def makeArcSwitch():# min point for Nurbs are 4 point
    goArc = cmds.checkBox('makeArc', q=1 ,v = 1)
    curveT = cmds.radioButtonGrp('curveType', q=1, sl=1)
    if goArc == 0:
        cmds.intSliderGrp('CPSlider', e=1, min= 4, v = 4 , fmx = 500)
    else:
        if curveT == 1:
            cmds.intSliderGrp('CPSlider', e=1, min= 2, v = 3, fmx = 500)
        else:
            cmds.intSliderGrp('CPSlider', e=1, min= 4, v = 4, fmx = 500)

def disableEvenSpaceCheckBox():
    snapCheck = cmds.checkBox('snapCurve',q = 1 ,v = 1)
    if snapCheck == 0 :
        cmds.checkBox('evenSpace', e=1 ,en=0)
    else:
        cmds.checkBox('evenSpace', e=1 ,en=1)

def controlNumberSwitch():# min point for Nurbs are 4 point
    curveT = cmds.radioButtonGrp('curveType', q=1, sl=1)
    getCurrentV = cmds.intSliderGrp('CPSlider', q=1 ,v = 1 )
    if curveT == 2:
        cmds.intSliderGrp('CPSlider', e=1, min= 4 )
        if getCurrentV < 4:
            cmds.intSliderGrp('CPSlider', e=1, v= 4 )
    else:
        cmds.intSliderGrp('CPSlider', e=1, min= 2 )

def vtxLoopOrderCheck():
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
    checkCircleState = 0
    if not getHeadTail: #close curve
        checkCircleState = 1
        getHeadTail.append(getNumber[0])
    vftOrder = []
    vftOrder.append(getHeadTail[0])
    count = 0
    while len(dup)> 0 and count < 1000:
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

if __name__ == "__main__":
    run()