#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
_____ _____  ______           _____ ______     
/ ____|  __ \|  ____|   /\    / ____|  ____|_   
| |    | |__) | |__     /  \  | (___ | |__ _| |_ 
| |    |  _  /|  __|   / /\ \  \___ \|  __|_   _|
| |____| | \ \| |____ / ____ \ ____) | |____|_|  
\_____|_|  \_\______/_/    \_\_____/|______|    

"""

# import maya.cmds as mc
import maya.api.OpenMaya as om
# import copy

# uses python maya 2

maya_useNewAPI = True

#################


def cPhardEdgeIds(mesh):
    edgeIter = om.MItMeshEdge(mesh)
    ids = []
    while not edgeIter.isDone():
        if not edgeIter.isSmooth:
            ids.append(edgeIter.index())
        edgeIter.next()
    return ids


def cPcompToIds(compdata, cptyp):
    compDataFn = om.MFnComponentListData(compdata)
    # compDataFn
    ids = []
    for i in range(compDataFn.length()):
        curcomp = compDataFn.get(i)
        if curcomp.hasFn(cptyp):
            sic = om.MFnSingleIndexedComponent(curcomp)
            for j in range(sic.elementCount):
                curIdx = sic.element(j)
                ids.append(curIdx)
    return ids


def cPidsToComp(ids, cptyp):
    sic = om.MFnSingleIndexedComponent()
    sic.create(cptyp)  # om.MFn.kMeshEdgeComponent

    sic.addElements(ids)

    compData = om.MFnComponentListData()
    compObj = compData.create()
    compData.add(sic.object())
    return (sic.object(), compObj)


def cPtransformMeshPoints(mesh, mat):
    meshFn = om.MFnMesh(mesh)
    pts = meshFn.getPoints()
    for pt in pts:
        pt *= mat

    meshFn.setPoints(pts)


"""
input: mesh 
output: componentlist
"""

MayaNodeT = om.MPxNode


class CpCurveBevel(MayaNodeT):

    kNodeName = "creasePlusCurveBevel"
    kNodeId = om.MTypeId(0x1154)

    aCvs = None
    aOffset = None
    aSeg = None
    aOffsetFrac = None
    aInputCurve = None
    aOutput = None

    def __init__(self):
        super(CpCurveBevel, self).__init__()

    @classmethod
    def creator(cls):
        return cls()

    @classmethod
    def initialize(cls):

        nAttr = om.MFnNumericAttribute()
        tAttr = om.MFnTypedAttribute()

        cls.aCvs = tAttr.create("cvComponentList", "cvs",
                                om.MFnComponentListData.kComponentList)

        cls.aOffset = nAttr.create("offset", "off", om.MFnNumericData.kFloat)
        nAttr.setMin(0)
        nAttr.default = 0.5
        nAttr.keyable = True
        cls.aSeg = nAttr.create("segments", "seg", om.MFnNumericData.kInt)
        nAttr.setMin(1)
        nAttr.default = 1
        nAttr.keyable = True

        cls.aOffsetFrac = nAttr.create("offsetAsFraction", "oaf",
                                       om.MFnNumericData.kBoolean)
        nAttr.default = False
        nAttr.keyable = True

        cls.aInputCurve = tAttr.create("inCurve", "inc",
                                       om.MFnData.kNurbsCurve)
        cls.aOutput = tAttr.create("outCurve", "out", om.MFnData.kNurbsCurve)
        tAttr.storable = False
        tAttr.writable = False

        MayaNodeT.addAttribute(cls.aCvs)
        MayaNodeT.addAttribute(cls.aOffset)
        MayaNodeT.addAttribute(cls.aSeg)
        MayaNodeT.addAttribute(cls.aOffsetFrac)
        MayaNodeT.addAttribute(cls.aInputCurve)
        MayaNodeT.addAttribute(cls.aOutput)

        MayaNodeT.attributeAffects(cls.aCvs, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aOffset, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aSeg, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aOffsetFrac, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aInputCurve, cls.aOutput)

    def setOutputToCopy(self, data):

        inCurveHandle = data.inputValue(CpCurveBevel.aInputCurve)
        outHandle = data.outputValue(CpCurveBevel.aOutput)
        outHandle.copy(inCurveHandle)
        outHandle.setClean()

    def compute(self, plug, data):

        if plug != CpCurveBevel.aOutput:
            return None

        inCurveHandle = data.inputValue(CpCurveBevel.aInputCurve)

        inCurve = inCurveHandle.asNurbsCurveTransformed()

        inCvsHandle = data.inputValue(CpCurveBevel.aCvs)
        compData = inCvsHandle.data()
        ids = cPcompToIds(compData, om.MFn.kCurveCVComponent)
        #
        inOffset = data.inputValue(CpCurveBevel.aOffset).asFloat()
        inSeg = data.inputValue(CpCurveBevel.aSeg).asInt()
        inFrac = data.inputValue(CpCurveBevel.aOffsetFrac).asBool()

        if len(ids) == 0 or inOffset == 0:
            self.setOutputToCopy(data)
            return

        curveFn = om.MFnNurbsCurve(inCurve)
        curveDegree = curveFn.degree
        curveForm = curveFn.form
        # curveKnots = curveFn.knots()
        curvePts = curveFn.cvPositions()  # to be modified
        numcv = len(curvePts)  # to be modified

        bevelParam = 1 / float(inSeg)
        bevelPts = []

        ids.sort()

        for cvIdx in ids:

            mpos = om.MVector(curvePts[cvIdx])

            if curveForm == curveFn.kPeriodic:
                lpos = om.MVector(curvePts[(cvIdx + numcv -
                                            (1 + curveDegree)) %
                                           (numcv - curveDegree)])
                rpos = om.MVector(curvePts[(cvIdx + 1) %
                                           (numcv - curveDegree)])
            else:
                lpos = om.MVector(curvePts[(cvIdx + numcv - 1) % numcv])
                rpos = om.MVector(curvePts[(cvIdx + 1) % numcv])

            lvec = lpos - mpos
            rvec = rpos - mpos

            lanchor = None
            ranchor = None
            if inFrac:
                lanchor = mpos + (inOffset * lvec)
                ranchor = mpos + (inOffset * rvec)
            else:
                lanchor = mpos + (inOffset * lvec.normal())
                ranchor = mpos + (inOffset * rvec.normal())

            bevelPts.append(lanchor)
            t = 1 * bevelParam
            for i in range(inSeg - 1):
                # (1-t)^2A+2t(1-t)B+t^2C
                res = (1 - t)**2 * lanchor + (2 * t * (1 - t) * mpos) + (
                    t**2 * ranchor)
                bevelPts.append(res)
                t += bevelParam
            bevelPts.append(ranchor)

        #
        i = len(bevelPts) - (inSeg + 1)
        ids.sort(reverse=True)
        for cvIdx in ids:
            curvePts[cvIdx] = bevelPts[i]
            curvePts[cvIdx + 1:cvIdx + 1] = bevelPts[i + 1:i + inSeg + 1]
            i -= (inSeg + 1)

        numcv = len(curvePts)
        if curveForm == curveFn.kPeriodic:
            curvePts[-curveDegree:] = curvePts[:curveDegree]

        if curveDegree == 1:
            knots = [float(i) for i in range(numcv)]

        else:
            knots = [None] * (numcv - curveDegree + (2 * curveDegree) - 1)

            if curveForm == curveFn.kPeriodic:
                knots[:curveDegree] = [
                    float(i) for i in reversed(range(0, -curveDegree, -1))
                ]
                knots[curveDegree:] = [
                    float(i) for i in range(1,
                                             len(knots) - curveDegree + 1)
                ]

            else:
                knots[:curveDegree] = [float(0)] * curveDegree
                knots[-curveDegree:] = [float(numcv - curveDegree)
                                        ] * curveDegree
                knots[curveDegree:-curveDegree] = [
                    float(i)
                    for i in range(1,
                                    len(knots) - (2 * curveDegree) + 1)
                ]

        curveDataFn = om.MFnNurbsCurveData()
        curveDataFn.create()

        knots = om.MDoubleArray(knots)
        curveFn.create(
            curvePts,
            knots,
            curveDegree,
            curveForm,
            False,
            False,
            parent=curveDataFn.object())

        out = data.outputValue(CpCurveBevel.aOutput)
        out.setMObject(curveDataFn.object())
        out.setClean()


class CpCurveToPoly(MayaNodeT):

    kNodeName = "creasePlusCurveToPoly"
    kNodeId = om.MTypeId(0x12547)

    aCount = None
    aRevNorm = None
    aControlPts = None
    aInputCurve = None
    aOutput = None

    def __init__(self):
        super(CpCurveToPoly, self).__init__()

    @classmethod
    def creator(cls):
        return cls()

    @classmethod
    def initialize(cls):

        nAttr = om.MFnNumericAttribute()
        tAttr = om.MFnTypedAttribute()

        cls.aRevNorm = nAttr.create("reverse", "rev",
                                    om.MFnNumericData.kBoolean)
        nAttr.default = False
        nAttr.keyable = True

        cls.aCount = nAttr.create("count", "cnt", om.MFnNumericData.kInt)
        nAttr.setMin(3)
        nAttr.default = 12
        nAttr.keyable = True

        cls.aControlPts = nAttr.create("controlPts", "cv",
                                       om.MFnNumericData.kBoolean)
        nAttr.default = True
        nAttr.keyable = True

        cls.aInputCurve = tAttr.create("inCurve", "inc",
                                       om.MFnData.kNurbsCurve)
        cls.aOutput = tAttr.create("outPoly", "out", om.MFnData.kMesh)
        tAttr.storable = False
        tAttr.writable = False

        MayaNodeT.addAttribute(cls.aRevNorm)
        MayaNodeT.addAttribute(cls.aCount)
        MayaNodeT.addAttribute(cls.aControlPts)
        MayaNodeT.addAttribute(cls.aInputCurve)
        MayaNodeT.addAttribute(cls.aOutput)

        MayaNodeT.attributeAffects(cls.aRevNorm, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aCount, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aControlPts, cls.aOutput)
        MayaNodeT.attributeAffects(cls.aInputCurve, cls.aOutput)

    def setOutputToNull(self, data):
        out = data.outputValue(CpCurveToPoly.aOutput)
        out.setMObject(om.MObject.kNullObj)
        out.setClean()

    def compute(self, plug, data):

        if plug != CpCurveToPoly.aOutput:
            return None

        reverseNormal = data.inputValue(CpCurveToPoly.aRevNorm).asBool()
        inCurveHandle = data.inputValue(CpCurveToPoly.aInputCurve)

        inCurve = inCurveHandle.asNurbsCurveTransformed()

        inCount = data.inputValue(CpCurveToPoly.aCount).asInt()  #
        useCvs = data.inputValue(CpCurveToPoly.aControlPts).asBool()

        curveFn = om.MFnNurbsCurve(inCurve)
        curveForm = curveFn.form
        curveDegree = curveFn.degree
        polyPts = None

        meshDataFn = om.MFnMeshData()
        meshDataFn.create()

        if useCvs:
            if curveForm == curveFn.kPeriodic:
                polyPts = curveFn.cvPositions()[:-curveDegree]
            else:
                polyPts = curveFn.cvPositions()
        else:
            polyPts = []
            domain = curveFn.knotDomain
            param = domain[1] / float(inCount)
            t = 0.0
            for i in range(inCount):
                polyPts.append(curveFn.getPointAtParam(t))
                t += param

        if reverseNormal:
            polyPts = [pt for pt in reversed(polyPts)]
        # create(vertices, polygonCounts, polygonConnects, uValues=None, vValues=None, parent=kNullObj) -> MObject
        meshFn = om.MFnMesh()
        meshFn.create(
            polyPts, [len(polyPts)], [i for i in range(len(polyPts))],
            parent=meshDataFn.object())

        out = data.outputValue(CpCurveToPoly.aOutput)
        out.setMObject(meshDataFn.object())
        out.setClean()


class CpHeIds(MayaNodeT):

    kNodeName = "creasePlusBevelHe"
    kNodeId = om.MTypeId(0x1157)

    aForceComp = None
    aInputMesh = None
    aIds = None

    def __init__(self):

        super(CpHeIds, self).__init__()

        self.numVertices = 0
        self.numPolygons = 0
        self.numNormals = 0
        self.dummycompute = False

    @classmethod
    def creator(cls):
        return cls()

    @classmethod
    def initialize(cls):
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()

        cls.aForceComp = nAttr.create("forceCompute", "fc",
                                      om.MFnNumericData.kBoolean, 0)
        nAttr.default = False
        nAttr.keyable = True

        cls.aInputMesh = tAttr.create("inMesh", "i", om.MFnData.kMesh)

        cls.aIds = tAttr.create("componentList", "cl",
                                om.MFnComponentListData.kComponentList)
        tAttr.storable = False
        tAttr.writable = False

        MayaNodeT.addAttribute(cls.aForceComp)
        MayaNodeT.addAttribute(cls.aInputMesh)
        MayaNodeT.addAttribute(cls.aIds)

    def attrToPlug(self, attr):
        return om.MPlug(self.thisMObject(), attr)

    def setDependentsDirty(self, plug, affect):

        if plug == CpHeIds.aForceComp:
            if self.dummycompute == False:
                self.dummycompute = True
                affect.append(self.attrToPlug(CpHeIds.aIds))
            else:
                self.dummycompute = False
        elif plug == CpHeIds.aInputMesh:
            affect.append(self.attrToPlug(CpHeIds.aIds))

    def compute(self, plug, data):
        if plug != CpHeIds.aIds:
            return None

        doingit = False

        data.inputValue(CpHeIds.aForceComp)
        inMeshHandle = data.inputValue(CpHeIds.aInputMesh)
        inmesh = inMeshHandle.asMesh()
        meshFn = om.MFnMesh(inmesh)

        if self.dummycompute == True:
            doingit = True
        elif (self.numVertices != meshFn.numVertices
              or self.numPolygons != meshFn.numPolygons
              or self.numNormals != meshFn.numNormals):
            doingit = True

        if doingit == True:
            heIds = cPhardEdgeIds(inmesh)
            compObj = cPidsToComp(heIds, om.MFn.kMeshEdgeComponent)[1]

            outIdsHandle = data.outputValue(CpHeIds.aIds)
            outIdsHandle.setMObject(compObj)
            outIdsHandle.setClean()

        if self.dummycompute == True:
            forceCompplug = self.attrToPlug(CpHeIds.aForceComp)
            forceCompplug.setBool(False)


def initializePlugin(obj):

    mplugin = om.MFnPlugin(obj, "Baidhir Hidair", "1.0")

    nodeName = None

    try:
        nodeName = CpHeIds.kNodeName
        mplugin.registerNode(CpHeIds.kNodeName, CpHeIds.kNodeId,
                             CpHeIds.creator, CpHeIds.initialize)

        nodeName = CpCurveBevel.kNodeName
        mplugin.registerNode(CpCurveBevel.kNodeName, CpCurveBevel.kNodeId,
                             CpCurveBevel.creator, CpCurveBevel.initialize)

        nodeName = CpCurveToPoly.kNodeName
        mplugin.registerNode(CpCurveToPoly.kNodeName, CpCurveToPoly.kNodeId,
                             CpCurveToPoly.creator, CpCurveToPoly.initialize)

    except:
        raise Exception('failed to register node: ' + nodeName)


def uninitializePlugin(obj):

    mplugin = om.MFnPlugin(obj)

    nodeName = None

    try:
        nodeName = CpHeIds.kNodeName
        mplugin.deregisterNode(CpHeIds.kNodeId)

        nodeName = CpCurveBevel.kNodeName
        mplugin.deregisterNode(CpCurveBevel.kNodeId)

        nodeName = CpCurveToPoly.kNodeName
        mplugin.deregisterNode(CpCurveToPoly.kNodeId)

    except:
        raise Exception('failed to deregister node: ' + nodeName)