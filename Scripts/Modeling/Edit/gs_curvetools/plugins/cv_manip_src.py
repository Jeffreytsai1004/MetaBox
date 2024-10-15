"""

License:
This collection of code named GS CurveTools is a property of George Sladkovsky (Yehor Sladkovskyi)
and can not be copied or distributed without his written permission.

GS CurveTools v1.3.1 Studio
Copyright 2023, George Sladkovsky (Yehor Sladkovskyi)
All Rights Reserved

Autodesk Maya is a property of Autodesk, Inc.

Social Media and Contact Links:

Discord Server:       https://discord.gg/f4DH6HQ
Online Store:         https://sladkovsky3d.artstation.com/store
Online Documentation: https://gs-curvetools.readthedocs.io/
Twitch Channel:       https://www.twitch.tv/videonomad
YouTube Channel:      https://www.youtube.com/c/GeorgeSladkovsky
ArtStation Portfolio: https://www.artstation.com/sladkovsky3d
Contact Email:        george.sladkovsky@gmail.com

"""

import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr
import maya.api.OpenMayaUI as omui
import maya.cmds as mc

# API parameters
maya_useNewAPI = True

# Cache and globals
CALLBACK_IDS = []  # Callback IDs cache


# ------------ Functions ------------
def onSelectionChanged(*_):
    DrawOverride.selectionList.clear()
    newSelection = om.MSelectionList()
    try:
        newSelection = om.MGlobal.getRichSelection(False).getSelection()
        DrawOverride.softSelectionActive = True
    except BaseException:
        DrawOverride.softSelectionActive = False
        newSelection = om.MGlobal.getActiveSelectionList()

        hilite = om.MGlobal.getHiliteList()  # type: om.MSelectionList
        if not hilite.isEmpty():
            newSelection.merge(hilite)
    DrawOverride.selectionList = newSelection


# ------------ Data Classes ----------------------
# Holds all the data for a single CV point
PointData = {
    "curveIndex": 0,
    "cvIndex": 0,
    "position": om.MPoint(),
    "isSelected": False,
    "hasWeight": False,
    "weight": 1.0,
    "colorMult": 1.0,
    "alphaMult": 1.0,
    "distance": 0.0,
}

# Holds all the data for a single curve point
CurveData = {
    "curveIndex": 0,
    "position": om.MPoint(),
    "color": om.MColor(),
    "pointIndex": 0,
    "distance": 0.0,
}


