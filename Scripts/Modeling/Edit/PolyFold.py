#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import math
import re
import maya.mel as mel

def updateSNA(new):
    cmds.intField('snapAngleV', e=1, v = new )

def polyFoldDoit():
    global snapStepping
    global pfGeo
    pfGeo = []
    getSV =  cmds.intField('snapAngleV', q=1, v =1 )
    snapStepping = getSV
    checCurrentkHUD =  cmds.headsUpDisplay(lh=1)
    if checCurrentkHUD is not None:
        for t in checCurrentkHUD:
            cmds.headsUpDisplay(t, rem=1)
    global ctx
    ctx = 'plCtx'
    # Delete dragger context if it already exists
    if cmds.draggerContext(ctx, exists=True):
        cmds.deleteUI(ctx)
    # Create dragger context and set it to the active tool
    cmds.draggerContext(ctx, pressCommand = pfPress, rc = pfOff, dragCommand = pfDrag, name=ctx, cursor='crossHair',undoMode='step')
    cmds.setToolTo(ctx)

def pfOff():
    global pfGeo
    cmds.delete(pfGeo[0], ch=1)
    cmds.headsUpDisplay( 'HUDunFoldStep',rem=True)
    cleanList = ('rotOffset','rotBase','rotCC')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    cmds.setToolTo('selectSuperContext')

def currentStep():
    global viewPortCount
    return viewPortCount

def pfPress():
    global ctx
    global screenX,screenY
    global lockCount
    global storeCount
    global viewPortCount
    global pfGeo
    viewPortCount = 0
    lockCount = 50
    storeCount = 0
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    lockX = vpX
    cmds.headsUpDisplay( 'HUDunFoldStep', section=1, block=0, blockSize='large', label='Fold Angle', labelFontSize='large', command=currentStep, atr=1)
    selFace = []
    selFace = cmds.filterExpand(expand=True ,sm=34)
    if selFace:
        pfGeo = cmds.ls(hl=1)
        cmds.delete(pfGeo[0], ch=1)
    cleanList = ('rotOffset','rotBase','rotCC')
    for c in cleanList:
        if cmds.objExists(c):
            cmds.delete(c)
    selGeo = cmds.ls(hl=1)
    cmds.ConvertSelectionToEdgePerimeter()
    cmds.polySelectConstraint(mode =2, type = 0x8000 ,where =2)
    cmds.polySelectConstraint(m =0,w=0)
    getEdges = cmds.ls(sl=1,fl=1)
    midEdge = getEdges[int((len(getEdges)/2))]
    cmds.select(midEdge)
    cmds.polySelectConstraint(type=0x8000, propagate=4)
    cmds.polySelectConstraint(m =0,w=0,propagate=0)
    contEdges = cmds.ls(sl=1,fl=1)
    commonList = list(set(getEdges) - (   set(getEdges) - set(contEdges)  )    )
    cmds.select(commonList)
    listVtx = vtxLoopOrder(commonList)
    pA = cmds.pointPosition(listVtx[0], w =1)
    pB = cmds.pointPosition(listVtx[-1], w =1)
    cmds.group( em=True, name='rotBase')
    cmds.setAttr('rotBase.translateX',pA[0])
    cmds.setAttr('rotBase.translateY',pA[1])
    cmds.setAttr('rotBase.translateZ',pA[2])
    cmds.group( em=True, name='rotAim')
    cmds.setAttr('rotAim.translateX',pB[0])
    cmds.setAttr('rotAim.translateY',pB[1])
    cmds.setAttr('rotAim.translateZ',pB[2])
    consNode = cmds.aimConstraint(('rotAim'),('rotBase'),offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType='scene')
    cmds.select(selFace)
    cmds.CreateCluster()
    checkClusterName = cmds.ls(sl=1,fl=1,typ='transform')
    cmds.rename(checkClusterName, 'rotCC')
    newNode = cmds.duplicate('rotBase',rr=1)
    cmds.rename(newNode[0],'rotOffset')
    cmds.parent('rotOffset', 'rotBase')
    cmds.delete('rotBase',constraints=1)
    cmds.setAttr('rotOffset.rotateX',0)
    cmds.setAttr('rotOffset.rotateY',0)
    cmds.setAttr('rotOffset.rotateZ',0)
    cmds.parent('rotCC','rotOffset')
    cmds.select(selFace)
    cmd = 'doMenuComponentSelection("' + pfGeo[0] +'", "facet");'
    mel.eval(cmd)
    cmds.delete('rotAim')
    cmds.setAttr('rotBase.visibility',0)

