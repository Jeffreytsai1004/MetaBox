from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from functools import partial
# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
import math

from . import PlugIt_Global
import importlib
importlib.reload(PlugIt_Global)
from . import PlugIt_CSS

##---------------------------------------------------------------------------------------------------------------- G L O B A L   V A R I A B L E S
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath
LIBRARY_PATH = PlugIt_Global.LIBRARY_PATH
TOOLS_PATH = PlugIt_Global.ToolsPath

# ----------------------------------------------------------------------//  I N I T    V A R
VERSION = mc.about(v=True)
DebugMode = 1
WrapMode = 0
ONEFACE = 0
BendWrapMode = 0
WindowTitle = "P L U G  -  O p t i o n s"
MeshName = "noMeshName"
ScriptJobNum = ""
MelScript_ExtractFace = TOOLS_PATH + 'wzx_ExtractFace.mel'

if VERSION == "2024":
    MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots.mel'
if VERSION == "2023":
    MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots.mel'
if VERSION == "2025":
    MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots.mel'
elif VERSION == "2022" :
    MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots_2022.mel'

def AutoConnect(face):
    selectedFace = face
    # ______ get number of vertice in selected face
    mc.ConvertSelectionToVertices()
    mc.ls(sl=True)
    vertexNumber = len(mc.filterExpand(ex=True, sm=31))
    if vertexNumber < 5:
        return
    mc.select(selectedFace)

    # ______ Found Vertice Number
    face = mc.ls(sl=True)
    mc.ConvertSelectionToEdges()
    mc.sets(n="PlugIt_Temps_VertNum")
    mc.select(mc.sets('Plug_EdgeBorder_set', int="PlugIt_Temps_VertNum"))
    mc.delete("PlugIt_Temps_VertNum")
    mc.ConvertSelectionToVertices()
    allVert = mc.filterExpand(ex=True, sm=31)
    numOfVert = len(allVert) - 2

    # ______
    mc.select(selectedFace)
    mc.Triangulate()
    mc.ConvertSelectionToContainedEdges()
    listOfAllContainsEdge = mc.filterExpand(ex=True, sm=32)
    listEdgesLen_Dict = {}
    for edge in listOfAllContainsEdge:
        # Get the world coordinates for the vertices that make up the current edge.
        ps = mc.xform(edge, q=1, t=1, ws=1)
        p1 = ps[0:3]  # XYZ coords for point 1
        p2 = ps[3:6]
        # Some math
        length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
        listEdgesLen_Dict[edge] = length

    # Sort du plus petit au plus long
    sorted_values = sorted(listEdgesLen_Dict.values())  # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in listEdgesLen_Dict.keys():
            if listEdgesLen_Dict[k] == i:
                sorted_dict[k] = listEdgesLen_Dict[k]

    sortenEdgeFromSelection = list(sorted_dict.keys())[:numOfVert]  # get and keep based on vert num
    mc.select(sortenEdgeFromSelection, d=True)
    mc.Delete()
    mc.SelectAll(d=True)

