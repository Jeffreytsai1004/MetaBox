#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sys
"""
_____ _____  ______           _____ ______     
/ ____|  __ \|  ____|   /\    / ____|  ____|_   
| |    | |__) | |__     /  \  | (___ | |__ _| |_ 
| |    |  _  /|  __|   / /\ \  \___ \|  __|_   _|
| |____| | \ \| |____ / ____ \ ____) | |____|_|  
\_____|_|  \_\______/_/    \_\_____/|______|    

"""

import math

from MayaUndoRun import mayaUndoRun
import maya.cmds as mc
import maya.mel as mel
import maya.api.OpenMaya as om

import CreasePlusExcept as crepexcept
import CreasePlusBase as crep
import CreasePlusNodes
import importlib

# TODO remove reloads
# crep = importlib.reload(crep)
# CreasePlusNodes = importlib.reload(CreasePlusNodes)

# uses python maya 2

maya_useNewAPI = True

def cPmayaScriptDir():
    return mc.internalVar(usd=True)

def cPmainDir():
    return cPmayaScriptDir() + 'CreasePlus/'

# GLOBALS

__ = str(CreasePlusNodes)
__ = __[__.find(" \'") + 2:__.find("\' from")]
__ = __[__.rfind('.') + 1:]

global_CP_Nodes_pluginstr = __


# bool namespace
try:
    global_cPboolNamespace
except:
    global_cPboolNamespace = mc.namespace(add='cPbool', parent=':')


def cPaddToMayaNamespace(toRename, newname):
    global global_cPboolNamespace
    if not mc.namespace(exists=global_cPboolNamespace):
        global_cPboolNamespace = mc.namespace(add='cPbool', parent=':')

    return mc.rename(toRename, newname)


#####


def creasePlusShapeShifter():

    sdir = mc.internalVar(
        usd=True) + 'AMTools/AMTScripts/StartShapeShifter.mel'
    ssExist = mel.eval('filetest -f "' + sdir + '";')

    # welcome

    if not ssExist:
        mc.warning(
            'unable to start ShapeShifter, you have to purchase or update ShapeShifter for CREASE+ support.\n'
        )
        return

    mel.eval('source "' + sdir + '";')


def cPgetGoz():
    if mc.about(win=True):
        # for windows
        assumed = "C:/Users/Public/Pixologic/GoZApps/Maya/GoZBrushFromMaya.mel"
        gozTest = mel.eval("filetest -f " + "\"" + assumed + "\";")
        sGoz = "source " + "\"" + assumed + "\";"
        if gozTest == 0:
            mc.warning("To use this feature you need Goz script from Pixologic Zbrush.\n")
            return
        else:
            mel.eval(sGoz)
    else:

        # for mac
        assumed = "/Users/Shared/Pixologic/GoZApps/Maya/GoZBrushFromMaya.mel"
        gozTest = mel.eval("filetest -f " + "\"" + assumed + "\";")
        sGoz = "source " + "\"" + assumed + "\";"
        if gozTest == 0:
            mc.warning("To use this feature you need Goz script from Pixologic Zbrush.\n")
            return
        else:
            mel.eval(sGoz)




def creasePlusGoz():

    osel = mc.ls(sl=True)
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelMesh)

    for shapeStr in sel:
        mc.select(shapeStr, r=True)
        mel.eval(
            'polyCleanupArgList 4 { "0","2","0","0","1","0","0","0","0","1e-005","0","1e-005","0","1e-005","0","-1","0","0" };'
        )
        if len(mc.ls(sl=True, fl=True)):
            mel.eval(
                'polyCleanupArgList 4 { "0","1","0","0","1","0","0","0","0","1e-005","0","1e-005","0","1e-005","0","-1","0","0" };'
            )

    mc.select(osel, r=True)
    cPgetGoz()


@mayaUndoRun
def creasePlusSmooth30():
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSel)

    for shapeStr in sel:
        mc.polySoftEdge(shapeStr, a=30, ch=True)
    mc.select(
        mc.listRelatives(sel, parent=True, fullPath=True, typ='transform'),
        r=True)


# creasePlusDisplayHardEdges(0)


def creasePlusDisplayHardEdges(disp=0):

    # disp = 0 for toggle
    # = 1 to display hard edges
    # = 2 for no display

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    for shapeStr in sel:

        if disp == 0:
            nodisp = mc.polyOptions(shapeStr, q=True, ae=True)[0]
            if nodisp:
                mc.polyOptions(shapeStr, hec=True)
            else:
                mc.polyOptions(shapeStr, ae=True)
        elif disp == 1:
            mc.polyOptions(shapeStr, hec=True)
        elif disp == 2:

            mc.polyOptions(shapeStr, ae=True)
        else:
            raise crepexcept.cPexcept('wrong kwarg value')


@mayaUndoRun
def creasePlusSelHardEdges():
    sel = om.MGlobal.getActiveSelectionList()
    selIt = om.MItSelectionList(sel)

    finalSel = om.MSelectionList()

    while not selIt.isDone():

        obj = selIt.getDependNode()

        if not obj.hasFn(om.MFn.kMesh):

            obj = crep.cPgotoChild(obj, om.MFn.kMesh)

            if not obj.hasFn(om.MFn.kMesh):
                selIt.next()
                continue

        dagp = crep.cPshapeDagPath(obj)
        edgeIter = om.MItMeshEdge(dagp)

        while not edgeIter.isDone():

            if not edgeIter.isSmooth:

                finalSel.add(
                    (dagp, edgeIter.currentItem()), mergeWithExisting=False)

            edgeIter.next()

        selIt.next()

    om.MGlobal.setActiveSelectionList(finalSel)

# @mayaUndoRun
def creasePlusToggleEdgeSmooth():

    sel = om.MGlobal.getActiveSelectionList()
    selIt = om.MItSelectionList(sel)
    selIt.setFilter(om.MFn.kMeshEdgeComponent)

    comps = []
    while not selIt.isDone():
        comps.append(selIt.getComponent())
        selIt.next()

    for comp in comps:
        toHardList = []
        toSoftenList = []

        edgeIter = om.MItMeshEdge(comp[0], comp[1])

        while not edgeIter.isDone():

            compstring = comp[0].partialPathName() + '.e[' + str(
                edgeIter.index()) + ']'

            if edgeIter.isSmooth:
                toHardList.append(compstring)
            else:
                toSoftenList.append(compstring)

            edgeIter.next()

        if len(toHardList):
            mc.polySoftEdge(toHardList, a=0, ch=True)

        if len(toSoftenList):
            mc.polySoftEdge(toSoftenList, a=180, ch=True)

        om.MGlobal.setActiveSelectionList(sel)


def cPdoPolyBevel(selStrings, nname):
    if crep.getmayaver().num > 2016 or (crep.getmayaver().num == 2016  and crep.getmayaver().extnum == 2):
        nodestr = mc.polyBevel3(
            selStrings,
            oaf=False,
            af=True,
            mia=0,
            c=True,
            f=0,
            o=0,
            sg=1,
            ws=True,
            sa=180,
            sn=True,
            ma=180,
            at=180,
        )[0]
    else:
        nodestr = mc.polyBevel3(
            selStrings,
            oaf=False,
            af=True,
            fn=1,
            o=0,
            sg=1,
            ws=True,
            sa=180,
        )[0]
        


    return mc.rename(nodestr, nname)


#

class CpMirrorStat:

    axisStr = 'axis'
    sideStr = 'side'
    posStr = 'position'
    dxs = 'dX'
    dys = 'dY'
    dzs = 'dZ'


