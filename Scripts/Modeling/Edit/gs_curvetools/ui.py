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

import os
from functools import partial as pa
from imp import reload

import maya.cmds as mc
import maya.OpenMayaUI as omui
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance

from . import core, uv_editor
from .constants import *
from .utils import gs_math as mt
from .utils import style, tooltips, utils, wrap
from .utils.utils import deferred, noUndo, undo
from .utils.wrap import WIDGETS

reload(core)
reload(uv_editor)
reload(utils)
reload(wrap)
reload(style)

MESSAGE = utils.logger
LOGGER = utils.logger.logger

# Maya Main Window and Workspace


def mayaMainWindow():
    """ Get Maya main window pointer"""
    mayaWindow = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QMainWindow)
    return mayaWindow


def mayaWorkspaceControl(name, label, retain=True, iw=164, ih=783, widthProperty='preferred'):
    """ Create Maya Dockable Workspace """
    try:
        control = mc.workspaceControl(name, l=label, r=retain, li=True, vis=True, wp=widthProperty, iw=iw, ih=ih, mw=iw, mh=100)
    except BaseException:
        LOGGER.debug("Using legacy workspace control")
        control = mc.workspaceControl(name, l=label, r=retain, li=True, vis=True, wp=widthProperty, iw=iw, ih=ih, mw=iw)
    qtControl = omui.MQtUtil.findControl(control)
    dock = wrapInstance(int(qtControl), QtWidgets.QWidget)
    wrap.WIDGETS[name] = dock

    return dock


def curveControlWorkspace():
    if mc.workspaceControl(CURVE_CONTROL_NAME, q=1, ex=1):
        if MAYA_VER >= 2018:
            if not mc.workspaceControl(CURVE_CONTROL_NAME, q=1, vis=1):
                mc.workspaceControl(CURVE_CONTROL_NAME, e=1, rs=1)
                deferred(core.updateMainUI)()
            else:
                mc.workspaceControl(CURVE_CONTROL_NAME, e=1, vis=0)
        else:
            mc.workspaceControl(CURVE_CONTROL_NAME, e=1, fl=1)
            mc.deleteUI(CURVE_CONTROL_NAME)
    else:
        CurveControlUI()
        core.curveControlUI.updateUI()
        from . import main
        main.checkScriptJobs(CURVE_CONTROL_NAME)