def PERFORM_PLUG(Plug_Path, oneFace, numberOfEdges):
    # ---------------------------------------------------------------------------------------------------------//  I N I T
    global ONEFACE
    ONEFACE = oneFace

    NumberOfEdges = numberOfEdges


    # ______________________________________________________________________________ Avoid ClashingName
    ClashingName = 0
    TargetMesh_OriginName = mc.ls(sl=True)[0].split(".f")[0]
    if "|" in TargetMesh_OriginName:
        ClashingName = 1
        TargetMesh_OriginNameClashing = TargetMesh_OriginName.split("|")[-1]
    TargetMesh_TempName = mc.rename(TargetMesh_OriginName, "PlugIt_TargetMesh")
    targetMesh_faceSelected = mc.ls(sl=True)

    # ______________________________________________________________________________ UNDO : Duplication Save for Delete Plug
    if mc.objExists("PlugItDupSave_*"):
        mc.select("PlugItDupSave_*")
        mc.delete()

    mc.select("PlugIt_TargetMesh")
    mc.duplicate(n= "PlugIt_TargetMesh_DupSave")
    mc.HideSelectedObjects()
    mc.setAttr("PlugIt_TargetMesh_DupSave.hiddenInOutliner", 1)
    try:
        mel.eval("AEdagNodeCommonRefreshOutliners();")
    except:
        pass


    parentSel = mc.ls(sl = True)
    if parentSel == []:
        pass
    else:
        mc.Unparent()




    # ______________________________________________________________________________ Flat or Curve
    if oneFace == 0:
        mc.select(targetMesh_faceSelected)
        faceSelection = mc.filterExpand(sm=34)
        mc.select(faceSelection[0])
        checkFaceA = mc.polyInfo(fn=True)
        #print(checkFaceA)
        XYZValues_FaceA = [checkFaceA[0][20], checkFaceA[0][21], checkFaceA[0][22], checkFaceA[0][23], checkFaceA[0][24],
                           checkFaceA[0][25]]
        #print("XYZValues_FaceA = " + str(XYZValues_FaceA))

        mc.select(faceSelection[1])
        checkFaceB = mc.polyInfo(fn=True)
        #print(checkFaceB)
        XYZValues_FaceB = [checkFaceB[0][20], checkFaceB[0][21], checkFaceB[0][22], checkFaceB[0][23], checkFaceB[0][24],
                           checkFaceB[0][25]]
        #print("XYZValues_FaceB = " + str(XYZValues_FaceB))

        if XYZValues_FaceA == XYZValues_FaceB:
            FACE_ANGLE_MODE = 0 #Flat
            #print("FLAT")
        else:
            FACE_ANGLE_MODE = 1  # CURVE
            #print("CURVE")
    else:
        FACE_ANGLE_MODE = 0  # Flat
        #print("FLAT")



    # ______________________________________________________________________________ Supp Selection Face
    mc.select(targetMesh_faceSelected)
    mc.ConvertSelectionToEdgePerimeter()
    mc.sets(n="Mesh_EdgeBorder_set")
    mc.select(targetMesh_faceSelected)






    # ______________________________________________________________________________ Extract Mesh Faces
    mc.ls(sl=True)
    mel.eval('source "' + MelScript_ExtractFace + '"')

    # ______________________________________________________________________________ AlignFace Pivot Mode
    if oneFace == 0:
        # ______ Create an empty plane
        extractFace = mc.ls(sl=True)
        dupFaceMatch = mc.duplicate(extractFace, n="PlugIt_DupFace_for_Match")
        mc.ConvertSelectionToFaces()
        mc.ConvertSelectionToContainedEdges()
        mc.DeleteEdge()
        mc.select(dupFaceMatch)
        mc.ConvertSelectionToFaces()
        #______ Align Pivot
        from .Tools import BakeTransformations
        BakeTransformations.BakeTransformations(optionBox=False)
    else:
        # ______ Align Pivot Classic
        mc.select("PlugIt_TargetMesh1")
        extractFace = "PlugIt_TargetMesh1"
        dupFaceMatch = "PlugIt_TargetMesh1"
        before = set(mc.ls(assemblies=True, l=True))
        mc.select("PlugIt_TargetMesh1")

        #TO FIX NO UV FACES BUG
        mc.polyAutoProjection(caching=1, lm=0, pb=0, ibd=1, cm=1, l=2, sc=1, o=1, p=6, uvSetName="PlugIT_uvSet", ps=0.2,      ws=0)
        mc.polyUVSet(currentUVSet=True, uvSet='PlugIT_uvSet')
        mc.select("PlugIt_TargetMesh1")



        mc.ConvertSelectionToFaces()
        mel.eval('createHair 8 8 2 0 0 0 0 5 0 2 2 2;')
        mc.select("PlugIt_TargetMesh1Follicle*")
        getFocilleNode = mc.ls(sl=True)
        curveNodeName = mc.listRelatives(getFocilleNode, c=True, ad=True)[-1]
        print(curveNodeName)

        mc.select("PlugIt_TargetMesh1", curveNodeName)
        mel.eval('source "' + MelScript_MatchPivot + '"')

        # CLEAN
        after = set(mc.ls(assemblies=True, l=True))
        imported = after.difference(before)
        mc.delete(imported)



    # ______________________________________________________________________________ Import Plug
    mc.file(Plug_Path, i=True)

    mc.select("PlugIt_PlugCountNumber_*")
    foundInfoNode = mc.ls(sl=True)
    plugNumberEdges = int(foundInfoNode[0].split("_")[-1]) - 1

    if 0 > plugNumberEdges:
        pass
    else:
        # ____ Clean ExtraSecure
        mc.select("Plug_ExtraSecure_set")
        mc.DeleteEdge()
        mc.delete("Plug_ExtraSecure_set")

        # Fix set bug after innerBorderEdges deleting
        mc.delete("Plug_Selection_set")
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.InvertSelection()
        mc.sets(n="Plug_Selection_set")


    if mc.objExists("PlugIt_PlugCountNumber_*"):
        mc.delete("PlugIt_PlugCountNumber_*")

    # ______________________________________________________________________________ Apply Mesh Shader
    mc.select(TargetMesh_TempName)
    theNodes = mc.ls(sl=True, dag=True, s=True)
    shadeEng = mc.listConnections(theNodes, type="shadingEngine")
    materials = mc.ls(mc.listConnections(shadeEng), materials=True)
    mc.select("Plug_Mesh")
    mc.hyperShade(a=materials[0])


    # ---------------------------------------------------------------------------------------------------------// P L A C E M E N T
    # ______________________________________________________________________________ Match Scale
    objA = dupFaceMatch
    objB = "Plug_Mesh"
    objA_BoundRaw = mc.xform(objA, q=1, bb=1)
    objB_BoundRaw = mc.xform(objB, q=1, bb=1)
    objA_BoundAll = [objA_BoundRaw[3] - objA_BoundRaw[0], objA_BoundRaw[4] - objA_BoundRaw[1], objA_BoundRaw[5] - objA_BoundRaw[2]]
    objA_Bound = sorted(objA_BoundAll)
    if FACE_ANGLE_MODE == 0: #Flat Faces
        moyenne = (objA_Bound[0] + objA_Bound[1])
    else:
        moyenne = (objA_Bound[0] + objA_Bound[1])/2  # divide by 2 to fix matchScale on curve rect ratio
    objB_Bound = [objB_BoundRaw[3] - objB_BoundRaw[0]]
    objBScaleOld = mc.xform(objB, q=1, s=1)
    boundDifference = [moyenne / objB_Bound[0]]
    objBScaleNew = [objBScaleOld[0] * boundDifference[0], objBScaleOld[1] * boundDifference[0], objBScaleOld[2] * boundDifference[0]]
    mc.xform(objB, scale=objBScaleNew)

    # ______________________________________________________________________________ Match Placement
    piv = mc.xform(extractFace, piv=True, q=True, ws=True)
    mc.xform(dupFaceMatch, ws=True, piv=(piv[0], piv[1], piv[2]))
    mc.select(objB)
    if oneFace ==0:
        mc.rotate(0, 0, -90)
    if oneFace == 1:
        mc.rotate(90, 0, 0)
    mc.FreezeTransformations()
    mc.matchTransform(objB, dupFaceMatch, pos=True, rot=True)
    mc.delete(dupFaceMatch)

    # ---------------------------------------------------------------------------------------------------------// W R A P
    if WrapMode == 0:
        if oneFace == 0:
            pass
            mc.delete(extractFace)
        else:
            pass
    else:
        mc.select(extractFace)
        mc.FreezeTransformations()
        mc.ConvertSelectionToEdges()
        mc.sets(rm="Mesh_EdgeBorder_set")
        mc.duplicate(extractFace, n="PlugIt_wrapFlaten")
        mc.select("PlugIt_wrapFlaten")
        mc.scale(0, 1, 1, ls=True, cs=True, r=True)
        blendShape = mc.blendShape(extractFace, 'PlugIt_wrapFlaten', n="PlugIt_wrapBlendShape")
    mc.select("Mesh_EdgeBorder_set")


    # ---------------------------------------------------------------------------------------------------------//  M A T C H  E D G E S  C O U N T
    PlugMesh_name = "Plug_Mesh"
    TargetMesh_BorderEdges = "Mesh_EdgeBorder_set"
    Plug_BorderEdges = "PlugIt_Plug_Border_Set"
    # ______________________________________________________________________________ Count TargetMesh Edges Num
    mc.select(TargetMesh_BorderEdges)
    TargetMesh_edgeCount = len(mc.filterExpand(sm=32))

    # ______________________________________________________________________________ Prepare PlugMesh BorderPerim + Add Division
    nbrToAdd = TargetMesh_edgeCount - 4
    PlugEdgeNbr = 4

    d, r = divmod(nbrToAdd, PlugEdgeNbr)
    divRepartList = [d + 1] * r + [d] * (PlugEdgeNbr - r)

    mc.select("Plug_EdgeBorder_set")
    Plug_EdgeBorder_name = mc.filterExpand(sm=32)
    print("Plug_EdgeBorder_name = " +str(Plug_EdgeBorder_name))

    edgesRepartition_Dict = {Plug_EdgeBorder_name[0]: divRepartList[0], Plug_EdgeBorder_name[1]: divRepartList[1],  Plug_EdgeBorder_name[2]: divRepartList[2], Plug_EdgeBorder_name[3]: divRepartList[3]}
    print("edgesRepartition_Dict = " + str(edgesRepartition_Dict))

    for each in edgesRepartition_Dict:
        mc.select(each)
        mc.polySubdivideEdge(ws=0, s=0, dv=edgesRepartition_Dict[each], ch=1)




    # ---------------------------------------------------------------------------------------------------------// I N S I D E  C O N N E C T I O N S
    # ______________________________________________________________________________ Found the face selection
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.ls(sl=True)
    allFaces = mc.filterExpand(ex=True, sm=34)
    allFaceSet_list = []
    for each in allFaces:
        mc.select(each)
        setName = mc.sets(n="PlugIt_IndivFacesSaved_" + str(each))
        allFaceSet_list.append(setName)
    for each in allFaceSet_list:
        AutoConnect(each)
        mc.delete(each)

    # WRAP
    if WrapMode == 1:
        # Clean Freeze
        mc.select("Plug_Mesh")
        mc.FreezeTransformations()

        # Create ProxiWrap
        import maya.internal.nodes.proximitywrap.node_interface as node_interface

        target = "Plug_Mesh"
        source = "PlugIt_wrapFlaten"
        sourceShapes = mc.listRelatives(source, shapes=True)[0]

        deformer = mc.deformer(target, type='proximityWrap', name=target + '_pWrap')[0]

        proximity_interface = node_interface.NodeInterface(deformer)
        proximity_interface.addDriver(sourceShapes)

        # ProxiWrap Setting
        mc.setAttr(deformer + '.maxDrivers', 1)

        # Blend
        mc.setAttr("PlugIt_wrapBlendShape." + str(extractFace[0]), 1)


    # ---Combine
    mc.select(TargetMesh_TempName, PlugMesh_name)

    if ClashingName == 1:
        meshName = TargetMesh_OriginNameClashing
    else:
        meshName = TargetMesh_OriginName

    global MeshName
    MeshName = meshName
    mc.polyUnite(ch=0, mergeUVSets=1, centerPivot=1, name=meshName)

    # ---------------------------------------------------------------------------------------------------------// B R I D G E
    # Try to BridgeConnect properly first
    mc.select("Plug_EdgeBorder_set", "Mesh_EdgeBorder_set")
    bridgeNode = mc.polyBridgeEdge(ch=1, divisions=0, twist=0, taper=0, curveType=0, smoothingAngle=30)
    # !!!!! si fonctionne mettre le nom du mesh pour eviter les doublon
    if ClashingName == 0:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginName
    else:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginNameClashing

    mc.rename(bridgeNode, BridgeNodeName)

    # Fix Plug_All_Face_set
    mc.delete("Plug_AllFaces_set")
    mc.select("Plug_Selection_set")
    mc.GrowPolygonSelectionRegion()
    mc.sets(n="Plug_AllFaces_set")

    # 1 - Take one internal edge create len than compare until shorter one
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.sets(n="PlugIt_Temp")
    mc.select(mc.sets('Plug_AllFaces_set', sub="PlugIt_Temp"))
    mc.ConvertSelectionToContainedEdges()
    internalEdge = mc.ls(sl=True)[0]
    mc.delete("PlugIt_Temp")

    # 2 - Test sur le nombre de countBridgeEdge_nrb
    lenList = []
    for each in range(0, TargetMesh_edgeCount + 1):
        # Set Bridge Value
        mc.setAttr(BridgeNodeName + ".bridgeOffset", each)

        # Calculate internalEdge LENGHT
        ps = mc.xform(internalEdge, q=1, t=1, ws=1)
        p1 = ps[0:3]
        p2 = ps[3:6]
        length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
        lenList.append(length)

    minimumLenght = min(lenList)
    index = lenList.index(minimumLenght)
    BridgeInitCount_nbr = index + TargetMesh_edgeCount + 1
    mc.setAttr(BridgeNodeName + ".bridgeOffset", BridgeInitCount_nbr)

    # Clean Plug EdgeBorder
    mc.select("Plug_EdgeBorder_set")
    mc.DeleteEdge()

    # SET CONTROLLER
    mc.select("Plug_Selection_set")
    mc.ConvertSelectionToFaces()
    mc.select("Plug_controler", add=True)
    mc.CreateWrap()

    #____ Clean NormalAngle Smooth
    mc.select("Mesh_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.polySoftEdge(angle=45, ch=1)




    # ---------------------------------------------------------------------------------------------------------// S C R I P T   J O B
    def autoBridgeOffset():
        lenList = []
        for each in range(0, TargetMesh_edgeCount + 1):
            # Set Bridge Value
            mc.setAttr(BridgeNodeName + ".bridgeOffset", each)

            # Calculate internalEdge LENGHT
            ps = mc.xform(internalEdge, q=1, t=1, ws=1)
            p1 = ps[0:3]
            p2 = ps[3:6]
            length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
            lenList.append(length)

        minimumLenght = min(lenList)
        index = lenList.index(minimumLenght)
        BridgeInitCount_nbr = index + TargetMesh_edgeCount + 1
        mc.setAttr(BridgeNodeName + ".bridgeOffset", BridgeInitCount_nbr)

    if oneFace == 0:
        jobNum = mc.scriptJob(attributeChange=["Plug_controler.rotateX", autoBridgeOffset])
    else:
        jobNum = mc.scriptJob(attributeChange=["Plug_controler.rotateY", autoBridgeOffset])
    global ScriptJobNum
    ScriptJobNum = jobNum


    # ______ Create Transform for Flip 1x1 axis info
    if oneFace == 1:
        mc.group(em=True, name='PlugIt_FlipY_info')


    if mc.objExists("PlugIt_TargetMesh_DupSave"):
        mc.matchTransform(meshName, 'PlugIt_TargetMesh_DupSave', piv=True)
        mc.rename("PlugIt_TargetMesh_DupSave", "PlugItDupSave_" + meshName)

    if mc.objExists("PlugIt_Plug_Shd"):
        mc.delete("PlugIt_Plug_Shd")

    if mc.objExists("Plug_ExtraSecure_set"):
        mc.delete("Plug_ExtraSecure_set")

    if mc.objExists("Plug_Hole_set"):
        mc.delete("Plug_Hole_set")


    if DebugMode == 0:
        elementToHide = ("Plug_Mesh", "Mesh_EdgeBorder_set", "Plug_AllFaces_set", "Plug_EdgeBorder_set", "Plug_Selection_set")
        for each in elementToHide:
            mc.select(each)
            mc.setAttr(each + ".hiddenInOutliner", 1)
        try:
            mel.eval("AEdagNodeCommonRefreshOutliners();")
        except:
            pass

    mc.setAttr("Plug_controler.visibility", 0)


    mc.select("Plug_controler")
    mc.setToolTo('RotateSuperContext')

    # Turn ON WireframeOnShade
    panel = mc.getPanel(withFocus=True)
    if not panel or "modelPanel" not in panel:
        raise RuntimeError("No active model panel found")
    mc.modelEditor(panel, e=1, wos=1)




    showUI()
    mc.flushUndo()


def PERFORM_1x1_PLUG(Plug_Path):
    if mc.objExists("PlugIt_TargetMesh"):
        mc.rename("PlugIt_TargetMesh", "newDebugMesh")

    listToDel = ("PlugIt_TargetMesh*","hairSystem*", "hairSystem*Follicles", "hairSystem*OutputCurves*", "nucleus*", "Mesh_EdgeBorder_set*")
    for each in listToDel:
        if mc.objExists(each):
            mc.delete(each)



    # Avoid ClashingName
    ClashingName = 0
    TargetMesh_OriginName = mc.ls(sl=True)[0].split(".f")[0]

    if "|" in TargetMesh_OriginName:
        ClashingName = 1
        TargetMesh_OriginNameClashing = TargetMesh_OriginName.split("|")[-1]

    TargetMesh_TempName = mc.rename(TargetMesh_OriginName, "PlugIt_TargetMesh")
    targetMesh_faceSelected = mc.ls(sl=True)

    #DuplicationSave
    if mc.objExists("PlugItDupSave_*"):
        mc.select("PlugItDupSave_*")
        mc.delete()


    mc.select("PlugIt_TargetMesh")
    mc.duplicate(n= "PlugIt_TargetMesh_DupSave")
    parentSel = mc.ls(sl=True)
    if parentSel == []:
        pass
    else:
        mc.Unparent()
    mc.HideSelectedObjects()
    mc.setAttr("PlugIt_TargetMesh_DupSave.hiddenInOutliner", 1)
    try:
        mel.eval("AEdagNodeCommonRefreshOutliners();")
    except:
        pass
    mc.select(targetMesh_faceSelected)




    # ______ Supp selection Face
    mc.select(targetMesh_faceSelected)
    mc.ConvertSelectionToEdgePerimeter()
    mc.sets(n="Mesh_EdgeBorder_set")
    mc.select(targetMesh_faceSelected)



    # ______ Extract Mesh Faces
    # ______________________________________________________________________________ Extract Mesh Faces
    mc.ls(sl=True)
    MelScript_ExtractFace = TOOLS_PATH + 'wzx_ExtractFace.mel'
    mel.eval('source "' + MelScript_ExtractFace + '"')
    mc.select("PlugIt_TargetMesh1")

    # ______ AlignFace Pivot Mode
    extractFace = "PlugIt_TargetMesh1"
    dupFaceMatch = "PlugIt_TargetMesh1"

    before = set(mc.ls(assemblies=True, l=True))

    mc.select("PlugIt_TargetMesh1")

    #__________________________________________ TEST OWN
    mc.ConvertSelectionToFaces()
    mel.eval('createHair 8 8 2 0 0 0 0 5 0 2 2 2;')
    mc.select("PlugIt_TargetMesh1Follicle*")
    getFocilleNode = mc.ls(sl=True)
    curveNodeName = mc.listRelatives(getFocilleNode, c=True, ad=True)[-1]
    print(curveNodeName)

    mc.select("PlugIt_TargetMesh1", curveNodeName)


    if VERSION == "2023":
        MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots.mel'
    elif VERSION == "2022":
        MelScript_MatchPivot = TOOLS_PATH + 'performMatchPivots_2022.mel'
    mel.eval('source "' + MelScript_MatchPivot + '"')

    # CLEAN
    after = set(mc.ls(assemblies=True, l=True))
    imported = after.difference(before)
    mc.delete(imported)





    # ______ Import Plug
    mc.file(Plug_Path, i=True)

    # ______ Apply Mesh Shader
    mc.select(TargetMesh_TempName)
    theNodes = mc.ls(sl=True, dag=True, s=True)
    shadeEng = mc.listConnections(theNodes, type="shadingEngine")
    materials = mc.ls(mc.listConnections(shadeEng), materials=True)
    mc.select("Plug_Mesh")
    mc.hyperShade(a=materials[0])



    # ----------------------------------------------------------------------// P L A C E M E N T
    # ______ Match Scale
    objA = dupFaceMatch
    objB = "Plug_Mesh"


    objA_BoundRaw = mc.xform(objA, q=1, bb=1)
    objB_BoundRaw = mc.xform(objB, q=1, bb=1)
    objA_BoundAll = [objA_BoundRaw[3] - objA_BoundRaw[0], objA_BoundRaw[4] - objA_BoundRaw[1],
                     objA_BoundRaw[5] - objA_BoundRaw[2]]
    objA_Bound = sorted(objA_BoundAll)
    moyenne = (objA_Bound[0] + objA_Bound[1])
    objB_Bound = [objB_BoundRaw[3] - objB_BoundRaw[0]]
    objBScaleOld = mc.xform(objB, q=1, s=1)
    boundDifference = [moyenne / objB_Bound[0]]
    objBScaleNew = [objBScaleOld[0] * boundDifference[0], objBScaleOld[1] * boundDifference[0],
                    objBScaleOld[2] * boundDifference[0]]
    mc.xform(objB, scale=objBScaleNew)




    # ______ Placement
    piv = mc.xform(extractFace, piv=True, q=True, ws=True)
    mc.xform(dupFaceMatch, ws=True, piv=(piv[0], piv[1], piv[2]))
    mc.select(objB)
    mc.rotate(90, 0, 0)
    mc.FreezeTransformations()
    mc.matchTransform(objB, dupFaceMatch, pos=True, rot=True)
    # pNormal = mc.normalConstraint(objA, objB, worldUpType="scene", aimVector=(0, 1, 0), upVector=(0, 1, 0), weight=1)
    # mc.delete(pNormal)
    mc.delete(dupFaceMatch)

    mc.select("Mesh_EdgeBorder_set")

    # ----------------------------------------------------------------------// M A T C H  E D G E S  C O U N T
    PlugMesh_name = "Plug_Mesh"
    TargetMesh_BorderEdges = "Mesh_EdgeBorder_set"
    Plug_BorderEdges = "PlugIt_Plug_Border_Set"
    # ______ Count TargetMesh Edges Num
    mc.select(TargetMesh_BorderEdges)
    TargetMesh_edgeCount = len(mc.filterExpand(sm=32))

    # ______ Prepare PlugMesh BorderPerim + Add Division
    nbrToAdd = TargetMesh_edgeCount - 4
    PlugEdgeNbr = 4

    d, r = divmod(nbrToAdd, PlugEdgeNbr)
    divRepartList = [d + 1] * r + [d] * (PlugEdgeNbr - r)

    mc.select("Plug_EdgeBorder_set")
    Plug_EdgeBorder_name = mc.filterExpand(sm=32)
    edgesRepartition_Dict = {Plug_EdgeBorder_name[0]: divRepartList[0], Plug_EdgeBorder_name[1]: divRepartList[1],
                             Plug_EdgeBorder_name[2]: divRepartList[2], Plug_EdgeBorder_name[3]: divRepartList[3]}
    for each in edgesRepartition_Dict:
        mc.select(each)
        mc.polySubdivideEdge(ws=0, s=0, dv=edgesRepartition_Dict[each], ch=1)

    # ----------------------------------------------------------------------// I N S I D E  C O N N E C T I O N S
    # ______ Found the face selection
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()



    # ______ EXECTURE
    mc.ls(sl=True)
    allFaces = mc.filterExpand(ex=True, sm=34)
    allFaceSet_list = []
    for each in allFaces:
        mc.select(each)
        setName = mc.sets(n="PlugIt_IndivFacesSaved_" + str(each))
        allFaceSet_list.append(setName)

    for each in allFaceSet_list:
        AutoConnect(each)
        mc.delete(each)

    # WRAP
    if WrapMode == 1:
        # Clean Freeze
        mc.select("Plug_Mesh")
        mc.FreezeTransformations()

        # Create ProxiWrap
        import maya.internal.nodes.proximitywrap.node_interface as node_interface

        target = "Plug_Mesh"
        source = "PlugIt_wrapFlaten"
        sourceShapes = mc.listRelatives(source, shapes=True)[0]

        deformer = mc.deformer(target, type='proximityWrap', name=target + '_pWrap')[0]

        proximity_interface = node_interface.NodeInterface(deformer)
        proximity_interface.addDriver(sourceShapes)

        # ProxiWrap Setting
        mc.setAttr(deformer + '.maxDrivers', 1)

        # Blend
        mc.setAttr("PlugIt_wrapBlendShape." + str(extractFace[0]), 1)

    # ---Combine
    mc.select(TargetMesh_TempName, PlugMesh_name)

    if ClashingName == 1:
        meshName = TargetMesh_OriginNameClashing
    else:
        meshName = TargetMesh_OriginName

    global MeshName
    MeshName = meshName
    mc.polyUnite(ch=0, mergeUVSets=1, centerPivot=1, name=meshName)

    # ----------------------------------------------------------------------// B R I D G E
    # Try to BridgeConnect properly first
    mc.select("Plug_EdgeBorder_set", "Mesh_EdgeBorder_set")
    bridgeNode = mc.polyBridgeEdge(ch=1, divisions=0, twist=0, taper=0, curveType=0, smoothingAngle=30)
    # !!!!! si fonctionne mettre le nom du mesh pour eviter les doublon
    if ClashingName == 0:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginName
    else:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginNameClashing

    mc.rename(bridgeNode, BridgeNodeName)

    # Fix Plug_All_Face_set
    mc.delete("Plug_AllFaces_set")
    mc.select("Plug_Selection_set")
    mc.GrowPolygonSelectionRegion()
    mc.sets(n="Plug_AllFaces_set")

    # 1 - Take one internal edge create len than compare until shorter one
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.sets(n="PlugIt_Temp")
    mc.select(mc.sets('Plug_AllFaces_set', sub="PlugIt_Temp"))
    mc.ConvertSelectionToContainedEdges()
    internalEdge = mc.ls(sl=True)[0]
    mc.delete("PlugIt_Temp")

    # 2 - Test sur le nombre de countBridgeEdge_nrb
    lenList = []
    for each in range(0, TargetMesh_edgeCount + 1):
        # Set Bridge Value
        mc.setAttr(BridgeNodeName + ".bridgeOffset", each)

        # Calculate internalEdge LENGHT
        ps = mc.xform(internalEdge, q=1, t=1, ws=1)
        p1 = ps[0:3]
        p2 = ps[3:6]
        length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
        lenList.append(length)

    minimumLenght = min(lenList)
    index = lenList.index(minimumLenght)
    BridgeInitCount_nbr = index + TargetMesh_edgeCount + 1
    mc.setAttr(BridgeNodeName + ".bridgeOffset", BridgeInitCount_nbr)




    #____ Clean Plug EdgeBorder
    mc.select("Plug_EdgeBorder_set")
    mc.DeleteEdge()

    #____ Clean NormalAngle Smooth
    mc.select("Mesh_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.polySoftEdge(angle=45, ch=1)



    #CLEAN
    if mc.objExists(MeshName):
        mc.delete(MeshName, constructionHistory=True)
    listToDelete = ("Mesh_EdgeBorder_set", "Plug_AllFaces_set", "Plug_EdgeBorder_set", "Plug_Selection_set", "Plug_Mesh")
    for each in listToDelete:
        if mc.objExists(each):
            mc.delete(each)

    if mc.objExists("Plug_Hole_set"):
        mc.delete("Plug_Hole_set")
    if mc.objExists("PlugIt_Plug_Shd"):
        mc.delete("PlugIt_Plug_Shd")
    if mc.objExists("PlugIt_Plug_Shd"):
        mc.delete("PlugIt_Plug_Shd")
    if mc.objExists("PlugIt_PlugCountNumber_*"):
        mc.delete("PlugIt_PlugCountNumber_*")

    if mc.objExists("PlugIt_TargetMesh_DupSave"):
        mc.rename("PlugIt_TargetMesh_DupSave", "PlugItDupSave_" + meshName)

    mc.select(meshName)
    mel.eval('changeSelectMode -component;')
    mel.eval('setComponentPickMask "Facet" true;')

    # ____ Clean ExtraSecure
    mc.select("Plug_ExtraSecure_set")
    mc.DeleteEdge()
    mc.delete("Plug_ExtraSecure_set")


    mc.delete(meshName, constructionHistory=True)

    mc.flushUndo()



def INIT_PERFORM_PLUG(Plug_Path, oneFace, numberOfEdges):
    # ---------------------------------------------------------------------------------------------------------//  I N I T
    global ONEFACE
    ONEFACE = oneFace

    NumberOfEdges = numberOfEdges


    # ______________________________________________________________________________ Avoid ClashingName
    ClashingName = 0
    TargetMesh_OriginName = mc.ls(sl=True)[0].split(".f")[0]
    if "|" in TargetMesh_OriginName:
        ClashingName = 1
        TargetMesh_OriginNameClashing = TargetMesh_OriginName.split("|")[-1]
    TargetMesh_TempName = mc.rename(TargetMesh_OriginName, "PlugIt_TargetMesh")
    targetMesh_faceSelected = mc.ls(sl=True)

    # ______________________________________________________________________________ UNDO : Duplication Save for Delete Plug
    if mc.objExists("PlugItDupSave_*"):
        mc.select("PlugItDupSave_*")
        mc.delete()

    mc.select("PlugIt_TargetMesh")
    mc.duplicate(n= "PlugIt_TargetMesh_DupSave")
    mc.HideSelectedObjects()
    mc.setAttr("PlugIt_TargetMesh_DupSave.hiddenInOutliner", 1)
    try:
        mel.eval("AEdagNodeCommonRefreshOutliners();")
    except:
        pass


    parentSel = mc.ls(sl = True)
    if parentSel == []:
        pass
    else:
        mc.Unparent()




    # ______________________________________________________________________________ Flat or Curve
    if oneFace == 0:
        mc.select(targetMesh_faceSelected)
        faceSelection = mc.filterExpand(sm=34)
        mc.select(faceSelection[0])
        checkFaceA = mc.polyInfo(fn=True)
        #print(checkFaceA)
        XYZValues_FaceA = [checkFaceA[0][20], checkFaceA[0][21], checkFaceA[0][22], checkFaceA[0][23], checkFaceA[0][24],
                           checkFaceA[0][25]]
        #print("XYZValues_FaceA = " + str(XYZValues_FaceA))

        mc.select(faceSelection[1])
        checkFaceB = mc.polyInfo(fn=True)
        #print(checkFaceB)
        XYZValues_FaceB = [checkFaceB[0][20], checkFaceB[0][21], checkFaceB[0][22], checkFaceB[0][23], checkFaceB[0][24],
                           checkFaceB[0][25]]
        #print("XYZValues_FaceB = " + str(XYZValues_FaceB))

        if XYZValues_FaceA == XYZValues_FaceB:
            FACE_ANGLE_MODE = 0 #Flat
            #print("FLAT")
        else:
            FACE_ANGLE_MODE = 1  # CURVE
            #print("CURVE")
    else:
        FACE_ANGLE_MODE = 0  # Flat
        #print("FLAT")



    # ______________________________________________________________________________ Supp Selection Face
    mc.select(targetMesh_faceSelected)
    mc.ConvertSelectionToEdgePerimeter()
    mc.sets(n="Mesh_EdgeBorder_set")
    mc.select(targetMesh_faceSelected)






    # ______________________________________________________________________________ Extract Mesh Faces
    mc.ls(sl=True)
    mel.eval('source "' + MelScript_ExtractFace + '"')

    # ______________________________________________________________________________ AlignFace Pivot Mode
    if oneFace == 0:
        # ______ Create an empty plane
        extractFace = mc.ls(sl=True)
        dupFaceMatch = mc.duplicate(extractFace, n="PlugIt_DupFace_for_Match")
        mc.ConvertSelectionToFaces()
        mc.ConvertSelectionToContainedEdges()
        mc.DeleteEdge()
        mc.select(dupFaceMatch)
        mc.ConvertSelectionToFaces()
        #______ Align Pivot
        from .Tools import BakeTransformations
        BakeTransformations.BakeTransformations(optionBox=False)
    else:
        # ______ Align Pivot Classic
        mc.select("PlugIt_TargetMesh1")
        extractFace = "PlugIt_TargetMesh1"
        dupFaceMatch = "PlugIt_TargetMesh1"
        before = set(mc.ls(assemblies=True, l=True))
        mc.select("PlugIt_TargetMesh1")

        # TO FIX NO UV FACES BUG
        mc.polyAutoProjection(caching=1, lm=0, pb=0, ibd=1, cm=1, l=2, sc=1, o=1, p=6, uvSetName="PlugIT_uvSet", ps=0.2,
                              ws=0)
        mc.polyUVSet(currentUVSet=True, uvSet='PlugIT_uvSet')
        mc.select("PlugIt_TargetMesh1")


        mc.ConvertSelectionToFaces()
        mel.eval('createHair 8 8 2 0 0 0 0 5 0 2 2 2;')
        mc.select("PlugIt_TargetMesh1Follicle*")
        getFocilleNode = mc.ls(sl=True)
        curveNodeName = mc.listRelatives(getFocilleNode, c=True, ad=True)[-1]
        print(curveNodeName)

        mc.select("PlugIt_TargetMesh1", curveNodeName)
        mel.eval('source "' + MelScript_MatchPivot + '"')

        # CLEAN
        after = set(mc.ls(assemblies=True, l=True))
        imported = after.difference(before)
        mc.delete(imported)



    # ______________________________________________________________________________ Import Plug
    mc.file(Plug_Path, i=True)

    mc.select("PlugIt_PlugCountNumber_*")
    foundInfoNode = mc.ls(sl=True)
    plugNumberEdges = int(foundInfoNode[0].split("_")[-1]) - 1

    if 0 > plugNumberEdges:
        pass
    else:
        # ____ Clean ExtraSecure
        mc.select("Plug_ExtraSecure_set")
        mc.DeleteEdge()
        mc.delete("Plug_ExtraSecure_set")

        # Fix set bug after innerBorderEdges deleting
        mc.delete("Plug_Selection_set")
        mc.select("Plug_EdgeBorder_set")
        mc.ConvertSelectionToFaces()
        mc.InvertSelection()
        mc.sets(n="Plug_Selection_set")


    if mc.objExists("PlugIt_PlugCountNumber_*"):
        mc.delete("PlugIt_PlugCountNumber_*")

    # ______________________________________________________________________________ Apply Mesh Shader
    mc.select(TargetMesh_TempName)
    theNodes = mc.ls(sl=True, dag=True, s=True)
    shadeEng = mc.listConnections(theNodes, type="shadingEngine")
    materials = mc.ls(mc.listConnections(shadeEng), materials=True)
    mc.select("Plug_Mesh")
    mc.hyperShade(a=materials[0])


    # ---------------------------------------------------------------------------------------------------------// P L A C E M E N T
    # ______________________________________________________________________________ Match Scale
    objA = dupFaceMatch
    objB = "Plug_Mesh"
    objA_BoundRaw = mc.xform(objA, q=1, bb=1)
    objB_BoundRaw = mc.xform(objB, q=1, bb=1)
    objA_BoundAll = [objA_BoundRaw[3] - objA_BoundRaw[0], objA_BoundRaw[4] - objA_BoundRaw[1], objA_BoundRaw[5] - objA_BoundRaw[2]]
    objA_Bound = sorted(objA_BoundAll)
    if FACE_ANGLE_MODE == 0: #Flat Faces
        moyenne = (objA_Bound[0] + objA_Bound[1])
    else:
        moyenne = (objA_Bound[0] + objA_Bound[1])/2  # divide by 2 to fix matchScale on curve rect ratio
    objB_Bound = [objB_BoundRaw[3] - objB_BoundRaw[0]]
    objBScaleOld = mc.xform(objB, q=1, s=1)
    boundDifference = [moyenne / objB_Bound[0]]
    objBScaleNew = [objBScaleOld[0] * boundDifference[0], objBScaleOld[1] * boundDifference[0], objBScaleOld[2] * boundDifference[0]]
    mc.xform(objB, scale=objBScaleNew)

    # ______________________________________________________________________________ Match Placement
    piv = mc.xform(extractFace, piv=True, q=True, ws=True)
    mc.xform(dupFaceMatch, ws=True, piv=(piv[0], piv[1], piv[2]))
    mc.select(objB)
    if oneFace ==0:
        mc.rotate(0, 0, -90)
    if oneFace == 1:
        mc.rotate(90, 0, 0)
    mc.FreezeTransformations()
    mc.matchTransform(objB, dupFaceMatch, pos=True, rot=True)
    mc.delete(dupFaceMatch)

    # ---------------------------------------------------------------------------------------------------------// W R A P
    if WrapMode == 0:
        if oneFace == 0:
            pass
            mc.delete(extractFace)
        else:
            pass
    else:
        mc.select(extractFace)
        mc.FreezeTransformations()
        mc.ConvertSelectionToEdges()
        mc.sets(rm="Mesh_EdgeBorder_set")
        mc.duplicate(extractFace, n="PlugIt_wrapFlaten")
        mc.select("PlugIt_wrapFlaten")
        mc.scale(0, 1, 1, ls=True, cs=True, r=True)
        blendShape = mc.blendShape(extractFace, 'PlugIt_wrapFlaten', n="PlugIt_wrapBlendShape")
    mc.select("Mesh_EdgeBorder_set")


    # ---------------------------------------------------------------------------------------------------------//  M A T C H  E D G E S  C O U N T
    PlugMesh_name = "Plug_Mesh"
    TargetMesh_BorderEdges = "Mesh_EdgeBorder_set"
    Plug_BorderEdges = "PlugIt_Plug_Border_Set"
    # ______________________________________________________________________________ Count TargetMesh Edges Num
    mc.select(TargetMesh_BorderEdges)
    TargetMesh_edgeCount = len(mc.filterExpand(sm=32))

    # ______________________________________________________________________________ Prepare PlugMesh BorderPerim + Add Division
    nbrToAdd = TargetMesh_edgeCount - 4
    PlugEdgeNbr = 4

    d, r = divmod(nbrToAdd, PlugEdgeNbr)
    divRepartList = [d + 1] * r + [d] * (PlugEdgeNbr - r)

    mc.select("Plug_EdgeBorder_set")
    Plug_EdgeBorder_name = mc.filterExpand(sm=32)
    print("Plug_EdgeBorder_name = " +str(Plug_EdgeBorder_name))

    edgesRepartition_Dict = {Plug_EdgeBorder_name[0]: divRepartList[0], Plug_EdgeBorder_name[1]: divRepartList[1],  Plug_EdgeBorder_name[2]: divRepartList[2], Plug_EdgeBorder_name[3]: divRepartList[3]}
    print("edgesRepartition_Dict = " + str(edgesRepartition_Dict))

    for each in edgesRepartition_Dict:
        mc.select(each)
        mc.polySubdivideEdge(ws=0, s=0, dv=edgesRepartition_Dict[each], ch=1)




    # ---------------------------------------------------------------------------------------------------------// I N S I D E  C O N N E C T I O N S
    # ______________________________________________________________________________ Found the face selection
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.ls(sl=True)
    allFaces = mc.filterExpand(ex=True, sm=34)
    allFaceSet_list = []
    for each in allFaces:
        mc.select(each)
        setName = mc.sets(n="PlugIt_IndivFacesSaved_" + str(each))
        allFaceSet_list.append(setName)
    for each in allFaceSet_list:
        AutoConnect(each)
        mc.delete(each)

    # WRAP
    if WrapMode == 1:
        # Clean Freeze
        mc.select("Plug_Mesh")
        mc.FreezeTransformations()

        # Create ProxiWrap
        import maya.internal.nodes.proximitywrap.node_interface as node_interface

        target = "Plug_Mesh"
        source = "PlugIt_wrapFlaten"
        sourceShapes = mc.listRelatives(source, shapes=True)[0]

        deformer = mc.deformer(target, type='proximityWrap', name=target + '_pWrap')[0]

        proximity_interface = node_interface.NodeInterface(deformer)
        proximity_interface.addDriver(sourceShapes)

        # ProxiWrap Setting
        mc.setAttr(deformer + '.maxDrivers', 1)

        # Blend
        mc.setAttr("PlugIt_wrapBlendShape." + str(extractFace[0]), 1)


    # ---Combine
    mc.select(TargetMesh_TempName, PlugMesh_name)

    if ClashingName == 1:
        meshName = TargetMesh_OriginNameClashing
    else:
        meshName = TargetMesh_OriginName

    global MeshName
    MeshName = meshName
    mc.polyUnite(ch=0, mergeUVSets=1, centerPivot=1, name=meshName)

    # ---------------------------------------------------------------------------------------------------------// B R I D G E
    # Try to BridgeConnect properly first
    mc.select("Plug_EdgeBorder_set", "Mesh_EdgeBorder_set")
    bridgeNode = mc.polyBridgeEdge(ch=1, divisions=0, twist=0, taper=0, curveType=0, smoothingAngle=30)
    # !!!!! si fonctionne mettre le nom du mesh pour eviter les doublon
    if ClashingName == 0:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginName
    else:
        BridgeNodeName = "PlugIt_Bridge_" + TargetMesh_OriginNameClashing

    mc.rename(bridgeNode, BridgeNodeName)

    # Fix Plug_All_Face_set
    mc.delete("Plug_AllFaces_set")
    mc.select("Plug_Selection_set")
    mc.GrowPolygonSelectionRegion()
    mc.sets(n="Plug_AllFaces_set")

    # 1 - Take one internal edge create len than compare until shorter one
    mc.select("Plug_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.sets(n="PlugIt_Temp")
    mc.select(mc.sets('Plug_AllFaces_set', sub="PlugIt_Temp"))
    mc.ConvertSelectionToContainedEdges()
    internalEdge = mc.ls(sl=True)[0]
    mc.delete("PlugIt_Temp")

    # 2 - Test sur le nombre de countBridgeEdge_nrb
    lenList = []
    for each in range(0, TargetMesh_edgeCount + 1):
        # Set Bridge Value
        mc.setAttr(BridgeNodeName + ".bridgeOffset", each)

        # Calculate internalEdge LENGHT
        ps = mc.xform(internalEdge, q=1, t=1, ws=1)
        p1 = ps[0:3]
        p2 = ps[3:6]
        length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
        lenList.append(length)

    minimumLenght = min(lenList)
    index = lenList.index(minimumLenght)
    BridgeInitCount_nbr = index + TargetMesh_edgeCount + 1
    mc.setAttr(BridgeNodeName + ".bridgeOffset", BridgeInitCount_nbr)

    # Clean Plug EdgeBorder
    mc.select("Plug_EdgeBorder_set")
    mc.DeleteEdge()

    # SET CONTROLLER
    mc.select("Plug_Selection_set")
    mc.ConvertSelectionToFaces()
    mc.select("Plug_controler", add=True)
    mc.CreateWrap()

    #____ Clean NormalAngle Smooth
    mc.select("Mesh_EdgeBorder_set")
    mc.ConvertSelectionToFaces()
    mc.polySoftEdge(angle=45, ch=1)




    # ---------------------------------------------------------------------------------------------------------// S C R I P T   J O B
    def autoBridgeOffset():
        lenList = []
        for each in range(0, TargetMesh_edgeCount + 1):
            # Set Bridge Value
            mc.setAttr(BridgeNodeName + ".bridgeOffset", each)

            # Calculate internalEdge LENGHT
            ps = mc.xform(internalEdge, q=1, t=1, ws=1)
            p1 = ps[0:3]
            p2 = ps[3:6]
            length = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) + math.pow(p1[2] - p2[2], 2))
            lenList.append(length)

        minimumLenght = min(lenList)
        index = lenList.index(minimumLenght)
        BridgeInitCount_nbr = index + TargetMesh_edgeCount + 1
        mc.setAttr(BridgeNodeName + ".bridgeOffset", BridgeInitCount_nbr)

    if oneFace == 0:
        jobNum = mc.scriptJob(attributeChange=["Plug_controler.rotateX", autoBridgeOffset])
    else:
        jobNum = mc.scriptJob(attributeChange=["Plug_controler.rotateY", autoBridgeOffset])
    global ScriptJobNum
    ScriptJobNum = jobNum


    # ______ Create Transform for Flip 1x1 axis info
    if oneFace == 1:
        mc.group(em=True, name='PlugIt_FlipY_info')


    if mc.objExists("PlugIt_TargetMesh_DupSave"):
        mc.matchTransform(meshName, 'PlugIt_TargetMesh_DupSave', piv=True)
        mc.rename("PlugIt_TargetMesh_DupSave", "PlugItDupSave_" + meshName)

    if mc.objExists("PlugIt_Plug_Shd"):
        mc.delete("PlugIt_Plug_Shd")

    if mc.objExists("Plug_ExtraSecure_set"):
        mc.delete("Plug_ExtraSecure_set")

    if mc.objExists("Plug_Hole_set"):
        mc.delete("Plug_Hole_set")


    if DebugMode == 0:
        elementToHide = ("Plug_Mesh", "Mesh_EdgeBorder_set", "Plug_AllFaces_set", "Plug_EdgeBorder_set", "Plug_Selection_set")
        for each in elementToHide:
            mc.select(each)
            mc.setAttr(each + ".hiddenInOutliner", 1)
        try:
            mel.eval("AEdagNodeCommonRefreshOutliners();")
        except:
            pass

    mc.setAttr("Plug_controler.visibility", 0)


    mc.select("Plug_controler")
    mc.setToolTo('RotateSuperContext')

    # Turn ON WireframeOnShade
    #panel = mc.getPanel(withFocus=True)
    #if not panel or "modelPanel" not in panel:
    #    raise RuntimeError("No active model panel found")
    #mc.modelEditor(panel, e=1, wos=1)


    mc.flushUndo()




class PopUp_UI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PopUp_UI, self).__init__()
        self.setMinimumSize(500, 255)
        self.buildUI()


    def buildUI(self):
        ##----------------------------------------------------------------------------------------/ U I   V A L U E
        self.setStyleSheet(PlugIt_Global.Theme)
        iconButtonSize = PlugIt_Global.IconButtonSize
        separatorWidth = 2

        ##----------------------------------------------------------------------------------------/ L A Y O U T S
        self.MAIN_Lyt = QtWidgets.QVBoxLayout()
        self.setLayout(self.MAIN_Lyt)
        self.MAIN_Lyt.setContentsMargins(6, 6, 6, 6)

        ##---------------------------------------------------- Separator
        self.MAIN_Lyt.addSpacing(2)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(2)
        self.MAIN_Lyt.addWidget(separator)
        self.MAIN_Lyt.addSpacing(1)



        ##----------------------------------------------------------------------------------------/  S E L E C T  P L U G
        self.SelectPlug_Btn = QtWidgets.QPushButton("-  S E L E C T   P L U G  -")
        self.SelectPlug_Btn.setObjectName("SaveSetting")
        self.SelectPlug_Btn.setFixedHeight(22)
        #self.SelectPlug_Btn.setStyleSheet("color:#909090;")
        self.SelectPlug_Btn.setToolTip("  Select Plug Manipulator  ")
        self.SelectPlug_Btn.clicked.connect(self.SelectPlug)
        self.MAIN_Lyt.addWidget(self.SelectPlug_Btn)
        self.MAIN_Lyt.addSpacing(2)

        ##----------------------------------------------------------------------------------------/  O F F S E T   S L I D E R
        Offset_Hlyt = QtWidgets.QHBoxLayout()
        self.MAIN_Lyt.addLayout(Offset_Hlyt)
        ##------------------------------------------------------------: LABEL
        Offset_Label = QtWidgets.QLabel("Manual Offset : ")
        Offset_Label.setStyleSheet("color:#909090;")
        Offset_Label.setFont(QtGui.QFont('Calibri', 9))
        Offset_Hlyt.addWidget(Offset_Label)
        ##------------------------------------------------------------: SLIDER
        self.Offset_Slider = QtWidgets.QSlider()
        self.Offset_Slider.setMinimum(0)
        self.Offset_Slider.setMaximum(20)
        bridgeValue = mc.getAttr("PlugIt_Bridge_" + MeshName + ".bridgeOffset")
        self.Offset_Slider.setProperty("value", bridgeValue)
        self.Offset_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Offset_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Offset_Slider.setTickInterval(1)
        self.Offset_Slider.setFixedHeight(22)
        self.Offset_Slider.valueChanged.connect(self.set_Slider)
        Offset_Hlyt.addWidget(self.Offset_Slider)
        ##------------------------------------------------------------: SPINBOX
        self.Offset_SpinBox = QtWidgets.QDoubleSpinBox()
        self.Offset_SpinBox.setDecimals(0)
        self.Offset_SpinBox.setFixedWidth(40)
        self.Offset_SpinBox.setFixedHeight(18)
        self.Offset_SpinBox.setRange(0, 20)
        self.Offset_SpinBox.setValue(bridgeValue)
        self.Offset_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Offset_SpinBox.editingFinished.connect(self.set_SpinBox)
        Offset_Hlyt.addWidget(self.Offset_SpinBox)

        ##---------------------------------------------------- Separator
        self.MAIN_Lyt.addSpacing(3)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(2)
        self.MAIN_Lyt.addWidget(separator)
        self.MAIN_Lyt.addSpacing(3)




        ##----------------------------------------------------------------------------------------/  F L I P
        Flip_Hlyt = QtWidgets.QHBoxLayout()
        self.MAIN_Lyt.addLayout(Flip_Hlyt)

        self.FlipPlug_Btn = QtWidgets.QPushButton("-  F l i p   P l u g  -")
        self.FlipPlug_Btn.setObjectName("StoreSet")
        self.FlipPlug_Btn.setFixedHeight(22)
        self.FlipPlug_Btn.setStyleSheet("color:#909090;")
        self.FlipPlug_Btn.clicked.connect(self.FlipPlug)
        Flip_Hlyt.addWidget(self.FlipPlug_Btn)


        self.ScaleManip_Btn = QtWidgets.QPushButton()
        self.ScaleManip_Btn.setIcon(QtGui.QIcon(IconPath + "Scale_Gizmo.png"))
        self.ScaleManip_Btn.setObjectName("TABSBTN")
        self.ScaleManip_Btn.setFixedSize(20, 20)
        self.ScaleManip_Btn.setIconSize(QtCore.QSize(20, 20))
        self.ScaleManip_Btn.setToolTip("  Manually Scale Plug with Manipulator  ")
        self.ScaleManip_Btn.clicked.connect(self.SelectScaleManip)
        Flip_Hlyt.addWidget(self.ScaleManip_Btn)


        ##----------------------------------------------------------------------------------------/  O P E R A T I O N
        Smoot_Hlyt = QtWidgets.QHBoxLayout()
        self.MAIN_Lyt.addLayout(Smoot_Hlyt)

        self.Smooth_Btn = QtWidgets.QPushButton("-  S m o o t h   P l u g  -")
        self.Smooth_Btn.setObjectName("StoreSet")
        self.Smooth_Btn.setFixedHeight(22)
        self.Smooth_Btn.setStyleSheet("color:#909090;")
        self.Smooth_Btn.clicked.connect(self.Smooth)
        self.Smooth_Btn.setToolTip("  Mesh Smooth Plug's faces  ")
        Smoot_Hlyt.addWidget(self.Smooth_Btn)

        self.Hole_Btn = QtWidgets.QPushButton("-  O p e n  H o l e  -")
        self.Hole_Btn.setObjectName("StoreSet")
        self.Hole_Btn.setFixedHeight(22)
        self.Hole_Btn.setStyleSheet("color:#909090;")
        self.Hole_Btn.setToolTip("  Open the Hole selection set at the Plug creation  ")
        self.Hole_Btn.clicked.connect(self.OpenHole)
        Smoot_Hlyt.addWidget(self.Hole_Btn)

        self.Delete_Btn = QtWidgets.QPushButton()
        self.Delete_Btn.setIcon(QtGui.QIcon(IconPath + "delete_ON.png"))
        self.Delete_Btn.setToolTip("  Undo and Delete this Plug ")
        self.Delete_Btn.setObjectName("TABSBTN")
        self.Delete_Btn.setFixedSize(20, 20)
        self.Delete_Btn.setIconSize(QtCore.QSize(20, 20))
        self.Delete_Btn.clicked.connect(self.Delete)
        Smoot_Hlyt.addWidget(self.Delete_Btn)




        ##---------------------------------------------------- Separator
        self.MAIN_Lyt.addSpacing(3)
        separator = QtWidgets.QLabel('')
        separator.setStyleSheet( "QLabel {background-color: #313131; padding: 0; margin: 0; border-bottom: 1 solid #262626; border-top: 1 solid #313131;}")
        separator.setMaximumHeight(2)
        self.MAIN_Lyt.addWidget(separator)
        self.MAIN_Lyt.addSpacing(3)



        ##----------------------------------------------------------------------------------------/  W R A P   M O D E
        global ONEFACE
        if ONEFACE == 0:
            self.Wrap_Btn = QtWidgets.QPushButton("-  W R A P   M O D E   -")
            self.Wrap_Btn.setObjectName("StoreSet")
            self.Wrap_Btn.setFixedHeight(22)
            if BendWrapMode == 0:
                self.Wrap_Btn.setStyleSheet("color:#909090;")
            else:
                self.Wrap_Btn.setStyleSheet("color:#202020; background-color : #65BEF1;")
            self.Wrap_Btn.clicked.connect(self.add_WrapBend)
            self.Wrap_Btn.setToolTip("  Mesh Smooth Plug's faces  ")
            self.MAIN_Lyt.addWidget(self.Wrap_Btn)


            ##----------------------------------------------------------------------------------------/  B E N D  H   S L I D E R
            BendH_Lyt = QtWidgets.QHBoxLayout()
            self.MAIN_Lyt.addLayout(BendH_Lyt)
            ##------------------------------------------------------------: LABEL
            self.BendH_Label = QtWidgets.QLabel("Bend H : ")
            if BendWrapMode == 1:
                self.BendH_Label.setStyleSheet("color:#909090;")
            else:
                self.BendH_Label.setStyleSheet("color:#303030;")
            self.BendH_Label.setFont(QtGui.QFont('Calibri', 9))
            BendH_Lyt.addWidget(self.BendH_Label)
            ##------------------------------------------------------------: SLIDER
            self.BendH_Slider = QtWidgets.QSlider()
            self.BendH_Slider.setMinimum(-180)
            self.BendH_Slider.setMaximum(180)
            self.BendH_Slider.setOrientation(QtCore.Qt.Horizontal)
            self.BendH_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
            self.BendH_Slider.setTickInterval(1)
            self.BendH_Slider.setFixedHeight(22)
            self.BendH_Slider.valueChanged.connect(self.set_BendH_Slider)
            if BendWrapMode == 1:
                self.BendH_Slider.setStyleSheet("QSlider::handle:horizontal { background: #65BEF1; height: 1px;}")
            else:
                self.BendH_Slider.setStyleSheet("QSlider::handle:horizontal { background: #303030; height: 1px;}")

            BendH_Lyt.addWidget(self.BendH_Slider)
            ##------------------------------------------------------------: SPINBOX
            self.BendH_SpinBox = QtWidgets.QDoubleSpinBox()
            self.BendH_SpinBox.setDecimals(0)
            self.BendH_SpinBox.setFixedWidth(40)
            self.BendH_SpinBox.setFixedHeight(18)
            self.BendH_SpinBox.setRange(-180, 180)
            self.BendH_SpinBox.setValue(0)
            self.BendH_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.BendH_SpinBox.editingFinished.connect(self.set_BendH_SpinBox)
            if BendWrapMode == 1:
                self.BendH_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #909090;   background-color: #242424;  width: 60px;}")
            else:
                self.BendH_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #303030;   background-color: #242424;  width: 60px;}")

            BendH_Lyt.addWidget(self.BendH_SpinBox)
            self.BendH_Slider.setEnabled(0)
            self.BendH_SpinBox.setEnabled(0)


            ##----------------------------------------------------------------------------------------/  B E N D  V   S L I D E R
            BendV_Lyt = QtWidgets.QHBoxLayout()
            self.MAIN_Lyt.addLayout(BendV_Lyt)
            ##------------------------------------------------------------: LABEL
            self.BendV_Label = QtWidgets.QLabel("Bend V : ")
            if BendWrapMode == 1:
                self.BendV_Label.setStyleSheet("color:#909090;")
            else:
                self.BendV_Label.setStyleSheet("color:#303030;")
            self.BendV_Label.setFont(QtGui.QFont('Calibri', 9))
            BendV_Lyt.addWidget(self.BendV_Label)
            ##------------------------------------------------------------: SLIDER
            self.BendV_Slider = QtWidgets.QSlider()
            self.BendV_Slider.setMinimum(-180)
            self.BendV_Slider.setMaximum(180)
            self.BendV_Slider.setOrientation(QtCore.Qt.Horizontal)
            self.BendV_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
            self.BendV_Slider.setTickInterval(1)
            self.BendV_Slider.setFixedHeight(22)
            self.BendV_Slider.valueChanged.connect(self.set_BendV_Slider)
            if BendWrapMode == 1:
                self.BendV_Slider.setStyleSheet("QSlider::handle:horizontal { background: #65BEF1; height: 1px;}")
            else:
                self.BendV_Slider.setStyleSheet("QSlider::handle:horizontal { background: #303030; height: 1px;}")

            BendV_Lyt.addWidget(self.BendV_Slider)
            ##------------------------------------------------------------: SPINBOX
            self.BendV_SpinBox = QtWidgets.QDoubleSpinBox()
            self.BendV_SpinBox.setDecimals(0)
            self.BendV_SpinBox.setFixedWidth(40)
            self.BendV_SpinBox.setFixedHeight(18)
            self.BendV_SpinBox.setRange(-180, 180)
            self.BendV_SpinBox.setValue(0)
            self.BendV_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.BendV_SpinBox.editingFinished.connect(self.set_BendV_SpinBox)
            if BendWrapMode == 1:
                self.BendV_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #909090;   background-color: #242424;  width: 60px;}")
            else:
                self.BendV_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #303030;   background-color: #242424;  width: 60px;}")

            BendV_Lyt.addWidget(self.BendV_SpinBox)
            self.BendV_Slider.setEnabled(0)
            self.BendV_SpinBox.setEnabled(0)


            self.MAIN_Lyt.addStretch()

        else:
            pass





    def SelectPlug(self):
        mc.select("Plug_controler")
        mc.setToolTo('Rotate')
        mc.manipRotateContext("Rotate", edit=True, mode=0)

    def FlipPlug(self):
        if mc.objExists("PlugIt_FlipY_info"):
            queryActalScaleX = mc.getAttr("Plug_controler.scaleX")
            queryActalScaleY = mc.getAttr("Plug_controler.scaleY")* -1
        else:
            queryActalScaleX = mc.getAttr("Plug_controler.scaleX") * -1
            queryActalScaleY = mc.getAttr("Plug_controler.scaleY")


        queryActalScaleZ = mc.getAttr("Plug_controler.scaleZ")
        mc.setAttr("Plug_controler.scale", queryActalScaleX, queryActalScaleY, queryActalScaleZ)


    def SelectScaleManip(self):
        mc.select("Plug_controler")
        mc.setToolTo('Scale')
        mc.manipScaleContext("Scale", edit=True, mode=0)
        mc.manipScaleContext("Scale", edit=True, preventNegativeScale=0)

    def Smooth(self):
        mc.select("Plug_Selection_set")
        mc.polySmooth()

    def SelectPlug(self):
        mc.select("Plug_controler")
        mc.setToolTo('MoveSuperContext')



    def OpenHole(self):
        try:
            mc.select("Plug_Hole_set")
            mc.Delete()
        except:
            PlugIt_Global.WarningWindow("There no Hole set for this Plug.", 350)
            return

    def Delete(self):
        mc.delete(MeshName)
        mc.select("PlugIt_TargetMesh_DupSave")
        mc.ShowSelectedObjects()
        mc.rename("PlugIt_TargetMesh_DupSave", "mesh")

        mc.deleteUI("P L U G  -  O p t i o n s")




    def set_Slider(self):
        SliderValue = self.Offset_Slider.value()
        self.Offset_SpinBox.setValue(SliderValue)
        mc.setAttr("PlugIt_Bridge_" + MeshName + ".bridgeOffset", SliderValue)

    def set_SpinBox(self):
        SpinBoxAValue = self.Offset_SpinBox.value()
        self.Offset_Slider.setValue(SpinBoxAValue)
        self.Offset_SpinBox.clearFocus()



    def set_BendH_Slider(self):
        SliderValue = self.BendH_Slider.value()
        self.BendH_SpinBox.setValue(SliderValue)
        mc.setAttr("PlugIt_Bend_1.curvature", SliderValue)

    def set_BendH_SpinBox(self):
        SpinBoxAValue = self.BendH_SpinBox.value()
        self.BendH_Slider.setValue(SpinBoxAValue)
        self.BendH_SpinBox.clearFocus()

    def set_BendV_Slider(self):
        SliderValue = self.BendV_Slider.value()
        self.BendV_SpinBox.setValue(SliderValue)
        mc.setAttr("PlugIt_Bend_2.curvature", SliderValue)

    def set_BendV_SpinBox(self):
        SpinBoxAValue = self.BendV_SpinBox.value()
        self.BendV_Slider.setValue(SpinBoxAValue)
        self.BendV_SpinBox.clearFocus()



    # ___________________________________________________________________________ / WRAP BEND
    def add_WrapBend(self):
        global BendWrapMode
        # _______________________________________/ BTN UPDATE
        if BendWrapMode == 1:
            self.BendH_Slider.setEnabled(0)
            self.BendH_SpinBox.setEnabled(0)
            self.BendV_Slider.setEnabled(0)
            self.BendV_SpinBox.setEnabled(0)

            self.BendH_Label.setStyleSheet("color:#303030;")
            self.BendH_Slider.setStyleSheet("QSlider::handle:horizontal { background: #303030; height: 1px;}")
            self.BendH_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #303030;   background-color: #242424;  width: 60px;}")
            self.BendV_Label.setStyleSheet("color:#303030;")
            self.BendV_Slider.setStyleSheet("QSlider::handle:horizontal { background: #303030; height: 1px;}")
            self.BendV_SpinBox.setStyleSheet( "QDoubleSpinBox{font-size:13px; color : #303030;   background-color: #242424;  width: 60px;}")


            BendWrapMode = 0

            self.Wrap_Btn.setStyleSheet("color:#909090;")

            mc.delete("PlugIt_Bend_1Handle")
            mc.delete("PlugIt_Bend_2Handle")

        else:
            BendWrapMode = 1

            self.Wrap_Btn.setStyleSheet("color:#202020; background-color : #65BEF1;")

            mc.setAttr("Plug_controler.visibility", 1)
            # _______________________________________/ CREATE BEND 1
            mc.select("Plug_Selection_set")
            mc.nonLinear(type='bend', curvature=0.0, n="PlugIt_Bend_1")
            locatorSize = mc.getAttr("Plug_controler.boundingBoxMaxY")
            mc.setAttr("PlugIt_Bend_1Handle.scaleX", locatorSize)
            mc.setAttr("PlugIt_Bend_1Handle.scaleY", locatorSize)
            mc.setAttr("PlugIt_Bend_1Handle.scaleZ", locatorSize)
            mc.matchTransform("PlugIt_Bend_1Handle", "Plug_controler", pos=True, rot=True)
            mc.parent("PlugIt_Bend_1Handle", "Plug_Mesh")

            # _______________________________________/ CREATE BEND 2
            mc.select("Plug_Selection_set")
            mc.nonLinear(type='bend', curvature=0.0, n="PlugIt_Bend_2")
            locatorSize = mc.getAttr("Plug_controler.boundingBoxMaxY")
            mc.setAttr("PlugIt_Bend_2Handle.scaleX", locatorSize)
            mc.setAttr("PlugIt_Bend_2Handle.scaleY", locatorSize)
            mc.setAttr("PlugIt_Bend_2Handle.scaleZ", locatorSize)
            mc.matchTransform("PlugIt_Bend_2Handle", "Plug_controler", pos=True, rot=True)
            mc.parent("PlugIt_Bend_2Handle", "Plug_Mesh")
            mc.setAttr("PlugIt_Bend_2Handle.rotateX", 90)

            mc.setAttr("Plug_controler.visibility", 0)
            #UPDATE UI
            self.BendH_Slider.setEnabled(1)
            self.BendH_SpinBox.setEnabled(1)
            self.BendV_Slider.setEnabled(1)
            self.BendV_SpinBox.setEnabled(1)


            bend1Value = mc.getAttr("PlugIt_Bend_1.curvature")
            self.BendH_Slider.setProperty("value", bend1Value)
            self.BendH_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #909090;   background-color: #242424;  width: 60px;}")
            self.BendH_Slider.setStyleSheet("QSlider::handle:horizontal { background: #65BEF1; height: 1px;}")
            self.BendH_Label.setStyleSheet("color:#909090;")
            
            bend2Value = mc.getAttr("PlugIt_Bend_2.curvature")
            self.BendV_Slider.setProperty("value", bend2Value)
            self.BendV_SpinBox.setStyleSheet("QDoubleSpinBox{font-size:13px; color : #909090;   background-color: #242424;  width: 60px;}")
            self.BendV_Slider.setStyleSheet("QSlider::handle:horizontal { background: #65BEF1; height: 1px;}")
            self.BendV_Label.setStyleSheet("color:#909090;")

            mc.select(d = True)







    def select_WrapBend_1(self):
        mc.select("PlugIt_Bend_1Handle")
        mc.setToolTo('scaleSuperContext')

    def select_WrapBend_2(self):
        mc.select("PlugIt_Bend_2Handle")
        mc.setToolTo('scaleSuperContext')