def cPmirrorAttrs(nodeString, mirrorNodeStr):
    axisStr = CpMirrorStat.axisStr
    sideStr = CpMirrorStat.sideStr
    posStr = CpMirrorStat.posStr
    dxs = CpMirrorStat.dxs
    dys = CpMirrorStat.dys
    dzs = CpMirrorStat.dzs

    if crep.getmayaver().num > 2016:
        
        if mc.attributeQuery(axisStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + axisStr)
        if mc.attributeQuery(sideStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + sideStr)
        if mc.attributeQuery(posStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + posStr)

        mc.addAttr(
            nodeString,
            ln=axisStr,
            k=True,
            at='enum',
            en='X=0:Y=1:Z=2',
            dv=0,
        )
        mc.addAttr(
            nodeString,
            ln=sideStr,
            k=True,
            at='enum',
            en='+=0:-=1',
            dv=0,
        )
        mc.addAttr(
            nodeString,
            ln=posStr,
            k=True,
            at='floatLinear',
            dv=mc.getAttr(mirrorNodeStr + '.mirrorPosition'))

        mc.connectAttr(nodeString + '.' + axisStr, mirrorNodeStr + '.axis')
        mc.connectAttr(nodeString + '.' + sideStr,
                    mirrorNodeStr + '.axisDirection')
        mc.connectAttr(nodeString + '.' + posStr,
                    mirrorNodeStr + '.mirrorPosition')
        
    else:
            
        if mc.attributeQuery(axisStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + axisStr)
        if mc.attributeQuery(dxs , node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + dxs )
        if mc.attributeQuery(dys , node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + dys )
        if mc.attributeQuery(dzs , node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + dzs )

        mc.addAttr(
            nodeString,
            ln=axisStr,
            k=True,
            at='enum',
            en='+X=0:-X=1:+Y=2:-Y=3:+Z=4:-Z=5',
            dv=0,
        )

        mc.addAttr(
            nodeString,
            ln=dxs,
            k=True,
            at='doubleLinear',
            dv=0.5)
            # dv=mc.getAttr(mirrorNodeStr + '.pivotX'))
        mc.addAttr(
            nodeString,
            ln=dys,
            k=True,
            at='doubleLinear',
            dv=0.5)
            # dv=mc.getAttr(mirrorNodeStr + '.pivotY'))
        mc.addAttr(
            nodeString,
            ln=dzs,
            k=True,
            at='doubleLinear',
            dv=0.5)
            # dv=mc.getAttr(mirrorNodeStr + '.pivotZ'))         

        mc.connectAttr(nodeString + '.' + axisStr, mirrorNodeStr + '.direction')
        mc.connectAttr(nodeString + "." + dxs,  mirrorNodeStr + '.pivotX')
        mc.connectAttr(nodeString + "." + dys,  mirrorNodeStr + '.pivotY')
        mc.connectAttr(nodeString + "." + dzs,  mirrorNodeStr + '.pivotZ')


def creasePlusMirrorCont(nodeString):

    crep.global_cPmirrorCtxStr

    axisStr = CpMirrorStat.axisStr
    sideStr = CpMirrorStat.sideStr
    posStr = CpMirrorStat.posStr
    dxs = CpMirrorStat.dxs
    dys = CpMirrorStat.dys
    dzs = CpMirrorStat.dzs

    cur = None
    if mc.currentCtx() == crep.global_cPmirrorCtxStr:
        cur = crep.cPmirrorIterIncVal()
    else:
        cur = crep.cPmirrorIterSetVal(0)

    mc.dragAttrContext(crep.global_cPmirrorCtxStr, e=True, reset=True)

    if crep.getmayaver().num > 2016:

        if cur == 0:
            mc.dragAttrContext(
                crep.global_cPmirrorCtxStr, e=True, ct=nodeString + '.' + posStr)
    else:
        if cur == 0:
            mc.setAttr(nodeString + "." + axisStr, 0)
        elif cur == 1:
            mc.setAttr(nodeString + "." + axisStr, 2)
        elif cur == 2:
            mc.setAttr(nodeString + "." + axisStr, 4)


    mc.setToolTo(crep.global_cPmirrorCtxStr)


def cPhasMirrorHistory(shape):

    dummy = om.MSelectionList()
    dummy.add(shape)
    dagFn = om.MFnDagNode(dummy.getDependNode(0))
    dagFn.setObject(dagFn.parent(0))
    transfrmStr = dagFn.partialPathName()

    if mc.attributeQuery(CpMirrorStat.axisStr, node=transfrmStr, ex=True):
        destPlugs = mc.connectionInfo(
            transfrmStr + '.' + CpMirrorStat.axisStr, dfs=True)
        for plugStr in destPlugs:
            if mc.nodeType(cPplugNode(plugStr)) == 'polyMirror':
                return True
    else:

        return False

    return False


@mayaUndoRun
def creasePlusMirror():
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelMesh)

    crep.global_cPmirrorCtxStr
    ctxActive = mc.currentCtx() == crep.global_cPmirrorCtxStr

    if ctxActive and cPhasMirrorHistory(sel[0]):
        transformStr = mc.listRelatives(
            sel[0], parent=True, fullPath=True, typ='transform')[0]
        creasePlusMirrorCont(transformStr)
        return

    transformNodes = []
    for shapeStr in sel:

        # shapeStr  = "pCubeShape1"

        transformStr = mc.listRelatives(
            shapeStr, parent=True, fullPath=True, typ='transform')[0]
        transformNodes.append(transformStr)
        mirNode = mc.polyMirrorFace(shapeStr)[0]
        # mc.polyMergeVertex(shapeStr, d=0.015, am=False)
        cPmirrorAttrs(transformStr, mirNode)

    mc.select(transformNodes, r=True)
    creasePlusMirrorCont(transformStr)


class CpBoolOpStat:

    title = 'boolOp'

    unionStr = 'union'
    diffStr = 'difference'
    intersecStr = 'intersect'


def cPboolOpAttrs(nodeString, boolNodeStr):

    mainAttrName = CpBoolOpStat.title

    unionStr = CpBoolOpStat.unionStr
    diffStr = CpBoolOpStat.diffStr
    intersecStr = CpBoolOpStat.intersecStr

    if mc.attributeQuery(mainAttrName, node=nodeString, ex=True):
        mc.deleteAttr(nodeString + '.' + mainAttrName)

    mc.addAttr(
        nodeString,
        ln=mainAttrName,
        k=True,
        at='enum',
        en=unionStr + '=1:' + diffStr + '=2:' + intersecStr + '=3',
        dv=2,
    )

    mc.connectAttr(nodeString + '.' + mainAttrName, boolNodeStr + '.operation')


# creasePlusBoolOpCont("polySurface1")


def creasePlusBoolOpCont(nodeString):

    crep.global_cPboolOpCtxStr

    mainAttrName = CpBoolOpStat.title

    cur = None
    if mc.currentCtx() == crep.global_cPboolOpCtxStr:
        cur = crep.cPboolOpIterIncVal()
    else:
        cur = crep.cPboolOpIterSetVal(0)

    mc.dragAttrContext(crep.global_cPboolOpCtxStr, e=True, reset=True)

    if cur == 0:
        mc.setAttr(nodeString + '.' + mainAttrName, 2)
    elif cur == 1:
        mc.setAttr(nodeString + '.' + mainAttrName, 1)
    elif cur == 2:
        mc.setAttr(nodeString + '.' + mainAttrName, 3)

    mc.setToolTo(crep.global_cPboolOpCtxStr)


def cPhasBoolHistory(shape):
    dummy = om.MSelectionList()
    dummy.add(shape)
    dagFn = om.MFnDagNode(dummy.getDependNode(0))
    dagFn.setObject(dagFn.parent(0))
    transfrmStr = dagFn.partialPathName()

    if mc.attributeQuery(CpBoolOpStat.title, node=transfrmStr, ex=True):
        destPlugs = mc.connectionInfo(
            transfrmStr + '.' + CpBoolOpStat.title, dfs=True)
        for plugStr in destPlugs:
            if mc.nodeType(cPplugNode(plugStr)) == 'polyCBoolOp':
                return True
    else:

        return False

    return False


