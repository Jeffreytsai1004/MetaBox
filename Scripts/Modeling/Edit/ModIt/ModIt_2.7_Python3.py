#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel
import json
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI
# Import MayaAPI
import maya.api.OpenMaya as MayaAPI

try:    
    import MASH.api as mapi
except ImportError:
    print("MASH module could not be imported.")
    mapi = None

preferencePath = cmds.internalVar(upd = True)+"scripts/ModIt_script/Preferences/"


if cmds.workspaceControl("ModIt 2.6", exists =True):
    cmds.deleteUI("ModIt 2.6")

def createCustomWorkspaceControlModIt(*args):
    #UI_______________________________________

    cmds.columnLayout(adj = True, w=250, h=460)
              
    #_________________SUPP ERROR MESSAGE
    cmds.warning()
    print('', end=' ')

        #__________________________________________________________________PRIMITIVES
    #________________
    cH1 = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  PRIMITIVES", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    cmds.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,48), (2,48), (3,48), (4,48), (5,48) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )

    imageSphere = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Sphere.png"
    imageCube = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Cube.png"
    imageCylindre = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Cylindre.png"
    imagePlane = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Plane.png"
    imageDisc = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Disc.png"

    

    PShpere = cmds.symbolButton( image= imageSphere, c= "PSphere20()", ann= "Create Sphere")
    cmds.popupMenu()
    cmds.menuItem(l= 'Sphere sbdv 10', c= 'PSphere10()')
    cmds.menuItem(l= 'Sphere sbdv 12', c= 'PSphere12()')
    cmds.menuItem(l= 'Sphere sbdv 14', c= 'PSphere14()')
    cmds.menuItem(l= 'Sphere sbdv 16', c= 'PSphere16()')
    cmds.menuItem(l= 'Sphere sbdv 18', c= 'PSphere18()')
    cmds.menuItem(l= 'Sphere sbdv 20', c= 'PSphere20()')

    PCube = cmds.symbolButton( image= imageCube, c= "PCube1()", ann= "Create Cube ")
    cmds.popupMenu()
    cmds.menuItem(l= 'Cube sbdv 1', c= 'PCube1()')
    cmds.menuItem(l= 'Cube sbdv 2', c= 'PCube2()')
    cmds.menuItem(l= 'Cube sbdv 4', c= 'PCube4()')

    PCylindre = cmds.symbolButton( image= imageCylindre, c= "PCylY28()", ann= "Create Cylinder on X with 6 Subdiv)")
    cmds.popupMenu()
    cmds.menuItem(l= '__________X')
    cmds.menuItem(l= 'Cylindre X 8', c= 'PCylX8()')
    cmds.menuItem(l= 'Cylindre X 12', c= 'PCylX12()')
    cmds.menuItem(l= 'Cylindre X 16', c= 'PCylX16()')
    cmds.menuItem(l= 'Cylindre X 28', c= 'PCylX28()')
    cmds.menuItem(l= '__________Y')
    cmds.menuItem(l= 'Cylindre Y 8', c= 'PCylY8()')
    cmds.menuItem(l= 'Cylindre Y 12', c= 'PCylY12()')
    cmds.menuItem(l= 'Cylindre Y 16', c= 'PCylY16()')
    cmds.menuItem(l= 'Cylindre Y 28', c= 'PCylY28()')
    cmds.menuItem(l= '__________Z')
    cmds.menuItem(l= 'Cylindre Z 8', c= 'PCylZ8()')
    cmds.menuItem(l= 'Cylindre Z 12', c= 'PCylZ12()')
    cmds.menuItem(l= 'Cylindre Z 16', c= 'PCylZ16()')
    cmds.menuItem(l= 'Cylindre Z 28', c= 'PCylZ28()')


    PPlane = cmds.symbolButton( image= imagePlane, c= "PPlaneX()", ann= "Create a Plane on X, Y or Z axis")
    cmds.popupMenu()
    cmds.menuItem(l= 'Plane X', c= 'PPlaneX()')
    cmds.menuItem(l= 'Plane Y', c= 'PPlaneY()')
    cmds.menuItem(l= 'Plane Z', c= 'PPlaneZ()')
    PDisk = cmds.symbolButton( image= imageDisc, c= "PDiscZ12()", ann= "Create a Disc on X, Y or Z axis")
    cmds.popupMenu()
    cmds.menuItem(l= '__________X')
    cmds.menuItem(l= 'Disc X 8', c= 'PDiscX8()')
    cmds.menuItem(l= 'Disc X 12', c= 'PDiscX12()')
    cmds.menuItem(l= 'Disc X 16', c= 'PDiscX16()')
    cmds.menuItem(l= '__________Y')
    cmds.menuItem(l= 'Disc Y 8', c= 'PDiscY8()')
    cmds.menuItem(l= 'Disc Y 12', c= 'PDiscY12()')
    cmds.menuItem(l= 'Disc Y 16', c= 'PDiscY16()')
    cmds.menuItem(l= '__________Z')
    cmds.menuItem(l= 'Disc Z 8', c= 'PDiscZ8()')
    cmds.menuItem(l= 'Disc Z 12', c= 'PDiscZ12()')
    cmds.menuItem(l= 'Disc Z 16', c= 'PDiscZ16()')

    cmds.setParent(cH1)
    cmds.separator(h= 1, style = 'none')


    #________________
    #__________________________________________________________________TOOLS
    #________________


    cH2 = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  TOOLS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    cmds.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,40), (2,40), (3,40), (4,40), (5,40), (6,40) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )

    imageCam = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Cameras.png"
    imageHardEdge = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/HardEdge.png"
    imageSym = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Sym.png"
    imageBevAdd = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/BevAdd.png"
    
    CamO = cmds.symbolButton( image= imageCam, c= "CamOrtho()", ann= "Hide and Lock Orthographique Cameras")


    Sym = cmds.symbolButton( image= imageSym, c= "SymX()", ann= "Make Symetrie")
    cmds.popupMenu()
    cmds.menuItem(l= '________Symmetry Merge')
    cmds.menuItem(l= 'Symmetry on X', c= 'SymX()')
    cmds.menuItem(l= 'Symmetry on Y', c= 'SymY()')
    cmds.menuItem(l= 'Symmetry on Z', c= 'SymZ()')
    cmds.menuItem(l= '________Flip Selection World')
    cmds.menuItem(l= 'Flip on X World', c= 'FlipXWorld()')
    cmds.menuItem(l= 'Flip on Y World', c= 'FlipYWorld()')
    cmds.menuItem(l= 'Flip on Z World', c= 'FlipZWorld()')
    cmds.menuItem(l= '________Flip Selection Pivot')
    cmds.menuItem(l= 'Flip on X', c= 'FlipX()')
    cmds.menuItem(l= 'Flip on Y', c= 'FlipY()')
    cmds.menuItem(l= 'Flip on Z', c= 'FlipZ()')

    HardEdge = cmds.symbolButton( image= imageHardEdge, c= "HardEdges()", ann= "Be sure to be in edge mode")
    cmds.popupMenu()
    cmds.menuItem(l= 'Smooth 30', c= 'cmds.polySoftEdge(angle= 30)')
    cmds.menuItem(l= 'Smooth 35', c= 'cmds.polySoftEdge(angle= 35)')
    cmds.menuItem(l= 'Smooth 40', c= 'cmds.polySoftEdge(angle= 40)')
    cmds.menuItem(l= 'Smooth 45', c= 'cmds.polySoftEdge(angle= 45)')

    Align = cmds.symbolButton( image= "CenterPivot.png", c= "Align()", ann= "Select at least 3 Vertices, 2 Edges or 1 Face")
    cmds.popupMenu()
    cmds.menuItem(l= 'A to B', c= 'BtoA()')
 
    BevAdd = cmds.symbolButton( image= imageBevAdd, c= "EdgeFlow()", ann= "Add Edge Flow")
    
    UVs = cmds.symbolButton( image= "polyAutoProjLarge.png", c= "UVsAuto()", ann= "Auto UVs")
    cmds.popupMenu()
    cmds.menuItem(l= 'Auto UVs', c= 'UVsAuto()')
    cmds.menuItem(l= 'Planar UVs', c= 'UVsPlanar()')
    cmds.menuItem(l= 'UVs Shader', c= 'UVs()')


    cmds.setParent(cH2)
    cmds.separator(h= 1, style = 'none')


    #________________
    #__________________________________________________________________COLORS
    #________________

    cH3 = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  COLORS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    cmds.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,40), (2,40), (3,40), (4,40), (5,40), (6,40) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center'), (6, 'center') ] )

    imageColorLambert = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorLambert.png"
    imageColorGreen = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorGreen.png"
    imageColorRed = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorRed.png"
    imageColorBlue = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorBlue.png"
    imageColorYellow = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorYellow.png"
    imageColorDarkGrey = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/ColorDarkGrey.png"

    ColorLambert = cmds.symbolButton( image= imageColorLambert, c= "lambert1()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectLambert()')
    cmds.menuItem(l= 'Transparancy', c= 'TransLambert()')
    cmds.menuItem(l= 'Attribut', c= 'AttributLambert()')

    ColorGreen = cmds.symbolButton( image= imageColorGreen, c= "SelGreen()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectGreen()')
    cmds.menuItem(l= 'Transparancy', c= 'TransGreen()')
    cmds.menuItem(l= 'Attribut', c= 'AttributGreen()')

    ColorRed = cmds.symbolButton( image= imageColorRed, c= "SelRed()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectRed()')
    cmds.menuItem(l= 'Transparancy', c= 'TransRed()')
    cmds.menuItem(l= 'Attribut', c= 'AttributRed()')

    ColorBlue = cmds.symbolButton( image= imageColorBlue, c= "SelBlue()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectBlue()')
    cmds.menuItem(l= 'Transparancy', c= 'TransBlue()')
    cmds.menuItem(l= 'Attribut', c= 'AttributBlue()')

    ColorYellow = cmds.symbolButton( image= imageColorYellow, c= "SelYellow()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectYellow()')
    cmds.menuItem(l= 'Transparancy', c= 'TransYellow()')
    cmds.menuItem(l= 'Attribut', c= 'AttributYellow()')

    ColorDarkGrey = cmds.symbolButton( image= imageColorDarkGrey, c= "SelGreyDark()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select', c= 'SelectDarkGrey()')
    cmds.menuItem(l= 'Transparancy', c= 'TransDarkGrey()')
    cmds.menuItem(l= 'Attribut', c= 'AttributDarkGrey()')


    cmds.setParent(cH3)
    cmds.separator(h= 1, style = 'none')

    #________________
    #__________________________________________________________________SELECTIONS
    #________________

    cH5f = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  SELECTIONS", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    cmds.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,48), (2,48), (3,48), (4,48), (5,48)], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )


    imageSelIco1 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelIco1.png"
    imageSelIco1b = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelIco1b.png"
    imageSelIco2 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelIco2.png"
    imageSelIco3 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelIco3.png"
    imageSelIco4 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelIco4.png"
    
    SelInt = cmds.symbolButton( image= imageSelIco1b, c= "selInner()", ann= "Select the Faces Inside selection")
    SelIntPlus = cmds.symbolButton( image= imageSelIco1, c= "selInnerPlus()", ann= "Select the Faces Inside selection and keep selection")
    SelRingN = cmds.symbolButton( image= imageSelIco3, c= "selRingN2()", ann= "Select 1 Edge each 2 edge in Ring mode")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select 1 Edge each 2 edge in Ring mode', c= 'selRingN2()')
    cmds.menuItem(l= 'Select 1 Edge each 3 edge in Ring mode', c= 'selRingN3()')
    cmds.menuItem(l= 'Select 1 Edge each 4 edge in Ring mode', c= 'selRingN4()')
    
    SelLoopN = cmds.symbolButton( image= imageSelIco4, c= "selLoopN2()", ann= "Select 1 Edge each 2 edge in Loop mode")
    cmds.popupMenu()
    cmds.menuItem(l= 'Select 1 Edge each 2 edge in Loop mode', c= 'selLoopN2()')
    cmds.menuItem(l= 'Select 1 Edge each 3 edge in Loop mode', c= 'selLoopN3()')
    cmds.menuItem(l= 'Select 1 Edge each 4 edge in Loop mode', c= 'selLoopN4()')

    
    PolyCheck = cmds.symbolButton( image= imageSelIco2, c= "checkNGon()", ann= "Select all Ngon on the select Mesh") 
    cmds.popupMenu()
    cmds.menuItem(l= 'Select all Ngon Faces on the select Mesh', c= 'checkNGon()')
    cmds.menuItem(l= 'Select all Quadrangle Faces on the select Mesh', c= 'checkQuad()')
    cmds.menuItem(l= 'Select all Triangle Faces on the select Mesh', c= 'checkTri()')
    cmds.menuItem(l= 'Select all Concave Faces on the select Mesh', c= 'checkNConcave()')
    
     
     

    cmds.setParent(cH5f)
    cmds.separator(h= 8, style='in')
    cmds.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,30), (2,110), (3,30), (4,30), (5,30) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'right'), (4, 'right'), (5, 'right')  ] )

    imageMoins = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Moins.png"
    imagePlus = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Plus.png"
    imageDel = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Del.png"
    imageSetSel = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SelSet.png"

    Moins1 = cmds.symbolButton( image= imageMoins, c= "Moins1()", ann= "Remove from Selection 1")
    Store1 = cmds.button(l= "Store Selection 1", c= "Store1()", w= 110, bgc= [0.22, 0.22, 0.22])
    Plus1 = cmds.symbolButton( image= imagePlus, c= "Plus1()", ann= "Add to Selection 1")
    Del1 = cmds.symbolButton( image= imageDel, c= "Del1()", ann= "Delete Selection 1")
    SetSel1 = cmds.symbolButton( image= imageSetSel, c= "SetSel1()", ann= "Get Selection 1")

    Moins2 = cmds.symbolButton( image= imageMoins, c= "Moins2()", ann= "Remove from Selection 2")
    Store2 = cmds.button(l= "Store Selection 2", c= "Store2()", w= 110, bgc= [0.22, 0.22, 0.22])
    Plus2 = cmds.symbolButton( image= imagePlus, c= "Plus2()", ann= "Add to Selection 2")
    Del2 = cmds.symbolButton( image= imageDel, c= "Del2()", ann= "Delete Selection 2")
    SetSel2 = cmds.symbolButton( image= imageSetSel, c= "SetSel2()", ann= "Get Selection 2")

    cmds.setParent(cH5f)
    cmds.separator(h= 2, style = 'none')


    #________________
    #__________________________________________________________________DUPLICATIONS
    #________________

    cH5d = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  DUPLICATE", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])

    cmds.rowColumnLayout (  numberOfColumns=5, columnWidth=[ (1,56), (2,56), (3,18), (4,56), (5,56)], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center') ] )

    imageSeparator = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/separator.png"
    imageDup1 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/DupliIcon1.png"
    imageDup2 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/DupliIcon2.png"
    imageDup3 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/DupliIcon3.png"
    imageDup4 = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/DupliIcon4.png"
       
    SmartDupli = cmds.symbolButton( image= imageDup1, c= "SmartDupli()", ann= "Duplicate Using Previous Transform")
    DupliLinear = cmds.symbolButton( image= imageDup2, c= "DupLinear()", ann= "Linear X,Y,Z Duplicate. For Multiple Mesh Group them before.")
    separator = cmds.image( image= imageSeparator)
    Chain = cmds.symbolButton( image= imageDup3, c= "Chain()", ann= "Duplicate Along Curve")
    cmds.popupMenu()
    cmds.menuItem(l= 'Bezier', c= "Bezier()")
    cmds.menuItem(l= 'EPCurve', c= "EPCurve()")
    cmds.menuItem(l= 'PencilCurve', c= "Pencil()")
    cmds.menuItem(l= 'Chain_Asset', c= "ChainA()")
    
    ChainBake = cmds.symbolButton( image= imageDup4, c= "ChainBake()", ann= "Bake Chain")
   
    cmds.setParent(cH5d)


    #________________
    #__________________________________________________________________ARNOLD
    #________________

    cH5b = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  ARNOLD", cll =1, cl =0, bgc= [0.15, 0.15, 0.15])
    cmds.rowColumnLayout (  numberOfColumns=7, columnWidth=[ (1,36), (2,36), (3,18), (4,40), (5,40), (6,18), (7,40) ], columnAlign=[ (1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center'), (6, 'center'), (7, 'center') ] )


    imageArnoldSubdiv = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Arnold_Subdiv.png"
    imageArnoldOpaque = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Arnold_Opaque.png"
    imageArnoldStandInExport = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Arnold_StandIn_Export.png"
    imageArnolStandInReplace = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Arnold_StandIn_Replace.png"
    imageArnolDOFVisor = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Arnold_DOFvisor.png"


    A_Subdiv = cmds.symbolButton( image= imageArnoldSubdiv, c= "Arnold_Sbdv_ON()", ann= "Activate Arnold Subdiv")
    cmds.popupMenu()
    cmds.menuItem(l= 'SubDv 1', c= "Arnold_Sbdv_1()")
    cmds.menuItem(l= 'SubDv 2', c= "Arnold_Sbdv_ON()")
    cmds.menuItem(l= 'SubDv 3', c= "Arnold_Sbdv_3()")
    cmds.menuItem(l= 'SubDv 4', c= "Arnold_Sbdv_4()")
    cmds.menuItem(l= 'Desactivate Arnold Subdiv', c= "Arnold_Sbdv_OFF()")
    A_Opaque = cmds.symbolButton( image= imageArnoldOpaque, c= "Arnold_Opaque_ON()", ann= "Desactivate Arnold Opaque")
    cmds.popupMenu()
    cmds.menuItem(l= 'Activate Arnold Opaque', c= "Arnold_Opaque_OFF()")
    separator = cmds.image( image= imageSeparator)
    A_StandInExport = cmds.symbolButton( image= imageArnoldStandInExport, c= "setStandInPath()", ann= "Set a path for StandIn export")
    A_StandInReplace = cmds.symbolButton( image= imageArnolStandInReplace, c= "Convert_To_StandIn()", ann= "Convert to StandIn")
    separator = cmds.image( image= imageSeparator)
    A_DOFVisor = cmds.symbolButton( image= imageArnolDOFVisor, c= "CamFocus()", ann= "Apply Face Color")
    cmds.popupMenu()
    cmds.menuItem(l= 'Aperture Attributes', c= "ApertureAttributes()")
    cmds.menuItem(l= 'Delete Camera Focus', c= "CamFocusOFF()")

    cmds.setParent(cH5b)
    cmds.separator(h= 1, style = 'none')




 
    #__________________________________________________________________SCREW and BOLTS
    #________________

    cH8 = cmds.columnLayout(adj =True)
    frameEdit = cmds.frameLayout(l = "  SREWS and BOLTS", cll =1, cl =1, bgc= [0.15, 0.15, 0.15])


    imageCustom= cmds.internalVar(upd = True)+"scripts/ShadeIt_script/Icons/Empty.png" 
    imageScrewA= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_A.png"
    imageScrewB= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_B.png"
    imageScrewC= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_C.png"
    imageScrewD= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_D.png"
    imageScrewE= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_E.png"
    imageScrewF= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Screw_F.png"

    imageBoltA= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_A.png"
    imageBoltB= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_B.png"
    imageBoltC= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_C.png"
    imageBoltD= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_D.png"
    imageBoltE= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_E.png"
    imageWasher= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Washer.png"
    
    imageBoltG= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_G.png"
    imageBoltH= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_H.png"
    imageBoltI= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_I.png"
    imageBoltJ= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_J.png"
    imageBoltK= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_K.png"
    imageBoltL= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Bolt_L.png"
    
    
    imageSF1= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_1.png"
    imageSF2= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_2.png"
    imageSF3= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_3.png"
    imageSF4= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_4.png"        
    imageSF5= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_5.png"
    imageSF6= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_6.png"
    imageSF7= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_7.png"
    imageSF8= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_8.png"
    imageSF9= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_9.png"
    imageSF10= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_10.png"        
    imageSF11= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_11.png"
    imageSF12= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_12.png"    
    imageSF13= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_13.png"
    imageSF14= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_14.png"
    imageSF15= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_15.png"
    imageSF16= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_16.png"        
    imageSF17= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_17.png"
    imageSF18= cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/SF_18.png"                    
                                    
                                                                    
    cmds.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,39), (2,39), (3,39), (4,39), (5,39), (6,39) ] )
    
    ScrewA = cmds.symbolButton( image= imageScrewA, c= "ScrewA()", ann= "Add Screw A")
    ScrewB = cmds.symbolButton( image= imageScrewB, c= "ScrewB()", ann= "Add Screw B")
    ScrewC = cmds.symbolButton( image= imageScrewC, c= "ScrewC()", ann= "Add Screw C")
    ScrewD = cmds.symbolButton( image= imageScrewD, c= "ScrewD()", ann= "Add Screw D")
    ScrewE = cmds.symbolButton( image= imageScrewE, c= "ScrewE()", ann= "Add Screw E")
    ScrewF = cmds.symbolButton( image= imageScrewF, c= "ScrewF()", ann= "Add Screw F")


    BoltA = cmds.symbolButton( image= imageBoltA, c= "BoltA()", ann= "Add Bolt A")
    BoltB = cmds.symbolButton( image= imageBoltB, c= "BoltB()", ann= "Add Bolt B")
    BoltC = cmds.symbolButton( image= imageBoltC, c= "BoltC()", ann= "Add Bolt C")
    BoltD = cmds.symbolButton( image= imageBoltD, c= "BoltD()", ann= "Add Bolt D")
    BoltE = cmds.symbolButton( image= imageBoltE, c= "BoltE()", ann= "Add Bolt E")
    Washer = cmds.symbolButton( image= imageWasher, c= "Washer()", ann= "Add Washer")
    
    BoltG = cmds.symbolButton( image= imageBoltG, c= "BoltG()", ann= "Add Bolt A")
    BoltH = cmds.symbolButton( image= imageBoltH, c= "BoltH()", ann= "Add Bolt B")
    BoltI = cmds.symbolButton( image= imageBoltI, c= "BoltI()", ann= "Add Bolt C")
    BoltJ = cmds.symbolButton( image= imageBoltJ, c= "BoltJ()", ann= "Add Bolt D")
    BoltK = cmds.symbolButton( image= imageBoltK, c= "BoltK()", ann= "Add Bolt E")
    BoltL = cmds.symbolButton( image= imageBoltL, c= "BoltL()", ann= "Add Bolt E")
    
    cmds.popupMenu()
    cmds.menuItem(l= 'Chain_B', c= "ChainB()")
    cmds.setParent( '..' )


    cH9 = cmds.columnLayout(adj =True)
    cmds.separator(h= 3, style='in')


    cmds.rowColumnLayout (  numberOfColumns=6, columnWidth=[ (1,39), (2,39), (3,39), (4,39), (5,39), (6,39) ] )
    
    SF1 = cmds.symbolButton( image= imageSF1, c= "SF1()", ann= "Add SF 1")
    SF2 = cmds.symbolButton( image= imageSF2, c= "SF2()", ann= "Add SF 2")
    SF3 = cmds.symbolButton( image= imageSF3, c= "SF3()", ann= "Add SF 3")
    SF4 = cmds.symbolButton( image= imageSF4, c= "SF4()", ann= "Add SF 4")
    SF5 = cmds.symbolButton( image= imageSF5, c= "SF5()", ann= "Add SF 5")
    SF6 = cmds.symbolButton( image= imageSF6, c= "SF6()", ann= "Add SF 6")

    SF7 = cmds.symbolButton( image= imageSF7, c= "SF7()", ann= "Add SF 7")
    SF8 = cmds.symbolButton( image= imageSF8, c= "SF8()", ann= "Add SF 8")
    SF9 = cmds.symbolButton( image= imageSF9, c= "SF9()", ann= "Add SF 9")
    SF10 = cmds.symbolButton( image= imageSF10, c= "SF10()", ann= "Add SF 10")
    SF11 = cmds.symbolButton( image= imageSF11, c= "SF11()", ann= "Add SF 11")
    SF12 = cmds.symbolButton( image= imageSF12, c= "SF12()", ann= "Add SF 12")
    
    SF13 = cmds.symbolButton( image= imageSF13, c= "SF13()", ann= "Add SF 13")
    SF14 = cmds.symbolButton( image= imageSF14, c= "SF14()", ann= "Add SF 14")
    SF15 = cmds.symbolButton( image= imageSF15, c= "SF15()", ann= "Add SF 15")
    SF16 = cmds.symbolButton( image= imageSF16, c= "SF16()", ann= "Add SF 16")
    SF17 = cmds.symbolButton( image= imageSF17, c= "SF17()", ann= "Add SF 17")
    SF18 = cmds.symbolButton( image= imageSF18, c= "SF18()", ann= "Add SF 18")
    
    
    cmds.setParent(cH8)   
    
    cmds.separator(h= 1, style = 'none')
    cmds.setParent( '..' )

#_________________________________________________________________________________________________________________HELP&INFO
    cH9 = cmds.columnLayout(adj =True)
    frameConvert = cmds.frameLayout(l = "Help & Info", cll =1, cl =1, bgc= [0.15, 0.15, 0.15])

    DiscordIcon = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Discord.png"
    WzxIcon = cmds.internalVar(upd = True)+"scripts/ModIt_script/Icons/Wzx.png"
    
    cmds.separator(h= 1, style = 'none')
    Discord = cmds.symbolButton( image= DiscordIcon, c= "DiscordLink()", ann= "Help about Cable on the Disord")
    cmds.separator(h= 8, style = 'none')
    WzxStore = cmds.symbolButton( image= WzxIcon, c= "WzxStoreLink()", ann= "Other Scripts and Tutorials on the WzxStore")

    cmds.setParent( '..' )


    cmds.separator(h= 10, style = 'none')
    cmds.setParent( '..' )
    cmds.setParent( '..' )

#________________




cmds.workspaceControl("ModIt 2.6", retain=False, floating=True, li= True, uiScript="createCustomWorkspaceControlModIt()");




class COMAND():
    def Comand():
        cmds.launch(web= "https://wizix.artstation.com/")

###________________________________________PRIMITIVES_______________________________###
###_________SPHERE

def PSphere10():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 10, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 10, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

def PSphere12():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 12, sy= 6, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 12, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

def PSphere14():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 14, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 14, sy= 8, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

def PSphere16():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 16, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 16, sy= 0o1, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

def PSphere18():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 18, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 18, sy= 10, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

def PSphere20():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polySphere(r= 1, sx= 20, sy= 12, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Sphere_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polySphere(r= 1, sx= 20, sy= 12, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Sphere_001")

###_________CUBE

def PCube1():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 1,sy= 1,sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cube_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 1,sy= 1,sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cube_001")

def PCube2():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 2,sy= 2,sz= 2, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cube_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 2,sy= 2,sz= 2, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cube_001")
   
def PCube4():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 4,sy= 4,sz= 4, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cube_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCube(w= 2, h= 2, d= 2, sx= 4,sy= 4,sz= 4, ax= [0, 1, 0], cuv= 4, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cube_001")
    
    
###_________CYLINDRE
   
def PCylX8():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
    

def PCylX12():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")

def PCylX16():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")


def PCylX28():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [1, 0, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
        

def PCylY8():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
        
    
def PCylY12():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
    

def PCylY16():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
        
def PCylY28():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 1, 0],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
    
def PCylZ8():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 8)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")

    
def PCylZ12():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 12)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")


def PCylZ16():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 16)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
        

def PCylZ28():
    selection = cmds.ls(sl= True)
    if selection == []:
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.rename("Cylinder_001")
        
    else: 
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        objectPrim = cmds.polyCylinder(r= 1, h= 2, sy= 1,sz= 0, ax= [0, 0, 1],sc= 0, cuv= 4, ch= 1, sa= 28)
        cmds.polySoftEdge (a= 45, ch= 1)
        cmds.select(objectPrim)
        cmds.move(pos[0], pos[1], pos[2])
        constr = cmds.normalConstraint(selection, objectPrim, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename("Cylinder_001")
        
   
    
    
###_________PLANE

def PPlaneX():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [1, 0, 0], cuv= 2, ch= 1)
        cmds.rename("Plane_001")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.rename("Plane")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_001") 


def PPlaneY():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.rename("Plane_001")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.rename("Plane")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_001") 


def PPlaneZ():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [0, 0, 1], cuv= 2, ch= 1)
        cmds.rename("Plane_001")

    else: 
    
        name = "Plane"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyPlane(w= 2, h= 2, sx= 1, sy= 1, ax= [0, 1, 0], cuv= 2, ch= 1)
        cmds.rename("Plane")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_001") 

    
###_________DISK

def PDiscX8():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")
    
    
def PDiscX12():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")
    
    
def PDiscX16():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(0, 0, -90)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")

    
def PDiscY8():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")

def PDiscY12():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")

def PDiscY16():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")


def PDiscZ8():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 8, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")

   
def PDiscZ12():
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 12, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")   
    
    
def PDiscZ16():
    
    selection = cmds.ls(sl= True)

    if selection == []:
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc_1")

    else: 
    
        name = "Disc"
        import maya.mel as mel
        mel.eval("setToolTo $gMove;")
        pos = cmds.manipMoveContext('Move', query=True, position=True) 
        cmds.polyDisc(sides= 16, subdivisionMode= 4, subdivisions= 1,radius= 1)
        cmds.rotate(90, 0, 0)
        cmds.rename("Disc")
        cmds.move(pos[0], pos[1], pos[2], name)
        constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
        cmds.delete(constr)
        cmds.rename(name, name + "_01")  
    
  
    
        

###________________________________________TOOLS_______________________________###
###_________CAMRRE

def CamOrtho():
    cmds.setAttr( "top.visibility", 0)
    cmds.setAttr( "top.v", lock= True)

    cmds.setAttr( "front.visibility", 0)
    cmds.setAttr( "front.v", lock= True)

    cmds.setAttr( "side.visibility", 0)
    cmds.setAttr( "side.v", lock= True)
    
    print("DONE")



###_________SYM

def SymX():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            cmds.FreezeTransformations()
            cmds.delete(ch= True)
            cmds.duplicate()
            cmds.rename("Dupli")
            cmds.setAttr("Dupli.scaleX", -1)
            cmds.polyUnite(selection, "Dupli", n = "polyTemps")
            cmds.delete(ch= True)
            cmds.CenterPivot()
            cmds.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            cmds.rename("Combiningwzx")
        

def SymY():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            cmds.FreezeTransformations()
            cmds.delete(ch= True)
            cmds.duplicate()
            cmds.rename("Dupli")
            cmds.setAttr("Dupli.scaleY", -1)
            cmds.polyUnite(selection, "Dupli", n = "polyTemps")
            cmds.delete(ch= True)
            cmds.CenterPivot()
            cmds.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            cmds.rename("Combiningwzx")        

def SymZ():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)

    for each in selection:
            cmds.FreezeTransformations()
            cmds.delete(ch= True)
            cmds.duplicate()
            cmds.rename("Dupli")
            cmds.setAttr("Dupli.scaleZ", -1)
            cmds.polyUnite(selection, "Dupli", n = "polyTemps")
            cmds.delete(ch= True)
            cmds.CenterPivot()
            cmds.polyMergeVertex( d = 0.001, am =  1,ch= 0)
            cmds.rename("Combiningwzx")    
    
    
def FlipXWorld():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    for each in selection:
            DupSel = cmds.duplicate(rc= True)
            cmds.group(em= True, n="DupliF")
            cmds.parent(DupSel, 'DupliF')
            cmds.setAttr("DupliF.scaleX", -1)
            cmds.rename("DupliF", "DupliFlip")

def FlipYWorld():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    for each in selection:
            DupSel = cmds.duplicate(rc= True)
            cmds.group(em= True, n="DupliF")
            cmds.parent(DupSel, 'DupliF')
            cmds.setAttr("DupliF.scaleY", -1)
            cmds.rename("DupliF", "DupliFlip")

def FlipZWorld():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    for each in selection:
            DupSel = cmds.duplicate(rc= True)
            cmds.group(em= True, n="DupliF")
            cmds.parent(DupSel, 'DupliF')
            cmds.setAttr("DupliF.scaleZ", -1)
            cmds.rename("DupliF", "DupliFlip")


def FlipX():
    cmds.duplicate(rc= True)
    cmds.rename("DupliF")
    cmds.setAttr("DupliF.scaleX", -1)
    cmds.rename("DupliF", "DupliFlip")

def FlipY():
    cmds.duplicate(rc= True)
    cmds.rename("DupliF")
    cmds.setAttr("DupliF.scaleY", -1)
    cmds.rename("DupliF", "DupliFlip")

def FlipZ():
    cmds.duplicate(rc= True)
    cmds.rename("DupliF")
    cmds.setAttr("DupliF.scaleX", -1)
    cmds.rename("DupliF", "DupliFlip")

###___________________________________________________________________________HARDEDGES
def HardEdges():
        cmds.polySelectConstraint(m= 3, t= 0x8000, sm= 1)
        cmds.polySelectConstraint(m= 0) 



def EdgeFlow():
    
    storeSelection = cmds.ls(sl=True)
    cmds.ConvertSelectionToContainedEdges()
    origEdge = cmds.sets(n="origEdgeSet")
    cmds.select(storeSelection)
    cmds.polySubdivideFacet (duv= 2, dvv= 1, sbm= 1, ch= 1)
    cmds.ConvertSelectionToContainedEdges()
    newsEdge = cmds.sets(n="newsEdgeSet")
    edge = cmds.sets("origEdgeSet", sub="newsEdgeSet")
    cmds.select(edge)
    cmds.polyEditEdgeFlow (constructionHistory= 1, adjustEdgeFlow= 1)
    cmds.delete("newsEdgeSet", "origEdgeSet")
    cmds.ConvertSelectionToFaces()





###___________________________________________________________________________UVS

def UVsAuto():   
    selection = cmds.ls(sl = True, fl = True, dag = True, type= 'mesh')
    
    for each in selection:
        cmds.DeleteHistory()
        cmds.polyAutoProjection(lm= 0, pb= 0, ibd= 1, sc= 1, o= 1, p= 3, ps= 0.1, ws= 0)
        cmds.polyEditUV(pu= 0.5, pv= 0.5, su= 0.5, sv= 0.5, u= -0.25, v= 0.25)
        cmds.select(each)
        cmds.DeleteHistory()
        print("UV Done")
    
def UVsPlanar():
    
    selection = cmds.ls(sl = True, fl = True, dag = True, type= 'mesh')
    
    for each in selection:
        cmds.DeleteHistory()
        cmds.polyProjection( each + '.f[*]', ch= 1, type= "planar", ibd= True, kir= True,  md= "c" )
        cmds.polyEditUV(pu= 0.5, pv= 0.5, su= 0.5, sv= 0.5, u= -0.25, v= 0.25)
        cmds.select(each)
        cmds.DeleteHistory()
        print("UV Done")

def UVs():
    
    UVsPath = cmds.internalVar(upd = True)+"scripts/ModIt_script/Shaders/Uvs.ma"
    selection = cmds.ls(sl = True, fl = True, dag = True)

    if cmds.objExists('UVs'):
      print("UVs_EXIST")
      for each in selection:
        cmds.hyperShade( a= "UVs")
        cmds.select("UVs")
        print("Done")
        
    else:
      cmds.sets(n= "Settemps")
      cmds.file(UVsPath, i = True)
      cmds.binMembership("UVs", addToBin= "Viewport_Shaders")
      cmds.select("Settemps")
      cmds.ls(selection= True)
      cmds.delete("Settemps")
      for each in selection:
        cmds.hyperShade( a= "UVs")
        cmds.select("UVs")
        print("Done")   

def BtoA():
    cmds.MatchTranslation()
    cmds.MatchRotation()
 

###________________________________________________________________________FACES COLORS
def lambert1():

    cmds.hyperShade( assign= "lambert1" )
    

def SelGreen():

    selection = cmds.ls(sl= True)

    if cmds.objExists('Sel_Green'):
        cmds.hyperShade( assign= "Sel_Green" )
    
    else:
        LambertGreen = cmds.shadingNode("lambert",asShader=True)
        cmds.setAttr(LambertGreen + ".color", 0.0, 0.798, 0.292, type = 'double3')
        cmds.rename("Sel_Green")
        cmds.select(selection)
        cmds.hyperShade( assign= "Sel_Green" )



def SelRed():

    selection = cmds.ls(sl= True)

    if cmds.objExists('Sel_Red'):
        cmds.hyperShade( assign= "Sel_Red" )
    
    else:
        LambertRed = cmds.shadingNode("lambert",asShader=True)
        cmds.setAttr(LambertRed + ".color", 0.7, 0.011, 0.011, type = 'double3')
        cmds.rename("Sel_Red")
        cmds.select(selection)
        cmds.hyperShade( assign= "Sel_Red" )

def SelBlue():

    selection = cmds.ls(sl= True)

    if cmds.objExists('Sel_Blue'):
        cmds.hyperShade( assign= "Sel_Blue" )
    
    else:
        LambertBlue = cmds.shadingNode("lambert",asShader=True)
        cmds.setAttr(LambertBlue + ".color", 0, 0.432, 0.7, type = 'double3')
        cmds.rename("Sel_Blue")
        cmds.select(selection)
        cmds.hyperShade( assign= "Sel_Blue" )

def SelYellow():

    selection = cmds.ls(sl= True)

    if cmds.objExists('Sel_Yellow'):
        cmds.hyperShade( assign= "Sel_Yellow" )
    
    else:
        LambertYellow = cmds.shadingNode("lambert",asShader=True)
        cmds.setAttr(LambertYellow + ".color", 0.9, 0.450, 0.0, type = 'double3')
        cmds.rename("Sel_Yellow")
        cmds.select(selection)
        cmds.hyperShade( assign= "Sel_Yellow" )

def SelGreyDark():

    selection = cmds.ls(sl= True)

    if cmds.objExists('Sel_GreyDark'):
        cmds.hyperShade( assign= "Sel_GreyDark" )
    
    else:
        LambertGreyDark = cmds.shadingNode("lambert",asShader=True)
        cmds.setAttr(LambertGreyDark + ".color", 0.05, 0.05, 0.05, type = 'double3')
        cmds.rename("Sel_GreyDark")
        cmds.select(selection)
        cmds.hyperShade( assign= "Sel_GreyDark" )    
        

def SelectLambert():

    if cmds.objExists('lambert1'):
       cmds.hyperShade( objects= "lambert1" )
    
    else:
        print("Please First Create this FaceColor Shader")   


def SelectGreen():

    if cmds.objExists('Sel_Green'):
       cmds.hyperShade( objects= "Sel_Green" )
    
    else:
        print("Please First Create this FaceColor Shader")         
        
        
def SelectRed():

    if cmds.objExists('Sel_Red'):
       cmds.hyperShade( objects= "Sel_Red" )
    
    else:
        print("Please First Create this FaceColor Shader")  


def SelectBlue():

    if cmds.objExists('Sel_Blue'):
       cmds.hyperShade( objects= "Sel_Blue" )
    
    else:
        print("Please First Create this FaceColor Shader")  

def SelectYellow():

    if cmds.objExists('Sel_Yellow'):
       cmds.hyperShade( objects= "Sel_Yellow" )
    
    else:
        print("Please First Create this FaceColor Shader")  

def SelectDarkGrey():

    if cmds.objExists('Sel_GreyDark'):
       cmds.hyperShade( objects= "Sel_GreyDark" )
    
    else:
        print("Please First Create this FaceColor Shader")   


def TransGreen():

    if cmds.objExists('Sel_Green'):
       cmds.window( title='Green Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='Sel_Green.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributGreen():

    if cmds.objExists('Sel_Green'):
       cmds.select('Sel_Green')
    
    else:
        print("Please First Create this FaceColor Shader") 


def TransLambert():

    if cmds.objExists('lambert1'):
       cmds.window( title='Lambert Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='lambert1.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributLambert():

    if cmds.objExists('lambert1'):
       cmds.select('lambert1')
    
    else:
        print("Please First Create this FaceColor Shader") 

def TransRed():

    if cmds.objExists('Sel_Red'):
       cmds.window( title='Red Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='Sel_Red.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributRed():

    if cmds.objExists('Sel_Red'):
       cmds.select('Sel_Red')
    
    else:
        print("Please First Create this FaceColor Shader") 


def TransBlue():

    if cmds.objExists('Sel_Blue'):
       cmds.window( title='Blue Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='Sel_Blue.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributBlue():

    if cmds.objExists('Sel_Blue'):
       cmds.select('Sel_Blue')
    
    else:
        print("Please First Create this FaceColor Shader") 


def TransYellow():

    if cmds.objExists('Sel_Yellow'):
       cmds.window( title='Yellow Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='Sel_Yellow.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributYellow():

    if cmds.objExists('Sel_Yellow'):
       cmds.select('Sel_Yellow')
    
    else:
        print("Please First Create this FaceColor Shader") 


def TransDarkGrey():

    if cmds.objExists('Sel_GreyDark'):
       cmds.window( title='GreyDark Transparancy' )
       cmds.columnLayout()
       cmds.attrColorSliderGrp( at='Sel_GreyDark.transparency')
       cmds.showWindow()
    
    else:
        print("Please First Create this FaceColor Shader")         
   

def AttributDarkGrey():

    if cmds.objExists('Sel_GreyDark'):
       cmds.select('Sel_GreyDark')
    
    else:
        print("Please First Create this FaceColor Shader") 


class ALIGN():
    def Comand():
        cmds.launch(web= "https://wizix.artstation.com/")
        
        
###________________________________________________________________________ALIGN
def Align():
    cmds.setToolTo('Move')
    getPivotPos = mel.eval("float $getPivotPos[] = `manipMoveContext -q -p Move`;")
    mel.eval("ConvertSelectionToVertices;")
    vtxSel=cmds.ls(fl=1, sl=1)
    selectedObjectStore= cmds.ls(o=1, sl=1)
    objectSelectionStore= cmds.listRelatives(selectedObjectStore[0], p=1)
    if len(vtxSel)<3:
        cmds.warning("Please select at least 3 Vertices, 2 Edges or 1 Face")
        
    plane=cmds.polyPlane(cuv=2, sy=1, sx=1, h=1, n='rotationPlane', ch=1, w=1, ax=(0, 1, 0))
    cmds.select((plane[0] + ".vtx[0:2]"), 
        vtxSel[0], vtxSel[1], vtxSel[2])
    mel.eval("snap3PointsTo3Points(0)")
    cmds.parent(objectSelectionStore, plane[0])
    cmds.makeIdentity(objectSelectionStore, apply=True, s=0, r=1, t=0, n=0)
    cmds.xform(ws=1, piv=(getPivotPos[0], getPivotPos[1], getPivotPos[2]))
    cmds.parent(objectSelectionStore, world=1)
    cmds.delete(plane)







###________________________________________SELECTIONS_______________________________###
###_________STORE1

def Store1():
    
    if cmds.objExists('ModSet1'):
       cmds.sets(add = "ModSet1")
      
    else :
       newSet1 = cmds.sets(n = "ModSet1")


def Plus1():
    cmds.sets(add = "ModSet1")


def Moins1():
    cmds.sets(rm = "ModSet1")


def Del1():
    cmds.delete("ModSet1")


def SetSel1():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    
    cmds.select( "ModSet1" )
    cmds.ls( selection= True )
    import maya.mel as mel    
    mel.eval('setSelectMode components Components; selectType -smp 0 -sme 1 -smf 0 -smu 0 -pv 0 -pe 1 -pf 0 -puv 0; HideManipulators;')


###_________STORE2

def Store2():
    
    if cmds.objExists('ModSet2'):
       cmds.sets(add = "ModSet2")
      
    else :
       newSet1 = cmds.sets(n = "ModSet2")


def Plus2():
    cmds.sets(add = "ModSet2")


def Moins2():
    cmds.sets(rm = "ModSet2")


def Del2():
    cmds.delete("ModSet2")


def SetSel2():
    selection = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    
    cmds.select( "ModSet2" )
    cmds.ls( selection= True )
    import maya.mel as mel    
    mel.eval('setSelectMode components Components; selectType -smp 0 -sme 1 -smf 0 -smu 0 -pv 0 -pe 1 -pf 0 -puv 0; HideManipulators;')



def Clean():
    cmds.sets(n = "selInnerPlusSet1")
    cmds.sets(add = "selInnerPlusSet1")
    cmds.SelectFacetMask()  
    cmds.polyUVSet(d= True, uvSet = "ModIt_UvLayout")
    cmds.select( clear=True )
    cmds.select( "selInnerPlusSet1" )
    cmds.delete( "selInnerPlusSet1" )

def CleanPluss():
    cmds.sets(n = "selInnerPlusSet1")
    cmds.sets(add = "selInnerPlusSet1")
    cmds.SelectFacetMask()  
    cmds.polyUVSet(d= True, uvSet = "ModIt_UvLayout")
    cmds.select( clear=True )
    cmds.select( "selInnerPlusSet1" )
    cmds.delete( "selInnerPlusSet1" )
    cmds.GrowPolygonSelectionRegion()
    


def selInner():
    selFace=cmds.ls(sl=True)
    selObj = cmds.ls(sl=1, fl=1, o=1)

    cmds.polyProjection (selObj, ch=1, type= "Planar", ibd = False, cm= True, uvSetName = "ModIt_UvLayout", kir = True, md= "c")
    cmds.polyUVSet(cuv= True, uvSet = "ModIt_UvLayout")

    selEdgePeri = cmds.ConvertSelectionToEdgePerimeter()
    cmds.polyMapCut()

    cmds.SelectMeshUVShell()

    cmds.scriptJob( runOnce=True, e = ["SelectionChanged", Clean])


def selInnerPlus():
    selFace=cmds.ls(sl=True)
    selObj = cmds.ls(sl=1, fl=1, o=1)

    cmds.polyProjection (selObj, ch=1, type= "Planar", ibd = False, cm= True, uvSetName = "ModIt_UvLayout", kir = True, md= "c")
    cmds.polyUVSet(cuv= True, uvSet = "ModIt_UvLayout")

    selEdgePeri = cmds.ConvertSelectionToEdgePerimeter()
    cmds.polyMapCut()

    cmds.SelectMeshUVShell()

    cmds.scriptJob( runOnce=True, e = ["SelectionChanged", CleanPluss])




def selRingN2():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeRing", 2))

def selRingN3():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeRing", 3))

def selRingN4():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeRing", 4))

def selLoopN2():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeLoop", 2))

def selLoopN3():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeLoop", 3))

def selLoopN4():
    mel.eval('polySelectEdgesEveryN "%s" %s;' % ("edgeLoop", 4))


def checkNGon():
    cmds.selectMode(q=True, co=True)
    cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=3)
    cmds.polySelectConstraint(dis=True)

def checkTri():
    cmds.selectMode(q=True, co=True)
    cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=1)
    cmds.polySelectConstraint(dis=True)

def checkQuad():
    cmds.selectMode(q=True, co=True)
    cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=2)
    cmds.polySelectConstraint(dis=True)


def checkNConcave():
    cmds.selectMode(q=True, co=True)
    cmds.polySelectConstraint(m=3 ,t = 0x0008, c=1)
    cmds.polySelectConstraint(dis=True)







###________________________________________ARNOLD______________________________###
###_________
def Arnold_Sbdv_ON():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiSubdivType", 1)
            cmds.setAttr(each + ".aiSubdivIterations", 2)

def Arnold_Sbdv_1():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiSubdivType", 1)
            cmds.setAttr(each + ".aiSubdivIterations", 1)


def Arnold_Sbdv_3():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiSubdivType", 1)
            cmds.setAttr(each + ".aiSubdivIterations", 3)

def Arnold_Sbdv_4():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiSubdivType", 1)
            cmds.setAttr(each + ".aiSubdivIterations", 4)

def Arnold_Sbdv_OFF():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiSubdivType", 0)
            cmds.setAttr(each + ".aiSubdivIterations", 0)

def Arnold_Opaque_ON():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiOpaque", 0)

def Arnold_Opaque_OFF():
    selection = cmds.ls(sl = True, fl = True, dag = True, type= "mesh")

    for each in selection:
            cmds.setAttr(each + ".aiOpaque", 1)


def setStandInPath():
    Path = cmds.fileDialog2(ds=1,cap="Select your path",fm=2)
    Path=Path[0]
    print(Path)
    d = {'path': Path}
    s = json.dumps(d)
    open(preferencePath + 'StandIn_path.json',"w").write(s)

def Convert_To_StandIn():
    pref_path=open(preferencePath + 'StandIn_path.json',"r")
    data_pref = json.load(pref_path)
    global Path
    Path=(data_pref['path'])
    d = {'path': Path}

    selName = cmds.ls(sl=True)[0]
    sel = cmds.ls(sl=True)

    cmds.file(Path + "/" + selName + ".ass", force=True, typ="ASS Export", pr=True, es=True)
    cmds.delete(sel)
    importASS = cmds.file(Path + "/" + selName + ".ass", rnn=True, i=True, type= "ASS",  ignoreVersion=True, mergeNamespacesOnClash=False)
    cmds.select(importASS)
    cmds.CenterPivot()
    transforms = cmds.ls(importASS, type='transform')
    for i, object in enumerate(transforms):
        cmds.rename(object, selName)

    cmds.setAttr(selName + "Shape.mode", 5)
    cmds.setAttr(selName + "Shape.overrideEnabled", 1)
    cmds.setAttr(selName + "Shape.overrideRGBColors", 1)
    cmds.setAttr(selName + "Shape.overrideColorRGB", 0.05, 0.05, 0.05)
    cmds.delete("ArnoldStandInDefaultLightSet")
    print("ASS Convert")
    
    
def CamFocus():
    
    FD_toolPath = cmds.internalVar(upd = True)+"scripts/ModIt_script/Tools/FocusDistanceTool.ma"

    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cmds.select(camPath)
        
    
    if cmds.objExists('CamOrgin'):
      print("Delete Existing Focus First")
      
    if camPath == "|persp|perspShape":
        cmds.warning("Don't work on Persp Camera")


    else:
        cmds.file(FD_toolPath,i=True)

        cmds.matchTransform("FD_Group",camPath , pos=True,rot=True, piv=True)
        cmds.parent("FD_Group",camPath)


        cmds.setAttr(camPath +".aiEnableDOF", 1)
        cmds.connectAttr("FocusDistance.distance", camPath + ".aiFocusDistance")

def CamFocusOFF():
    cmds.delete("FD_Group")


def ApertureAttributes():
    if cmds.window("DOFWindows", exists =True):
        cmds.deleteUI("DOFWindows")
        
            
    cmds.window("DOFWindows", title='Aperture Size', s= True, w= 500 )
    cmds.columnLayout(adj =True, w= 400)

    cmds.separator(h= 8, style = 'none')
    cmds.checkBox("Enable_DOF", onc = "enableDOF_ON()", ofc ="enableDOF_OFF()" , w= 200, align='right')
    cmds.separator(h= 4, style = 'none')

    cmds.floatSliderGrp('Slider_Aperture', l = "Aperture Size",pre= 3, min =0, max =5 ,po =True, field =True, cc="ApertureSize()", dc="ApertureSize()", adj =0, cat= [1, "left", 3], cw= [1, 80])
    cmds.separator(h= 5, style = 'none')



    def UpdateInfo():
        ApertureValue = GetApertureSize()
        EnableDOFValue = GetEnableDOF()
        cmds.floatSliderGrp( "Slider_Aperture",e=True, value = ApertureValue)
        cmds.checkBox( "Enable_DOF",e=True, value = EnableDOFValue)

    UpdateInfo()


    cmds.showWindow()


def enableDOF_ON():
    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    
    cmds.setAttr(camPath + ".aiEnableDOF", 1)

def enableDOF_OFF():
    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    
    cmds.setAttr(camPath + ".aiEnableDOF", 0)
    

def ApertureSize():
    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    
    myValueWidght = cmds.floatSliderGrp("Slider_Aperture", q= True, value=True)
    cmds.setAttr(camPath + ".aiApertureSize", myValueWidght)

def GetApertureSize():
    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    
    getValue = cmds.getAttr(camPath + ".aiApertureSize")
    return getValue

def GetEnableDOF():
    
    view = OpenMayaUI.M3dView.active3dView()
    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    
    getValue = cmds.getAttr(camPath + ".aiEnableDOF")
    return getValue
    

###________________________________________DUPLICATION_______________________________###
def DupLinear():
    
    AssetSel = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
    cmds.parent(AssetSel, world=True )
    cmds.FreezeTransformations()
    cmds.rename(AssetSel, "DuplicateAsset")
    # create a new MASH network
    mashNetwork = mapi.Network()
    mashNetwork.createNetwork(name = "ModIt_Duplicate", geometry="Instancer")

    if cmds.window("Duplicate", exists =True):
        cmds.deleteUI("Duplicate")        
            
    cmds.window("Duplicate", title='Duplicate Attribute', s= True, w= 500 )
    cmds.columnLayout(adj =True, w= 400)
    cmds.separator(h= 8, style = 'none')
    cmds.floatSliderGrp('Slider_Iteration', l = "Number",pre= 3, min =0, max =500 ,po =True, field =True, cc="Iteration()", dc="Iteration()", adj =0, cat= [1, "left", 3], cw= [1, 80])
    cmds.floatSliderGrp('Slider_IterationX', l = "Distance X",pre= 3, min =-500, max =500 ,po =True, field =True, cc="IterationX()", dc="IterationX()", adj =0, cat= [1, "left", 3], cw= [1, 80])
    cmds.floatSliderGrp('Slider_IterationY', l = "Distance Y",pre= 3, min =-500, max =500 ,po =True, field =True, cc="IterationY()", dc="IterationY()", adj =0, cat= [1, "left", 3], cw= [1, 80])
    cmds.floatSliderGrp('Slider_IterationZ', l = "Distance Z",pre= 3, min =-500, max =500 ,po =True, field =True, cc="IterationZ()", dc="IterationZ()", adj =0, cat= [1, "left", 3], cw= [1, 80])
    cmds.separator(h= 5, style = 'none')

    def UpdateInfo():
        IterationValue = GetIteration()
        IterationXValue = GetIterationX()
        IterationYValue = GetIterationY()
        IterationZValue = GetIterationZ()
        cmds.floatSliderGrp( "Slider_Iteration",e=True, value = IterationValue)
        cmds.floatSliderGrp( "Slider_IterationX",e=True, value = IterationXValue)
        cmds.floatSliderGrp( "Slider_IterationY",e=True, value = IterationYValue)
        cmds.floatSliderGrp( "Slider_IterationZ",e=True, value = IterationZValue)

    UpdateInfo()
    cmds.showWindow()
    cmds.scriptJob(uiDeleted=['Duplicate' , atClose])


def Iteration():
    myValueWidght = cmds.floatSliderGrp("Slider_Iteration", q= True, value=True)
    cmds.setAttr("ModIt_Duplicate_Distribute" + '.pointCount', myValueWidght)

def GetIteration():
    getValue = cmds.getAttr("ModIt_Duplicate_Distribute" + '.pointCount')
    return getValue

def IterationX():
    myValueWidght = cmds.floatSliderGrp("Slider_IterationX", q= True, value=True)
    cmds.setAttr("ModIt_Duplicate_Distribute" + '.amplitudeX', myValueWidght)

def GetIterationX():
    getValue = cmds.getAttr("ModIt_Duplicate_Distribute" + '.amplitudeX')
    return getValue

def IterationY():
    myValueWidght = cmds.floatSliderGrp("Slider_IterationY", q= True, value=True)
    cmds.setAttr("ModIt_Duplicate_Distribute" + '.amplitudeY', myValueWidght)

def GetIterationY():
    getValue = cmds.getAttr("ModIt_Duplicate_Distribute" + '.amplitudeY')
    return getValue

def IterationZ():
    myValueWidght = cmds.floatSliderGrp("Slider_IterationZ", q= True, value=True)
    cmds.setAttr("ModIt_Duplicate_Distribute" + '.amplitudeZ', myValueWidght)

def GetIterationZ():
    getValue = cmds.getAttr("ModIt_Duplicate_Distribute" + '.amplitudeZ')
    return getValue

def atClose():
    cmds.select("ModIt_Duplicate_Instancer")
    import maya.mel as mel    
    mel.eval('MASHBakeGUI;')
    cmds.select("ModIt_Duplicate_Instancer")
    try:
        import MASHbakeInstancer
    except ImportError:
        cmds.warning("Unable to import MASHbakeInstancer. Please ensure the MASH plugin is installed and enabled.")
    else:
        MASHbakeInstancer.MASHbakeInstancer(False)
    cmds.deleteUI("mashBakeStill", window=True )

    cmds.select("ModIt_Duplicate_Instancer_objects")
    cmds.SelectHierarchy("M_Chain_Instancer_objects")
    cmds.CenterPivot()
    cmds.delete(ch= True)
    cmds.showHidden(a= True)
    cmds.delete("DuplicateAsset")
    cmds.rename("ModIt_Duplicate_Instancer_objects", "Duplicate")
    cmds.delete("ModIt_Duplicate_Instancer")
    cmds.delete("ModIt_Duplicate")

def SmartDupli():
    cmds.duplicate(rr= True, st=True)




###________________________________________CHAIN_______________________________###

def Chain():
    
    if cmds.objExists('M_Chain'):
        cmds.window("Chain", title='Chain Attribute', s= True, w= 500 )
        cmds.columnLayout(adj =True, w= 400)
        cmds.separator(h= 8, style = 'none')
        cmds.floatSliderGrp('Slider_ChainNumver', l = "Number",pre= 3, min =0, max =200 ,po =True, field =True, cc="ChainNumber()", dc="ChainNumber()", adj =0, cat= [1, "left", 3], cw= [1, 80])
        cmds.separator(h= 5, style = 'none')

        def UpdateInfo():
            ChainIterationValue = GetChainNumber()

            cmds.floatSliderGrp( "Slider_ChainNumver",e=True, value = ChainIterationValue)

        UpdateInfo()
        cmds.showWindow()

    else:        
        selection1 = cmds.ls(sl = True, fl = True, dag = True, hd = 1)
        selection2 = cmds.ls(sl = True, fl = True, dag = True, tl= 1, shapes= True)
        
        cmds.select(selection1)
        
        # create a new MASH network
        mashNetwork = mapi.Network()
        mashNetwork.createNetwork(name = "M_Chain", geometry="Instancer")
        cmds.setAttr(mashNetwork.distribute + '.pointCount', 30)
        cmds.setAttr(mashNetwork.distribute + '.arrangement', 8)
        # create a world node
        curveNode = mashNetwork.addNode("MASH_Curve")
        cmds.connectAttr(selection2[0]+".worldSpace[0]", "M_Chain_Curve.inCurves[0]")
        cmds.setAttr("M_Chain_Curve.parametricLength", 1)

        if cmds.window("Chain", exists =True):
            cmds.deleteUI("Chain")        
                
        cmds.window("Chain", title='Chain Attribute', s= True, w= 500 )
        cmds.columnLayout(adj =True, w= 400)
        cmds.separator(h= 8, style = 'none')
        cmds.floatSliderGrp('Slider_ChainNumver', l = "Number",pre= 3, min =0, max =200 ,po =True, field =True, cc="ChainNumber()", dc="ChainNumber()", adj =0, cat= [1, "left", 3], cw= [1, 80])
        cmds.separator(h= 5, style = 'none')

        def UpdateInfo():
            ChainIterationValue = GetChainNumber()

            cmds.floatSliderGrp( "Slider_ChainNumver",e=True, value = ChainIterationValue)


        UpdateInfo()
        cmds.showWindow()



def ChainNumber():
    myValueWidght = cmds.floatSliderGrp("Slider_ChainNumver", q= True, value=True)
    cmds.setAttr("M_Chain_Distribute" + '.pointCount', myValueWidght)

def GetChainNumber():
    getValue = cmds.getAttr("M_Chain_Distribute" + '.pointCount')
    return getValue

def ChainBake():
    cmds.select("M_Chain_Instancer")
    import maya.mel as mel    
    mel.eval('MASHBakeGUI;')
    cmds.select("M_Chain_Instancer")
    try:
        import MASHbakeInstancer
    except ImportError:
        cmds.warning("Unable to import MASHbakeInstancer. Please ensure the MASH plugin is installed and enabled.")
    else:
        MASHbakeInstancer.MASHbakeInstancer(False)
    cmds.deleteUI("mashBakeStill", window=True )

    cmds.select("M_Chain_Instancer_objects")
    cmds.SelectHierarchy("M_Chain_Instancer_objects")
    cmds.CenterPivot()
    cmds.delete(ch= True)
    cmds.showHidden(a= True)
    cmds.delete("M_Chain_Instancer")
    cmds.rename("M_Chain_Instancer_objects", "Chain_Duplicate")
    cmds.delete("M_Chain")




def Bezier():
    cmds.CreateBezierCurveTool()
    
def EPCurve():
    cmds.EPCurveTool()
        
def Pencil():
    cmds.PencilCurveTool()    










###________________________________________SCREW AND BOLTS______________________________###
###_________SCREW1

def ScrewA():
    
    name = "Screw_A"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_A.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def ScrewB():
    
    name = "Screw_B"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_B.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def ScrewC():
    
    name = "Screw_C"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_C.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def ScrewD():
    
    name = "Screw_D"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_D.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def ScrewE():
    
    name = "Screw_E"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_E.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

    
def ScrewF():
    
    name = "Screw_F"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Screw_F.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")    


def BoltA():
    
    name = "Bolt_A"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_A.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def BoltB():
    
    name = "Bolt_B"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_B.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def BoltC():
    
    name = "Bolt_C"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_C.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")



def BoltD():
    
    name = "Bolt_D"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_D.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")



def BoltE():
    
    name = "Bolt_E"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_E.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def Washer():
    
    name = "Washer"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Washer.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def ChainA():
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Chain_A.ma"
    target = cmds.file(fileO, i= True)

    cmds.rename("Chain_A", "Chain_A_01")

def BoltG():
    
    name = "Bolt_G"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_G.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def BoltH():
    
    name = "Bolt_H"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_H.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")
    
def BoltI():
    
    name = "Bolt_I"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_I.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")
    
def BoltJ():
    
    name = "Bolt_J"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_J.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")
    
def BoltK():
    
    name = "Bolt_K"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_K.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")
    
def BoltL():
    
    name = "Bolt_L"
    # get current position of the move manipulator
    import maya.mel as mel
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    
    # get the current selection
    selection = cmds.ls(selection=True)
    
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/Bolt_L.ma"
    target = cmds.file(fileO, i= True)

    cmds.move(pos[0], pos[1], pos[2], name)

    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")    

def SF1():
    
    name = "SF_1"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_1.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF2():
    
    name = "SF_2"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_2.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF3():
    
    name = "SF_3"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_3.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF4():
    
    name = "SF_4"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_4.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF5():
    
    name = "SF_5"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_5.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF6():
    
    name = "SF_6"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_6.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF7():
    
    name = "SF_7"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_7.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF8():
    
    name = "SF_8"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_8.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF9():
    
    name = "SF_9"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_9.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF10():
    
    name = "SF_10"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_10.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF11():
    
    name = "SF_11"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_11.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF12():
    
    name = "SF_12"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_12.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")


def SF13():
    
    name = "SF_13"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_13.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF14():
    
    name = "SF_14"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_14.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF15():
    
    name = "SF_15"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_15.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF16():
    
    name = "SF_16"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_16.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF17():
    
    name = "SF_17"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_17.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def SF18():
    
    name = "SF_18"
    mel.eval("setToolTo $gMove;")
    pos = cmds.manipMoveContext('Move', query=True, position=True) 
    selection = cmds.ls(selection=True)
    fileO = cmds.internalVar(upd = True)+"scripts/ModIt_script/Mesh/SF_18.ma"
    target = cmds.file(fileO, i= True)
    cmds.move(pos[0], pos[1], pos[2], name)
    constr = cmds.normalConstraint(selection, name, aimVector = (0,1,0), worldUpType= 0)
    cmds.delete(constr)
    cmds.rename(name, name + "_01")

def DiscordLink():
    cmds.showHelp("https://discord.gg/2mkvw9r", absolute=True)

def WzxStoreLink():
    cmds.showHelp("http://www.wzxstore.com/", absolute=True)