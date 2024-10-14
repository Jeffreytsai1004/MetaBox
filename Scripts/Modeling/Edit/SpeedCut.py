#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import math
import maya.api.OpenMaya as OpenMaya
import maya.mel as mel
import re
from collections import OrderedDict
import random

def run():
    if cmds.window("jwSpeedCutWin", exists=True):
        cmds.deleteUI("jwSpeedCutWin")
    if cmds.dockControl('speedCutDock', q=1, ex=1):
        cmds.deleteUI('speedCutDock', control=1)

    mayaHSize = cmds.window('MayaWindow', q=1, h=1)
    jwSpeedCutWin = cmds.window("jwSpeedCutWin", title="Spped Cut", mxb=False, s=1, bgc=[0.2, 0.2, 0.2])
    cmds.tabLayout(tv=0)
    cmds.columnLayout(adj=1)
    cmds.rowColumnLayout(nc=4, cw=[(1, 180), (2, 30), (3, 30), (4, 30)])
    cmds.text(l='')
    cmds.button('SCminFrame', l="1", c=lambda *args: SCUI("min"), bgc=[0.24, 0.5, 0.2])
    cmds.button('SCmidFrame', l="2", c=lambda *args: SCUI("mid"), bgc=[0.2, 0.4, 0.5])
    cmds.button('SCmaxFrame', l="3", c=lambda *args: SCUI("max"), bgc=[0.45, 0.2, 0.5])
    cmds.setParent('..')
    cmds.scrollLayout('SCScrol', h=(mayaHSize * 0.95))
    cmds.columnLayout()
    cmds.frameLayout('meshSetupFrame', cll=1, cl=0, label="Mesh Setup", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=4, cw=[(1, 70), (2, 140), (3, 5), (4, 80)])
    cmds.text(l='Base Mesh')
    cmds.optionMenu('baseMeshMenu', bgc=[0.28, 0.28, 0.28], bsp=checkBaseMeshList, cc=lambda *args: (loadSymmetryState(), cageVisToggle(), showAllCutter(), updateVisLayer(), updateSnapState(), fadeOutCage(), rdMirrorUIUpdate()))
    cmds.menuItem("NoBaseMeshMenu", label='No Base Mesh')
    cmds.text(l='')
    cmds.button('setBaseButton', l="Set", c=lambda *args: (checkBaseMeshList(), setCutterBaseMesh(), baseMeshColorUpdate(), updateVisLayer()), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=9, cw=[(1, 70), (2, 5), (3, 30), (4, 5), (5, 30), (6, 5), (7, 65), (8, 5), (9, 80)])
    cmds.text(l='')
    cmds.text(l='')
    cmds.iconTextButton('meshLayerButton', h=20, w=30, c=lambda *args: toggleLayer(), style='iconOnly', image1='nodeGrapherModeAll.svg')
    cmds.text(l='')
    cmds.iconTextButton('meshColorUpdateButton', h=20, w=30, c=lambda *args: baseMeshColorUpdate(), style='iconOnly', image1='out_colorComposite_200.png')
    cmds.text(l='')
    cmds.button('reTargetButton', l="reTarget", c=lambda *args: reTarget(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('freeResultButton', l="Finalize", c=lambda *args: freeResultMesh(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout('cutterFrame', cll=1, cl=0, label="Cutter", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 58), (3, 5), (4, 58), (5, 5), (6, 58), (7, 5), (8, 58)])
    cmds.text(l='Show', h=20)
    cmds.iconTextButton(w=40, style='textOnly', l="Selected", rpt=True, c=lambda *args: hideUnSelectedCutters(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(w=40, style='textOnly', l="All", c=lambda *args: showAllCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(w=40, style='textOnly', l="None", c=lambda *args: hideAllCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='', h=20)
    cmds.iconTextButton(w=40, style='textOnly', l="Loop", rpt=True, c=lambda *args: showLastCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=5, cw=[(1, 40), (2, 50), (3, 5), (4, 110), (5, 85)])
    cmds.columnLayout()
    cmds.text(l=' Cutter', h=50)
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.separator(height=1, style='none')
    cmds.iconTextButton('newCutButton', h=23, w=50, style='textOnly', l="[ * ]", rpt=True, c=lambda *args: goPressCutter(4), bgc=[0.28, 0.28, 0.28])
    cmds.separator(height=3, style='none')
    cmds.iconTextButton('drawCutButton', h=23, w=50, style='textOnly', l="Draw", rpt=True, c=lambda *args: goDraw(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.intSliderGrp('cutterSideSlider', en=1, vis=0, v=4, min=3, max=6, s=1, cw3=[35, 40, 200], label="side  ", field=True)
    cmds.columnLayout()
    cmds.rowColumnLayout(nc=5, cw=[(1, 30), (2, 5), (3, 30), (4, 5), (5, 30)])
    cmds.iconTextButton('triButton', w=30, style='textOnly', l="3", rpt=True, c=lambda *args: goPressCutter(3), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton('pentaButton', w=30, style='textOnly', l="5", rpt=True, c=lambda *args: goPressCutter(5), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton('hexButton', w=30, style='textOnly', l="6", rpt=True, c=lambda *args: goPressCutter(6), bgc=[0.28, 0.28, 0.28])
    cmds.separator(height=1, style='none')
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.iconTextButton('selCutButton', w=100, style='textOnly', l="Selected", rpt=True, c=lambda *args: useOwnCutterShape(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.iconTextButton('dulCutButton', w=80, style='textOnly', l="Duplicate", rpt=True, c=lambda *args: cutterDulpicate(), bgc=[0.28, 0.28, 0.28])
    cmds.separator(height=4, style='none')
    cmds.iconTextButton('comCutButton', w=80, style='textOnly', l="Combine", rpt=True, c=lambda *args: combineSelCutters(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.floatSliderGrp('cutterScaleSlider', v=1, min=0.1, max=5, s=0.1, cw3=[40, 50, 190], label="Scale  ", field=True)
    cmds.floatField('cuterPreSize', value=1, vis=0)
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 58), (3, 5), (4, 58), (5, 5), (6, 58), (7, 5), (8, 58)])
    cmds.text(l='Opera', h=10)
    cmds.button('subsButton', l="Difference", c=lambda *args: cutterType("subs"), bgc=[0.3, 0.5, 0.6])
    cmds.text(l='')
    cmds.button('unionButton', l="Union", c=lambda *args: cutterType("union"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('cutButton', l="After Cut", c=lambda *args: cutterType("cut"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('cutToNewMeshButton', l="New Grp", c=lambda *args: cutter2NewMeshGrp(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='Mirror', h=10)
    cmds.button(w=50, l="X", c=lambda *args: cutterMirror("x"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(w=50, l="Y", c=lambda *args: cutterMirror("y"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(w=50, l="Z", c=lambda *args: cutterMirror("z"), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    ########################################################################################################################################################################
    cmds.frameLayout('controlFrame', cll=1, cl=0, label="Control", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='', h=20)
    cmds.button(w=50, l="Bevel", c=lambda *args: QBoxBevel(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(w=50, l="Smooth", c=lambda *args: QBoxSmooth(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(w=50, l="Remove", c=lambda *args: QBoxBevelRemove(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout()
    cmds.columnLayout()
    cmds.floatSliderGrp('fractionSlider', v=0.2, min=0.001, max=1, s=0.01, cw3=[55, 40, 180], label=" Fraction", field=True, cc=lambda *args: attributeFloatSlider("fraction"), dc=lambda *args: attributeFloatSlider("fraction"))
    cmds.intSliderGrp('segmentsSlider', v=1, min=1, max=10, fmx=20, s=1, cw3=[55, 40, 180], label="Segments", field=True, cc=lambda *args: attributeIntSlider("segments"), dc=lambda *args: attributeIntSlider("segments"))
    cmds.floatSliderGrp('depthSlider', v=1, min=-1, max=1, fmn=-3, fmx=3, s=1, cw3=[55, 40, 180], label="Depth", field=True, cc=lambda *args: attributeFloatSlider("depth"), dc=lambda *args: attributeFloatSlider("depth"))
    cmds.setParent('..')
    cmds.text(l='')
    cmds.separator(height=5, style='none')
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='', h=10)
    cmds.button('makePanelButton', w=50, l="Gap", c=lambda *args: makeGap(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('ScrapeButton', w=50, l="Scrape", c=lambda *args: scrapeCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('removePanelButton', w=50, l="Remove", c=lambda *args: removeGap(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout()
    cmds.columnLayout()
    cmds.floatSliderGrp('gapSlider', v=0.3, min=0.01, max=5, fmx=20, s=0.01, cw3=[55, 40, 180], label="Gap   ", field=True, cc=lambda *args: attributeGapSlider(), dc=lambda *args: attributeGapSlider())
    cmds.floatSliderGrp('scrapeSlider', v=0.3, min=0.01, max=1, fmx=5, s=0.01, cw3=[55, 40, 180], label="Scrape   ", field=True)
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    #######################################################################################################################################################################################
    cmds.frameLayout('meshSymmetryFrame', cll=1, cl=1, label="Mesh Symmetry", bgc=[0.14, 0.14, 0.14], w=300)
    buttonSize = 25
    cmds.rowColumnLayout(nc=10, cw=[(1, 70), (2, buttonSize), (3, buttonSize), (4, buttonSize), (5, buttonSize), (6, buttonSize), (7, buttonSize), (8, buttonSize), (9, buttonSize), (10, buttonSize)])
    cmds.text(l='      Direction')
    cmds.text(l='X')
    cmds.button('symmXButtonP', l="-", c=lambda *args: boolSymmetry("x", 1), bgc=[0.28, 0.28, 0.28])
    cmds.button('symmXButtonN', l="+", c=lambda *args: boolSymmetry("x", 2), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='Y')
    cmds.button('symmYButtonP', l="-", c=lambda *args: boolSymmetry("y", 1), bgc=[0.28, 0.28, 0.28])
    cmds.button('symmYButtonN', l="+", c=lambda *args: boolSymmetry("y", 2), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='Z')
    cmds.button('symmZButtonP', l="-", c=lambda *args: boolSymmetry("z", 1), bgc=[0.28, 0.28, 0.28])
    cmds.button('symmZButtonN', l="+", c=lambda *args: boolSymmetry("z", 2), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=6, cw=[(1, 80), (2, 104), (3, 6), (4, 104)])
    cmds.text(l='')
    cmds.button(l="Reset", c=lambda *args: boolSymmetryReset(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(l="Freeze", c=lambda *args: boolSymmetryFreeze(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=6, cw=[(1, 70), (2, 75), (3, 30), (4, 57), (5, 12), (6, 50)])
    cmds.text(l='      Cage')
    cmds.colorSliderGrp('CageColorSlider', l='', cw=[(1, 2), (2, 13)], rgb=(0.5, 0, 0), dc=lambda *args: updateCageColor())
    cmds.iconTextButton(en=1, w=30, style='iconOnly', image1='eye.png')
    cmds.floatSlider('CageTransparentSlider', min=0.1, max=1, value=0.5, step=0.1, dc=lambda *args: updateCageTransparent())
    cmds.text(l='')
    cmds.button(l='On/Off', w=35, bgc=[0.28, 0.28, 0.28], c=lambda *args: cageVisToggle())
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout('meshRadialMirrorFrame', cll=1, cl=1, label="Mesh Radial Mirror", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=9, cw=[(1, 70), (2, 40), (3, 40), (4, 40), (5, 5), (6, 60), (7, 20), (8, 20)])
    cmds.text(l='Axis')
    cmds.button('rMirrorXButton', l="X", c=lambda *args: rdMirror("x"), bgc=[0.28, 0.28, 0.28])
    cmds.button('rMirrorYButton', l="Y", c=lambda *args: rdMirror("y"), bgc=[0.28, 0.28, 0.28])
    cmds.button('rMirrorZButton', l="Z", c=lambda *args: rdMirror("z"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.text(l='Half')
    cmds.button('rMirrorNegButton', l="-", c=lambda *args: rdMirrorHalf("n"), bgc=[0.28, 0.28, 0.28])
    cmds.button('rMirrorPosButton', l="+", c=lambda *args: rdMirrorHalf("p"), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=3, cw=[(1, 240), (2, 15), (3, 40)])
    cmds.intSliderGrp('rMirrorSideSlider', v=1, min=3, max=15, fmx=20, s=1, cw3=[70, 40, 30], label="Side        ", field=True, cc=lambda *args: rdMirrorUpdate(), dc=lambda *args: rdMirrorUpdate())
    cmds.text(l='')
    cmds.text(l='')
    cmds.intSliderGrp('rMirrorOffsetSlider', v=10, min=-20, max=20, fmn=-200, fmx=200, s=1, cw3=[70, 40, 30], label="Offset        ", field=True, cc=lambda *args: rdMirrorOffsetUpdate(), dc=lambda *args: rdMirrorOffsetUpdate())
    cmds.text(l='')
    cmds.button(l="Done", c=lambda *args: rdMirrorOutput(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    ########################################################################################################################################################################
    cmds.frameLayout('alignmentFrame', cll=1, cl=1, label="Alignment", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 50), (3, 5), (4, 50), (5, 5), (6, 50), (7, 10), (8, 80)])
    cmds.text(l='Rotate', h=20)
    cmds.iconTextButton(style='textOnly', l="X", rpt=True, c=lambda *args: QChangeCutterDir("X"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(style='textOnly', l="Y", rpt=True, c=lambda *args: QChangeCutterDir("Y"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(style='textOnly', l="Z", rpt=True, c=lambda *args: QChangeCutterDir("Z"), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=4, cw=[(1, 40), (2, 200), (3, 5), (4, 170), (5, 50)])
    cmds.text(l='Border', h=20)
    cmds.intSliderGrp('bboxDivSlider', v=2, min=1, max=10, fmx=20, s=1, cw3=[10, 40, 170], label="", field=True, dc=lambda *args: borderAlginBBoxDivUpdate())
    cmds.button('borderAlginButton', l='On/Off', w=50, bgc=[0.28, 0.28, 0.28], c=lambda *args: borderAlginBBoxToggle())
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 50), (3, 5), (4, 50), (5, 5), (6, 50), (7, 10), (8, 80)])
    cmds.text(l='Axis', h=20)
    cmds.button('toggleAxisX', l="X", c=lambda *args: toggleAxisButton("X"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('toggleAxisY', l="Y", c=lambda *args: toggleAxisButton("Y"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('toggleAxisZ', l="Z", c=lambda *args: toggleAxisButton("Z"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='', h=20)
    cmds.button('toggleAxisXYZ', l="XYZ", c=lambda *args: toggleAxisButton("XYZ"), bgc=[0.3, 0.5, 0.6])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='Snap')
    cmds.iconTextButton(w=50, style='textOnly', l="Border", rpt=True, c=lambda *args: alignCutterToBase(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(w=50, style='textOnly', l="Last Cutter", rpt=True, c=lambda *args: alignLastCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(w=50, style='textOnly', l="Select Cutter", rpt=True, c=lambda *args: alignSelCutter(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='Even', h=20)
    cmds.iconTextButton(w=50, style='textOnly', l="left / right", rpt=True, c=lambda *args: evenObjLineUp("x"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton(w=50, style='textOnly', l="up/ down", rpt=True, c=lambda *args: evenObjLineUp("y"), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    ########################################################################################################################################################################
    cmds.frameLayout('patternFrame', cll=1, cl=1, label="Pattern", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 50), (3, 5), (4, 50), (5, 5), (6, 50), (7, 10), (8, 80)])
    cmds.text(l='Type', h=20)
    cmds.button('arrayLinear', l="Linear", c=lambda *args: toggleArrayType(), bgc=[0.3, 0.5, 0.6])
    cmds.text(l='')
    cmds.button('arrayRadial', l="Radial", c=lambda *args: toggleArrayType(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.text(l='')
    cmds.text(l='')
    cmds.button(l="Freeze", c=lambda *args: instBake(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=8, cw=[(1, 40), (2, 50), (3, 5), (4, 50), (5, 5), (6, 50), (7, 10), (8, 80)])
    cmds.text(l='Axis', h=20)
    cmds.button('arrayAxisX', l="X", c=lambda *args: arrayPattrn("X"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('arrayAxisY', l="Y", c=lambda *args: arrayPattrn("Y"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('arrayAxisZ', l="Z", c=lambda *args: arrayPattrn("Z"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button(l="Remove", c=lambda *args: removeArrayGrp(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.rowColumnLayout()
    cmds.columnLayout()
    cmds.intSliderGrp('instNumSlider', v=1, min=1, max=10, fmx=20, s=1, cw3=[55, 40, 180], label="Number", field=True, cc=lambda *args: instReNew(), dc=lambda *args: instReNew())
    cmds.floatSliderGrp('disSlider', v=1, min=-3, max=3, fmx=20, fmn=-20, s=0.01, cw3=[55, 40, 180], label="Distance", field=True, cc=lambda *args: instDistanceUpdate(), dc=lambda *args: instDistanceUpdate())
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    ##########################################################################################################################################################################
    cmds.frameLayout('liveDrawFrame', cll=1, cl=1, label="Live Draw", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=7, cw=[(1, 40), (2, 78), (3, 5), (4, 78), (5, 5), (6, 78)])
    cmds.text(l='Grid')
    cmds.iconTextButton('snapGridCameraVisButton', w=50, style='textOnly', l="Camera", c=lambda *args: snapGridCamera(), rpt=True, bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton('snapGridPointVisButton', w=50, style='textOnly', l="Point", c=lambda *args: goPressDraw(), rpt=True, bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.iconTextButton('snapGridVisToggleButton', w=50, style='textOnly', l="Remove", c=lambda *args: drawGirdOff(), rpt=True, bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.columnLayout()
    cmds.intSliderGrp('snapGirdSize', v=10, min=1, max=50, fmx=100, s=1, cw3=[35, 40, 200], label="Grid  ", field=True, dc=lambda *args: resizeSnapGrid())
    cmds.intSliderGrp('snapGirdRot', v=0, min=0, max=90, s=1, cw3=[35, 40, 200], label="Rot   ", field=True, dc=lambda *args: rotateSnapGrid())
    cmds.floatSliderGrp('snapGirdOffset', v=0.1, min=0.01, max=3, fmx=20, s=0.01, cw3=[35, 40, 200], label="Offset", field=True, dc=lambda *args: offsetSnapGrid())
    cmds.setParent('..')
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 78), (3, 5), (4, 78), (5, 5), (6, 78)])
    cmds.text(l='Tools')
    cmds.button('cureveDrawButtton', w=50, l="Draw Curve", c=lambda *args: drawCurveNow(), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('buildBlockButton', w=50, l="Make Block", c=lambda *args: makeDrawBlock(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    ##########################################################################################################################################################################
    cmds.frameLayout('bakeFrame', cll=1, cl=1, label="Bake", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=6, cw=[(1, 40), (2, 80), (3, 5), (4, 80), (5, 5), (6, 80)])
    cmds.text(l='', h=10)
    cmds.button('bakeUnSelButton', w=50, l="Unselect", c=lambda *args: bakeCutter("unselect"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('bakeAllButton', w=50, l="All", c=lambda *args: bakeCutter("all"), bgc=[0.28, 0.28, 0.28])
    cmds.text(l='')
    cmds.button('bakeRestoreButton', w=50, l="Restore", c=lambda *args: restoreCutterWithSymmtry(), bgc=[0.28, 0.28, 0.28])
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.frameLayout('meshBevelManagerFrame', cll=1, cl=1, label="Mesh Bevel Manager", bgc=[0.14, 0.14, 0.14], w=300)
    cmds.rowColumnLayout(nc=4, cw=[(1, 80), (2, 185), (3, 5), (4, 58)])
    cmds.text(l='', h=20)
    cmds.iconTextButton('preBevelButton', w=40, style='textOnly', l="Bevel Manager", rpt=True, c=lambda *args: jwSpeedCutBevelMangerSetup(), bgc=[0.14, 0.14, 0.14])
    cmds.separator(height=15, style='none')
    cmds.setParent('..')
    cmds.separator(height=15, style='none')
    cmds.showWindow(jwSpeedCutWin)
    cmds.window("jwSpeedCutWin", e=True, w=320, h=1250)
    cmds.commandEcho(state=False)
    cmds.scriptEditorInfo(suppressWarnings=0, suppressInfo=0, se=0)
    checkBaseMeshList()
    allowedAreas = ['right', 'left']
    cmds.dockControl('speedCutDock', l='Speed Cut', area='right', content='jwSpeedCutWin', allowedArea=allowedAreas, fcc=lambda *args: floatSCUIsize())
    #start with floating UI
    #cmds.dockControl('speedCutDock', l='speedCut 1.69', area='right', content = 'jwSpeedCutWin',  allowedArea= allowedAreas, fcc =lambda: floatSCUIsize(),fl=1)

def SCUI(state):
    frameList = {'meshSetupFrame','meshSymmetryFrame','meshRadialMirrorFrame','cutterFrame','controlFrame','alignmentFrame','patternFrame','bakeFrame','liveDrawFrame','meshBevelManagerFrame'}
    midList = {'meshSetupFrame','cutterFrame','controlFrame'}
    otherList = list(set(frameList) - set(midList))
    if state == 'min':
        for f in frameList:
            cmds.frameLayout(f, e=1, cl= 1)
    elif state == 'mid':
        for m in midList:
            cmds.frameLayout(m, e=1, cl= 0)
        for o in otherList:
            cmds.frameLayout(o, e=1, cl= 1)
    elif state == 'max':
        for f in frameList:
            cmds.frameLayout(f, e=1, cl= 0)

def floatSCUIsize():
    SCUI('mid')
    checkState = cmds.dockControl('speedCutDock', q=1, fl=1)
    mayaHSize = cmds.window('MayaWindow', q=1, h=1)
    if checkState == 0:
        cmds.scrollLayout('SCScrol', e=1, h=(mayaHSize * 0.95))
    else:
        cmds.scrollLayout('SCScrol', e=1, h=570)
        cmds.dockControl('speedCutDock', e=1, h=570)

def cutter2NewMeshGrp():
    selCut = cmds.ls(sl=1,l=1)
    if len(selCut) == 1:
        myType = checkInstType()
        if myType[1] != 'new':
            instBake()
            selCut = cmds.ls(sl=1,l=1)
        getOPType = cmds.getAttr(selCut[0]+'.cutterOp')
        if getOPType != 'union':
            #create new box shape by adding all union cutter and base mesh
            meshNameGrp = selCut[0].split('|')[1]
            meshName = meshNameGrp.replace('BoolGrp','')
            liveCutterList = cmds.ls('|'+ meshNameGrp + '|' + meshName + '_cutterGrp|boxCutter*',l=True)
            bakeCutterList = cmds.ls('|'+ meshNameGrp + '|' + meshName + '_bakeStep|bakeCutter*',l=True)
            totalList =   liveCutterList +  bakeCutterList
            collectUnionShape =[]
            for t in totalList:
                checkType = cmds.getAttr(t+'.cutterOp')
                if checkType == 'union':
                    collectUnionShape.append(t)
            if cmds.objExists('|'+ meshNameGrp + '|' + meshName + '_bakeStep|' + meshName + '_bakeBaseMesh'):
                collectUnionShape.append('|'+ meshNameGrp + '|' + meshName + '_bakeStep|' + meshName + '_bakeBaseMesh')
            else:
                collectUnionShape.append('|'+ meshNameGrp + '|' + meshName)
            dulMesh = cmds.duplicate(collectUnionShape, rr = True, un=True)
            cmds.parent(dulMesh,w=1)
            selList = cmds.ls(sl=1,fl=1,transforms=1,l=1)
            while len(selList) > 1:
                cmds.polyCBoolOp(selList[0], selList[1], op=1, ch=1, preserveColor=0, classification=1, name=selList[0])
                cmds.DeleteHistory()
                if cmds.objExists(selList[1]):
                    cmds.delete(selList[1])
                cmds.rename(selList[0])
                selList.remove(selList[1])
            combineShape = cmds.ls(sl=1)
            checkNumber = ''.join([n for n in selCut[0].split('|')[-1] if n.isdigit()])
            cmds.rename(meshName + "bc" + str(checkNumber))
            shadowMesh = cmds.ls(sl=1)
            checkBaseMeshList()
            cmds.select(shadowMesh)
            setCutterBaseMesh()
            updateVisLayer()
            cutterShapeNode = cmds.listRelatives(selCut[0], s=True, f=True )
            preCutShapeNode = cmds.listRelatives(shadowMesh[0], s=True, f=True  )
            dulCombineMesh = cmds.duplicate(preCutShapeNode, rr = True, un=True)
            cmds.rename(dulCombineMesh, shadowMesh[0]+'_myInterMesh')
            interMeshShapeNode = cmds.listRelatives(shadowMesh[0]+'_myInterMesh', s=True, f=True  )
            cmds.createNode('polyCBoolOp')
            cmds.rename(shadowMesh[0]+'_myInter')
            cmds.connectAttr((interMeshShapeNode[0]+'.outMesh'), (shadowMesh[0]+'_myInter.inputPoly[0]'),f=True)
            cmds.connectAttr((interMeshShapeNode[0]+'.worldMatrix[0]'), (shadowMesh[0]+'_myInter.inputMat[0]'),f=True)
            cmds.connectAttr((cutterShapeNode[0]+'.outMesh'), (shadowMesh[0]+'_myInter.inputPoly[1]'),f=True)
            cmds.connectAttr((cutterShapeNode[0]+'.worldMatrix[0]'), (shadowMesh[0]+'_myInter.inputMat[1]'),f=True)
            cmds.setAttr((shadowMesh[0]+'_myInter.operation'),3)
            cmds.connectAttr((shadowMesh[0]+'_myInter.output'), (preCutShapeNode[0]+'.inMesh'),f=True)
            cmds.select(selCut)
            cmds.sets(name = (shadowMesh[0] + 'Shadow'), text= (shadowMesh[0] + 'Shadow'))
            showAllCutter()
            baseMeshColorUpdate()
            cmds.setAttr((shadowMesh[0]+".translate"),0,0,0)
            cmds.setAttr((shadowMesh[0]+".rotate"),0,0,0)
            cmds.setAttr((shadowMesh[0]+".scale"),1,1,1)
        else:
            print('only work for different or after cut')
    else:
        print ('select one cutter Only!')

def fixShadowLink():
    listAllShadow = cmds.ls('*Shadow')
    for l in listAllShadow:
        checkNodeType = cmds.nodeType(l)
        if checkNodeType == 'objectSet':
            shadowName = cmds.sets(l,q=1)
            targetName = l.replace('Shadow','')
            if cmds.objExists((targetName +'BoolGrp')) == 0:
                cmds.delete(l)
            else:
                cutterShapeNode = cmds.listRelatives(shadowName[0], s=True, f=True )
                preCutShapeNode = cmds.listRelatives(targetName, s=True, f=True )
                shapes = cmds.listRelatives((targetName+'_bool'), shapes=True)
                shadeEng = cmds.listConnections(shapes , type = 'shadingEngine')
                materials = cmds.ls(cmds.listConnections(shadeEng ), materials = True)
                if cmds.objExists((targetName +'_myInter')) == 0:
                    cmds.createNode('polyCBoolOp')
                    cmds.rename(targetName+'_myInter')
                    cmds.connectAttr((preCutShapeNode[0]+'.outMesh'), (targetName+'_myInter.inputPoly[0]'),f=True)
                    cmds.connectAttr((preCutShapeNode[0]+'.worldMatrix[0]'), (targetName+'_myInter.inputMat[0]'),f=True)
                    cmds.connectAttr((cutterShapeNode[0]+'.outMesh'), (targetName+'_myInter.inputPoly[1]'),f=True)
                    cmds.connectAttr((cutterShapeNode[0]+'.worldMatrix[0]'), (targetName+'_myInter.inputMat[1]'),f=True)
                    cmds.setAttr((targetName+'_myInter.operation'),2)
                    cmds.connectAttr((targetName+'_myInter.output'), (targetName+'_preSubBoxShape.inMesh'),f=True)
                else:
                    cmds.connectAttr((cutterShapeNode[0]+'.outMesh'), (targetName+'_myInter.inputPoly[1]'),f=True)
                    cmds.connectAttr((cutterShapeNode[0]+'.worldMatrix[0]'), (targetName+'_myInter.inputMat[1]'),f=True)
                    cmds.connectAttr((targetName+'_myInter.output'), (targetName+'_preSubBoxShape.inMesh'),f=True)

                if cmds.objExists(targetName+'_ShaderSG'):
                    cmds.sets((targetName+'_bool'), e=True, forceElement = (targetName+'_ShaderSG'))

###################################################################################################################################################
def deSelect():
    obj_shape = cmds.listRelatives(parent=True, f=True)
    obj = cmds.listRelatives(obj_shape,parent=True, f=True)
    cmds.select(obj)
    cmds.selectMode(leaf=True)
    cmd = "changeSelectMode -object;"
    mel.eval(cmd)
    cmds.select(clear=True)

def instDistanceUpdate():
    myType = checkInstType()
    if myType[1] != 'new':
        checkMaster = myType[0]
        checkDis =  cmds.floatSliderGrp('disSlider',q=True, v = True  )
        checkState = cmds.attributeQuery('arrayOffset',node = checkMaster,ex=True)
        if checkState == 1:
            cmds.setAttr((checkMaster+'.arrayOffset'),checkDis)

def instReNew():
    myType = checkInstType()
    if myType[1] != 'new':
        instRemove()
        checkMaster = myType[0]
        currentDir = cmds.getAttr(checkMaster+'.arrayDirection')

        if myType[1] == 'linear':
            instLinearAdd(currentDir)
        else:
            instRadAdd(currentDir)

def instTypeToggle():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    currentSel =cmds.ls(sl=1,fl=1)
    if len(currentSel) == 1:
        #case one Linear to Radial
        myType = checkInstType()
        if myType[1] != 'new':
            getNumber = cmds.getAttr(myType[0]+'.arrayNumber')
            getDis = cmds.getAttr(myType[0]+'.arrayOffset')
            getDir = cmds.getAttr(myType[0]+'.arrayDirection')
            cmds.intSliderGrp('instNumSlider', e=True,  v = getNumber)
            cmds.floatSliderGrp('disSlider',e=True, v = getDis)
            if myType[1] == 'linear':
                instRemove()
                instRadAdd(getDir)

            elif myType[1] == 'radial':
                removeRadArray()
                instLinearAdd(getDir)

def instLinearAdd(direction):
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        selCutterCheck = cmds.ls(sl=1, fl=1, l=1, type='transform')
        if 'boxCutter' in selCutterCheck[0]:
            cmds.button('arrayLinear',e=True, bgc = [0.3, 0.5, 0.6] )
            cmds.button('arrayRadial',e=True, bgc = [0.28,0.28,0.28])
            myType = checkInstType()
            instRemove()
            dir = direction
            arraySample = cmds.ls(sl=1,fl=1)
            sourcePivot = cmds.xform(arraySample[0], q=1, ws=1 ,rp=1)
            if 'boxCutter' in arraySample[0] and len(arraySample)==1:
                bbox= cmds.xform(arraySample[0], q=1, ws=1, bb=1)
                myLength = []
                if dir == 'X':
                    myLength=math.sqrt((math.pow(bbox[0]-bbox[3],2)))
                if dir == 'Y':
                    myLength=math.sqrt((math.pow(bbox[1]-bbox[4],2)))
                if dir == 'Z':
                    myLength=math.sqrt((math.pow(bbox[2]-bbox[5],2)))

                getIntNumber = []
                getDist = []

                if myType[1] == 'new':
                    getIntNumber = 2
                    getDist = 1.5
                    cmds.intSliderGrp('instNumSlider', e=True,  v = 2)
                    cmds.floatSliderGrp('disSlider',e=True, v = 1.5)
                else:
                    getIntNumber = cmds.intSliderGrp('instNumSlider', q=True,  v = True)
                    checkState = cmds.attributeQuery('arrayOffset',node = myType[0],ex=True)
                    if checkState == 1:
                        getDist = cmds.getAttr(myType[0]+'.arrayOffset')
                        cmds.floatSliderGrp('disSlider',e=True, v = getDist)
                #create Attr
                if not cmds.attributeQuery('arrayNumber', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayNumber')

                if not cmds.attributeQuery('arrayDirection', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayDirection' ,dt= 'string')

                if not cmds.attributeQuery('arrayType', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayType',dt= 'string')

                if not cmds.attributeQuery('arrayLength', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayLength')

                if not cmds.attributeQuery('arrayOffset', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayOffset')

                if not cmds.attributeQuery('arrayMaster', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayMaster'  ,dt= 'string')
                    cmds.setAttr((arraySample[0]+'.arrayOffset'),1)

                cmds.setAttr((arraySample[0]+'.arrayNumber'),getIntNumber)
                cmds.setAttr((arraySample[0]+'.arrayDirection'),dir,type="string")
                cmds.setAttr((arraySample[0]+'.arrayType'),'linear',type="string")
                cmds.setAttr((arraySample[0]+'.arrayLength'),myLength)
                cmds.setAttr((arraySample[0]+'.arrayMaster'),arraySample[0],type="string")

                dirA = (arraySample[0]+'.translate'+dir)
                collections=[]

                for i in range(getIntNumber-1):
                    newIns = cmds.instance(arraySample[0])
                    collections.append(newIns[0])
                    if not cmds.attributeQuery('arrayOrder', node = newIns[0], ex=True ):
                        cmds.addAttr(newIns[0], ln='arrayOrder')
                    cmds.setAttr((newIns[0]+'.arrayOrder'),(i+1))
                    cmds.setAttr((arraySample[0] + '.arrayOffset'),getDist)
                    cmdTextA = (newIns[0] + '.translate' + dir + '= ' + arraySample[0] + '.arrayLength *' + arraySample[0] + '.arrayOffset *' +  newIns[0] + '.arrayOrder +'+ dirA +';')
                    cmds.expression( s = cmdTextA, o = newIns[0], ae = True, uc = all)
                    attrList = {'translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'}
                    attrList.remove(('translate' + str(dir)))
                    for a in attrList:
                        cmds.connectAttr((arraySample[0]+'.' + a), (newIns[0] + '.' + a),f=True)
                parent = cmds.listRelatives(arraySample[0], p=True )
                if not 'ArrayGrp' in parent[0]:
                    cmds.group(arraySample[0],collections)
                    cmds.rename(arraySample[0]+'ArrayGrp')

                cmds.xform((arraySample[0]+'ArrayGrp') ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))
                cmds.setAttr( (arraySample[0]+".arrayNumber"),getIntNumber)
                cmds.setAttr( (arraySample[0]+".arrayOffset"),getDist)
                cmds.select((arraySample[0]+'ArrayGrp'))
                fixBoolNodeConnection()

def toggleArrayType():
    #toggle existing pattern
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    currentSel =cmds.ls(sl=1,fl=1)
    checkState = cmds.button('arrayLinear', q=True , bgc =True )
    if len(currentSel) == 1:
        myType = checkInstType()
        if myType[1] != 'new':
            getNumber = cmds.getAttr(myType[0]+'.arrayNumber')
            getDis = cmds.getAttr(myType[0]+'.arrayOffset')
            getDir = cmds.getAttr(myType[0]+'.arrayDirection')
            getGap = cmds.getAttr(myType[0]+'.panelGap')
            cmds.intSliderGrp('instNumSlider', e=True,  v = getNumber)
            cmds.floatSliderGrp('disSlider',e=True, v = getDis)
            cmds.floatSliderGrp('gapSlider',e=True, v = getGap)
            if (checkState[0] < 0.285):
                removeRadArray()
                instLinearAdd(getDir)

            else:
                instRemove()
                instRadAdd(getDir)


    if (checkState[0] < 0.285):
        cmds.button('arrayRadial' ,e=True, bgc = [0.28,0.28,0.28])
        cmds.button('arrayLinear', e=True, bgc = [0.3, 0.5, 0.6] )
    else:
        cmds.button('arrayRadial' ,e=True, bgc = [0.3, 0.5, 0.6] )
        cmds.button('arrayLinear', e=True, bgc = [0.28,0.28,0.28])

def arrayPattrn(dir):
    checkState = cmds.button('arrayLinear', q=True , bgc =True )
    if (checkState[0] > 0.285):#Linear
        instLinearAdd(dir)
    else:
        instRadAdd(dir)

def checkInstType():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    arraySample = []
    checkGrp = cmds.ls(sl=1,fl=1,l=1)
    if 'ArrayGrp' in checkGrp[0]:
        cmds.connectControl('disSlider', (''))
        allChild = cmds.listRelatives(checkGrp[0], ad=True)
        getShapeNode = cmds.ls(allChild,type ='shape')
        listTransNode = cmds.listRelatives(getShapeNode,  p=True )
        arraySample = listTransNode
        checkMaster = cmds.getAttr(arraySample[0]+'.arrayMaster')
        checkMasterType = cmds.getAttr(arraySample[0]+'.arrayType')
        cmds.floatSliderGrp('disSlider',e=True, en= True )
        cmds.intSliderGrp('instNumSlider',e=True, en= True )
        return (checkMaster,checkMasterType)
    else:
        if cmds.attributeQuery('arrayMaster', node = checkGrp[0], ex=True ):
            checkMaster = cmds.getAttr(checkGrp[0]+'.arrayMaster')
            checkMasterType = cmds.getAttr(checkGrp[0]+'.arrayType')
            if checkMasterType != None:
                return (checkMaster,checkMasterType)
        else:
            return ('new','new')

def removeArrayGrp():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selCutterCheck = cmds.ls(sl=1, fl=1, l=1, type='transform')
    if len(selCutterCheck) == 1 and 'boxCutter' in selCutterCheck[0] and 'ArrayGrp' in selCutterCheck[0]:
        myType = checkInstType()
        cmds.select(myType[0])
        if myType[1] == 'radial':
            removeRadArray()
        elif myType[1] == 'linear':
            instRemove()
            cmds.parent(myType[0],(beseMesh +'_cutterGrp'))
            cmds.delete(myType[0]+'ArrayGrp')
        cmds.setAttr((myType[0]+'.arrayType'),'new',type="string")
        cmds.setAttr((myType[0]+'.arrayMaster'),'new',type="string")

def instRadReNew():
    cmds.radioButtonGrp('arrayTypeButton',e=True, sl = 2)
    myType = checkInstType()
    if myType[1] != 'radial':#lin
        instLink()
    removeRadArray()
    checkMaster = myType[0]
    if cmds.attributeQuery('arrayDirection', node = checkMaster, ex=True ):
        currentDir = cmds.getAttr(checkMaster+'.arrayDirection')
        instRadAdd(currentDir)
    fixBoolNodeConnection()
    instLink()

def instRadAdd(direction):
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selCutterCheck = cmds.ls(sl=1, fl=1, l=1, type='transform')
    if len(beseMesh) > 0:
        if 'boxCutter' in selCutterCheck[0] :
            cmds.button('arrayLinear',e=True, bgc = [0.28,0.28,0.28])
            cmds.button('arrayRadial',e=True, bgc = [0.3, 0.5, 0.6])
            myType = checkInstType()
            removeArrayGrp()
            arraySample = cmds.ls(sl=1,fl=1)
            dir = direction
            getIntNumber = []
            getDist = []

            if myType[1] == 'new':
                getIntNumber = 3
                getDist = 1
                cmds.intSliderGrp('instNumSlider', e=True,  v = 3)
                cmds.floatSliderGrp('disSlider',e=True, v = 1)
            else:
                getIntNumber = cmds.intSliderGrp('instNumSlider', q=True,  v = True)
                checkState = cmds.attributeQuery('arrayOffset',node = myType[0],ex=True)
                if checkState == 1:
                    getDist = cmds.getAttr(myType[0]+'.arrayOffset')
                    cmds.floatSliderGrp('disSlider',e=True, v = getDist)
            collection =[]

            #create Attr
            if not cmds.attributeQuery('arrayNumber', node = arraySample[0], ex=True ):
                cmds.addAttr(arraySample[0], ln='arrayNumber')

            if not cmds.attributeQuery('arrayDirection', node = arraySample[0], ex=True ):
                cmds.addAttr(arraySample[0], ln='arrayDirection' ,dt= 'string')

            if not cmds.attributeQuery('arrayType', node = arraySample[0], ex=True ):
                cmds.addAttr(arraySample[0], ln='arrayType',dt= 'string')

            if not cmds.attributeQuery('arrayOffset', node = arraySample[0], ex=True ):
                cmds.addAttr(arraySample[0], ln='arrayOffset')

            if not cmds.attributeQuery('arrayMaster', node = arraySample[0], ex=True ):
                cmds.addAttr(arraySample[0], ln='arrayMaster'  ,dt= 'string')
                cmds.setAttr((arraySample[0]+'.arrayOffset'),1)
            if not cmds.attributeQuery('arrayLength', node = arraySample[0], ex=True ):
                    cmds.addAttr(arraySample[0], ln='arrayLength')

            cmds.setAttr((arraySample[0]+'.arrayNumber'),getIntNumber)
            cmds.setAttr((arraySample[0]+'.arrayOffset'),getDist)
            cmds.setAttr((arraySample[0]+'.arrayDirection'),dir,type="string")
            cmds.setAttr((arraySample[0]+'.arrayType'),'radial',type="string")
            cmds.setAttr((arraySample[0]+'.arrayMaster'),arraySample[0],type="string")

            bbox= cmds.xform(arraySample[0], q=1, ws=1, bb=1)
            length=math.sqrt((math.pow(bbox[0]-bbox[3],2)+math.pow(bbox[1]-bbox[4],2)+math.pow(bbox[2]-bbox[5],2))/3)
            cmds.setAttr((arraySample[0]+'.arrayLength'),length)

            sourcePivot = cmds.xform(arraySample[0], q=1, ws=1 ,rp=1)

            rAngle = 360.0 / getIntNumber
            #inst
            collection = []
            for i in range(getIntNumber-1):
                cmds.select(arraySample[0])
                cmds.instance()
                newNode = cmds.ls(sl=True)
                cmds.select(newNode)
                cmds.group()
                cmds.rename(newNode[0]+'_Trans')
                cmds.group()
                cmds.rename(newNode[0]+'_Rot')
                collection.append(newNode[0]+'_Rot')
                cmds.xform((newNode[0]+'_Rot') ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))
                if dir == 'X':
                    cmds.rotate((rAngle*(i)+rAngle), 0 ,0, r=True, ws=True, fo=True)
                elif dir == 'Y':
                    cmds.rotate(0,(rAngle*(i)+rAngle),0, r=True, ws=True, fo=True)
                else:
                    cmds.rotate(0,0,(rAngle*(i)+rAngle), r=True, ws=True, fo=True)
            # group master
            cmds.select(arraySample[0])
            cmds.group()
            cmds.rename(arraySample[0]+'_Trans')
            cmds.group()
            cmds.rename(arraySample[0]+'_Rot')
            collection.append(arraySample[0]+'_Rot')
            cmds.xform((arraySample[0]+'_Rot') ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))

            cmds.select(collection)
            cmds.group()
            cmds.rename(arraySample[0]+'ArrayGrp')
            OffsetDir =[]

            if dir == 'X':
                OffsetDir = 'Y'
            elif dir == 'Y':
               OffsetDir = 'X'
            else:
              OffsetDir = 'X'

            for c in collection:
                cutterName = c.replace('_Rot', '')
                cmdTextA = (cutterName + '_Trans.translate' + OffsetDir + '= ' + arraySample[0] + '.arrayLength *' + arraySample[0] + '.arrayOffset;')
                cmds.expression( s = cmdTextA, o = (arraySample[0] + '_Trans.translate'), ae = True, uc = all)
                cmds.select((arraySample[0]+'ArrayGrp'))
                cmds.xform((arraySample[0]+'ArrayGrp') ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))
                attrList = {'translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'}
                if cutterName != arraySample[0]:
                    for a in attrList:
                        cmds.connectAttr((arraySample[0]+'.' + a), (cutterName + '.' + a),f=True)

            cmds.setAttr( (arraySample[0]+".arrayNumber"),getIntNumber)
            cmds.setAttr( (arraySample[0]+".arrayOffset"),getDist)
            fixBoolNodeConnection()

def removeRadArray():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    boolNode = cmds.listConnections(cmds.listHistory((beseMesh +'_bool'),f=1),type='polyCBoolOp')
    myType = checkInstType()
    if myType[1] == 'radial':
        arraySample = myType[0]
        if cmds.objExists(arraySample+'_Rot*'):
            cmds.select(arraySample+'_Rot*')
            listRArray = cmds.ls(sl=1,fl=1)
            cmds.delete(listRArray[1:len(listRArray)])
            cmds.parent(arraySample,beseMesh+'_cutterGrp')
            sourcePivot = cmds.xform((arraySample+'_Rot'), q=1, ws=1 ,rp=1)
            cmds.select(arraySample)
            cmds.move( sourcePivot[0],sourcePivot[1],sourcePivot[2],rpr=True)
            if cmds.objExists(arraySample+'ArrayGrp'):
                cmds.delete(arraySample+'ArrayGrp')
        if cmds.objExists(arraySample+'ArrayGrp'):
            cmds.delete(arraySample+'ArrayGrp')

        shapeNode = cmds.listRelatives(arraySample, s=True )
        listConnect = cmds.connectionInfo((shapeNode[0]+'.outMesh'), dfs=True )
        if len(listConnect)>0:
            for a in listConnect:
                cmds.disconnectAttr((shapeNode[0]+'.outMesh'), a)
        checkNumber = ''.join([n for n in arraySample.split('|')[-1] if n.isdigit()])
        cmds.connectAttr( (shapeNode[0]+".outMesh"), ((boolNode[0]+'.inputPoly['+str(checkNumber)+']')),f=True)
        cmds.connectAttr( (shapeNode[0]+".worldMatrix[0]"), ((boolNode[0]+'.inputMat['+str(checkNumber)+']')),f=True)
        cmds.select(arraySample)

def instBake():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkSel = cmds.ls(sl=True)
    if len(checkSel) > 0:
        myType = checkInstType()
        if myType[1] != 'new':
            opType = cmds.getAttr(myType[0]+'.cutterOp')
            arraySample = myType[0]
            sourcePivot = cmds.xform((arraySample+'ArrayGrp'), q=1, ws=1 ,rp=1)
            cmds.select(arraySample+'ArrayGrp')
            cmds.select(hi=True)
            cmds.select(arraySample,d=True)
            cmds.select((arraySample+'ArrayGrp'),d=True)
            cutterList = cmds.ls('boxCutter*',sl=True,type='transform')
            cmds.select(arraySample)
            cmds.ConvertInstanceToObject()
            if myType[1] == 'radial':
                cmds.parent(arraySample,(arraySample+'ArrayGrp'))
            unInstanceMesh = cmds.ls(sl=1,fl=1, l=1)
            for c in cutterList:
                if '_Rot' not in c and '_Trans' not in c and 'ArrayGrp' not in c:
                    if myType[1] == 'radial':
                        cmds.parent(c , (arraySample + 'ArrayGrp'))
                    cmds.select(arraySample,r=True)
                    cmds.duplicate()
                    newNode=cmds.ls(sl=True)
                    cmds.select(c,add=1)
                    cmds.matchTransform(pos =True,rot=True)
                    cmds.delete(c)
                    cmds.rename(newNode,c)
            for c in cutterList:
                if '_Rot' in c :
                    cmds.delete(c)
            cmds.select(arraySample+'ArrayGrp')
            cmds.select(hi=True)
            cmds.select((arraySample+'ArrayGrp'),d=True)
            listNew = cmds.ls('boxCutter*',sl=True,type='transform')
            for n in listNew:
                cmds.rename(n,'tempCutter01')
            listBake=cmds.ls('tempCutter*',s=1)
            while len(listBake) > 1:
                cmds.polyCBoolOp(listBake[0], listBake[1], op=1, ch=1, preserveColor=0, classification=1, name=listBake[0])
                cmds.DeleteHistory()
                if cmds.objExists(listBake[1]):
                    cmds.delete(listBake[1])
                cmds.rename(listBake[0])
                listBake.remove(listBake[1])
            #in case cutterGrp will get delete when delete history
            if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
                cmds.CreateEmptyGroup()
                cmds.rename((beseMesh +'_cutterGrp'))
                cmds.parent((beseMesh +'_cutterGrp'),(beseMesh +'BoolGrp'))
            cmds.select(listBake[0])
            useOwnCutterShape()
            newCutter = cmds.ls(sl=True, fl=True)
            cmds.rename(newCutter[0],arraySample)
            cmds.xform(arraySample ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))
            if cmds.objExists(arraySample+'ArrayGrp'):
                cmds.delete(arraySample+'ArrayGrp')
                cmds.ogs(reset =1)
            if not cmds.attributeQuery('cutterOp', node = arraySample, ex=True ):
                cmds.addAttr(arraySample, ln='cutterOp',  dt= 'string')
            cmds.setAttr((arraySample+'.cutterOp'),e=True, keyable=True)
            cmds.setAttr((arraySample+'.cutterOp'),opType,type="string")
            cmds.select(arraySample)
            fixBoolNodeConnection()
    else:
        print ('nothing selected!')

def instRemove():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    myType = checkInstType()
    if myType[1] == 'linear':
        arraySample = myType[0]
        listA = cmds.listConnections(arraySample,type = 'expression')
        if listA != None:
            listA = set(listA)
            collectInst=[]
            for l in listA:
                checkConnection = cmds.connectionInfo( (l+'.output[0]'), dfs=True)
                mesh = checkConnection[0].split(".")[0]
                collectInst.append(mesh)
            cmds.delete(collectInst)
        shapeNode = cmds.listRelatives(arraySample, s=True )
        listConnect = cmds.connectionInfo((shapeNode[0]+'.outMesh'), dfs=True )
        if len(listConnect)>0:
            for a in listConnect:
                cmds.disconnectAttr((shapeNode[0]+'.outMesh'), a)
        checkNumber = ''.join([n for n in arraySample.split('|')[-1] if n.isdigit()])
        if cmds.objExists(beseMesh + '_mySubs') == 0:
            restoreCutterWithSymmtry()

        setType = cmds.getAttr(arraySample+'.cutterOp')

        cmds.connectAttr( (shapeNode[0]+".outMesh"), ((beseMesh +'_my' + setType.title() + '.inputPoly['+str(checkNumber)+']')),f=True)
        cmds.connectAttr( (shapeNode[0]+".worldMatrix[0]"), ((beseMesh +'_my' + setType.title() +'.inputMat['+str(checkNumber)+']')),f=True)
        cmds.select(arraySample)
        checkGap = cmds.getAttr(arraySample + '.panelGap')
        if checkGap > 0:
            makeGap()
            cmds.floatSliderGrp('gapSlider',e=True, en= True,v=checkGap )

#######################################################################################################################################################################################
#######################################################################################################################################################################################
def moveRightItem():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selListRight = cmds.textScrollList('bevelList', q=True, si=True)
    checkState = cmds.iconTextButton('visRight', q = True , image1 = True)
    if selListRight != None:
        if len(selListRight) > 0:
            cmds.textScrollList('nonBevelList',edit = True, da = True)
            for s in selListRight:
                cmds.textScrollList('bevelList',edit = True, ri = s)
                cmds.textScrollList('nonBevelList',edit = True, si = s, append = s)
            sortBevelList()
            for s in selListRight:
                cmds.textScrollList('nonBevelList',edit = True, si = s)
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                if checkState == 'nodeGrapherSoloed.svg':
                    cmds.setAttr((longName + '.visibility'), 1)
                else:
                    cmds.setAttr((longName + '.visibility'), 0)
                cmds.setAttr((longName+'.preBevel'),0)

def moveLeftItem():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selListLeft = cmds.textScrollList('nonBevelList', q=True, si=True)
    checkState = cmds.iconTextButton('visLeft', q = True , image1 = True)
    if selListLeft != None:
        if len(selListLeft) > 0:
            cmds.textScrollList('bevelList',edit = True, da = True)
            for s in selListLeft:
                cmds.textScrollList('nonBevelList',edit = True, ri = s)
                cmds.textScrollList('bevelList',edit = True, si = s ,append = s)
            sortBevelList()
            for s in selListLeft:
                cmds.textScrollList('bevelList',edit = True, si = s)
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                if checkState == 'nodeGrapherSoloed.svg':
                    cmds.setAttr((longName + '.visibility'), 1)
                else:
                    cmds.setAttr((longName + '.visibility'), 0)
                cmds.setAttr((longName+'.preBevel'),1)

def reselctList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    currentSel = cmds.ls(sl=True,l=True)
    cmds.textScrollList('nonBevelList', e=True, da=True)
    selListRight = cmds.textScrollList('nonBevelList', q=True, ai=True)
    if selListRight != None:
        for c in currentSel:
            shortName = c.split('|')[-1]
            for s in selListRight:
                if shortName == s:
                    cmds.textScrollList('nonBevelList',edit = True, si = shortName)

    cmds.textScrollList('bevelList', e=True, da=True)
    selListLeft = cmds.textScrollList('bevelList', q=True, ai=True)
    if selListLeft != None:
        for c in currentSel:
            shortName = c.split('|')[-1]
            for s in selListLeft:
                if shortName == s:
                    cmds.textScrollList('bevelList',edit = True, si = shortName)

def togglevisLeft():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkState = cmds.iconTextButton('visLeft', q = True , image1 = True)
    selListLeft = cmds.textScrollList('bevelList', q=True, ai=True)
    if checkState == 'nodeGrapherSoloed.svg':
        cmds.iconTextButton('visLeft', e = True , image1 = 'circle.png')
        if selListLeft != None and len(selListLeft) > 0:
            for s in selListLeft:
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                cmds.setAttr((longName + '.visibility'), 0)
    else:
        cmds.iconTextButton('visLeft', e = True , image1 = 'nodeGrapherSoloed.svg')
        if selListLeft != None and len(selListLeft) > 0:
            for s in selListLeft:
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                cmds.setAttr((longName + '.visibility'), 1)

def togglevisRight():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkState = cmds.iconTextButton('visRight', q = True , image1 = True)
    selListRight = cmds.textScrollList('nonBevelList', q=True, ai=True)
    if checkState == 'nodeGrapherSoloed.svg':
        cmds.iconTextButton('visRight', e = True , image1 = 'circle.png')
        if selListRight != None and len(selListRight) > 0:
            for s in selListRight:
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                cmds.setAttr((longName + '.visibility'), 0)
    else:
        cmds.iconTextButton('visRight', e = True , image1 = 'nodeGrapherSoloed.svg')
        if selListRight != None and len(selListRight) > 0:
            for s in selListRight:
                longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
                cmds.setAttr((longName + '.visibility'), 1)

def selBevelList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selList = cmds.textScrollList('bevelList', q=True, si=True)
    cmds.textScrollList('nonBevelList',edit = True, da = True)
    longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + selList[0]
    cmds.select(longName, r=True)

def selNonBevelList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selList = cmds.textScrollList('nonBevelList', q=True, si=True)
    cmds.textScrollList('bevelList',edit = True, da = True)
    longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + selList[0]
    cmds.select(longName, r=True)

def visListOn():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selListLeft = cmds.textScrollList('bevelList', q=True, ai=True)
    cmds.iconTextButton('visLeft', e = True , image1 = 'nodeGrapherSoloed.svg')
    if selListLeft != None and len(selListLeft) > 0:
        for s in selListLeft:
            longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
            cmds.setAttr((longName + '.visibility'), 1)

    selListRight = cmds.textScrollList('nonBevelList', q=True, ai=True)
    cmds.iconTextButton('visRight', e = True , image1 = 'nodeGrapherSoloed.svg')
    if selListRight != None and len(selListRight) > 0:
        for s in selListRight:
            longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
            cmds.setAttr((longName + '.visibility'), 1)
    cmds.setAttr((beseMesh+'_bakeStep.visibility'),1)

def visListOff():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selListLeft = cmds.textScrollList('bevelList', q=True, ai=True)
    cmds.iconTextButton('visLeft', e = True , image1 = 'circle.png')
    if selListLeft != None and len(selListLeft) > 0:
        for s in selListLeft:
            longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
            cmds.setAttr((longName + '.visibility'), 0)

    selListRight = cmds.textScrollList('nonBevelList', q=True, ai=True)
    cmds.iconTextButton('visRight', e = True , image1 = 'circle.png')
    if selListRight != None and len(selListRight) > 0:
        for s in selListRight:
            longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + s
            cmds.setAttr((longName + '.visibility'), 0)
    cmds.setAttr((beseMesh+'_bakeStep.visibility'),1)

def loadBevelList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    list = cmds.ls('bakeCutter*',type='transform',l=True)
    if len(list) > 0:
        cleanList = []
        for l in list:
            if beseMesh in l:
                cleanList.append(l)
        cmds.textScrollList('bevelList',edit = True, ra = True)
        cmds.textScrollList('nonBevelList',edit = True, ra = True)
        for c in cleanList:
            shortName = c.split('|')[-1]
            checkState = cmds.getAttr(c+'.preBevel')
            if checkState == 1:
                cmds.textScrollList('bevelList',edit = True, append = shortName)
            else:
                cmds.textScrollList('nonBevelList',edit = True, append = shortName)

def publishFinal():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        if cmds.objExists(beseMesh + '_publishMesh'):
            print ('publishMesh existed!')

        else:
            if cmds.objExists(beseMesh + '_preBevelMeshFinal'):
                newNode = cmds.duplicate((beseMesh + '_preBevelMeshFinal'),rr = True, un=True)
                cmds.rename(newNode[0],(beseMesh + '_publishMesh'))
                cmds.parent((beseMesh + '_publishMesh'),w=True)
                cmds.DeleteHistory()
                cmds.setAttr((beseMesh+ 'BoolGrp.visibility'),0)
            else:
                if cmds.objExists(beseMesh + '_preBaseMesh'):
                    newNode = cmds.duplicate((beseMesh + '_preBaseMesh'),rr = True, un=True)
                    cmds.rename(newNode[0],(beseMesh + '_publishMesh'))
                    cmds.parent((beseMesh + '_publishMesh'),w=True)
                    cmds.DeleteHistory()
                    cmds.setAttr((beseMesh+ 'BoolGrp.visibility'),0)
                else:
                    print ('nothing to publish')

def preCheckBevelByVolumn():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    bbox = cmds.xform(beseMesh, q=True, ws=True, bbi=True)
    disX =  math.sqrt((bbox[3] - bbox[0])*(bbox[3] - bbox[0]))
    disY =  math.sqrt((bbox[4] - bbox[1])*(bbox[4] - bbox[1]))
    disZ =  math.sqrt((bbox[5] - bbox[2])*(bbox[5] - bbox[2]))
    baseVolumn = disX * disY *disZ
    guildVolumn = baseVolumn * 0.01 # 5% of base
    #check all cutter
    cmds.select((beseMesh+'_bakeStep'), hi=True)
    cmds.select((beseMesh+'_bakeStep'),d=True)
    cmds.select((beseMesh+'_bakeBaseMesh'),d=True)
    sel = cmds.ls(sl=1,fl=1,type='transform',l=True)
    cmds.select(cl=True)
    for s in sel:
        checkState = cmds.getAttr(s+'.statePanel')# skip if gap or panel
        if not cmds.attributeQuery('preBevel', node = s, ex=True ):
            cmds.addAttr(s, ln='preBevel', at = "float" )
            cmds.setAttr((s+'.preBevel'), 0)
            checkStateBevel = cmds.getAttr(s+'.preBevel')# already Made as non bevel
            if checkState == 0 and checkStateBevel == 1 :
                bbox = cmds.xform(s, q=True, ws=True, bbi=True)
                disX =  math.sqrt((bbox[3] - bbox[0])*(bbox[3] - bbox[0]))
                disY =  math.sqrt((bbox[4] - bbox[1])*(bbox[4] - bbox[1]))
                disZ =  math.sqrt((bbox[5] - bbox[2])*(bbox[5] - bbox[2]))
                volumn = disX * disY *disZ
                if volumn < guildVolumn:
                    cmds.setAttr((s+'.preBevel'), 0)
                else:
                    cmds.setAttr((s+'.preBevel'), 1)

def removeNonBevelList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        removeLeftOver()
        cmds.setAttr(beseMesh + '_preBevel.visibility',1)
        cmds.rename((beseMesh + '_preBevel'),(beseMesh + '_preBaseMesh'))
        list = cmds.listHistory((beseMesh + '_preBaseMesh'))
        for l in list:
            nodeTypeA = cmds.nodeType(l)
            if nodeTypeA == 'polyBevel3':
                cmds.rename(l,(beseMesh+'_edgePreBevel'))
            elif  nodeTypeA == 'polyExtrudeFace':
                cmds.rename(l,(beseMesh+'_lcokFace'))
            else:
                pass
        offsetV = cmds.floatSliderGrp('offsetSliderPre',q=1, v =True)
        lockV = cmds.floatSliderGrp('lockFaceSliderPre',q=1, v =True)
        segV = cmds.intSliderGrp('segmentSliderPre',  q=1, v =True)
        miterV = cmds.intSliderGrp('miteringSliderPre', q=1,v =True)
        cmds.setAttr((beseMesh+'_lcokFace.offset'),lockV)
        cmds.setAttr((beseMesh+'_edgePreBevel.segments'), segV)
        cmds.setAttr((beseMesh+'_edgePreBevel.mitering'), miterV)
        cmds.setAttr((beseMesh+'_edgePreBevel.offset'), offsetV)
        visListOff()
        outlineClean()
        cmds.button('addPreBButton',e=True,en=False)
        cmds.button('removePreBButton',e=True,en=True)
        cmds.button('addPreNonBButton',e=True,en=True)
        cmds.button('removePreNonBButton',e=True,en=False)
        cmds.floatSliderGrp('lockFaceSliderPre',e=1, en=0)
        cmds.floatSliderGrp('offsetSliderPre',e=1, en=1)
        cmds.intSliderGrp('segmentSliderPre',e=1, en=1)
        cmds.intSliderGrp('miteringSliderPre',e=1, en=1)
        cmds.connectControl('segmentSliderPre', (beseMesh+'_edgePreBevel.segments'))
        cmds.connectControl('miteringSliderPre',(beseMesh+'_edgePreBevel.mitering'))
        cmds.connectControl('offsetSliderPre', (beseMesh+'_edgePreBevel.offset'))
        if cmds.objExists(beseMesh + '_preBevelGrp'):
            cmds.delete(beseMesh + '_preBevelGrp')
        cmds.select((beseMesh + '_preBaseMesh'))

def addNonBevelList():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists(beseMesh + '_boolNonBevelUnion') == 0 or cmds.objExists(beseMesh + '_boolNonBevelSubs') == 0 or cmds.objExists(beseMesh + '_boolNonBevelCut') == 0:
        if len(beseMesh) > 0:
            boolPreNonBevel()
            visListOff()
            #outlineClean()
            cmds.intSliderGrp('segmentSliderPre',e=True,en=True)
            cmds.intSliderGrp('miteringSliderPre',e=True,en=True)
            cmds.button('addPreBButton',e=True,en=False)
            cmds.button('removePreBButton',e=True,en=True)
            cmds.button('addPreNonBButton',e=True,en=False)
            cmds.button('removePreNonBButton',e=True,en=True)
            cmds.button('removeLockButton', e=1, en = 0)
            cmds.button('removePreBButton', e=1, en = 0)
            cmds.intSliderGrp('segmentSliderPre',e=1, en=0)
            cmds.intSliderGrp('miteringSliderPre',e=1, en=0)

def rebuildPreview():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        if cmds.objExists('*preBevel*'):
            cmds.delete('*preBevel*')
        if cmds.objExists('*_preBaseMesh*'):
            cmds.delete('*_preBaseMesh*')
        if cmds.objExists('*boolNon*'):
            cmds.delete('*boolNon*')
        cmds.setAttr((beseMesh +'BoolGrp.visibility'),1)
        cmds.setAttr((beseMesh +'_bool.visibility'),1)
        cmds.button('addPreBButton',e=True,en=False)
        cmds.button('removePreBButton',e=True,en=False)

def killPreview():
    rebuildPreview()
    restoreCutter()
    cmds.button('addPreBButton',e=True,en=False)
    cmds.button('removePreBButton',e=True,en=False)
    cmds.button('addPreNonBButton',e=True,en=False)
    cmds.button('removePreNonBButton',e=True,en=False)
    cmds.button('removeLockButton',e=True,en=False)
    cmds.button('addLockButton',e=True,en=False)
    cmds.button('addCutButton',e=True,en=True)


    #if cmds.window("jwSpeedCutBevelManger", exists = True):
    #    cmds.deleteUI("jwSpeedCutBevelManger")

def preBevelUpdate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        cutUpdate()
        lcokUpdate()
        addPreBevelEdgeRun()
        addNonBevelList()
        cmds.floatSliderGrp('lockFaceSliderPre',e=1, en=1)
        cmds.floatSliderGrp('offsetSliderPre', e=True, v = 1, min = 0.001, max = 1, fmx = 10)

def cutUpdate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    offsetV = cmds.floatSliderGrp('offsetSliderPre',q=1, v =True)
    lockV = cmds.floatSliderGrp('lockFaceSliderPre',q=1, v =True)
    segV = cmds.intSliderGrp('segmentSliderPre',  q=1, v =True)
    miterV = cmds.intSliderGrp('miteringSliderPre', q=1,v =True)
    if len(beseMesh) > 0:
        loadBevelList()
        rebuildPreview()
        setPreBevelGrp()
        boolPreBevel()
        visListOff()
        #outlineClean()
        member = beseMesh + '_preBaseMesh'
        cmds.select(beseMesh + '_preBaseMesh')
        cmds.intSliderGrp('segmentSliderPre',e=True,en=False)
        cmds.intSliderGrp('miteringSliderPre',e=True,en=False)
        cmds.floatSliderGrp('lockFaceSliderPre',e=True,en=False)
        cmds.floatSliderGrp('offsetSliderPre',e=True,en=False)
        cmds.button('addLockButton',e=True,en=True)
        #Retop
        cmds.polySelectConstraint(m=3,t=0x8000,sm=1)
        cmds.polySelectConstraint(disable =True)
        triNode = cmds.polyTriangulate(member,ch=0)
        quadNode = cmds.polyQuad(member,a = 30, kgb = 0 ,ktb = 0, khe= 1, ws = 0, ch = 0)
        cmds.delete(ch = True)
        #Clean
        cmds.select(member)
        mergeNode = cmds.polyMergeVertex( d = 0.01,ch = True)
        softNode = cmds.polySoftEdge(angle=0.3)
        mel.eval("ConvertSelectionToEdges;")
        cmds.polySelectConstraint(t=0x8000, m=3, sm=2)
        cmds.polySelectConstraint(disable =True)
        selectEdges=cmds.ls(sl=1,fl=1)
        if len(selectEdges)>0:
            cmds.polyDelEdge(cv = True, ch = False)
        #Clean unused vertex points
        cmds.select(member)
        mergeNode = cmds.polyMergeVertex( d = 0.01,ch = True)
        cmds.select(member)
        cmds.ConvertSelectionToVertices()
        selected = cmds.ls(sl=1, fl=1)
        cmds.select(clear=True)
        for v in selected:
            if len( re.findall('\d+', cmds.polyInfo(v,ve=True)[0]) ) == 3:
                cmds.select(v,add=True)
        cmds.delete(cmds.ls(sl=True))
        cmds.select(member)
        softNode = cmds.polySoftEdge(angle=30)
        #merge very close vertex by user
        cmds.select(member)
        cmds.delete(ch = True)
        cmds.select(member)
        mergeNode = cmds.polyMergeVertex( d = 0.01,ch = 0)
        cmds.button('removeLockButton', e=1, en = 0)
        cmds.select(member)
        cmds.button('addLockButton', e=1, en = 1)

def bevelPreviewLockFace():
    global sourceFaces
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    member = beseMesh + '_preBaseMesh'
    cmds.select(member)
    cmds.polySelectConstraint(m=3,t=0x8000,sm=1)
    cmds.polySelectConstraint(disable =True)
    hardEdges = cmds.ls(sl=1,fl=1)
    cmds.DetachComponent()
    listH = cmds.listHistory(member, lv=0 )
    for h in listH:
        checkNode = cmds.nodeType(h)
        if checkNode == 'polySplitEdge':
            cmds.rename(h,'lockStart')
    cmds.select(member)
    cmds.ConvertSelectionToFaces()
    sourceFaces = cmds.ls(sl=1,fl=1)
    offsetData = cmds.floatSliderGrp('offsetSliderPre', q=1, v = 1)
    createSupportNode = cmds.polyExtrudeFacet(sourceFaces, constructionHistory =1, keepFacesTogether = 1, divisions = 1, off = offsetData, smoothingAngle = 30)
    faceLockNode = cmds.rename(createSupportNode[0], (beseMesh+'_lcokFace'))
    cmds.GrowPolygonSelectionRegion()
    shapeExtrude = cmds.ls(sl=1,fl=1)
    cmds.select(member)
    cmds.ConvertSelectionToFaces()
    cmds.select(shapeExtrude,d=1 )
    cmds.delete()
    cmds.select(member)
    cmds.polyMergeVertex(d = 0.001, ch = 1)
    cmds.setAttr((faceLockNode + ".offset"), offsetData)
    cmds.connectControl('lockFaceSliderPre', (faceLockNode + ".offset"))
    cmds.setAttr((faceLockNode + ".offset"),0.1)
    cmds.polySelectConstraint(m=3,t=0x8000,sm=1)
    cmds.polySelectConstraint(disable =True)
    softNode = cmds.polySoftEdge(angle= 180)
    cmds.rename(softNode,'preSoftEdge')
    cmds.select(cl=True)

def mergeHardEdgeVex():# vertices too close
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    member = beseMesh + '_preBaseMesh'
    cmds.select(member)
    cmds.polySelectConstraint(m=3,t=0x8000,sm=1)
    cmds.polySelectConstraint(disable =True)
    cmds.ConvertSelectionToVertices()
    cmds.polyMergeVertex(d= 0.1,am= 1, ch= 1)

def smoothAroundLockEdge():#relax vertices surround lock edge then snap back to bool mesh to maintain shape
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = beseMesh + '_bool'
    global sourceFaces
    cmds.select(sourceFaces)
    mel.eval('InvertSelection')
    cmds.ConvertSelectionToVertices()
    tempSel=cmds.ls(sl=1,fl=1)
    cmds.GrowPolygonSelectionRegion()
    cmds.select(tempSel, d=1 )
    cmds.polyAverageVertex(i=10)
    cmds.polyAverageVertex(i=10)
    cmds.select(snapMesh,add=1)
    cmds.transferAttributes(transferPositions =1, transferNormals= 0, transferUVs =0, transferColors= 2, sampleSpace = 0, searchMethod = 3, flipUVs = 0, colorBorders =0)
    cmds.select(cl=1)

def bevelPreviewLockFaceRemove():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    member = beseMesh + '_preBaseMesh'
    cmds.select(member)
    listH = cmds.listHistory(member, lv=0 )
    for h in listH:
        checkNode = cmds.nodeType(h)
        if checkNode != 'mesh':
            cmds.delete(h)
            if 'lockStart' in h:
                break
    cmds.button('removeLockButton', e=1, en = 0)
    cmds.button('addLockButton', e=1, en = 1)
    cmds.button('addPreBButton', e=1, en = 0)
    cmds.button('removePreBButton', e=1, en = 0)
    cmds.button('addPreNonBButton', e=1, en = 0)
    cmds.button('removePreNonBButton', e=1, en = 0)
    cmds.connectControl('lockFaceSliderPre', (beseMesh + '_lcokFace.offset'))
    cmds.select(member)
    softHardVis()

def lcokUpdate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    offsetV = cmds.floatSliderGrp('offsetSliderPre',q=1, v =True)
    lockV = cmds.floatSliderGrp('lockFaceSliderPre',q=1, v =True)
    segV = cmds.intSliderGrp('segmentSliderPre',  q=1, v =True)
    miterV = cmds.intSliderGrp('miteringSliderPre', q=1,v =True)
    if len(beseMesh) > 0:
        bevelPreviewLockFace()
        cmds.setAttr((beseMesh+'_lcokFace.offset'),lockV)
        visListOff()
        outlineClean()
        cmds.select(beseMesh + '_preBaseMesh')
        cmds.button('addPreBButton',e=True,en=True)
        cmds.button('removePreBButton',e=True,en=False)
        cmds.button('addPreNonBButton',e=True,en=False)
        cmds.button('removePreNonBButton',e=True,en=False)
        cmds.button('removeLockButton', e=1, en = 1)
        cmds.button('addLockButton', e=1, en = 0)

def addPreBevelEdgeRun():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists(beseMesh +'_edgePreBevel') == 0:
        lockV = cmds.floatSliderGrp('lockFaceSliderPre',q=1, v =True)
        addPreBevelEdge()
        visListOff()
        outlineClean()
        cmds.button('addPreBButton',e=True,en=False)
        cmds.button('removePreBButton',e=True,en=True)
        cmds.floatSliderGrp('lockFaceSliderPre',e=True,en=False)
        cmds.floatSliderGrp('offsetSliderPre',e=True,en=True , max = lockV)
        cmds.button('addPreNonBButton',e=True,en=True)
        cmds.button('removePreNonBButton',e=True,en=False)
        cmds.button('addLockButton',e=True,en=False)
        cmds.setAttr((beseMesh+'_edgePreBevel.offset'),lockV)
        cmds.select(beseMesh + '_preBaseMesh')
        cmds.TogglePolyDisplayEdges()
        cmds.button('removeLockButton',e=1, en=0)

def removePreBevelEdgeRun():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    cmds.delete(beseMesh + '_preBaseMesh')
    cmds.showHidden(beseMesh + '_preBaseLock')
    cmds.rename((beseMesh + '_preBaseLock') ,(beseMesh + '_preBaseMesh'))
    outlineClean()
    cmds.button('addPreBButton',e=True,en=True)
    cmds.button('removePreBButton',e=True,en=False)
    cmds.floatSliderGrp('lockFaceSliderPre',e=True,en=True)
    cmds.floatSliderGrp('offsetSliderPre',e=True,en=False)
    cmds.button('addPreNonBButton',e=True,en=False)
    cmds.button('removePreNonBButton',e=True,en=False)
    cmds.button('removeLockButton', e=1, en = 0)
    cmds.button('addLockButton', e=1, en = 0)
    cmds.button('removeLockButton', e=1, en = 1)
    cmds.select(beseMesh + '_preBaseMesh')
    listH = cmds.listHistory((beseMesh + '_preBaseMesh'), lv=0 )
    for l in listH:
        checkType=cmds.nodeType(l)
        if  checkType == "polyExtrudeFace":
            cmds.connectControl('lockFaceSliderPre', (l + ".offset"))

def addPreBevelEdge():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    newGrp = cmds.duplicate((beseMesh + '_preBaseMesh'),rr = True, un=True)
    if cmds.objExists(beseMesh+'_preBaseLock'):
        cmds.delete(beseMesh + '_preBaseLock')
    cmds.rename(newGrp,(beseMesh + '_preBaseLock'))
    cmds.hide(beseMesh + '_preBaseLock')
    cmds.select(beseMesh + '_preBaseMesh')
    mel.eval("ConvertSelectionToEdges;")
    softNode = cmds.polySoftEdge(angle=30)
    cmds.polySelectConstraint(m=3,t=0x8000,sm=1)
    cmds.polySelectConstraint(disable =True)
    hardEdges = cmds.ls(sl=1,fl=1)
    bevelNodeNew = cmds.polyBevel3(hardEdges, offset = 0.1, offsetAsFraction= 0, autoFit= 1, depth= 1, mitering= 1 ,miterAlong= 0 ,chamfer =1 ,segments= 3 ,worldSpace= 0 ,smoothingAngle= 30 ,subdivideNgons =1 ,mergeVertices= 1, mergeVertexTolerance= 0.0001, miteringAngle=180, angleTolerance =180 ,ch= 1)
    cmds.rename(bevelNodeNew,(beseMesh+'_edgePreBevel'))
    cmds.connectControl('segmentSliderPre', (beseMesh+'_edgePreBevel.segments'))
    cmds.connectControl('miteringSliderPre',(beseMesh+'_edgePreBevel.mitering'))
    cmds.connectControl('offsetSliderPre', (beseMesh+'_edgePreBevel.offset'))
    softHardVis()

def outlineClean():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkList = ['_cutterGrp','_preSubBox','_preUnionBox','_preBevelMeshUnion','_preBevelMeshSubs','_myBoolUnion','_bool','_preBaseMeshBackup' ,'_preBevelGrp','_preBaseMesh','_preBaseMeshFinal','_preBevelMeshFinal','_boolNonBevelUnion','_boolNonBevelsubs']
    for c in checkList:
        checkGrp = cmds.ls((beseMesh + c), l=True)
        if len(checkGrp)>0:
            if 'BoolGrp' not in checkGrp[0]:
                cmds.parent(checkGrp[0],(beseMesh +'BoolGrp'))

def removeLeftOver():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkList = ['_preBevelMeshSubs','_boolNonBevelUnion','_boolNonBevelSubs','_preBevelMeshFinal']
    for c in checkList:
        if cmds.objExists(beseMesh + c):
            cmds.delete(beseMesh + c)

def boolPreNonBevel():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    preBevelMesh = (beseMesh + '_preBaseMesh')
    newNode = cmds.duplicate(preBevelMesh,n=(beseMesh + '_preBaseMeshBackup'),rr=1,un=1)
    cmds.setAttr(beseMesh + '_preBaseMeshBackup.visibility',0)
    cmds.rename(newNode, (beseMesh + '_preBevel'))
    nonBevelsList = cmds.textScrollList('nonBevelList', q=True, ai=True)

    if cmds.objExists(beseMesh+'_preBevelGrp') == 0:
        newGrp = cmds.duplicate((beseMesh + '_bakeStep'),rr = True, un=True)
        cmds.parent(newGrp,w=True)
        cmds.rename(beseMesh + '_preBevelGrp')
        cmds.select(hi=True)
        #rename
        listCutters = cmds.ls(sl=True, type ='transform',l=True)
        for l in listCutters:
            if '_bakeBaseMesh' in l:
                cmds.delete(l)
            else:
                sName = l.replace('bake','pre')
                cmds.rename(l, sName.split("|")[-1])
        cmds.parent((beseMesh + '_preBevelGrp'),(beseMesh + 'BoolGrp'))
        # sort operation type
    subsGrp = []
    unionGrp = []
    cutGrp = []
    for b in nonBevelsList:
        longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + b
        if cmds.objExists(longName):
            checkOP = cmds.getAttr(longName + '.cutterOp')
            if checkOP == 'subs':
                subsGrp.append(b)
            elif checkOP == 'union':
                unionGrp.append(b)
            elif checkOP == 'cut':
                cutGrp.append(b)

    for s in subsGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|' +  beseMesh  + '_preBevelGrp|'+ (s.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=2, ch=1, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    for u in unionGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|' +  beseMesh  + '_preBevelGrp|'+ (u.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=1, ch=1, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    for c in cutGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|' +  beseMesh  + 'BoolGrp|' + beseMesh + '_preBevelGrp|'+ (c.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=2, ch=1, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    cmds.rename(beseMesh + '_preBevelMeshFinal')
    cmds.parent((beseMesh + '_preBevelMeshFinal') ,( beseMesh  + 'BoolGrp|'))

def boolPreBevel():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    bevelsList = cmds.textScrollList('bevelList', q=True, ai=True)
    cmds.parent(('|' +  beseMesh  + 'BoolGrp|'  +  beseMesh  + '_preBevelGrp|' + beseMesh + '_preBaseMesh'),w=True)
    preBevelMesh = (beseMesh + '_preBaseMesh')
    # sort operation type
    subsGrp = []
    unionGrp = []
    cutGrp = []
    for b in bevelsList:
        longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_bakeStep|' + b
        if cmds.objExists(longName):
            checkOP = cmds.getAttr(longName + '.cutterOp')
            if checkOP == 'subs':
                subsGrp.append(b)
            elif checkOP == 'union':
                unionGrp.append(b)
            elif checkOP == 'cut':
                cutGrp.append(b)

    for s in subsGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|'  +  beseMesh  + '_preBevelGrp|'+ (s.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=2, ch=0, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    for u in unionGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|'  +  beseMesh  + '_preBevelGrp|'+ (u.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=1, ch=0, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    for c in cutGrp:
        newNode =  '|' +  beseMesh  + 'BoolGrp|'  +  beseMesh  + '_preBevelGrp|'+ (c.replace('bake','pre'))
        cmds.polyCBoolOp(preBevelMesh, newNode, op=2, ch=0, preserveColor=0, classification=1, name= preBevelMesh)
        cmds.DeleteHistory()
        cmds.rename(preBevelMesh)
    cmds.parent(preBevelMesh,('|' +  beseMesh  + 'BoolGrp|'))
    cmds.select(preBevelMesh)
    mel.eval('setSelectMode components Components')
    cmds.selectType(smp= 0, sme= 1, smf= 0, smu = 0, pv= 0, pe = 1, pf= 0, puv= 0)
    cmds.TogglePolyDisplayHardEdgesColor()

def setPreBevelGrp():
    bakeCutter('All')
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    newGrp = cmds.duplicate((beseMesh + '_bakeStep'),rr = True, un=True)
    cmds.parent(newGrp,w=True)
    cmds.rename(beseMesh + '_preBevelGrp')
    cmds.select(hi=True)
    #rename
    listCutters = cmds.ls(sl=True, type ='transform',l=True)
    for l in listCutters:
        sName = l.replace('bake','pre')
        cmds.rename(l, sName.split("|")[-1])
    #show
    listCutters = cmds.ls(sl=True, type ='transform',l=True)
    for l in listCutters:
        cmds.setAttr((l + '.visibility'),1)
    cmds.setAttr((beseMesh + 'BoolGrp.visibility'),1)
    cmds.setAttr((beseMesh + '_bakeStep.visibility'),1)
    cmds.setAttr((beseMesh + '_bool.visibility'),0)
    cmds.setAttr((beseMesh + '_preBevelGrp.visibility'),1)
    list = cmds.ls('preCutter*',type='transform')
    for i in list:
        cmds.setAttr((i + '.visibility'),0)
    cmds.parent((beseMesh + '_preBevelGrp'),(beseMesh + 'BoolGrp'))

def sortBevelList():
    selListLeft = cmds.textScrollList('bevelList', q=True, ai=True)
    if selListLeft != None:
        if len(selListLeft) > 0:
            selListLeft.sort()
            cmds.textScrollList('bevelList',edit = True, ra = True)
            for s in selListLeft:
                cmds.textScrollList('bevelList',edit = True, append = s)

    selListRight = cmds.textScrollList('nonBevelList', q=True, ai=True)
    if selListRight != None:
        if len(selListRight) > 0:
            selListRight.sort()
            cmds.textScrollList('nonBevelList',edit = True, ra = True)
            for s in selListRight:
                cmds.textScrollList('nonBevelList',edit = True, append = s)

def jwSpeedCutBevelMangerSetup():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh)>0:
        jwSpeedCutBevelMangerUI()
        bakeCutter('all')
        preCheckBevelByVolumn()
        loadBevelList()
        visListOn()
        cmds.button('addPreBButton',e=True,en=False)
        cmds.button('removePreBButton',e=True,en=False)
        cmds.button('addPreNonBButton',e=True,en=False)
        cmds.button('removePreNonBButton',e=True,en=False)

def softHardVis():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkState = cmds.iconTextButton('edgeVis' , q = True , image1 = True)
    if cmds.objExists((beseMesh + '_preBaseMesh')):
        cmds.select(beseMesh + '_preBaseMesh')
        if checkState == 'nodeGrapherSoloed.svg':
            cmds.iconTextButton('edgeVis' , e = True , image1 = 'circle.png')
            cmds.TogglePolyDisplayEdges()
        else:
            cmds.iconTextButton('edgeVis' , e = True , image1 = 'nodeGrapherSoloed.svg')
            cmds.TogglePolyDisplayHardEdgesColor()
    #change to edge mode
    mel.eval('setSelectMode components Components')
    cmds.selectType(smp= 0, sme= 1, smf= 0, smu = 0, pv= 0, pe = 1, pf= 0, puv= 0)

def jwSpeedCutBevelMangerUI():
    if cmds.window("jwSpeedCutBevelManger", exists = True):
        cmds.deleteUI("jwSpeedCutBevelManger")
    jwSpeedCutBevelManger = cmds.window("jwSpeedCutBevelManger",title = "speedCut Bevel Manger",w = 400,h = 380, mxb = False, s = 1, bgc = [0.2, 0.2, 0.2  ])
    cmds.columnLayout()
    cmds.rowColumnLayout(nc= 1, cw = [(1, 420)])
    cmds.separator( height=15, style='none' )
    cmds.setParent( '..' )
    cmds.rowColumnLayout(nc= 5, cw = [(1, 20),(2, 200),(3, 40),(4,10),(5, 200)])
    cmds.text(l ='')
    cmds.menuBarLayout()
    cmds.rowColumnLayout(nc= 3, cw = [(1,50),(2,100),(3,20)])
    cmds.text(l ='Bevel' ,en=False)
    cmds.text(l ='')
    cmds.iconTextButton('visLeft' , h = 20, style='iconOnly', image1 = 'nodeGrapherSoloed.svg',  c = 'togglevisLeft()')
    cmds.setParent( '..' )
    cmds.scrollLayout(h = 320)
    cmds.textScrollList('bevelList',  h= 300, w =180, vis = True, ams= True, sc= 'selBevelList()')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.columnLayout()
    cmds.text(l ='',h=150)
    cmds.iconTextButton('moveLeft' , w = 30, style='iconOnly', image1 = 'timeplay.png',  c = 'moveRightItem()')
    cmds.text(l ='',h=10)
    cmds.iconTextButton('moveRight' , w = 30, style='iconOnly', image1 = 'timerev.png',  c = 'moveLeftItem()')
    cmds.text(l ='',h=10)
    cmds.setParent( '..' )
    cmds.text(l ='',h=10)
    cmds.menuBarLayout()
    cmds.rowColumnLayout(nc= 3, cw = [(1,50),(2,100),(3,20)])
    cmds.text(l ='Ignore' ,en=False)
    cmds.text(l ='')
    cmds.iconTextButton('visRight' , h = 20, style='iconOnly', image1 = 'nodeGrapherSoloed.svg',  c = 'togglevisRight()')
    cmds.setParent( '..' )
    cmds.scrollLayout(h= 320)
    cmds.textScrollList('nonBevelList',  h= 300, w =180, vis = True, ams= True, sc= 'selNonBevelList()')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.separator( height=1, style='none' )
    cmds.rowColumnLayout(nc=2, cw = [(1,215),(2,270)])
    cmds.frameLayout(  labelVisible = 0,vis = 1)
    cmds.columnLayout()
    cmds.rowColumnLayout(nc=6, cw = [(1,55),(2,50),(3,3),(4,50),(5,3),(6,50)])
    cmds.text(l ='All')
    cmds.button('updatePreBButton', w = 50, l= "Auto",  c = 'preBevelUpdate()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('killPreBButton', w = 50,   l= "x",  c = 'killPreview()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('outMeshButton', w = 50,   l= "Output",  c = 'publishFinal()',bgc = [0.14, 0.14, 0.14] )
    cmds.setParent( '..' )
    bSize = 76 #button
    sSize = 250#slider
    tSize = 65 #slider Text
    cmds.separator( height=5, style='none' )
    cmds.rowColumnLayout(nc=6, cw = [(1,55),(2,50),(3,3),(4,50),(5,3),(6,50)])
    cmds.text(l ='Mesh ')
    cmds.button('addCutButton', w = 50,   l= "Cut",  c = 'cutUpdate()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('addLockButton', w = 50, en=0,  l= "Lock",  c = 'lcokUpdate()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('removeLockButton', w = 50, en = 0,  l= "Remove",  c = 'bevelPreviewLockFaceRemove()',bgc = [0.14, 0.14, 0.14] )
    cmds.setParent( '..' )
    cmds.separator( height=5, style='none' )
    cmds.rowColumnLayout(nc=4, cw = [(1,55),(2,bSize),(3,3),(4,bSize)])
    cmds.text(l ='Bevel ')
    cmds.button('addPreBButton', w = bSize,   l= "Add",  c = 'addPreBevelEdgeRun()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('removePreBButton', w = bSize,   l= "Remove",  c = 'removePreBevelEdgeRun()',bgc = [0.14, 0.14, 0.14] )
    cmds.setParent( '..' )
    cmds.separator( height=5, style='none' )
    cmds.rowColumnLayout(nc=4, cw = [(1,55),(2,bSize),(3,3),(4,bSize)])
    cmds.text(l =' NonBevel')
    cmds.button('addPreNonBButton', w = bSize,   l= "Add",  c = 'addNonBevelList()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('removePreNonBButton', w = bSize,   l= "Remove",  c = 'removeNonBevelList()',bgc = [0.14, 0.14, 0.14] )
    cmds.setParent( '..' )
    cmds.separator( height=5, style='none' )
    cmds.rowColumnLayout(nc=8, cw = [(1,55),(2,20),(3,9),(4,40),(5,3),(6,40),(7,3),(8,40)])
    cmds.text(l =' Edge')
    cmds.iconTextButton('edgeVis' , h = 20, style='iconOnly', image1 = 'circle.png',  c = 'softHardVis()')
    cmds.text(l ='')
    cmds.button('selContEdgeButton',  l= "Loop",  c = 'cmds.SelectContiguousEdges()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('edgeHardButton', l= "H",  c = 'cmds.PolygonHardenEdge()',bgc = [0.14, 0.14, 0.14] )
    cmds.text(l ='')
    cmds.button('edgeSoftButton',  l= "S",  c = 'cmds.PolygonSoftenEdge()',bgc = [0.14, 0.14, 0.14] )

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout(  labelVisible = 0,vis = 1)
    cmds.floatSliderGrp('lockFaceSliderPre', en=1, v = 0.1, min = 0.001, max = 1, fmx = 5, s = 0.01, cw3 = [tSize,40,sSize] , label = "Lock" ,field =True)
    cmds.floatSliderGrp('offsetSliderPre', en=1, v = 0.1, min = 0.001, max = 1, fmx = 10, s = 0.01, cw3 = [tSize,40,sSize] , label = "Offset" ,field =True)
    cmds.intSliderGrp('segmentSliderPre',  en=1, v = 2,   min = 1 ,    max = 5, s = 1,    cw3 = [tSize,40,sSize] , label = "Segments" ,field =True)
    cmds.intSliderGrp('miteringSliderPre', en=1, v = 1,   min = 0, max = 3,  s = 1, cw3 = [tSize,40,sSize] , label = "Mitering " ,field =True)
    cmds.setParent( '..' )
    cmds.text(l ='')
    cmds.separator( height=15, style='none' )
    cmds.showWindow(jwSpeedCutBevelManger)
    obNum = cmds.scriptJob ( p = 'jwSpeedCutBevelManger', event = ["SelectionChanged", reselctList])
##################################################################################################################
def baseMeshColorUpdate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    shapes = cmds.listRelatives((beseMesh+'_bool'), shapes=True)
    shadeEng = cmds.listConnections(shapes , type = 'shadingEngine')
    if shadeEng:
        colorData ={  2 : (0.25, 0.25 , 0.25),
                      3 : (0.6 , 0.6  , 0.6 ),
                      4 : (0.61, 0    , 0.16),
                      5 : (0.0 , 0.02 , 0.38),
                      6 : (0.0 , 0    , 1   ),
                      7 : (0.0 , 0.28 , 0.1 ),
                      8 : (0.15, 0.0  , 0.26),
                      9 : (0.78, 0.0  , 0.78),
                     10 : (0.54, 0.28 , 0.2 ),
                     11 : (0.25, 0.14 , 0.12),
                     12 : (0.32 , 0.02 , 0.0 ),
                     15 : (0.0 , 0.26 , 0.6 ),
                     20 : (1.0 , 0.43 , 0.43),
                     21 : (0.9 , 0.68 , 0.47),
                     23 : (0.0 , 0.60 , 0.33),
                     24 : (0.63, 0.42 , 0.19),
                     25 : (0.62, 0.63 , 0.19),
                     26 : (0.41, 0.63 , 0.19),
                     27 : (0.19, 0.63 , 0.36),
                     28 : (0.19, 0.63 , 0.63),
                     29 : (0.19, 0.40 , 0.63),
                     30 : (0.44, 0.15 , 0.63),
                     31 : (0.63, 0.19 , 0.42),
                     }
        score = list(colorData.items())

        materials = cmds.ls(cmds.listConnections(shadeEng ), materials = True)
        if materials[0] == (beseMesh+'_Shader'):
            cmds.sets((beseMesh+'_bool'), e=True, forceElement = 'initialShadingGroup')
            if cmds.objExists(beseMesh+'_Shader'):
                cmds.delete(beseMesh+'_Shader')
            if cmds.objExists(beseMesh+'_ShaderSG'):
                cmds.delete(beseMesh+'_ShaderSG')
            cmds.setAttr((beseMesh + '_BoolResult.color'),0)
            cmds.setAttr((beseMesh + "BoolGrp.useOutlinerColor"), 0)
        else:
            if cmds.objExists(beseMesh+'_Shader') == 0:
                shd = cmds.shadingNode('lambert', name=(beseMesh+'_Shader'), asShader=True)
                shdSG = cmds.sets(name=(beseMesh+'_ShaderSG'), empty=True, renderable=True, noSurfaceShader=True)
                cmds.connectAttr((shd +'.outColor'), (shdSG +'.surfaceShader'))
            colorID = random.randint(0,(len(score)-1))
            getInfo = score[colorID]

            cmds.setAttr ((beseMesh +'_Shader.color'), getInfo[1][0],getInfo[1][1],getInfo[1][2], type = 'double3' )
            cmds.sets((beseMesh+'_bool'), e=True, forceElement = (beseMesh+'_ShaderSG'))
            cmds.setAttr((beseMesh + '_BoolResult.color'),getInfo[0])


            cmds.setAttr((beseMesh + "BoolGrp.useOutlinerColor"), 1)
            cmds.setAttr((beseMesh + "BoolGrp.outlinerColor"),  getInfo[1][0],getInfo[1][1],getInfo[1][2])


    else:
        cmds.sets((beseMesh+'_bool'), e=True, forceElement = 'initialShadingGroup')
        cmds.setAttr((beseMesh + '_BoolResult.color'),0)
        cmds.setAttr((beseMesh + "BoolGrp.useOutlinerColor"), 0)

def hsv2rgb(h, s, v):
    h, s, v = [float(x) for x in (h, s, v)]
    hi = (h / 60) % 6
    hi = int(round(hi))
    f = (h / 60) - (h / 60)
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    if hi == 0:
        return v, t, p
    elif hi == 1:
        return q, v, p
    elif hi == 2:
        return p, v, t
    elif hi == 3:
        return p, q, v
    elif hi == 4:
        return t, p, v
    elif hi == 5:
        return v, p, q

def toggleLayer():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkState = cmds.iconTextButton('meshLayerButton', q=1, image1= True )
    if checkState == 'nodeGrapherModeSimple.svg':
        cmds.iconTextButton('meshLayerButton', e=1, image1= 'nodeGrapherModeAll.svg')
        BoolGrpList = cmds.ls('*BoolGrp')
        cmds.showHidden(BoolGrpList)
    else:
        cmds.iconTextButton('meshLayerButton', e=1, image1= 'nodeGrapherModeSimple.svg')
        BoolGrpList = cmds.ls('*BoolGrp')
        cmds.hide(BoolGrpList)
        cmds.showHidden(beseMesh+'BoolGrp')

def updateVisLayer():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkState = cmds.iconTextButton('meshLayerButton', q=1, image1= True )
    if checkState == 'nodeGrapherModeSimple.svg':
        BoolGrpList = cmds.ls('*BoolGrp')
        cmds.hide(BoolGrpList)
        cmds.showHidden(beseMesh+'BoolGrp')
    else:
        BoolGrpList = cmds.ls('*BoolGrp')
        cmds.showHidden(BoolGrpList)

def cutterType(boolType):
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkButtonStateList = ['subsButton','unionButton','cutButton']
    for c in checkButtonStateList:
        buttonState = cmds.button( c ,e=1,  bgc = [0.28,0.28,0.28] )
    selCutter = cmds.ls(sl=1, fl=1, type='transform')
    if len(selCutter) > 0:
        selCutterCheck = cmds.ls(sl=1, fl=1, l=1, type='transform')
        for s in selCutterCheck:
            checkShortName = s.split("|")
            shortName = checkShortName[-1]
            cmds.select(s)
            myType = checkInstType()
            if myType[1] != 'new':
                s = myType[0]

            if 'boxCutter' in shortName:
                cmds.setAttr((s+'.cutterOp'),boolType,type="string")
                shapeNode = cmds.listRelatives(s, f = True, shapes=True)
                if boolType == 'union':
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 31)
                elif boolType == 'subs':
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 28)
                elif boolType == 'cut':
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 25)
                fixBoolNodeConnection()

    if boolType == 'union':
        buttonState = cmds.button('unionButton',e=1,  bgc = [0.3,0.5,0.6] )
    elif boolType == 'subs':
        buttonState = cmds.button('subsButton' ,e=1,  bgc = [0.3,0.5,0.6] )
    elif boolType == 'cut':
        buttonState = cmds.button('cutButton' ,e=1,  bgc = [0.3,0.5,0.6] )

def fixBoolNodeConnection():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    transNode = cmds.ls(sl=1,fl=1)
    myType = checkInstType()
    if myType[1] != 'new':
        transNode[0] = myType[0]

    checkNumber = ''.join([n for n in transNode[0].split('|')[-1] if n.isdigit()])
    opType = cmds.getAttr(transNode[0]+'.cutterOp')
    shapeNode = cmds.listRelatives(transNode[0], s=True ,f=True)
    boolNode = ''

    if 'subs' in opType:
        boolNode = beseMesh+'_mySubs'

    elif 'union' in opType:
        boolNode = beseMesh+'_myUnion'

    elif 'cut' in opType:
        boolNode = beseMesh+'_myCut'

    if len(shapeNode)>0:
        listConnect = cmds.connectionInfo((shapeNode[0]+'.outMesh'), dfs=True )
        if len(listConnect)>0:
            for a in listConnect:
                cmds.disconnectAttr((shapeNode[0]+'.outMesh'), a)


    start_index = 0
    while start_index < 1000:
        listConnectMa = cmds.connectionInfo((shapeNode[0]+'.worldMatrix[' + str(start_index) + ']'), dfs=True )
        if len(listConnectMa) > 0:
            for a in listConnectMa:
                try:
                    cmds.disconnectAttr((shapeNode[0]+'.worldMatrix[' + str(start_index) + ']'), a)
                except:
                    pass
        start_index += 1


    cmds.connectAttr( (shapeNode[0]+".outMesh"), ((boolNode+'.inputPoly['+str(checkNumber)+']')),f=True)
    cmds.connectAttr( (shapeNode[0]+".worldMatrix[0]"), ((boolNode+'.inputMat['+str(checkNumber)+']')),f=True)

    if myType[1] != 'new':
        cmds.select(transNode[0]+'*Grp')
        grpName = cmds.ls(sl=True,fl=True)
        transformList = cmds.listRelatives(grpName, c=True)
        cleanList = []
        if  myType[1] == 'radial':
            for t in transformList:
                removeUnwant = t.replace('_Rot','')
                cleanList.append(removeUnwant)
        else:
            cleanList = transformList

        cleanList.remove(transNode[0])

        for i in range(len(cleanList)):
            checkNumber = ''.join([n for n in cleanList[i].split('|')[-1] if n.isdigit()])
            cmds.connectAttr( (shapeNode[0]+".worldMatrix[" + str(int(i)+ int(1)) + "]"), ((boolNode+'.inputMat['+str(checkNumber)+']')),f=True)
            cmds.connectAttr( (shapeNode[0]+".outMesh"), ((boolNode+'.inputPoly['+str(checkNumber)+']')),f=True)

def get_latest_free_multi_index( attr_name, start_index ):
    '''Find the latest unconnected multi index starting at the passed in index.'''
    listCuttersIndex = []
    while start_index < 100:
        if cmds.connectionInfo( '{}[{}]'.format(attr_name,start_index), sfd=True ):
            listCuttersIndex.append(start_index)
        start_index += 1
    nextIndex = (listCuttersIndex[-1]+1)
    return nextIndex

def nextCutterNumber():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    cutterGrpName = beseMesh + '_cutterGrp'
    cmds.select(cutterGrpName,hi=True)
    listAllCutter = cmds.ls('boxCutter*',type = 'transform')
    cmds.select(cl=True)
    checkNumber = 2
    if len(listAllCutter) > 0:
        newList = []
        for l in listAllCutter:
            if 'ArrayGrp' not in l:
                newList.append(l)
            else:
                grpNumber = ''.join([n for n in l.split('|')[-1] if n.isdigit()])
                newList.append(grpNumber)
        checkNumber = ''.join([n for n in newList[-1].split('|')[-1] if n.isdigit()])
        checkNumber = int(checkNumber) + 1
    return checkNumber

def get_latest_free_multi_index( attr_name, start_index ):
    '''Find the latest unconnected multi index starting at the passed in index.'''
    listCuttersIndex = []
    while start_index < 100:
        if cmds.connectionInfo( '{}[{}]'.format(attr_name,start_index), sfd=True ):
            listCuttersIndex.append(start_index)
        start_index += 1
    nextIndex = (listCuttersIndex[-1]+1)
    return nextIndex

def get_next_free_multi_index( attr_name, start_index ):
    '''Find the next unconnected multi index starting at the passed in index.'''
    # assume a max of 100 connections
    while start_index < 100:
        if len( cmds.connectionInfo( '{}[{}]'.format(attr_name,start_index), sfd=True ) or [] ) == 0:
            return start_index
        start_index += 1
    return 0

#################################################################################################
def goDraw():
    hideAllCutter()
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = beseMesh + '_bool'
    cmds.optionVar(iv = ('inViewMessageEnable', 0))
    cmds.makeLive(snapMesh)
    xrayOn()
    cmds.evalDeferred('drawBoxRun()')

def drawBoxRun():
    cmds.setToolTo( "CreatePolyCubeCtx" )
    cmds.scriptJob ( runOnce=True, event = ["PostToolChanged", xrayOff])

def xrayOn():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = beseMesh + '_bool'
    cmds.displaySurface(snapMesh , x =1)

def xrayOff():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = beseMesh + '_bool'
    cmds.displaySurface(snapMesh , x =0)
    cmds.makeLive( none=True )
    newCut = cmds.ls(sl=1,tr=1)
    cmds.select(newCut, r=1)
    cmds.evalDeferred('useOwnCutterShape()')
    newCut = cmds.ls(sl=1,tr=1)
    cmds.setAttr((newCut[0]+".scaleX") ,1.01)
    cmds.setAttr((newCut[0]+".scaleY") ,1.01)
    cmds.setAttr((newCut[0]+".scaleZ") ,1.01)

#####################################################################################################
def rdMirrorCurrentState():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    rdMAxis = ''
    rdMPol = ''
    divSide = 3
    divOffset = 10
    bcv = cmds.button('rMirrorXButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX < 0.27:
        rdMAxis = 'x'
    bcv = cmds.button('rMirrorYButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX < 0.27:
        rdMAxis = 'y'
    bcv = cmds.button('rMirrorZButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX < 0.27:
        rdMAxis = 'z'
    checkV = cmds.button('rMirrorPosButton', q=1 , bgc = 1)
    if checkV[0] > 0.30 :
        rdMPol = 'p'
    checkV = cmds.button('rMirrorNegButton', q=1 , bgc = 1)
    if checkV[0] > 0.30 :
        rdMPol = 'n'
    divSide = cmds.intSliderGrp('rMirrorSideSlider',  q=1 , v = 1)
    divOffset = cmds.intSliderGrp('rMirrorOffsetSlider',  q=1 , v = 1)
    return rdMAxis, rdMPol, divSide, divOffset

def rdMirrorUIUpdate():
    answer = ['','','','']
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists((beseMesh + "_rMirrorGrp")):
        answer[0]= cmds.getAttr(beseMesh + '_rMirrorGrp.rdMAxis')
        answer[1]= cmds.getAttr(beseMesh + '_rMirrorGrp.rdMHalf')
        answer[2]= cmds.getAttr(beseMesh + '_rMirrorGrp.rdMSide')
        answer[3]= cmds.getAttr(beseMesh + '_rMirrorGrp.rdMOffset')
        rdMirrorReset()
        if answer[0] == 'x':
            cmds.button('rMirrorXButton',e=1, bgc =  [0.34, 0.14, 0.14])
        elif answer[0] == 'y':
            cmds.button('rMirrorYButton',e=1, bgc =  [0.14, 0.34, 0.14])
        elif answer[0] == 'z':
            cmds.button('rMirrorZButton',e=1, bgc =  [0.14, 0.14, 0.34])
        if answer[1] == 'p':
            cmds.button('rMirrorPosButton', e=1 , bgc = [0.3, 0.5, 0.6])
        elif answer[1] == 'n':
            cmds.button('rMirrorNegButton', e=1 , bgc = [0.3, 0.5, 0.6])
        cmds.intSliderGrp('rMirrorSideSlider',  e=1 , v = answer[2] )
        cmds.intSliderGrp('rMirrorOffsetSlider',  e=1 , v = answer[3] )
    else:
        rdMirrorReset()

def rdMirrorReset():
    cmds.button('rMirrorXButton',e=1, bgc = [0.28,0.28,0.28])
    cmds.button('rMirrorYButton',e=1, bgc = [0.28,0.28,0.28])
    cmds.button('rMirrorZButton',e=1, bgc = [0.28,0.28,0.28])
    cmds.button('rMirrorNegButton', e=1 , bgc = [0.28,0.28,0.28])
    cmds.button('rMirrorPosButton', e=1 , bgc = [0.28,0.28,0.28])
    cmds.intSliderGrp('rMirrorSideSlider',  e=1 , v = 3)

def rdMirrorOffsetUpdate():
    rMirrorList = cmds.ls('*_rMirrorGrp')
    offsetV = cmds.intSliderGrp('rMirrorOffsetSlider',q=1,v=1)
    for r in rMirrorList:
        cmds.move((-1.0*offsetV), 0, 0 ,r , a=1, os=1, wd=1)
        cmds.setAttr((r + '.rdMOffset'),offsetV)

def rdMirrorOutput():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists((beseMesh + "_rMirrorGrp")):
        insList = cmds.ls((beseMesh + "_ringGrp*"),fl=1)
        cmds.select(beseMesh + "_ringGrp")
        collectList = []
        for i in insList:
            new = cmds.duplicate((beseMesh + "_ringGrp"),rr=1)
            collectList.append(new)
            cmds.select(new,i)
            cmds.matchTransform(pos=1,rot=1)
        cmds.delete(insList)
        cmds.select(beseMesh + "_rMirrorGrp")
        cmds.polyUnite(ch=0, objectPivot=1)
        cmds.rename(beseMesh + "_rMirrorGeo")
        cmds.delete(beseMesh + "_rMirrorGrp")
        cmds.polyMergeVertex(d=0.01, am=1, ch=0)
        cmds.select(beseMesh + "_rMirrorGeo")
        cmds.button('rMirrorPosButton', e=1 ,bgc = [0.28,0.28,0.28])
        cmds.button('rMirrorNegButton', e=1 ,bgc = [0.28,0.28,0.28])
        cmds.button('rMirrorXButton',e=1, bgc = [0.28,0.28,0.28])
        cmds.button('rMirrorYButton',e=1, bgc = [0.28,0.28,0.28])
        cmds.button('rMirrorZButton',e=1, bgc = [0.28,0.28,0.28])
        cmds.intSliderGrp('rMirrorSideSlider',  e=1 , v = 3)

def rdMirrorHalf(side):
    buttonXOn = 1
    buttonYOn = 1
    buttonZOn = 1
    bcv = cmds.button('rMirrorXButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX > 0.27:
        buttonXOn = 0

    bcv = cmds.button('rMirrorYButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX > 0.27:
        buttonYOn = 0

    bcv = cmds.button('rMirrorZButton',q=1, bgc =1)
    totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
    if totalBcVX > 0.27:
        buttonZOn = 0
    if buttonXOn == 0 and buttonYOn == 0 and buttonZOn == 0:
        if cmds.objExists((beseMesh + "_rMirrorGrp")):
            cmds.delete((beseMesh + "_rMirrorGrp"))
    else:
        if side == 'p':
            checkV = cmds.button('rMirrorPosButton', q=1 , bgc = 1)
            if checkV[0] < 0.30 :
                cmds.button('rMirrorPosButton', e=1 , bgc = [0.3, 0.5, 0.6])
            else:
                cmds.button('rMirrorPosButton', e=1 , bgc = [0.28,0.28,0.28])
            cmds.button('rMirrorNegButton', e=1 , bgc = [0.28,0.28,0.28])
        elif side == 'n':
            checkV = cmds.button('rMirrorNegButton', q=1 , bgc = 1)
            if checkV[0] < 0.30 :
                cmds.button('rMirrorNegButton', e=1 , bgc = [0.3, 0.5, 0.6])
            else:
                cmds.button('rMirrorNegButton', e=1 , bgc = [0.28,0.28,0.28])
            cmds.button('rMirrorPosButton', e=1 , bgc = [0.28,0.28,0.28])
        rdMirrorUpdate()

def rdMirror(axis):
    currentSel = cmds.ls(sl=1)
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        divSide =  cmds.intSliderGrp('rMirrorSideSlider',  q=1 , v = 1)
        divAngle = 360.0 /  divSide
        commnadA = ''
        commnadC = ''
        commnadD = ''
        commnadG = ''
        rotV = 90 - (360.0 / divSide / 2)
        createMirror = 1
        halfOn = 0
        checkVP = cmds.button('rMirrorPosButton', q=1 , bgc = 1)
        checkVN = cmds.button('rMirrorNegButton', q=1 , bgc = 1)
        if (checkVP[1]+ checkVN[1]) > 0.57:
            halfOn = 1

        buttonXOn = 1
        buttonYOn = 1
        buttonZOn = 1
        bcv = cmds.button('rMirrorXButton',q=1, bgc =1)
        totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
        if totalBcVX > 0.27:
            buttonXOn = 0

        bcv = cmds.button('rMirrorYButton',q=1, bgc =1)
        totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
        if totalBcVX > 0.27:
            buttonYOn = 0

        bcv = cmds.button('rMirrorZButton',q=1, bgc =1)
        totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
        if totalBcVX > 0.27:
            buttonZOn = 0
        if buttonXOn == 0 and buttonYOn == 0 and buttonZOn == 0:
            if cmds.objExists((beseMesh + "_rMirrorGrp")):
                cmds.delete((beseMesh + "_rMirrorGrp"))

        if axis == 'x':
            if buttonXOn == 1:
                if cmds.objExists((beseMesh + "_rMirrorGrp")):
                    cmds.delete((beseMesh + "_rMirrorGrp"))
                cmds.button('rMirrorXButton',e=1, bgc = [0.28,0.28,0.28])
                createMirror = 0
            else:
                if buttonYOn == 1 or buttonZOn == 1:
                    if cmds.objExists((beseMesh + "_rMirrorGrp")):
                        cmds.delete((beseMesh + "_rMirrorGrp"))
                commnadA = 'polyMirrorCut 0.001 0 1;'
                commnadC = 'rotate -r  ' + str(divAngle) +  ' 0 0;'

                if halfOn == 1:
                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(90) + ');'

                else:
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                cmds.button('rMirrorXButton',e=1, bgc = [0.34, 0.14, 0.14])
                cmds.button('rMirrorYButton',e=1, bgc = [0.28,0.28,0.28])
                cmds.button('rMirrorZButton',e=1, bgc = [0.28,0.28,0.28])

        elif axis == 'y':
            if buttonYOn == 1:
                if cmds.objExists((beseMesh + "_rMirrorGrp")):
                    cmds.delete((beseMesh + "_rMirrorGrp"))
                cmds.button('rMirrorYButton',e=1, bgc = [0.28,0.28,0.28])
                createMirror = 0
            else:
                if buttonXOn == 1 or buttonZOn == 1:
                    if cmds.objExists((beseMesh + "_rMirrorGrp")):
                        cmds.delete((beseMesh + "_rMirrorGrp"))
                commnadA = 'polyMirrorCut 0 0.001 1;'
                commnadC = 'rotate -r  0 ' + str(divAngle) +  ' 0;'
                if halfOn == 1:
                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(90) + ');'
                else:
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(rotV) + ');'
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(rotV) + ');'
                cmds.button('rMirrorXButton',e=1, bgc = [0.28,0.28,0.28])
                cmds.button('rMirrorYButton',e=1, bgc = [0.14, 0.34, 0.14])
                cmds.button('rMirrorZButton',e=1, bgc = [0.28,0.28,0.28])
        else:
            if buttonZOn == 1:
                if cmds.objExists((beseMesh + "_rMirrorGrp")):
                    cmds.delete((beseMesh + "_rMirrorGrp"))
                cmds.button('rMirrorZButton',e=1, bgc = [0.28,0.28,0.28])
                createMirror = 0
            else:
                if buttonXOn == 1 or buttonYOn == 1:
                    if cmds.objExists((beseMesh + "_rMirrorGrp")):
                        cmds.delete((beseMesh + "_rMirrorGrp"))

                commnadA = 'polyMirrorCut 1 0 0.001;'
                commnadC = 'rotate -r 0 0 ' + str(divAngle) +  ';'

                if halfOn == 1:

                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(90) + ');'
                else:
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                cmds.button('rMirrorXButton',e=1, bgc = [0.28,0.28,0.28])
                cmds.button('rMirrorYButton',e=1, bgc = [0.28,0.28,0.28])
                cmds.button('rMirrorZButton',e=1, bgc = [0.14, 0.14, 0.34])

        if createMirror == 1:
            rmSource = beseMesh+ '_bool'
            newRing = cmds.duplicate(rmSource)
            cmds.rename(newRing , (beseMesh + '_ringGeo'))
            cmds.connectAttr( (rmSource+'Shape.outMesh') ,(beseMesh + '_ringGeoShape.inMesh'),f=1)
            cmds.select(beseMesh + '_ringGeo')
            mel.eval(commnadA)
            cmds.rename(beseMesh + '_cutPlaneA')
            cmds.select((beseMesh + '_ringGeo'),add=1)
            cmds.matchTransform(pos=1)
            list = cmds.listConnections((beseMesh + '_cutPlaneA'),t= "transform")
            cmds.delete(list[0])
            mel.eval(commnadD)
            cmds.select(beseMesh + '_ringGeo')
            mel.eval(commnadA)
            cmds.rename(beseMesh + '_cutPlaneB')
            cmds.select((beseMesh + '_ringGeo'),add=1)
            cmds.matchTransform(pos=1)
            mel.eval(commnadG)
            list = cmds.listConnections((beseMesh + '_cutPlaneB'),t= "transform")

            if halfOn == 1:
                cmds.rename(list[0], (beseMesh + '_ringGeoMirror'))
                cmds.group((beseMesh + '_ringGeo'),(beseMesh + '_ringGeoMirror'))
            else:
                cmds.delete(list[0])
                cmds.group((beseMesh + '_ringGeo'))
            cmds.rename(beseMesh + '_ringGrp')
            getTrans = cmds.xform((beseMesh + '_cutPlaneA'), q=1, piv=1, a=1, ws=1)
            cmds.move(getTrans[0], getTrans[1], getTrans[2],(beseMesh + '_ringGrp.scalePivot'), (beseMesh + '_ringGrp.rotatePivot'), a=1, ws=1)
            cmds.instance()
            mel.eval(commnadC)
            for i in range(divSide-2):
                cmds.instance(st=1)
            cmds.group((beseMesh + '_cutPlane*'),(beseMesh + '_ringGrp*'))
            cmds.rename(beseMesh + "_rMirrorGrp")
            offsetV = cmds.intSliderGrp('rMirrorOffsetSlider',q=1,v=1)
            cmds.move((-1.0*offsetV), 0, 0 ,r=1, os=1, wd=1)
            cmds.setAttr((beseMesh + '_cutPlaneA.visibility'),0)
            cmds.setAttr((beseMesh + '_cutPlaneB.visibility'),0)
            cmds.parent((beseMesh + "_rMirrorGrp"),(beseMesh + "BoolGrp"))
            cmds.select(d=1)
            if not cmds.attributeQuery('rdMAxis', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                cmds.addAttr((beseMesh + '_rMirrorGrp'), ln='rdMAxis' ,dt= 'string')
            if not cmds.attributeQuery('rdMHalf', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                cmds.addAttr((beseMesh + '_rMirrorGrp'), ln='rdMHalf' ,dt= 'string')
            if not cmds.attributeQuery('rdMSide', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                cmds.addAttr((beseMesh + '_rMirrorGrp'),at='long' , dv = 0 ,ln='rdMSide')
            if not cmds.attributeQuery('rdMOffset', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                cmds.addAttr((beseMesh + '_rMirrorGrp'),at='long' , dv = 0 ,ln='rdMOffset')
            answer = rdMirrorCurrentState()
            cmds.setAttr((beseMesh + '_rMirrorGrp.rdMAxis'), answer[0], type="string")
            cmds.setAttr((beseMesh + '_rMirrorGrp.rdMHalf'), answer[1], type="string")
            cmds.setAttr((beseMesh + '_rMirrorGrp.rdMSide'), answer[2])
            cmds.setAttr((beseMesh + '_rMirrorGrp.rdMOffset'), answer[3])
        else:
            rdMirrorReset()
        if currentSel:
            cmds.select(currentSel)
            cmds.MoveTool()

def rdMirrorUpdate():
    currentSel = cmds.ls(sl=1)
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if len(beseMesh) > 0:
        if cmds.objExists((beseMesh + "_rMirrorGrp")):
            divSide =  cmds.intSliderGrp('rMirrorSideSlider',  q=1 , v = 1)
            divAngle = 360.0 /  divSide
            commnadA = ''
            commnadC = ''
            commnadD = ''
            commnadG = ''
            rotV = 90 - (360.0 / divSide / 2)
            createMirror = 1
            halfOn = 0
            checkVP = cmds.button('rMirrorPosButton', q=1 , bgc = 1)
            checkVN = cmds.button('rMirrorNegButton', q=1 , bgc = 1)
            if (checkVP[1]+ checkVN[1]) > 0.57:
                halfOn = 1
            buttonXOn = 1
            buttonYOn = 1
            buttonZOn = 1
            bcv = cmds.button('rMirrorXButton',q=1, bgc =1)
            totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
            if totalBcVX > 0.27:
                buttonXOn = 0
            bcv = cmds.button('rMirrorYButton',q=1, bgc =1)
            totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
            if totalBcVX > 0.27:
                buttonYOn = 0
            bcv = cmds.button('rMirrorZButton',q=1, bgc =1)
            totalBcVX = (bcv[0]+ bcv[1]+ bcv[2])/3
            if totalBcVX > 0.27:
                buttonZOn = 0
            if buttonXOn == 1 or buttonYOn == 1 or buttonZOn == 1:
                if cmds.objExists((beseMesh + "_rMirrorGrp")):
                    cmds.delete((beseMesh + "_rMirrorGrp"))
            if buttonXOn == 1:
                commnadA = 'polyMirrorCut 0.001 0 1;'
                commnadC = 'rotate -r  ' + str(divAngle) +  ' 0 0;'
                if halfOn == 1:
                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(90) + ');'
                else:
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
            elif buttonYOn == 1:
                commnadA = 'polyMirrorCut 0 0.001 1;'
                commnadC = 'rotate -r  0 ' + str(divAngle) +  ' 0;'
                if halfOn == 1:
                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(90) + ');'
                else:
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateY (' + str(rotV) + ');'
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateY (-1.0 * ' + str(rotV) + ');'

            elif buttonZOn == 1:
                commnadA = 'polyMirrorCut 1 0 0.001;'
                commnadC = 'rotate -r 0 0 ' + str(divAngle) +  ';'
                if halfOn == 1:
                    if checkVP[1] > 0.30:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(90) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    else:
                        commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'
                        commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(90) + ');'
                else:
                    commnadD = 'setAttr '  + beseMesh + '_cutPlaneA.rotateX (-1.0 * ' + str(rotV) + ');'
                    commnadG = 'setAttr '  + beseMesh + '_cutPlaneB.rotateX (' + str(rotV) + ');'


            if createMirror == 1:
                rmSource = beseMesh+ '_bool'
                newRing = cmds.duplicate(rmSource)
                cmds.rename(newRing , (beseMesh + '_ringGeo'))
                cmds.connectAttr( (rmSource+'Shape.outMesh') ,(beseMesh + '_ringGeoShape.inMesh'),f=1)
                cmds.select(beseMesh + '_ringGeo')
                mel.eval(commnadA)
                cmds.rename(beseMesh + '_cutPlaneA')
                cmds.select((beseMesh + '_ringGeo'),add=1)
                cmds.matchTransform(pos=1)
                list = cmds.listConnections((beseMesh + '_cutPlaneA'),t= "transform")
                cmds.delete(list[0])
                mel.eval(commnadD)
                cmds.select(beseMesh + '_ringGeo')
                mel.eval(commnadA)
                cmds.rename(beseMesh + '_cutPlaneB')
                cmds.select((beseMesh + '_ringGeo'),add=1)
                cmds.matchTransform(pos=1)
                mel.eval(commnadG)
                list = cmds.listConnections((beseMesh + '_cutPlaneB'),t= "transform")

                if halfOn == 1:
                    cmds.rename(list[0], (beseMesh + '_ringGeoMirror'))
                    cmds.group((beseMesh + '_ringGeo'),(beseMesh + '_ringGeoMirror'))
                else:
                    cmds.delete(list[0])
                    cmds.group((beseMesh + '_ringGeo'))
                cmds.rename(beseMesh + '_ringGrp')
                getTrans = cmds.xform((beseMesh + '_cutPlaneA'), q=1, piv=1, a=1, ws=1)
                cmds.move(getTrans[0], getTrans[1], getTrans[2],(beseMesh + '_ringGrp.scalePivot'), (beseMesh + '_ringGrp.rotatePivot'), a=1, ws=1)
                cmds.instance()
                mel.eval(commnadC)
                for i in range(divSide-2):
                    cmds.instance(st=1)
                cmds.group((beseMesh + '_cutPlane*'),(beseMesh + '_ringGrp*'))
                cmds.rename(beseMesh + "_rMirrorGrp")
                offsetV = cmds.intSliderGrp('rMirrorOffsetSlider',q=1,v=1)
                cmds.move((-1.0*offsetV), 0, 0 ,r=1, os=1, wd=1)
                cmds.setAttr((beseMesh + '_cutPlaneA.visibility'),0)
                cmds.setAttr((beseMesh + '_cutPlaneB.visibility'),0)
                cmds.parent((beseMesh + "_rMirrorGrp"),(beseMesh + "BoolGrp"))
                cmds.select(d=1)
                if not cmds.attributeQuery('rdMAxis', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                    cmds.addAttr((beseMesh + '_rMirrorGrp'), ln='rdMAxis' ,dt= 'string')
                if not cmds.attributeQuery('rdMHalf', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                    cmds.addAttr((beseMesh + '_rMirrorGrp'), ln='rdMHalf' ,dt= 'string')
                if not cmds.attributeQuery('rdMSide', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                    cmds.addAttr((beseMesh + '_rMirrorGrp'),at='long' , dv = 0 ,ln='rdMSide')
                if not cmds.attributeQuery('rdMOffset', node = (beseMesh + '_rMirrorGrp'), ex=True ):
                    cmds.addAttr((beseMesh + '_rMirrorGrp'),at='long' , dv = 0 ,ln='rdMOffset')
                answer = rdMirrorCurrentState()
                cmds.setAttr((beseMesh + '_rMirrorGrp.rdMAxis'), answer[0], type="string")
                cmds.setAttr((beseMesh + '_rMirrorGrp.rdMHalf'), answer[1], type="string")
                cmds.setAttr((beseMesh + '_rMirrorGrp.rdMSide'), answer[2])
                cmds.setAttr((beseMesh + '_rMirrorGrp.rdMOffset'), answer[3])
            else:
                rdMirrorReset()

            if currentSel:
                cmds.select(currentSel)
                cmds.MoveTool()

#####################################################################################################
def symmetryCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    getSymX = 0
    getSymY = 0
    getSymZ = 0

    cmds.setAttr((beseMesh+'.visibility'), 1)
    mirrorPivot = cmds.objectCenter(beseMesh, gl=True)
    cmds.setAttr((beseMesh+'.visibility'), 0)

    if cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
        getSymX =  cmds.getAttr(beseMesh+'.symmetryX')
    if cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
        getSymY =  cmds.getAttr(beseMesh+'.symmetryY')
    if cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
        getSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')

    if getSymX != 0 or getSymY != 0 or getSymZ != 0:
        #mirror all cutter
        cmds.select((beseMesh+'_bakeStep'), hi=True)
        cmds.select((beseMesh+'_bakeStep'),d=True)
        cmds.select((beseMesh+'_bakeBaseMesh'),d=True)
        restoreCutter = cmds.ls(sl=1,fl=1,type='transform')
        for r in restoreCutter:
            if getSymX == 1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 0 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
            elif  getSymX == -1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 0 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =1, p = mirrorPivot)

            if getSymY == 1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 1 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
            elif  getSymY == -1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 1 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =1, p = mirrorPivot)

            if getSymZ == 1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 2 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
            elif  getSymZ == -1:
                cmds.polyMirrorFace(r, cutMesh = 1, axis = 2 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)

def fadeOutCage():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists(beseMesh+'_cageGrp'):
        cmds.setAttr((beseMesh+'_cageGrp.visibility'),1)
        storeCurrent = cmds.floatSlider('CageTransparentSlider',q=1 ,value=True)
        val = storeCurrent
        i = 0.005
        while val < 1:
            i += 0.005
            val = 0.5 + i
            cmds.setAttr("CageShader.transparencyB", val)
            cmds.setAttr("CageShader.transparencyR", val)
            cmds.setAttr("CageShader.transparencyG", val)
            cmds.refresh(cv=True,f=True)

        cmds.setAttr((beseMesh+'_cageGrp.visibility'),0)
        cmds.setAttr("CageShader.transparencyB", storeCurrent)
        cmds.setAttr("CageShader.transparencyR", storeCurrent)
        cmds.setAttr("CageShader.transparencyG", storeCurrent)

def updateCageColor():
    if cmds.objExists('CageShader'):
        checkColor = cmds.colorSliderGrp('CageColorSlider', q=True, rgb=True )
        cmds.setAttr('CageShader.color', checkColor[0], checkColor[1], checkColor[2] , type= 'double3')

def updateCageTransparent():
    if cmds.objExists('CageShader'):
        checkTransp = 0
        checkTransp = cmds.floatSlider('CageTransparentSlider',q=True, value=True)
        cmds.setAttr('CageShader.transparency', checkTransp, checkTransp, checkTransp, type= 'double3')

def cageVisToggle():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    listAllCageGrps = cmds.ls('*_cageGrp')
    if cmds.objExists(beseMesh+'_cageGrp'):
        checkState = cmds.getAttr(beseMesh+'_cageGrp.visibility')
        cmds.hide(listAllCageGrps)
        if checkState == 0:
            cmds.setAttr((beseMesh+'_cageGrp.visibility'),1)
        else:
            cmds.setAttr((beseMesh+'_cageGrp.visibility'),0)
    else:
        cmds.hide(listAllCageGrps)

def boolSymmetryCage():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists(beseMesh +'_cageGrp'):
        cmds.delete(beseMesh +'_cageGrp')
    if cmds.objExists(beseMesh +'_cageA*'):
        cmds.delete(beseMesh +'_cageA*')
    tempLattice = cmds.lattice(beseMesh,divisions =(2, 2, 2), objectCentered = True, ldv = (2, 2 ,2))
    BBcenter = cmds.xform(tempLattice[1],q =True, t=True)
    BBrotate = cmds.xform(tempLattice[1],q =True, ro=True)
    BBscale  = cmds.xform(tempLattice[1],q =True, r=True, s=True)
    BBcube = cmds.polyCube(w =1, h =1, d =1, sx= 1, sy= 1, sz= 1, ax= (0, 1, 0), ch = 0)
    cmds.xform(BBcube[0], t = (BBcenter[0], BBcenter[1],BBcenter[2]))
    cmds.xform(BBcube[0], ro = (BBrotate[0], BBrotate[1],BBrotate[2]))
    cmds.xform(BBcube[0], s = (BBscale[0], BBscale[1],BBscale[2]))
    cmds.delete(tempLattice)
    cmds.rename(BBcube[0],(beseMesh+'_cageA'))
    cmds.setAttr((beseMesh+'.visibility'), 1)
    mirrorPivot = cmds.objectCenter(beseMesh, gl=True)
    cmds.setAttr((beseMesh+'.visibility'), 0)
    cutDir = {'X','Y','Z'}
    for c in cutDir:
        cutPlane= cmds.polyCut((beseMesh + '_cageA'), ws = True, cd = c , df = True , ch =True)
        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterX'), mirrorPivot[0])
        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterY'), mirrorPivot[1])
        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterZ'), mirrorPivot[2])
    cmds.DeleteHistory(beseMesh + '_cageA')
    cmds.move(mirrorPivot[0],mirrorPivot[1],mirrorPivot[2], (beseMesh + '_cageA.scalePivot'),(beseMesh + '_cageA.rotatePivot'), absolute=True)
    cmds.makeIdentity((beseMesh + '_cageA'),apply= True, t= 1, r =1, s =1, n= 0,pn=1)
    cmds.setAttr((beseMesh + '_cageA.scaleX'), 1.01)
    cmds.setAttr((beseMesh + '_cageA.scaleY'), 1.01)
    cmds.setAttr((beseMesh + '_cageA.scaleZ'), 1.01)
    cmds.setAttr((beseMesh + '_cageA.visibility'), 0)
    cmds.setAttr((beseMesh + '_cageAShape.castsShadows'), 0)
    cmds.setAttr((beseMesh + '_cageAShape.receiveShadows'), 0)
    cmds.makeIdentity((beseMesh + '_cageA'),apply= True, t= 1, r =1, s =1, n= 0,pn=1)
    if not cmds.objExists('CageShader'):
        lambertNode = cmds.shadingNode("lambert", asShader=1)
        cmds.rename(lambertNode,('CageShader'))
        sgNode = cmds.sets(renderable=1, noSurfaceShader=1, empty=1, name= 'CageShaderSG')
        cmds.connectAttr('CageShader.color', sgNode+".surfaceShader",f=1)
        cmds.connectControl( 'CageColorSlider', 'CageShader.color')
        cmds.colorSliderGrp('CageColorSlider', e=True, rgb=(0.5, 0, 0))
    cageColor = cmds.colorSliderGrp('CageColorSlider', q=True, rgb=True)
    cageTrans = cmds.floatSlider('CageTransparentSlider', q=True, value = True)
    cmds.setAttr('CageShader.transparency', cageTrans,cageTrans,cageTrans, type= 'double3')
    cmds.setAttr('CageShader.color',  cageColor[0],cageColor[1],cageColor[2], type= 'double3')
    cmds.sets((beseMesh +'_cageA'), e=1, fe= 'CageShaderSG')
    cmds.modelEditor('modelPanel4', e=True, udm=False )
    cmds.CreateEmptyGroup()
    cmds.rename((beseMesh +'_cageGrp'))
    cmds.parent((beseMesh +'_cageA'), (beseMesh +'_cageGrp'))
    cmds.parent((beseMesh +'_cageGrp'), (beseMesh +'BoolGrp'))
    if not cmds.objExists('BoolSymmetryCage'):
        cmds.createDisplayLayer(name = ('BoolSymmetryCage'))
    cmds.editDisplayLayerMembers( ('BoolSymmetryCage'),(beseMesh +'_cageGrp'))
    cmds.setAttr(('BoolSymmetryCage.displayType'),2)

    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleX'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleY'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleZ'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleX'), -1)
    cmds.setAttr((newNode[0]+'.scaleY'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleX'), -1)
    cmds.setAttr((newNode[0]+'.scaleZ'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleY'), -1)
    cmds.setAttr((newNode[0]+'.scaleZ'), -1)
    newNode = cmds.duplicate((beseMesh + '_cageA'),rr=True)
    cmds.setAttr((newNode[0]+'.scaleX'), -1)
    cmds.setAttr((newNode[0]+'.scaleY'), -1)
    cmds.setAttr((newNode[0]+'.scaleZ'), -1)


    if cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
        getSymX =  cmds.getAttr(beseMesh+'.symmetryX')
    if cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
        getSymY =  cmds.getAttr(beseMesh+'.symmetryY')
    if cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
        getSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')

    if getSymX != 0 or getSymY != 0 or getSymZ != 0:
        cageList = cmds.ls((beseMesh + '_cageA*'),type='transform')

        if getSymX == 1:
            for c in cageList:
                checkX = cmds.getAttr(c+'.scaleX')
                if checkX == -1:
                    cmds.setAttr((c+'.visibility'),1)


        elif getSymX == -1:
            for c in cageList:
                checkX = cmds.getAttr(c+'.scaleX')
                if checkX == 1:
                    cmds.setAttr((c+'.visibility'),1)


        if getSymY == 1:
            for c in cageList:
                checkY = cmds.getAttr(c+'.scaleY')
                if checkY == -1:
                    cmds.setAttr((c+'.visibility'),1)


        elif getSymY == -1:
            for c in cageList:
                checkY = cmds.getAttr(c+'.scaleY')
                if checkY == 1:
                    cmds.setAttr((c+'.visibility'),1)

        if getSymZ == 1:
            for c in cageList:
                checkY = cmds.getAttr(c+'.scaleZ')
                if checkY == -1:
                    cmds.setAttr((c+'.visibility'),1)


        elif getSymZ == -1:
            for c in cageList:
                checkY = cmds.getAttr(c+'.scaleZ')
                if checkY == 1:
                    cmds.setAttr((c+'.visibility'),1)
    cmds.select(cl=True)

def boolSymmetryReset():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    symmNode = cmds.listConnections(cmds.listHistory((beseMesh+'_bool'),af=1),type='polyMirror')
    if symmNode != None :
        if len(symmNode)>0:
            cmds.delete(symmNode)

    resetBoolSymmetryUI()
    if cmds.objExists(beseMesh +'_cageGrp'):
        cmds.delete(beseMesh +'_cageGrp')

def resetBoolSymmetryUI():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)

    if not cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryX', at = "long" )
    cmds.setAttr((beseMesh+'.symmetryX'),0)
    if not cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryY', at = "long" )
    cmds.setAttr((beseMesh+'.symmetryY'),0)
    if not cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryZ', at = "long" )
    cmds.setAttr((beseMesh+'.symmetryZ'),0)
    cmds.button('symmXButtonP',e=True, bgc = [0.14, 0.14, 0.14])
    cmds.button('symmYButtonP',e=True, bgc = [0.14, 0.14, 0.14])
    cmds.button('symmZButtonP',e=True, bgc = [0.14, 0.14, 0.14])
    cmds.button('symmXButtonN',e=True, bgc = [0.14, 0.14, 0.14])
    cmds.button('symmYButtonN',e=True, bgc = [0.14, 0.14, 0.14])
    cmds.button('symmZButtonN',e=True, bgc = [0.14, 0.14, 0.14])

def boolSymmetryFreeze():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    symmNode = cmds.listConnections(cmds.listHistory((beseMesh+'_bool'),af=1),type='polyMirror')
    if symmNode != None  and len(symmNode)>0:
        bakeCutter('all')
        symmetryCutter()
        symmetryBase()
        cmds.select(cl=True)
        restoreCutter()
        resetBoolSymmetryUI()
        if cmds.objExists(beseMesh +'_cageGrp'):
            cmds.delete(beseMesh +'_cageGrp')

def symmetryBase():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    getSymX = 0
    getSymY = 0
    getSymZ = 0

    cmds.setAttr((beseMesh+'.visibility'), 1)
    mirrorPivot = cmds.objectCenter(beseMesh, gl=True)
    cmds.setAttr((beseMesh+'.visibility'), 0)


    if cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
        getSymX =  cmds.getAttr(beseMesh+'.symmetryX')
    if cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
        getSymY =  cmds.getAttr(beseMesh+'.symmetryY')
    if cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
        getSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')

    if getSymX != 0 or getSymY != 0 or getSymZ != 0:
        if getSymX == 1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 0 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
        elif  getSymX == -1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 0 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =1, p = mirrorPivot)

        if getSymY == 1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 1 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
        elif  getSymY == -1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 1 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =1, p = mirrorPivot)

        if getSymZ == 1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 2 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
        elif  getSymZ == -1:
            cmds.polyMirrorFace(beseMesh, cutMesh = 1, axis = 2 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1,  ws =1, p = mirrorPivot)
        cmds.DeleteHistory()

def boolSymmetry(axis,dir):
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selPoly = beseMesh+'_bool'

    if not cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryX', at = "long" )
        cmds.setAttr((beseMesh+'.symmetryX'),0)
    if not cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryY', at = "long" )
        cmds.setAttr((beseMesh+'.symmetryY'),0)
    if not cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
        cmds.addAttr(beseMesh, ln='symmetryZ', at = "long" )
        cmds.setAttr((beseMesh+'.symmetryZ'),0)

    cmds.setAttr((beseMesh+'.visibility'), 1)
    mirrorPivot = cmds.objectCenter(beseMesh, gl=True)
    cmds.setAttr((beseMesh+'.visibility'), 0)


    mirrorName = []
    checkSymm = 0
    symmNode = cmds.listConnections(cmds.listHistory((selPoly),af=1),type='polyMirror')
    if axis == 'x' :
        checkDirState=[]
        if symmNode != None:
            for s in symmNode:
                if 'symmetryX' in s:
                    checkSymm = 1
                    checkDirState = s
        if checkSymm == 0:
            if dir == 1:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 0 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryX'),1)
                cmds.button('symmXButtonP',e=True, bgc = [0.34, 0.14, 0.14])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryXP'))
            else:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 0 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryX'),-1)
                cmds.button('symmXButtonN',e=True, bgc = [0.34, 0.14, 0.14])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryXN'))
        else:
            if cmds.objExists((beseMesh +'_symmetryXP')):
                cmds.delete(beseMesh + '_symmetryXP')
            if cmds.objExists((beseMesh +'_symmetryXN')):
                cmds.delete(beseMesh + '_symmetryXN')
            cmds.button('symmXButtonP',e=True, bgc = [0.28,0.28,0.28])
            cmds.button('symmXButtonN',e=True, bgc = [0.28,0.28,0.28])
            if dir == 1:
                if checkDirState == (beseMesh + '_symmetryXP'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryX'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 0 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryX'),1)
                    cmds.button('symmXButtonP',e=True, bgc = [0.34, 0.14, 0.14])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryXP'))
            else:
                if checkDirState == (beseMesh + '_symmetryXN'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryX'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 0 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryX'),-1)
                    cmds.button('symmXButtonN',e=True, bgc = [0.34, 0.14, 0.14])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryXN'))




    elif axis == 'y' :
        checkDirState=[]
        if symmNode != None:
            for s in symmNode:
                if 'symmetryY' in s:
                    checkSymm = 1
                    checkDirState = s
        if checkSymm == 0:
            if dir == 1:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 1 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryY'),1)
                cmds.button('symmYButtonP',e=True, bgc = [0.14, 0.34, 0.14])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryYP'))
            else:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 1 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryY'),-1)
                cmds.button('symmYButtonN',e=True, bgc = [0.14, 0.34, 0.14])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryYN'))


        else:
            if cmds.objExists((beseMesh +'_symmetryYP')):
                cmds.delete(beseMesh + '_symmetryYP')
            if cmds.objExists((beseMesh +'_symmetryYN')):
                cmds.delete(beseMesh + '_symmetryYN')
            cmds.button('symmYButtonP',e=True, bgc = [0.28,0.28,0.28])
            cmds.button('symmYButtonN',e=True, bgc = [0.28,0.28,0.28])
            if dir == 1:
                if checkDirState == (beseMesh + '_symmetryYP'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryY'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 1 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryY'),1)
                    cmds.button('symmYButtonP',e=True, bgc = [0.14, 0.34, 0.14])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryYP'))
            else:
                if checkDirState == (beseMesh + '_symmetryYN'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryY'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 1 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryY'),-1)
                    cmds.button('symmYButtonN',e=True, bgc = [0.14, 0.34, 0.14])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryYN'))


    else:
        checkDirState=[]
        if symmNode != None:
            for s in symmNode:
                if 'symmetryZ' in s:
                    checkSymm = 1
                    checkDirState = s
        if checkSymm == 0:
            if dir == 1:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 2 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryZ'),1)
                cmds.button('symmZButtonP',e=True, bgc = [0.14, 0.14, 0.34])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryZP'))
            else:
                mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 2 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                cmds.setAttr((beseMesh+'.symmetryZ'),-1)
                cmds.button('symmZButtonN',e=True, bgc = [0.14, 0.14, 0.34])
                cmds.rename(mirrorName[0],(beseMesh + '_symmetryZN'))

        else:
            if cmds.objExists((beseMesh +'_symmetryZP')):
                cmds.delete(beseMesh + '_symmetryZP')
            if cmds.objExists((beseMesh +'_symmetryZN')):
                cmds.delete(beseMesh + '_symmetryZN')
            cmds.button('symmZButtonP',e=True, bgc = [0.28,0.28,0.28])
            cmds.button('symmZButtonN',e=True, bgc = [0.28,0.28,0.28])
            if dir == 1:
                if checkDirState == (beseMesh + '_symmetryZP'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryZ'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 2 , axisDirection = 1 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryZ'),1)
                    cmds.button('symmZButtonP',e=True, bgc = [0.14, 0.14, 0.34])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryZP'))
            else:
                if checkDirState == (beseMesh + '_symmetryZN'):# same button press, remove it
                    cmds.setAttr((beseMesh+'.symmetryZ'),0)
                else:
                    mirrorName = cmds.polyMirrorFace(selPoly, cutMesh = 1, axis = 2 , axisDirection = 0 , mergeMode = 1 , mergeThresholdType = 0 , mergeThreshold = 0.001 , mirrorAxis = 2, mirrorPosition= 0, smoothingAngle = 30, flipUVs = 0, ch=1, ws =True, p = mirrorPivot)
                    cmds.setAttr((beseMesh+'.symmetryZ'),-1)
                    cmds.button('symmZButtonN',e=True, bgc = [0.14, 0.14, 0.34])
                    cmds.rename(mirrorName[0],(beseMesh + '_symmetryZN'))


    boolSymmetryCage()

def loadSymmetryState():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    symmNode = cmds.listConnections(cmds.listHistory((beseMesh+'_bool'),af=1),type='polyMirror')
    cmds.button('symmXButtonP',e=True, bgc = [0.28, 0.28, 0.28])
    cmds.button('symmYButtonP',e=True, bgc = [0.28, 0.28, 0.28])
    cmds.button('symmZButtonP',e=True, bgc = [0.28, 0.28, 0.28])
    cmds.button('symmXButtonN',e=True, bgc = [0.28, 0.28, 0.28])
    cmds.button('symmYButtonN',e=True, bgc = [0.28, 0.28, 0.28])
    cmds.button('symmZButtonN',e=True, bgc = [0.28, 0.28, 0.28])

    checkState = 0
    if symmNode != None:
        for s in symmNode:
            if 'symmetryXP' in s :
                cmds.button('symmXButtonP',e=True, bgc = [0.34, 0.14, 0.14])
                checkState = 1
            elif  'symmetryXN' in s :
                cmds.button('symmXButtonN',e=True, bgc = [0.34, 0.14, 0.14])
                checkState = 1
            elif  'symmetryYP' in s :
                cmds.button('symmYButtonP',e=True, bgc = [0.14, 0.34, 0.14])
                checkState = 1
            elif  'symmetryYN' in s :
                cmds.button('symmYButtonN',e=True, bgc = [0.14, 0.34, 0.14])
                checkState = 1
            elif  'symmetryZP' in s :
                cmds.button('symmZButtonP',e=True, bgc = [0.14, 0.14, 0.34])
                checkState = 1
            elif  'symmetryZN' in s :
                cmds.button('symmZButtonN',e=True, bgc = [0.14, 0.14, 0.34])
                checkState = 1

def screenRes():
    windowUnder = cmds.getPanel(withFocus=True)
    if 'modelPanel' not in windowUnder:
        windowUnder = 'modelPanel4'
    viewNow = omui.M3dView()
    omui.M3dView.getM3dViewFromModelEditor(windowUnder, viewNow)
    screenW = omui.M3dView.portWidth(viewNow)
    screenH = omui.M3dView.portHeight(viewNow)
    return screenW,screenH

def worldSpaceToImageSpace(cameraName, worldPoint):
    resWidth,resHeight = screenRes()
    selList = om.MSelectionList()
    selList.add(cameraName)
    dagPath = om.MDagPath()
    selList.getDagPath(0,dagPath)
    dagPath.extendToShape()
    camInvMtx = dagPath.inclusiveMatrix().inverse()
    fnCam = om.MFnCamera(dagPath)
    mFloatMtx = fnCam.projectionMatrix()
    projMtx = om.MMatrix(mFloatMtx.matrix)
    mPoint = om.MPoint(worldPoint[0],worldPoint[1],worldPoint[2]) * camInvMtx * projMtx;
    x = (mPoint[0] / mPoint[3] / 2 + .5) * resWidth
    y = (mPoint[1] / mPoint[3] / 2 + .5) * resHeight

    return [x,y]

def evenObjLineUp(dir):
    lineupList = cmds.ls(sl=1,fl=1)
    #collect 2d posision
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
    dataX = {}
    dataY = {}
    for l in lineupList:
        bbox = cmds.xform(l, q=True, ws=True, piv=True)
        pos2D = worldSpaceToImageSpace(cameraTrans[0],(bbox[0],bbox[1],bbox[2]))
        dataX.update( {l : pos2D[0]} )
        dataY.update( {l : pos2D[1]} )

    if dir == 'x' :
        score = OrderedDict(sorted(dataX.items(), key = lambda fd: fd[1],reverse = False))
    else:
        score = OrderedDict(sorted(dataY.items(), key = lambda fd: fd[1],reverse = False))

    #use fd[0] to get name order, fd[1] to get key order
    orderList = []
    for key in score:
        orderList.append(key)
    # get distanceGap
    posStart = cmds.xform(orderList[0], q=True, ws=True, piv=True)
    posEnd = cmds.xform(orderList[-1], q=True, ws=True, piv=True)
    gapX = (posEnd[0] - posStart[0]) / (len(orderList) - 1)
    gapY = (posEnd[1] - posStart[1]) / (len(orderList) - 1)
    gapZ = (posEnd[2] - posStart[2]) / (len(orderList) - 1)


    rotStartX = cmds.getAttr(orderList[0]+'.rotateX')
    rotStartY = cmds.getAttr(orderList[0]+'.rotateY')
    rotStartZ = cmds.getAttr(orderList[0]+'.rotateZ')
    rotEndX = cmds.getAttr(orderList[-1]+'.rotateX')
    rotEndY = cmds.getAttr(orderList[-1]+'.rotateY')
    rotEndZ = cmds.getAttr(orderList[-1]+'.rotateZ')

    rotX = (rotEndX - rotStartX) /   (len(orderList) - 1)
    rotY = (rotEndY - rotStartY) /   (len(orderList) - 1)
    rotZ = (rotEndZ - rotStartZ) /   (len(orderList) - 1)



    for i in range(1,(len(orderList)-1)):
        cmds.move( (posStart[0] + (i *gapX)) , (posStart[1] + (i *gapY)), (posStart[2] + (i *gapZ)), orderList[i], rpr = True ,absolute=True )
        cmds.setAttr( (orderList[i] + '.rotateX'), ((i *rotX)+ rotStartX) )
        cmds.setAttr( (orderList[i] + '.rotateY'), ((i *rotY)+ rotStartY) )
        cmds.setAttr( (orderList[i] + '.rotateZ'), ((i *rotZ)+ rotStartZ) )

def borderAlginBBoxDivUpdate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if not cmds.objExists(beseMesh +'_borderBox'):
        borderAlginBBoxCreate()
    checkDiv =  cmds.intSliderGrp('bboxDivSlider', q=True, v = True)
    cmds.setAttr((beseMesh + '_bbox.subdivisionsDepth') , checkDiv)
    cmds.setAttr((beseMesh + '_bbox.subdivisionsWidth') , checkDiv)
    cmds.setAttr((beseMesh + '_bbox.subdivisionsHeight'), checkDiv)

def borderAlginBBoxCreate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selStore = cmds.ls(sl=True,fl=True)
    checkDiv =  cmds.intSliderGrp('bboxDivSlider', q=True, v = True)
    if not cmds.objExists(beseMesh +'_borderBoxGrp') and not cmds.objExists(beseMesh +'_borderBox'):
        tempLattice = cmds.lattice(beseMesh,divisions =(2, 2, 2), objectCentered = True, ldv = (2, 2 ,2))
        BBcenter = cmds.xform(tempLattice[1],q =True, t=True)
        BBrotate = cmds.xform(tempLattice[1],q =True, ro=True)
        BBscale  = cmds.xform(tempLattice[1],q =True, r=True, s=True)
        BBcube = cmds.polyCube(w =1, h =1, d =1, sx= checkDiv, sy= checkDiv, sz= checkDiv, ax= (0, 1, 0), ch = 1)
        cmds.rename(BBcube[0],(beseMesh+'_borderBox'))
        cmds.rename(BBcube[1],(beseMesh+'_bbox'))

        cmds.xform((beseMesh+'_borderBox'), t = (BBcenter[0], BBcenter[1],BBcenter[2]))
        cmds.xform((beseMesh+'_borderBox'), ro = (BBrotate[0], BBrotate[1],BBrotate[2]))
        cmds.xform((beseMesh+'_borderBox'), s = (BBscale[0], BBscale[1],BBscale[2]))
        cmds.delete(tempLattice)

        cmds.group()
        cmds.rename(beseMesh+'_borderBoxGrp')
        cmds.parent((beseMesh+'_borderBoxGrp'), (beseMesh+'BoolGrp'))
        if not cmds.objExists('BorderBox'):
            cmds.createDisplayLayer(name = ('BorderBox'))
        cmds.editDisplayLayerMembers( ('BorderBox'),(beseMesh+'_borderBoxGrp'))
        cmds.setAttr(('BorderBox.displayType'),1)
    cmds.select(selStore)

def borderAlginBBoxToggle():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selStore = cmds.ls(sl=True,fl=True)
    if not cmds.objExists(beseMesh +'_borderBoxGrp') and not cmds.objExists(beseMesh +'_borderBox'):
        borderAlginBBoxCreate()
        cmds.button('borderAlginButton',e=True, bgc =  [0.3,0.5,0.6])
        cmds.makeLive(  beseMesh +'_borderBox' )
        cmds.manipMoveContext('Move',e=True, snapLivePoint= True)
    else:
        cmds.delete(beseMesh +'_borderBoxGrp')
        cmds.button('borderAlginButton',e=True, bgc =  [0.28,0.28,0.28])
        cmds.makeLive( none=True )
        cmds.manipMoveContext('Move',e=True, snapLivePoint= False)
    cmds.select(selStore)

def toggleAxisButton(dir):
    if dir == "X":
        checkStateX = cmds.button('toggleAxisX', q=True , bgc =True )
        if (checkStateX[0] < 0.285):
            cmds.button('toggleAxisX', e=True , bgc = [.3, 0, 0] )
            cmds.button('toggleAxisXYZ', e=True ,bgc = [0.28,0.28,0.28]  )
        else:
             cmds.button('toggleAxisX', e=True ,bgc = [0.28,0.28,0.28]  )
    if dir == "Y":
        checkStateY = cmds.button('toggleAxisY', q=True , bgc =True )
        if (checkStateY[1] < 0.285):
            cmds.button('toggleAxisY', e=True , bgc = [0, 0.3, 0] )
            cmds.button('toggleAxisXYZ', e=True ,bgc = [0.28,0.28,0.28]  )
        else:
             cmds.button('toggleAxisY', e=True ,bgc = [0.28,0.28,0.28]  )
    if dir == "Z":
        checkStateZ = cmds.button('toggleAxisZ', q=True , bgc =True )
        if (checkStateZ[2] < 0.285):
            cmds.button('toggleAxisZ', e=True , bgc = [0, 0, 0.3] )
            cmds.button('toggleAxisXYZ', e=True ,bgc = [0.28,0.28,0.28]  )
        else:
             cmds.button('toggleAxisZ', e=True ,bgc = [0.28,0.28,0.28]  )

    if dir == "XYZ":
        checkState = cmds.button('toggleAxisXYZ', q=True , bgc =True )
        if (checkState[0] < 0.285):
            cmds.button('toggleAxisXYZ', e=True , bgc = [0.3, 0.5, 0.6] )
            cmds.button('toggleAxisX', e=True ,bgc = [0.28,0.28,0.28]  )
            cmds.button('toggleAxisY', e=True ,bgc = [0.28,0.28,0.28]  )
            cmds.button('toggleAxisZ', e=True ,bgc = [0.28,0.28,0.28]  )

        else:
             cmds.button('toggleAxisXYZ', e=True ,bgc = [0.28,0.28,0.28]  )
             cmds.button('toggleAxisX', e=True , bgc = [.3, 0, 0] )

    checkStateX = cmds.button('toggleAxisX', q=True , bgc =True )
    checkStateY = cmds.button('toggleAxisY', q=True , bgc =True )
    checkStateZ = cmds.button('toggleAxisZ', q=True , bgc =True )
    if (checkStateX[0] < 0.285) and (checkStateY[1] < 0.285) and (checkStateZ[2] < 0.285):
        cmds.button('toggleAxisXYZ', e=True , bgc = [0.3, 0.5, 0.6] )
    elif (checkStateX[0] > 0.285) and (checkStateY[1] > 0.285) and (checkStateZ[2] > 0.285):
        cmds.button('toggleAxisXYZ', e=True , bgc = [0.3, 0.5, 0.6] )
        cmds.button('toggleAxisX', e=True ,bgc = [0.28,0.28,0.28]  )
        cmds.button('toggleAxisY', e=True ,bgc = [0.28,0.28,0.28]  )
        cmds.button('toggleAxisZ', e=True ,bgc = [0.28,0.28,0.28]  )

def alignSelCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    cutterList = cmds.ls(type='transform',os=1)
    if len(cutterList) == 2:
        currentX = cmds.getAttr(cutterList[0]+'.translateX')
        currentY = cmds.getAttr(cutterList[0]+'.translateY')
        currentZ = cmds.getAttr(cutterList[0]+'.translateZ')
        cmds.select(cutterList[0],cutterList[1],r=True)
        cmds.MatchTranslation()
        checkState = cmds.button('toggleAxisXYZ', q=True , bgc =True )
        if checkState[0] < 0.285:
            checkStateX = cmds.button('toggleAxisX', q=True , bgc =True )
            if checkStateX[0] <0.285:
                cmds.setAttr((cutterList[0]+'.translateX'),currentX)

            checkStateY = cmds.button('toggleAxisY', q=True , bgc =True )
            if checkStateY[1] <0.285:
                cmds.setAttr((cutterList[0]+'.translateY'),currentY)
            checkStateZ = cmds.button('toggleAxisZ', q=True , bgc =True )
            if checkStateZ[2] <0.285:
                cmds.setAttr((cutterList[0]+'.translateZ'),currentZ)
    cmds.select(cutterList[0])

def alignLastCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selCutter = cmds.ls(sl=1,fl=1)
    cmds.select(beseMesh+'_cutterGrp')
    cmds.select(hi=True)
    cmds.select((beseMesh+'_cutterGrp'),d=True)
    cmds.select(selCutter,d=True)
    cutterList = cmds.ls(sl=1,fl=1,type='transform')
    if len(cutterList) > 0:
        lastCutter = cutterList[-1]
        for s in selCutter:
            currentX = cmds.getAttr(s+'.translateX')
            currentY = cmds.getAttr(s+'.translateY')
            currentZ = cmds.getAttr(s+'.translateZ')
            cmds.select(s,lastCutter,r=True)
            cmds.MatchTranslation()
            checkState = cmds.button('toggleAxisXYZ', q=True , bgc =True )
            if checkState[0] < 0.285:
                checkStateX = cmds.button('toggleAxisX', q=True , bgc =True )
                if checkStateX[0] <0.285:
                    cmds.setAttr((s+'.translateX'),currentX)

                checkStateY = cmds.button('toggleAxisY', q=True , bgc =True )
                if checkStateY[1] <0.285:
                    cmds.setAttr((s+'.translateY'),currentY)
                checkStateZ = cmds.button('toggleAxisZ', q=True , bgc =True )
                if checkStateZ[2] <0.285:
                    cmds.setAttr((s+'.translateZ'),currentZ)
    cmds.select(selCutter)

def alignCutterToBase():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selCutters = cmds.ls(sl=True,fl=True)
    if len(selCutters) > 0:
        if cmds.objExists('tempSnap'):
            cmds.delete('tempSnap')
        if cmds.objExists(beseMesh+'_borderBox') == 0:
            borderAlginBBoxToggle()

        borderBox = beseMesh + '_borderBox'
        cvNo = cmds.polyEvaluate(borderBox, v=True )

        for s in selCutters:
            checkMinDistance = 10000000
            cutterPosition = cmds.xform(s, q =True, sp=True,ws=True)
            closetestPos = [0,0,0]
            currentX = cmds.getAttr(s+'.translateX')
            currentY = cmds.getAttr(s+'.translateY')
            currentZ = cmds.getAttr(s+'.translateZ')
            for i in range(cvNo):
                cvBboxPosition = cmds.pointPosition(borderBox+'.vtx[' + str(i) + ']',w=1)
                checkDistance = math.sqrt( ((cutterPosition[0] - cvBboxPosition[0])**2)  + ((cutterPosition[1] - cvBboxPosition[1])**2) + ((cutterPosition[2] - cvBboxPosition[2])**2))
                if checkDistance < checkMinDistance:
                    checkMinDistance = checkDistance
                    closetestPos = cvBboxPosition
            cmds.spaceLocator( p=(closetestPos[0], closetestPos[1], closetestPos[2]),n='tempSnap')
            cmds.CenterPivot()
            cmds.select(s,'tempSnap',r=True)
            cmds.MatchTranslation()
            cmds.delete('tempSnap')
            checkState = cmds.button('toggleAxisXYZ', q=True , bgc =True )
            if checkState[0] < 0.285:
                checkStateX = cmds.button('toggleAxisX', q=True , bgc =True )
                if checkStateX[0] <0.285:
                    cmds.setAttr((s+'.translateX'),currentX)

                checkStateY = cmds.button('toggleAxisY', q=True , bgc =True )
                if checkStateY[1] <0.285:
                    cmds.setAttr((s+'.translateY'),currentY)

                checkStateZ = cmds.button('toggleAxisZ', q=True , bgc =True )
                if checkStateZ[2] <0.285:
                    cmds.setAttr((s+'.translateZ'),currentZ)
        borderAlginBBoxToggle()
        cmds.select(selCutters)

def combineSelCutters():#work with different type of OP, but mixing type may be cause unexpect result
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selList = cmds.ls(sl=True,fl=True)
    restoreMissingGrps()
    getOpType = ''
    if len(selList) > 1:
        #bake array
        for s in selList:
            if cmds.objExists(s):
                cmds.select(s)
                myType = checkInstType()
                if myType[1] != 'new':
                    instBake()
                    newNode = cmds.ls(sl=1,fl=1)
                    selList.append(newNode[0])
        subsGrp = []
        unionGrp = []
        cutGrp = []
        for b in selList:
            longName = '|' +  beseMesh  + 'BoolGrp' + '|' + beseMesh+'_cutterGrp|' + b
            if cmds.objExists(longName):
                checkOP = cmds.getAttr(longName + '.cutterOp')
                if checkOP == 'subs':
                    subsGrp.append(b)
                elif checkOP == 'union':
                    unionGrp.append(b)
                elif checkOP == 'cut':
                    cutGrp.append(b)
        if (len(subsGrp) + len(unionGrp) + len(cutGrp))>1:
            #union each type
            selList = subsGrp
            if len(selList)> 0:
                cmds.select(selList)
                while len(selList) > 1:
                    cmds.polyCBoolOp(selList[0], selList[1], op=1, ch=1, preserveColor=0, classification=1, name=selList[0])
                    cmds.DeleteHistory()
                    if cmds.objExists(selList[1]):
                        cmds.delete(selList[1])
                    cmds.rename(selList[0])
                    selList.remove(selList[1])
                cmds.rename('subsMesh')

            selList = unionGrp
            if len(selList)> 0:
                cmds.select(selList)
                while len(selList) > 1:
                    cmds.polyCBoolOp(selList[0], selList[1], op=1, ch=1, preserveColor=0, classification=1, name=selList[0])
                    cmds.DeleteHistory()
                    if cmds.objExists(selList[1]):
                        cmds.delete(selList[1])
                    cmds.rename(selList[0])
                    selList.remove(selList[1])
                cmds.rename('unionMesh')

            selList = cutGrp
            if len(selList)> 0:
                cmds.select(selList)
                while len(selList) > 1:
                    cmds.polyCBoolOp(selList[0], selList[1], op=1, ch=1, preserveColor=0, classification=1, name=selList[0])
                    cmds.DeleteHistory()
                    if cmds.objExists(selList[1]):
                        cmds.delete(selList[1])
                    cmds.rename(selList[0])
                    selList.remove(selList[1])
                cmds.rename('cutMesh')

        if cmds.objExists('subsMesh'):
            if cmds.objExists('unionMesh'):
                cmds.polyCBoolOp('subsMesh', 'unionMesh', op=2, ch=1, preserveColor=0, classification=1, name='outMesh')
                if cmds.objExists('cutMesh'):
                    cmds.polyCBoolOp('outMesh', 'cutMesh', op=1, ch=1, preserveColor=0, classification=1, name='outMesh')
            else:
                 if cmds.objExists('cutMesh'):
                    cmds.polyCBoolOp('subsMesh', 'cutMesh', op=1, ch=1, preserveColor=0, classification=1, name='outMesh')
            newCutter = cmds.ls(sl=1,fl=1)
            cmds.DeleteHistory('outMesh')
            useOwnCutterShape()
            cutterType('subs')

        else:
            if cmds.objExists('unionMesh'):
                if cmds.objExists('cutMesh'):
                    cmds.polyCBoolOp('unionMesh', 'cutMesh', op=2, ch=1, preserveColor=0, classification=1, name='outMesh')
            newCutter = cmds.ls(sl=1,fl=1)
            cmds.DeleteHistory('outMesh')
            useOwnCutterShape()
            cutterType('union')

        cleanList = ['subsMesh','cutMesh','unionMesh','outMesh']
        for l in cleanList:
            if cmds.objExists(l):
                cmds.delete(l)
    else:
        print ('need more then one cutter!')

def recreateBool():
    #recreate bool
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)

    cleanList = ['_mySubs','_myUnion','_preSubBox','_preUnionBox','_myBoolUnion','_afterSubBox','_myBoolSub','_myCut']
    for l in cleanList:
        if cmds.objExists(beseMesh + l):
            cmds.delete(beseMesh + l)
    if cmds.objExists((beseMesh +'_bool')) ==0:
        cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
        cmds.rename(beseMesh +'_preSubBox')

        cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
        cmds.rename(beseMesh +'_afterSubBox')

        cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
        cmds.rename(beseMesh +'_preUnionBox')

        subNode= cmds.polyCBoolOp((beseMesh ), (beseMesh +'_preSubBox') , op= 2, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_bool'))
        cmds.rename(subNode[0],(beseMesh +'_myBoolSub'))

        unionNode = cmds.polyCBoolOp((beseMesh +'_myBoolSub'), (beseMesh +'_preUnionBox') , op= 1, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_union'))
        cmds.rename(unionNode[0],(beseMesh +'_myBoolUnion'))

        subNode= cmds.polyCBoolOp((beseMesh +'_myBoolUnion'), (beseMesh +'_afterSubBox') , op= 2, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_bool'))
        cmds.rename(subNode[0],(beseMesh +'_bool'))

    boolNode = cmds.listConnections(cmds.listHistory((beseMesh +'_bool'),f=1,ac=1),type='polyCBoolOp')
    boolNode = set(boolNode)

    #hack it by check '_', this is used by other group
    listClean = []
    for b in boolNode:
        if '_' not in b:
            listClean.append(b)

    if len(listClean) == 3:
        for l in listClean:
            checkOp = cmds.getAttr( l +'.operation')
            if checkOp == 2:
                if cmds.objExists(beseMesh +'_mySubs'):
                    cmds.rename(l,(beseMesh +'_myCut'))
                else:
                    cmds.rename(l,(beseMesh +'_mySubs'))
            else:
                cmds.rename(l,(beseMesh +'_myUnion'))

    cmds.setAttr((beseMesh + '.visibility'), 0)
    cmds.setAttr((beseMesh+'Shape.intermediateObject'), 0)

    baseShapeNode = cmds.listRelatives(beseMesh, f = True)
    cmds.parent(baseShapeNode, beseMesh+'BoolGrp')
    cmds.delete(beseMesh)
    cmds.rename(beseMesh)

    cmds.editDisplayLayerMembers( (beseMesh +'_BoolResult'),(beseMesh +'_bool')) # store my selection into the display layer
    cmds.setAttr((beseMesh +'_BoolResult.displayType'),2)

    checkList = ['_cutterGrp','_preSubBox','_preUnionBox','_myBoolUnion','_bool', '', '_afterSubBox','_myBoolSub' ]
    for c in checkList:
        checkGrp = cmds.ls((beseMesh + c), l=True)
        if 'BoolGrp' not in checkGrp[0]:
            cmds.parent(checkGrp[0],(beseMesh +'BoolGrp'))

    cmds.select(cl=True)
    meshBBox()

def bakeCutter(mode):
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selectedCutter = cmds.ls(sl=1,fl=1)
    checkGrp = cmds.ls(sl=1,fl=1,l=1)
    if mode == 'unselect' and len(selectedCutter) == 0:
        print ('nothing selected!')
    else:
        #store any symmtry
        cmds.setAttr((beseMesh+'.visibility'), 1)
        mirrorPivot = cmds.objectCenter(beseMesh, gl=True)
        cmds.setAttr((beseMesh+'.visibility'), 0)
        getSymX = 0
        getSymY = 0
        getSymZ = 0
        if cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
            getSymX =  cmds.getAttr(beseMesh+'.symmetryX')
        if cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
            getSymY =  cmds.getAttr(beseMesh+'.symmetryY')
        if cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
            getSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')
        #flatten all cutters
        flattenAlllCutter()
        if mode == 'unselect':
            if beseMesh in checkGrp[0]:#check if cutter in current base mesh
                #getList after flattern
                cleanList = []
                for s in selectedCutter:
                    if 'ArrayGrp' in s:
                        s = s.replace("ArrayGrp", "")
                    if cmds.objExists(s.split('|')[-1]):
                        cleanList.append(s.split('|')[-1])
                cmds.select(cleanList)
                #disconnect from bool
                for c in cleanList:
                    shapeNode = cmds.listRelatives(c, f = True, shapes=True)
                    if len(shapeNode)>0:
                        listConnect = cmds.connectionInfo((shapeNode[0]+'.outMesh'), dfs=True )
                        if len(listConnect)>0:
                            for a in listConnect:
                                cmds.disconnectAttr((shapeNode[0]+'.outMesh'), a)
                        listConnectMa = cmds.connectionInfo((shapeNode[0]+'.worldMatrix[0]'), dfs=True )
                        if len(listConnectMa)>0:
                            for b in listConnectMa:
                                cmds.disconnectAttr((shapeNode[0]+'.worldMatrix[0]'), b)
                # move to temp grp
                if cmds.objExists((beseMesh +'_tempStoreGrp')) == 0:
                    cmds.CreateEmptyGroup()
                    cmds.rename((beseMesh +'_tempStoreGrp'))
                    cmds.parent((beseMesh +'_tempStoreGrp'), (beseMesh+'BoolGrp'))
                cmds.parent(cleanList , (beseMesh +'_tempStoreGrp'))

        #make bool mesh as new base mesh
        newMesh = cmds.duplicate((beseMesh+'_bool'),rr=1)
        cmds.delete(beseMesh+'_bool')
        #create Step up Group
        if cmds.objExists((beseMesh +'_bakeStep')) == 0:
            cmds.CreateEmptyGroup()
            cmds.rename((beseMesh +'_bakeStep'))
            cmds.parent((beseMesh +'_bakeStep'), (beseMesh+'BoolGrp'))
        cmds.setAttr((beseMesh +'_bakeStep.visibility'),0)

        if cmds.objExists((beseMesh +'_bakeBaseMesh')) == 0:
            #bake base mesh
            bakeMesh = cmds.duplicate(beseMesh, rr=1)
            cmds.delete(beseMesh)
            cmds.parent(bakeMesh,(beseMesh +'_bakeStep'))
            cmds.rename(bakeMesh,(beseMesh +'_bakeBaseMesh'))
            bakeShape = cmds.listRelatives((beseMesh +'_bakeBaseMesh'), shapes=True,f=True)
            #cmds.setAttr((bakeShape[0] + '.overrideShading'), 1)
            cmds.rename(newMesh,beseMesh)
        else:
            cmds.delete(beseMesh)
            cmds.rename(newMesh,beseMesh)
        if cmds.objExists(beseMesh +'_myBool'):
            cmds.delete(beseMesh+'_myBool')
        #reNumber
        cmds.select((beseMesh+'_bakeStep'), hi=True)
        cmds.select((beseMesh+'_bakeStep'),(beseMesh +'_bakeBaseMesh'),d=True)
        existCutterList = cmds.ls(sl=1,fl=1,type='transform')
        #start rename old cutters
        cmds.select((beseMesh+'_cutterGrp'), hi=True)
        cmds.select((beseMesh+'_cutterGrp'),d=True)
        oldCutterList = cmds.ls(sl=1,fl=1,type='transform')
        initalIndex = len(existCutterList) + 2
        for o in oldCutterList:
            newName = ('bakeCutter' + str(initalIndex))
            cmds.rename(o, newName)
            initalIndex += 1
        newList= cmds.ls(sl=1,fl=1,type='transform')
        if len(newList)>0:
            cmds.parent(newList,(beseMesh +'_bakeStep'))

        #unlock connection
        shape = cmds.listRelatives(beseMesh, shapes=True,f=True)
        checkConnection = cmds.listConnections((shape[0]+'.drawOverride'),c=1,p=1)
        if checkConnection != None:
            cmds.disconnectAttr(checkConnection[1],checkConnection[0])

        #recreate bool
        recreateBool()
        cmds.move(mirrorPivot[0],mirrorPivot[1],mirrorPivot[2], (beseMesh + ".scalePivot"),(beseMesh + ".rotatePivot"), absolute=True)

        if mode == 'unselect':

            #reconnect selected Cutters
            newCutterList = []
            for c in cleanList:
                cmds.select(c)
                fixBoolNodeConnection()
                newC = cmds.ls(sl=1)
                newCutterList.append(newC[0])

            cmds.parent(newCutterList , (beseMesh +'_cutterGrp'))
            if cmds.objExists((beseMesh +'_tempStoreGrp')):
                cmds.delete((beseMesh +'_tempStoreGrp'))

        setCutterBaseMesh()
        if mode == 'unselect':
            cmds.select(selectedCutter)

        #restore symmetry
        if not cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryX', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryX'),getSymX)
        if not cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryY', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryY'),getSymY)
        if not cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryZ', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryZ'),getSymZ)

        #checkSymmetryState
        checkSymX =  cmds.getAttr(beseMesh+'.symmetryX')
        checkSymY =  cmds.getAttr(beseMesh+'.symmetryY')
        checkSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')

        if checkSymX == 1:
            boolSymmetry('x',1)
        elif checkSymX == -1:
            boolSymmetry('x',2)

        if checkSymY == 1:
            boolSymmetry('y',1)
        elif checkSymY == -1:
            boolSymmetry('y',2)

        if checkSymZ == 1:
            boolSymmetry('z',1)
        elif checkSymZ == -1:
            boolSymmetry('z',2)

        #hide all cage
        if cmds.objExists(beseMesh + '_cageGrp'):
            cmds.hide(beseMesh + '_cageGrp')
        #cageList = cmds.ls((beseMesh + '_cage*'),type='transform')
        #for c in cageList:
        #    cmds.setAttr((c+'.visibility'),0)
    cmds.optionMenu('baseMeshMenu', e = True, value = beseMesh)
    restoreMissingGrps()

def restoreCutterWithSymmtry():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    #check current
    shapes = cmds.listRelatives((beseMesh+'_bool'), shapes=True)
    shadeEng = cmds.listConnections(shapes , type = 'shadingEngine')
    materials = cmds.ls(cmds.listConnections(shadeEng ), materials = True)
    checkX1 = cmds.button('symmXButtonP', q=1 , bgc = 1)
    checkX2 = cmds.button('symmXButtonN', q=1 , bgc = 1)
    checkY1 = cmds.button('symmYButtonP', q=1 , bgc = 1)
    checkY2 = cmds.button('symmYButtonN', q=1 , bgc = 1)
    checkZ1 = cmds.button('symmZButtonP', q=1 , bgc = 1)
    checkZ2 = cmds.button('symmZButtonN', q=1 , bgc = 1)
    restoreCutter()
    if checkX1[0]>0.29:
        boolSymmetry("x" ,1)
    if checkX2[0]>0.29:
        boolSymmetry("x" ,2)

    if checkY1[1]>0.29:
        boolSymmetry("y" ,1)
    if checkY2[1]>0.29:
        boolSymmetry("y" ,2)

    if checkZ1[2]>0.29:
        boolSymmetry("z" ,1)
    if checkZ2[2]>0.29:
        boolSymmetry("z" ,2)
    #resotre shader
    if materials[0] == (beseMesh+'_Shader'):
        cmds.sets((beseMesh+'_bool'), e=True, forceElement = (beseMesh+'_ShaderSG'))
    else:
        cmds.sets((beseMesh+'_bool'), e=True, forceElement = 'initialShadingGroup')

def restoreCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
        cmds.CreateEmptyGroup()
        cmds.rename((beseMesh +'_cutterGrp'))
        cmds.parent((beseMesh +'_cutterGrp'),(beseMesh +'BoolGrp'))

    if cmds.objExists((beseMesh +'_bool')) ==0:
        cmds.polyCube(w = 0.01, h=0.01, d=0.01 ,sx =1 ,sy= 1, sz= 1)
        cmds.rename(beseMesh +'_preSubBox')
        cmds.polyCube(w = 0.01, h=0.01, d=0.01 ,sx =1 ,sy= 1, sz= 1)
        cmds.rename(beseMesh +'_preUnionBox')
        unionNode = cmds.polyCBoolOp(beseMesh, (beseMesh +'_preUnionBox') , op= 1, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_union'))
        cmds.rename(unionNode[0],(beseMesh +'_myBoolUnion'))
        subNode= cmds.polyCBoolOp((beseMesh +'_myBoolUnion'), (beseMesh +'_preSubBox') , op= 2, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_bool'))
        cmds.rename(subNode[0],(beseMesh +'_bool'))
        boolNode = cmds.listConnections(cmds.listHistory((beseMesh +'_bool'),f=1,ac=1),type='polyCBoolOp')
        boolNode = set(boolNode)

        #hack it by check '_', this is used by other group
        listClean = []
        for b in boolNode:
            if '_' not in b:
                listClean.append(b)


        if len(listClean) == 3:
            for l in listClean:
                checkOp = cmds.getAttr( l +'.operation')
                if checkOp == 2:
                    if cmds.objExists(beseMesh +'_mySubs'):
                        cmds.rename(l,(beseMesh +'_myCut'))
                    else:
                        cmds.rename(l,(beseMesh +'_mySubs'))
                else:
                    cmds.rename(l,(beseMesh +'_myUnion'))

        cmds.setAttr((beseMesh + '.visibility'), 0)
        baseNodes = cmds.listRelatives(beseMesh, ad = True, f = True)
        baseTransNode = cmds.ls(baseNodes,type = 'transform')
        baseMeshNode = cmds.ls(baseNodes,type = 'mesh')
        cmds.setAttr((baseMeshNode[0]+'.intermediateObject'), 0)
        cmds.parent(baseMeshNode[0],(beseMesh +'BoolGrp'))
        cmds.delete(beseMesh)
        cmds.rename(beseMesh)

    bakeCutter('all')
    cmds.delete(beseMesh+'_bool')
    cmds.delete(beseMesh)
    cmds.parent((beseMesh +'_bakeBaseMesh'),  (beseMesh+'BoolGrp'))
    cmds.rename((beseMesh +'_bakeBaseMesh'), beseMesh)
    baseShape = cmds.listRelatives((beseMesh), shapes=True,f=True)
    checkAtt =  cmds.getAttr(baseShape[0] + '.overrideShading')
    if checkAtt == 0:
        cmds.setAttr((baseShape[0] + '.overrideShading'), 1)
    #recreate bool
    recreateBool()
    #restore cutters
    cmds.select((beseMesh+'_bakeStep'), hi=True)
    cmds.select((beseMesh+'_bakeStep'),d=True)
    restoreCutterList = cmds.ls(sl=1,fl=1,type='transform')
    for r in restoreCutterList:
        shapeNode = cmds.listRelatives(r, f = True, shapes=True)
        cmds.setAttr( (shapeNode[0]+".overrideEnabled") , 1)
        cmds.setAttr( (shapeNode[0]+".overrideShading") , 0)
        cmds.setAttr( (shapeNode[0]+".castsShadows") , 0)
        cmds.setAttr( (shapeNode[0]+".receiveShadows") , 0)
        cmds.setAttr( (shapeNode[0]+".primaryVisibility") , 0)
        cmds.setAttr( (shapeNode[0]+".visibleInReflections") , 0)
        cmds.setAttr( (shapeNode[0]+".visibleInRefractions") , 0)
        cmds.select(r)
        fixBoolNodeConnection()
        name = r.split('|')[-1]
        checkNumber = ''.join([n for n in name.split('|')[-1] if n.isdigit()])
        cmds.rename(r ,('boxCutter' + str(checkNumber)))

    if cmds.objExists((beseMesh +'_cutterGrp')):
        cmds.delete(beseMesh +'_cutterGrp')

    cmds.rename((beseMesh +'_bakeStep'),(beseMesh +'_cutterGrp'))
    cmds.select(cl=True)
    showAllCutter()
    fixShadowLink()

def flattenAlllCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    cmds.select((beseMesh+'_cutterGrp'), hi=True)
    cmds.select((beseMesh+'_cutterGrp'),d=True)
    if cmds.objExists('bakeCutter*'):
        cmds.select('bakeCutter*',d=True)
    selList = cmds.ls(sl=1,fl=1,type='transform')
    if len(selList) > 1:
        #bake array
        for s in selList:
            if cmds.objExists(s):
                cmds.select(s)
                myType = checkInstType()
                if myType[1] != 'new':
                    instBake()
                    newNode = cmds.ls(sl=1,fl=1)
                    selList.append(newNode[0])

def freeResultMesh():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists((beseMesh+'_Done')) == 0 :
        bakeCutter("all")
        resultMesh = beseMesh +'_bool'
        cmds.select(resultMesh)
        cmds.duplicate(rr=True)
        cmds.rename(beseMesh+'_Done')
        newNode = cmds.ls(sl=True,fl=True)
        shapeNew = cmds.listRelatives(newNode[0], s=True )
        cmds.parent(w=True)
        cmds.layerButton((beseMesh +'_BoolResult'), e=True ,lv=0)
        cmds.setAttr((beseMesh +'BoolGrp.visibility'),0)
        cmds.disconnectAttr((beseMesh+'_BoolResult.drawInfo'), (shapeNew[0]+'.drawOverride'))
        cmds.editDisplayLayerMembers('defaultLayer',newNode)
        cmds.hide(beseMesh+'BoolGrp')

def drawCurveNow():
    cmds.snapMode(grid=1)
    cmds.CVCurveTool()

def makeDrawBlock():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    curveSel = cmds.ls(sl=1,fl=1)
    if len(curveSel) == 1 :
        cmds.snapMode(grid=0)
        shapeNode = cmds.listRelatives(curveSel[0], f = True, shapes=True)
        checkOpen = cmds.getAttr(shapeNode[0]+'.form')
        if checkOpen == 0:
            cmds.closeCurve( curveSel[0], ch=True, rpo=True )

        cmds.select(curveSel)
        cmds.duplicate()
        cmds.group(w=True)
        cmds.rename('tempMirrorGrp')

        cmds.parent('tempMirrorGrp','lineDrawPlaneOffset')
        cmds.FreezeTransformations()
        getPresize = cmds.floatField( 'cuterPreSize' , q=1, value = True)
        setScale =   cmds.floatSliderGrp('cutterScaleSlider', q=1, value = True)
        cmds.setAttr('tempMirrorGrp.translateZ',(getPresize*setScale*0.5*-1))

        cmds.Ungroup()
        cmds.select(curveSel,add=1)
        cmds.FreezeTransformations()
        curveSel = cmds.ls(sl=1,fl=1)
        cmds.select(curveSel)
        loftNode = cmds.loft(ch =1, u=1, c= 0, ar= 1, d= 3, ss= 1, rn= 0, po =1, rsn= True)
        list = cmds.listConnections(loftNode, type = 'nurbsTessellate')

        cmds.setAttr((list[0]+'.polygonType'), 1)
        checkCurveType = cmds.getAttr(curveSel[0]+'.degree')
        if checkCurveType > 1:
            cmds.setAttr((list[0]+'.format'), 0)
        else:
            cmds.setAttr((list[0]+'.format'), 2)
        cmds.setAttr((list[0]+'.uNumber'), 1)
        cmds.setAttr((list[0]+'.vNumber'), 1)
        cmds.FillHole()
        cmds.delete(curveSel)
        cmds.rename('drawBlock')
        blockSel = cmds.listRelatives(cmds.listRelatives(f = True, shapes=True), parent=1 , f=1 )
        cmds.CenterPivot()
        cmds.polyMergeVertex(blockSel,d = 0.01, am= 1,ch=0)
        cmds.polySetToFaceNormal()
        renew = cmds.listRelatives(cmds.listRelatives(f = True, shapes=True), parent=1 , f=1 )
        cmds.DeleteHistory()
        #fix normal direction
        checkNormalMehs = cmds.ls(sl=1,fl=1,l=1)
        cmds.polyExtrudeFacet(constructionHistory = 1, keepFacesTogether= 1, ltz = 0.001)
        cmds.polySeparate(checkNormalMehs,ch=0)
        testMesh = cmds.ls(sl=1,fl=1)

        worldFaceA = cmds.polyEvaluate(testMesh[0],wa=True)
        worldFaceB = cmds.polyEvaluate(testMesh[1],wa=True)
        if worldFaceA > worldFaceB:
            cmds.delete(testMesh[1])
        else:
            cmds.delete(testMesh[0])

        cmds.parent(w=True)
        cmds.delete(checkNormalMehs[0])
        cmds.rename('drawBlock1')
        newBlock = cmds.ls(sl=1,fl=1)
        cmds.select(newBlock[0])

        #remove unwant edgeLoop
        if checkCurveType > 1:
            cmds.polySelectConstraint(m=3,t=0x0008,sz=3)
            cmds.polySelectConstraint(disable =True)
            ngon = cmds.ls(sl=1,fl=1)
            cmds.select(ngon)
            cmds.ConvertSelectionToEdges()
            hardEdge = cmds.ls(sl=1,fl=1)
            cmds.SelectEdgeRingSp()
            cmds.select(hardEdge,d=1)
            cmds.polyDelEdge(cv=1)
            cmds.select(newBlock[0])

        cmds.parent(newBlock[0],'drawPlaneGrp')
        cmds.FreezeTransformations()
        cmds.CenterPivot()
        cmds.parent(newBlock[0],w=True)
        cmds.DeleteHistory()
        cmds.ScaleTool()

def goPressDraw():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = (beseMesh +'_bool')
    if cmds.objExists('snapLive*'):
        cmds.delete('snapLive*')
    cmds.duplicate(snapMesh,n='snapLive')
    cmds.setAttr('snapLive.visibility',0)
    global ctxCutter
    if cmds.draggerContext(ctxCutter, exists=True):
        cmds.deleteUI(ctxCutter)
    cmds.draggerContext(ctxCutter, pressCommand = onPressDrawGrid, dragCommand = onDragDrawGridCMD, rc = offPressDrawGrid, name=ctxCutter, cursor='crossHair',undoMode='all')
    cmds.setToolTo(ctxCutter)

def onDragDrawGridCMD():
    cmds.undoInfo(swf=0)
    onDragDrawGrid()
    cmds.undoInfo(swf=1)

def onDragDrawGrid():
    global ctxCutter
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, dragPoint=True)
    screenX = vpX
    screenY = vpY
    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()
    omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    #current camera
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
    cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)
    checkHit = 0
    finalMesh = []
    finalX = []
    finalY = []
    finalZ = []
    shortDistance = 10000000000
    distanceBetween = 1000000000
    hitFacePtr = om.MScriptUtil().asIntPtr()
    hitFace = []
    checkList = []
    checkList.append('snapLive')
    for mesh in checkList:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)

        intersection = fnMesh.closestIntersection(
        om.MFloatPoint(pos2),
        om.MFloatVector(dir),
        None,
        None,
        False,
        om.MSpace.kWorld,
        99999,
        False,
        None,
        hitpoint,
        None,
        hitFacePtr,
        None,
        None,
        None)

        if intersection:
            x = hitpoint.x
            y = hitpoint.y
            z = hitpoint.z
            distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
            if distanceBetween < shortDistance:
                shortDistance = distanceBetween
                finalMesh = mesh
                finalX = x
                finalY = y
                finalZ = z
                hitFace = om.MScriptUtil(hitFacePtr).asInt()
            hitFaceName = (mesh + '.f[' + str(hitFace) +']')
            rx, ry, rz = getFaceAngle(hitFaceName)
            cmds.move(finalX,finalY,finalZ,'drawPlaneGrp',absolute=1)
            tz = cmds.floatSliderGrp('snapGirdOffset', q=True, v = True)
            cmds.setAttr('drawPlaneGrp.rotateX', rx)
            cmds.setAttr('drawPlaneGrp.rotateY', ry)
            cmds.setAttr('drawPlaneGrp.rotateZ', rz)
            #cmds.setAttr('lineDrawPlaneOffset.translateX', 0)
            #cmds.setAttr('lineDrawPlaneOffset.translateY', 0)
            cmds.setAttr('lineDrawPlaneOffset.translateZ',tz)
            cmds.refresh(cv=True,f=True)

def offPressDrawGrid():
    if cmds.objExists('snapLive*'):
        cmds.delete('snapLive*')
    cmds.setToolTo('moveSuperContext')

def onPressDrawGrid():
    global ctxCutter
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()
    omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    #current camera
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
    cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)
    checkHit = 0
    finalMesh = []
    finalX = []
    finalY = []
    finalZ = []
    shortDistance = 10000000000
    distanceBetween = 1000000000
    hitFacePtr = om.MScriptUtil().asIntPtr()
    hitFace = []
    checkList = []
    checkList.append('snapLive')
    for mesh in checkList:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)

        intersection = fnMesh.closestIntersection(
        om.MFloatPoint(pos2),
        om.MFloatVector(dir),
        None,
        None,
        False,
        om.MSpace.kWorld,
        99999,
        False,
        None,
        hitpoint,
        None,
        hitFacePtr,
        None,
        None,
        None)

        if intersection:
            x = hitpoint.x
            y = hitpoint.y
            z = hitpoint.z
            distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
            if distanceBetween < shortDistance:
                shortDistance = distanceBetween
                finalMesh = mesh
                finalX = x
                finalY = y
                finalZ = z
                hitFace = om.MScriptUtil(hitFacePtr).asInt()
            hitFaceName = (mesh + '.f[' + str(hitFace) +']')
            rx, ry, rz = getFaceAngle(hitFaceName)
            if cmds.objExists('lineDrawPlane'):
                cmds.delete('lineDrawPlane')
            if cmds.objExists('drawPlaneGrp'):
                cmds.delete('drawPlaneGrp')
            mesh = (beseMesh +'_bool')
            bbox= cmds.xform(mesh, q=1, ws=1, bb=1)
            length=math.sqrt((math.pow(bbox[0]-bbox[3],2)+math.pow(bbox[1]-bbox[4],2)+math.pow(bbox[2]-bbox[5],2))/3)
            length = int(length *1.1 )
            cmds.plane(s=length, r=[0,0,0])
            cmds.rename('lineDrawPlane')
            cmds.group('lineDrawPlane')
            cmds.rename('lineDrawPlaneOffset')
            cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1 )
            cmds.group('lineDrawPlaneOffset')
            cmds.rename('lineDrawPlaneOffsetFreeze')
            cmds.setAttr(("lineDrawPlaneOffsetFreeze.rotateX"), -90)
            cmds.group('lineDrawPlaneOffsetFreeze')
            cmds.rename('drawPlaneGrp')
            cmds.move(finalX,finalY,finalZ,'drawPlaneGrp',absolute=1)
            cmds.setAttr('drawPlaneGrp.rotateX', rx)
            cmds.setAttr('drawPlaneGrp.rotateY', ry)
            cmds.setAttr('drawPlaneGrp.rotateZ', rz)

            cmds.makeLive('lineDrawPlane')
            cmds.snapMode(grid=1)
            resizeSnapGrid()
            offsetSnapGrid()

def resizeSnapGrid():
    if cmds.objExists('lineDrawPlane'):
        gridData=  cmds.intSliderGrp('snapGirdSize', q = True, v =True)
        cmds.makeLive(n=True)
        cmds.grid( spacing=10, d= gridData )
        cmds.makeLive('lineDrawPlane')
        cmds.snapMode(grid=1)

def rotateSnapGrid():
    if cmds.objExists('lineDrawPlane'):
        checkRot = cmds.intSliderGrp('snapGirdRot',q=True, v = True)
        cmds.setAttr("lineDrawPlane.rotateZ", checkRot)

def offsetSnapGrid():
    if cmds.objExists('lineDrawPlane'):
        checkOffset =  cmds.floatSliderGrp('snapGirdOffset',q=True, v = True)
        cmds.setAttr("lineDrawPlaneOffset.translateZ", checkOffset)

def snapGridCamera():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkOffset = cmds.floatSliderGrp('snapGirdOffset', q=True, v = True)
    cmds.intSliderGrp('snapGirdRot',e=True, v = 0)
    curPanel = cmds.getPanel(wf=1)
    if not 'modelPanel' in curPanel:
        curPanel = 'modelPanel4'
    cmds.modelEditor( curPanel,e=1, planes=1)
    curCam = cmds.modelPanel(curPanel,q=1, cam=1)
    cameraPos = cmds.xform(curCam,q=1,ws=1,t=1)
    orthoValue = cmds.camera(curCam,q=1, o=1)
    cameraUsed=[]
    planePos=[]
    if orthoValue ==0:
        camRot = cmds.camera(curCam,q=1, rot=1)
        camRotFixed = []
        for i in range(2):
            camRotTemp = camRot[i] / 360
            intOfTemp = int(camRotTemp)
            rotOver = 360 * intOfTemp
            camRotFixed.append( camRot[i] - rotOver)

        for i in range(2):
            if camRotFixed[i] < 0 :
                  camRotFixed[i]= camRotFixed[i] +360;

        cameraUsed=[]
        if (camRotFixed[0] >= 45 and camRotFixed[0] < 135):
            cameraUsed = 'buttom'
        elif (camRotFixed[0] >= 225 and camRotFixed[0] < 315):
            cameraUsed = 'top'
        elif (camRotFixed[1] < 45):
            cameraUsed = 'front'
        elif (camRotFixed[1] >= 315 ):
            cameraUsed = 'front'
        elif (camRotFixed[1] >= 45 and camRotFixed[1] < 135):
            cameraUsed = 'right'
        elif (camRotFixed[1] >= 135 and camRotFixed[1] < 225):
            cameraUsed = 'back'
        elif (camRotFixed[1] >= 225 and camRotFixed[1] < 315):
            cameraUsed = 'left'

        mesh = (beseMesh +'_bool')
        bbox= cmds.xform(mesh, q=1, ws=1, bb=1)
        length=math.sqrt((math.pow(bbox[0]-bbox[3],2)+math.pow(bbox[1]-bbox[4],2)+math.pow(bbox[2]-bbox[5],2))/3)
        length = int(length *1.1 )
        meshCOORD = cmds.objectCenter(mesh,gl=True)
        constructionPlanePos=[]
        if cmds.objExists('lineDrawPlane'):
            cmds.delete('lineDrawPlane')
        if cmds.objExists('drawPlaneGrp'):
            cmds.delete('drawPlaneGrp')

        if cameraUsed == 'front' or cameraUsed == 'back':
            if cameraUsed == 'front':
                    planePos = bbox[5]
            elif cameraUsed == 'back':
                if (bbox[2] - cameraPos[2]) > 0:
                    planePos = bbox[2]
            constructionPlanePos = [meshCOORD[0],meshCOORD[1],planePos]

        elif  cameraUsed == 'top' or cameraUsed == 'buttom':# check y asix
            if cameraUsed == 'top':
                planePos = bbox[4]
            elif cameraUsed == 'buttom':
                planePos = bbox[1]
            constructionPlanePos = [meshCOORD[0],planePos,meshCOORD[2]]

        elif  cameraUsed == 'left' or cameraUsed == 'right':# check x asix
            if cameraUsed == 'right':
                planePos = bbox[3]
            elif cameraUsed == 'left':
                planePos = bbox[0]
            constructionPlanePos = [planePos,meshCOORD[1],meshCOORD[2]]

        cmds.plane(s=length, r=[0,0,0])
        cmds.rename('lineDrawPlane')
        cmds.group('lineDrawPlane')
        cmds.rename('lineDrawPlaneOffset')
        cmds.move(constructionPlanePos[0],constructionPlanePos[1],constructionPlanePos[2],absolute=1)
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1 )
        cmds.group('lineDrawPlaneOffset')
        cmds.rename('drawPlaneGrp')

        if cameraUsed == 'front':
            cmds.setAttr("drawPlaneGrp.rotateZ", -90)
        elif cameraUsed == 'back':
            cmds.setAttr("drawPlaneGrp.rotateX", 180)

        elif  cameraUsed == 'top':
            cmds.setAttr("drawPlaneGrp.rotateX", -90)
        elif cameraUsed == 'buttom':
            cmds.setAttr("drawPlaneGrp.rotateX", 90)

        elif  cameraUsed == 'left':
            cmds.setAttr("drawPlaneGrp.rotateY", -90)
        elif cameraUsed == 'right':
            cmds.setAttr("drawPlaneGrp.rotateY", 90)

        cmds.makeLive('lineDrawPlane')
        cmds.snapMode(grid=1)
        resizeSnapGrid()
        offsetSnapGrid()

def drawGirdOff():
    if cmds.objExists('lineDrawPlane'):
        cmds.delete('lineDrawPlane*')
    if cmds.objExists('tempScaleOffset'):
        cmds.delete('tempScaleOffset*')
    if cmds.objExists('drawPlaneGrp'):
        cmds.delete('drawPlaneGrp*')
    cmds.snapMode(grid=0)
    cmds.MoveTool()

def drawGirdOn():
    cmds.CVCurveTool()
    cmds.curveCVCtx(cmds.currentCtx(), e=True, d=1, bez= 0)

def removeGap():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    for n in newCutter:
        if 'boxCutter' in n:
            if 'ArrayGrp' in n:
                n = n.replace('ArrayGrp','')
            extrudeNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyExtrudeFace')
            if extrudeNode != None:
                cmds.delete(extrudeNode)
            cmds.setAttr((n+'.statePanel'),0)
            cmds.setAttr((n+'.preBevel'),1)

def makeGap():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    for n in newCutter:
        if 'boxCutter' in n:
            if 'ArrayGrp' in n:
                n = n.replace('ArrayGrp','')
            extrudeNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyExtrudeFace')
            if extrudeNode != None:
                cmds.delete(extrudeNode)
            gapV = []
            storeX = cmds.getAttr( n + '.scaleX')
            gapV = cmds.floatSliderGrp('gapSlider', q=True, v = True)
            if gapV < 0.01:
                gapV = 0.01
                cmds.floatSliderGrp('gapSlider', e = True, v=0.01)
            cmds.setAttr((n+'.panelGap'),gapV)
            cmds.setAttr((n+'.intPanelGap'),gapV)
            cmds.setAttr((n+'.intScaleX'),storeX)
            cmds.select(n)
            extNode = cmds.polyExtrudeFacet( constructionHistory=True, keepFacesTogether = True, smoothingAngle=30, tk = gapV )
            cmdText = (extNode[0] + '.thickness = ' + n + '.intScaleX/' +  n + '.scaleX*' + str(gapV) + '*' + n + '.panelGap/' +  n + '.intPanelGap')
            cmds.expression( s = cmdText, o = extNode[0], ae = True, uc = all)
            cmds.setAttr((n+'.statePanel'),1)
            cmds.setAttr((n+'.preBevel'),0)
    cmds.select(newCutter)

def hideAllCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    getCutters = cmds.ls((beseMesh+'_cutterGrp|boxCutter*'),type = 'transform',l=True)
    cmds.hide(getCutters)

def showLastCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    currentOne = cmds.ls(sl=True,fl=True)
    getCutters = cmds.ls((beseMesh+'_cutterGrp|boxCutter*'),type = 'transform')
    checkVis = []
    if len(getCutters) > 0:
        for g in getCutters:
            checkme = cmds.getAttr(g+'.visibility')
            if checkme == 1:
               checkVis.append(g)
        if len(currentOne) > 0:
            checkCutter = []
            for c in currentOne:
                if 'boxCutter' in c:
                    checkCutter.append(c)
            if len(checkCutter)>0:
                checkSel = cmds.getAttr(checkCutter[0]+'.visibility')
                cmds.hide(getCutters)
                if checkSel == 0:
                    cmds.setAttr((checkCutter[0]+'.visibility'), 1)
                else:
                    if len(checkVis) > 1:
                        cmds.select(checkCutter[0])
                        cmds.showHidden(checkCutter[0])
                    elif len(checkVis) == 1:
                        preCutter = 0
                        for i in range(len(getCutters)):
                            if getCutters[i] == checkCutter[0]:
                                preCutter = i - 1
                        cmds.select(getCutters[preCutter])
                        cmds.showHidden(getCutters[preCutter])
                    else:
                        cmds.select(getCutters[-1])
                        cmds.showHidden(getCutters[-1])
        else:
            cmds.hide(getCutters)
            cmds.select(getCutters[-1])
            cmds.showHidden(getCutters[-1])
        cmds.setAttr((beseMesh+'_cutterGrp.visibility'), 1)

def showAllCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    getCutters = cmds.ls((beseMesh+'_cutterGrp|boxCutter*'),type = 'transform',l=True)
    checkAllCutterGrps = cmds.ls(('*_cutterGrp'),type = 'transform',l=True)
    cmds.hide(checkAllCutterGrps)
    cmds.showHidden(getCutters)
    if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
        cmds.CreateEmptyGroup()
        cmds.rename((beseMesh +'_cutterGrp'))
        cmds.parent((beseMesh +'_cutterGrp'),(beseMesh +'BoolGrp'))

    cmds.setAttr((beseMesh+'_cutterGrp.visibility'), 1)

def hideUnSelectedCutters():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    currentSel = cmds.ls(sl= True)
    getCutters = cmds.ls((beseMesh+'_cutterGrp|boxCutter*'),type = 'transform',l=True)
    checkVisList = []
    for g in getCutters:
        state = cmds.getAttr(g+'.visibility')
        if state == 1:
            checkVisList.append(g)
    if len(checkVisList) == len(currentSel):
        showAllCutter()
    else:
        cmds.hide(getCutters)
        cmds.showHidden(currentSel)
    cmds.select(currentSel)

def attributeGapSlider():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    checkSlider = cmds.floatSliderGrp('gapSlider',q=True, v= True )
    if len(newCutter) > 0:
        for n in newCutter:
            if 'ArrayGrp' in n:
                 n = n.replace('ArrayGrp','')
            checkGap = cmds.getAttr(n +'.statePanel')
            if checkGap == 1:
                cmds.setAttr((n +'.panelGap'),checkSlider)

def attributeIntSlider(attributName):
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    sliderName = (str(attributName)+'Slider')
    checkSlider = cmds.intSliderGrp(sliderName,q=True, v= True )
    if len(newCutter) > 0:
        for n in newCutter:
            if 'ArrayGrp' in n:
                 n = n.replace('ArrayGrp','')
            bevelNode = cmds.listConnections(cmds.listHistory(n),type='polyBevel3')
            if bevelNode != None:
                cmds.setAttr((bevelNode[0] +'.' + attributName),checkSlider)

def attributeFloatSlider(attributName):
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    sliderName = (str(attributName)+'Slider')
    checkSlider = cmds.floatSliderGrp(sliderName,q=True, v= True )
    if len(newCutter) > 0:
        for n in newCutter:
            if 'ArrayGrp' in n:
                 n = n.replace('ArrayGrp','')
            bevelNode = cmds.listConnections(cmds.listHistory(n),type='polyBevel3')
            if bevelNode != None:
                cmds.setAttr((bevelNode[0] +'.' + attributName),checkSlider)

def cutterMirrorOver(direction):
    listSel = cmds.ls(sl=True, fl=True ,l=True)
    if len(listSel) > 0 and 'boxCutter' in listSel[0] and 'ArrayGrp' not in listSel[0]:
        cmds.duplicate(rr=True, un=True)
        cmds.group()
        if cmds.objExists('tempPivot'):
            cmds.delete('tempPivot')
        cmds.rename('tempPivot')
        beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
        meshCOORD = cmds.objectCenter(beseMesh,gl=True)
        cmds.xform(ws=True,  pivots =[meshCOORD[0],meshCOORD[1],meshCOORD[2]])

        if direction == 'x':
            cmds.setAttr( ('tempPivot.scaleX'),-1)
        if direction == 'y':
            cmds.setAttr( ('tempPivot.scaleY'),-1)
        if direction == 'z':
            cmds.setAttr( ('tempPivot.scaleZ'),-1)
        cmds.FreezeTransformations()

        cmds.select(cmds.listRelatives('tempPivot', c=True, f = True, typ='transform'))
        cmds.select((beseMesh+'_cutterGrp'), add=True)
        cmds.parent()
        listNew = cmds.ls(sl=True, fl=True ,l=True)
        fixBoolNodeConnection()

        cmds.delete('tempPivot')
        for s in listSel:
            cmds.setAttr((s+'.visibility'),0)
        cmds.select(listNew)

def cutterMirror(axis):
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    dulCutter = []
    if len(newCutter) > 0:
        for n in newCutter:
            if 'Cutter' in n:
                cmds.FreezeTransformations()
                bboxObj = cmds.xform(n , q = True, ws =True, bb=True)

                mirrorMode = 0

                if axis == 'x' :
                    if bboxObj[3] > 0 and bboxObj[0] > 0:
                        mirrorMode = 1
                    elif  bboxObj[3] < 0 and bboxObj[0] < 0:
                        mirrorMode = 1

                elif axis == 'y' :
                    if bboxObj[4] > 0 and bboxObj[1] > 0:
                        mirrorMode = 1
                    elif  bboxObj[4] < 0 and bboxObj[1] < 0:
                        mirrorMode = 1

                elif axis == 'z' :
                    if bboxObj[5] > 0 and bboxObj[2] > 0:
                        mirrorMode = 1
                    elif  bboxObj[5] < 0 and bboxObj[2] < 0:
                        mirrorMode = 1

                if mirrorMode == 1:
                    cmds.select(n)
                    cutterMirrorOver(axis)
                    newC = cmds.ls(sl=1)
                    dulCutter.append(newC[0])
                else:

                    lengthObj=math.sqrt((math.pow(bboxObj[0]-bboxObj[3],2)+math.pow(bboxObj[1]-bboxObj[4],2)+math.pow(bboxObj[2]-bboxObj[5],2))/3)
                    closeRange = lengthObj / 100

                    bboxSel = cmds.xform(n , q = True, ws =True, bb=True)
                    midX = (bboxSel[3]+bboxSel[0])/2
                    midY = (bboxSel[4]+bboxSel[1])/2
                    midZ = (bboxSel[5]+bboxSel[2])/2
                    inRangeCv = []
                    vNo = cmds.polyEvaluate(n, v = True )
                    checkPoint = 0
                    if axis == 'x' :
                        checkPoint = 0
                    elif axis == 'y' :
                        checkPoint = 1
                    else:
                        checkPoint = 2
                    for i in range(vNo):
                        positionV = cmds.pointPosition((n +'.vtx[' + str(i) + ']') , w = True)
                        length= math.sqrt(math.pow(positionV[checkPoint],2))
                        if length <= closeRange:
                           inRangeCv.append((n +'.vtx[' + str(i) + ']'))
                        cmds.select(inRangeCv, r=True)

                    # push those point off center a bit then mirror cut
                    if axis == 'x' :
                        for n in inRangeCv:
                            posiV = cmds.pointPosition(n , w = True)
                            if midX >= 0:
                                cmds.move((closeRange * -1.5) , posiV[1], posiV[2], n ,absolute=1)
                            else:
                                cmds.move( (closeRange * 1.5) , posiV[1], posiV[2], n ,absolute=1)
                        cutPlane= cmds.polyCut(n, ws = True, cd = 'X' , df = True , ch =True)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterX'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterY'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterZ'), 0)
                        if midX > 0:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateY'), 90)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 0, axisDirection = 1, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)
                        else:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateY'), -90)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 0, axisDirection = 0, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)

                    if axis == 'y' :
                        for n in inRangeCv:
                            posiV = cmds.pointPosition(n , w = True)
                            if midY >= 0:
                                cmds.move(posiV[0], (closeRange  * -1.5) , posiV[2], n ,absolute=1)
                            else:
                                cmds.move(posiV[0], (closeRange  * 1.5) , posiV[2], n ,absolute=1)
                        cutPlane= cmds.polyCut(n, ws = True, cd = 'Y' , df = True , ch =True)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterX'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterY'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterZ'), 0)
                        if midY > 0:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateX'), -90)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 1, axisDirection = 1, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)
                        else:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateX'), 90)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 1, axisDirection = 0, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)

                    if axis == 'z' :
                        for n in inRangeCv:
                            posiV = cmds.pointPosition(n , w = True)
                            if midZ >= 0:
                                cmds.move(posiV[0], posiV[1],(closeRange  * -1.5), n ,absolute=1)
                            else:
                                cmds.move(posiV[0], posiV[1],(closeRange  * 1.5), n ,absolute=1)
                        cutPlane= cmds.polyCut(n, ws = True, cd = 'Z' , df = True , ch =True)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterX'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterY'), 0)
                        cmds.setAttr((cutPlane[0]+'.cutPlaneCenterZ'), 0)
                        if midZ > 0:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateY'), 0)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 2, axisDirection = 1, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)
                        else:
                            cmds.setAttr((cutPlane[0]+'.cutPlaneRotateY'), 180)
                            cmds.polyMirrorFace(n,cutMesh =1, axis = 2, axisDirection = 0, mergeMode = 1, mergeThresholdType = 1, mergeThreshold =0.001, mirrorAxis = 0 ,mirrorPosition = 0 ,smoothingAngle= 30 ,flipUVs =0 ,ch = 0)
                    cmds.select(n)
                    dulCutter.append(n)
                    cmds.BakeNonDefHistory()
            cmds.select(dulCutter)

def useOwnCutterShape():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    ownCutter = cmds.ls(sl=True, fl=True ,l=True)
    restoreMissingGrps()
    o = ownCutter[0]
    if len(ownCutter) > 0:
        for o in ownCutter:
            if ('_cutterGrp') in o:
                print ('shape already been used')
            else:
                if cmds.objExists(beseMesh + '_BoolResult') == 0:
                    restoreCutterWithSymmtry()
                cmds.select(o)
                cmds.parent(o,(beseMesh+'_cutterGrp'))
                ownCutter = cmds.ls(sl=True, fl=True ,l=True)
                newNumber = nextCutterNumber()
                newName = 'boxCutter'+str(newNumber)
                cmds.select(ownCutter)
                cmds.rename(newName)
                newCutter = cmds.ls(sl=True, fl=True)
                shapeNode = cmds.listRelatives(newCutter, f = True, shapes=True)
                cmds.setAttr( (shapeNode[0]+".overrideEnabled") , 1)
                cmds.setAttr( (shapeNode[0]+".overrideShading") , 0)
                cmds.setAttr( (shapeNode[0]+".castsShadows") , 0)
                cmds.setAttr( (shapeNode[0]+".receiveShadows") , 0)
                cmds.setAttr( (shapeNode[0]+".primaryVisibility") , 0)
                cmds.setAttr( (shapeNode[0]+".visibleInReflections") , 0)
                cmds.setAttr( (shapeNode[0]+".visibleInRefractions") , 0)
                checkButtonStateList = ['subsButton','unionButton','cutButton']
                getCurrentType = ''
                for c in checkButtonStateList:
                    buttonState = cmds.button( c ,q=1,  bgc = True )
                    if buttonState[1] > 0.4:
                        getCurrentType = c
                setType = getCurrentType.replace('Button','')
                if setType == 'subs':
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 28)
                elif setType == 'union':
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 31)
                else:
                    cmds.setAttr( (shapeNode[0]+'.overrideColor'), 25)
                cmds.connectAttr( (shapeNode[0]+".worldMatrix[0]"), ((beseMesh +'_my' + setType.title() +'.inputMat['+str(newNumber)+']')),f=True)
                cmds.connectAttr( (shapeNode[0]+".outMesh"), ((beseMesh +'_my' + setType.title() + '.inputPoly['+str(newNumber)+']')),f=True)

                if not cmds.attributeQuery('cutterDir', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='cutterDir',  dt= 'string')
                if not cmds.attributeQuery('cutterType', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='cutterType',  dt= 'string')
                cmds.setAttr((newCutter[0]+'.cutterDir'),e=True, keyable=True)
                cmds.setAttr((newCutter[0]+'.cutterType'),e=True, keyable=True)

                if not cmds.attributeQuery('cutterOp', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='cutterOp',  dt= 'string')
                cmds.setAttr((newCutter[0]+'.cutterOp'),e=True, keyable=True)
                cmds.setAttr((newCutter[0]+'.cutterOp'),setType,type="string")

                if not cmds.attributeQuery('statePanel', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='statePanel', at = "float" )
                if not cmds.attributeQuery('panelGap', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='panelGap', at = "float" )
                if not cmds.attributeQuery('intPanelGap', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='intPanelGap', at = "float" )
                if not cmds.attributeQuery('intScaleX', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='intScaleX', at = "float" )

                if not cmds.attributeQuery('preBevel', node = newCutter[0], ex=True ):
                    cmds.addAttr(newCutter[0], ln='preBevel', at = "float" )

                cmds.setAttr((newCutter[0]+'.statePanel'),0)
                cmds.setAttr((newCutter[0]+'.preBevel'),1)
                cmds.select(newCutter[0])
                cmds.setAttr((newCutter[0]+'.cutterType'),'custom' ,type="string")
    else:
        print ('nothing select!')

def cutterDulpicate():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    dulCutter = cmds.ls(sl=True, fl=True , l=True)
    newCutterList = []
    if len(dulCutter) > 0:
        for d in dulCutter:
            checkParent = d.split('|')
            if len(checkParent)>2 and 'boxCutter' in d and 'cutterGrp' in d:
                newNumber = nextCutterNumber()
                newName = 'boxCutter'+str(newNumber)
                cmds.select(d)
                cmds.duplicate(rr = True, un=True)
                cmds.rename(newName)
                newCutter = cmds.ls(sl=True, fl=True)
                shapeNode = cmds.listRelatives(newCutter[0], f = True, shapes=True)
                cmds.setAttr( (shapeNode[0]+".overrideEnabled") , 1)
                cmds.setAttr( (shapeNode[0]+".overrideShading") , 0)
                cmds.setAttr( (shapeNode[0]+".castsShadows") , 0)
                cmds.setAttr( (shapeNode[0]+".receiveShadows") , 0)
                cmds.setAttr( (shapeNode[0]+".primaryVisibility") , 0)
                cmds.setAttr( (shapeNode[0]+".visibleInReflections") , 0)
                cmds.setAttr( (shapeNode[0]+".visibleInRefractions") , 0)
                boolNode = cmds.listConnections(cmds.listHistory((beseMesh +'_bool'),f=1),type='polyCBoolOp')
                if boolNode != None:
                    cmds.connectAttr( (shapeNode[0]+".worldMatrix[0]"), ((boolNode[0]+'.inputMat['+str(newNumber)+']')),f=True)
                    cmds.connectAttr( (shapeNode[0]+".outMesh"), ((boolNode[0]+'.inputPoly['+str(newNumber)+']')),f=True)
                    cmds.select(newCutter[0])
                    fixBoolNodeConnection()
                    newCutterList.append(newCutter[0])
            else:
                print (d + 'is not a cutter!!')
        cmds.select(newCutterList)
    else:
        print ('nothing selected!')

def QChangeCutterDir(dir):
    selObj = cmds.ls(sl=1, fl=1,l=True, type='transform')
    if len(selObj) == 1:

        checkMasterDir = []
        checkMasterNumber = []
        checkMasterDis = []
        arraySample = []
        myType = checkInstType()
        if 'ArrayGrp' in selObj[0]:
            myType = checkInstType()
            arraySample = myType[0]
            if myType[1] != 'new':
                checkMasterDir = cmds.getAttr(arraySample+'.arrayDirection')
                checkMasterNumber = cmds.getAttr(arraySample+'.arrayNumber')
                checkMasterDis = cmds.getAttr(arraySample+'.arrayOffset')
                checkMasterType = myType[1]
                if myType[1] == 'radial':
                    removeRadArray()
                else:
                    instRemove()
            selObj = cmds.ls(sl=1, fl=1,l=True, type='transform')
        cmds.setAttr((selObj[0]+'.rotateX'), 0)
        cmds.setAttr((selObj[0]+'.rotateY'), 0)
        cmds.setAttr((selObj[0]+'.rotateZ'), 0)
        cutterDirection = cmds.getAttr(selObj[0]+'.cutterDir')

        if dir == 'X':
            dir = 'Z'
        elif dir == 'Y':
            pass
        else:
            dir = 'X'

        parnetGrp = cmds.listRelatives(selObj[0], parent =1, f=1)
        cmds.group(em=True, name = (selObj[0]+'_offset'),parent = parnetGrp[0])
        newNode = cmds.ls(sl=True,fl=True)
        cmds.FreezeTransformations()
        sourcePivot = cmds.xform(selObj[0], q=1, ws=1 ,rp=1)
        cmds.xform(newNode ,ws=1, piv = (sourcePivot[0],sourcePivot[1],sourcePivot[2]))
        cmds.parent(selObj[0],newNode)
        cmds.setAttr((newNode[0]+'.rotate' + dir), 90)
        newNode = cmds.ls(sl=True,fl=True)
        parnetGrpRemove = cmds.listRelatives(newNode[0], parent =1, f=1)
        cmds.parent(newNode[0],parnetGrp)
        cmds.delete(parnetGrpRemove)
        newNode = cmds.ls(sl=True,fl=True)
        if myType[1] != 'new':
            if myType[1] == 'radial':
                instRadAdd(checkMasterDir)
            else:
                instLinearAdd(checkMasterDir)
            cmds.setAttr((newNode[0]+'.arrayNumber'),checkMasterNumber)
            cmds.setAttr((newNode[0]+'.arrayOffset'),checkMasterDis)

def QBoxSmooth():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    if len(newCutter) > 0:
        for n in newCutter:
            if 'Cutter' in n:
                if 'ArrayGrp' in n:
                    myType = checkInstType()
                    n = (myType[0])
            #in case gap exist
            extrudeNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyExtrudeFace')
            if extrudeNode != None:
                cmds.delete(extrudeNode)
            bevelNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyBevel3')
            bevelType = []
            getFrac = []
            getSeg = []
            getDep = []
            cmds.select(n)
            if bevelNode != None:
                cmds.makeIdentity( n, apply=True, scale=True )
                #record old setting
                getFrac = cmds.getAttr(bevelNode[0]+'.fraction')
                getSeg = cmds.getAttr(bevelNode[0]+'.segments')
                getDep = cmds.getAttr(bevelNode[0]+'.depth')
                cmds.delete(bevelNode)
                cmds.DeleteHistory()
            bevelNodeNew = cmds.polyBevel3(n, mv = 1, mvt =0.001, fn = 1, fraction = 0.5, offsetAsFraction = 1, autoFit = 1, depth = 1, mitering = 0, miterAlong = 0, chamfer = 1,  segments = 5,  ch = 1)
            cmds.floatSliderGrp('fractionSlider', e=True , v = 0.5)
            cmds.intSliderGrp('segmentsSlider',   e=True , v = 5)
            cmds.floatSliderGrp('depthSlider',    e=True , v = 1)
            if bevelNode != None:
                cmds.setAttr((bevelNodeNew[0]+'.fraction'),getFrac)
                cmds.setAttr((bevelNodeNew[0]+'.segments'),getSeg)
                cmds.setAttr((bevelNodeNew[0]+'.depth'),getDep)
                cmds.floatSliderGrp('fractionSlider', e=True , v = getFrac)
                cmds.intSliderGrp('segmentsSlider',   e=True , v = getSeg)
                cmds.floatSliderGrp('depthSlider',    e=True , v = getDep)
            cmds.setAttr((n+'.cutterType'),'smooth',type="string")
            checkGapState = cmds.getAttr(n+'.statePanel')
            if checkGapState == 1:
                cmds.select(n)
                makeGap()
        cmds.select(newCutter)

def QBoxBevel():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    if len(newCutter) > 0:
        for n in newCutter:
            if 'Cutter' in n:
                if 'ArrayGrp' in n:
                    myType = checkInstType()
                    n = (myType[0])
            #in case gap exist
            extrudeNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyExtrudeFace',s=True)
            if extrudeNode != None:
                cmds.delete(extrudeNode)
            bevelNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyBevel3')
            bevelList = []
            bevelType = []
            getFrac = []
            getSeg = []
            getDep = []
            cmds.select(n)
            cmds.makeIdentity( n, apply=True, scale=True )
            if bevelNode != None:
                #record old setting
                getFrac = cmds.getAttr(bevelNode[0]+'.fraction')
                getSeg = cmds.getAttr(bevelNode[0]+'.segments')
                getDep = cmds.getAttr(bevelNode[0]+'.depth')
                cmds.delete(bevelNode)
                cmds.DeleteHistory()

            cmds.select(n)
            cmds.polySelectConstraint(mode = 3, type = 0x0008, size=1)
            cmds.polySelectConstraint(disable =True)
            triFind = cmds.ls(sl=1,fl=1)
            cmds.select(n)
            cmds.polySelectConstraint(mode = 3, type = 0x0008, size=3)
            cmds.polySelectConstraint(disable =True)
            ngonFind = cmds.ls(sl=1,fl=1)

            if len(triFind) == 2 and len(ngonFind) == 0:# case is triprism
                bevelList = str(n + '.e[6:8]')

            elif len(triFind) > 0 or len(ngonFind) > 0:
                if len(triFind) > 0:
                    cmds.select(triFind)
                    cmds.InvertSelection()#added - usless
                else:
                    cmds.select(ngonFind)
                cmds.select(n)
                cmds.ConvertSelectionToFaces()
                cmds.select(ngonFind,d=True)
                cmds.ConvertSelectionToContainedEdges()
                bevelList = cmds.ls(sl=1,fl=1)
            else:#case is cube
                checkNoCustom = cmds.getAttr(n+'.cutterType')
                if checkNoCustom == 'custom':
                    cmds.select(str(n + '.e[4:5]'))
                    cmds.select(str(n + '.e[8:9]'), add =1 )
                    bevelList = cmds.ls(sl=1,fl=1)
                else:
                    bevelList = str(n + '.e[8:11]')

            bevelNodeNew = cmds.polyBevel3(bevelList, mv = 1, mvt =0.001, fn = 1, fraction = 0.5, offsetAsFraction = 1, autoFit = 1, depth = 1, mitering = 0, miterAlong = 0, chamfer = 1,  segments = 5,  ch = 1)
            cmds.floatSliderGrp('fractionSlider', e=True , v = 0.5)
            cmds.intSliderGrp('segmentsSlider',   e=True , v = 5)
            cmds.floatSliderGrp('depthSlider',    e=True , v = 1)
            if bevelNode != None:
                cmds.setAttr((bevelNodeNew[0]+'.fraction'),getFrac)
                cmds.setAttr((bevelNodeNew[0]+'.segments'),getSeg)
                cmds.setAttr((bevelNodeNew[0]+'.depth'),getDep)
                cmds.floatSliderGrp('fractionSlider', e=True , v = getFrac)
                cmds.intSliderGrp('segmentsSlider',   e=True , v = getSeg)
                cmds.floatSliderGrp('depthSlider',    e=True , v = getDep)
            if extrudeNode != None:
                makeGap()
            cmds.setAttr((n+'.cutterType'),'bevel',type="string")
            checkGapState = cmds.getAttr(n+'.statePanel')
            if checkGapState == 1:
                cmds.select(n)
                makeGap()
        cmds.select(newCutter)

    else:
        cmds.ConvertSelectionToEdges()
        selEdges =cmds.filterExpand(ex =1, sm =32)
        if len(selEdges)>0:
            geoList = cmds.ls(hl=1)
            for g in geoList:
                cmds.setAttr((g+'.cutterType'),'bevel',type="string")
                checkEdge = []
                for s in selEdges:
                    if g in s:
                        checkEdge.append(s)
                bevelNodeNew = cmds.polyBevel3(checkEdge, mv = 1, mvt =0.001, fn = 1, fraction = 0.5, offsetAsFraction = 1, autoFit = 1, depth = 1, mitering = 0, miterAlong = 0, chamfer = 1,  segments = 5,  ch = 1)
        cmds.select(geoList)
        cmds.floatSliderGrp('fractionSlider', e=True , v = 0.5)
        cmds.intSliderGrp('segmentsSlider',   e=True , v = 5)
        cmds.floatSliderGrp('depthSlider',    e=True , v = 1)

def QBoxBevelRemove():
    newCutter = cmds.ls(sl=True,fl=True,type = 'transform')
    if len(newCutter) > 0:
        for n in newCutter:
            if 'Cutter' in n:
                if 'ArrayGrp' in n:
                    myType = checkInstType()
                    n = (myType[0])
                checkNoCustom = cmds.getAttr(n+'.cutterType')
                if checkNoCustom == 'bevel' or checkNoCustom == 'smooth':
                    cmds.makeIdentity( n, apply=True, scale=True )
                    shapeNode = cmds.listRelatives(n, f = True, shapes=True)
                    bevelNode = cmds.listConnections(cmds.listHistory(shapeNode,ac=1),type='polyBevel3')
                    if bevelNode != None:
                        checkGapState = cmds.getAttr(n+'.statePanel')
                        if checkGapState == 1:
                            extrudeNode = cmds.listConnections(cmds.listHistory(n,ac=1),type='polyExtrudeFace')
                            if extrudeNode != None:
                                cmds.delete(extrudeNode)
                        cmds.delete(bevelNode)
                    cmds.select(n)
                    cmds.DeleteHistory()
                    cmds.setAttr((n+'.cutterType'),'none',type="string")
                    checkGapState = cmds.getAttr(n+'.statePanel')
                    if checkGapState == 1:
                        cmds.select(n)
                        makeGap()
    cmds.select(newCutter)

def scrapeCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    selCutter = cmds.ls(sl=1, fl=1, type='transform')
    myType = checkInstType()
    if len(selCutter) == 1 and 'boxCutter' in selCutter[0] and  myType[1] == 'new':
        shapeNode = cmds.listRelatives(selCutter[0], f = True, shapes=True)
        checkConnection = cmds.listConnections(shapeNode[0]+'.worldMatrix',d=1,p=1)
        cmds.disconnectAttr((shapeNode[0]+'.worldMatrix'), checkConnection[0])
        checkConnection = cmds.listConnections(shapeNode[0]+'.outMesh',d=1,p=1)
        cmds.disconnectAttr((shapeNode[0]+'.outMesh'), checkConnection[0])

        newNode = cmds.duplicate((beseMesh+'_bool'),rr=1)
        cmds.polyExtrudeFacet(newNode,constructionHistory = 1, keepFacesTogether= 1, tk = 0.1)
        cmds.polySeparate(newNode, ch=0)
        testMesh = cmds.ls(sl=1,fl=1)
        worldFaceA = cmds.polyEvaluate(testMesh[0],wa=True)
        worldFaceB = cmds.polyEvaluate(testMesh[1],wa=True)

        if worldFaceA > worldFaceB:
            cmds.delete(testMesh[1])
        else:
            cmds.delete(testMesh[0])
        cmds.rename(selCutter[0] + '_skinMesh')

        if cmds.objExists(selCutter[0] + 'skinGrp') == 0:
            cmds.CreateEmptyGroup()
            cmds.rename(selCutter[0] +'skinGrp')

        cmds.parent((selCutter[0] + '_skinMesh'),(selCutter[0] +'skinGrp'))
        cmds.delete(newNode)
        cmds.ReversePolygonNormals()
        cmds.DeleteHistory()


        #create intersection boolean
        subNode= cmds.polyCBoolOp(selCutter[0],(selCutter[0] + '_skinMesh') , op= 3, ch= 1, preserveColor= 0, classification= 1, name= 'skinCutter')
        cmds.DeleteHistory()

        #add cutter back
        extNode = cmds.polyExtrudeFacet( constructionHistory=True, keepFacesTogether = True, smoothingAngle=30, tk = 1 )
        if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
            cmds.CreateEmptyGroup()
            cmds.rename((beseMesh +'_cutterGrp'))
            cmds.parent((beseMesh +'_cutterGrp'),(beseMesh +'BoolGrp'))

        cmds.select('skinCutter')
        useOwnCutterShape()
        #add skin attribute
        selCutter = cmds.ls(sl=1, fl=1, type='transform')
        if not cmds.attributeQuery('skinOffset', node = selCutter[0], ex=True ):
            cmds.addAttr(selCutter[0], ln='skinOffset', at = "float" )
            cmds.setAttr((selCutter[0]+'.skinOffset'),0.5)

        cmds.setAttr((selCutter[0]+'.cutterType'),'scrape',type="string")
        cmds.connectAttr((selCutter[0] +'.skinOffset'), (extNode[0] +'.thickness'),f=True)
        #link slider
        cmds.connectControl('scrapeSlider', (selCutter[0] +'.skinOffset'))

def addBevelDirectionAttr():
    newCutter = cmds.ls(sl=True, fl=True)
    cmds.setAttr((newCutter[0]+'.cutterDir'),'x',type="string")
    cmds.setAttr((newCutter[0]+'.cutterType'),'bevel',type="string")

def offPressCutter():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    checkNoSnapX = cmds.getAttr('sampleLoc.translateX')
    checkNoSnapY = cmds.getAttr('sampleLoc.translateY')
    checkNoSnapZ = cmds.getAttr('sampleLoc.translateZ')
    if checkNoSnapX !=0 and  checkNoSnapY !=0 and  checkNoSnapZ !=0:
        cmds.select('sampleLoc')
        cmds.pickWalk(d='down')
        newCutter = cmds.ls(sl=1,fl=1)
        cmds.parent(newCutter,(beseMesh+'_cutterGrp'))
    if cmds.objExists('sampleLoc*'):
        cmds.delete('sampleLoc*')
    if cmds.objExists('snapLive*'):
        cmds.delete('snapLive*')
    cmds.setToolTo('moveSuperContext')

def goPressCutter(boxSide):
    global currentScaleRecord
    global currentCutterName
    hideAllCutter()
    if cmds.objExists('sampleLoc*'):
        cmds.delete('sampleLoc*')
    if cmds.objExists('snapLive*'):
        cmds.delete('snapLive*')
    #create cutter
    sideNumber = boxSide
    preRotAngle = []
    if sideNumber == 3:
        preRotAngle = 60
    elif sideNumber == 4:
        preRotAngle = 45
    elif sideNumber == 5:
        preRotAngle = 72
    elif sideNumber == 6:
        preRotAngle = 30

    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists(beseMesh + '_BoolResult') == 0:
        restoreCutterWithSymmtry()
    nextIndex = nextCutterNumber()
    member =cmds.editDisplayLayerMembers((beseMesh+'_BoolResult'),q=True)
    snapMesh =[]
    if member != None:
        snapMesh = member[0]
    cmds.setToolTo('moveSuperContext')
    getPresize = cmds.floatField( 'cuterPreSize' , q=1, value = True)
    setScale =   cmds.floatSliderGrp('cutterScaleSlider', q=1, value = True)
    cmds.polyCylinder(r = getPresize, h= (1.5*getPresize) ,sx= boxSide, sy =0, sz=0, rcp= 0 , cuv =3 ,ch=1)
    cmds.rename('boxCutter'+str(nextIndex))
    newCutter = cmds.ls(sl=True, fl=True)
    currentCutterName = newCutter[0]
    cmds.setAttr( (newCutter[0]+'.rotateY'), preRotAngle)
    cmds.makeIdentity((newCutter[0]),apply =1, t = 0, r = 1, s =0, n =0, pn= 1)
    cmds.setAttr( (newCutter[0]+'.scaleX'),(setScale))
    cmds.setAttr( (newCutter[0]+'.scaleZ'),(setScale))
    cmds.setAttr( (newCutter[0]+'.scaleY'),(setScale))
    currentScaleRecord = setScale
    #cmds.CenterPivot()
    cmds.group()
    cmds.rename('sampleLoc')
    cmds.xform(ws =True, piv =(0,0,0))
    cmds.setAttr('sampleLoc.scaleX', 0.001)
    cmds.setAttr('sampleLoc.scaleY', 0.001)
    cmds.setAttr('sampleLoc.scaleZ', 0.001)
    refTopNode = cmds.ls(sl = True,fl =True, type= 'transform')[0]
    transDownNode = cmds.listRelatives('sampleLoc', c=True,f=True )
    #cutter in position
    #add attr
    shapeNode = cmds.listRelatives(newCutter[0], shapes=True ,f =True)
    cmds.setAttr( (shapeNode[0]+".overrideEnabled") , 1)
    cmds.setAttr( (shapeNode[0]+".overrideShading") , 0)
    cmds.setAttr( (shapeNode[0]+".castsShadows") , 0)
    cmds.setAttr( (shapeNode[0]+".receiveShadows") , 0)
    cmds.setAttr( (shapeNode[0]+".primaryVisibility") , 0)
    cmds.setAttr( (shapeNode[0]+".visibleInReflections") , 0)
    cmds.setAttr( (shapeNode[0]+".visibleInRefractions") , 0)

    if not cmds.attributeQuery('cutterDir', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='cutterDir',  dt= 'string')
    if not cmds.attributeQuery('cutterType', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='cutterType',  dt= 'string')
    cmds.setAttr((newCutter[0]+'.cutterDir'),e=True, keyable=True)
    cmds.setAttr((newCutter[0]+'.cutt erType'),e=True, keyable=True)

    if not cmds.attributeQuery('cutterOp', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='cutterOp',  dt= 'string')
    cmds.setAttr((newCutter[0]+'.cutterOp'),e=True, keyable=True)

    checkButtonStateList = ['subsButton','unionButton','cutButton']
    getCurrentType = ''
    for c in checkButtonStateList:
        buttonState = cmds.button( c ,q=1,  bgc = True )
        if buttonState[1] > 0.4:
            getCurrentType = c

    setType = getCurrentType.replace('Button','')
    cmds.setAttr((newCutter[0]+'.cutterOp'),setType,type="string")
    if setType == 'subs':
        cmds.setAttr( (shapeNode[0]+'.overrideColor'), 28)
    elif setType == 'union':
        cmds.setAttr( (shapeNode[0]+'.overrideColor'), 31)
    else:
        cmds.setAttr( (shapeNode[0]+'.overrideColor'), 25)

    if not cmds.attributeQuery('statePanel', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='statePanel', at = "float" )
    if not cmds.attributeQuery('panelGap', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='panelGap', at = "float" )
    if not cmds.attributeQuery('intPanelGap', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='intPanelGap', at = "float" )
    if not cmds.attributeQuery('intScaleX', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='intScaleX', at = "float" )
    if not cmds.attributeQuery('preBevel', node = newCutter[0], ex=True ):
        cmds.addAttr(newCutter[0], ln='preBevel', at = "float" )
    cmds.setAttr((newCutter[0]+'.statePanel'),0)
    cmds.setAttr((newCutter[0]+'.preBevel'),1)
    cmds.select(('boxCutter'+str(nextIndex)))
    fixBoolNodeConnection()
    addBevelDirectionAttr()
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    snapMesh = (beseMesh +'_bool')
    cmds.duplicate(snapMesh,n='snapLive')
    cmds.setAttr('snapLive.visibility',0)
    cmds.select(cl=1)
    ##### undo ######
    global ctxCutter
    ctxCutter = 'ctxCutter'
    cmds.intSliderGrp('cutterSideSlider', e=1,  v = boxSide)
    if cmds.draggerContext(ctxCutter, exists=True):
        cmds.deleteUI(ctxCutter)
    cmds.draggerContext(ctxCutter, pressCommand = onPressCutter, rc = offPressCutter, dragCommand = onDragCutterCMD, name=ctxCutter, cursor='crossHair', undoMode='all')
    cmds.setToolTo(ctxCutter)

def onDragCutterCMD():
    cmds.undoInfo(swf=0)
    onDragCutter()
    cmds.undoInfo(swf=1)

def onDragCutter():
    global ctxCutter
    global screenX,screenY
    global currentScaleRecord
    global currentCutterName
    selSample = 'sampleLoc'
    modifiers = cmds.getModifiers()
    if (modifiers == 1):
        #print 'shift Press'
        vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, dragPoint=True)
        distanceA = (vpX - screenX)
        rotateRun = (distanceA) /4
        if rotateRun > 360 :
            rotateRun = 360
        elif rotateRun < -360 :
            rotateRun = -360

        cmds.setAttr((currentCutterName + '.rotateY'),rotateRun)
        cmds.refresh(cv=True,f=True)

    elif(modifiers == 4):
        #print 'ctrl selSample'
        vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, dragPoint=True)
        distanceB = vpX - screenX
        scaleCheck = distanceB / 100
        scaleRun = currentScaleRecord + scaleCheck
        if scaleRun > 5:
            scaleRun = 5
        elif scaleRun < 0:
            scaleRun = 0.1
        cmds.floatSliderGrp('cutterScaleSlider',  e=1 ,v = scaleRun )
        cmds.setAttr(('sampleLoc.scaleX'),scaleRun)
        cmds.setAttr(('sampleLoc.scaleY'),scaleRun)
        cmds.setAttr(('sampleLoc.scaleZ'),scaleRun)
        cmds.refresh(cv=True,f=True)
    elif(modifiers == 8):
        vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, dragPoint=True)
        pos = om.MPoint()
        dir = om.MVector()
        hitpoint = om.MFloatPoint()
        omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
        pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
        #current camera
        view = omui.M3dView.active3dView()
        cam = om.MDagPath()
        view.getCamera(cam)
        camPath = cam.fullPathName()
        cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
        cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)
        checkHit = 0
        finalMesh = []
        finalX = 0
        finalY = 0
        finalZ = 0
        shortDistance = 10000000000
        distanceBetween = 1000000000
        meshNode = cmds.listRelatives(selSample, fullPath=True ,ad=True)
        myShape = cmds.listRelatives(meshNode, shapes=True,f=True)
        hitFacePtr = om.MScriptUtil().asIntPtr()
        hitFace = []
        beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
        member =cmds.editDisplayLayerMembers((beseMesh+'_BoolResult'),q=True)
        snapMesh = (beseMesh +'_boolShape')
        checkList = []
        checkList.append('snapLive')
        for mesh in checkList:
            selectionList = om.MSelectionList()
            selectionList.add(mesh)
            dagPath = om.MDagPath()
            selectionList.getDagPath(0, dagPath)
            fnMesh = om.MFnMesh(dagPath)
            intersection = fnMesh.closestIntersection(
            om.MFloatPoint(pos2),
            om.MFloatVector(dir),
            None,
            None,
            False,
            om.MSpace.kWorld,
            99999,
            False,
            None,
            hitpoint,
            None,
            hitFacePtr,
            None,
            None,
            None)
            if intersection:
                x = hitpoint.x
                y = hitpoint.y
                z = hitpoint.z
                distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
                if distanceBetween < shortDistance:
                    shortDistance = distanceBetween
                    finalMesh = mesh
                    hitFace = om.MScriptUtil(hitFacePtr).asInt()

                    hitFaceName = (mesh + '.f[' + str(hitFace) +']')

                cpX,cpY,cpZ = getPolyFaceCenter(hitFaceName)
                # bug, for some reason it doesn't like value is 0
                if cpX == 0:
                    cpX = 0.000001
                if cpY == 0:
                    cpY = 0.000001
                if cpZ == 0:
                    cpZ = 0.000001
                cmds.setAttr(('sampleLoc.translateX'),cpX)
                cmds.setAttr(('sampleLoc.translateY'),cpY)
                cmds.setAttr(('sampleLoc.translateZ'),cpZ)
                cmds.refresh(cv=True,f=True)
    else:
        vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, dragPoint=True)
        currentSX = vpX
        currentSY = vpY
        pos = om.MPoint()
        dir = om.MVector()
        hitpoint = om.MFloatPoint()
        omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
        pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
        #current camera
        view = omui.M3dView.active3dView()
        cam = om.MDagPath()
        view.getCamera(cam)
        camPath = cam.fullPathName()

        cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
        cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)

        checkHit = 0
        finalMesh = []
        finalX = 0
        finalY = 0
        finalZ = 0
        shortDistance = 10000000000
        distanceBetween = 1000000000
        meshNode = cmds.listRelatives(selSample, fullPath=True ,ad=True)
        myShape = cmds.listRelatives(meshNode, shapes=True,f=True)

        hitFacePtr = om.MScriptUtil().asIntPtr()
        hitFace = []
        beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
        member =cmds.editDisplayLayerMembers((beseMesh+'_BoolResult'),q=True)
        snapMesh = (beseMesh +'_boolShape')
        checkList = []
        checkList.append('snapLive')
        for mesh in checkList:
            selectionList = om.MSelectionList()
            selectionList.add(mesh)
            dagPath = om.MDagPath()
            selectionList.getDagPath(0, dagPath)
            fnMesh = om.MFnMesh(dagPath)
            intersection = fnMesh.closestIntersection(
            om.MFloatPoint(pos2),
            om.MFloatVector(dir),
            None,
            None,
            False,
            om.MSpace.kWorld,
            99999,
            False,
            None,
            hitpoint,
            None,
            hitFacePtr,
            None,
            None,
            None)
            if intersection:
                x = hitpoint.x
                y = hitpoint.y
                z = hitpoint.z
                distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
                if distanceBetween < shortDistance:
                    shortDistance = distanceBetween
                    finalMesh = mesh
                    hitFace = om.MScriptUtil(hitFacePtr).asInt()
                    finalX = x
                    finalY = y
                    finalZ = z
                # bug, for some reason it doesn't like value is 0
                if finalX == 0:
                    finalX = 0.000001
                if finalY == 0:
                    finalY = 0.000001
                if finalZ == 0:
                    finalZ = 0.000001
                cmds.setAttr('sampleLoc.translateX', finalX)
                cmds.setAttr('sampleLoc.translateY', finalY)
                cmds.setAttr('sampleLoc.translateZ',finalZ)
                hitFaceName = (mesh + '.f[' + str(hitFace) +']')
                rx, ry, rz = getFaceAngle(hitFaceName)
                cmds.setAttr('sampleLoc.rotateX', rx)
                cmds.setAttr('sampleLoc.rotateY', ry)
                cmds.setAttr('sampleLoc.rotateZ', rz)
                cmds.select('sampleLoc')
                cmds.refresh(cv=True,f=True)

def onPressCutter():
    global ctxCutter
    global screenX,screenY
    vpX, vpY, _ = cmds.draggerContext(ctxCutter, query=True, anchorPoint=True)
    screenX = vpX
    screenY = vpY
    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()
    omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    #current camera
    view = omui.M3dView.active3dView()
    cam = om.MDagPath()
    view.getCamera(cam)
    camPath = cam.fullPathName()
    cameraTrans = cmds.listRelatives(camPath,type='transform',p=True)
    cameraPosition = cmds.xform(cameraTrans,q=1,ws=1,rp=1)
    checkHit = 0
    finalMesh = []
    finalX = []
    finalY = []
    finalZ = []
    shortDistance = 10000000000
    distanceBetween = 1000000000
    hitFacePtr = om.MScriptUtil().asIntPtr()
    hitFace = []
    checkList = []
    checkList.append('snapLive')
    for mesh in checkList:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)

        intersection = fnMesh.closestIntersection(
        om.MFloatPoint(pos2),
        om.MFloatVector(dir),
        None,
        None,
        False,
        om.MSpace.kWorld,
        99999,
        False,
        None,
        hitpoint,
        None,
        hitFacePtr,
        None,
        None,
        None)

        if intersection:
            x = hitpoint.x
            y = hitpoint.y
            z = hitpoint.z
            distanceBetween = math.sqrt( ((float(cameraPosition[0]) - x)**2)  + ((float(cameraPosition[1]) - y)**2) + ((float(cameraPosition[2]) - z)**2))
            if distanceBetween < shortDistance:
                shortDistance = distanceBetween
                finalMesh = mesh
                finalX = x
                finalY = y
                finalZ = z
                hitFace = om.MScriptUtil(hitFacePtr).asInt()
            cmds.setAttr('sampleLoc.translateX', finalX)
            cmds.setAttr('sampleLoc.translateY', finalY)
            cmds.setAttr('sampleLoc.translateZ',finalZ)
            hitFaceName = (mesh + '.f[' + str(hitFace) +']')
            rx, ry, rz = getFaceAngle(hitFaceName)
            cmds.setAttr('sampleLoc.rotateX', rx)
            cmds.setAttr('sampleLoc.rotateY', ry)
            cmds.setAttr('sampleLoc.rotateZ', rz)
            cmds.setAttr('sampleLoc.scaleX', 1)
            cmds.setAttr('sampleLoc.scaleY', 1)
            cmds.setAttr('sampleLoc.scaleZ', 1)
            cmds.select('sampleLoc')
            cmds.refresh(cv=True,f=True)

def getFaceAngle(faceName):
    shapeNode = cmds.listRelatives(faceName, fullPath=True , parent=True )
    transformNode = cmds.listRelatives(shapeNode[0], fullPath=True , parent=True )
    obj_matrix = OpenMaya.MMatrix(cmds.xform(transformNode, query=True, worldSpace=True, matrix=True))
    face_normals_text = cmds.polyInfo(faceName, faceNormals=True)[0]
    face_normals = [float(digit) for digit in re.findall(r'-?\d*\.\d*', face_normals_text)]
    v = OpenMaya.MVector(face_normals) * obj_matrix
    upvector = OpenMaya.MVector (0,1,0)
    getHitNormal = v
    quat = OpenMaya.MQuaternion(upvector, getHitNormal)
    quatAsEuler = OpenMaya.MEulerRotation()
    quatAsEuler = quat.asEulerRotation()
    rx, ry, rz = math.degrees(quatAsEuler.x), math.degrees(quatAsEuler.y), math.degrees(quatAsEuler.z)
    return rx, ry, rz

def reTarget():
    newTarget = cmds.ls(sl=1,fl=1)
    if len(newTarget) == 1:
        beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)

        #record symmetry
        getSymX = 0
        getSymY = 0
        getSymZ = 0

        if cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
            getSymX =  cmds.getAttr(beseMesh+'.symmetryX')
        if cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
            getSymY =  cmds.getAttr(beseMesh+'.symmetryY')
        if cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
            getSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')


        bakeCutter("all")
        cmds.parent(newTarget, (beseMesh+'_bakeStep'))
        #cmds.delete((beseMesh+'_bakeBaseMesh'))
        cmds.rename((beseMesh+'_bakeBaseMesh'),(beseMesh+'_temp'))
        cmds.parent((beseMesh+'_temp'),w=1)
        cmds.rename(newTarget, (beseMesh+'_bakeBaseMesh'))
        cmds.rename((beseMesh+'_temp'), (beseMesh+'_old'))
        restoreCutter()


        #apply to new target
        if not cmds.attributeQuery('symmetryX', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryX', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryX'),getSymX)
        if not cmds.attributeQuery('symmetryY', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryY', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryY'),getSymY)
        if not cmds.attributeQuery('symmetryZ', node = beseMesh, ex=True ):
            cmds.addAttr(beseMesh, ln='symmetryZ', at = "long" )
            cmds.setAttr((beseMesh+'.symmetryZ'),getSymZ)

        #hide all cage
        cageList = cmds.ls((beseMesh + '_cage*'),type='transform')
        for c in cageList:
            cmds.setAttr((c+'.visibility'),0)

        #checkSymmetryState
        checkSymX =  cmds.getAttr(beseMesh+'.symmetryX')
        checkSymY =  cmds.getAttr(beseMesh+'.symmetryY')
        checkSymZ =  cmds.getAttr(beseMesh+'.symmetryZ')

        if checkSymX == 1:
            boolSymmetry('x',1)
        elif checkSymX == -1:
            boolSymmetry('x',2)

        if checkSymY == 1:
            boolSymmetry('y',1)
        elif checkSymY == -1:
            boolSymmetry('y',2)

        if checkSymZ == 1:
            boolSymmetry('z',1)
        elif checkSymZ == -1:
            boolSymmetry('z',2)

def getPolyFaceCenter(faceName):
    meshFaceName = faceName.split('.')[0]
    findVtx = cmds.polyInfo(faceName, fv=1)
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
        x,y,z = cmds.pointPosition((meshFaceName + '.vtx['+g + ']'),w=1)
        centerX = centerX + x
        centerY = centerY + y
        centerZ = centerZ + z

    centerX = centerX/len(getNumber)
    centerY = centerY/len(getNumber)
    centerZ = centerZ/len(getNumber)
    return centerX,centerY,centerZ

def meshBBox():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if beseMesh is not None:
        mesh = (beseMesh +'_bool')
        if cmds.objExists(mesh):
            bbox= cmds.xform(mesh, q=1, ws=1, bb=1)
            length=math.sqrt((math.pow(bbox[0]-bbox[3],2)+math.pow(bbox[1]-bbox[4],2)+math.pow(bbox[2]-bbox[5],2))/3)
            bestV = length / 10
            cmds.floatField( 'cuterPreSize' , e=True ,value=bestV )
            loadSymmetryState()

def checkBaseMeshList():    
    beseMesh = cmds.optionMenu('baseMeshMenu', query=True, ils=True)
    if beseMesh is not None:
        for c in beseMesh:
            if not 'NoBaseMeshMenu' in c:
                meshName = c.replace('Menu', 'BoolGrp')
                if cmds.objExists(meshName) == 0:
                    cmds.deleteUI(c)
    beseMeshCheck = cmds.ls('*BoolGrp', type='transform')
    if len(beseMeshCheck) > 0:
        checkBaseList = cmds.optionMenu('baseMeshMenu', query=True, ils=True)
        for b in beseMeshCheck:
            removeGrp = b.replace('BoolGrp', '')
            checkSelMesh = cmds.menuItem((removeGrp + "Menu"), q=True, ex=True)
            if checkSelMesh == 0:
                cmds.menuItem((removeGrp + "Menu"), label=removeGrp, p='baseMeshMenu')
    beseMesh = cmds.optionMenu('baseMeshMenu', query=True, ils=True)
    if beseMesh is not None:
        if len(beseMesh) > 1:
            checkNoBase = cmds.menuItem('NoBaseMeshMenu', q=True, ex=True)
            if checkNoBase == 1:
                cmds.deleteUI("NoBaseMeshMenu")
    else:
        cmds.menuItem("NoBaseMeshMenu", label='No Base Mesh', p='baseMeshMenu')
    meshBBox()
    allLayers = cmds.ls(type='displayLayer')
    for a in allLayers:
        if not 'defaultLayer' in a:
            members = cmds.editDisplayLayerMembers(a, query=True)
            if members == None:
                cmds.delete(a)


def updateSnapState():
        #check snap border state
    cmds.makeLive( none=True )
    cmds.manipMoveContext('Move',e=True, snapLivePoint= False)
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    cmds.button('borderAlginButton',e=True, bgc =  [0.28,0.28,0.28])
    if cmds.objExists(beseMesh +'_borderBoxGrp') and cmds.objExists(beseMesh +'_borderBox'):
        cmds.button('borderAlginButton',e=True, bgc =  [0.3,0.5,0.6])
        cmds.makeLive(  beseMesh +'_borderBox' )
        cmds.manipMoveContext('Move',e=True, snapLivePoint= True)

def restoreMissingGrps():
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
        cmds.CreateEmptyGroup()
        cmds.rename((beseMesh +'_cutterGrp'))
        cmds.parent((beseMesh +'_cutterGrp'),(beseMesh +'BoolGrp'))


def setCutterBaseMesh():
    beseMesh = cmds.ls(sl=True,fl=True,type='transform')
    if len(beseMesh) == 1:
        cmds.delete(beseMesh[0],ch=1)
        #cmds.makeIdentity(beseMesh[0],apply= True, t= 1, r =1, s =1, n= 0,pn=1)
        cmds.editDisplayLayerMembers('defaultLayer',beseMesh[0])
        topNode = mel.eval('rootOf '+beseMesh[0])
        meshName = []
        if 'BoolGrp' in topNode:
            removeGrp = topNode.replace('BoolGrp','')
            removeParent = removeGrp.replace('|','')
            meshName = removeParent
        else:
            meshName =  beseMesh[0]
        meshName = meshName.replace('|','')
        checkSelMesh = cmds.menuItem((meshName +"Menu"), q=True, ex = True)
        if checkSelMesh == 0:
            cmds.menuItem((meshName +"Menu"), label = meshName ,p = 'baseMeshMenu')
            #cmds.optionMenu('baseMeshMenu|OptionMenu', q=True, v=True) # to get the name of the current value
            #cmds.optionMenu('baseMeshMenu|OptionMenu', q=True, sl=True) # to get the current index
            #cmds.optionMenu('baseMeshMenu|OptionMenu', e=True, sl = 3 )# to change the current value
            cmds.optionMenu('baseMeshMenu', e=True, v = meshName )# to change the current value
    beseMesh = cmds.optionMenu('baseMeshMenu', query = True, v = True)
    if beseMesh != 'No Base Mesh':
        if cmds.objExists(beseMesh):
            checkPivot = cmds.xform(beseMesh, q =True, sp=True,ws=True)
            if cmds.objExists((beseMesh +'_cutterGrp')) == 0:
                cmds.CreateEmptyGroup()
                cmds.rename((beseMesh +'_cutterGrp'))
            if cmds.objExists((beseMesh +'BoolGrp')) == 0:
                cmds.CreateEmptyGroup()
                cmds.rename((beseMesh +'BoolGrp'))
            if cmds.objExists((beseMesh +'_bool')) ==0:
                cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
                cmds.rename(beseMesh +'_preSubBox')
                cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
                cmds.rename(beseMesh +'_afterSubBox')
                cmds.polyCube(w = 0.0001, h=0.0001, d=0.0001 ,sx =1 ,sy= 1, sz= 1)
                cmds.rename(beseMesh +'_preUnionBox')
                #move pre box to base mesh center prevent error
                bbox= cmds.xform(beseMesh, q=1, ws=1, bb=1)
                bX = (bbox[3]-bbox[0])/2 + bbox[0]
                bY = (bbox[4]-bbox[1])/2 + bbox[1]
                bZ = (bbox[5]-bbox[2])/2 + bbox[2]
                attrList = ['translateX','translateY','translateZ']
                preBoxList = [(beseMesh +'_preSubBox'),(beseMesh +'_afterSubBox'),(beseMesh +'_preUnionBox')]
                posList = [bX,bY,bZ]
                for p in preBoxList:
                    for i in range(0,3):
                        cmds.setAttr(( p + '.' + attrList[i]),posList[i])
                subNode= cmds.polyCBoolOp((beseMesh ), (beseMesh +'_preSubBox') , op= 2, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_bool'))
                cmds.rename(subNode[0],(beseMesh +'_myBoolSub'))
                unionNode = cmds.polyCBoolOp((beseMesh +'_myBoolSub'), (beseMesh +'_preUnionBox') , op= 1, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_union'))
                cmds.rename(unionNode[0],(beseMesh +'_myBoolUnion'))
                subNode= cmds.polyCBoolOp((beseMesh +'_myBoolUnion'), (beseMesh +'_afterSubBox') , op= 2, ch= 1, preserveColor= 0, classification= 1, name= (beseMesh +'_bool'))
                cmds.rename(subNode[0],(beseMesh +'_bool'))
                boolNode = cmds.listConnections(cmds.listHistory((beseMesh +'_bool'),f=1,ac=1),type='polyCBoolOp')
                boolNode = set(boolNode)
                #hack it by check '_', this is used by other group
                listClean = []
                for b in boolNode:
                    if '_' not in b:
                        listClean.append(b)

                for l in listClean:
                    checkNodeType = cmds.nodeType(l)
                    if checkNodeType == 'polyCBoolOp':
                        checkOp = cmds.getAttr( l +'.operation')
                        if checkOp == 2:
                            if cmds.objExists(beseMesh +'_mySubs'):
                                cmds.rename(l,(beseMesh +'_myCut'))
                            else:
                                cmds.rename(l,(beseMesh +'_mySubs'))
                        else:
                            cmds.rename(l,(beseMesh +'_myUnion'))

                baseNodes = cmds.listRelatives(beseMesh, ad = True, f = True)
                baseTransNode = cmds.ls(baseNodes,type = 'transform')
                baseMeshNode = cmds.ls(baseNodes,type = 'mesh')
                cmds.setAttr((baseMeshNode[0]+'.intermediateObject'), 0)
                cmds.parent(baseMeshNode[0],(beseMesh +'BoolGrp'),s=True)
                cmds.delete(beseMesh)
                cmds.pickWalk(d='up')
                cmds.rename(beseMesh)
                cmds.setAttr((beseMesh + '.visibility'), 0)
            if not cmds.objExists((beseMesh +'_BoolResult')):
                cmds.createDisplayLayer(name = (beseMesh +'_BoolResult'))
            cmds.editDisplayLayerMembers( (beseMesh +'_BoolResult'),(beseMesh +'_bool')) # store my selection into the display layer
            cmds.setAttr((beseMesh +'_BoolResult.displayType'),2)

            checkList = ['_cutterGrp','_preSubBox','_preUnionBox','_myBoolUnion','_bool', '', '_afterSubBox','_myBoolSub' ]
            for c in checkList:
                checkGrp = cmds.ls((beseMesh + c), l=True)
                if len(checkGrp)>0:
                    if 'BoolGrp' not in checkGrp[0]:
                        cmds.parent(checkGrp[0],(beseMesh +'BoolGrp'))

            cmds.select(cl=True)
            cmds.setAttr((beseMesh +'BoolGrp.visibility'),1)
            cmds.move(checkPivot[0],checkPivot[1],checkPivot[2], (beseMesh + ".scalePivot"),(beseMesh + ".rotatePivot"), absolute=True)
            meshBBox()
    else:
        removeNotExistBaseMesh()

if __name__ == "__main__":
    run()