# @mayaUndoRun
def creasePlusToggleBoolGhost():
    global global_cPboolNamespace
    vs = mc.ls(global_cPboolNamespace + ":*", o=True, v=True)
    ivs = mc.ls(global_cPboolNamespace + ":*", o=True, iv=True)

    if (len(vs)):
        mc.hide(vs)
    elif (len(ivs)):
        mc.showHidden(ivs)


@mayaUndoRun
def creasePlusBool(keepOperands=False):
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelMesh)

    crep.global_cPboolOpCtxStr
    ctxActive = mc.currentCtx() == crep.global_cPboolOpCtxStr

    hasBoolHistory = cPhasBoolHistory(sel[0])

    if ctxActive and hasBoolHistory or len(sel) == 1 and hasBoolHistory:
        curTransfrm = mc.listRelatives(
            sel[0],
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]
        creasePlusBoolOpCont(curTransfrm)
        return
    elif len(sel) < 2:
        raise crepexcept.cPexcept(crep.CpMsg.kSelLeastTwoMesh)

    if keepOperands:
        for curShape in sel[1:]:
            mc.setAttr(curShape + '.visibility', True)
            mc.setAttr(curShape + '.hiddenInOutliner', False)
            mc.setAttr(curShape + '.intermediateObject', False)
            mc.setAttr(curShape + '.overrideShading', True)
            mc.setAttr(curShape + '.overrideColor', 0)
            mc.setAttr(curShape + '.overrideEnabled', False)
        sel[1:] = mc.listRelatives(
            mc.duplicate(sel[1:], renameChildren=True),
            children=True,
            fullPath=True,
            noIntermediate=False,
            typ='mesh')

    newObj = mc.polyCBoolOp(
        sel,
        useCarveBooleans=True,
        classification=1,
        op=2,
        preserveColor=False,
        ch=True,
    )

    if mc.nodeType(newObj[0]) == 'mesh':
        newObj[0] = mc.listRelatives(
            newObj[0],
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]

    dummy = om.MSelectionList()
    dummy.add(newObj[1])

    depFn = om.MFnDependencyNode(dummy.getDependNode(0))
    allPlugs = depFn.getConnections()

    inShapeStrings = set()
    fstShapeStr = None
    for i in range(len(allPlugs)):
        curPlug = allPlugs[i]

        if not curPlug.isDestination:
            continue

        srcPlug = mc.connectionInfo(curPlug.name(), sfd=True)
        srcShapeStr = cPplugNode(srcPlug)
        if mc.nodeType(srcShapeStr) == 'mesh':
            if fstShapeStr == None:
                fstShapeStr = srcShapeStr
            inShapeStrings.add(srcShapeStr)

    global global_cPboolNamespace

    for curShape in inShapeStrings:

        # curShape = next(iter(inShapeStrings))

        if curShape == fstShapeStr:
            continue

        # def creasePlusBool()

        curTransfrm = mc.listRelatives(
            curShape,
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]

        mc.setAttr(curShape + '.visibility', True)
        mc.setAttr(curShape + '.hiddenInOutliner', False)
        mc.setAttr(curShape + '.intermediateObject', False)
        mc.setAttr(curShape + '.overrideEnabled', True)
        mc.setAttr(curShape + '.overrideShading', False)
        mc.setAttr(curShape + '.overrideColor', 4)
        mc.xform(curShape,cp=True)

        if not ((global_cPboolNamespace + ":") in curTransfrm):
            curTransfrm = cPaddToMayaNamespace(
                curTransfrm, global_cPboolNamespace + ":" +
                curTransfrm[curTransfrm.rfind("|") + 1:])

        mc.setAttr(curTransfrm + '.visibility', True)

    cPboolOpAttrs(newObj[0], newObj[1])
    creasePlusBoolOpCont(newObj[0])
    mc.select(newObj[0], r=True)

    # mel.eval("AEdagNodeCommonRefreshOutliners();")

    if crep.getmayaver().num > 2016:
        mel.eval(
            'attributeEditorVisibilityStateChange(`workspaceControl -q -visible AttributeEditor`, "");'
        )


@mayaUndoRun
def creasePlusPanelBool():

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    #

    if len(sel) < 2:
        raise crepexcept.cPexcept(crep.CpMsg.kSelLeastTwoMesh)

    dupl = mc.duplicate(sel, renameChildren=True)

    newObj = mc.polyCBoolOp(
        sel,
        useCarveBooleans=True,
        classification=1,
        op=2,
        preserveColor=False,
        ch=True,
    )[0]
    newObj1 = mc.polyCBoolOp(
        dupl,
        useCarveBooleans=True,
        classification=1,
        op=3,
        preserveColor=False,
        ch=True,
    )[0]
    mc.select([newObj, newObj1], r=True)
    mc.xform(mc.ls(sl=True),cp=True)
    # mc.polyUnite()


class CpHBevelStat:

    offsetStr = 'hOffset'
    divStr = 'hDivisions'
    miterStr = 'hMitering'


def cPhBevelAttrs(nodeString, bevelNodeStr):

    offsetStr = CpHBevelStat.offsetStr
    divStr = CpHBevelStat.divStr
    miterStr = CpHBevelStat.miterStr


    if crep.getmayaver().num > 2016 or (crep.getmayaver().num == 2016 and crep.getmayaver().extnum == 2):
        if mc.attributeQuery(offsetStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + offsetStr)

        if mc.attributeQuery(divStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + divStr)

        if mc.attributeQuery(miterStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + miterStr)

        mc.addAttr(
            nodeString,
            ln=offsetStr,
            k=True,
            at='doubleLinear',
            hnv=True,
            min=0,
            dv=0,
        )
        mc.addAttr(
            nodeString,
            ln=divStr,
            k=True,
            at='long',
            hnv=True,
            min=0,
            dv=1,
        )
        mc.addAttr(
            nodeString,
            ln=miterStr,
            k=True,
            at='enum',
            en='Auto=0:Star=2:Round=3',
            dv=0,
        )

        mc.connectAttr(nodeString + '.' + offsetStr, bevelNodeStr + '.offset')
        mc.connectAttr(nodeString + '.' + divStr, bevelNodeStr + '.segments')
        mc.connectAttr(nodeString + '.' + miterStr, bevelNodeStr + '.mitering')
    else:
        if mc.attributeQuery(offsetStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + offsetStr)

        if mc.attributeQuery(divStr, node=nodeString, ex=True):
            mc.deleteAttr(nodeString + '.' + divStr)

        mc.addAttr(
            nodeString,
            ln=offsetStr,
            k=True,
            at='doubleLinear',
            hnv=True,
            min=0,
            dv=0,
        )
        mc.addAttr(
            nodeString,
            ln=divStr,
            k=True,
            at='long',
            hnv=True,
            min=0,
            dv=1,
        )
        
        mc.connectAttr(nodeString + '.' + offsetStr, bevelNodeStr + '.offset')
        mc.connectAttr(nodeString + '.' + divStr, bevelNodeStr + '.segments')

def cPhasHBevelHistory(shape):
    dummy = om.MSelectionList()
    dummy.add(shape)
    dagFn = om.MFnDagNode(dummy.getDependNode(0))
    dagFn.setObject(dagFn.parent(0))
    transfrmStr = dagFn.partialPathName()

    if mc.attributeQuery(CpHBevelStat.offsetStr, node=transfrmStr, ex=True):
        destPlugs = mc.connectionInfo(
            transfrmStr + '.' + CpHBevelStat.offsetStr, dfs=True)
        for plugStr in destPlugs:
            if mc.nodeType(cPplugNode(plugStr)) == 'polyBevel3':
                return True
    else:

        return False

    return False


# creasePlusBool(keepOperands =True)
# creasePlusHBevelCont("polySurface1")
# creasePlusHBevelCont("pCube1")


