import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.api.OpenMaya as OpenMaya
from maya.OpenMaya import MGlobal
import math


def run():
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
    myShape = mc.listRelatives(mayaMesh, shapes=True,f=True)
    checkList = screenVisPoly()
    checkList.remove(myShape[0])
    meshPos = mc.xform(mayaMesh,q=1, ws=1, a=1, piv=1)
    posXXX = [meshPos[0],meshPos[1],meshPos[2]]
    shortDistanceCheck = 10000
    resultFace = []
    resultCV =[]
    resultHitPoint = []
    for c in checkList:
        transNode = mc.listRelatives(c, p=True)
        getFaceDist,getFace,getHitPoint  = getClosestPointOnFace(transNode[0],posXXX)
        #print (getCV, getFaceDist, getFace)
        if getFaceDist < shortDistanceCheck:
            shortDistanceCheck = getFaceDist
            resultFace = getFace
            resultHitPoint = getHitPoint
    return (resultFace,resultHitPoint)



def getClosestPointOnFace(mayaMesh,pos=[0,0,0]):
    mVector = OpenMaya.MVector(pos)#using MVector type to represent position
    selectionList = OpenMaya.MSelectionList()
    selectionList.add(mayaMesh)
    dPath= selectionList.getDagPath(0)
    mMesh=OpenMaya.MFnMesh(dPath)
    ID = mMesh.getClosestPoint(OpenMaya.MPoint(mVector),space=OpenMaya.MSpace.kWorld)[1] #getting closest face ID
    closestPoint= mMesh.getClosestPoint(OpenMaya.MPoint(mVector),space=OpenMaya.MSpace.kWorld)[0]
    cpx = closestPoint[0]
    cpy = closestPoint[1]
    cpz = closestPoint[2]
    hitPointPosition = [cpx,cpy,cpz]
    hitFaceName = (mayaMesh+'.f['+str(ID)+']')
    getFaceDist = math.sqrt( ((pos[0] - cpx)**2)  + ((pos[1]- cpy)**2) + ((pos[2] - cpz)**2))
    return (getFaceDist, hitFaceName,hitPointPosition)



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

if __name__ == "__main__":
    run()