class CurveControlUI(QtWidgets.QWidget):

    def __init__(self):
        parent = mayaWorkspaceControl(name=CURVE_CONTROL_NAME,
                                      label=CURVE_CONTROL_LABEL,
                                      retain=False, iw=350, ih=750, widthProperty="free")
        # Dockable Workspace Connection
        super(CurveControlUI, self).__init__(parent)
        self.ui()
        parent.layout().addWidget(self)

    def ui(self):
        # Layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(*style.scale([2, 0, 2, 0]))

        self.scrollWidget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(self.scrollWidget)
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidget(self.scrollWidget)
        mainLayout.addWidget(scrollArea)

        # Layout Settings
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(style.scale(2))
        layout.setMargin(0)
        layout.setAlignment(QtCore.Qt.AlignTop)

        scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        scrollArea.setWidgetResizable(True)

        # Main Controls
        layout.addWidget(wrap.separator())

        # Layer Selector, Color Picker, Curve Name and Line Thickness
        with wrap.Row(layout, 'gsCurveControlHeader') as row:
            layerSelector = wrap.LayerSelector('gsLayerSelector', row.layout())
            layerSelector.setFixedWidth(style.scale(40))
            layerSelector.currentIndexChanged.connect(core.changeLayerViaOptionMenu)

            layerColorPicker = wrap.ColorPicker('gsColorPicker', row.layout())
            layerColorPicker.setContentsMargins(*style.scale([3, 3, 1, 3]))
            layerColorPicker.setFixedWidth(style.scale(20))
            layerColorPicker.connectCommand(core.toggleColor.changeLayerColor)

            curveColorPicker = wrap.ColorPicker('gsCurveColorPicker', row.layout())
            curveColorPicker.setContentsMargins(*style.scale([1, 3, 2, 3]))
            curveColorPicker.setFixedWidth(style.scale(20))
            curveColorPicker.connectCommand(core.toggleColor.changeCurveColor)

            selectedObjectName = wrap.LineEdit('selectedObjectName', row.layout())
            selectedObjectName.setPlaceholderText('Select Curve')
            selectedObjectName.returnPressed.connect(undo(core.renameSelected))

            lineThickness = wrap.FloatField('lineWidth', row.layout())
            lineThickness.setFixedWidth(style.scale(35))
            lineThickness.setRange(-1, 10)
            lineThickness.setValue(-1)
            lineThickness.setDragCommand(pa(core.sliders.curveControlSliderDrag, lineThickness))
            lineThickness.setReleaseCommand(core.sliders.release)

        layout.addWidget(wrap.separator())

        # Select Curves Prompt
        label = wrap.Label(layout, 'selectCurvesPrompt')
        label.setLabel('Select Compatible Curves')
        label.setFontSize(14)
        label.setVisible(False)

        # Axis Control
        with wrap.Column(layout, 'axisFrame') as column:
            label = wrap.Label(column.layout())
            label.setLabel('Axis Control')
            label.setFontSize(14)
            with wrap.Row(column.layout()) as row:
                WIDGETS['Axis'] = axisButtonGrp = QtWidgets.QButtonGroup()

                axisAuto = wrap.Button(row.layout(), 'gsBindAxisAuto')
                axisAuto.setLabel('Auto', lineHeight=100)
                axisAuto.setCheckable(True)
                axisAuto.setButtonStyle('small')
                axisAuto.setChecked(True)
                axisAuto.clicked.connect(pa(undo(core.applyAxis), 0))

                axisX = wrap.Button(row.layout(), 'gsBindAxisX')
                axisX.setLabel('X', lineHeight=100)
                axisX.setCheckable(True)
                axisX.setButtonStyle('small')
                axisX.clicked.connect(pa(undo(core.applyAxis), 1))

                axisY = wrap.Button(row.layout(), 'gsBindAxisY')
                axisY.setLabel('Y', lineHeight=100)
                axisY.setCheckable(True)
                axisY.setButtonStyle('small')
                axisY.clicked.connect(pa(undo(core.applyAxis), 2))

                axisZ = wrap.Button(row.layout(), 'gsBindAxisZ')
                axisZ.setLabel('Z', lineHeight=100)
                axisZ.setCheckable(True)
                axisZ.setButtonStyle('small')
                axisZ.clicked.connect(pa(undo(core.applyAxis), 3))

                axisButtonGrp.addButton(axisAuto, 0)
                axisButtonGrp.addButton(axisX, 1)
                axisButtonGrp.addButton(axisY, 2)
                axisButtonGrp.addButton(axisZ, 3)

                axisFlip = wrap.Button(row.layout(), 'AxisFlip')
                axisFlip.setLabel('Flip', lineHeight=100)
                axisFlip.setCheckable(True)
                axisFlip.setButtonStyle('small')
                axisFlip.clicked.connect(pa(undo(core.applyAxis), -1))

            column.layout().addWidget(wrap.separator())

            # Edit Original Objects
            with wrap.Row(column.layout(), margins=style.scale([0, 0, 0, 0]), objName='originalCurvesRow') as originalCurvesRow:
                selectOriginalCurves = wrap.Button(originalCurvesRow.layout(), 'selectOriginalCurves')
                selectOriginalCurves.setLabel('Select Original Curves', lineHeight=100)
                selectOriginalCurves.setButtonStyle('small-filled')
                selectOriginalCurves.clicked.connect(undo(core.curveControlUI.selectOriginalObjects))

                editOrigObj = wrap.Button(originalCurvesRow.layout(), 'editOrigObj')
                editOrigObj.setLabel('Edit Original Objects', lineHeight=100)
                editOrigObj.setCheckable(True)
                editOrigObj.setButtonStyle('small')
                editOrigObj.clicked.connect(undo(core.curveControlUI.editOriginalObjects))

            column.layout().addWidget(wrap.separator())

        # Length Divisions
        with wrap.Row(layout, margins=style.scale([0, 0, 3, 0])) as lengthDivisionsRow:
            lengthDivision = wrap.ControlSlider(objName='lengthDivisions', typ='int')
            lengthDivision.setLabel('L-Div')
            lengthDivision.setMinMax(2, 100)
            lengthDivision.setFieldMinMax(2, 10000)
            lengthDivision.setValue(2)
            lengthDivision.setDragCommand(pa(core.sliders.curveControlSliderDrag, lengthDivision))
            lengthDivision.setReleaseCommand(core.sliders.release)

            dynamicDivisionsToggle = wrap.Button(objName='dynamicDivisions')
            dynamicDivisionsToggle.setLabel('Auto')
            dynamicDivisionsToggle.setFixedWidth(style.scale(35))
            dynamicDivisionsToggle.setButtonStyle('small')
            dynamicDivisionsToggle.setCheckable(True)
            dynamicDivisionsToggle.clicked.connect(undo(core.toggleDynamicDivisions))

            lengthDivisionsRow.layout().addWidget(lengthDivision, 4)
            lengthDivisionsRow.layout().addWidget(dynamicDivisionsToggle, 1)

        # Width Divisions
        widthDivision = wrap.ControlSlider(layout, 'widthDivisions', 'int')
        widthDivision.setLabel('W-Div')
        widthDivision.setMinMax(2, 31)
        widthDivision.setFieldMinMax(2, 10000)
        widthDivision.setValue(2)
        widthDivision.setDragCommand(pa(core.sliders.curveControlSliderDrag, widthDivision))
        widthDivision.setReleaseCommand(core.sliders.release)

        # Orientation
        orientation = wrap.ControlSlider(layout, 'Orientation', 'float')
        orientation.setLabel('Orien')
        orientation.setMinMax(-180, 180)
        orientation.setFieldMinMax(-36000, 36000)
        orientation.setPrecision(1)
        orientation.setStep(0.5)
        orientation.setDragCommand(pa(core.sliders.curveControlSliderDrag, orientation))
        orientation.setReleaseCommand(core.sliders.release)

        # Twist
        twist = wrap.ControlSlider(layout, 'Twist', 'float')
        twist.setLabel('Twist')
        twist.setMinMax(-180, 180)
        twist.setFieldMinMax(-36000, 36000)
        twist.setPrecision(1)
        twist.setStep(0.5)
        twist.setDragCommand(pa(core.sliders.curveControlSliderDrag, twist))
        twist.setReleaseCommand(core.sliders.release)

        # Twist
        invTwist = wrap.ControlSlider(layout, 'invTwist', 'float')
        invTwist.setLabel('Inv.Twist')
        invTwist.setMinMax(-180, 180)
        invTwist.setFieldMinMax(-36000, 36000)
        invTwist.setPrecision(1)
        invTwist.setStep(0.5)
        invTwist.setDragCommand(pa(core.sliders.curveControlSliderDrag, invTwist))
        invTwist.setReleaseCommand(core.sliders.release)

        # Twist Curve Graph
        with wrap.Frame(layout, 'twistCurveFrame', margins=[0, 1, 0, 2]) as twistCurveFrame:
            twistCurveFrame.frameButton.setLabel('Twist Curve Graph')
            twistGraph = wrap.FallOffCurve(twistCurveFrame.getFrameLayout(), 'twistCurve')

            def twistGraphCommand(_):  # BUG: When undoing multiple edits, last edit is not reverted
                core.attributes.propagateGraphs(twistGraph)
                core.attributes.storeGraphs(twistGraph)
            twistGraph.changeCommand(twistGraphCommand)

            with wrap.Row(twistCurveFrame.getFrameLayout(), margins=style.scale([5, 0, 5, 2])) as row:
                row.setFixedHeight(style.BUTTON_HEIGHT)

                magnitude = wrap.FloatField('Magnitude', row.layout())
                magnitude.setFixedWidth(style.scale(45))
                magnitude.setRange(-99, 99)
                magnitude.setStep(0.01)
                magnitude.setPrecision(2)
                magnitude.setDragCommand(pa(core.sliders.curveControlSliderDrag, magnitude))
                magnitude.setReleaseCommand(core.sliders.release)

                resetButton = wrap.Button(row.layout(), 'gsTwistGraphResetButton')
                resetButton.setLabel('Reset Curve')

                def resetTwistCmd():
                    utils.resetSingleGraph('twist')
                    core.attributes.storeGraphs(twistGraph)
                resetButton.clicked.connect(undo(resetTwistCmd))

                popOutButton = wrap.Button(row.layout(), 'gsTwistGraphPopOut')
                popOutButton.setFixedWidth(style.scale(56))
                popOutButton.setLabel('^')
                popOutButton.clicked.connect(self.twistGraphPopOut)

        # Width
        width = wrap.ControlSlider(layout, 'Width', 'float')
        width.setLabel('Width')
        width.setMinMax(0.001, 5)
        width.setFieldMinMax(0.001, 1000)
        width.setPrecision(3)
        width.setStep(0.001)
        width.setValue(1)
        width.setDragCommand(pa(core.sliders.curveControlSliderDrag, width))
        width.setReleaseCommand(core.sliders.release)

        # Taper
        taper = wrap.ControlSlider(layout, 'Taper', 'float')
        taper.setLabel('Taper')
        taper.setMinMax(0.001, 3)
        taper.setFieldMinMax(0.001, 1000)
        taper.setPrecision(3)
        taper.setStep(0.001)
        taper.setValue(1)
        taper.setDragCommand(pa(core.sliders.curveControlSliderDrag, taper))
        taper.setReleaseCommand(core.sliders.release)

        # Width for Tubes
        with wrap.Row(layout, objName='widthComboSlider', spacing=0) as row:
            with wrap.Column(row.layout()) as column:
                widthX = wrap.ControlSlider(column.layout(), "WidthX", 'float')
                widthX.setLabel("WidthX")
                widthX.setMinMax(0.001, 5)
                widthX.setFieldMinMax(0.001, 1000)
                widthX.setPrecision(3)
                widthX.setStep(0.001)
                widthX.setValue(1)
                widthX.setDragCommand(pa(core.sliders.curveControlSliderDrag, widthX))
                widthX.setReleaseCommand(core.sliders.release)

                widthZ = wrap.ControlSlider(column.layout(), "WidthZ", 'float')
                widthZ.setLabel("WidthZ")
                widthZ.setMinMax(0.001, 5)
                widthZ.setFieldMinMax(0.001, 1000)
                widthZ.setPrecision(3)
                widthZ.setStep(0.001)
                widthZ.setValue(1)
                widthZ.setDragCommand(pa(core.sliders.curveControlSliderDrag, widthZ))
                widthZ.setReleaseCommand(core.sliders.release)

            lockButton = wrap.IconCheckButton(row.layout(), 'widthLockSwitch')
            lockButton.setIcons(utils.getFolder.icons() + 'sliderLock_en_reversed.png',
                                utils.getFolder.icons() + 'sliderLock_reversed.png')
            lockButton.setIconWidthHeight(10, 30)
            lockButton.setChecked(True)

        # Width Curve Graph
        with wrap.Frame(layout, 'widthCurveFrame', margins=[0, 1, 0, 2]) as widthCurveFrame:
            widthCurveFrame.frameButton.setLabel('Width Curve Graph')
            widthGraph = wrap.FallOffCurve(widthCurveFrame.getFrameLayout(), 'scaleCurve')

            def widthGraphCommand(_):  # BUG: When undoing multiple edits, last edit is not reverted
                core.attributes.propagateGraphs(widthGraph)
                core.attributes.storeGraphs(widthGraph)
            widthGraph.changeCommand(widthGraphCommand)

            with wrap.Row(widthCurveFrame.getFrameLayout(), margins=style.scale([5, 0, 5, 2])) as row:
                row.setFixedHeight(style.BUTTON_HEIGHT)

                resetButton = wrap.Button(row.layout(), 'gsWidthGraphResetButton')
                resetButton.setLabel('Reset Curve')

                def resetWidthCmd():
                    utils.resetSingleGraph('scale')
                    core.attributes.storeGraphs(widthGraph)
                resetButton.clicked.connect(undo(resetWidthCmd))

                popOutButton = wrap.Button(row.layout(), 'gsWidthGraphPopOut')
                popOutButton.setFixedWidth(style.scale(56))
                popOutButton.setLabel('^')
                popOutButton.clicked.connect(self.widthGraphPopOut)

        # Length Unlock Switch
        lengthUnlock = wrap.Button(layout, 'LengthLock')
        lengthUnlock.setLabel('Length Unlock', lineHeight=100)
        lengthUnlock.setCheckable(True)
        lengthUnlock.setButtonStyle('small')
        lengthUnlock.setFixedWidth(style.scale(106))
        lengthUnlock.clicked.connect(pa(core.curveControlCheckBoxes, 2))

        # Length
        length = wrap.ControlSlider(layout, 'Length', 'float')
        length.setLabel('Length')
        length.setMinMax(0.001, 3)
        length.setFieldMinMax(-1000, 1000)
        length.setPrecision(3)
        length.setStep(0.001)
        length.setValue(1)
        length.setDragCommand(pa(core.sliders.curveControlSliderDrag, length))
        length.setReleaseCommand(core.sliders.release)

        # TODO: Offset card from curve attribute
        # Offset
        offset = wrap.ControlSlider(layout, 'Offset', 'float')
        offset.setLabel('Offset')
        offset.setMinMax(-1, 1)
        offset.setFieldMinMax(-30, 30)
        offset.setStep(0.001)
        offset.setValue(1)
        offset.setDragCommand(pa(core.sliders.curveControlSliderDrag, offset))
        offset.setReleaseCommand(core.sliders.release)

        # Profile
        profile = wrap.ControlSlider(layout, 'Profile', 'float')
        profile.setLabel('Profile')
        profile.setMinMax(-2, 2)
        profile.setFieldMinMax(-1000, 1000)
        profile.setStep(0.001)
        profile.setDragCommand(pa(core.sliders.curveControlSliderDrag, profile))
        profile.setReleaseCommand(core.sliders.release)

        # Profile Curve Graph
        with wrap.Frame(layout, 'profileCurveGraph', margins=[0, 1, 0, 2]) as profileCurveFrame:
            profileCurveFrame.frameButton.setLabel('Profile Curve Graph')
            profileGraph = wrap.FallOffCurve(profileCurveFrame.getFrameLayout(), 'profileCurve', attr=False)

            def changeCommand(value):
                core.updateLattice(value)
                core.equalizeProfileCurve()
                core.attributes.storeGraphs(profileGraph)
            profileGraph.changeCommand(changeCommand)

            profileSmoothingSlider = wrap.ControlSlider(profileCurveFrame.getFrameLayout(), 'profileSmoothing', 'int')
            profileSmoothingSlider.setLabel('Smoothing')
            profileSmoothingSlider.setMinMax(2, 30)
            profileSmoothingSlider.setValue(2)
            profileSmoothingSlider.setDragCommand(pa(core.sliders.curveControlSliderDrag, profileSmoothingSlider))
            profileSmoothingSlider.setReleaseCommand(core.sliders.release)

            with wrap.Row(profileCurveFrame.getFrameLayout(), margins=style.scale([5, 0, 5, 2])) as row:
                row.setFixedHeight(style.BUTTON_HEIGHT)

                profileMagnitude = wrap.FloatField('profileMagnitude', row.layout())
                profileMagnitude.setFixedWidth(style.scale(45))
                profileMagnitude.setValue(1)
                profileMagnitude.setRange(-2, 2)
                profileMagnitude.setStep(0.01)
                profileMagnitude.setPrecision(2)
                profileMagnitude.setDragCommand(pa(core.sliders.curveControlSliderDrag, profileMagnitude))
                profileMagnitude.setReleaseCommand(core.sliders.release)

                with wrap.Column(row.layout(), spacing=0) as eqColumn:
                    eqColumn.setFixedHeight(style.scale(24))
                    with wrap.Row(eqColumn.layout(), spacing=0) as eqRow:
                        def toggleEq():
                            WIDGETS['equalizeCurveButton'].setDisabled(
                                WIDGETS['autoEqualizeSwitchOn'].isChecked()
                            )
                        autoEqualizeGroup = QtWidgets.QButtonGroup(eqRow.layout())
                        autoEqualizeGroup.buttonClicked.connect(toggleEq)
                        autoEqualizeGroup.buttonClicked.connect(undo(core.equalizeProfileCurve))

                        autoEqualize = wrap.Button(eqRow.layout(), 'autoEqualizeSwitchOn')
                        autoEqualize.setLabel('Auto', lineHeight=100)
                        autoEqualize.setLabelStyle('small')
                        autoEqualize.setButtonStyle('small-compound-top-left')
                        autoEqualize.setCheckable(True)
                        autoEqualize.setChecked(True)

                        autoEqualizeOff = wrap.Button(eqRow.layout(), 'autoEqualizeSwitchOff')
                        autoEqualizeOff.setLabel('Manual', lineHeight=100)
                        autoEqualizeOff.setLabelStyle('small')
                        autoEqualizeOff.setButtonStyle('small-compound-top-right')
                        autoEqualizeOff.setCheckable(True)

                        autoEqualizeGroup.addButton(autoEqualize)
                        autoEqualizeGroup.addButton(autoEqualizeOff)

                    equalizeProfileCurve = wrap.Button(eqColumn.layout(), 'equalizeCurveButton')
                    equalizeProfileCurve.setLabel('Equalize Curve', lineHeight=100)
                    equalizeProfileCurve.setLabelStyle('small')
                    equalizeProfileCurve.setButtonStyle('small-filled-compound-bottom')
                    equalizeProfileCurve.setDisabled(True)
                    equalizeProfileCurve.clicked.connect(pa(undo(core.equalizeProfileCurve), True))

                resetButton = wrap.Button(row.layout(), 'gsResetProfileGraphButton')
                resetButton.setLabel('Reset Curve')

                def resetButtonClicked(*_):
                    core.resetProfileCurve()
                    core.attributes.storeGraphs(profileGraph)
                resetButton.clicked.connect(undo(resetButtonClicked))

                popOutButton = wrap.Button(row.layout(), 'gsProfileGraphPopOut')
                popOutButton.setFixedWidth(style.scale(56))
                popOutButton.setLabel('^')
                popOutButton.clicked.connect(self.profileGraphPopOut)
        # Normals
        normals = wrap.ControlSlider(layout, 'surfaceNormals', 'float')
        normals.setLabel('Normals')
        normals.setMinMax(0, 180)
        normals.setPrecision(1)
        normals.setValue(180)
        normals.setDragCommand(pa(core.sliders.curveControlSliderDrag, normals))
        normals.setReleaseCommand(core.sliders.release)

        # Reverse Normals Switch
        reverseNormals = wrap.Button(layout, 'reverseNormals')
        reverseNormals.setLabel('Reverse Normals', lineHeight=100)
        reverseNormals.setCheckable(True)
        reverseNormals.setButtonStyle('small')
        reverseNormals.setFixedWidth(style.scale(106))
        reverseNormals.clicked.connect(pa(core.curveControlCheckBoxes, 0))

        with wrap.Frame(layout, 'otherFrame', label='Other', margins=[2, 2, 2, 2]) as refineFrame:
            samplingAccuracy = wrap.ControlSlider(parent=refineFrame.getFrameLayout(), objName='samplingAccuracy', typ='float')
            samplingAccuracy.setLabel('SamplAcc')
            samplingAccuracy.setMinMax(0.001, 2)
            samplingAccuracy.setStep(0.01)
            samplingAccuracy.setValue(0.33)
            samplingAccuracy.setDragCommand(pa(core.sliders.curveControlSliderDrag, samplingAccuracy))
            samplingAccuracy.setReleaseCommand(core.sliders.release)
            # Refine
            with wrap.Row(refineFrame.getFrameLayout(), margins=style.scale([0, 0, 3, 0])) as curveRefineRow:
                refine = wrap.ControlSlider(layout, 'curveRefine', 'int')
                refine.setLabel('Refine')
                refine.setMinMax(0, 100)
                refine.setFieldMinMax(0, 10000)
                refine.setValue(20)
                refine.setDragCommand(pa(core.sliders.curveControlSliderDrag, refine))
                refine.setReleaseCommand(core.sliders.release)

                autoRefineToggle = wrap.Button(objName='autoRefine')
                autoRefineToggle.setLabel('Auto')
                autoRefineToggle.setFixedWidth(style.scale(35))
                autoRefineToggle.setButtonStyle('small')
                autoRefineToggle.setCheckable(True)
                autoRefineToggle.clicked.connect(undo(core.toggleAutoRefine))

                curveRefineRow.layout().addWidget(refine, 4)
                curveRefineRow.layout().addWidget(autoRefineToggle, 1)

            # Smooth
            smooth = wrap.ControlSlider(refineFrame.getFrameLayout(), 'curveSmooth', 'float')
            smooth.setLabel('Smooth')
            smooth.setMinMax(0, 10)
            smooth.setDragCommand(pa(core.sliders.curveControlSliderDrag, smooth))
            smooth.setReleaseCommand(core.sliders.release)

        with wrap.Frame(layout, 'orientToNormalsFrame', label='Orient to Normals',
                        margins=[2, 2, 2, 2]) as orientFrame:

            orientFrame.setVisible(False)

            def selectMesh():
                sel = mc.filterExpand(mc.ls(sl=1, l=1), sm=12)
                if not sel:
                    sel = mc.ls(hl=1, o=1, l=1)
                if not sel:
                    MESSAGE.warningInView('Select compatible mesh.')
                    return
                self.meshName.setText(sel[0])

            with wrap.Row(orientFrame.getFrameLayout()) as row:
                selectMeshBtn = wrap.Button(row.layout(), "gsOrientToNormalsSelectTarget")
                selectMeshBtn.setFixedWidth(style.scale(100))
                selectMeshBtn.setLabel('Select Target')
                selectMeshBtn.clicked.connect(selectMesh)

                self.meshName = wrap.LineEdit('gsOrientMeshName', row.layout())
                self.meshName.setPlaceholderText('Select or Type Target Mesh')
                self.meshName.setClearButtonEnabled(True)

            orientFrame.getFrameLayout().addWidget(wrap.separator())

            with wrap.Row(orientFrame.getFrameLayout()) as row:
                iterationsSlider = wrap.ControlSlider(row.layout(), 'gsIterationsSlider', 'int')
                iterationsSlider.setMinMax(1, 100)
                iterationsSlider.setValue(10)
                iterationsSlider.setLabel('Iterations')

                autoRefreshButton = wrap.Button(row.layout(), 'orientRefreshViewport')
                autoRefreshButton.setButtonStyle('small')
                autoRefreshButton.setCheckable(True)
                autoRefreshButton.setChecked(True)
                autoRefreshButton.setWidthHeight(w=style.scale(50))
                autoRefreshButton.setLabel('Refresh VP', lineHeight=100)

            with wrap.Row(orientFrame.getFrameLayout()) as row:
                minAngleSlider = wrap.ControlSlider(row.layout(), 'gsMinimumAngle', 'float')
                minAngleSlider.setMinMax(0.1, 90)
                minAngleSlider.setValue(1)
                minAngleSlider.setLabel('Min Angle')

            orientFrame.getFrameLayout().addWidget(wrap.separator())

            with wrap.Row(orientFrame.getFrameLayout()) as row:
                orient = wrap.Button(row.layout(), 'gsOrientToNormals')
                orient.setLabel('Orient')
                orient.clicked.connect(undo(core.orientToFaceNormals))

        with wrap.Frame(layout, 'solidifyFrame', label='Solidify Controls', margins=[2, 2, 2, 2]) as solidifyFrame:
            # Solidify Activate
            solidify = wrap.Button(solidifyFrame.getFrameLayout(), 'solidify')
            solidify.setLabel('Solidify', lineHeight=100)
            solidify.setCheckable(True)
            solidify.setButtonStyle('small')
            solidify.setFixedWidth(style.scale(106))
            solidify.clicked.connect(pa(core.curveControlCheckBoxes, 1))

            # Thickness
            thickness = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyThickness', 'float')
            thickness.setLabel('Thickness')
            thickness.setMinMax(0.001, 5)
            thickness.setFieldMinMax(-100, 100)
            thickness.setValue(0.25)
            thickness.setStep(0.01)
            thickness.setDragCommand(pa(core.sliders.curveControlSliderDrag, thickness))
            thickness.setReleaseCommand(core.sliders.release)

            # Divisions
            divisions = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyDivisions', 'int')
            divisions.setLabel('Divisions')
            divisions.setMinMax(0, 10)
            divisions.setFieldMinMax(0, 100)
            divisions.setDragCommand(pa(core.sliders.curveControlSliderDrag, divisions))
            divisions.setReleaseCommand(core.sliders.release)

            # ScaleX
            solidifyScaleX = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyScaleX', 'float')
            solidifyScaleX.setLabel('ScaleX')
            solidifyScaleX.setMinMax(-10, 10)
            solidifyScaleX.setFieldMinMax(-100, 100)
            solidifyScaleX.setDragCommand(pa(core.sliders.curveControlSliderDrag, solidifyScaleX))
            solidifyScaleX.setReleaseCommand(core.sliders.release)

            # ScaleY
            solidifyScaleY = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyScaleY', 'float')
            solidifyScaleY.setLabel('ScaleY')
            solidifyScaleY.setMinMax(-10, 10)
            solidifyScaleY.setFieldMinMax(-100, 100)
            solidifyScaleY.setDragCommand(pa(core.sliders.curveControlSliderDrag, solidifyScaleY))
            solidifyScaleY.setReleaseCommand(core.sliders.release)

            # Offset
            offset = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyOffset', 'float')
            offset.setLabel('Offset')
            offset.setMinMax(-10, 10)
            offset.setFieldMinMax(-100, 100)
            offset.setDragCommand(pa(core.sliders.curveControlSliderDrag, offset))
            offset.setReleaseCommand(core.sliders.release)

            # Normals
            solidifyNormals = wrap.ControlSlider(solidifyFrame.getFrameLayout(), 'solidifyNormals', 'float')
            solidifyNormals.setLabel('SNormals')
            solidifyNormals.setMinMax(0, 180)
            solidifyNormals.setPrecision(1)
            solidifyNormals.setValue(180)
            solidifyNormals.setDragCommand(pa(core.sliders.curveControlSliderDrag, solidifyNormals))
            solidifyNormals.setReleaseCommand(core.sliders.release)

        with wrap.Frame(layout, 'UVFrame', label='UV Controls', margins=[2, 2, 2, 2]) as UVFrame:
            flipUV = wrap.Button(UVFrame.getFrameLayout(), 'flipUV')
            flipUV.setLabel('H-Flip UV', lineHeight=100)
            flipUV.setCheckable(True)
            flipUV.setButtonStyle('small')
            flipUV.setFixedWidth(style.scale(106))
            flipUV.clicked.connect(pa(undo(core.curveControlCheckBoxes), 3))

            # Move U
            moveU = wrap.ControlSlider(UVFrame.getFrameLayout(), 'moveU', 'float')
            moveU.setLabel('MoveU')
            moveU.setMinMax(-0.5, 0.5)
            moveU.setStep(0.001)
            moveU.setFieldMinMax(-100, 100)
            moveU.setDragCommand(pa(core.sliders.curveControlSliderDrag, moveU))
            moveU.setReleaseCommand(core.sliders.release)

            # Move V
            moveV = wrap.ControlSlider(UVFrame.getFrameLayout(), 'moveV', 'float')
            moveV.setLabel('MoveV')
            moveV.setMinMax(-0.5, 0.5)
            moveV.setStep(0.001)
            moveV.setFieldMinMax(-100, 100)
            moveV.setDragCommand(pa(core.sliders.curveControlSliderDrag, moveV))
            moveV.setReleaseCommand(core.sliders.release)

            # Scale U
            scaleU = wrap.ControlSlider(UVFrame.getFrameLayout(), 'scaleU', 'float')
            scaleU.setLabel('ScaleU')
            scaleU.setMinMax(0.001, 1.999)
            scaleU.setFieldMinMax(0, 100)
            scaleU.setStep(0.001)
            scaleU.setValue(1)
            scaleU.setDragCommand(pa(core.sliders.curveControlSliderDrag, scaleU))
            scaleU.setReleaseCommand(core.sliders.release)

            # Scale V
            scaleV = wrap.ControlSlider(UVFrame.getFrameLayout(), 'scaleV', 'float')
            scaleV.setLabel('ScaleV')
            scaleV.setMinMax(0.001, 1.999)
            scaleV.setFieldMinMax(0, 100)
            scaleV.setStep(0.001)
            scaleV.setValue(1)
            scaleV.setDragCommand(pa(core.sliders.curveControlSliderDrag, scaleV))
            scaleV.setReleaseCommand(core.sliders.release)

            # Rotate UV
            rotateUV = wrap.ControlSlider(UVFrame.getFrameLayout(), 'rotateUV', 'float')
            rotateUV.setLabel('RotUV')
            rotateUV.setMinMax(-180, 180)
            rotateUV.setFieldMinMax(-3600, 3600)
            rotateUV.setPrecision(2)
            rotateUV.setDragCommand(pa(core.sliders.curveControlSliderDrag, rotateUV))
            rotateUV.setReleaseCommand(core.sliders.release)

            # Rotate UV Root (Legacy)
            rotateUVRoot = wrap.ControlSlider(UVFrame.getFrameLayout(), 'rotateRootUV', 'float')
            rotateUVRoot.setLabel('RotRtUV')
            rotateUVRoot.setMinMax(-180, 180)
            rotateUVRoot.setFieldMinMax(-3600, 3600)
            rotateUVRoot.setPrecision(2)
            rotateUVRoot.setDragCommand(pa(core.sliders.curveControlSliderDrag, rotateUVRoot))
            rotateUVRoot.setReleaseCommand(core.sliders.release)
            rotateUVRoot.setVisible(False)

            # Rotate Tip UV (Legacy)
            rotateUVTip = wrap.ControlSlider(UVFrame.getFrameLayout(), 'rotateTipUV', 'float')
            rotateUVTip.setLabel('RotTipUV')
            rotateUVTip.setMinMax(-180, 180)
            rotateUVTip.setFieldMinMax(-3600, 3600)
            rotateUVTip.setPrecision(2)
            rotateUVTip.setDragCommand(pa(core.sliders.curveControlSliderDrag, rotateUVTip))
            rotateUVTip.setReleaseCommand(core.sliders.release)
            rotateUVRoot.setVisible(False)

            # UV Bug Message
            if MAYA_VER in [2020, 2022] and not mc.optionVar(q='GSCT_UVBugMessageDismissed'):
                with wrap.Row(UVFrame.getFrameLayout()) as row:
                    label = wrap.Label(row.layout())
                    label.setLabel('<p style="color:#FF542F">How To Fix Maya 2020-2022 UV Bug:</p>')

                    linkButton = wrap.Button(row.layout())
                    linkButton.setLabel('Open Fix')
                    linkButton.setButtonStyle('small-filled')
                    linkButton.clicked.connect(lambda: utils.openLink(
                        'https://gs-curvetools.readthedocs.io/en/latest/faq.html#maya-2020-2022-and-broken-uvs'))

                    dismissMessage = wrap.Button(row.layout())
                    dismissMessage.setLabel('Dismiss')
                    dismissMessage.setButtonStyle('small-filled')
                    dismissMessage.clicked.connect(lambda: row.setHidden(True))
                    dismissMessage.clicked.connect(lambda: mc.optionVar(iv=['GSCT_UVBugMessageDismissed', 1]))

        # Advanced Visibility Frame
        with wrap.Frame(layout, 'advancedVisibilityFrame', label='Advanced Visibility',
                        margins=style.scale([3, 2, 3, 2]), spacing=style.scale(3)) as visibilityFrame:
            with wrap.Row(visibilityFrame.getFrameLayout()) as row:

                geometryHighlight = wrap.Button(row.layout(), 'geometryHighlight')
                geometryHighlight.setLabel('Geometry Highlight', lineHeight=100)
                geometryHighlight.setCheckable(True)
                geometryHighlight.setChecked(bool(mc.optionVar(q="GSCT_GeometryHighlightEnabled")))
                geometryHighlight.setButtonStyle('small')

                geometryHighlight.clicked.connect(noUndo(core.advancedVisibility.geometryHighlightCommand))

                curveHighlight = wrap.Button(row.layout(), 'curveHighlight')
                curveHighlight.setLabel('Curve Highlight', lineHeight=100)
                curveHighlight.setCheckable(True)
                curveHighlight.setButtonStyle('small')
                curveHighlight.setChecked(False)
                curveHighlight.clicked.connect(undo(core.advancedVisibility.toggleCurveHighlightFromUI))

            visibilityFrame.getFrameLayout().addWidget(wrap.separator())

            def sliderChangeCommand(*_):
                core.advancedVisibility.applySettingsToNode()
                core.advancedVisibility.saveSettingsFromUI()

            with wrap.Column(visibilityFrame.getFrameLayout(), objName='gsCurveHighlightFrame', spacing=style.scale(4)) as column:
                column.setEnabled(False)  # Disable immediately. We are going to check its state later.

                # CV Size
                with wrap.Row(column.layout(), spacing=4) as row:
                    CVsizeLabel = wrap.Label()
                    CVsizeLabel.setLabel("CV Size:")
                    CVsizeLabel.setFixedWidth(style.scale(100))
                    CVsizeLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    pointSizeSlider = wrap.mayaSlider(
                        mc.floatSliderGrp(
                            'gsPointSizeSlider',
                            f=1, adj=2, w=1, cw=[1, 45], min=1, max=100, v=10,
                            dc=lambda _: noUndo(core.advancedVisibility.applySettingsToNode)(),
                            cc=noUndo(sliderChangeCommand),
                        )
                    )
                    WIDGETS['gsPointSizeSlider'] = pointSizeSlider

                    row.layout().addWidget(CVsizeLabel, 0)
                    row.layout().addWidget(pointSizeSlider, 1)

                # Selected Color
                with wrap.Row(column.layout(), spacing=style.scale(4)) as row:
                    selectedColorLabel = wrap.Label()
                    selectedColorLabel.setLabel("Selected Color:")
                    selectedColorLabel.setFixedWidth(style.scale(100))
                    selectedColorLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    selectedColorPicker = wrap.ColorPicker("gsSelectedCVColor")
                    selectedColorPicker.connectDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    selectedColorPicker.connectCommand(noUndo(sliderChangeCommand))

                    selectedAlphaValue = wrap.FloatField("gsSelectedCVAlpha")
                    selectedAlphaValue.setFixedWidth(style.scale(45))
                    selectedAlphaValue.setValue(1.0)
                    selectedAlphaValue.setRange(0, 1)
                    selectedAlphaValue.setStep(0.01)
                    selectedAlphaValue.setPrecision(2)
                    selectedAlphaValue.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    selectedAlphaValue.setReleaseCommand(noUndo(sliderChangeCommand))

                    row.layout().addWidget(selectedColorLabel, 0)
                    row.layout().addWidget(selectedColorPicker, 1)
                    row.layout().addWidget(selectedAlphaValue, 0)

                # Deselected Color
                with wrap.Row(column.layout(), spacing=style.scale(4)) as row:
                    deselectedColorLabel = wrap.Label()
                    deselectedColorLabel.setLabel("Deselected Color:")
                    deselectedColorLabel.setFixedWidth(style.scale(100))
                    deselectedColorLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    deselectedColorPicker = wrap.ColorPicker("gsDeselectedCVColor")
                    deselectedColorPicker.connectDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    deselectedColorPicker.connectCommand(noUndo(sliderChangeCommand))

                    deselectedAlphaValue = wrap.FloatField("gsDeselectedCVAlpha")
                    deselectedAlphaValue.setFixedWidth(style.scale(45))
                    deselectedAlphaValue.setValue(1)
                    deselectedAlphaValue.setRange(0, 1)
                    deselectedAlphaValue.setStep(0.01)
                    deselectedAlphaValue.setPrecision(2)
                    deselectedAlphaValue.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    deselectedAlphaValue.setReleaseCommand(noUndo(sliderChangeCommand))

                    row.layout().addWidget(deselectedColorLabel, 0)
                    row.layout().addWidget(deselectedColorPicker, 1)
                    row.layout().addWidget(deselectedAlphaValue, 1)

                column.layout().addWidget(wrap.separator())

                # Curve Visibility
                curveVisibility = wrap.Button(column.layout(), 'curveVisibility')
                curveVisibility.setLabel('Curve Visibility', lineHeight=100)
                curveVisibility.setCheckable(True)
                curveVisibility.setButtonStyle('small')
                curveVisibility.setChecked(True)
                curveVisibility.clicked.connect(noUndo(sliderChangeCommand))

                with wrap.Row(column.layout(), spacing=4) as row:
                    curveWidthLabel = wrap.Label()
                    curveWidthLabel.setLabel("Curve Width:")
                    curveWidthLabel.setFixedWidth(style.scale(100))
                    curveWidthLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    curveWidthSlider = wrap.mayaSlider(
                        mc.floatSliderGrp(
                            'gsCurveWidthSlider',
                            f=1, adj=2, w=1, cw=[1, 45], min=1, max=100, v=4,
                            dc=lambda _: noUndo(core.advancedVisibility.applySettingsToNode)(),
                            cc=noUndo(sliderChangeCommand),
                        ),
                    )
                    WIDGETS['gsCurveWidthSlider'] = curveWidthSlider

                    row.layout().addWidget(curveWidthLabel, 0)
                    row.layout().addWidget(curveWidthSlider, 1)

                with wrap.Row(column.layout(), spacing=style.scale(4)) as row:
                    curveHighlightColorLabel = wrap.Label()
                    curveHighlightColorLabel.setLabel("Curve Color:")
                    curveHighlightColorLabel.setFixedWidth(style.scale(100))
                    curveHighlightColorLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    curveHighlightColor = wrap.ColorPicker("gsCurveHighlightColor")
                    curveHighlightColor.connectDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    curveHighlightColor.connectCommand(noUndo(sliderChangeCommand))

                    curveHighlightAlpha = wrap.FloatField("gsCurveHighlightAlpha")
                    curveHighlightAlpha.setFixedWidth(style.scale(45))
                    curveHighlightAlpha.setValue(1.0)
                    curveHighlightAlpha.setRange(0, 1)
                    curveHighlightAlpha.setStep(0.01)
                    curveHighlightAlpha.setPrecision(2)
                    curveHighlightAlpha.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    curveHighlightAlpha.setReleaseCommand(noUndo(sliderChangeCommand))

                    row.layout().addWidget(curveHighlightColorLabel, 0)
                    row.layout().addWidget(curveHighlightColor, 1)
                    row.layout().addWidget(curveHighlightAlpha, 1)

                column.layout().addWidget(wrap.separator())

                # Hull Visibility
                hullVisibility = wrap.Button(column.layout(), 'hullVisibility')
                hullVisibility.setLabel('Hull Visibility', lineHeight=100)
                hullVisibility.setCheckable(True)
                hullVisibility.setButtonStyle('small')
                hullVisibility.clicked.connect(noUndo(sliderChangeCommand))

                with wrap.Row(column.layout(), spacing=4) as row:
                    hullWidthLabel = wrap.Label()
                    hullWidthLabel.setLabel("Hull Width:")
                    hullWidthLabel.setFixedWidth(style.scale(100))
                    hullWidthLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    hullWidthSlider = wrap.mayaSlider(
                        mc.floatSliderGrp(
                            'gsHullWidthSlider',
                            f=1, adj=2, w=1, cw=[1, 45], min=1, max=100, v=3,
                            dc=lambda _: noUndo(core.advancedVisibility.applySettingsToNode)(),
                            cc=noUndo(sliderChangeCommand),
                        )
                    )
                    WIDGETS['gsHullWidthSlider'] = hullWidthSlider

                    row.layout().addWidget(hullWidthLabel, 0)
                    row.layout().addWidget(hullWidthSlider, 1)

                with wrap.Row(column.layout(), spacing=style.scale(4)) as row:
                    hullColorLabel = wrap.Label()
                    hullColorLabel.setLabel("Hull Color:")
                    hullColorLabel.setFixedWidth(style.scale(100))
                    hullColorLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    hullColor = wrap.ColorPicker("gsHullHighlightColor")
                    hullColor.connectDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    hullColor.connectCommand(noUndo(sliderChangeCommand))

                    hullAlpha = wrap.FloatField("gsHullHighlightAlpha")
                    hullAlpha.setFixedWidth(style.scale(45))
                    hullAlpha.setValue(1.0)
                    hullAlpha.setRange(0, 1)
                    hullAlpha.setStep(0.01)
                    hullAlpha.setPrecision(2)
                    hullAlpha.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                    hullAlpha.setReleaseCommand(noUndo(sliderChangeCommand))

                    row.layout().addWidget(hullColorLabel, 0)
                    row.layout().addWidget(hullColor, 1)
                    row.layout().addWidget(hullAlpha, 1)

                column.layout().addWidget(wrap.separator())

                with wrap.Frame(column.layout(), 'advancedVisibilityFrame', label='Other Options:',
                                margins=style.scale([3, 2, 3, 2]), spacing=style.scale(3)) as optionsFrame:
                    with wrap.Row(optionsFrame.getFrameLayout()) as row:
                        lazyUpdate = wrap.Button(row.layout(), 'lazyUpdate')
                        lazyUpdate.setLabel("Lazy Update", lineHeight=100)
                        lazyUpdate.setCheckable(True)
                        lazyUpdate.setButtonStyle('small')
                        lazyUpdate.clicked.connect(noUndo(sliderChangeCommand))

                        alwaysOnTop = wrap.Button(row.layout(), 'alwaysOnTop')
                        alwaysOnTop.setLabel("Always On Top", lineHeight=100)
                        alwaysOnTop.setCheckable(True)
                        alwaysOnTop.setButtonStyle('small')
                        alwaysOnTop.setChecked(True)
                        alwaysOnTop.clicked.connect(noUndo(sliderChangeCommand))

                    optionsFrame.getFrameLayout().addWidget(wrap.separator())

                    experimentalLabel = wrap.Label(optionsFrame.getFrameLayout())
                    experimentalLabel.setLabel("Distance Colors:")

                    with wrap.Row(optionsFrame.getFrameLayout()) as row:
                        curveDistanceColor = wrap.Button(row.layout(), 'curveDistanceColor')
                        curveDistanceColor.setLabel("Curve", lineHeight=100)
                        curveDistanceColor.setCheckable(True)
                        curveDistanceColor.setButtonStyle('small')
                        curveDistanceColor.setChecked(True)
                        curveDistanceColor.clicked.connect(noUndo(sliderChangeCommand))

                        cvDistanceColor = wrap.Button(row.layout(), 'cvDistanceColor')
                        cvDistanceColor.setLabel("CV", lineHeight=100)
                        cvDistanceColor.setCheckable(True)
                        cvDistanceColor.setButtonStyle('small')
                        cvDistanceColor.setChecked(True)
                        cvDistanceColor.clicked.connect(noUndo(sliderChangeCommand))

                        hullDistanceColor = wrap.Button(row.layout(), 'hullDistanceColor')
                        hullDistanceColor.setLabel("Hull", lineHeight=100)
                        hullDistanceColor.setCheckable(True)
                        hullDistanceColor.setButtonStyle('small')
                        hullDistanceColor.setChecked(True)
                        hullDistanceColor.clicked.connect(noUndo(sliderChangeCommand))

                    with wrap.Row(optionsFrame.getFrameLayout()) as row:
                        distanceColorMinLabel = wrap.Label()
                        distanceColorMinLabel.setLabel("Color Min:")
                        distanceColorMinLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                        distanceColorMinInput = wrap.FloatField("gsDistanceColorMinValue")
                        distanceColorMinInput.setValue(0.25)
                        distanceColorMinInput.setRange(0.01, 1)
                        distanceColorMinInput.setStep(0.01)
                        distanceColorMinInput.setPrecision(2)
                        distanceColorMinInput.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                        distanceColorMinInput.setReleaseCommand(noUndo(sliderChangeCommand))

                        distanceColorMaxLabel = wrap.Label()
                        distanceColorMaxLabel.setLabel("Color Max:")
                        distanceColorMaxLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                        distanceColorMaxInput = wrap.FloatField("gsDistanceColorMaxValue")
                        distanceColorMaxInput.setValue(1.0)
                        distanceColorMaxInput.setRange(0.01, 1)
                        distanceColorMaxInput.setStep(0.01)
                        distanceColorMaxInput.setPrecision(2)
                        distanceColorMaxInput.setDragCommand(lambda *_: noUndo(core.advancedVisibility.applySettingsToNode)())
                        distanceColorMaxInput.setReleaseCommand(noUndo(sliderChangeCommand))

                        row.layout().addWidget(distanceColorMinLabel, 1)
                        row.layout().addWidget(distanceColorMinInput, 1)
                        row.layout().addWidget(distanceColorMaxLabel, 1)
                        row.layout().addWidget(distanceColorMaxInput, 1)

                    optionsFrame.getFrameLayout().addWidget(wrap.separator())

                    experimentalLabel = wrap.Label(optionsFrame.getFrameLayout())
                    experimentalLabel.setLabel("Experimental (possibly slow):")

                    CVocclusion = wrap.Button(optionsFrame.getFrameLayout(), 'CVocclusion')
                    CVocclusion.setLabel("Enable CV Occlusion", lineHeight=100)
                    CVocclusion.setCheckable(True)
                    CVocclusion.setButtonStyle('small')
                    CVocclusion.clicked.connect(noUndo(sliderChangeCommand))

                    with wrap.Row(optionsFrame.getFrameLayout(), spacing=style.scale(4)) as row:
                        selectOccluderButton = wrap.Button(row.layout(), "gsSelectOccluderButton")
                        selectOccluderButton.setFixedWidth(style.scale(100))
                        selectOccluderButton.setLabel('Select Occluder')
                        selectOccluderButton.clicked.connect(noUndo(core.advancedVisibility.selectOccluderFromScene))

                        occluderMeshName = wrap.LineEdit('gsOccluderMeshName', row.layout())
                        occluderMeshName.setPlaceholderText('Select or Type Occluder Mesh Name')
                        occluderMeshName.setClearButtonEnabled(True)
                        occluderMeshName.editingFinished.connect(noUndo(sliderChangeCommand))
        core.advancedVisibility.loadSettingsFromOptionVar()
        tooltips.toggleCustomTooltipsCurveControl(core.getOption('enableTooltips'))

        layout.addWidget(wrap.separator())

        resetButton = wrap.Button(layout, 'resetControlSliders')
        resetButton.setLabel('Reset Sliders Range')
        resetButton.clicked.connect(core.resetControlSliders)

    def twistGraphPopOut(self):
        name = "GSCT_TwistGraphPopOut"
        if mc.workspaceControl(name, q=1, ex=1):
            mc.deleteUI(name)
        popOut = CreatePopOut(name, "Twist Graph Large", 512, 400)
        graph = wrap.FallOffCurve(popOut.widgetLayout, 'twistCurve_large')

        def twistGraphCommand(_):
            core.attributes.propagateGraphs(graph)
            core.attributes.storeGraphs(graph)
        graph.changeCommand(twistGraphCommand)
        with wrap.Row(popOut.widgetLayout, margins=style.scale([5, 0, 5, 2])) as row:
            row.setFixedHeight(style.BUTTON_HEIGHT)

            magnitude = wrap.FloatField('Magnitude_large', row.layout(), attrName='Magnitude')
            magnitude.setFixedWidth(style.scale(45))
            magnitude.setRange(-99, 99)
            magnitude.setStep(0.01)
            magnitude.setPrecision(2)
            magnitude.setDragCommand(pa(core.sliders.curveControlSliderDrag, magnitude))
            magnitude.setReleaseCommand(core.sliders.release)

            resetButton = wrap.Button(row.layout())
            resetButton.setLabel('Reset Curve')

            def resetTwist():
                utils.resetSingleGraph('twist')
                core.attributes.storeGraphs(graph)
            resetButton.clicked.connect(undo(resetTwist))

        core.curveControlUI.updateUI()

    def widthGraphPopOut(self):
        name = "GSCT_WidthGraphPopOut"
        if mc.workspaceControl(name, q=1, ex=1):
            mc.deleteUI(name)
        popOut = CreatePopOut(name, "Width Graph Large", 512, 400)
        graph = wrap.FallOffCurve(popOut.widgetLayout, 'scaleCurve_large')

        def widthGraphCommand(_):
            core.attributes.propagateGraphs(graph)
            core.attributes.storeGraphs(graph)
        graph.changeCommand(widthGraphCommand)
        with wrap.Row(popOut.widgetLayout, margins=style.scale([5, 0, 5, 2])) as row:
            row.setFixedHeight(style.BUTTON_HEIGHT)
            resetButton = wrap.Button(row.layout())
            resetButton.setLabel('Reset Curve')

            def resetWidthCmd():
                utils.resetSingleGraph('width')
                core.attributes.storeGraphs(graph)
            resetButton.clicked.connect(undo(resetWidthCmd))
        core.curveControlUI.updateUI()

    def profileGraphPopOut(self):
        name = "GSCT_ProfileGraphPopOut"
        if mc.workspaceControl(name, q=1, ex=1):
            mc.deleteUI(name)
        popOut = CreatePopOut(name, "Profile Graph Large", 512, 400)
        graph = wrap.FallOffCurve(popOut.widgetLayout, 'profileCurve_large', attr=False)

        def changeCommand(value):
            core.updateLattice(value)
            core.equalizeProfileCurve()
        graph.changeCommand(changeCommand)
        with wrap.Row(popOut.widgetLayout, margins=style.scale([5, 0, 5, 2])) as row:
            row.setFixedHeight(style.BUTTON_HEIGHT)
            resetButton = wrap.Button(row.layout())
            resetButton.setLabel('Reset Curve')
            resetButton.clicked.connect(undo(core.resetProfileCurve))
        core.curveControlUI.updateUI()