def pfDrag():
    global screenX,screenY
    global viewPortCount
    global lockCount
    global storeCount
    global snapStepping
    modifiers = cmds.getModifiers()
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, dragPoint=True)
    stepping = snapStepping
    if(modifiers == 1):
        if screenX > vpX:
            lockCount = lockCount - 1
        else:
            lockCount = lockCount + 1
        screenX = vpX

        if lockCount < -360:
            lockCount = 360
        elif lockCount > 360:
            lockCount = 360
        getX = int(lockCount / stepping)*stepping
        if storeCount != getX:
            storeCount = getX
            cmds.setAttr('rotOffset.rotateX',storeCount)
            viewPortCount = storeCount
    elif(modifiers == 4):
        if screenX > vpX:
            lockCount = lockCount - 5
        else:
            lockCount = lockCount + 5
        screenX = vpX

        if lockCount < -360:
            lockCount = 360
        elif lockCount > 360:
            lockCount = 360
        getX = int(lockCount / stepping)*stepping
        if storeCount != getX:
            storeCount = getX
            cmds.setAttr('rotOffset.rotateX',storeCount)
            viewPortCount = storeCount
    else:
        if screenX > vpX:
            lockCount = lockCount -1
        else:
            lockCount = lockCount + 1
        screenX = vpX
        if lockCount < -360:
            lockCount = 360
        elif lockCount > 360:
            lockCount = 360
        cmds.setAttr('rotOffset.rotateX',lockCount)
        viewPortCount = lockCount

    cmds.refresh(f=True)

def vtxLoopOrder(edgelist):
    selEdges = edgelist
    #print(selEdges)
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

def run():
    if cmds.window("polyFoldDoitUI", exists = True):
        cmds.deleteUI("polyFoldDoitUI")
    polyFoldDoitUI = cmds.window("polyFoldDoitUI",title = "Poly Fold", w=340)
    cmds.frameLayout(labelVisible= False)
    cmds.text(l ='')
    cmds.rowColumnLayout(nc=15 ,cw=[(1,5),(2,80),(3,40),(4,5),(5,20),(6,5),(7,20),(8,5),(9,20),(10,5),(11,20),(12,5),(13,20),(14,5),(15,50)])
    cmds.text(l ='')
    cmds.text(l ='Snap Angle:')
    cmds.intField('snapAngleV', v = 15 )
    cmds.text(l ='')
    cmds.button( l= '5',  c= lambda x: updateSNA(5))
    cmds.text(l ='')
    cmds.button( l= '10', c= lambda x: updateSNA(10))
    cmds.text(l ='')
    cmds.button( l= '15', c= lambda x: updateSNA(15))
    cmds.text(l ='')
    cmds.button( l= '30', c= lambda x: updateSNA(30))
    cmds.text(l ='')
    cmds.button( l= '45', c= lambda x: updateSNA(45))
    cmds.text(l ='')
    cmds.iconTextButton(style='textOnly', l='Fold', rpt=1,bgc = [0.2,0.2,0.2], c=polyFoldDoit)
    cmds.setParent( '..' )
    cmds.text(l ='')
    cmds.showWindow(polyFoldDoitUI)

if __name__ == "__main__":
    run()