def creasePlusHBevelCont(nodeString):

    crep.global_hBevelCtxStr

    offsetStr = CpHBevelStat.offsetStr
    divStr = CpHBevelStat.divStr

    cur = None
    if mc.currentCtx() == crep.global_hBevelCtxStr:
        cur = crep.cPhBevelIterIncVal()
    else:
        cur = crep.cPhBevelIterSetVal(0)

    mc.dragAttrContext(crep.global_hBevelCtxStr, e=True, reset=True)
    if cur == 0:
        mc.dragAttrContext(
            crep.global_hBevelCtxStr, e=True, ct=nodeString + '.' + offsetStr)
    elif cur == 1:
        mc.dragAttrContext(
            crep.global_hBevelCtxStr, e=True, ct=nodeString + '.' + divStr)

    mc.setToolTo(crep.global_hBevelCtxStr)


@mayaUndoRun
def creasePlusBakeHBL():

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    
    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSel)

    mc.setToolTo('moveSuperContext')
    
    
    beveliTransforms = []
    for shapeStr in sel:
        (cpheNode, bevelNode, beveli)= cPisbevelCage(shapeStr)
        if cpheNode and bevelNode and beveli:
            beveliTrans = mc.listRelatives(beveli, parent=True, noIntermediate=False, typ='transform')[0]
            mc.delete(beveliTrans + '.translate', icn=True)
            mc.delete(beveliTrans + '.rotate'   , icn=True)
            mc.delete(beveliTrans + '.scale'    , icn=True)
            mc.delete(beveli, ch=True)
            mc.select(beveli,r=True)
            cPcleanAttrs()
            beveliTransforms.append(beveliTrans)
            try:
                mc.delete(shapeStr)
            except:
                pass
        else:
            (cpheNode, bevelNode, beveli, beveliCage) = cPhasbevelCage(shapeStr)
            if cpheNode and bevelNode and beveli and beveliCage:
                beveliTrans = mc.listRelatives(beveli, parent=True, noIntermediate=False, typ='transform')[0]
                mc.delete(beveliTrans + '.translate', icn=True)
                mc.delete(beveliTrans + '.rotate'   , icn=True)
                mc.delete(beveliTrans + '.scale'    , icn=True)
                mc.delete(beveli, ch=True)
                mc.select( beveli,r=True)
                cPcleanAttrs()
                beveliTransforms.append(beveliTrans)
                try:
                    mc.delete(beveliCage)
                except:
                    pass
    
    if len(beveliTransforms) :
        mc.select(beveliTransforms, r=True)
    else:
        mc.select( cl=True)

@mayaUndoRun
def creasePlusHBevel():

    sel = om.MGlobal.getActiveSelectionList()

    if sel.length() == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSel)

    crep.global_hBevelCtxStr
    ctxActive = mc.currentCtx() == crep.global_hBevelCtxStr

    selIt = om.MItSelectionList(sel)

    principalObjIdx = None
    transformNodes = []
    while not selIt.isDone():

        (shape, __, edges, faces) = crep.cPgetShapeAndCoStrings(selIt)

        if not shape:
            selIt.next()
            continue

        shapeStr = shape.partialPathName()
        
        (cpheNode, bevelNode, beveli)= cPisbevelCage(shapeStr)
        if cpheNode and bevelNode and beveli:
            creasePlusHBevelCont(
                mc.listRelatives(
                beveli,
                parent=True,
                noIntermediate=False,
                typ='transform')[0] 
            )
            return 
        
        
        dagFn = om.MFnDagNode(shape)
        dagFn.setObject(dagFn.parent(0))
        transfrmStr = dagFn.partialPathName()
        transformNodes.append(transfrmStr)

        if ctxActive and cPhasHBevelHistory(shapeStr):
            creasePlusHBevelCont(transfrmStr)
            return
        else:
            ctxActive = False

        edgeStrings = None

        if faces:
            edgeStrings = crep.cPfaceToHardEdgeStrings(shape, faces)
        elif edges:

            edgeStrings = crep.cPedgeToStrings(shape, edges)
        else:

            edgeStrings = crep.cPhardEdgesStrings(shape)

        #

        if len(edgeStrings) == 0:
            selIt.next()
            continue
        elif principalObjIdx == None:
            principalObjIdx = len(transformNodes) - 1

        # mc.polyMergeVertex(transfrmStr, d=0.015, am=False)
        nname = 'hBevel'
        nname = cPdoPolyBevel(edgeStrings, nname)

        cPhBevelAttrs(transfrmStr, nname)

        selIt.next()

    # set selection

    mc.select(transformNodes, r=True)

    #

    if principalObjIdx != None:
        creasePlusHBevelCont(transformNodes[principalObjIdx])
    else:
        raise crepexcept.cPexcept(crep.CpMsg.kNoHardEdges)


def cPplugNode(plugStr):
    return plugStr[:plugStr.find('.')]


def cPhasbevelCage(shpStr):
    
    cpheNode = None
    bevelNode = None
    beveli = None
    beveliCage = None
    
    hists = mc.listHistory(shpStr , bf=False, f=False, lf=True)

    for n in hists:
        if mc.nodeType(n) == 'polyBevel3' and bevelNode == None:
            bevelNode = n
        elif mc.nodeType(n) == CreasePlusNodes.CpHeIds.kNodeName and cpheNode == None:
            cpheNode= n
        if cpheNode and bevelNode:
            break
    
    if cpheNode and bevelNode:
        beveli = shpStr
    
    if cpheNode and bevelNode and beveli:
        plugs = mc.connectionInfo(bevelNode + '.inputPolymesh', sfd=True)      
        if isinstance(plugs, str) and mc.nodeType(cPplugNode(plugs)) == 'mesh':
            beveliCage = cPplugNode(plugs)
        else:
            for plugStr in plugs:
                if mc.nodeType(cPplugNode(plugStr)) == 'mesh':
                    beveliCage = cPplugNode(plugStr)
                    break
    
    return (cpheNode, bevelNode, beveli, beveliCage)



def cPisbevelCage(cageshpstr):

    cpheNode = None
    bevelNode = None
    beveli = None
    
    plugs = mc.connectionInfo(cageshpstr + ".outMesh", dfs=True)
    
    if isinstance(plugs, str) and mc.nodeType(cPplugNode(plugs)) == CreasePlusNodes.CpHeIds.kNodeName:
        cpheNode = cPplugNode(plugs)
    else:
        for plugStr in plugs:
            if mc.nodeType(cPplugNode(plugStr)) == CreasePlusNodes.CpHeIds.kNodeName:
                cpheNode = cPplugNode(plugStr)
                break

    if cpheNode:
        hists = mc.listHistory(cpheNode, bf=False, f=True, lf=True)

        for n in hists:
            if mc.nodeType(n) == 'polyBevel3':
                bevelNode = n
                break
        beveli = hists[-1:][0]
        if mc.nodeType(beveli) != 'mesh':
            beveli = None

    return (cpheNode, bevelNode, beveli)

    