# UV Editor Window
def uvEditorWorkspace():
    global uveditor
    if mc.workspaceControl(UV_EDITOR_NAME, q=1, ex=1):
        if MAYA_VER >= 2018:
            if not mc.workspaceControl(UV_EDITOR_NAME, q=1, vis=1):
                mc.workspaceControl(UV_EDITOR_NAME, e=1, rs=1)
            else:
                mc.workspaceControl(UV_EDITOR_NAME, e=1, vis=0)
            try:
                uveditor.updateEditor()  # pylint: disable=used-before-assignment
            except Exception as e:
                LOGGER.exception(e)
        else:
            mc.workspaceControl(UV_EDITOR_NAME, e=1, fl=1)
            mc.deleteUI(UV_EDITOR_NAME)
    else:
        uveditor = UVEditor('uveditor')
        uveditor.init()
        uveditor.updateEditor()
        from . import main
        main.checkScriptJobs(UV_EDITOR_NAME)


class UVEditor(QtWidgets.QWidget):

    def __init__(self, name):
        super(UVEditor, self).__init__()
        self.name = name
        self.timer = utils.Timer()
        self.mouseToggle = False
        self.previousSelection = []
        self.uvUpdateCheck = 0
        self.isolateMode = False
        self.currentSelection = []

    def init(self):
        if mc.workspaceControl(UV_EDITOR_NAME, q=1, ex=1):
            mc.deleteUI(UV_EDITOR_NAME)
        parent = mayaWorkspaceControl(name=UV_EDITOR_NAME,
                                      label=UV_EDITOR_LABEL,
                                      retain=False, iw=705, ih=575,
                                      widthProperty="free")
        self.setParent(parent)

        parent.layout().addWidget(self)
        self.window()

        self.editor.signal_keyPress.connect(self.updateButtons)
        self.editor.signal_mouseMove.connect(self._updateCurves)
        self.editor.signal_mouseRelease.connect(self._stopCurvesUpdate)
        self.editor.signal_uvDrawEnd.connect(self.manualCurveUpdate)
        self.editor.signal_functionKeyPress.connect(undo(self.functionSwitch))
        self.uvList.signal_keyPressed.connect(self.updateVisibility)

    def window(self):
        # Layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setContentsMargins(*style.scale([2, 2, 2, 2]))

        self.scrollWidget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(self.scrollWidget)
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidget(self.scrollWidget)
        mainLayout.addWidget(scrollArea)

        # Layout Settings
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(style.scale(2))
        layout.setMargin(0)
        layout.setAlignment(QtCore.Qt.AlignTop)

        scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        scrollArea.setWidgetResizable(True)

        # Editor Init
        self.editor = uv_editor.Editor()
        self.editor.init()
        self.updateColors()

        # Main Widgets
        with wrap.Row(layout) as mainRow:
            with wrap.Column(mainRow.layout()) as mainColumn:
                mainColumn.layout().setAlignment(QtCore.Qt.AlignTop)
                mainColumn.setFixedWidth(style.scale(130))

                # Controller switches
                mainColumn.layout().addWidget(wrap.separator())
                controllerLabel = wrap.Label(mainColumn.layout())
                controllerLabel.setLabel('Controller Mode')

                self.controllerGroup = QtWidgets.QButtonGroup(mainColumn.layout())
                self.controllerGroup.buttonReleased.connect(self.updateControllerMode)

                with wrap.Row(mainColumn.layout()) as selectMove:
                    select = wrap.Button(selectMove.layout(), 'gsUVSelect')
                    select.setCheckable(True)
                    select.setChecked(True)
                    select.setLabel("Select (Q)")
                    move = wrap.Button(selectMove.layout(), 'gsUVMove')
                    move.setCheckable(True)
                    move.setLabel("Move (W)")
                with wrap.Row(mainColumn.layout()) as rotateScale:
                    rotate = wrap.Button(rotateScale.layout(), 'gsUVRotate')
                    rotate.setCheckable(True)
                    rotate.setLabel("Rotate (E)")
                    scale = wrap.Button(rotateScale.layout(), 'gsUVScale')
                    scale.setCheckable(True)
                    scale.setLabel("Scale (R)")

                with wrap.Row(mainColumn.layout()) as scaleRow:
                    self.directionSwitch = QtWidgets.QButtonGroup(scaleRow.layout())
                    self.directionSwitch.buttonReleased.connect(self.updateControllerMode)

                    horizontal = wrap.Button(scaleRow.layout(), 'gsUVHorizontalScale')
                    horizontal.setLabel('H')
                    horizontal.setButtonStyle('small')
                    horizontal.setCheckable(True)
                    horizontal.setChecked(True)
                    vertical = wrap.Button(scaleRow.layout(), 'gsUVVerticalScale')
                    vertical.setButtonStyle('small')
                    vertical.setCheckable(True)
                    vertical.setLabel('V')

                    self.directionSwitch.addButton(horizontal, 0)
                    self.directionSwitch.addButton(vertical, 1)

                drawUV = wrap.Button(mainColumn.layout(), 'gsDrawUVs')
                drawUV.setCheckable(True)
                drawUV.setLabel('Draw (D)')

                self.controllerGroup.addButton(select, 0)
                self.controllerGroup.addButton(move, 1)
                self.controllerGroup.addButton(rotate, 2)
                self.controllerGroup.addButton(scale, 3)
                self.controllerGroup.addButton(drawUV, 4)

                mainColumn.layout().addWidget(wrap.separator())

                # Utility Functions
                utilityLabel = wrap.Label(mainColumn.layout())
                utilityLabel.setLabel('Utility Functions')

                with wrap.Row(mainColumn.layout()) as HVFlip:
                    hFlipUV = wrap.Button(HVFlip.layout(), 'gsHorizontalFlipUV')
                    hFlipUV.setLabel('H-Flip (H)')
                    hFlipUV.clicked.connect(undo(self.horizontalFlipUV))

                    vFlipUV = wrap.Button(HVFlip.layout(), 'gsVerticalFlipUV')
                    vFlipUV.setLabel('V-Flip (V)')
                    vFlipUV.clicked.connect(undo(self.verticalFlipUV))

                resetUV = wrap.Button(mainColumn.layout(), 'gsResetUVs')
                resetUV.setLabel('Reset UV (X)')
                resetUV.clicked.connect(undo(self.resetUVs))

                syncSelection = wrap.Button(mainColumn.layout(), 'gsSyncSelectionUVs')
                syncSelection.setLabel('Sync Selection (S)')
                syncSelection.clicked.connect(undo(self.syncSelection))

                randomizeUVs = wrap.Button(mainColumn.layout(), 'gsRandomizeUVs')
                randomizeUVs.setLabel('Randomize')
                randomizeUVs.setIcon('mod-bottom')
                randomizeUVs.clicked.connect(undo(self.randomizeUVs))

                mainColumn.layout().addWidget(wrap.separator())

                # UV List
                uvListLabel = wrap.Label(mainColumn.layout())
                uvListLabel.setLabel('UV List')

                self.uvList = wrap.UVItemList(mainColumn.layout())
                self.uvList.setLayout(mainColumn.layout())
                self.uvList.signal_mouseReleased.connect(self.updateVisibility)

                focusView = wrap.Button(mainColumn.layout(), 'gsFocusUVs')
                focusView.setLabel('Focus View (F)')
                focusView.clicked.connect(self.editor.focusView)

                with wrap.Row(mainColumn.layout()) as hideIsolate:
                    isolateSelect = wrap.Button(hideIsolate.layout(), 'gsUVIsolateSelect')
                    isolateSelect.setLabel('Isolate (I)')
                    isolateSelect.clicked.connect(self.isolateSelect)

                    hide = wrap.Button(hideIsolate.layout(), 'gsUVHide')
                    hide.setLabel('Hide (O)')
                    hide.clicked.connect(self.hide)

                showAllButton = wrap.Button(mainColumn.layout(), 'gsUVShowAll')
                showAllButton.setLabel('Show All (A)')
                showAllButton.clicked.connect(self.showAll)

                mainColumn.layout().addWidget(wrap.separator())

                with wrap.Frame(mainColumn.layout(), label="Options") as optionsFrame:
                    # Texture Controls
                    textureFunctionsLabel = wrap.Label(optionsFrame.getFrameLayout())
                    textureFunctionsLabel.setLabel('Texture Controls:')

                    transparency = wrap.Button(optionsFrame.getFrameLayout(), 'UVEditorTransparencyToggle')
                    transparency.setButtonStyle('small')
                    transparency.setCheckable(True)
                    transparency.setChecked(mc.optionVar(q='GSCT_UVEditorTransparencyToggle'))
                    transparency.setLabel("Transparency")

                    alphaOnly = wrap.Button(optionsFrame.getFrameLayout(), 'UVEditorAlphaOnlyToggle')
                    alphaOnly.setButtonStyle('small')
                    alphaOnly.setCheckable(True)
                    alphaOnly.setChecked(mc.optionVar(q='GSCT_UVEditorAlphaOnly'))
                    alphaOnly.setLabel("Alpha Only")

                    useTransforms = wrap.Button(optionsFrame.getFrameLayout(), 'UVEditorUseTransforms')
                    useTransforms.setButtonStyle('small')
                    useTransforms.setCheckable(True)
                    useTransforms.setChecked(True)
                    useTransforms.setLabel("Use Transforms")
                    useTransforms.clicked.connect(self.updateTexture)

                    def toggleAlphaCommand():
                        if transparency.isChecked():
                            self.editor.toggleAlpha(True)
                        else:
                            self.editor.toggleAlpha(False)
                            alphaOnly.setChecked(False)
                        self.updateTexture()
                        mc.optionVar(iv=['GSCT_UVEditorTransparencyToggle', transparency.isChecked()])
                    transparency.clicked.connect(toggleAlphaCommand)

                    def toggleAlphaOnlyCommand():  # BUG: Find out why switching textures does not update alpha
                        if alphaOnly.isChecked():
                            transparency.setChecked(True)
                        else:
                            transparency.setChecked(False)
                        toggleAlphaCommand()
                        mc.optionVar(iv=['GSCT_UVEditorAlphaOnly', alphaOnly.isChecked()])
                    alphaOnly.clicked.connect(toggleAlphaOnlyCommand)

                    optionsFrame.getFrameLayout().addWidget(wrap.separator())

                    # Editor Colors
                    textureFunctionsLabel = wrap.Label(optionsFrame.getFrameLayout())
                    textureFunctionsLabel.setLabel('Editor Colors:')

                    with wrap.Row(optionsFrame.getFrameLayout(), margins=style.scale([5, 0, 5, 5])) as colorRow:
                        backgroundColorPicker = wrap.ColorPicker('UVEditorBGColorPicker', colorRow.layout())
                        backgroundColorPicker.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorBGColor")))
                        )
                        backgroundColorPicker.connectCommand(self.updateColors)

                        gridColorPicker = wrap.ColorPicker('UVEditorGridColorPicker', colorRow.layout())
                        gridColorPicker.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorGridColor")))
                        )
                        gridColorPicker.connectCommand(self.updateColors)

                        frameColorPicker = wrap.ColorPicker('UVEditorFrameColorPicker', colorRow.layout())
                        frameColorPicker.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorFrameColor")))
                        )
                        frameColorPicker.connectCommand(self.updateColors)

                    # UV Card Colors
                    cardColors = wrap.Label(optionsFrame.getFrameLayout())
                    cardColors.setLabel('UV Colors:')

                    with wrap.Row(optionsFrame.getFrameLayout(), margins=style.scale([5, 0, 5, 5])) as colorRow2:
                        selectedCardFrameColor = wrap.ColorPicker('UVEditorUVFrameSelectedColorPicker', colorRow2.layout())
                        selectedCardFrameColor.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorUVFrameSelectedColor")))
                        )
                        selectedCardFrameColor.connectCommand(self.updateColors)

                        deselectedCardFrameColor = wrap.ColorPicker('UVEditorUVFrameDeselectedColorPicker', colorRow2.layout())
                        deselectedCardFrameColor.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorUVFrameDeselectedColor")))
                        )
                        deselectedCardFrameColor.connectCommand(self.updateColors)

                        cardFillColor = wrap.ColorPicker('UVEditorUVCardFillColorPicker', colorRow2.layout())
                        cardFillColor.setRGBColors(
                            utils.colorFrom255to1(eval(mc.optionVar(q="GSCT_UVEditorUVCardFillColor")))
                        )
                        cardFillColor.connectCommand(self.updateColors)

                mainColumn.layout().addWidget(wrap.separator())

            mainRow.layout().addWidget(self.editor)

            if MAYA_VER in [2020, 2022] and not mc.optionVar(q='GSCT_UVBugMessageDismissed'):
                with wrap.Row(mainLayout) as row:
                    label = wrap.Label(row.layout())
                    label.setLabel('<p style="color:#FF542F">How To Fix Maya 2020-2022 UV Bug:</p>')

                    linkButton = wrap.Button(row.layout())
                    linkButton.setLabel('Open Fix')
                    linkButton.setButtonStyle('small-filled')
                    linkButton.clicked.connect(lambda: utils.openLink(
                        'https://gs-curvetools.readthedocs.io/en/latest/faq.html#maya-2020-2022-and-broken-uvs')
                    )

                    dismissMessage = wrap.Button(row.layout())
                    dismissMessage.setLabel('Dismiss Message')
                    dismissMessage.setButtonStyle('small-filled')
                    dismissMessage.clicked.connect(lambda: row.setHidden(True))
                    dismissMessage.clicked.connect(lambda: mc.optionVar(iv=['GSCT_UVBugMessageDismissed', 1]))

    def updateColors(self, *_):
        if self.editor:
            core.saveOptions()
            try:
                self.editor.changeColor(
                    eval(mc.optionVar(q="GSCT_UVEditorBGColor")),
                    eval(mc.optionVar(q="GSCT_UVEditorGridColor")),
                    eval(mc.optionVar(q="GSCT_UVEditorFrameColor")),
                    eval(mc.optionVar(q="GSCT_UVEditorUVCardFillColor")),
                    eval(mc.optionVar(q="GSCT_UVEditorUVFrameSelectedColor")),
                    eval(mc.optionVar(q="GSCT_UVEditorUVFrameDeselectedColor"))
                )
            except Exception as e:
                self.editor.changeColor()
                LOGGER.exception(e)
            self.editor.update()

    @noUndo
    def updateEditor(self):
        uveditor.updateItemList()
        uveditor.updateUVs()
        uveditor.updateTexture()

    def showAll(self):
        self.uvList.expandAll()
        self.uvList.selectAll()
        self.updateVisibility()
        self.isolateMode = False

    @noUndo
    def updateUVs(self, keepSelection=False):
        sel = mc.filterExpand(mc.ls(sl=1, fl=1, l=1), sm=9)
        oldUVs = self.editor.UVDict
        self.editor.purgeUVs()
        if not sel:
            return
        sel = self.checkForLegacyUVs(sel)
        for item in sel:
            if (mc.attributeQuery('Orientation', n=item, ex=1) and
                    mc.connectionInfo(item + '.Orientation', isSource=1)):
                if (mc.attributeQuery('gsmessage', n=item, ex=1) and
                        mc.listConnections(item + '.gsmessage')):
                    curves = core.getAllConnectedCurves(item)
                else:
                    curves = [item]
                for curve in curves:
                    attrs = core.attributes.getUVs(curve)
                    cb = core.attributes.getCheckboxes(curve)
                    if attrs:
                        uv = self.editor.createUV(curve)
                        if 'flipUV' in cb:
                            uv.flip = not cb['flipUV']
                        uv.moveUV(
                            x=attrs['moveU'],
                            y=attrs['moveV'],
                            rot=attrs['rotateUV'] * -1,
                            sx=attrs['scaleU'],
                            sy=attrs['scaleV'],
                        )
        if keepSelection:
            newUVs = self.editor.UVDict
            for uv in newUVs:
                if uv in oldUVs:
                    newUVs[uv].setSelected(True)

    def checkForLegacyUVs(self, curves):
        legacyCurves = []
        for curve in curves:
            root = mc.attributeQuery('rotateRootUV', n=curve, ex=1)
            tip = mc.attributeQuery('rotateTipUV', n=curve, ex=1)
            if root or tip:
                rootValue = mc.getAttr(curve + '.rotateRootUV')
                tipValue = mc.getAttr(curve + '.rotateTipUV')
                if rootValue or tipValue:
                    legacyCurves.append(curve)
        if not legacyCurves:
            return curves
        else:
            MESSAGE.warningInView('Non Zero Legacy UV Attributes Detected')
            dialog = mc.confirmDialog(
                title='Legacy UVs',
                message='Non Zero Legacy UVs Detected.\nUV Editor is not compatible with them.\nZero them out to proceed?',
                icon='warning',
                button=['Yes', 'Cancel'],
                cancelButton='Cancel',
                dismissString='Cancel'
            )
            if dialog == 'Yes':
                for curve in legacyCurves:
                    mc.setAttr(curve + '.rotateRootUV', 0)
                    mc.setAttr(curve + '.rotateTipUV', 0)
                return curves
            elif dialog == 'Cancel':
                dialog = mc.confirmDialog(
                    title='Legacy UVs',
                    message='UV Editor is not compatible with the old UVs.\nSome of the cards are ignored.',
                    icon='information',
                    button='OK',
                    cancelButton='OK',
                    dismissString='OK'
                )
                return list(set(curves) - set(legacyCurves))

    @noUndo
    def updateTexture(self):
        sel = core.selectPart(2, justReturn=True)
        if not sel:
            self.editor.removeTexture()
            self.editor.diffusePath = ''
            return
        geo = mc.filterExpand(sel, sm=12)
        if not geo:
            return
        dag = mc.ls(geo[-1], dag=1, s=1)
        shader = mc.listConnections(dag, d=1, s=1, t='shadingEngine')
        if not shader:
            return
        network = mc.hyperShade(lun=shader[0])
        fileNode = None
        alphaNode = None
        if network:
            for node in network:
                if mc.nodeType(node) == 'file' and mc.connectionInfo(node + '.outColor', isSource=1):
                    fileNode = node
                    break
            for node in network:
                if mc.nodeType(node) == 'file' and mc.connectionInfo(node + '.outTransparency', isSource=1):
                    alphaNode = node
                    break
        if not fileNode:
            return
        texturePath = mc.getAttr(fileNode + '.fileTextureName')
        alphaPath = mc.getAttr(alphaNode + '.fileTextureName') if alphaNode else None

        # Find place2dTexture node
        place2dTexture = None
        if mc.attributeQuery('coverage', n=fileNode, ex=1):
            info = mc.connectionInfo(fileNode + '.coverage', sfd=1)
            if info:
                place2dTexture = info.split('.')
                if place2dTexture:
                    place2dTexture = place2dTexture[0]

        # Get coverage and transformFrame from place2dTexture
        cov, trans = None, None
        if place2dTexture and mc.objExists(place2dTexture) and WIDGETS['UVEditorUseTransforms'].isChecked():
            if (mc.attributeQuery('coverage', ex=1, n=place2dTexture) and
                    mc.attributeQuery('translateFrame', ex=1, n=place2dTexture)):
                try:
                    cov = mc.getAttr(place2dTexture + '.coverage')[0]
                    trans = mc.getAttr(place2dTexture + '.translateFrame')[0]
                except Exception as e:
                    LOGGER.exception(e)
        coverage = cov if cov else (1.0, 1.0)
        translation = (trans[0], trans[1]) if trans and trans else (0, 0)

        if not WIDGETS['UVEditorTransparencyToggle'].isChecked() and not WIDGETS['UVEditorAlphaOnlyToggle'].isChecked():
            alphaPath = None
        if texturePath:
            _, ext = os.path.splitext(texturePath)
            try:  # Python 3
                supportedFormats = list([str(x, encoding='ASCII').lower() for x in QtGui.QImageReader.supportedImageFormats()])
            except BaseException:  # Python 2 fallback
                supportedFormats = list([str(x).decode('ASCII').lower() for x in QtGui.QImageReader.supportedImageFormats()])
            if ext and (ext[1:].lower() not in supportedFormats):
                MESSAGE.warning(
                    "{} format is not supported. Use JPG/JPEG, PNG, TIF/TIFF (LZW or No Compression), TGA (24bit, no RLE)".format(ext[1:].upper()))
                return
            err = self.editor.setTexture('%s' % texturePath, alphaPath, coverage, translation)
            if err == 'SamePath':
                return
            elif err == 'NoTexture':
                MESSAGE.warning("Texture file could not be loaded.")
                return
            elif err == 'ZeroTexture':
                MESSAGE.warning("Invalid Path or Zero Texture")
                return

    def manualCurveUpdate(self):
        try:
            self._updateCurves()
        except Exception as e:
            LOGGER.exception(e)
        finally:
            self._stopCurvesUpdate()

    def _updateCurves(self):
        if self.uvUpdateCheck == 0:
            mc.undoInfo(ock=1, cn='gsUVUpdate')
            self.uvUpdateCheck = 1

            sel = mc.filterExpand(mc.ls(sl=1), sm=9)
            uvs = self.editor.getUVs()
            self.currentSelection *= 0

            if not sel:
                return

            for curve in sel:
                if curve in uvs:
                    self.currentSelection.append(curve)
                else:
                    if (mc.attributeQuery('gsmessage', n=curve, ex=1) and
                            mc.listConnections(curve + '.gsmessage')):
                        boundCurves = core.getAllConnectedCurves(curve)
                        if boundCurves:
                            self.currentSelection += boundCurves

        if not self.timer.increment(1.0 / 60.0):
            return
        if not self.currentSelection:
            return

        uvs = self.editor.getUVs()
        for curve in self.currentSelection:
            if curve in uvs:
                core.attributes.setAttr(curve, uvs[curve])

    def _stopCurvesUpdate(self):
        if self.uvUpdateCheck == 1:
            mc.undoInfo(cck=1)
            self.uvUpdateCheck = 0
            self.currentSelection *= 0
            core.curveControlUI.updateUI()

    def updateButtons(self, controllerMode, scaleMode):
        buttons = self.controllerGroup.buttons()
        direction = self.directionSwitch.buttons()
        if controllerMode == 'SELECT':
            buttons[0].setChecked(True)
        elif controllerMode == 'MOVE':
            buttons[1].setChecked(True)
        elif controllerMode == 'ROTATE':
            buttons[2].setChecked(True)
        elif controllerMode == 'SCALE':
            buttons[3].setChecked(True)
            if scaleMode == 'H':
                direction[0].setChecked(True)
            else:
                direction[1].setChecked(True)
        elif controllerMode == 'DRAW':
            buttons[4].setChecked(True)

    def updateControllerMode(self):
        buttonID = self.controllerGroup.checkedId()
        scaleID = self.directionSwitch.checkedId()
        scale = 'H'
        if buttonID == 0:
            mode = 'SELECT'
        elif buttonID == 1:
            mode = 'MOVE'
        elif buttonID == 2:
            mode = 'ROTATE'
        elif buttonID == 3:
            mode = 'SCALE'
            if scaleID == 0:
                scale = 'H'
            else:
                scale = 'V'
        else:
            mode = 'DRAW'
        self.editor.controllerModeChange(mode, scale)

    def updateItemList(self):
        sel = mc.filterExpand(mc.ls(sl=1), sm=9)
        if not sel:
            self.uvList.clearItemList()
            return

        finalDict = {}
        for curve in sel:
            if (mc.attributeQuery('Orientation', n=curve, ex=1) and
                    mc.connectionInfo(curve + '.Orientation', isSource=1)):
                if (mc.attributeQuery('gsmessage', n=curve, ex=1) and
                        mc.listConnections(curve + '.gsmessage')):
                    boundCurves = core.getAllConnectedCurves(curve)
                    finalDict[curve] = boundCurves
                else:
                    finalDict[curve] = []
        self.uvList.updateItemList(finalDict)

    def updateVisibility(self):
        itemList = self.uvList.getSelection()
        items = self.editor.getAllUVs()
        for item in items:
            if item.name in itemList:
                item.setVisible(True)
            else:
                item.setVisible(False)
        self.editor.update()

    def hide(self):
        """Hides selected UV items"""
        selUVs = self.editor.getAllUVs(selected=True)
        selUVsList = [i.name for i in selUVs]
        for uv in selUVs:
            uv.setVisible(False)
        itemList = self.uvList.getItemList()
        selectList = []
        for item in itemList:
            if item.curveName in selUVsList:
                selectList.append(item)
        self.uvList.selectItems(selectList)

    def isolateSelect(self):
        allUVs = self.editor.getAllUVs()
        selUVs = self.editor.getAllUVs(selected=True)
        if not selUVs:
            return
        if self.isolateMode:
            self.showAll()
            self.isolateMode = False
            return
        self.isolateMode = True
        selUVsList = [i.name for i in selUVs]
        for uv in allUVs:
            if uv.name not in selUVsList:
                uv.setVisible(False)
        itemList = self.uvList.getItemList()
        deselectList = []
        for item in itemList:
            if item.curveName not in selUVsList:
                deselectList.append(item)
        self.uvList.selectItems(deselectList)

    def horizontalFlipUV(self):
        items = self.editor.getAllUVs(selected=True)
        for item in items:
            if item.name and mc.attributeQuery('flipUV', n=item.name, ex=1):
                flip = mc.getAttr(item.name + '.flipUV')
                mc.setAttr(item.name + '.flipUV', not flip)
                item.flip = flip
                item.update()
        if items:
            self.editor.update()

    def verticalFlipUV(self):
        self.editor.verticalFlipUV()
        self.manualCurveUpdate()

    def functionSwitch(self, key):
        if key == 'H':
            self.horizontalFlipUV()
        elif key == 'V':
            self.verticalFlipUV()
        elif key == 'X':
            self.resetUVs()
        elif key == 'I':
            self.isolateSelect()
        elif key == 'O':
            self.hide()
        elif key == 'A':
            self.showAll()
        elif key == 'S':
            self.syncSelection()

    def resetUVs(self):
        self.editor.resetUV()
        self.manualCurveUpdate()

    def randomizeUVs(self):
        if utils.getMod() == 'Shift':
            self.editor.randomizeUVs(True)
        else:
            self.editor.randomizeUVs(False)
        self.manualCurveUpdate()

    def syncSelection(self):
        """Selects curves in Maya Viewport based on UV Editor selection"""
        sel = mc.filterExpand(mc.ls(sl=1), sm=9)
        if not sel:
            return
        selUVs = [x.name for x in self.editor.getAllUVs(selected=True)]
        newSel = [x for x in sel if x in selUVs]
        if newSel:
            mc.select(newSel, r=1)

            @utils.deferredLp
            def x():
                uvs = self.editor.getAllUVs()
                for uv in uvs:
                    uv.setSelected(True)
                self.editor.scene().update()
            x()


