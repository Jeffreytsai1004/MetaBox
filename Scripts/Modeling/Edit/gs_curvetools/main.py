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
import sys
from datetime import datetime
from functools import partial as pa
from imp import reload

import maya.cmds as mc
from PySide2 import QtCore, QtGui, QtWidgets

from . import core, ui
from . import constants
from .constants import *
from .utils import style, tooltips, utils, wrap
from .utils.utils import deferred, deferredLp, noUndo, undo
from .utils.wrap import WIDGETS

reload(core)
reload(utils)
reload(style)
reload(wrap)
reload(ui)
reload(tooltips)
reload(constants)

# Loggers
MESSAGE = utils.logger
LOGGER = utils.logger.logger

LOGGER.debug('-----------------Starting Log Session-----------------')
LOGGER.debug('                 {}                 '.format(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))

### Interface Script Jobs ###


def checkScriptJobs(controlName):
    """ Checks if script jobs exist and adds them if necessary """
    jobNumbers = list()
    workspaceExists = False
    UI = 'control'
    if mc.workspaceControl(controlName, exists=1):
        workspaceExists = True
    if controlName == MAIN_WINDOW_NAME:
        UI = 'main'
    elif controlName == UV_EDITOR_NAME:
        UI = 'uv_editor'
    elif controlName == SCALE_FACTOR_UI:
        UI = 'scale_factor_ui'
    jobList = mc.scriptJob(lj=1)
    for job in jobList:
        if controlName in job:
            jobNumbers.append(job.split()[0][0:-1])
    if len(jobNumbers) == 0 and workspaceExists:
        scriptJobsInit(UI)
        LOGGER.info('scriptJobs created for "%s" UI!' % UI)
    elif len(jobNumbers) > 0 and not workspaceExists:
        LOGGER.info('scriptJobs deleted!')
        for number in jobNumbers:
            mc.scriptJob(k=number)


def scriptJobsInit(uiName):
    if uiName == 'main':
        mc.scriptJob(per=1, p=MAIN_WINDOW_NAME, event=['SceneOpened', pa(checkScriptJobs, MAIN_WINDOW_NAME)])
        mc.scriptJob(per=1, p=MAIN_WINDOW_NAME, event=['SceneOpened', pa(deferred(core.updateMainUI), True)])
        mc.scriptJob(per=1, p=MAIN_WINDOW_NAME, event=['SceneOpened', deferredLp(core.onSceneOpenedUpdateLayerCount)])
        mc.scriptJob(per=1, p=MAIN_WINDOW_NAME, event=['SelectionChanged', core.updateMainUI])
        mc.scriptJob(per=1, p=MAIN_WINDOW_NAME, event=['Undo', core.updateMainUI])
    elif uiName == 'control':
        mc.scriptJob(per=1, p=CURVE_CONTROL_NAME, event=['SelectionChanged', core.curveControlUI.updateUI])
        mc.scriptJob(per=1, p=CURVE_CONTROL_NAME, event=['Undo', deferred(core.curveControlUI.updateUI)])
    elif uiName == 'uv_editor':
        def updateUVs():
            if (mc.workspaceControl(UV_EDITOR_NAME, q=1, ex=1) and
                    mc.workspaceControl(UV_EDITOR_NAME, q=1, r=1)):
                ui.uveditor.updateEditor()
        mc.scriptJob(per=1, p=UV_EDITOR_NAME, event=['SelectionChanged', updateUVs])
        mc.scriptJob(per=1, p=UV_EDITOR_NAME, event=['Undo', updateUVs])


def main():
    utils.checkNativePlugins(['curveWarp'], MAIN_WINDOW_NAME)
    if mc.workspaceControl(MAIN_WINDOW_NAME, q=1, ex=1):
        if MAYA_VER >= 2018:
            if not mc.workspaceControl(MAIN_WINDOW_NAME, q=1, vis=1):
                mc.workspaceControl(MAIN_WINDOW_NAME, e=1, rs=1)
                core.updateMainUI()
            else:
                mc.workspaceControl(MAIN_WINDOW_NAME, e=1, vis=0)
        else:
            mc.workspaceControl(MAIN_WINDOW_NAME, e=1, fl=1)
            mc.deleteUI(MAIN_WINDOW_NAME)
    else:
        CurveToolsUI()
        mc.workspaceControl(MAIN_WINDOW_NAME, e=1, ui=UI_SCRIPT)
        try:
            core.toggleColor.checkColorStorageNode()
            checkScriptJobs(MAIN_WINDOW_NAME)
            utils.deferred(core.onSceneOpenedUpdateLayerCount)()  # Also updates the UI
        except Exception as e:
            LOGGER.exception(e)

# Main UI