def creasePlusHBevelLiveCmd():
    global global_CP_Nodes_pluginstr

    # mel.eval("print " + global_CP_Nodes_pluginstr + " ;")

    if not mc.pluginInfo(global_CP_Nodes_pluginstr, q=True, loaded=True):
        try:
            mc.loadPlugin(cPmainDir() + global_CP_Nodes_pluginstr + '.py')
        except:
            raise crepexcept.cPexcept(crep.CpMsg.kcPnodePluginNotLoaded)

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    if len(sel) != 1:
        raise crepexcept.cPexcept(crep.CpMsg.kSelOneMesh)
    sel = sel[0]
    mc.select(sel, r=True)
    
    (cpheNode, bevelNode, beveli)= cPisbevelCage(sel)
    if cpheNode and bevelNode and beveli:
        creasePlusHBevelCont(
            mc.listRelatives(
            beveli,
            parent=True,
            noIntermediate=False,
            typ='transform')[0] 
        )
        return 
    
    mc.xform(sel,cp=True)
    creasePlusHBevel()
    srcPlugs = mc.connectionInfo(sel + '.inMesh', sfd=True)
    bevelNode = None
    if isinstance(srcPlugs, str) and mc.nodeType(
            cPplugNode(srcPlugs)) == 'polyBevel3':
        bevelNode = cPplugNode(srcPlugs)
    else:
        for plugStr in srcPlugs:
            if mc.nodeType(cPplugNode(plugStr)) == 'polyBevel3':
                bevelNode = cPplugNode(plugStr)
                break
    srcPlugs = mc.connectionInfo(bevelNode + '.inputPolymesh', sfd=True)

    sourceMesh = None
    if isinstance(srcPlugs, str):
        plugStr = srcPlugs
        if mc.nodeType(cPplugNode(srcPlugs)) == 'mesh':
            sourceMesh = cPplugNode(srcPlugs)
    else:
        plugStr = srcPlugs[0]
        if mc.nodeType(cPplugNode(plugStr)) == 'mesh':
            sourceMesh = cPplugNode(plugStr)

    if not sourceMesh:
        sourceMesh = mc.createNode('mesh')
        mc.disconnectAttr(plugStr, bevelNode + '.inputPolymesh')
        mc.connectAttr(plugStr, sourceMesh + '.inMesh')
        mc.connectAttr(sourceMesh + '.outMesh', bevelNode + '.inputPolymesh')

        sourcetrans = mc.listRelatives(
            sourceMesh,
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]
        seltrans = mc.listRelatives(
            sel,
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]
        mc.xform(sourcetrans,cp=True)
        

        mc.connectAttr(seltrans + '.translate', sourcetrans + '.translate')
        mc.connectAttr(seltrans + '.rotate', sourcetrans + '.rotate')
        mc.connectAttr(seltrans + '.scale', sourcetrans + '.scale')
        mc.disconnectAttr(seltrans + '.translate', sourcetrans + '.translate')
        mc.disconnectAttr(seltrans + '.rotate', sourcetrans + '.rotate')
        mc.disconnectAttr(seltrans + '.scale', sourcetrans + '.scale')
    else:
        mc.setAttr(sourceMesh + '.visibility', True)
        mc.setAttr(sourceMesh + '.hiddenInOutliner', False)
        mc.setAttr(sourceMesh + '.intermediateObject', False)
        newtrans = mc.createNode('transform')
        seltrans = mc.listRelatives(
            sel,
            parent=True,
            fullPath=True,
            noIntermediate=False,
            typ='transform')[0]

        mc.connectAttr(seltrans + '.translate', newtrans + '.translate')
        mc.connectAttr(seltrans + '.rotate', newtrans + '.rotate')
        mc.connectAttr(seltrans + '.scale', newtrans + '.scale')
        mc.disconnectAttr(seltrans + '.translate', newtrans + '.translate')
        mc.disconnectAttr(seltrans + '.rotate', newtrans + '.rotate')
        mc.disconnectAttr(seltrans + '.scale', newtrans + '.scale')

        mc.parent(sourceMesh, newtrans, shape=True, relative=True)

    mc.setAttr(sourceMesh + '.overrideEnabled', True)
    mc.setAttr(sourceMesh + '.overrideShading', False)
    mc.setAttr(sourceMesh + '.overrideColor', 5)

    idsnode = mc.createNode(CreasePlusNodes.CpHeIds.kNodeName)
    mc.connectAttr(sourceMesh + '.outMesh', idsnode + '.i')
    mc.connectAttr(idsnode + '.cl', bevelNode + '.inputComponents')

    sourcetrans = mc.listRelatives(
        sourceMesh,
        parent=True,
        fullPath=True,
        noIntermediate=False,
        typ='transform')[0]
    seltrans = mc.listRelatives(
        sel, parent=True, fullPath=True, noIntermediate=False,
        typ='transform')[0]
    mc.connectAttr(sourcetrans + '.translate', seltrans + '.translate')
    mc.connectAttr(sourcetrans + '.rotate', seltrans + '.rotate')
    mc.connectAttr(sourcetrans + '.scale', seltrans + '.scale')

    mc.setAttr(seltrans + '.' + CpHBevelStat.offsetStr, 0.05)
    mc.select(sourcetrans, r=True)

@mayaUndoRun
def creasePlusHBevelLive():
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelMesh) 
    
    for i in range(len(sel)):
        mc.select(sel[i],r=True)
        creasePlusHBevelLiveCmd()
        if i != len(sel)-1:
            mc.setToolTo("moveSuperContext")


def cPautoCenterpiv():
    if len(mc.ls(sl=True)):
        mc.xform(cp=True)

@mayaUndoRun
def creasePlusDrawCurve():
    mc.setToolTo(crep.global_cPcurveCtxStr)
    mc.scriptJob(cu=True, ro=True, e=['PostToolChanged', cPautoCenterpiv])

@mayaUndoRun
def creasePlusAttachCurve():
    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelLeastTwoCurve)

    newCurve = mc.attachCurve(
        selCurve,
        ch=False,
        rpo=True,
        kmk=True,
        m=0,
        bb=0.5,
        bki=False,
        p=0.1,
    )[0]

    # mc.delete(newCurve, ch=True)

    mc.select(newCurve, r=True)


@mayaUndoRun
def creasePlusCloseCurve():

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelCurve)

    for shapeStr in selCurve:

        curveForm = mc.getAttr(shapeStr + '.form')

        if mc.getAttr(shapeStr + '.degree') == 3:

            # mc.closeCurve( rpo=True)

            if curveForm == 0:
                mc.closeCurve(
                    shapeStr,
                    ch=False,
                    ps=0,
                    rpo=True,
                    bb=0.5,
                    bki=True,
                    p=0.1,
                )
        else:
            if curveForm == 0:
                mc.closeCurve(
                    shapeStr,
                    ch=False,
                    ps=1,
                    rpo=True,
                    bb=0.5,
                    bki=False,
                    p=0.1,
                )

    mc.select(
        mc.listRelatives(
            selCurve, parent=True, fullPath=True, typ='transform'),
        r=True)


@mayaUndoRun
def creasePlusCurveIntersect():

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(selCurve) < 2:
        raise crepexcept.cPexcept(crep.CpMsg.kSelLeastTwoCurve)

    mel.eval('cutCurvePreset(0,1,0.01,6,0,1,0,1,2);')
    mc.select(cl=True)


@mayaUndoRun
def creasePlusCurveDoubleCvs():

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelCurve)

    for shapeStr in selCurve:
        dummy = om.MSelectionList()
        dummy.add(shapeStr)
        curveFn = om.MFnNurbsCurve(dummy.getDependNode(0))
        deg = curveFn.degree

        # mc.select(mc.listRelatives(shapeStr,parent=True,fullPath=True, typ="transform")[0], r=True)

        mel.eval('selectCurveCV all;')

        # newNumCv = (len(mc.ls(sl=True ,fl=True)) * 2)

        mc.rebuildCurve(
            shapeStr,
            ch=True,
            rpo=True,
            rt=0,
            end=1,
            kr=2,
            kcp=False,
            kep=True,
            kt=False,
            s=curveFn.numSpans * 2,
            d=deg,
            tol=0.01,
        )

    mc.select(mc.listRelatives(selCurve, parent=True, fullPath=True), r=True)


def cPsphereSegIntersect(
        q,
        v,
        p,
        r,
):
    a = (v - q).length()**2
    b = 2 * ((v - q) * (q - p))
    c = p.length()**2 + q.length()**2 - 2 * (p * q) - r**2

    sqr = b**2 - 4 * a * c
    if sqr < 0 or a == 0:
        return None
    s = (-b + math.sqrt(sqr)) / (2 * a)
    t = None
    if sqr > 0:
        t = (-b - math.sqrt(sqr)) / (2 * a)

    # intp = q + (s*(v-q))

    return (1 * s, 1 * t)