uveditor = UVEditor('uveditor')


# Colors Window

class CustomLayerColors:

    def window(self, *_):
        self.windowName = 'GSCT_CustomLayerColorsWindow'
        if mc.workspaceControl(self.windowName, q=1, ex=1):
            mc.deleteUI(self.windowName)
        popOut = CreatePopOut(self.windowName, "Layers Customization", 280, 586)

        layout = popOut.widgetLayout
        layout.setAlignment(QtCore.Qt.AlignTop)

        letters = [chr(l) for l in range(ord('A'), ord('A') + 10)]

        wrap.Label(layout).setLabel("Color Controls:")

        with wrap.Frame(layout, label='Gradient', margins=[2, 2, 2, 2]) as generateFrame:

            self.gradientRowsNumber = wrap.ControlSlider(generateFrame.getFrameLayout())
            self.gradientRowsNumber.setLabel('Rows')
            self.gradientRowsNumber.setMinMax(1, 80)
            self.gradientRowsNumber.setValue(20)

            with wrap.Row(generateFrame.getFrameLayout()) as gradientColorsLayout:
                self.minGradientSwatch = wrap.ColorPicker('gradientSwatchMin', gradientColorsLayout.layout())
                self.minGradientSwatch.setHSVColors([0.1, 1, 1])
                self.maxGradientSwatch = wrap.ColorPicker('gradientSwatchMax', gradientColorsLayout.layout())
                self.maxGradientSwatch.setHSVColors([300, 1, 1])

            generateGradient = wrap.Button(generateFrame.getFrameLayout(), 'gsGenerateLayerColorGradient')
            generateGradient.setLabel('Generate Gradient')
            generateGradient.clicked.connect(self.generateColorGradient)

        with wrap.Frame(layout, label='Randomize', margins=[2, 2, 2, 2]) as randomizeFrame:

            self.saturationMin = wrap.ControlSlider(randomizeFrame.getFrameLayout(), typ='float')
            self.saturationMin.setMinMax(0, 1)
            self.saturationMin.setValue(0.8)
            self.saturationMin.setStep(0.01)
            self.saturationMin.setLabel('SatMin')

            self.saturationMax = wrap.ControlSlider(randomizeFrame.getFrameLayout(), typ='float')
            self.saturationMax.setMinMax(0, 1)
            self.saturationMax.setValue(1.0)
            self.saturationMax.setStep(0.01)
            self.saturationMax.setLabel('SatMax')

            randomizeButton = wrap.Button(randomizeFrame.getFrameLayout(), 'gsRandomizeLayerColors')
            randomizeButton.setLabel('Randomize All')
            randomizeButton.clicked.connect(self.randomizeAllColors)

        layout.addWidget(wrap.separator())

        wrap.Label(layout).setLabel("Layers:")

        def colorRow(parent, i):
            with wrap.Row(parent) as singleColor:
                singleColor.setFixedHeight(style.scale(16))

                label = wrap.Label()
                if 10 <= i < 20:
                    label.setLabel('%s (%s)' % (i, letters[i - 10]))
                else:
                    label.setLabel(str(i))
                label.setFixedWidth(style.scale(int(35)))

                layerName = wrap.LineEdit('layerCustomName_%s' % i)
                newFont = QtGui.QFont('Roboto')
                newFont.setPointSizeF(style.scale(5))
                layerName.setFixedHeight(style.scale(18))
                layerName.setFrame(False)
                layerName.setFont(newFont)
                layerName.setAutoFormat(True)
                layerName.setClearButtonEnabled(True)

                swatch = wrap.ColorPicker('layerColorPicker_%s' % i)

                randButton = wrap.Button()
                randButton.setButtonStyle('small-filled')
                randButton.setLabel('Rand', lineHeight=100)
                randButton.setLabelStyle('small')
                randButton.setWidthHeight(h=style.scale(10))
                randButton.clicked.connect(pa(self.randomizeColor, swatch))

                resetButton = wrap.Button()
                resetButton.setButtonStyle('small-filled')
                resetButton.setLabel('Reset', lineHeight=100)
                resetButton.setLabelStyle('small')
                resetButton.setWidthHeight(h=style.scale(10))
                resetButton.clicked.connect(pa(self.resetColor, swatch))
                resetButton.clicked.connect(pa(self.resetName, layerName))

                singleColor.layout().addWidget(label)
                singleColor.layout().addWidget(layerName, 3)
                singleColor.layout().addWidget(swatch, 1)
                singleColor.layout().addWidget(randButton, 1)
                singleColor.layout().addWidget(resetButton, 1)
            return singleColor

        with wrap.Frame(layout, label='0-19') as frame1:
            for i in range(20):
                colorRow(frame1.getFrameLayout(), i)
                frame1.setCollapsed(False)
        with wrap.Frame(layout, label='20-39') as frame2:
            for i in range(20, 40):
                colorRow(frame2.getFrameLayout(), i)
                frame2.setCollapsed(True)
        with wrap.Frame(layout, label='40-79') as frame3:
            for i in range(40, 80):
                colorRow(frame3.getFrameLayout(), i)
                frame3.setCollapsed(True)

        layout.addWidget(wrap.separator())

        wrap.Label(layout).setLabel("Commands:")

        resetButton = wrap.Button(layout, 'gsResetAllLayerColors')
        resetButton.setLabel('Reset All')
        resetButton.clicked.connect(self.resetAll)

        with wrap.Row(layout) as controlButtons:
            getCurrent = wrap.Button(controlButtons.layout(), 'gsGetCurrentSceneLayers')
            getCurrent.setLabel('Get From Scene')
            getCurrent.clicked.connect(self.getFromLayers)

            setAsCurrent = wrap.Button(controlButtons.layout(), 'gsSetAsCurrentSceneLayers')
            setAsCurrent.setLabel('Set To Scene')
            setAsCurrent.clicked.connect(self.setToLayers)

        with wrap.Row(layout) as buttonsFrame:

            loadSaved = wrap.Button(buttonsFrame.layout(), 'gsLoadGlobalLayerPreset')
            loadSaved.setLabel('Load Preset')
            loadSaved.clicked.connect(self.loadPreset)

            saveButton = wrap.Button(buttonsFrame.layout(), 'gsSaveGlobalLayerPreset')
            saveButton.setLabel('Save As Preset')
            saveButton.clicked.connect(self.savePreset)

        self.getFromLayers()

    def randomizeColor(self, swatch):
        satMin = self.saturationMin.getValue()
        satMax = self.saturationMax.getValue()
        swatch.setRGBColors(core.toggleColor.generateBrightColor(satMin, satMax))

    def randomizeAllColors(self):
        for i in range(80):
            self.randomizeColor(WIDGETS['layerColorPicker_%s' % i])

    def resetColor(self, swatch):
        swatch.setRGBColors([0, 0, 0])

    def resetName(self, field):
        field.clear()

    def resetAll(self):
        for i in range(80):
            WIDGETS['layerColorPicker_%s' % i].setRGBColors([0, 0, 0])
            WIDGETS['layerCustomName_%s' % i].clear()

    def generateColorGradient(self):
        rows = self.gradientRowsNumber.getValue()
        colorMin = self.minGradientSwatch.getHSVColors()
        colorMax = self.maxGradientSwatch.getHSVColors()
        for i in range(rows):
            fraction = i / float(rows)
            h = mt.lerp(fraction, colorMin[0], colorMax[0])
            s = mt.lerp(fraction, colorMin[1], colorMax[1])
            v = mt.lerp(fraction, colorMin[2], colorMax[2])
            WIDGETS['layerColorPicker_%s' % i].setHSVColors([h, s, v])

    def getFromLayers(self):
        # Getting colors
        colorDict = core.toggleColor.readColorDict()
        for key in colorDict:
            WIDGETS['layerColorPicker_%s' % key].setRGBColors(colorDict[key])
        # Getting names
        core.toggleColor.checkColorStorageNode()
        nameDict = eval(mc.getAttr(core.toggleColor.STORAGE_NODE + '.layerName'))
        for key in nameDict:
            if nameDict[key]:
                WIDGETS['layerCustomName_%s' % key].setText(nameDict[key])

    def getCurrentSwatches(self):
        colorDict = {}
        for i in range(80):
            colorDict[i] = WIDGETS['layerColorPicker_%s' % i].getRGBColors()
        return colorDict

    def getCurrentNames(self):
        core.toggleColor.checkColorStorageNode()
        nameDict = {}
        for i in range(80):
            nameDict[i] = WIDGETS['layerCustomName_%s' % i].text()
        return nameDict

    def setToLayers(self):
        colorDict = self.getCurrentSwatches()
        core.toggleColor.writeColorDict(colorDict)
        if WIDGETS['colorMode'].isChecked():
            core.toggleColor.updateColors()
        if WIDGETS['syncCurveColor'].isChecked():
            core.toggleColor.syncCurveColors()
        core.updateMainUI()

        # Setting names
        nameDict = self.getCurrentNames()
        core.toggleColor.checkColorStorageNode()
        mc.setAttr(core.toggleColor.STORAGE_NODE + '.layerName', str(nameDict), typ='string')

    def setCurrentSwathes(self, colorDict):
        for key in colorDict:
            WIDGETS['layerColorPicker_%s' % key].setRGBColors(colorDict[key])

    def setCurrentNames(self, nameDict):
        for key in nameDict:
            WIDGETS['layerCustomName_%s' % key].setText(nameDict[key])

    def savePreset(self):
        mc.optionVar(sv=['gsCurveToolsCustomColors', str(self.getCurrentSwatches())])
        mc.optionVar(sv=['gsCurveToolsCustomLayerNames', str(self.getCurrentNames())])

    def loadPreset(self):
        colorString = mc.optionVar(q='gsCurveToolsCustomColors')
        colorDict = eval(colorString)
        self.setCurrentSwathes(colorDict)
        nameString = mc.optionVar(q='gsCurveToolsCustomLayerNames')
        nameDict = eval(nameString)
        self.setCurrentNames(nameDict)