class CurveToolsUI(QtWidgets.QWidget):

    def __init__(self):
        WIDGETS.clear()
        # Maya Native Workspace
        parent = ui.mayaWorkspaceControl(name=MAIN_WINDOW_NAME, label=MAIN_WINDOW_LABEL)

        # Resolve Fonts
        fontDatabase = QtGui.QFontDatabase()
        fontDatabase.removeAllApplicationFonts()
        fonts = os.listdir(utils.getFolder.fonts())
        for font in fonts:
            fontDatabase.addApplicationFont(utils.getFolder.fonts() + font)

        # Dockable Workspace Connection
        super(CurveToolsUI, self).__init__(parent)
        self.ui()
        parent.layout().addWidget(self)
        self.scrollWidget.setFocus()

        checkScriptJobs(MAIN_WINDOW_NAME)

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

        # Menu buttons
        menuBarWidget = QtWidgets.QWidget()
        menuBarLayout = QtWidgets.QHBoxLayout(menuBarWidget)
        menuBarLayout.setContentsMargins(0, 0, 0, 0)
        menuBarLayout.setAlignment(QtCore.Qt.AlignCenter)

        menuBar = QtWidgets.QMenuBar()
        menuBar.setSizePolicy(PREFERRED_POLICY)
        menuBarLayout.addWidget(menuBar)
        layout.addWidget(menuBarWidget)

        # Options Menu
        with wrap.Menu('Options', menuBar) as menu:
            menu.triggered.connect(core.saveOptions)

            menu.addSection('Import / Export')
            importCurves = wrap.MenuItem('importCurves', 'Import Curves', menu)
            importCurves.triggered.connect(noUndo(core.importExport.importCurves))
            exportCurves = wrap.MenuItem('exportCurves', 'Export Curves', menu)
            exportCurves.triggered.connect(core.importExport.exportCurves)

            menu.addSection('Global Modifiers')
            changeScaleFactor = wrap.MenuItem('changeScaleFactor', 'Change Scale Factor', menu)
            changeScaleFactor.triggered.connect(ui.scaleFactorWindow)
            globalCurveThickness = wrap.MenuItem('globalCurveThickness', 'Global Curve Thickness', menu)
            globalCurveThickness.triggered.connect(ui.curveThicknessWindow)

            menu.addSection('Viewport Commands')
            setAOSettings = wrap.MenuItem('setAOSettings', 'Set AO Settings', menu)
            setAOSettings.triggered.connect(core.setAOSettings)

            with wrap.Menu('Transparency Settings', menu) as transparencySettingsMenu:
                simpleTransparency = wrap.MenuItem(
                    'setSimpleTransparency',
                    'Simple Transparency (Fast, Inncaurate)',
                    transparencySettingsMenu
                )
                simpleTransparency.triggered.connect(noUndo(pa(core.setTransparencySettings, 0)))
                objectSortingTransparency = wrap.MenuItem(
                    'setObjectSortingTransparency',
                    'Object Sorting Transparency (Average)',
                    transparencySettingsMenu
                )
                objectSortingTransparency.triggered.connect(noUndo(pa(core.setTransparencySettings, 1)))
                setDepthTransparency = wrap.MenuItem(
                    'setDepthTransparency',
                    'Depth Transparency (Accurate, Slow)',
                    transparencySettingsMenu
                )
                setDepthTransparency.triggered.connect(noUndo(pa(core.setTransparencySettings, 2)))

            menu.addSection('Convert Curves')
            with wrap.Menu('Convert Curves', menu) as convertCurvesSubmenu:
                convertToWarpCard = wrap.MenuItem('convertToWarpCard', "Convert to Warp Card", convertCurvesSubmenu)
                convertToWarpCard.triggered.connect(pa(undo(core.convertSelectionTo), 0))
                convertToWarpTube = wrap.MenuItem('convertToWarpTube', "Convert to Warp Tube", convertCurvesSubmenu)
                convertToWarpTube.triggered.connect(pa(undo(core.convertSelectionTo), 1))
                convertToExtrudeCard = wrap.MenuItem('convertToExtrudeCard', "Convert to Extrude Card", convertCurvesSubmenu)
                convertToExtrudeCard.triggered.connect(pa(undo(core.convertSelectionTo), 2))
                convertToExtrudeTube = wrap.MenuItem('convertToExtrudeTube', "Convert to Extrude Tube", convertCurvesSubmenu)
                convertToExtrudeTube.triggered.connect(pa(undo(core.convertSelectionTo), 3))

            menu.addSection('General Options')
            wrap.MenuItem('keepCurveAttributes', 'Keep Curve Attributes', menu, True, core.getOption('keepCurveAttributes'))
            wrap.MenuItem('populateBlendAttributes', 'Add Cards/Tubes Blend Attributes',
                          menu, True, core.getOption('populateBlendAttributes'))
            wrap.MenuItem('convertInstances', 'Auto Convert Instances', menu, True, core.getOption('convertInstances'))

            wrap.MenuItem('useAutoRefineOnNewCurves', 'Use Auto-Refine on New Curves',
                          menu, True, core.getOption('useAutoRefineOnNewCurves'))
            wrap.MenuItem('flipUVsAfterMirror', 'Flip UVs After Mirror',
                          menu, True, core.getOption('flipUVsAfterMirror'))
            enableTooltipsMenu = wrap.MenuItem('enableTooltips', 'Enable Tooltips', menu, True, core.getOption('enableTooltips'))
            enableTooltipsMenu.triggered.connect(self.toggleTooltips)

            menu.addSection('Color Options')
            syncColor = wrap.MenuItem('syncCurveColor', 'Sync Curve Color to Layer Color', menu, True, core.getOption('syncCurveColor'))
            syncColor.triggered.connect(core.toggleColor.syncCurveColors)
            wrap.MenuItem('colorizedRegroup', 'Colorize Regrouped Layers', menu, True, core.getOption('colorizedRegroup'))
            colorOnlyDiffuse = wrap.MenuItem('colorOnlyDiffuse', 'Color Only Affects Diffuse',
                                             menu, True, core.getOption('colorOnlyDiffuse'))
            colorOnlyDiffuse.triggered.connect(core.toggleColor.updateColorOptions)
            checkerPattern = wrap.MenuItem('checkerPattern', 'Checker Pattern for Color Mode', menu, True, core.getOption('checkerPattern'))
            checkerPattern.triggered.connect(core.toggleColor.updateColorOptions)

            menu.addSection('Bind Options')
            wrap.MenuItem('boundCurvesFollowParent', 'Bound Curves Follow Parent', menu, True, core.getOption('boundCurvesFollowParent'))
            wrap.MenuItem('massBindOption', 'Bind to All Available Empty Curves', menu, True, core.getOption('massBindOption'))
            wrap.MenuItem('bindDuplicatesCurves', 'Duplicate Curves Before Bind', menu, True, core.getOption('bindDuplicatesCurves'))
            wrap.MenuItem('bindFlipUVs', 'Flip UVs before Bind', menu, True, core.getOption('bindFlipUVs'))

            menu.addSection('Layer Options')
            wrap.MenuItem('ignoreLastLayer', 'Ignore Last Layer', menu, True, core.getOption('ignoreLastLayer'))
            wrap.MenuItem('syncOutlinerLayerVis', 'Sync Outliner/Layer Visibility', menu, True, core.getOption('syncOutlinerLayerVis'))
            wrap.MenuItem('replacingCurveLayerSelection', 'Replacing Curve Layer Selection', menu, True,
                          core.getOption('replacingCurveLayerSelection'))
            onlyNumbersInLayers = wrap.MenuItem('layerNumbersOnly', 'Use Only Numbers in Layers', menu, True,
                                                core.getOption('layerNumbersOnly'))
            onlyNumbersInLayers.triggered.connect(core.changeLayersToNumbers)
            onlyNumbersInLayers.triggered.connect(self.updateLayerList)
            with wrap.Menu('Number of Active Layers', menu) as layerNumberMenu:
                with wrap.ActionGroup('layerRowsActionGroup', layerNumberMenu) as actionGroup:
                    wrap.MenuItem('2layerRows', '20 Layers', layerNumberMenu, True,
                                  core.getOption('2layerRows'), collection=actionGroup)
                    wrap.MenuItem('3layerRows', '30 Layers', layerNumberMenu, True,
                                  core.getOption('3layerRows'), collection=actionGroup)
                    wrap.MenuItem('4layerRows', '40 Layers', layerNumberMenu, True,
                                  core.getOption('4layerRows'), collection=actionGroup)
                    wrap.MenuItem('6layerRows', '60 Layers', layerNumberMenu, True,
                                  core.getOption('6layerRows'), collection=actionGroup)
                    wrap.MenuItem('8layerRows', '80 Layers', layerNumberMenu, True,
                                  core.getOption('8layerRows'), collection=actionGroup)
                    actionGroup.triggered.connect(core.updateMainUI)

            menu.addSection('Layer Collection Options')
            wrap.MenuItem('ignoreTemplateCollections', 'Ignore "Template" Collection Names', menu, True, core.getOption('ignoreTemplateCollections'))
            wrap.MenuItem('groupTemplateCollections', 'Group "Template" Collections Together', menu, True, core.getOption('groupTemplateCollections'))
            layerCollectionsToggle = wrap.MenuItem('showLayerCollectionsMenu', 'Show Layer Collections Menu',
                                                   menu, True, core.getOption('showLayerCollectionsMenu'))
            layerCollectionsToggle.triggered.connect(core.layerCollections.toggleLayerCollectionsWidget)
            wrap.MenuItem('importIntoANewCollection', 'Import Into a New Collection',
                          menu, True, core.getOption('importIntoANewCollection'))

            menu.addSection('Other Options')
            with wrap.Menu('Other Options', menu) as otherOptionsMenu:
                otherOptionsMenu.addSection('Utility Commands')
                convertToNewLayerSystem = wrap.MenuItem('convertToNewLayerSystem', 'Convert to New Layer System', otherOptionsMenu)
                convertToNewLayerSystem.triggered.connect(utils.convertToNewLayerSystem)
                updateLayers = wrap.MenuItem('updateLayers', 'Update Layers', otherOptionsMenu)
                updateLayers.triggered.connect(undo(core.deleteUnusedLayers))  # TODO: Check if undo breaks anything
                resetToDefaults = wrap.MenuItem('resetToDefaults', 'Reset to Defaults', otherOptionsMenu)
                resetToDefaults.triggered.connect(utils.resetUI)

                otherOptionsMenu.addSection('Fixes')
                maya2020UVFix = wrap.MenuItem('maya2020UVFix', 'Fix Maya 2020-2022 UV Bug', otherOptionsMenu)
                maya2020UVFix.triggered.connect(undo(utils.fixMaya2020UVs))
                fixBrokenGraphs = wrap.MenuItem('mayaFixBrokenGraphs', 'Fix Broken Graphs', otherOptionsMenu)
                fixBrokenGraphs.triggered.connect(undo(utils.fixBrokenGraphs))
                convertBezierToNurbs = wrap.MenuItem('convertBezierToNurbs', 'Convert Selected Bezier to NURBS', otherOptionsMenu)
                convertBezierToNurbs.triggered.connect(undo(utils.convertBezierToNurbs))
                maya2020TwistFix = wrap.MenuItem('maya2020TwistAttribute', 'Fix Maya 2020.4 Twist Attribute', otherOptionsMenu)
                maya2020TwistFix.triggered.connect(undo(utils.fixMaya2020Twist))
                maya2020UnbindFix = wrap.MenuItem('maya2020UnbindFix', 'Fix Maya 2020.4 Unbind Function', otherOptionsMenu)
                maya2020UnbindFix.triggered.connect(undo(utils.fixMaya2020Unbind))
                deleteAllAnimationKeys = wrap.MenuItem('deleteAllAnimationKeys', 'Delete All Animation Keys', otherOptionsMenu)
                deleteAllAnimationKeys.triggered.connect(undo(utils.deleteKeysOnAllObjects))

        # Help Menu
        with wrap.Menu('Help', menuBar) as menu:
            openLogFile = wrap.MenuItem('openLogFile', 'Open Log File', menu)
            openLogFile.triggered.connect(utils.logger.openLogFile)
            openOnlineDocumentation = wrap.MenuItem('openOnlineDocumentation', 'Open Online Documentation', menu)
            openOnlineDocumentation.triggered.connect(utils.openDocs)
            usefulLinks = wrap.MenuItem('usefulLinks', 'Useful Links and Contacts', menu)
            usefulLinks.triggered.connect(ui.about.socialWindow)

        # About Menu
        with wrap.Menu('About', menuBar) as menu:
            aboutAction = wrap.MenuItem('gsAbout', 'About', menu)
            aboutAction.triggered.connect(ui.about.aboutWindow)
            menu.addSeparator()
            menu.addAction('Made by George Sladkovsky (%s)' % YEAR).setEnabled(False)

        # MAIN UI

        layout.addWidget(wrap.separator())

        # Extrude Warp Switch
        with wrap.Row(layout) as row:
            # Switch Group
            extrudeWarpSwitchGroup = QtWidgets.QButtonGroup(layout)
            WIDGETS['gsExtrudeWarpSwitchGroup'] = extrudeWarpSwitchGroup
            extrudeWarpSwitchGroup.buttonToggled.connect(self.extrudeWarpToggle)
            extrudeWarpSwitchGroup.buttonClicked.connect(core.saveOptions)

            warpSwitch = wrap.Button(row.layout(), 'warpSwitch')
            warpSwitch.setLabel('Warp', lineHeight=100)
            warpSwitch.setButtonStyle('small')
            warpSwitch.setCheckable(True)

            extrudeSwitch = wrap.Button(row.layout(), 'extrudeSwitch')
            extrudeSwitch.setLabel('Extrude', lineHeight=100)
            extrudeSwitch.setButtonStyle('small')
            extrudeSwitch.setCheckable(True)

            extrudeWarpSwitchGroup.addButton(warpSwitch, 0)
            extrudeWarpSwitchGroup.addButton(extrudeSwitch, 1)

        # New Card and New Tube
        with wrap.Row(layout) as row:
            newCard = wrap.Button(row.layout(), 'newCard')
            newCard.setLabel('New Card')
            newCard.clicked.connect(pa(undo(core.create.new), 0))

            newTube = wrap.Button(row.layout(), 'newTube')
            newTube.setLabel('New Tube')
            newTube.clicked.connect(pa(undo(core.create.new), 1))

        # Convert Curve to Card and Convert Curve to Tube
        with wrap.Row(layout) as row:
            curveCard = wrap.Button(row.layout(), 'curveCard')
            curveCard.setLabel('Curve Card')
            curveCard.clicked.connect(pa(undo(core.create.multiple), 0))

            curveTube = wrap.Button(row.layout(), 'curveTube')
            curveTube.setLabel('Curve Tube')
            curveTube.clicked.connect(pa(undo(core.create.multiple), 1))

        # Bind and Unbind
        with wrap.Row(layout) as row:
            bind = wrap.Button(row.layout(), 'gsBind')
            bind.setLabel('Bind')
            bind.setIcon('mod-top')
            bind.clicked.connect(undo(core.create.bind))

            unbind = wrap.Button(row.layout(), 'gsUnbind')
            unbind.setLabel('Unbind')
            unbind.clicked.connect(undo(core.create.unbind))

        layout.addWidget(wrap.separator())

        # Add Curve and Add Tube
        with wrap.Row(layout) as row:
            addCards = wrap.Button(row.layout(), 'addCards')
            addCards.setLabel('Add Card')
            addCards.setIcon('mod-top')
            addCards.clicked.connect(pa(undo(core.create.populate), 0))

            addTubes = wrap.Button(row.layout(), 'addTubes')
            addTubes.setLabel('Add Tube')
            addTubes.setIcon('mod-top')
            addTubes.clicked.connect(pa(undo(core.create.populate), 1))

        # Fill and Multiply
        with wrap.Row(layout) as row:
            fill = wrap.Button(row.layout(), 'gsFill')
            fill.setLabel('Fill')
            fill.setIcon('mod-top')
            fill.clicked.connect(pa(undo(core.create.fill)))

            subdivide = wrap.Button(row.layout(), 'gsSubdivide')
            subdivide.setLabel('Subdivide')
            subdivide.setIcon('mod-top')
            subdivide.clicked.connect(pa(undo(core.subdivideCurve)))

        # Add Slider
        with wrap.Row(layout) as row:
            m_addCardsSlider = mc.intSliderGrp('gsCurvesSlider', l='Add', f=1, adj=3,
                                               cw=[(1, 20), (2, 25), (3, 1)],
                                               min=1, max=10, v=3)
            addCardsSlider = wrap.mayaSlider(m_addCardsSlider, layout=row.layout())
            WIDGETS['gsCurvesSlider'] = addCardsSlider
            addCardsSlider.setContentsMargins(0, 0, 0, 0)
            addCardsSlider.children()[2].setFocusPolicy(QtCore.Qt.NoFocus)

        layout.addWidget(wrap.separator())

        # Edge to Curve
        with wrap.Row(layout) as row:
            edgeToCurve = wrap.Button(row.layout(), 'gsEdgeToCurve')
            edgeToCurve.setLabel('Edge To Curve')
            edgeToCurve.clicked.connect(pa(undo(core.edgeToCurve)))

            cardToCurve = wrap.Button(row.layout(), 'gsCardToCurve')
            cardToCurve.setLabel('Card To Curve')
            cardToCurve.clicked.connect(ui.cardToCurveWindow.openUI)

        layout.addWidget(wrap.separator())

        # Layer Collections Menu
        with wrap.Row(layout, objName='LayerCollectionsLayout', spacing=1) as layerCollectionsLayout:
            layerComboBox = wrap.LayerCollectionWidget('layerCollectionsComboBox')
            layerComboBox.setStyleSheet(style.smallComboBox)

            layerComboBox.currentIndexChanged.connect(lambda *_: deferred(core.updateMainUI)())
            layerComboBox.setSizeAdjustPolicy(layerComboBox.AdjustToMinimumContentsLength)
            layerComboBox.setDuplicatesEnabled(False)
            layerComboBox.setMinimumWidth(0)
            layerComboBox.setFixedHeight(style.scale(16))

            mc.popupMenu(mm=1, p=layerComboBox.objectName())
            mc.menuItem(rp='N', l='Clear', c=lambda *_: undo(core.layerCollections.clear)())
            mc.menuItem(rp='E', l='Copy', c=lambda *_: noUndo(core.layerCollections.copy)())
            mc.menuItem(rp='NE', l='Move Up', c=lambda *_: noUndo(core.layerCollections.moveUp)())
            mc.menuItem(rp='NW', l='Merge Up', c=lambda *_: noUndo(core.layerCollections.mergeUp)())
            mc.menuItem(rp='W', l='Paste', c=lambda *_: undo(core.layerCollections.paste)())
            mc.menuItem(rp='SW', l='Merge Down', c=lambda *_: noUndo(core.layerCollections.mergeDown)())
            mc.menuItem(rp='SE', l='Move Down', c=lambda *_: noUndo(core.layerCollections.moveDown)())
            mc.menuItem(rp='S', l='Rename', c=lambda *_: noUndo(core.layerCollections.rename)())

            with wrap.Row(layerCollectionsLayout.layout(), margins=style.scale([1, 0, 0, 0])) as plusMinusButtonsLayout:
                layerComboPlus = wrap.Button(objName="layerCollectionsPlus", layout=plusMinusButtonsLayout.layout())
                layerComboPlus.setFixedHeight(style.scale(16))
                layerComboPlus.setLabel("+", lineHeight=100)
                layerComboPlus.setMinimumWidth(1)
                layerComboPlus.setButtonStyle("small-filled")
                layerComboPlus.clicked.connect(core.layerCollections.createLayerCollection)

                layerComboMinus = wrap.Button(objName="layerCollectionsMinus", layout=plusMinusButtonsLayout.layout())
                layerComboMinus.setEnabled(False)
                layerComboMinus.setFixedHeight(style.scale(16))
                layerComboMinus.setMinimumWidth(1)
                layerComboMinus.setLabel("-", lineHeight=100)
                layerComboMinus.setButtonStyle("small-filled")
                layerComboMinus.clicked.connect(undo(core.layerCollections.deleteLayerCollection))

            layerCollectionsLayout.layout().addWidget(layerComboBox, 3)
            layerCollectionsLayout.layout().addWidget(plusMinusButtonsLayout, 1)

            layerComboBox.insertItem(0, "Main")

        # Layer Filters
        with wrap.Row(layout) as row:
            allFilter = wrap.Button(row.layout(), 'gsAllFilter')
            allFilter.setButtonStyle('small-filled')
            allFilter.setLabel('All', lineHeight=100)
            allFilter.setIcon('mod-top')
            allFilter.clicked.connect(pa(undo(core.layersFilterToggle), True, True))

            curveFilter = wrap.Button(row.layout(), 'gsCurveFilter')
            curveFilter.setButtonStyle('small-filled')
            curveFilter.setLabel('Curve', lineHeight=100)
            curveFilter.clicked.connect(pa(undo(core.layersFilterToggle), True, False, ignore=["Shift+Ctrl"]))

            mc.popupMenu(mm=1, p=curveFilter.objectName())
            mc.menuItem(rp='N', l='Toggle Always on Top', c=lambda *_: undo(core.alwaysOnTopToggle)())
            mc.menuItem(rp='S', l='Auto-Hide Curves on Inactive Collections',
                        cb=mc.optionVar(q='GSCT_AutoHideCurvesOnInactiveCollections'),
                        c=lambda cb: undo(core.collectionVisibilityToggle)(cb))

            geoFilter = wrap.Button(row.layout(), 'gsGeoFilter')
            geoFilter.setButtonStyle('small-filled')
            geoFilter.setLabel('Geo', lineHeight=100)
            geoFilter.clicked.connect(pa(undo(core.layersFilterToggle), False, True, ignore=["Shift+Ctrl"]))

            colorMode = wrap.Button(row.layout(), 'colorMode')
            colorMode.setButtonStyle('small-filled')
            colorMode.setCheckable(True)
            colorMode.setChecked(False)
            colorMode.setLabel('Color', lineHeight=100)
            colorMode.clicked.connect(pa(undo(core.toggleColor.toggleColorVis)))

            mc.popupMenu(mm=1, p=colorMode.objectName())
            mc.menuItem(rp='N', l='Randomize Colors', c=lambda *_: undo(core.toggleColor.randomizeColors)())
            mc.menuItem(rp='E', l='Reset Curve Colors', c=lambda *_: core.toggleColor.resetCurveColors())
            mc.menuItem(rp='W', l='Apply Curve Colors', c=lambda *_: core.toggleColor.syncCurveColors(True))
            mc.menuItem(rp='S', l='Custom Colors Window', c=ui.customLayerColors.window)

        # Layers
        with wrap.Layout(layout, objName='LayerLayout') as layerLayout:
            layerButtonGrp = QtWidgets.QButtonGroup(layerLayout.layout())
            layerButtonGrp.setObjectName(wrap.getUniqueName('LayerGroup'))
            layerButtonGrp.setExclusive(True)
            WIDGETS['LayerGroup'] = layerButtonGrp

            # First Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow0', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i, row.layout(), i))

            # Second Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow1', spacing=0) as row:
                letter = ord('A')
                letters = [chr(i) for i in range(letter, letter + 10)]
                if WIDGETS['layerNumbersOnly'].isChecked():
                    letters = [i for i in range(10, 20)]
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 10, row.layout(), letters[i]))

            # Third Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow2', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 20, row.layout(), i + 20))
            WIDGETS['layerRow2'].setHidden(True)

            # Fourth Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow3', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 30, row.layout(), i + 30))
            WIDGETS['layerRow3'].setHidden(True)

            # Fifth Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow4', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 40, row.layout(), i + 40))
            WIDGETS['layerRow4'].setHidden(True)

            # Sixth Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow5', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 50, row.layout(), i + 50))
            WIDGETS['layerRow5'].setHidden(True)

            # Seventh Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow6', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 60, row.layout(), i + 60))
            WIDGETS['layerRow6'].setHidden(True)

            # Eighth Layer Row
            with wrap.Row(layerLayout.layout(), 'layerRow7', spacing=0) as row:
                for i in range(10):
                    layerButtonGrp.addButton(self.selectionSets(i + 70, row.layout(), i + 70))
            WIDGETS['layerRow7'].setHidden(True)

            WIDGETS['curveGrp0'].setChecked(True)

        # Extract Selected and Extract All
        with wrap.Row(layout) as row:
            extractSelected = wrap.Button(row.layout(), 'gsExtractSelected')
            extractSelected.setLabel('Extract<br>Selected')
            extractSelected.setIcon('mod-bottom')
            extractSelected.clicked.connect(pa(undo(core.extractSelectedCurves)))

            extractAll = wrap.Button(row.layout(), 'gsExtractAll')
            extractAll.setLabel('Extract<br>All')
            extractAll.setIcon('mod-bottom')
            extractAll.clicked.connect(undo(core.extractAllCurves))

        layout.addWidget(wrap.separator())

        # Select Curve, Geo and Group
        with wrap.Row(layout) as row:
            selectCurve = wrap.Button(row.layout(), 'gsSelectCurve')
            selectCurve.setLabel('Select<br>Curve')
            selectCurve.clicked.connect(pa(undo(core.selectPart), 1))

            selectGeo = wrap.Button(row.layout(), 'gsSelectGeo')
            selectGeo.setLabel('Select<br>Geo')
            selectGeo.clicked.connect(pa(undo(core.selectPart), 2))

            selectGroup = wrap.Button(row.layout(), 'gsSelectGroup')
            selectGroup.setLabel('Select<br>Group')
            selectGroup.clicked.connect(pa(undo(core.selectPart), 0))

        # Group Curves Button
        with wrap.Row(layout) as row:
            groupCurves = wrap.Button(row.layout(), 'gsGroupCurves')
            groupCurves.setLabel('Group<br>Curves')
            groupCurves.clicked.connect(undo(core.groupCurves))

            regroupByLayer = wrap.Button(row.layout(), 'gsRegroupByLayer')
            regroupByLayer.setLabel('Regroup<br>by Layer')
            regroupByLayer.clicked.connect(undo(core.regroupByLayer))

        # Group Name Input Field
        groupName = wrap.LineEdit('gsGroupNameTextField', layout)
        groupName.setAlignment(QtCore.Qt.AlignCenter)
        groupName.setAutoFormat(True)
        groupName.setClearButtonEnabled(True)
        groupName.setPlaceholderText("Group Name")

        # Custom Layer Names Window
        customLayerNamesColors = wrap.Button(layout, 'gsCustomLayerNamesAndColors')
        customLayerNamesColors.setButtonStyle('small-filled')
        customLayerNamesColors.setLabel('Layer Names & Colors')
        customLayerNamesColors.clicked.connect(ui.customLayerColors.window)

        layout.addWidget(wrap.separator())

        # Select CVs Label
        layout.addWidget(wrap.wrapControl(mc.text(l='Select CVs')))

        # Select CVs Slider
        sliderWidget = wrap.wrapControl(
            mc.floatSliderGrp(
                'gsSelectCVSlider',
                w=1, min=0, max=1, step=0.05,
                dc=core.sliders.selectCVSlider,
                cc=core.sliders.release
            )
        )
        WIDGETS['gsSelectCVSlider'] = sliderWidget
        layout.addWidget(sliderWidget)

        # Select Curve, Geo and Group
        with wrap.Row(layout) as row:
            transferAttributes = wrap.Button(row.layout(), 'gsTransferAttributes')
            transferAttributes.setLabel('Transfer<br>Attr.')
            transferAttributes.setIcon('mod-bottom')
            transferAttributes.clicked.connect(undo(core.attributes.transferAttr))
            mc.popupMenu(mm=1, p=transferAttributes.objectName())
            mc.menuItem('gsCopyAttributes', rp='N', l='Copy Attrs', aob=1, c=lambda _: core.attributes.copyAttributes())
            mc.menuItem(ob=1, c=lambda _: ui.attributesFilter.openUI())
            mc.menuItem('gsPasteAttributes', rp='S', l='Paste Attrs', aob=1, c=lambda _: core.attributes.pasteAttributes())
            mc.menuItem(ob=1, c=lambda _: ui.attributesFilter.openUI())

            transferUVs = wrap.Button(row.layout(), 'gsTransferUVs')
            transferUVs.setLabel('Transfer<br>UVs')
            transferUVs.setIcon('mod-bottom')
            transferUVs.clicked.connect(undo(core.attributes.transferUV))
            mc.popupMenu(mm=1, p=transferUVs.objectName())
            mc.menuItem('gsCopyUVs', aob=1, rp='N', l='Copy UVs', c=lambda _: core.attributes.copyUVs())
            mc.menuItem(ob=1, c=lambda _: ui.attributesFilter.openUI())
            mc.menuItem('gsPasteUVs', aob=1, rp='S', l='Paste UVs', c=lambda _: core.attributes.pasteUVs())
            mc.menuItem(ob=1, c=lambda _: ui.attributesFilter.openUI())

            resetPivot = wrap.Button(row.layout(), 'gsResetPivot')
            resetPivot.setLabel('Reset<br>Pivot')
            resetPivot.clicked.connect(undo(core.resetCurvePivotPoint))
            resetPivot.setIcon('mod-bottom')
            mc.popupMenu(mm=1, p=resetPivot.objectName())
            mc.menuItem('gsResetPivotToRoot', rp='N', l='Reset to Root', c=lambda _: core.resetCurvePivotPoint())
            mc.menuItem('gsResetPivotToTip', rp='S', l='Reset to Tip', c=lambda _: core.resetCurvePivotPoint(2))

        layout.addWidget(wrap.separator())

        # Rebuild Curve
        def rebuildSliderRelease(_):
            core.sliders.rebuildSliderRelease()
            core.sliders.release()

        def rebuildButtonClicked():
            core.sliders.rebuildSliderDrag()
            rebuildSliderRelease(None)

        with wrap.Row(layout, margins=style.scale([1.5, 0, 1.5, 0])) as rebuildResetRow:
            rebuildButton = wrap.Button(objName='gsRebuildWithCurrentValue')
            rebuildButton.setButtonStyle('small-filled')
            rebuildButton.setLabel("R", lineHeight=100)
            rebuildButton.setMinimumWidth(1)
            rebuildButton.setMaximumSize(*style.scale([16, 16]))
            rebuildButton.clicked.connect(rebuildButtonClicked)

            resetButton = wrap.Button(objName='gsResetRebuildSliderRange')
            resetButton.setButtonStyle('small-filled')
            resetButton.setIcon('reset')
            resetButton.setMinimumWidth(1)
            resetButton.setMaximumSize(*style.scale([16, 16]))
            resetButton.clicked.connect(lambda: mc.intSliderGrp('gsRebuildSlider', e=1, min=1, max=50))

            rebuildResetRow.layout().addWidget(rebuildButton, 1)
            rebuildResetRow.layout().addWidget(wrap.wrapControl(mc.text(l='Rebuild Curve')), 3)
            rebuildResetRow.layout().addWidget(resetButton, 1)

        rebuildCurveSlider = wrap.wrapControl(mc.intSliderGrp(
            'gsRebuildSlider', f=1, cw=[(1, 32), (2, 28)], min=1, max=50, fmx=999, v=1,
            dc=core.sliders.rebuildSliderDrag,
            cc=rebuildSliderRelease))
        WIDGETS['gsRebuildSlider'] = rebuildCurveSlider
        layout.addWidget(rebuildCurveSlider)

        # Duplicate and Randomize
        with wrap.Row(layout) as row:
            duplicateCurve = wrap.Button(row.layout(), 'gsDuplicateCurve')
            duplicateCurve.setLabel('Duplicate')
            duplicateCurve.clicked.connect(undo(core.duplicateCurve))

            randomizeCurve = wrap.Button(row.layout(), 'gsRandomizeCurve')
            randomizeCurve.setLabel('Randomize')
            randomizeCurve.clicked.connect(ui.randomizeCurveWindow)

        # Extend and Reduce
        with wrap.Row(layout) as row:
            extendCurve = wrap.Button(row.layout(), 'gsExtendCurve')
            extendCurve.setLabel('Extend')
            extendCurve.clicked.connect(undo(core.extendCurve))

            reduceCurve = wrap.Button(row.layout(), 'gsReduceCurve')
            reduceCurve.setLabel('Reduce')
            reduceCurve.clicked.connect(undo(core.reduceCurve))

        # Smooth
        with wrap.Row(layout) as row:
            smooth = wrap.Button(row.layout(), 'gsSmooth')
            smooth.setLabel('Smooth')
            smooth.clicked.connect(undo(core.smoothCurve))
            smooth.setIcon('marking-top')
            mc.popupMenu(mm=1, p=smooth.objectName())
            mc.radioMenuItemCollection()
            mc.menuItem('gsSmoothMult1', rp='N', rb=1, l='x1')
            mc.menuItem('gsSmoothMult3', rp='E', rb=0, l='x3')
            mc.menuItem('gsSmoothMult5', rp='S', rb=0, l='x5')
            mc.menuItem('gsSmoothMult10', rp='W', rb=0, l='x10')

        # Smooth Slider
        factorSlider = wrap.wrapControl(mc.floatSliderGrp(
            'gsFactorSlider', l='Factor', adj=3, w=1, cw=[(1, 32), (2, 28)], min=1, max=100))
        WIDGETS['gsFactorSlider'] = factorSlider
        layout.addWidget(factorSlider)

        layout.addWidget(wrap.separator())

        # Mirroring
        with wrap.Frame(layout, objName='MirrorFrame', label='Mirroring', margins=[1, 1, 1, 1]) as frame:
            with wrap.Row(frame.getFrameLayout()) as row:
                mirrorX = wrap.Button(row.layout(), 'mirrorX')
                mirrorX.setLabel('X')
                mirrorX.setFontSize(16)
                mirrorX.clicked.connect(pa(undo(core.mirrorHair), 0))
                mirrorY = wrap.Button(row.layout(), 'mirrorY')
                mirrorY.setLabel('Y')
                mirrorY.setFontSize(16)
                mirrorY.clicked.connect(pa(undo(core.mirrorHair), 1))
                mirrorZ = wrap.Button(row.layout(), 'mirrorZ')
                mirrorZ.setLabel('Z')
                mirrorZ.setFontSize(16)
                mirrorZ.clicked.connect(pa(undo(core.mirrorHair), 2))

            with wrap.Row(frame.getFrameLayout()) as row:
                mirrorFlipGrp = QtWidgets.QButtonGroup(row.layout())
                mirror = wrap.Button(row.layout(), 'mirrorRadio')
                mirror.setLabel('Mirror')
                mirror.setButtonStyle('small')
                mirror.setCheckable(True)
                mirror.setChecked(True)
                flip = wrap.Button(row.layout(), 'flipRadio')
                flip.setLabel('Flip')
                flip.setButtonStyle('small')
                flip.setCheckable(True)

                mirrorFlipGrp.addButton(mirror)
                mirrorFlipGrp.addButton(flip)

        layout.addWidget(wrap.separator())

        # Control Curve and Apply
        with wrap.Row(layout) as row:
            controlCurve = wrap.Button(row.layout(), 'gsControlCurve')
            controlCurve.setLabel('Control Curve')
            controlCurve.clicked.connect(undo(core.controlCurveCreate))

            applyControlCurve = wrap.Button(row.layout(), 'gsApplyControlCurve')
            applyControlCurve.setLabel('Apply')
            applyControlCurve.setFixedWidth(style.scale(48))
            applyControlCurve.clicked.connect(undo(core.controlCurveApply))

        layout.addWidget(wrap.separator())

        # Curve Control Window
        with wrap.Row(layout) as row:
            curveControlWindow = wrap.Button(row.layout(), 'gsCurveControlWindow')
            curveControlWindow.setLabel('Curve Control Window')
            curveControlWindow.pressed.connect(ui.curveControlWorkspace)

        layout.addWidget(wrap.separator())

        # UV Editor Window
        with wrap.Row(layout) as row:
            uvEditor = wrap.Button(row.layout(), 'gsUVEditorMain')
            uvEditor.setLabel('UV Editor Window')
            uvEditor.pressed.connect(ui.uvEditorWorkspace)

        layout.addWidget(wrap.separator())

        # Version
        layout.addWidget(wrap.wrapControl(mc.text(l=core.VERSION)))

        # Toggling the correct switch
        warpSwitch.setChecked(core.getOption('warpSwitch'))
        extrudeSwitch.setChecked(not core.getOption('warpSwitch'))

        # Toggling layer collections widget
        core.layerCollections.toggleLayerCollectionsWidget()

        # Setting the custom tooltips
        tooltips.toggleCustomTooltipsMain(core.getOption('enableTooltips'))

    def selectionSets(self, i, layout, label):  # Creates layer button
        def toggleGeometryEdit(*_):
            core.curveGeometryEditToggle(i)
            core.updateMainUI()

        def toggleCurveVisibility(*_):
            core.toggleObjVisibility(i, 0)
            core.updateMainUI()

        def toggleGeoVisibility(*_):
            core.toggleObjVisibility(i, 1)
            core.updateMainUI()

        def toggleLayerVisibility(*_):
            core.toggleLayerVisibility(i)
            core.updateMainUI()
        selSet = wrap.Layer(layout=layout, objName='curveGrp%s' % i)
        selSet.setStyleSheet(style.layer())
        selSet.setLabel(str(label))
        mc.popupMenu(mm=1, p=selSet.objectName())
        mc.menuItem(rp='N', l='Add Selection to Layer', c=lambda _: core.curveAddToLayer(i))
        mc.menuItem(rp='NW', l='Extract Geometry', c=lambda _: core.extractCurveGeo(i))
        mc.menuItem(rp='NE', l='Toggle Geometry Edit', c=toggleGeometryEdit)
        mc.menuItem(rp='W', l='Select Curves', c=lambda _: core.curveLayerSelectObj(i, 0))
        mc.menuItem(rp='E', l='Select Geometry', c=lambda _: core.curveLayerSelectObj(i, 1))
        mc.menuItem(rp='SW', l='Toggle Curve Visibility', c=toggleCurveVisibility)
        mc.menuItem(rp='SE', l='Toggle Geo Visibility', c=toggleGeoVisibility)
        mc.menuItem(rp='S', l='Toggle Layer Visibility', c=toggleLayerVisibility)
        selSet.clicked.connect(pa(undo(core.layerClicked), i))
        return selSet

    def extrudeWarpToggle(self):
        buttons = ['newCard', 'newTube', 'curveCard', 'curveTube', 'addCards', 'addTubes']
        buttonStyle = style.buttonNormal
        if WIDGETS['extrudeSwitch'].isChecked():
            buttonStyle = style.buttonNormalBlueBorder
        for button in buttons:
            WIDGETS[button].setStyleSheet(buttonStyle)

    def updateLayerList(self):
        if 'gsLayerSelector' in WIDGETS:
            WIDGETS['gsLayerSelector'].updateLayerList()
            core.curveControlUI.updateUI()

    def toggleTooltips(self):
        for widget in WIDGETS:
            if hasattr(WIDGETS[widget], "enableTooltip") and callable(getattr(WIDGETS[widget], "enableTooltip")):
                WIDGETS[widget].enableTooltip(core.getOption('enableTooltips'))
        tooltips.toggleCustomTooltipsMain(core.getOption('enableTooltips'))
        tooltips.toggleCustomTooltipsCurveControl(core.getOption('enableTooltips'))