def cPsegInsideSphere(
        q,
        v,
        p,
        r,
):
    a = (q - p).length()
    b = (v - p).length()

    if a < r and b < r:
        return True
    else:
        return False


# do not use


def creasePlusCurveRebuild(numSeg, numCv=None):

    if numCv != None:
        numSeg = numCv - 1

    if numSeg < 1:
        raise crepexcept.cPexcept(crep.CpMsg.kInvalidFuncArgs)

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelCurve)

    dummy = om.MSelectionList()
    dummy.add(selCurve[0])
    curveFn = om.MFnNurbsCurve(dummy.getDependNode(0))
    polyline = curveFn.cvPositions()
    polyline = [om.MVector(pt) for pt in polyline]

    pllen = float(0)
    for i in range(len(polyline) - 1):
        p0 = polyline[i]
        p1 = polyline[i + 1]
        pllen += (p1 - p0).length()

    param = pllen / float(numSeg)

    # numCv = numSeg+1

    i = 0
    newPolyline = []
    lastPt = polyline[i]
    newPolyline.append(1 * lastPt)
    while len(newPolyline) < numSeg and i < len(polyline) - 1:
        while len(newPolyline) < numSeg and i < len(polyline) - 1:

            p0 = polyline[i]
            p1 = polyline[i + 1]

            if cPsegInsideSphere(p0, p1, lastPt, 1 * param):
                i += 1
                continue

            s = cPsphereSegIntersect(p0, p1, lastPt, 1 * param)[0]

            # respt = p0 + s * (p1-p0)

            if s == None:
                i += 1
                continue

            if 0 <= s <= 1:
                lastPt = p0 + s * (p1 - p0)
                newPolyline.append(1 * lastPt)
                break

            i += 1

    newPolyline.append(1 * polyline[len(polyline) - 1])
    for pt in newPolyline:
        mc.spaceLocator(p=[pt.x, pt.y, pt.z])


# cPhasCurveBevelHistory("curveShape4")


def cPhasCurveBevelHistory(shape):

    # shape = "curveShape2"

    srcPlugs = mc.connectionInfo(shape + '.create', sfd=True)
    if isinstance(srcPlugs, str) and mc.nodeType(
            cPplugNode(srcPlugs)) == CreasePlusNodes.CpCurveBevel.kNodeName:
        return cPplugNode(srcPlugs)
    else:
        for plugStr in srcPlugs:
            if mc.nodeType(cPplugNode(
                    plugStr)) == CreasePlusNodes.CpCurveBevel.kNodeName:
                return cPplugNode(plugStr)

    return None


def creasePlusCurveBevelCont(nodeString):

    # crep.global_cPcurveBevelCtxStr

    cur = None
    if mc.currentCtx() == crep.global_cPcurveBevelCtxStr:
        cur = crep.cPcurveBevelIterIncVal()
    else:
        cur = crep.cPcurveBevelIterSetVal(0)

    mc.dragAttrContext(crep.global_cPcurveBevelCtxStr, e=True, reset=True)
    if cur == 0:
        mc.dragAttrContext(
            crep.global_cPcurveBevelCtxStr, e=True, ct=nodeString + '.offset')
    elif cur == 1:
        mc.dragAttrContext(
            crep.global_cPcurveBevelCtxStr,
            e=True,
            ct=nodeString + '.segments')

    mc.setToolTo(crep.global_cPcurveBevelCtxStr)


@mayaUndoRun
def creasePlusCurveBevelCmd():

    global global_CP_Nodes_pluginstr
    if not mc.pluginInfo(global_CP_Nodes_pluginstr, q=True, loaded=True):
        try:
            mc.loadPlugin(cPmainDir() + global_CP_Nodes_pluginstr + '.py')
        except:
            raise crepexcept.cPexcept(crep.CpMsg.kcPnodePluginNotLoaded)

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)
    if len(selCurve) != 1:
        raise crepexcept.cPexcept(crep.CpMsg.kWorksForOne)

    selCurve = selCurve[0]

    ctxActive = mc.currentCtx() == crep.global_cPcurveBevelCtxStr
    node = None
    try:
        node = cPhasCurveBevelHistory(selCurve)
    except:
        node = None

    if ctxActive and node != None:
        creasePlusCurveBevelCont(node)
        return

    selCvs = mc.filterExpand(mc.ls(sl=True), sm=28, ex=True)
    if selCvs == None:
        raise crepexcept.cPexcept(crep.CpMsg.kSelCurveCv)
    if len(selCvs) == 0:
        if node != None:
            creasePlusCurveBevelCont(node)
            return
        else:
            raise crepexcept.cPexcept(crep.CpMsg.kSelCurveCv)

    node = mc.createNode(CreasePlusNodes.CpCurveBevel.kNodeName)
    newcurveShape = mc.createNode('nurbsCurve')

    mc.setAttr(
        node + '.cvs',
        len(selCvs),
        type='componentList',
        *[curcv[curcv.find('.') + 1:] for curcv in selCvs])

    mc.connectAttr(selCurve + '.worldSpace[0]', node + '.inc')
    mc.connectAttr(node + '.out', newcurveShape + '.create')

    #

    creasePlusCurveBevelCont(node)


@mayaUndoRun
def creasePlusCurveToPolyCmd():

    global global_CP_Nodes_pluginstr
    if not mc.pluginInfo(global_CP_Nodes_pluginstr, q=True, loaded=True):
        try:
            mc.loadPlugin(cPmainDir() + global_CP_Nodes_pluginstr + '.py')
        except:
            raise crepexcept.cPexcept(crep.CpMsg.kcPnodePluginNotLoaded)

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)
    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelCurve)

    for shapeStr in selCurve:
        node = mc.createNode(CreasePlusNodes.CpCurveToPoly.kNodeName)
        npoly = mc.createNode('mesh')

        mc.connectAttr(shapeStr + '.worldSpace[0]', node + '.inc')
        mc.connectAttr(node + '.out', npoly + '.inMesh')

        mc.sets(npoly, e=1, forceElement='initialShadingGroup')

    mc.select(
        mc.listRelatives(npoly, parent=True, fullPath=True, typ='transform'),
        r=True)