customLayerColors = CustomLayerColors()


class CreatePopOut(QtWidgets.QWidget):

    def __init__(self, name, label, width, height):
        self.name = name

        parent = mayaWorkspaceControl(name=name,
                                      label=label,
                                      retain=False, iw=width, ih=height, widthProperty="free")

        super(CreatePopOut, self).__init__(parent)

        self.ui()

        parent.layout().addWidget(self)

    def ui(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(*style.scale([5, 5, 5, 5]))

        self.scrollWidget = QtWidgets.QWidget()
        self.widgetLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidget(self.scrollWidget)
        self.mainLayout.addWidget(scrollArea)

        # Layout Settings
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetLayout.setSpacing(style.scale(2))
        self.widgetLayout.setMargin(0)

        scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        scrollArea.setWidgetResizable(True)


class About:  # Creates "About" and "Contacts" windows

    def social(self):
        layout = mc.columnLayout()
        mc.textFieldButtonGrp(
            bl='>',
            bc=pa(
                utils.openLink,
                'https://discord.gg/f4DH6HQ'),
            l='Discord Server',
            tx='https://discord.gg/f4DH6HQ')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'https://sladkovsky3d.artstation.com/store'),
                              l='Online Store', tx='https://sladkovsky3d.artstation.com/store')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'http://gs-curvetools.readthedocs.io/'),
                              l='Online Documentation', tx='http://gs-curvetools.readthedocs.io/')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'https://www.twitch.tv/videonomad'),
                              l='Twitch Channel', tx='https://www.twitch.tv/videonomad')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'https://www.youtube.com/GeorgeSladkovsky'),
                              l='YouTube Channel', tx='https://www.youtube.com/GeorgeSladkovsky')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'https://www.artstation.com/sladkovsky3d'),
                              l='ArtStation Portfolio', tx='https://www.artstation.com/sladkovsky3d')
        mc.textFieldButtonGrp(bl='>', bc=pa(utils.openLink, 'mailto:george.sladkovsky@gmail.com'),
                              l='Contact Email', tx='george.sladkovsky@gmail.com')
        return layout

    def socialWindow(self):
        if (mc.window('gsSocialMedia', ex=1)):
            mc.deleteUI('gsSocialMedia')
        mc.window('gsSocialMedia', t='Useful Links:', tlb=1)
        self.social()
        mc.showWindow()

    def aboutWindow(self):
        if mc.window('gsAboutWindow', ex=1):
            mc.deleteUI('gsAboutWindow')
        mc.window('gsAboutWindow', t='About', tlb=1)
        mc.rowColumnLayout(h=400, co=[1, 'left', 10], cal=([1, 'left'], [2, 'right']), nc=2, cw=[1, 200])
        mc.text(al='left', l='Version: \n%s' % core.VERSION)
        mc.iconTextButton(al='right', w=90, h=80, i=utils.getFolder.icons() + 'gsCurveToolsIcon_logo.png')
        mc.setParent('..')
        mc.columnLayout(w=460, h=400)
        mc.text(w=400, ww=1, al='left',
                l='License:\nThis collection of code named GS CurveTools is a property of George Sladkovsky\
                   (Yehor Sladkovskyi) and can not be copied or distributed without his written permission.\
                   \n\n%s\nGeorge Sladkovsky (Yehor Sladkovskyi)\nAll Rights Reserved\
                   \n\nAutodesk Maya is a property of Autodesk, Inc.\n' % core.VERSION)
        mc.text(l='Social Media and Contact Links:\n')
        self.social()
        mc.showWindow('gsAboutWindow')