# ------------ Draw Manager (Locator) ------------
class DrawManagerNode(omui.MPxLocatorNode):
    id = om.MTypeId(0x0013bc41)
    drawDbClassification = "drawdb/geometry/GSCT_CurveTools_DrawManager"
    drawRegistrantId = "GSCT_CurveTools_DrawManagerPlugin"

    # Curve attributes
    aDrawAlwaysOnTop = om.MObject()
    aPointSize = om.MObject()
    aLineWidth = om.MObject()
    aHullWidth = om.MObject()
    aCurveDivisions = om.MObject()
    aDeselectedPointColor = om.MObject()
    aDeselectedPointAlpha = om.MObject()
    aSelectedPointColor = om.MObject()
    aSelectedPointAlpha = om.MObject()
    aCurveColor = om.MObject()
    aCurveAlpha = om.MObject()
    aHullColor = om.MObject()
    aHullAlpha = om.MObject()
    aUseCVDistanceColor = om.MObject()
    aUseCurveDistanceColor = om.MObject()
    aUseHullDistanceColor = om.MObject()
    aDistanceColorMin = om.MObject()
    aDistanceColorMax = om.MObject()
    aOccluderMeshName = om.MObject()
    aUseCVOcclusion = om.MObject()
    aShowCurve = om.MObject()
    aShowHull = om.MObject()
    aLazyUpdate = om.MObject()

    def __init__(self):
        CALLBACK_IDS.append(om.MEventMessage.addEventCallback("SelectionChanged", onSelectionChanged))
        super(DrawManagerNode, self).__init__()

    @staticmethod
    def creator():  # Creator method to be passed in initializePlugin
        return DrawManagerNode()

    @staticmethod
    def initialize():  # Init method to be passed in initializePlugin
        # Init plugs attributes
        numericAttr = om.MFnNumericAttribute()
        typedAttr = om.MFnTypedAttribute()

        # Add attributes
        DrawManagerNode.aDrawAlwaysOnTop = numericAttr.create("drawOnTop", "dot", om.MFnNumericData.kBoolean, True)
        om.MPxNode.addAttribute(DrawManagerNode.aDrawAlwaysOnTop)

        DrawManagerNode.aPointSize = numericAttr.create("pointSize", "psize", om.MFnNumericData.kFloat, 10.0)
        numericAttr.setMin(1)
        numericAttr.setMax(100)
        om.MPxNode.addAttribute(DrawManagerNode.aPointSize)

        DrawManagerNode.aLineWidth = numericAttr.create("lineWidth", "lwidth", om.MFnNumericData.kFloat, 4.0)
        numericAttr.setMin(1)
        numericAttr.setMax(100)
        om.MPxNode.addAttribute(DrawManagerNode.aLineWidth)

        DrawManagerNode.aHullWidth = numericAttr.create("hullWidth", "hwidth", om.MFnNumericData.kFloat, 3.0)
        numericAttr.setMin(1)
        numericAttr.setMax(100)
        om.MPxNode.addAttribute(DrawManagerNode.aHullWidth)

        DrawManagerNode.aCurveDivisions = numericAttr.create("curveDivisions", "crvdiv", om.MFnNumericData.kInt, 5)
        numericAttr.setMin(2)
        numericAttr.setMax(64)
        om.MPxNode.addAttribute(DrawManagerNode.aCurveDivisions)

        DrawManagerNode.aDeselectedPointColor = numericAttr.create("deselectedPointColor", "dpcolor", om.MFnNumericData.k3Float)
        numericAttr.default = (1.0, 0, 0)
        numericAttr.usedAsColor = True
        om.MPxNode.addAttribute(DrawManagerNode.aDeselectedPointColor)

        DrawManagerNode.aDeselectedPointAlpha = numericAttr.create("deselectedPointAlpha", "dpalpha", om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aDeselectedPointAlpha)

        DrawManagerNode.aSelectedPointColor = numericAttr.create("selectedPointColor", "spcolor", om.MFnNumericData.k3Float)
        numericAttr.default = (0, 1.0, 0)
        numericAttr.usedAsColor = True
        om.MPxNode.addAttribute(DrawManagerNode.aSelectedPointColor)

        DrawManagerNode.aSelectedPointAlpha = numericAttr.create("selectedPointAlpha", "spalpha", om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aSelectedPointAlpha)

        DrawManagerNode.aCurveColor = numericAttr.create("curveColor", "ccolor", om.MFnNumericData.k3Float)
        numericAttr.default = (0, 0, 1.0)
        numericAttr.usedAsColor = True
        om.MPxNode.addAttribute(DrawManagerNode.aCurveColor)

        DrawManagerNode.aCurveAlpha = numericAttr.create("curveAlpha", "calpha", om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aCurveAlpha)

        DrawManagerNode.aHullColor = numericAttr.create("hullColor", "hcolor", om.MFnNumericData.k3Float)
        numericAttr.default = (0.5, 0, 0.5)
        numericAttr.usedAsColor = True
        om.MPxNode.addAttribute(DrawManagerNode.aHullColor)

        DrawManagerNode.aHullAlpha = numericAttr.create("hullAlpha", "halpha", om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aHullAlpha)

        DrawManagerNode.aUseCVDistanceColor = numericAttr.create("useCVDistanceColor", "usecvdcolor", om.MFnNumericData.kBoolean, True)
        om.MPxNode.addAttribute(DrawManagerNode.aUseCVDistanceColor)

        DrawManagerNode.aUseHullDistanceColor = numericAttr.create(
            "useHullDistanceColor", "usehulldcolor", om.MFnNumericData.kBoolean, True)
        om.MPxNode.addAttribute(DrawManagerNode.aUseHullDistanceColor)

        DrawManagerNode.aUseCurveDistanceColor = numericAttr.create(
            "useCurveDistanceColor", "usecurvedcolor", om.MFnNumericData.kBoolean, True)
        om.MPxNode.addAttribute(DrawManagerNode.aUseCurveDistanceColor)

        DrawManagerNode.aDistanceColorMin = numericAttr.create("distanceColorMin", "dcolormin", om.MFnNumericData.kFloat, 0.25)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aDistanceColorMin)

        DrawManagerNode.aDistanceColorMax = numericAttr.create("distanceColorMax", "dcolormax", om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        om.MPxNode.addAttribute(DrawManagerNode.aDistanceColorMax)

        DrawManagerNode.aOccluderMeshName = typedAttr.create("occluderMeshName", "oclmeshname", om.MFnData.kString)
        om.MPxNode.addAttribute(DrawManagerNode.aOccluderMeshName)

        DrawManagerNode.aUseCVOcclusion = numericAttr.create("useCVOcclusion", "usecvocclusion", om.MFnNumericData.kBoolean, False)
        om.MPxNode.addAttribute(DrawManagerNode.aUseCVOcclusion)

        DrawManagerNode.aShowCurve = numericAttr.create("showCurve", "showcurve", om.MFnNumericData.kBoolean, True)
        om.MPxNode.addAttribute(DrawManagerNode.aShowCurve)

        DrawManagerNode.aShowHull = numericAttr.create("showHull", "showhull", om.MFnNumericData.kBoolean, False)
        om.MPxNode.addAttribute(DrawManagerNode.aShowHull)

        DrawManagerNode.aLazyUpdate = numericAttr.create("lazyUpdate", "lazyupdate", om.MFnNumericData.kBoolean, False)
        om.MPxNode.addAttribute(DrawManagerNode.aLazyUpdate)


# ------------ Draw Manager Data ------------
class UserData(om.MUserData):

    def __init__(self):
        super(UserData, self).__init__(False)

        self.curveDataArray = []  # type: list[dict]
        self.processedCurvePoints = []  # type: list[om.MPointArray]
        self.processedCurveColors = []  # type: list[om.MColorArray]

        self.pointDataArray = []  # type: list[dict]

        # Sorted and colored CV arrays
        self.cvPosArray = om.MPointArray()
        self.cvColorArray = om.MColorArray()

        self.rootCVsArray = om.MPointArray()
        self.rootCVsColors = om.MColorArray()

        # Paired and colored hull arrays
        self.hullPosArray = []  # List of MPointArray
        self.hullColorArray = []  # list of MColorArray

        self.pointSize = 10.0
        self.lineWidth = 4.0
        self.hullWidth = 3.0
        self.curveDivisions = 5  # type: int
        self.selectedPointColor = om.MColor((0, 1.0, 0.0, 1.0))
        self.deselectedPointColor = om.MColor((1.0, 0.0, 0.0, 1.0))
        self.curveColor = om.MColor((0, 0, 1.0, 1.0))
        self.hullColor = om.MColor((.5, 0, .5, 1.0))

        self.drawAlwaysOnTop = True  # type: bool
        self.drawCurve = False  # type: bool
        self.drawHull = False  # type: bool

    def clear(self):
        self.pointDataArray = []
        self.processedCurvePoints = []
        self.processedCurveColors = []
        self.curveDataArray = []
        self.hullPosArray = []
        self.hullColorArray = []
        self.cvPosArray.clear()
        self.cvColorArray.clear()
        self.rootCVsArray.clear()
        self.rootCVsColors.clear()


# ------------ Draw Manager Draw Override ------------
class DrawOverride(omr.MPxDrawOverride):

    nodeState = 0
    selectionInitialized = False
    softSelectionActive = False
    selectionList = om.MSelectionList()
    previousSelectionString = ""

    def __init__(self, obj):
        super(DrawOverride, self).__init__(obj, None)
        self.thisMObject = obj  # type: om.MObject

        # Cache
        self.CVCache = {}  # type: dict[str, om.MPointArray]
        self.splinePointsCache = {}  # type: dict[str, om.MPointArray]
        self.oldCurveDivisions = 0  # type: int

    @staticmethod
    def creator(obj):
        return DrawOverride(obj)

    def supportedDrawAPIs(self):
        return omr.MRenderer.kAllDevices

    def hasUIDrawables(self):
        return True

    def prepareForDraw(self, objPath, cameraPath, frameContext, oldData):
        # type: (om.MDagPath, om.MDagPath, omr.MFrameContext, om.MUserData) -> om.MUserData
        if self.thisMObject.isNull():
            return
        data = oldData
        if not isinstance(data, UserData):
            data = UserData()

        data.clear()

        lazyUpdate = om.MPlug(self.thisMObject, DrawManagerNode.aLazyUpdate).asBool()  # type: bool

        # Get selection list from callback
        if not DrawOverride.selectionList or not lazyUpdate:
            onSelectionChanged()
        sel = DrawOverride.selectionList

        # Clear cache if no selection exists
        if sel.isEmpty():
            self.CVCache.clear()
            self.splinePointsCache.clear()
            return data

        # Getting the node state and bypassing if not "Normal"
        if mc.getAttr(objPath.fullPathName() + '.nodeState') != 0:
            return data

        # Get the data from plugs
        data = self.updateDataFromPlugs(data)

        # Check if selection strings are the same
        if data.drawCurve:
            selectionString = "".join(self.selectionList.getSelectionStrings())  # type: str
            if selectionString != self.previousSelectionString:
                # print("Clearing CV and SplinePointsCache")
                self.CVCache.clear()
                self.splinePointsCache.clear()
                self.previousSelectionString = selectionString

        # Iterate over curves
        processedCurves = set()
        curveIndex = 0  # type: int
        for selIndex in range(sel.length()):
            try:
                dag = sel.getDagPath(selIndex).extendToShape()  # type: om.MDagPath
            except BaseException:
                continue

            if dag.apiType() != 267:
                continue

            fullName = dag.fullPathName()  # type: str

            # Check if current curve was processed already
            if fullName in processedCurves:
                continue

            # Create curve function set and get CVs and curve points
            curve = om.MFnNurbsCurve(dag)
            cvPos, curvePoints = self.processMayaCurve(curve, fullName, data, curveIndex)
            data.curveDataArray += curvePoints
            processedCurves.add(fullName)  # Prevent from double processing of curves

            # Check selection display status (selection context)
            displayStatus = omui.M3dView.displayStatus(dag)  # type: int
            if displayStatus != 4 and displayStatus != 2:
                curveIndex += 1
                continue

            # Check if selection list item has components
            comps = sel.getComponent(selIndex)  # type: tuple[om.MDagPath, om.MObject]
            if comps[1] != om.MObject.kNullObj:
                compFn = om.MFnSingleIndexedComponent(comps[1])

                if compFn.componentType != om.MFn.kCurveCVComponent:
                    data.clear()
                    return data

                selectedIDs = om.MIntArray()
                selectedWeights = om.MFloatArray()
                # Getting soft selection component weights and IDs
                for i in range(compFn.elementCount):
                    weight = 1.0
                    if compFn.hasWeights:
                        weight = compFn.weight(i).influence  # type: float
                    selectedIDs.append(compFn.element(i))
                    selectedWeights.append(weight)
                # Adding selected CVs and their colors to data
                for i, index in enumerate(selectedIDs):
                    pointData = PointData.copy()
                    pointData["curveIndex"] = curveIndex
                    pointData["cvIndex"] = selectedIDs[i]
                    pointData["position"] = om.MPoint(cvPos[index])
                    pointData["isSelected"] = True
                    pointData["hasWeight"] = True
                    pointData["weight"] = selectedWeights[i]
                    data.pointDataArray.append(pointData)
                # Adding deselected CVs and their colors to data
                for i in range(len(cvPos)):
                    if i not in selectedIDs:
                        pointData = PointData.copy()
                        pointData["curveIndex"] = curveIndex
                        pointData["cvIndex"] = i
                        pointData["position"] = om.MPoint(cvPos[i])
                        data.pointDataArray.append(pointData)
            else:
                # If no components selected, just add all the CVs with deselected colors
                for i in range(len(cvPos)):
                    pointData = PointData.copy()
                    pointData["curveIndex"] = curveIndex
                    pointData["cvIndex"] = i
                    pointData["position"] = om.MPoint(cvPos[i])
                    data.pointDataArray.append(pointData)
            curveIndex += 1

        # Skip everything else if there were no processed curves
        if not processedCurves:
            data.clear()
            return data

        # Process draw indices (depth sorting)
        camera = om.MFnCamera(cameraPath)
        camTransform = om.MFnDagNode(camera.parent(0))
        camTransformMatrix = camTransform.transformationMatrix()  # type: om.MMatrix
        cameraPoint = om.MPoint(
            camTransformMatrix.getElement(3, 0),
            camTransformMatrix.getElement(3, 1),
            camTransformMatrix.getElement(3, 2)
        )

        # Add camera distances
        for point in data.pointDataArray:
            point["distance"] = point["position"].distanceTo(cameraPoint)
        data.pointDataArray.sort(key=lambda p: p["distance"], reverse=True)

        # Ray-casting for occlusion of verts
        useOcclusion = om.MPlug(self.thisMObject, DrawManagerNode.aUseCVOcclusion).asBool()  # type: bool
        if useOcclusion:
            self.calculateOcclusion(data, cameraPoint)

        # Optional color changed based on the distance from camera
        useCVDistanceColor = om.MPlug(self.thisMObject, DrawManagerNode.aUseCVDistanceColor).asBool()  # type: bool
        useHullDistanceColor = om.MPlug(self.thisMObject, DrawManagerNode.aUseHullDistanceColor).asBool()  # type: bool
        useCurveDistanceColor = om.MPlug(self.thisMObject, DrawManagerNode.aUseCurveDistanceColor).asBool()  # type: bool

        distanceColorMin = om.MPlug(self.thisMObject, DrawManagerNode.aDistanceColorMin).asFloat()  # type: float
        distanceColorMax = om.MPlug(self.thisMObject, DrawManagerNode.aDistanceColorMax).asFloat()  # type: float
        if distanceColorMax < distanceColorMin:
            distanceColorMax = distanceColorMin

        # Process color multiplier
        if not self.softSelectionActive and (useCVDistanceColor or useHullDistanceColor or useCurveDistanceColor):
            for i, point in enumerate(data.pointDataArray):
                point["colorMult"] = i / float(len(data.pointDataArray))

        # Process curve points
        if data.drawCurve:
            self.processCurvePoints(data, cameraPoint, useCurveDistanceColor, distanceColorMin, distanceColorMax)

        # Process CVs
        for point in data.pointDataArray:
            if point["cvIndex"] == 0:
                x, y, _ = omui.M3dView.active3dView().worldToView(point["position"])
                data.rootCVsArray.append(om.MPoint(x, y, 0))
                rootColor = om.MColor()
                if point["isSelected"]:
                    rootColor = data.selectedPointColor
                    if useCVDistanceColor:
                        rootColor = data.selectedPointColor * max(point["weight"] * point["colorMult"] * distanceColorMax, distanceColorMin)
                else:
                    rootColor = data.deselectedPointColor
                    if useCVDistanceColor:
                        rootColor = data.deselectedPointColor * max(point["colorMult"] * distanceColorMax, distanceColorMin)
                data.rootCVsColors.append(rootColor)

            data.cvPosArray.append(point["position"])
            color = om.MColor()
            if point["isSelected"]:
                if useCVDistanceColor:
                    color = data.selectedPointColor * max(point["weight"] * point["colorMult"] *
                                                          distanceColorMax, distanceColorMin)  # type: om.MColor
                else:
                    color = data.selectedPointColor * max(point["weight"] * distanceColorMax, distanceColorMin)  # type: om.MColor
            else:
                color = data.deselectedPointColor
                if useCVDistanceColor:
                    color = data.deselectedPointColor * max(point["colorMult"] * distanceColorMax, distanceColorMin)
            color.a = color.a * point["alphaMult"]
            data.cvColorArray.append(color)

        # Process hull points
        if data.drawHull:
            self.processHullPoints(data, useHullDistanceColor, distanceColorMin, distanceColorMax)
        else:
            data.hullPosArray = []
            data.hullColorArray = []

        return data

    def addUIDrawables(self, objPath, drawManager, frameContext, userData):
        # type: (om.MDagPath, omr.MUIDrawManager, omr.MFrameContext, om.MUserData) -> None
        if not isinstance(userData, UserData):
            return

        if mc.getAttr(objPath.fullPathName() + '.nodeState') != 0:
            return

        if userData.drawAlwaysOnTop:
            drawManager.beginDrawInXray()
        else:
            drawManager.beginDrawable()

        # Draw curve
        if userData.drawCurve:
            drawManager.setLineWidth(userData.lineWidth)
            for i in range(len(userData.processedCurvePoints)):
                drawManager.mesh(drawManager.kLines, userData.processedCurvePoints[i], None,
                                 userData.processedCurveColors[i], None, None)

        # Draw hull
        if userData.drawHull:
            for i in range(len(userData.hullPosArray)):
                drawManager.setLineWidth(userData.hullWidth)
                drawManager.mesh(drawManager.kLines,
                                 userData.hullPosArray[i],
                                 None,
                                 userData.hullColorArray[i])

        # Draw CVs
        if len(userData.cvPosArray) > 0:
            drawManager.setPointSize(userData.pointSize)
            drawManager.mesh(drawManager.kPoints,
                             userData.cvPosArray,
                             None,
                             userData.cvColorArray)
            # Draw root CV
            drawManager.setLineWidth(1.0)
            for i in range(len(userData.rootCVsArray)):
                drawManager.setColor(userData.rootCVsColors[i])
                drawManager.circle2d(userData.rootCVsArray[i], userData.pointSize / 2.0 + 4.0, False)

        if userData.drawAlwaysOnTop:
            drawManager.endDrawInXray()
        else:
            drawManager.endDrawable()

    def updateDataFromPlugs(self, data):
        # type: (UserData) -> UserData
        # Getting attributes
        data.drawAlwaysOnTop = om.MPlug(self.thisMObject, DrawManagerNode.aDrawAlwaysOnTop).asBool()
        data.pointSize = om.MPlug(self.thisMObject, DrawManagerNode.aPointSize).asFloat()
        data.lineWidth = om.MPlug(self.thisMObject, DrawManagerNode.aLineWidth).asFloat()
        data.hullWidth = om.MPlug(self.thisMObject, DrawManagerNode.aHullWidth).asFloat()
        data.curveDivisions = om.MPlug(self.thisMObject, DrawManagerNode.aCurveDivisions).asInt()

        # Selected points color
        selectedPointColorPlug = om.MPlug(self.thisMObject, DrawManagerNode.aSelectedPointColor).asMObject()  # type: om.MObject
        selectedPointColorData = om.MFnNumericData(selectedPointColorPlug)
        data.selectedPointColor = om.MColor(selectedPointColorData.getData())
        pointAlphaPlug = om.MPlug(self.thisMObject, DrawManagerNode.aSelectedPointAlpha)
        data.selectedPointColor.a = pointAlphaPlug.asFloat()

        # Deselected points color
        deselectedPointColorPlug = om.MPlug(self.thisMObject, DrawManagerNode.aDeselectedPointColor).asMObject()  # type: om.MObject
        deselectedPointColorData = om.MFnNumericData(deselectedPointColorPlug)
        data.deselectedPointColor = om.MColor(deselectedPointColorData.getData())
        pointAlphaPlug = om.MPlug(self.thisMObject, DrawManagerNode.aDeselectedPointAlpha)
        data.deselectedPointColor.a = pointAlphaPlug.asFloat()

        # Curve color
        curveColorPlug = om.MPlug(self.thisMObject, DrawManagerNode.aCurveColor).asMObject()  # type: om.MObject
        curveColorData = om.MFnNumericData(curveColorPlug)
        data.curveColor = om.MColor(curveColorData.getData())
        curveAlphaPlug = om.MPlug(self.thisMObject, DrawManagerNode.aCurveAlpha)
        data.curveColor.a = curveAlphaPlug.asFloat()

        # Hull color
        hullColorPlug = om.MPlug(self.thisMObject, DrawManagerNode.aHullColor).asMObject()  # type: om.MObject
        hullColorPlugData = om.MFnNumericData(hullColorPlug)
        data.hullColor = om.MColor(hullColorPlugData.getData())
        hullAlphaPlug = om.MPlug(self.thisMObject, DrawManagerNode.aCurveAlpha)
        data.hullColor.a = hullAlphaPlug.asFloat()

        data.drawCurve = om.MPlug(self.thisMObject, DrawManagerNode.aShowCurve).asBool()
        data.drawHull = om.MPlug(self.thisMObject, DrawManagerNode.aShowHull).asBool()

        return data

    def processMayaCurve(self, curve, name, data, curveIndex):
        # type: (om.MFnNurbsCurve, str, UserData, int) -> tuple[om.MPointArray, list]
        cvPos = curve.cvPositions(space=om.MSpace.kWorld)  # type: om.MPointArray

        # Check if curve is being drawn at all
        if not data.drawCurve:
            return cvPos, []

        needsUpdate = False
        if self.oldCurveDivisions != data.curveDivisions:
            needsUpdate = True
            self.oldCurveDivisions = data.curveDivisions

        if self.CVCache and name in self.CVCache and len(self.CVCache[name]) == len(cvPos) and not needsUpdate:
            for i, cv in enumerate(cvPos):
                if not cv.isEquivalent(self.CVCache[name][i]):
                    needsUpdate = True
                    break
        else:
            needsUpdate = True

        if not needsUpdate:
            return cvPos, self.splinePointsCache[name]

        self.CVCache.update({name: cvPos})

        splinePoints = []
        knotDomainMin = curve.knotDomain[0]  # type: float
        knotDomainMax = curve.knotDomain[1]  # type: float
        r = knotDomainMin  # type: float
        step = knotDomainMax / (curve.numSpans * data.curveDivisions)  # type: float
        index = 0
        while r < knotDomainMax:
            pointAtParam = curve.getPointAtParam(r, space=om.MSpace.kWorld)  # type: om.MPoint
            curveData = CurveData.copy()
            curveData["curveIndex"] = curveIndex
            curveData["position"] = pointAtParam
            curveData["color"] = data.curveColor
            curveData["pointIndex"] = index
            splinePoints.append(curveData)
            if r + step >= knotDomainMax:
                index += 1
                curveData = CurveData.copy()
                pointAtParam = curve.getPointAtParam(knotDomainMax - 0.0001, space=om.MSpace.kWorld)
                curveData["curveIndex"] = curveIndex
                curveData["position"] = pointAtParam
                curveData["color"] = data.curveColor
                curveData["pointIndex"] = index
                splinePoints.append(curveData)
                break
            r += step
            index += 1
        self.splinePointsCache.update({name: splinePoints})
        return cvPos, splinePoints

    def calculateOcclusion(self, data, cameraPoint):
        # type: (UserData, om.MPoint) -> UserData
        try:
            occluderMeshName = om.MPlug(self.thisMObject, DrawManagerNode.aOccluderMeshName).asString()
            meshSel = om.MSelectionList().add(occluderMeshName)  # type: om.MSelectionList
            meshSel = meshSel.getDagPath(0)
            occluderMesh = om.MFnMesh(meshSel)
            params = occluderMesh.autoUniformGridParams()  # type: om.MMeshIsectAccelParams
            for pointData in data.pointDataArray:
                result = occluderMesh.anyIntersection(om.MFloatPoint(cameraPoint),
                                                      om.MFloatVector(pointData["position"]) - om.MFloatVector(cameraPoint),
                                                      om.MSpace.kWorld,
                                                      1.0,
                                                      False,
                                                      accelParams=params)
                if result:
                    pointData["alphaMult"] = 0.0
        except BaseException:
            pass
        return data

    def processCurvePoints(self, data, cameraPoint, useCurveDistanceColor, colorMin, colorMax):
        # type: (UserData, om.MPoint, bool, float, float) -> UserData
        for curve in data.curveDataArray:
            curve["distance"] = curve["position"].distanceTo(cameraPoint)

        min_e = min(data.curveDataArray, key=lambda x: x["distance"])  # type: dict
        max_e = max(data.curveDataArray, key=lambda x: x["distance"])  # type: dict

        splitCurves = dict()  # type: dict[int, list[dict]]

        for curvePoint in data.curveDataArray:
            if useCurveDistanceColor:
                invLerp = 1 - (curvePoint["distance"] - min_e["distance"]) / (max_e["distance"] - min_e["distance"])
                curvePoint["color"] = data.curveColor * max(invLerp * colorMax, colorMin)
            splitCurves.setdefault(curvePoint["curveIndex"], []).append(curvePoint)

        processedPointsArray = om.MPointArray()
        processedColorsArray = om.MColorArray()
        for curve in splitCurves.values():
            for i in range(1, len(curve)):
                processedPointsArray.append(om.MPoint(curve[i - 1]["position"]))
                processedPointsArray.append(om.MPoint(curve[i]["position"]))
                processedColorsArray.append(curve[i - 1]["color"])
                processedColorsArray.append(curve[i]["color"])

        data.processedCurvePoints.append(processedPointsArray)
        data.processedCurveColors.append(processedColorsArray)

    def processHullPoints(self, data, distanceColors, colorMin, colorMax):
        # type: (UserData, bool, float, float) -> UserData
        # Split points into different curves
        filteredPoints = dict()  # type: dict[int, dict[int, om.MPoint]]
        filteredColors = dict()  # type: dict[int, dict[int, om.MPoint]]
        for point in data.pointDataArray:
            filteredPoints.setdefault(point["curveIndex"], dict()).update({point["cvIndex"]: point["position"]})
            color = om.MColor()
            if point["isSelected"]:
                if distanceColors:
                    color = data.selectedPointColor * max(point["weight"] * point["colorMult"] * colorMax, colorMin)  # type: om.MColor
                else:
                    color = data.selectedPointColor * max(point["weight"] * colorMax, colorMin)  # type: om.MColor
            else:
                color = data.hullColor
                if distanceColors:
                    color = data.hullColor * max(point["colorMult"] * colorMax, colorMin)
            color.a = point["alphaMult"] * data.hullColor.a
            filteredColors.setdefault(point["curveIndex"], dict()).update({point["cvIndex"]: color})

        for i in range(len(filteredPoints)):  # Curve index
            try:
                pointArray = om.MPointArray()
                colorArray = om.MColorArray()
                for j in range(1, len(filteredPoints[i])):  # CV index
                    pointArray.append(om.MPoint(filteredPoints[i][j - 1]))
                    pointArray.append(om.MPoint(filteredPoints[i][j]))
                    colorArray.append(filteredColors[i][j - 1])
                    colorArray.append(filteredColors[i][j])
                data.hullPosArray.append(pointArray)
                data.hullColorArray.append(colorArray)
            except BaseException:
                pass


'''
# ------------ Init & UnInit Plugin ------------
def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "GeorgeSladkovsky", "1.3", "Any")
    try:
        plugin.registerNode(
            "GSCT_CurveTools_DrawManagerNode",
            DrawManagerNode.id,
            DrawManagerNode.creator,
            DrawManagerNode.initialize,
            om.MPxNode.kLocatorNode,
            DrawManagerNode.drawDbClassification)
    except BaseException:
        sys.stderr.write("Failed to register node\n")
        raise

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(
            DrawManagerNode.drawDbClassification,
            DrawManagerNode.drawRegistrantId,
            DrawOverride.creator)
    except BaseException:
        sys.stderr.write("Failed to register override\n")
        raise


def uninitializePlugin(obj):
    global CALLBACK_IDS
    om.MMessage.removeCallbacks(CALLBACK_IDS)
    CALLBACK_IDS = []
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterNode(DrawManagerNode.id)
    except BaseException:
        sys.stderr.write("Failed to deregister node\n")
        raise

    try:
        omr.MDrawRegistry.deregisterGeometryOverrideCreator(DrawManagerNode.drawDbClassification, DrawManagerNode.drawRegistrantId)
    except BaseException:
        sys.stderr.write("Failed to deregister override\n")
        raise
'''