@mayaUndoRun
def creasePlusCurveSlice():

    selCurve = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)
    selMesh = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(selCurve) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelCurve)

    if len(selMesh) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelMesh)

    dplane = crep.cPcameraDominantPlane()

    curveDupl = mc.listRelatives(
        mc.duplicate(selCurve[0], renameChildren=True),
        children=True,
        fullPath=True,
        typ='nurbsCurve')[0]

    dagFn = om.MFnDagNode()
    dummy = om.MSelectionList()

    dummy.add(curveDupl)
    dagFn.setObject(dummy.getDependNode(0))

    curveBb = dagFn.boundingBox
    curvemin = curveBb.min
    curvemax = curveBb.max

    # print (curvemin)

    curveWhd = (abs(curvemax.x - curvemin.x), abs(curvemax.y - curvemin.y),
                abs(curvemax.z - curvemin.z))

    curveMaxOffset = 0
    if curveMaxOffset < curveWhd[0]:
        curveMaxOffset = curveWhd[0]
    if curveMaxOffset < curveWhd[1]:
        curveMaxOffset = curveWhd[1]
    if curveMaxOffset < curveWhd[2]:
        curveMaxOffset = curveWhd[2]

    curveDepth = 0

    i = 1
    finalSel = []
    for shapeStr in selMesh:

        # shapeStr = "pCubeShape1"

        dummy.add(shapeStr)
        dagFn.setObject(dummy.getDependNode(i))

        bb = dagFn.boundingBox
        bbmin = bb.min
        bbmax = bb.max
        bbWhd = (abs(bbmax.x - bbmin.x), abs(bbmax.y - bbmin.y),
                 abs(bbmax.z - bbmin.z))

        bbMaxOffset = 0
        if bbMaxOffset < bbWhd[0]:
            bbMaxOffset = bbWhd[0]
        if bbMaxOffset < bbWhd[1]:
            bbMaxOffset = bbWhd[1]
        if bbMaxOffset < bbWhd[2]:
            bbMaxOffset = bbWhd[2]

        curveDepth = bbMaxOffset
        curveDepth += curveMaxOffset + curveDepth * 0.1

        dirIdx = None
        extrudeVec = None
        axisCenter = None
        if dplane == 'x':
            dirIdx = 0
            extrudeVec = [1, 0, 0]
            axisCenter = bb.center.x
        elif dplane == 'y':
            dirIdx = 1
            extrudeVec = [0, 1, 0]
            axisCenter = bb.center.y
        elif dplane == 'z':
            dirIdx = 2
            extrudeVec = [0, 0, 1]
            axisCenter = bb.center.z

        #

        mel.eval(
            'nurbsToPolygonsPref -f 3 -ucr 0 -uch 0 -pt 0 -m 0 -mt 0.1 -mrt 0;'
        )

        mc.optionVar(iv=('extrudeDirectionType', dirIdx))
        mc.optionVar(fv=('extrudeLength', curveDepth))

        nsurface = mc.extrude(
            curveDupl,
            ch=False,
            rn=False,
            po=1,
            et=0,
            upn=0,
            direction=extrudeVec,
            length=curveDepth,
            ro=0,
            sc=1,
            dl=1,
        )[0]

        if mc.getAttr(curveDupl + '.form') == 1:
            mel.eval('polyCloseBorder -ch 0 ' + nsurface)

        mc.xform(nsurface, cp=True)
        mc.delete(nsurface, ch=True)

        if dplane == 'x':
            mel.eval('move -rpr -moveX ' + str(axisCenter) + ';')
        elif dplane == 'y':
            mel.eval('move -rpr -moveY ' + str(axisCenter) + ';')
        elif dplane == 'z':
            mel.eval('move -rpr -moveZ ' + str(axisCenter) + ';')

        mc.select([shapeStr, nsurface], r=True)
        creasePlusPanelBool()
        finalSel += mc.ls(sl=True)
        i += 1

    # creasePlusCurveSlice()

    mc.delete(
        mc.listRelatives(
            curveDupl, parent=True, fullPath=True, typ='transform'))

    # mc.delete(finalSel, ch=True) # delete final sel history

    mc.select(finalSel, r=True)


def cPdoUnfold(shapeStr):      
    if crep.getmayaver().num > 2016:
        mel.eval(
            'u3dUnfold -ite 10 -p 1 -bi 1 -tf 1 -ms 1024 -rs 0 ' + shapeStr + ';')
    else:
        mel.eval(
            'Unfold3D -u -ite 10 -p 1 -bi 1 -tf 1 -ms 1024 -rs 0 ' + shapeStr + ';')


@mayaUndoRun
def creasePlusMakeUv():

    if not mc.pluginInfo('Unfold3D', q=True, loaded=True):
        raise crepexcept.cPexcept("\'Unfold3D\' plugin must be loaded.\n")

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    
    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelMesh)

    for shapeStr in sel:

        faces = mc.polyListComponentConversion(shapeStr, tf=True)
        mc.polyProjection(
            faces,
            ch=True,
            t='planar',
            ibd=True,
            kir=True,
            md='c',
        )

        edgeStrings = crep.cPhardEdgesStrings(shapeStr)

        if len(edgeStrings) == 0:
            raise crepexcept.cPexcept(
                shapeStr + ' has no hard edges, UV generation failed.\n')

        mc.select(edgeStrings, r=True)
        mc.polyMapCut(ch=True)

        cPdoUnfold(shapeStr)
        

    mc.select(
        mc.listRelatives(parent=True, fullPath=True, typ='transform'), r=True)
    if len(mc.ls(sl=True)):
        print('DONE!')


# SUBD TOOLS


def cPapplyCrease(sel, val, clearcrease=False):
    if clearcrease:
        mc.polyCrease(sel, op=2)
    mc.polyCrease(sel, v=val)


def cPdisplayNotSmooth(shapeStr):
    mc.setAttr(shapeStr + '.displaySmoothMesh', 0)


def cPdisplaySmooth(shapeStr):
    mc.setAttr(shapeStr + '.displaySmoothMesh', 2)


def cPsmoothGroupsSubDAttrs(shapeStr, nodestr1, nodestr2):

    # shapeStr = "pCubeShape1"

    transfrmStr = mc.listRelatives(
        shapeStr, parent=True, fullPath=True, typ='transform')[0]
    mc.addAttr(
        transfrmStr,
        k=True,
        ln='baseDiv',
        at='short',
        dv=2,
        hnv=True,
        min=0,
        softMaxValue=5,
    )
    mc.addAttr(
        transfrmStr,
        k=True,
        ln='divisions',
        at='short',
        dv=1,
        hnv=True,
        min=0,
        softMaxValue=5,
    )
    mc.connectAttr(transfrmStr + '.baseDiv', nodestr1 + '.divisions')
    mc.connectAttr(transfrmStr + '.divisions', nodestr2 + '.divisions')


def cPshowCreaseEd():
    mel.eval(
        'python ("from maya.app.general import creaseSetEditor; creaseSetEditor.showCreaseSetEditor()");'
    )


@mayaUndoRun
def creasePlusNocrease():
    objsel = mc.filterExpand(mc.ls(sl=True), ex=True, sm=12)
    if objsel != None:
        mc.polyCrease(op=2)
    else:
        mc.polyCrease(mc.ls(sl=True), op=1)


@mayaUndoRun
def creasePlusSmoothGroupsSubD():
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelMesh)

    mel.eval('LowQualityDisplay;')

    for shapeStr in sel:
        edgeStrings = crep.cPhardEdgesStrings(shapeStr)
        if len(edgeStrings) == 0:
            continue

        mc.polyCrease(shapeStr, op=2)
        mc.polyCrease(edgeStrings, v=5.0)

        nnode1 = mc.polySmooth(shapeStr)[0]

        mc.polyCrease(shapeStr, op=2)

        nnode2 = mc.polySmooth(shapeStr)[0]

        cPsmoothGroupsSubDAttrs(shapeStr, nnode1, nnode2)

    mc.select(
        mc.listRelatives(sel, parent=True, fullPath=True, typ='transform'),
        r=True)


@mayaUndoRun
def creasePlusSubDpreset():

    osel = mc.ls(sl=True)
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelMesh)

    mc.polyOptions(dce=False)
    mel.eval('LowQualityDisplay;')

    for shapeStr in sel:
        smtlvl = cPsetCreaseSmoothLevel(shapeStr)
        mc.setAttr(shapeStr + '.smoothLevel', 2)
        smoothNode = mc.polySmooth(shapeStr)[0]

        mc.setAttr(smoothNode + '.divisions', smtlvl)

    mc.select(osel, r=True)


def cPupdateSmoothLvl():

    edgesel = mc.filterExpand(mc.ls(sl=True), ex=True, sm=32)

    if not edgesel:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSelEdge)

    # mc.polyOptions(dce = False)

    shapeStr = mc.listRelatives(
        edgesel[0], parent=True, fullPath=True, typ='mesh')[0]

    mc.setAttr(shapeStr + '.osdSmoothTriangles', 1)

    cPsetCreaseSmoothLevel(shapeStr)


def cPsetCreaseSmoothLevel(shapeStr):

    # shapeStr = "pCube1"

    maxv = -1.0
    vals = mc.polyCrease(shapeStr + '.e[*]', q=True, v=True)
    for cur in vals:
        if maxv < cur:
            maxv = cur

    # newlvl =  math.ceil(maxv)

    newlvl = float(int(maxv) + 1)

    if newlvl < 1:
        newlvl = 1

    mc.setAttr(shapeStr + '.smoothLevel', newlvl)

    # mc.setAttr(shapeStr + ".smoothLevel", newlvl + 1)

    return newlvl