about = About()


class AttributesFilter:

    def __init__(self):
        self.uiName = "GSCT_AttributesFilterPopOut"
        self.attrs = [
            ('Length Divisions', 'lengthDivisions'),
            ('Dynamic Divisions', 'dynamicDivisions'),
            ('Width Divisions', 'widthDivisions'),
            ('Orientation', 'Orientation'),
            ('Twist', 'Twist'),
            ('Inverted Twist', 'invTwist'),
            ('Width', 'Width'),
            ('WidthX', 'WidthX'),
            ('WidthZ', 'WidthZ'),
            ('Taper', 'Taper'),
            ('Length Lock', 'LengthLock'),
            ('Length', 'Length'),
            ('Offset', 'Offset'),
            ('Profile', 'Profile'),
            ('Refine', 'curveRefine'),
            ('Auto Refine', 'autoRefine'),
            ('Smooth', 'curveSmooth'),
            ('Normals', 'surfaceNormals'),
            ('Reverse Normals', 'reverseNormals'),
            ('Axis Flip', 'AxisFlip'),
            ('Line Width', 'lineWidth'),
            ('Sampling', 'samplingAccuracy'),
        ]

        self.solidify = [
            ('Solidify', 'solidify'),
            ('Solidify Thickness', 'solidifyThickness'),
            ('Solidify Divisions', 'solidifyDivisions'),
            ('Solidify Scale X', 'solidifyScaleX'),
            ('Solidify Scale Y', 'solidifyScaleY'),
            ('Solidify Offset', 'solidifyOffset'),
            ('Solidify Normals', 'solidifyNormals'),
        ]

        self.uvs = [
            ('Move U', 'moveU'),
            ('Move V', 'moveV'),
            ('Rotate UV', 'rotateUV'),
            ('Scale U', 'scaleU'),
            ('Scale V', 'scaleV'),
            ('Flip UV', 'flipUV'),
            ('Rotate Root UV', 'rotateRootUV'),
            ('Rotate Tip UV', 'rotateTipUV'),
        ]

        self.graphs = [
            ('Twist Graph', 'twistCurve'),
            ('Scale Graph', 'scaleCurve'),
            ('Profile Graph', 'profileCurve'),
            ('Twist Magnitude', 'Magnitude'),
            ('Profile Smoothing', 'profileSmoothing'),
            ('Profile Magnitude', 'profileMagnitude'),
        ]

    def openUI(self):
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            if mc.workspaceControl(self.uiName, q=1, vis=1):
                mc.deleteUI(self.uiName)
                return
            else:
                mc.deleteUI(self.uiName)
        popOut = CreatePopOut(self.uiName, "Attributes Filter", 260, 456.0)

        layout = popOut.widgetLayout
        layout.setAlignment(QtCore.Qt.AlignTop)
        with wrap.Row(layout, margins=style.scale([6, 0, 6, 0]), spacing=style.scale(10)) as mainRow:
            mainRow.layout().setAlignment(QtCore.Qt.AlignTop)
            with wrap.Column(mainRow.layout()) as leftColumn:
                with wrap.Frame(leftColumn.layout(), label='Attributes', margins=[2, 0, 2, 0]) as leftFrame:
                    leftFrame.setCollapsible(False)
                    leftFrame.getFrameLayout().setAlignment(QtCore.Qt.AlignTop)
                    for i in range(len(self.attrs)):
                        btn = wrap.Button(leftFrame.getFrameLayout(), 'gsFilter_%s' % self.attrs[i][1])
                        btn.setLabel(self.attrs[i][0])
                        btn.setButtonStyle('small')
                        btn.setCheckable(True)
                        btn.setChecked(False if self.attrs[i][0] == 'Orientation' else True)
            with wrap.Column(mainRow.layout()) as rightColumn:
                rightColumn.layout().setAlignment(QtCore.Qt.AlignTop)
                with wrap.Frame(rightColumn.layout(), label='Solidify', margins=[2, 0, 2, 0]) as rightFrame1:
                    rightFrame1.setCollapsible(False)
                    rightFrame1.getFrameLayout().setAlignment(QtCore.Qt.AlignTop)
                    for i in range(len(self.solidify)):
                        btn = wrap.Button(rightFrame1.getFrameLayout(), 'gsFilter_%s' % self.solidify[i][1])
                        btn.setLabel(self.solidify[i][0])
                        btn.setButtonStyle('small')
                        btn.setCheckable(True)
                        btn.setChecked(True)
                with wrap.Frame(rightColumn.layout(), label='Graphs', margins=[2, 0, 2, 0]) as rightFrame2:
                    rightFrame2.setCollapsible(False)
                    rightFrame2.getFrameLayout().setAlignment(QtCore.Qt.AlignTop)
                    for i in range(len(self.graphs)):
                        btn = wrap.Button(rightFrame2.getFrameLayout(), 'gsFilter_%s' % self.graphs[i][1])
                        btn.setLabel(list(self.graphs)[i][0])
                        btn.setButtonStyle('small')
                        btn.setCheckable(True)
                        btn.setChecked(True)
                with wrap.Frame(rightColumn.layout(), label='UVs', margins=[2, 0, 2, 0]) as rightFrame3:
                    rightFrame3.setCollapsible(False)
                    rightFrame3.getFrameLayout().setAlignment(QtCore.Qt.AlignTop)
                    for i in range(len(self.uvs)):
                        btn = wrap.Button(rightFrame3.getFrameLayout(), 'gsFilter_%s' % self.uvs[i][1])
                        btn.setLabel(list(self.uvs)[i][0])
                        btn.setButtonStyle('small')
                        btn.setCheckable(True)
                        btn.setChecked(True)

        layout.addWidget(wrap.separator())

        with wrap.Row(layout) as confirmCancelLayout:
            btn = wrap.Button(confirmCancelLayout.layout())
            btn.setLabel('Save')
            btn.clicked.connect(self.saveToOptionVar)
            btn.clicked.connect(lambda: MESSAGE.printInView("Filters Saved"))
            btn = wrap.Button(confirmCancelLayout.layout())
            btn.setLabel('Close')
            btn.clicked.connect(self.closeUI)

        self.updateUI()
        self.saveToOptionVar()

    def closeUI(self):
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            mc.deleteUI(self.uiName)

    def updateUI(self):
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            controlsDict = self.getFromOptionVar()
            if controlsDict and isinstance(controlsDict, dict):
                for key in controlsDict:
                    buttonName = 'gsFilter_%s' % key
                    WIDGETS[buttonName].setChecked(controlsDict[key])

    def saveToOptionVar(self):
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            allControls = self.attrs + self.graphs + self.uvs + self.solidify
            controlsDict = {}
            for control in allControls:
                buttonName = 'gsFilter_%s' % control[1]
                button = WIDGETS[buttonName] if buttonName in WIDGETS else None
                if button:
                    controlsDict.update({control[1]: button.isChecked()})
            mc.optionVar(sv=('GSCT_AttributesFilter', str(controlsDict)))

    def getFromOptionVar(self):
        if mc.optionVar(ex='GSCT_AttributesFilter'):
            dictString = mc.optionVar(q='GSCT_AttributesFilter')
            if dictString:
                return dict(eval(dictString))