def Dock(Widget, width=200, height=200, hp="free", show=True):
    name = WindowTitle
    label = getattr(Widget, "label", name)

    try:
        cmds.deleteUI(name)
    except RuntimeError:
        pass

    dockControl = cmds.workspaceControl(
        name,
        initialWidth=width,
        minimumWidth=False,
        widthProperty=hp,
        heightProperty=hp,
        label=label
    )

    dockPtr = omui.MQtUtil.findControl(dockControl)
    dockWidget = QtCompat.wrapInstance(int(dockPtr), QtWidgets.QWidget)
    dockWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    child = Widget(dockWidget)
    dockWidget.layout().addWidget(child)


    if show:
        cmds.evalDeferred(
            lambda *args: cmds.workspaceControl(
                dockControl,
                edit=True,
                widthProperty="free",
                restore=True
            )
        )

    return child


def atClose():
    mc.scriptJob(kill = ScriptJobNum, force=True)

    if mc.objExists(MeshName):
        mc.delete(MeshName, constructionHistory=True)

    listToDelete = ("Mesh_EdgeBorder_set", "Plug_AllFaces_set", "Plug_EdgeBorder_set", "Plug_Selection_set", "Plug_Mesh", "PlugIt_FlipY_info")
    for each in listToDelete:
        if mc.objExists(each):
            mc.delete(each)

    if mc.objExists(MeshName):
        mc.select(MeshName)

    if mc.objExists("PlugIt_TargetMesh_DupSave"):
        mc.rename("PlugIt_TargetMesh_DupSave", "PlugItDupSave_" + MeshName)


    mc.flushUndo()