@mayaUndoRun
def creasePlusWeigthTool():

    objsel = mc.filterExpand(mc.ls(sl=True), ex=True, sm=12)
    edgesel = mc.filterExpand(mc.ls(sl=True), ex=True, sm=32)

    if objsel == None and edgesel == None:
        raise crepexcept.cPexcept(crep.CpMsg.kSelEdgeOrOneMesh)

    if objsel != None:
        edgesel = crep.cPhardEdgesStrings(
            mc.listRelatives(
                objsel[0], children=True, fullPath=True, typ='mesh')[0])
        if len(edgesel) == 0:
            raise crepexcept.cPexcept(crep.CpMsg.kNoHardEdges)

    mc.polyOptions(dce=False)
    shapeStr = mc.listRelatives(edgesel[0], parent=True, fullPath=True)[0]
    mc.setAttr(shapeStr + '.osdSmoothTriangles', 1)
    cPdisplaySmooth(shapeStr)

    crep.global_cPcreaseCtxStr
    mc.setToolTo(crep.global_cPcreaseCtxStr)
    mc.scriptJob(cu=True, ro=True, e=['PostToolChanged', cPupdateSmoothLvl])


@mayaUndoRun
def creasePlusPhysicalCrease():
    # sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    # if len(sel) == 0:
    #     raise crepexcept.cPexcept(crep.CpMsg.kSelMesh)
    
    # mc.select(sel, r=True)
    
    if mc.currentCtx() == crep.global_hBevelCtxStr:
        creasePlusHBevel()
        return None   
    
    creasePlusHBevel()
    
    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    if len(sel) == 0:
        return None
    
    for shapestr in sel:
        transfrmStr = mc.listRelatives(shapestr, parent=True, type="transform")[0]
        bevelNode = None 
        if mc.attributeQuery(CpHBevelStat.offsetStr, node=transfrmStr, ex=True):
            destPlugs = mc.connectionInfo(
                transfrmStr + '.' + CpHBevelStat.offsetStr, dfs=True)
            for plugStr in destPlugs:
                if mc.nodeType(cPplugNode(plugStr)) == 'polyBevel3':
                    bevelNode = cPplugNode(plugStr)
                    break
        
        if bevelNode:
            nname = 'pCrease'
            nname = mc.rename(bevelNode, nname)
            bevelNode = nname
            if crep.getmayaver().num > 2016 or (crep.getmayaver().num == 2016  and crep.getmayaver().extnum == 2):
                mc.setAttr(bevelNode + ".chamfer" , False)
            else:
                mc.setAttr(bevelNode + ".segments", 2)
        else:
            pass
    


@mayaUndoRun
def creasePlusCreasePreset(presetnum):

    # presetnum == 1, 2, 3

    sel = om.MGlobal.getActiveSelectionList()

    if sel.length() == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kNoSel)

    selIt = om.MItSelectionList(sel)

    principalObjIdx = None
    transformNodes = []
    while not selIt.isDone():

        (shape, __, edges, faces) = crep.cPgetShapeAndCoStrings(selIt)

        if not shape:
            selIt.next()
            continue

        shapeStr = shape.partialPathName()
        dagFn = om.MFnDagNode(shape)
        dagFn.setObject(dagFn.parent(0))
        transfrmStr = dagFn.partialPathName()
        transformNodes.append(transfrmStr)

        edgeStrings = None

        if faces:
            edgeStrings = crep.cPfaceToHardEdgeStrings(shape, faces)
        elif edges:

            edgeStrings = crep.cPedgeToStrings(shape, edges)
        else:

            edgeStrings = crep.cPhardEdgesStrings(shape)

        #

        if len(edgeStrings) == 0:
            selIt.next()
            continue
        elif principalObjIdx == None:
            principalObjIdx = len(transformNodes) - 1

        resetCrease = not(faces or edges)
        if presetnum == 1:
            cPapplyCrease(edgeStrings, 2.0, resetCrease)
            cPsetCreaseSmoothLevel(shapeStr)
        elif presetnum == 2:
            cPapplyCrease(edgeStrings, 3.0, resetCrease)
            cPsetCreaseSmoothLevel(shapeStr)
        elif presetnum == 3:
            cPapplyCrease(edgeStrings, 4.0, resetCrease)
            cPsetCreaseSmoothLevel(shapeStr)
        elif presetnum == 0:
            cPapplyCrease(edgeStrings, 0.0, resetCrease)
            cPsetCreaseSmoothLevel(shapeStr)
        else:
            raise crepexcept.cPexcept(crep.CpMsg.kInvalidFuncArgs)

        cPdisplaySmooth(shapeStr)
        selIt.next()

    # set selection

    mc.select(transformNodes, r=True)

    #

    if principalObjIdx == None:
        raise crepexcept.cPexcept(crep.CpMsg.kNoHardEdges)
    else:
        mc.polyOptions(dce=False)


###############


@mayaUndoRun
def cPcleanAttrs():
    sel = mel.eval(
        'listRelatives -p -f `eval("listRelatives -p -f `polyListComponentConversion -tv`")`'
    )
    for trans in sel:
        cusattr = mc.listAttr(trans, ud=True)
        if cusattr != None:
            for a in cusattr:
                mel.eval('deleteAttr -at ' + a + ' ' + trans + ' ;')


def creasePlusLastCtx():
    meshsel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)
    curvesel = crep.cPgetShapeStringsFromSel(om.MFn.kNurbsCurve)

    if len(meshsel):
        shapeStr = meshsel[0]
        trnsfrm = mc.listRelatives(
            meshsel[0], parent=True, fullPath=True, typ='transform')[0]

        if cPhasHBevelHistory(shapeStr):
            creasePlusHBevelCont(trnsfrm)
        elif cPhasBoolHistory(shapeStr):
            creasePlusBoolOpCont(trnsfrm)
        elif cPhasMirrorHistory(shapeStr):
            creasePlusMirrorCont(trnsfrm)
    elif len(curvesel):
        shapeStr = curvesel[0]
        trnsfrm = mc.listRelatives(
            curvesel[0], parent=True, fullPath=True, typ='transform')[0]
        curvebvlnode = cPhasCurveBevelHistory(shapeStr)
        if curvebvlnode != None:
            creasePlusCurveBevelCont(curvebvlnode)


def cPcopyHBevelAttrs(srcnode, targetnode):
    offsetStr = CpHBevelStat.offsetStr
    divStr = CpHBevelStat.divStr
    miterStr = CpHBevelStat.miterStr

    a1 = mc.getAttr(srcnode + '.' + offsetStr)
    a2 = mc.getAttr(srcnode + '.' + divStr)
    a3 = mc.getAttr(srcnode + '.' + miterStr)

    mc.setAttr(targetnode + '.' + offsetStr, a1)
    mc.setAttr(targetnode + '.' + divStr, a2)
    mc.setAttr(targetnode + '.' + miterStr, a3)


@mayaUndoRun
def creasePlusTransferHBevel():

    sel = crep.cPgetShapeStringsFromSel(om.MFn.kMesh)

    if len(sel) == 0:
        raise crepexcept.cPexcept(crep.CpMsg.kSelMesh)

    if not cPhasHBevelHistory(sel[0]):
        raise crepexcept.cPexcept('no Hbevel history found on first object')

    seltrans = mc.listRelatives(
        sel[0], parent=True, fullPath=True, typ='transform')[0]
    for shapeStr in sel[1:]:
        if cPhasHBevelHistory(shapeStr):
            cPcopyHBevelAttrs(seltrans,
                              mc.listRelatives(
                                  shapeStr,
                                  parent=True,
                                  fullPath=True,
                                  typ='transform')[0])


###############


def main():
    return None


if __name__ == '__main__':
    main()