attributesFilter = AttributesFilter()


class CardToCurveWindow:

    def __init__(self):
        self.uiName = "GSCT_CardToCurvePopOut"
        self.buttonsDict = {}

    def openUI(self):
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            if mc.workspaceControl(self.uiName, q=1, vis=1):
                mc.deleteUI(self.uiName)
                return
            else:
                mc.deleteUI(self.uiName)

        self.buttonsDict = self.loadClickedButtons()
        self.getBtn = lambda name: self.buttonsDict[name] if name in self.buttonsDict else True

        popOut = CreatePopOut(self.uiName, "Card to Curve", 245, 271)
        layout = popOut.widgetLayout
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.mainButtonGroup = QtWidgets.QButtonGroup()
        self.mainButtonGroup.setExclusive(False)
        self.mainButtonGroup.buttonClicked.connect(self.saveButtonsState)
        with wrap.Column(layout) as mainColumn:
            mainColumn.layout().setAlignment(QtCore.Qt.AlignTop)

            with wrap.Frame(mainColumn.layout(), label='Output Type:', objName='gsCardToCurve_outputTypeSwitch') as outputTypeFrame:
                outputTypeFrame.setCollapsible(False)
                outputTypeFrame.setCollapsed(False)

                with wrap.Row(outputTypeFrame.getFrameLayout()) as outputTypeSwitch:
                    self.outputTypeGroup = QtWidgets.QButtonGroup()
                    WIDGETS['gsCardToCurve_cardTypeGroup'] = self.outputTypeGroup

                    generateCards = wrap.Button(outputTypeSwitch.layout(), 'gsCardToCurve_generateCards')
                    generateCards.setButtonStyle('small')
                    generateCards.setLabel('Cards')
                    generateCards.setCheckable(True)

                    generateCurves = wrap.Button(outputTypeSwitch.layout(), 'gsCardToCurve_generateCurves')
                    generateCurves.setButtonStyle('small')
                    generateCurves.setLabel('Curves Only')
                    generateCurves.setCheckable(True)

                    self.outputTypeGroup.addButton(generateCards, 0)
                    self.outputTypeGroup.addButton(generateCurves, 1)
                    generateCards.setChecked(not mc.optionVar(q='GSCT_CardToCurveOutputType'))
                    generateCurves.setChecked(mc.optionVar(q='GSCT_CardToCurveOutputType'))
                    self.outputTypeGroup.buttonClicked.connect(self.updateActiveButtons)

            with wrap.Frame(mainColumn.layout(), label='Card Type:', objName="gsCardToCurve_cardType") as cardTypeFrame:
                self.cardTypeFrame = cardTypeFrame
                cardTypeFrame.setCollapsible(False)
                cardTypeFrame.setCollapsed(False)

                with wrap.Row(cardTypeFrame.getFrameLayout()) as outputTypeSwitch:
                    self.cardTypeGroup = QtWidgets.QButtonGroup()
                    WIDGETS['gsCardToCurve_cardTypeGroup'] = self.cardTypeGroup

                    self.warpCards = wrap.Button(outputTypeSwitch.layout(), 'gsCardToCurve_warp')
                    self.warpCards.setButtonStyle('small')
                    self.warpCards.setLabel('Warp')
                    self.warpCards.setCheckable(True)

                    extrudeCards = wrap.Button(outputTypeSwitch.layout(), 'gsCardToCurve_extrude')
                    extrudeCards.setButtonStyle('small')
                    extrudeCards.setLabel('Extrude')
                    extrudeCards.setCheckable(True)

                    self.cardTypeGroup.addButton(self.warpCards, 0)
                    self.cardTypeGroup.addButton(extrudeCards, 1)
                    self.warpCards.setChecked(not mc.optionVar(q='GSCT_CardToCurveCardType'))
                    extrudeCards.setChecked(mc.optionVar(q='GSCT_CardToCurveCardType'))
                    self.cardTypeGroup.buttonClicked.connect(self.updateActiveButtons)

            with wrap.Frame(mainColumn.layout(), label='Match Attributes:', objName="gsCardToCurve_matchAttributes") as matchAttributeFrame:
                self.matchAttributeFrame = matchAttributeFrame
                matchAttributeFrame.setCollapsible(False)
                matchAttributeFrame.setCollapsed(False)

                with wrap.Row(matchAttributeFrame.getFrameLayout()) as row:
                    orientation = wrap.Button(row.layout(), 'gsCardToCurve_orientation')
                    orientation.setButtonStyle('small')
                    orientation.setLabel('Orientation')
                    orientation.setCheckable(True)
                    orientation.setChecked(self.getBtn('gsCardToCurve_orientation'))

                    width = wrap.Button(row.layout(), 'gsCardToCurve_width')
                    width.setButtonStyle('small')
                    width.setLabel('Width')
                    width.setCheckable(True)
                    width.setChecked(self.getBtn('gsCardToCurve_width'))

                    self.mainButtonGroup.addButton(orientation)
                    self.mainButtonGroup.addButton(width)

                with wrap.Row(matchAttributeFrame.getFrameLayout()) as row:
                    taper = wrap.Button(row.layout(), 'gsCardToCurve_taper')
                    taper.setButtonStyle('small')
                    taper.setLabel('Taper')
                    taper.setCheckable(True)
                    taper.setChecked(self.getBtn('gsCardToCurve_taper'))

                    twist = wrap.Button(row.layout(), 'gsCardToCurve_twist')
                    twist.setButtonStyle('small')
                    twist.setLabel('Twist')
                    twist.setCheckable(True)
                    twist.setChecked(self.getBtn('gsCardToCurve_twist'))

                    self.mainButtonGroup.addButton(taper)
                    self.mainButtonGroup.addButton(twist)

                with wrap.Row(matchAttributeFrame.getFrameLayout()) as row:
                    profile = wrap.Button(row.layout(), 'gsCardToCurve_profile')
                    profile.setButtonStyle('small')
                    profile.setLabel('Profile')
                    profile.setCheckable(True)
                    profile.setChecked(self.getBtn('gsCardToCurve_profile'))

                    material = wrap.Button(row.layout(), 'gsCardToCurve_material')
                    material.setButtonStyle('small')
                    material.setLabel('Material')
                    material.setCheckable(True)
                    material.setChecked(self.getBtn('gsCardToCurve_material'))

                    self.mainButtonGroup.addButton(profile)
                    self.mainButtonGroup.addButton(material)

                UVs = wrap.Button(matchAttributeFrame.getFrameLayout(), 'gsCardToCurve_UVs')
                UVs.setButtonStyle('small')
                UVs.setLabel('UVs')
                UVs.setCheckable(True)
                UVs.setChecked(self.getBtn('gsCardToCurve_UVs'))
                UVs.clicked.connect(self.updateActiveButtons)
                self.mainButtonGroup.addButton(UVs)

            with wrap.Frame(mainColumn.layout(), label='UV Match Options:', objName="gsCardToCurve_UVMatchOptions") as uvMatchOptionsFrame:
                self.uvMatchOptionsFrame = uvMatchOptionsFrame
                uvMatchOptionsFrame.setCollapsible(False)
                uvMatchOptionsFrame.setCollapsed(False)

                with wrap.Row(uvMatchOptionsFrame.getFrameLayout()) as row:
                    verticalFlip = wrap.Button(row.layout(), 'gsCardToCurve_verticalFlip')
                    verticalFlip.setButtonStyle('small')
                    verticalFlip.setLabel('Vertical Flip')
                    verticalFlip.setCheckable(True)
                    verticalFlip.setChecked(self.getBtn('gsCardToCurve_verticalFlip'))

                    horizontalFlip = wrap.Button(row.layout(), 'gsCardToCurve_horizontalFlip')
                    horizontalFlip.setButtonStyle('small')
                    horizontalFlip.setLabel('Horizontal Flip')
                    horizontalFlip.setCheckable(True)
                    horizontalFlip.setChecked(self.getBtn('gsCardToCurve_horizontalFlip'))

                    self.mainButtonGroup.addButton(verticalFlip)
                    self.mainButtonGroup.addButton(horizontalFlip)

            with wrap.Frame(mainColumn.layout(), label='Other:') as otherOptionsFrame:
                otherOptionsFrame.setCollapsible(False)
                otherOptionsFrame.setCollapsed(False)
                reverseCurve = wrap.Button(otherOptionsFrame.getFrameLayout(), 'gsCardToCurve_reverseCurve')
                reverseCurve.setButtonStyle('small')
                reverseCurve.setLabel('Reverse Curve')
                reverseCurve.setCheckable(True)
                reverseCurve.setChecked(self.getBtn('gsCardToCurve_reverseCurve'))

                self.mainButtonGroup.addButton(reverseCurve)

            mainColumn.layout().addWidget(wrap.separator())
            with wrap.Row(mainColumn.layout(), margins=style.scale([0, 3, 0, 3])) as _:
                pass
            mainColumn.layout().addWidget(wrap.separator())
            with wrap.Row(mainColumn.layout()) as row:
                convertSelected = wrap.Button(row.layout(), objName="gsCardToCurve_convertSelected")
                convertSelected.setLabel('Convert Selected')
                convertSelected.clicked.connect(undo(core.cardToCurve))

                cancel = wrap.Button(row.layout())
                cancel.setLabel('Cancel')
                cancel.clicked.connect(self.closeUI)

            self.updateActiveButtons()
            self.saveButtonsState()

    def closeUI(self):
        self.saveButtonsState()
        if mc.workspaceControl(self.uiName, q=1, ex=1):
            if mc.workspaceControl(self.uiName, q=1, vis=1):
                mc.deleteUI(self.uiName)
            else:
                mc.deleteUI(self.uiName)

    def updateActiveButtons(self):
        if self.outputTypeGroup.checkedId() == 1:
            self.matchAttributeFrame.setEnabled(False)
            self.uvMatchOptionsFrame.setEnabled(False)
            self.cardTypeFrame.setEnabled(False)
            mc.optionVar(iv=['GSCT_CardToCurveOutputType', 1])
        else:
            mc.optionVar(iv=['GSCT_CardToCurveOutputType', 0])
            mc.optionVar(iv=['GSCT_CardToCurveCardType', int(not self.warpCards.isChecked())])
            self.matchAttributeFrame.setEnabled(True)
            self.cardTypeFrame.setEnabled(True)
            if WIDGETS['gsCardToCurve_UVs'].isChecked():
                self.uvMatchOptionsFrame.setEnabled(True)
            else:
                self.uvMatchOptionsFrame.setEnabled(False)

    def saveButtonsState(self):
        buttons = self.mainButtonGroup.buttons()
        buttonsDict = {}
        for b in buttons:
            buttonsDict.update({b.objName: b.isChecked()})
        mc.optionVar(sv=['GSCT_CardToCurveOptions', str(buttonsDict)])

    def loadClickedButtons(self):
        return eval(mc.optionVar(q='GSCT_CardToCurveOptions'))