def showUI():
    ui = Dock(PopUp_UI)
    ui.show()

    ##DELETE PopUp UI
    if mc.window("Settings", exists=True):
        mc.deleteUI("Settings")
    if mc.window("WarningWindow", exists=True):
        mc.deleteUI("WarningWindow")
    if mc.window("Thumbnail Framing", exists=True):
        mc.deleteUI("Thumbnail Framing")
    if mc.window("Add Asset", exists=True):
        mc.deleteUI("Add Asset")
    if mc.window("Add New Tab", exists=True):
        mc.deleteUI("Add New Tab")
    if mc.window("Add New Sub Tab", exists=True):
        mc.deleteUI("Add New Sub Tab")

    ##CLEAN Scene
    if mc.objExists("PlugIt_Thumb_Group"):
        mc.delete("PlugIt_Thumb_Group")
        mc.delete("PlugIt_Thumb_shd")
        mc.delete("PlugIt_ThumbScene_HDR")
        mc.delete("AssetI_ThumbScene_place2dTexture")
        if mc.objExists("PlugIt_Thumb_Scene_uiConfigurationScriptNode"):
            mc.delete("PlugIt_Thumb_Scene_uiConfigurationScriptNode")
        if mc.objExists("PlugIt_Thumb_Scene_sceneConfigurationScriptNode"):
            mc.delete("PlugIt_Thumb_Scene_sceneConfigurationScriptNode")

    # Get a pointer and convert it to Qt Widget object
    qw = omui.MQtUtil.findWindow(WindowTitle)
    try:
        widget = wrapInstance(int(qw), QWidget)
        # Create a QIcon object
        icon = QIcon(IconPath + "PlugIt_Window_Ico.png")
        # Assign the icon
        widget.setWindowIcon(icon)
    except:
        pass #Pour si on reload alos qu'il est dock


    mc.setToolTo("Move")
    mc.scriptJob(uiDeleted=[WindowTitle, atClose])

    return ui















