cardToCurveWindow = CardToCurveWindow()


def scaleFactorWindow():
    windowName = SCALE_FACTOR_UI
    if mc.workspaceControl(windowName, q=1, ex=1):
        mc.deleteUI(windowName)
    popOut = CreatePopOut(windowName, "Scale Factor", 300, 95)

    layout = popOut.widgetLayout

    scaleFactor = core.getScaleFactor()
    m_slider = mc.floatSliderGrp('GSCT_scaleFactorSlider',
                                 pre=3, ss=0.01, min=0.01, max=10, fmn=0.001, fmx=1000, f=1,
                                 v=scaleFactor
                                 )

    wrap.MayaSlider(m_slider, layout=layout)

    with wrap.Row(layout) as row:
        saveButton = wrap.Button(row.layout())
        saveButton.setLabel('Save')
        saveButton.clicked.connect(pa(core.saveScaleFactor, windowName, False))
        saveButton.clicked.connect(updateScaleFactorWindow)
        saveAndCloseButton = wrap.Button(row.layout())
        saveAndCloseButton.setLabel('Save & Close')
        saveAndCloseButton.clicked.connect(pa(core.saveScaleFactor, windowName))
        cancelButton = wrap.Button(row.layout())
        cancelButton.setLabel('Cancel')
        cancelButton.clicked.connect(lambda: mc.deleteUI(windowName))

    layout.addWidget(wrap.separator())

    with wrap.Row(layout) as row:
        with wrap.Row(row.layout(), margins=style.scale([2, 0, 2, 0])) as globalRow:
            label = wrap.Label(globalRow.layout())
            label.setLabel("Global:")
            globalValue = mc.optionVar(q=('GSCT_globalScaleFactor'))
            field = wrap.LineEdit("scaleFactorGlobalValue", globalRow.layout())
            field.setText(str(globalValue))
            field.setEnabled(False)
        with wrap.Row(row.layout(), margins=style.scale([2, 0, 2, 0])) as sceneRow:
            label = wrap.Label(sceneRow.layout())
            label.setLabel("Scene:")
            if mc.objExists('gsScaleFactorStorageNode') and mc.attributeQuery('scaleFactor', n='gsScaleFactorStorageNode', ex=1):
                sceneValue = mc.getAttr('gsScaleFactorStorageNode.scaleFactor')
            else:
                sceneValue = "####"
            field = wrap.LineEdit("scaleFactorSceneValue", sceneRow.layout())
            field.setText(str(sceneValue))
            field.setEnabled(False)

        with wrap.Row(row.layout(), margins=style.scale([2, 0, 2, 0])) as sceneRow:
            label = wrap.Label(sceneRow.layout())
            label.setLabel("Selected:")
            if mc.objExists('gsScaleFactorStorageNode') and mc.attributeQuery('scaleFactor', n='gsScaleFactorStorageNode', ex=1):
                sceneValue = mc.getAttr('gsScaleFactorStorageNode.scaleFactor')
            else:
                sceneValue = "####"
            field = wrap.LineEdit("scaleFactorSelectedValue", sceneRow.layout())
            field.setText(str(sceneValue))
            field.setEnabled(False)

    from . import main
    main.checkScriptJobs(SCALE_FACTOR_UI)


def updateScaleFactorWindow():
    WIDGETS["scaleFactorGlobalValue"].setText(str(mc.optionVar(q=('GSCT_globalScaleFactor'))))
    if mc.objExists('gsScaleFactorStorageNode') and mc.attributeQuery('scaleFactor', n='gsScaleFactorStorageNode', ex=1):
        sceneValue = mc.getAttr('gsScaleFactorStorageNode.scaleFactor')
    else:
        sceneValue = "####"
    WIDGETS["scaleFactorSceneValue"].setText(str(sceneValue))


def scaleFactorConversionDialog():
    MESSAGE.warningInView('Curves Without Scale Factor Detected')
    dialog = mc.confirmDialog(
        title='No Scale Factor',
        message='Curves without scale factor detected\nThose Curves were created before v1.2.7 and might not convert correctly',
        icon='warning',
        button=['Skip Old Curves', 'Convert All', 'Cancel'],
        cancelButton='Cancel',
        dismissString='Cancel'
    )
    if dialog == 'Cancel':
        return None
    if dialog == 'Skip Old Curves':
        return 'Skip'
    if 'Convert All':
        return 'All'


def curveThicknessWindow():
    name = 'GSCT_CurveThicknessWindow'
    if mc.workspaceControl(name, q=1, ex=1):
        mc.deleteUI(name)
    popOut = CreatePopOut(name, "Curve Thickness", 300, 65)

    layout = popOut.widgetLayout

    layout.setAlignment(QtCore.Qt.AlignTop)

    m_slider = mc.floatSliderGrp('GSCT_curveThicknessSlider',
                                 pre=3, ss=0.01, min=-1, max=10, fmn=0.001, fmx=1000, f=1,
                                 v=mc.optionVar(q='GSCT_globalCurveThickness')
                                 )

    wrap.MayaSlider(m_slider, layout=layout)

    with wrap.Row(layout, margins=style.scale([0, 5, 0, 0])) as row:
        def save():
            mc.optionVar(fv=('GSCT_globalCurveThickness', mc.floatSliderGrp('GSCT_curveThicknessSlider', q=1, v=1)))
            mc.deleteUI(name)

        def update():
            mc.optionVar(fv=('GSCT_globalCurveThickness', mc.floatSliderGrp('GSCT_curveThicknessSlider', q=1, v=1)))
            core.updateLayerThickness()
        saveButton = wrap.Button(row.layout())
        saveButton.setLabel('Save')
        saveButton.clicked.connect(save)
        updateCurves = wrap.Button(row.layout())
        updateCurves.setLabel('Update Curves')
        updateCurves.clicked.connect(update)
        cancelButton = wrap.Button(row.layout())
        cancelButton.setLabel('Cancel')
        cancelButton.clicked.connect(lambda: mc.deleteUI(name))


def randomizeCurveWindow():
    name = "GSCT_RandomizeCurvePopOut"
    if mc.workspaceControl(name, q=1, ex=1):
        if mc.workspaceControl(name, q=1, vis=1):
            mc.deleteUI(name)
            return
        else:
            mc.deleteUI(name)
    popOut = CreatePopOut(name, "Randomize Curve", 270, 565)

    layout = popOut.widgetLayout
    layout.setAlignment(QtCore.Qt.AlignTop)

    def release(slider, *_):
        core.sliders.randSliderDrag(slider)
        core.sliders.randSliderRelease(slider)
        core.sliders.release()
    # Control Points
    with wrap.Frame(layout, label='Control Points') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider0')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveCVsRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        with wrap.Row(frame.getFrameLayout()) as row:
            lockFirst = wrap.Button(row.layout(), 'gsLockFirstCV')
            lockFirst.setLabel('Lock First CV', lineHeight=100)
            lockFirst.setButtonStyle('small')
            lockFirst.setCheckable(True)

            lockLast = wrap.Button(row.layout(), 'gsLockLastCV')
            lockLast.setLabel('Lock Last CV', lineHeight=100)
            lockLast.setButtonStyle('small')
            lockLast.setCheckable(True)

        with wrap.Row(frame.getFrameLayout()) as row:
            axisX = wrap.Button(row.layout(), 'gsRandAxisX')
            axisX.setLabel('X', lineHeight=100)
            axisX.setButtonStyle('small')
            axisX.setCheckable(True)

            axisY = wrap.Button(row.layout(), 'gsRandAxisY')
            axisY.setLabel('Y', lineHeight=100)
            axisY.setButtonStyle('small')
            axisY.setCheckable(True)

            axisZ = wrap.Button(row.layout(), 'gsRandAxisZ')
            axisZ.setLabel('Z', lineHeight=100)
            axisZ.setButtonStyle('small')
            axisZ.setCheckable(True)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveCVsRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 0),
                cc=pa(release, 0),
            ),
            layout=frame.getFrameLayout()
        )

    # Rotation
    with wrap.Frame(layout, label='Rotation') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider1')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveRotationRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        with wrap.Row(frame.getFrameLayout()) as row:
            axisX = wrap.Button(row.layout(), 'gsRandRotateAxisX')
            axisX.setLabel('X', lineHeight=100)
            axisX.setButtonStyle('small')
            axisX.setCheckable(True)

            axisY = wrap.Button(row.layout(), 'gsRandRotateAxisY')
            axisY.setLabel('Y', lineHeight=100)
            axisY.setButtonStyle('small')
            axisY.setCheckable(True)

            axisZ = wrap.Button(row.layout(), 'gsRandRotateAxisZ')
            axisZ.setLabel('Z', lineHeight=100)
            axisZ.setButtonStyle('small')
            axisZ.setCheckable(True)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveRotationRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 1),
                cc=pa(release, 1),
            ),
            layout=frame.getFrameLayout()
        )

    # Orientation
    with wrap.Frame(layout, label='Orientation') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider2')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveOrientationRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveOrientationRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 2),
                cc=pa(release, 2),
            ),
            layout=frame.getFrameLayout()
        )

    # Twist
    with wrap.Frame(layout, label='Twist') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider3')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveTwistRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveTwistRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 3),
                cc=pa(release, 3),
            ),
            layout=frame.getFrameLayout()
        )

    # Width
    with wrap.Frame(layout, label='Width') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider4')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveWidthRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        uniform = wrap.Button(frame.getFrameLayout(), 'gsWidthCheckBoxUniform')
        uniform.setButtonStyle('small')
        uniform.setLabel('Uniform', lineHeight=100)
        uniform.setCheckable(True)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveWidthRand', min=0.001, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 4),
                cc=pa(release, 4),
            ),
            layout=frame.getFrameLayout()
        )

    # Taper
    with wrap.Frame(layout, label='Taper') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider5')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveTaperRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveTaperRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 5),
                cc=pa(release, 5),
            ),
            layout=frame.getFrameLayout()
        )

    # Profile
    with wrap.Frame(layout, label='Profile') as frame:
        frame.setCollapsible(False)
        with wrap.Row(frame.getFrameLayout()) as row:
            enable = wrap.Button(row.layout(), 'curveRandomizeSlider6')
            enable.setLabel('Enabled', lineHeight=100)
            enable.setButtonStyle('small')
            enable.setCheckable(True)

            slider = wrap.mayaSlider(mc.floatSliderGrp('gsCurveProfileRandMulti', l='Mult:',
                                                       min=1, max=50, pre=1, step=0.5, cw=[(1, 30), (2, 1)]))
            row.layout().addWidget(slider)

        uniform = wrap.Button(frame.getFrameLayout(), 'gsProfileCheckBoxNegative')
        uniform.setButtonStyle('small')
        uniform.setLabel('Allow Negative Values', lineHeight=100)
        uniform.setCheckable(True)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveProfileRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 6),
                cc=pa(release, 6),
            ),
            layout=frame.getFrameLayout()
        )

    # Selection
    with wrap.Frame(layout, label='Selection') as frame:
        frame.setCollapsible(False)

        enable = wrap.Button(frame.getFrameLayout(), 'curveRandomizeSlider7')
        enable.setLabel('Enabled', lineHeight=100)
        enable.setButtonStyle('small')
        enable.setCheckable(True)

        wrap.MayaSlider(
            mc.floatSliderGrp(
                'gsCurveSelectRand', min=0, max=1, step=0.05,
                dc=pa(core.sliders.randSliderDrag, 7),
                cc=pa(release, 7),
            ),
            layout=frame.getFrameLayout()
        )

    layout.addWidget(wrap.separator())

    with wrap.Row(layout) as row:
        def randomizeClick():
            core.sliders.randSliderDrag(-1)
            core.sliders.randSliderRelease(-1)
            core.sliders.release()
        randomize = wrap.Button(row.layout())
        randomize.setLabel("Randomize")
        randomize.clicked.connect(randomizeClick)

        close = wrap.Button(row.layout())
        close.setLabel("Close")
        close.clicked.connect(lambda: mc.deleteUI(name))
