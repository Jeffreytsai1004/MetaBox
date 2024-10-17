#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import colorsys
import math
import os
import random
import re
from imp import reload

import maya.api.OpenMaya as om
import maya.cmds as mc
import maya.mel as mel

from .constants import *
from .utils import gs_math as mt
from .utils import style, utils, wrap
from .utils.wrap import WIDGETS

reload(utils)
reload(mt)
reload(wrap)
reload(style)

MESSAGE = utils.logger
LOGGER = utils.logger.logger


### Core Classes ###

class Attributes:

    def __init__(self, name):
        self.name = name
        self.copyAttributesSourceCurve = None
        self.copyUVsSourceCurve = None

    attrList = {
        'lengthDivisions',
        'dynamicDivisions',
        'widthDivisions',
        'Orientation',
        'Twist',
        'invTwist',
        'Width',
        'WidthX',
        'WidthZ',
        'LengthLock',
        'Length',
        'Taper',
        'Profile',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'reverseNormals',
        'surfaceNormals',
        'flipUV',
        'moveU',
        'moveV',
        'rotateUV',
        'rotateRootUV',
        'rotateTipUV',
        'scaleU',
        'scaleV',
        'solidify',
        'solidifyThickness',
        'solidifyDivisions',
        'solidifyScaleX',
        'solidifyScaleY',
        'solidifyOffset',
        'solidifyNormals',
        'Axis',
        'AxisFlip',
        'Offset',
        'lineWidth',
        'samplingAccuracy',
        'Magnitude',
        'profileSmoothing',
        'profileMagnitude',
    }

    uvAttr = {
        'moveU',
        'moveV',
        'rotateUV',
        'rotateRootUV',
        'rotateTipUV',
        'scaleU',
        'scaleV',
        'flipUV',
    }

    checkBoxes = {
        'autoRefine',
        'dynamicDivisions',
        'LengthLock',
        'reverseNormals',
        'solidify',
        'Axis',
        'AxisFlip',
    }

    multiInst = {
        'twistCurve',
        'scaleCurve'
    }

    graphAttributes = {
        'twistCurve',
        'scaleCurve',
        'profileCurve',
    }

    def getAttr(self, inputCurve, excludeUV=False, excludeCheckboxes=False, manualExclude=False):
        getAttr = dict()
        for attr in self.attrList:
            if excludeUV and attr in self.uvAttr:
                continue
            if excludeCheckboxes and attr in self.checkBoxes:
                continue
            if manualExclude and attr in manualExclude:
                continue
            try:
                getAttr[attr] = mc.getAttr(inputCurve + '.' + attr)
            except Exception as e:
                # LOGGER.exception(e)
                pass
        return getAttr

    def getCheckboxes(self, inputCurve):
        checkboxes = dict()
        for attr in self.checkBoxes:
            try:
                checkboxes[attr] = mc.getAttr(inputCurve + '.' + attr)
            except BaseException:
                pass
        return checkboxes

    def getUVs(self, inputCurve):
        getUVs = dict()
        for attr in self.uvAttr:
            try:
                getUVs[attr] = mc.getAttr(inputCurve + '.' + attr)
            except BaseException:
                pass
        return getUVs

    def getMultiInst(self, inputCurve):
        if mc.attributeQuery('Length', n=inputCurve, ex=1):
            try:
                node = mc.ls(mc.listHistory(selectPart(2, True, inputCurve), ac=1, il=0), typ='curveWarp')[0]
            except BaseException:
                return None
            returnList = list()
            for attr in self.multiInst:
                cList = list()
                cIndex = mc.getAttr(node + '.' + attr, mi=1)
                for i in cIndex:
                    cList.append(mc.getAttr(node + '.%s[%s]' % (attr, i))[0])
                cList.append(attr)
                returnList.append(cList)
            return returnList

    @staticmethod
    def setMultiInst(targetCurve, inputList):
        if mc.attributeQuery('Length', n=targetCurve, ex=1):
            geo = selectPart(2, True, targetCurve)
            targetNode = mc.ls(mc.listHistory(geo, ac=1, il=0), typ='curveWarp')[0]
            attribute = inputList[-1]

            attributes.resetMultiInst(targetNode, attribute)

            for i in range(len(inputList) - 1):
                mc.setAttr(targetNode + '.%s[%s]' % (attribute, i), inputList[i][0], inputList[i][1])

    @staticmethod
    def resetMultiInst(node, attr):
        index = mc.getAttr(node + '.%s' % attr, mi=1)
        for i in index:
            if i == 0:
                continue
            mc.removeMultiInstance(node + '.%s[%s]' % (attr, i))
        for i in range(4):
            mc.setAttr(node + '.%s[%s]' % (attr, i), i / 3.0, 0.5, typ='double2')

    @staticmethod
    def blendMultInst(source, target, ratio):  # TODO: Add better support for different number of points
        returnList = list()
        sourceL = len(source)
        targetL = len(target)
        if sourceL == targetL:
            for i in range(sourceL - 1):
                returnList.append((source[i][0], mt.lerp(ratio, source[i][1], target[i][1])))
        elif sourceL < targetL:
            returnList.append((source[0][0], mt.lerp(ratio, source[0][1], target[0][1])))
            for i in range(1, sourceL - 2):
                returnList.append((source[i][0], mt.lerp(ratio, source[i][1], target[i][1])))
            returnList.append((source[-2][0], mt.lerp(ratio, source[-2][1], target[-2][1])))
        else:
            returnList.append((source[0][0], mt.lerp(ratio, source[0][1], target[0][1])))
            for i in range(1, targetL - 2):
                returnList.append((source[i][0], mt.lerp(ratio, source[i][1], target[i][1])))
            returnList.append((source[-2][0], mt.lerp(ratio, source[-2][1], target[-2][1])))
        returnList.append(source[-1])
        return returnList

    @staticmethod
    def setAttr(inputCurve, inputDict, exclude=None):
        for attr in inputDict:
            if exclude and attr in exclude:
                continue
            try:
                mc.setAttr(inputCurve + "." + attr, inputDict[attr])
            except BaseException:
                pass

    def copyAttributes(self):
        """Select the last curve in selection list for attribute copy command"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        self.copyAttributesSourceCurve = None
        if not sel:
            MESSAGE.warningInView('Select at least one Curve')
            return
        self.copyAttributesSourceCurve = sel[-1]
        mc.headsUpMessage('[Copied]', o=self.copyAttributesSourceCurve, time=1, vp=1)

    def pasteAttributes(self):
        """Copy and paste the attributes from the source curve (copyAttributes function) to the target selection list"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel:
            MESSAGE.warningInView('Select at least one Curve.')
            return
        if not self.copyAttributesSourceCurve:
            MESSAGE.warningInView('No copied attributes available.')
            return
        if not mc.objExists(self.copyAttributesSourceCurve):
            MESSAGE.warningInView('Original curve was not found, copying cancelled.')
            self.copyAttributesSourceCurve = None
            return
        sourceAttr = self.getAttr(self.copyAttributesSourceCurve, excludeUV=True)
        filterAttrs = dict(eval(mc.optionVar(q='GSCT_AttributesFilter')))
        filteredSourceAttrs = sourceAttr.copy()
        for attr in filterAttrs:
            if filterAttrs and attr in filterAttrs and not filterAttrs[attr]:
                filteredSourceAttrs.pop(attr, None)
        multiInd = None
        if 'Length' in sourceAttr:
            multiInd = self.getMultiInst(self.copyAttributesSourceCurve)
            for attr in multiInd:
                if filterAttrs and attr[-1] in filterAttrs and not filterAttrs[attr[-1]]:
                    continue
                for target in sel:
                    self.setMultiInst(target, attr)
        for target in sel:
            self.setAttr(target, filteredSourceAttrs)
            if filterAttrs and 'profileCurve' in filterAttrs and filterAttrs['profileCurve']:
                transferProfileCurve(self.copyAttributesSourceCurve, target)
        LOGGER.info('Attributes transferred from "%s" to %s target curve(s).' % (self.copyAttributesSourceCurve, len(sel)))
        curveControlUI.updateUI()

    def transferAttr(self, hk=None):  # Transfer settings from curve to curve
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel or len(sel) < 2:
            MESSAGE.warningInView('Select at least two Curves')
            return -1
        # Init Vars
        source = str()
        targets = list()
        # Get modifier
        mod = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
        # Set source and targets
        if mod:
            source = sel[-1]
            targets = sel[0:-1]
        else:
            source = sel[0]
            targets = sel[1:]
        mc.headsUpMessage('[Source]', o=source, time=1, vp=1)
        sourceAttr = self.getAttr(source, 1)
        filterAttrs = dict(eval(mc.optionVar(q='GSCT_AttributesFilter')))
        filteredSourceAttrs = sourceAttr.copy()
        for attr in filterAttrs:
            if filterAttrs and attr in filterAttrs and not filterAttrs[attr]:
                filteredSourceAttrs.pop(attr, None)
        multiInd = None
        if 'Length' in sourceAttr:
            multiInd = self.getMultiInst(source)
            for attr in multiInd:
                if filterAttrs and attr[-1] in filterAttrs and not filterAttrs[attr[-1]]:
                    continue
                for target in targets:
                    self.setMultiInst(target, attr)
        for target in targets:
            self.setAttr(target, filteredSourceAttrs)
            if filterAttrs and 'profileCurve' in filterAttrs and filterAttrs['profileCurve']:
                transferProfileCurve(source, target)
        LOGGER.info('Attributes transferred from "%s" to %s target curve(s).' % (source, len(targets)))
        curveControlUI.updateUI()

    def copyUVs(self):
        """Select the last curve in selection list for UVs copy command"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        self.copyUVsSourceCurve = None
        if not sel:
            MESSAGE.warningInView('Select at least one Curve')
            return
        self.copyUVsSourceCurve = sel[-1]
        mc.headsUpMessage('[Copied]', o=self.copyUVsSourceCurve, time=1, vp=1)

    def pasteUVs(self):
        """Copy and paste the UVs from the source curve (copyUVs function) to the target selection list"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel:
            MESSAGE.warningInView('Select at least one Curve.')
            return
        if not self.copyUVsSourceCurve:
            MESSAGE.warningInView('No copied UVs available.')
            return
        if not mc.objExists(self.copyUVsSourceCurve):
            MESSAGE.warningInView('Original curve was not found, copying cancelled.')
            self.copyUVsSourceCurve = None
            return
        source = self.copyUVsSourceCurve
        targets = sel
        self._transferUVs(source, targets)
        LOGGER.info('UVs transferred from "' + str(source) + '" to ' + str(len(sel)) + ' target curve(s).')
        curveControlUI.updateUI()
        if mc.workspaceControl(UV_EDITOR_NAME, q=1, ex=1):
            from . import ui
            ui.uveditor.updateEditor()

    def transferUV(self, hk=None):  # Transfer Curve UVs
        # type: (int|bool|None) -> None
        """Transfer UVs from last/first selected curve to all others"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel or len(sel) < 2:
            MESSAGE.warningInView('Select at least two Curves')
            return -1
        source = str()
        targets = list()
        # Get modifier
        mod = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
        # Set source and targets
        if mod:
            source = sel[-1]
            targets = sel[0:-1]
        else:
            source = sel[0]
            targets = sel[1:]
        mc.headsUpMessage('[Source]', o=source, time=1, vp=1)
        self._transferUVs(source, targets)
        LOGGER.info('UVs transferred from "' + str(source) + '" to ' + str(len(targets)) + ' target curve(s).')
        curveControlUI.updateUI()
        if mc.workspaceControl(UV_EDITOR_NAME, q=1, ex=1):
            from . import ui
            ui.uveditor.updateEditor()

    def _transferUVs(self, source, targets):
        # type: (str, list[str]) -> None
        """Transfer UVs from source to target"""
        # Check if source curve is bound curve
        filterAttrs = dict(eval(mc.optionVar(q='GSCT_AttributesFilter')))
        if mc.attributeQuery('gsmessage', n=source, ex=1):
            bindMessage = mc.listConnections(source + '.gsmessage', d=1, s=0)
            if bindMessage:
                source = bindMessage
        # Get source UVs
        sourceUVs = []
        if isinstance(source, list):
            for s in source:
                sourceUVs.append(self.getUVs(s))
        else:
            sourceUVs.append(self.getUVs(source))
        # Filter source UVs
        for uvs in sourceUVs:
            for attr in uvs:
                if filterAttrs and attr in filterAttrs and not filterAttrs[attr]:
                    uvs.pop(attr, None)
        for target in targets:
            # Check if target is a bound curve
            bindMessage = None
            if mc.attributeQuery('gsmessage', n=target, ex=1):
                bindMessage = mc.listConnections(target + '.gsmessage', d=1, s=0)
            if bindMessage:
                target = bindMessage
                if len(target) == len(sourceUVs):
                    for i, t in enumerate(target):
                        self.setAttr(t, sourceUVs[i])
                else:
                    for t in target:
                        self.setAttr(t, sourceUVs[-1])
            else:
                self.setAttr(target, sourceUVs[-1])

    def deleteAttr(self, inputCurve):  # Delete Attributes from Curve
        attrDict = self.attrList
        for attr in attrDict:
            if mc.attributeQuery(attr, n=inputCurve, ex=1):
                mc.deleteAttr(inputCurve + '.' + attr)

    def storeGraphs(self, graph, *_):
        """ Store graphs values on curves """
        graphName = graph.objName
        graphString = WIDGETS[graphName].getGraph()
        selection = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not selection:
            selection = mc.filterExpand(mc.listRelatives(mc.ls(sl=1, o=1), p=1, pa=1), sm=9)
        if not selection:
            return
        for sel in selection:
            if not mc.attributeQuery(graphName, n=sel, ex=1):
                mc.addAttr(sel, ln=graphName, dt='string', k=0)
            mc.setAttr(sel + '.' + graphName, graphString, type='string')

    def propagateGraphs(self, graph):
        """ Copy the graph changes to other selected curves """
        graphName = graph.objName.replace("_large", "")
        selection = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not selection:
            selection = mc.filterExpand(mc.listRelatives(mc.ls(sl=1, o=1), p=1, pa=1), sm=9)
        if not selection:
            return
        sourceAttr = self.getAttr(selection[-1], 1)
        if 'Length' in sourceAttr:
            multiInd = self.getMultiInst(selection[-1])
            for sel in selection:
                for attr in multiInd:
                    if attr[-1] == graphName:
                        self.setMultiInst(sel, attr)


attributes = Attributes("attributes")


class Create:

    def __init__(self, name):
        self.name = name
        self.globalThickness = mc.optionVar(q='GSCT_globalCurveThickness')
        self.sf = 1.0
        self.nurbsTesselate = None
        self.curveWarp = None
        self.polyMoveUV_mid = None
        self.polyMoveUV_tip = None
        self.polyMoveUV_root = None
        self.solidifyNode = None
        self.solidifyChoice = None
        self.extrude = None
        self.lattice = None
        self.twist = None
        self.magnExpr = None
        self.scaleExpr = None
        self.uvExpr = None
        self.polyNormalNode = None
        self.polySoftEdge = None
        self.autoRefineCalculate = None

    def currentLayerInd(self):
        return WIDGETS['LayerGroup'].checkedId() * -1 - 2

    def initialize(self):
        self.__init__(self.name)
        # Check if color mode is enabled
        if utils.getAttr('gsColorShaderStorageNode', 'colorApplied'):
            toggleColor.updateColors()
        self.sf = getScaleFactor()

        # Check if layer is empty
        ind = self.currentLayerInd()
        self.collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
        layer, _, _ = utils.getFormattedLayerNames(self.collectionID, ind)
        if mc.objExists(layer):
            test = mc.editDisplayLayerMembers(layer, q=1, nr=1, fn=1)
            if not test:
                deleteUnusedLayers()

    ### Common Creation Methods ###

    def new(self, mode, hk=None):
        # type: (int, bool|None) -> None
        """Creates a new card or tube of specified type"""
        self.initialize()
        warpRadio = WIDGETS['warpSwitch'].isChecked()
        if warpRadio or hk:
            mode = mode + 2
        pathCurve = mc.curve(d=3,
                             p=[(0, -0.0001, 0), (1.666667 * self.sf, 0, 0), (5 * self.sf, 0, 0), (10 * self.sf, 0, 0),
                                (15 * self.sf, 0, 0), (18.333333 * self.sf, 0, 0), (20 * self.sf, 0, 0)],
                             k=[0, 0, 0, 1, 2, 3, 4, 4, 4], n='pathCurve_inst#')
        mc.rebuildCurve(pathCurve, kr=2)
        finalCurve = []
        if mode == 0:
            finalCurve = self.extrudeCard(pathCurve, False)
        elif mode == 1:
            finalCurve = self.extrudeTube(pathCurve, False)
        elif mode == 2:
            finalCurve = self.warpCard(pathCurve, False)
        elif mode == 3:
            finalCurve = self.warpTube(pathCurve, False)
        else:
            mc.delete(pathCurve)
            LOGGER.error("Wrong mode parameter value")
            raise ValueError("Wrong mode parameter value")
        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()
        mc.select(finalCurve)

    def multiple(self, mode, hk=False, progressBar=True, keepAttrs=False):
        # type: (int, bool, bool, bool) -> None
        """Creates Curves from multiple curves selected"""
        self.initialize()
        selPool = mc.filterExpand(mc.ls(sl=1, l=1, tr=1), sm=9)
        try:
            selPool = utils.convertInstanceToObj(selPool)
        except BaseException:
            pass

        if selPool == -1:
            return 0

        if WIDGETS['warpSwitch'].isChecked() or hk:
            mode = mode + 2

        if mode == 0:
            create = 'extrudeCards'
        elif mode == 1:
            create = 'extrudeTubes'
        elif mode == 2:
            create = 'warpCards'
        elif mode == 3:
            create = 'warpTubes'
        else:
            LOGGER.error("Wrong mode parameter value")
            raise ValueError("Wrong mode parameter value")
        progress = None
        allCurves = list()

        if not selPool:
            MESSAGE.warningInView('Select at least one curve')
            return

        if progressBar:
            progress = utils.ProgressBar('Creating ' + create, len(selPool))

        for pathInst in selPool:
            if progress and progress.tick(1):
                break
            prevAttrs = attributes.getAttr(pathInst)
            graphAttrs = {}
            for attr in attributes.graphAttributes:
                if mc.attributeQuery(attr, n=pathInst, ex=1):
                    graphAttrs[attr] = mc.getAttr(pathInst + '.' + attr)
            if utils.attrExists(pathInst, 'lengthDivisions'):
                if mc.connectionInfo(pathInst + '.lengthDivisions', isSource=1):
                    LOGGER.info('%s is not a compatible curve. Skipped.' % pathInst)
                    continue
                attributes.deleteAttr(pathInst)
            if utils.attrExists(pathInst, 'Axis'):
                if mc.connectionInfo(pathInst + '.Axis', isSource=1):
                    LOGGER.info('%s is not a compatible curve. Skipped.' % pathInst)
                    continue
                attributes.deleteAttr(pathInst)
            pathInst = mc.rename(pathInst, 'pathCurve_inst#')
            returnCurve = list()

            # Bezier curve auto-check
            pathInst = utils.checkIfBezier(pathInst)

            if mode == 0:
                returnCurve = self.extrudeCard(pathInst)
            elif mode == 1:
                returnCurve = self.extrudeTube(pathInst)
            elif mode == 2:
                returnCurve = self.warpCard(pathInst)
            elif mode == 3:
                returnCurve = self.warpTube(pathInst)
            if returnCurve:
                if WIDGETS['keepCurveAttributes'].isChecked() and not keepAttrs:
                    for attr in graphAttrs:
                        values = graphAttrs[attr]
                        if attr == 'profileCurve':
                            updateLattice(values, returnCurve)
                        else:
                            rebuildCurve = mc.listConnections(returnCurve + '.curveSmooth')[0]
                            warp = mc.listConnections(rebuildCurve + '.outputCurve', et=True, t='curveWarp')
                            if warp:
                                graphValues = utils.fromStringToDouble2(values)
                                utils.setDouble2Attr(warp[0], attr, graphValues)
                    attributes.setAttr(returnCurve, prevAttrs)
                allCurves.append(returnCurve)
        if progress:
            progress.end()
        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()
        mc.select(allCurves, r=1)
        return allCurves

    def populate(self, mode, hk=None):  #
        # type: (int, bool) -> None
        """Creates new Curves in between existing curves"""
        self.initialize()
        sel = mc.filterExpand(mc.ls(sl=1, l=1, dag=1, tr=1), sm=9)

        if not sel or len(sel) < 2:
            MESSAGE.warningInView('Select at least two curves')
            return 0

        topGrp = mc.listRelatives(mc.listRelatives(sel[0], p=1, pa=1), p=1, pa=1)

        if WIDGETS['warpSwitch'].isChecked():
            mode = mode + 2

        # Get original shader
        nodes = mc.listHistory(mc.listRelatives(sel[0], c=1, pa=1), f=1)
        shapes = mc.ls(nodes, s=1, l=1)
        shapeFilter = list()
        if len(nodes) > 0:
            for node in nodes:
                shadingEngine = mc.listConnections(node, c=True, d=True, t='shadingEngine')
                if shadingEngine:
                    break
            shapeFilter = mc.ls(shadingEngine, et='shadingEngine')

        loft = mc.loft(sel, c=0, ch=1, d=3, ss=4, rsn=True, ar=1, u=1, rn=0, po=0)

        step = 1.0 / (mc.intSliderGrp('gsCurvesSlider', q=1, value=1) + 1.0)
        cond = len(sel) - 1
        allCurves = list()
        i = 0
        progress = utils.ProgressBar('Adding Cards', cond * 100)
        while i < cond:
            if progress.tick(step * 100):
                break
            roundI = round(i, 1)
            crv0 = int(math.floor(roundI))
            crv = int(math.ceil(roundI))
            mod = math.fmod(roundI, 1)
            if mod != 0:  # Exclude whole numbers

                # Create curve from loft and convert it to curveCard
                pathInst = mc.duplicateCurve((loft[0] + '.v[' + str(i) + ']'), rn=0, ch=0, local=0, n='pathCurve_inst#')
                mc.rebuildCurve(pathInst, kr=2, kcp=1)

                # Get original scale factor for source curve
                interpScaleFactor = scaleFactor0 = scaleFactor1 = getScaleFactor()
                if WIDGETS['populateBlendAttributes'].isChecked():
                    if mc.attributeQuery('scaleFactor', n=sel[crv0], ex=1):
                        scaleFactor0 = mc.getAttr(sel[crv0] + '.scaleFactor')
                    # Get original scale factor for target curve
                    if mc.attributeQuery('scaleFactor', n=sel[crv], ex=1):
                        scaleFactor1 = mc.getAttr(sel[crv] + '.scaleFactor')
                    # Interpolate scale factor
                    interpScaleFactor = mt.lerp(i - crv0, scaleFactor0, scaleFactor1)

                if interpScaleFactor:
                    mc.addAttr(pathInst[0], ln='scaleFactor', at='double', dv=interpScaleFactor)

                newCurve = str()
                if mode == 0:
                    newCurve = self.extrudeCard(pathInst[0])
                elif mode == 1:
                    newCurve = self.extrudeTube(pathInst[0])
                elif mode == 2:
                    newCurve = self.warpCard(pathInst[0])
                elif mode == 3:
                    newCurve = self.warpTube(pathInst[0])

                if WIDGETS['populateBlendAttributes'].isChecked():

                    # Getting all available attributes
                    crv0Attr = attributes.getAttr(sel[crv0])
                    crv0ScaleX = mc.getAttr(sel[crv0] + '.scaleX')

                    sourceMultInd = None
                    if 'Length' in crv0Attr and 'Taper' in crv0Attr and (mode == 2 or mode == 3):
                        sourceMultInd = attributes.getMultiInst(sel[crv0])

                    # Blending
                    mod = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
                    if not mod:
                        crvAttr = attributes.getAttr(sel[crv], 1, 1)
                        crv1ScaleX = mc.getAttr(sel[crv] + '.scaleX')
                        crv0ScaleX = mt.lerp(i - crv0, crv0ScaleX, crv1ScaleX)
                        for attr in crv0Attr:
                            if attr in crvAttr:
                                crv0Attr[attr] = mt.lerp(i - crv0, crv0Attr[attr], crvAttr[attr])
                        if 'Length' in crvAttr and 'Taper' in crvAttr and (mode == 2 or mode == 3):
                            targetMultInd = attributes.getMultiInst(sel[crv])
                            if sourceMultInd:
                                for attr in range(len(sourceMultInd)):
                                    blendMultInst = attributes.blendMultInst(sourceMultInd[attr],
                                                                             targetMultInd[attr],
                                                                             i - crv0)
                                    attributes.setMultiInst(newCurve, blendMultInst)

                        profileCurve = blendProfileCurve(sel[crv0], sel[crv], i - crv0)
                        if profileCurve:
                            updateLattice(profileCurve, newCurve)

                    # Applying Settings
                    attributes.setAttr(newCurve, crv0Attr, ['Width', 'WidthX', 'WidthZ'])

                    if mc.attributeQuery('Width', n=newCurve, ex=1):
                        newWidth = 1
                        if 'Width' in crv0Attr:
                            newWidth = crv0ScaleX * crv0Attr['Width']
                        elif 'WidthX' in crv0Attr:
                            newWidth = (crv0Attr['WidthX'] + crv0Attr['WidthZ']) / 2 * crv0ScaleX
                        mc.setAttr(newCurve + '.Width', newWidth)
                    elif mc.attributeQuery('WidthX', n=newCurve, ex=1):
                        newWidthX = 1
                        newWidthZ = 1
                        if 'Width' in crv0Attr:
                            newWidthX = crv0ScaleX * crv0Attr['Width']
                            newWidthZ = newWidthX
                        elif 'WidthX' in crv0Attr:
                            newWidthX = crv0ScaleX * crv0Attr['WidthX']
                            newWidthZ = crv0ScaleX * crv0Attr['WidthZ']
                        mc.setAttr(newCurve + '.WidthX', newWidthX)
                        mc.setAttr(newCurve + '.WidthZ', newWidthZ)

                    try:
                        if shapes[1]:  # Applying Shader
                            newSel = mc.listRelatives(newCurve, c=1, pa=1)
                            newHist = mc.listHistory(newSel[0], f=1)
                            newShape = mc.ls(newHist, shapes=1, l=1)
                            mc.sets(newShape, forceElement=shapeFilter[0], nw=1)
                    except Exception as e:
                        LOGGER.exception(e)

                    allCurves.append(newCurve)
            i += step
        progress.end()
        mc.delete(loft[0])

        # Adding to group if exists
        if topGrp:
            mc.select(cl=1)
            for curve in allCurves:
                curveGrp = mc.listRelatives(curve, p=1, pa=1)[0]
                mc.parent(curveGrp, topGrp)
        mc.select(allCurves, r=1)
        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()
        resetCurvePivotPoint()

    def fill(self, hk=None):
        # type: (int) -> None
        """Place curve duplicates in-between selected curves"""
        self.initialize()
        sel = mc.filterExpand(mc.ls(sl=1, l=1, dag=1, tr=1), sm=9)
        if not sel or len(sel) < 2:
            MESSAGE.warningInView('Select at least two curves')
            return 0
        loft = mc.loft(sel, c=0, ch=1, d=3, ss=4, rsn=True, ar=1, u=1, rn=0, po=0)
        step = 1.0 / (mc.intSliderGrp('gsCurvesSlider', q=1, value=1) + 1.0)
        cond = len(sel) - 1
        allCurves = []
        i = 0
        progress = utils.ProgressBar('Adding Cards', cond * 100)
        while i < cond:
            if progress.tick(step * 100):
                break
            roundI = round(i, 1)
            crv0 = int(math.floor(roundI))
            crv = int(math.ceil(roundI))
            mod = math.fmod(roundI, 1)
            if mod != 0:  # Exclude whole numbers
                # Create curve from loft
                pathInst = mc.duplicateCurve('%s.v[%s]' % (loft[0], i), rn=0, ch=0, local=0, n='pathCurve_inst#')
                mc.rebuildCurve(pathInst, kr=2, s=mc.getAttr(sel[crv0] + '.spans'))
                targetPoints = mc.getAttr(pathInst[0] + '.cp[:]')
                mc.delete(pathInst)
                newCurve = duplicateCurve(customSel=[sel[crv0]])
                if newCurve:
                    newCurve = newCurve[0]
                else:
                    MESSAGE.warningInView('Wrong Selection Detected: %s' % sel[crv0])
                    break
                for p in range(0, len(targetPoints)):
                    mc.xform('%s.cp[%s]' % (newCurve, p), t=targetPoints[p], wd=1, ws=1)

                # Get Attributes
                previousAttr = attributes.getAttr(sel[crv0], excludeCheckboxes=True, excludeUV=True)
                targetAttr = attributes.getAttr(sel[crv], excludeCheckboxes=True, excludeUV=True)
                newAttr = previousAttr

                previousMultiInst = attributes.getMultiInst(sel[crv0])
                targetMultiInst = attributes.getMultiInst(sel[crv])
                blendMultiInst = []

                modifier = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
                if not modifier:
                    # Interpolate Attributes
                    for attr in previousAttr:
                        if attr in targetAttr:
                            newAttr[attr] = mt.lerp(i - crv0, previousAttr[attr], targetAttr[attr])

                    if previousMultiInst and targetMultiInst and (len(previousMultiInst) == len(targetMultiInst)):
                        for attr in range(len(previousMultiInst)):
                            blendMultiInst.append(attributes.blendMultInst(previousMultiInst[attr], targetMultiInst[attr], i - crv0))

                    profileCurve = blendProfileCurve(sel[crv0], sel[crv], i - crv0)
                    if profileCurve:
                        updateLattice(profileCurve, newCurve)

                # Apply Attributes
                attributes.setAttr(newCurve, newAttr)
                allCurves.append(newCurve)

                for attr in blendMultiInst:
                    attributes.setMultiInst(newCurve, attr)

            i += step
        mc.delete(loft)
        progress.end()
        mc.select(allCurves, r=1)
        resetCurvePivotPoint(customCurves=allCurves)

    ### Curve Extrude Creation Methods ###

    def extrudeCard(self, pathInst, auto=True):
        # type: (str, bool) -> str
        """Creates Curve Card from pathInst"""
        self.pathInst = mc.filterExpand(pathInst, sm=9)[0]

        if not self.pathInst:
            MESSAGE.warningInView('Select nurbs or bezier curve')
            return 0

        spans = mc.getAttr(self.pathInst + '.spans')
        self.ldiv = 10
        self.refine = 20
        if auto:
            self.ldiv = spans * 2 if spans <= 10 else spans
            self.refine = 20 if spans <= 20 else spans

        # Breaking if connection exist
        try:
            mc.disconnectAttr(self.pathInst + '.sx', self.pathInst + '.sy')
        except BaseException:
            pass
        try:
            mc.disconnectAttr(self.pathInst + '.sx', self.pathInst + '.sz')
        except BaseException:
            pass

        # Checking the stored scale factor
        scaleFactor = self.sf
        if mc.attributeQuery('scaleFactor', n=self.pathInst, ex=1) and WIDGETS['keepCurveAttributes'].isChecked():
            scaleFactor = mc.getAttr(self.pathInst + '.scaleFactor')

        # Creating profile
        self.profileInst = mc.curve(
            p=[(0, 0, -2.5 * scaleFactor), (0, 0.5 * scaleFactor, -1.666667 * scaleFactor), (0, 1 * scaleFactor, 0),
               (0, 0.5 * scaleFactor, 1.666667 * scaleFactor), (0, 0, 2.5 * scaleFactor)], k=[0, 0, 0, 1, 2, 2, 2], d=3,
            n='profileCurve_inst#')
        mc.makeIdentity(self.pathInst, n=0, s=1, r=1, t=1, apply=True, pn=1)
        curveOrigin = mc.pointPosition(self.pathInst + '.cv[0]', w=1)
        mc.xform(self.pathInst, ws=1, piv=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))
        mc.move(0, 0, 0, self.pathInst, rpr=1, ws=1)
        mc.makeIdentity(self.pathInst, n=0, s=1, r=1, t=1, apply=True, pn=1)
        mc.nurbsToPolygonsPref(polyType=1, vType=1, format=2, uType=1, vNumber=10, uNumber=3)
        self.hairCard = mc.extrude(self.profileInst, self.pathInst, upn=1, ch=True, rotation=0, ucp=1, n='geoCard#', fpt=1, scale=1,
                                   et=2, rn=False, rsp=1, po=1)[0]

        # Turning off inherit transform
        mc.setAttr(self.hairCard + '.inheritsTransform', 0)

        mc.xform(self.hairCard, t=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))

        # Create actual path curve
        self.pathCurve = str(mc.rename(mc.duplicate(self.pathInst, ilf=1, rr=1)[0], 'pathCurve#'))
        pathInstShape = mc.ls(self.pathInst, s=1, dag=1, l=1)[0]
        self.nurbsTesselate = mc.listConnections(mc.ls(self.hairCard, s=1, dag=1, l=1), s=True, d=False)[0]
        self.extrude = mc.listConnections(self.nurbsTesselate, s=True, d=False)[0]
        mc.setAttr(self.extrude + '.useProfileNormal', 1)

        # Connecting

        mc.connectAttr(self.pathCurve + '.translate', self.hairCard + '.translate', f=1)
        mc.connectAttr(self.pathCurve + '.rotate', self.hairCard + '.rotate', f=1)
        mc.connectAttr(self.pathCurve + '.scale', self.hairCard + '.scale', f=1)
        mc.connectAttr(self.pathCurve + '.scaleX', self.pathCurve + '.scaleY', f=1)
        mc.connectAttr(self.pathCurve + '.scaleX', self.pathCurve + '.scaleZ', f=1)
        mc.connectAttr(self.pathCurve + '.rotatePivot', self.hairCard + '.rotatePivot', f=1)
        mc.connectAttr(self.pathCurve + '.scalePivot', self.hairCard + '.scalePivot', f=1)
        mc.connectAttr(self.pathCurve + '.rotatePivotTranslate', self.hairCard + '.rotatePivotTranslate', f=1)
        mc.connectAttr(self.pathCurve + '.scalePivotTranslate', self.hairCard + '.scalePivotTranslate', f=1)
        mc.connectAttr(pathInstShape + '.editPoints[0]', self.profileInst + '.translate', f=1)
        mc.connectAttr(pathInstShape + '.editPoints[0]', self.extrude + '.pivot', f=1)

        # Moving path curve to original position

        mc.xform(self.pathCurve, ws=1, t=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))

        # Attribute addition
        mc.addAttr(self.pathCurve, ln='lengthDivisions', dv=self.ldiv, smx=500, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln='widthDivisions', dv=3, smx=11, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln='Orientation', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Twist', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Width', dv=1, smx=5, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='Taper', dv=1, smx=5, at='double', min=0, k=1)
        mc.addAttr(self.pathCurve, ln='Profile', smn=-2, dv=0, at='double', smx=2, k=1)
        mc.connectAttr(self.pathCurve + '.lengthDivisions', (self.nurbsTesselate + '.vNumber'), f=1)
        mc.connectAttr(self.pathCurve + '.widthDivisions', (self.nurbsTesselate + '.uNumber'), f=1)
        mc.connectAttr(self.pathCurve + '.Orientation', (self.profileInst + '.rotateX'), f=1)
        mc.connectAttr(self.pathCurve + '.Twist', (self.extrude + '.rotation'), f=1)
        mc.connectAttr(self.pathCurve + '.Width', (self.profileInst + '.scaleZ'), f=1)
        mc.connectAttr(self.pathCurve + '.Taper', (self.extrude + '.scale'), f=1)
        mc.connectAttr(self.pathCurve + '.Profile', (self.profileInst + '.scaleY'), f=1)

        # Add Modules

        self.addRefine()
        self.addAutoRefine()
        self.addPolyNormal()
        self.addUVs()
        self.addSolidify()
        self.addMessage()
        self.addScaleFactor()
        self.addDynamicDivisions()
        self.setCurveThickness()
        self.hideNodes()
        self.group('curveCard#')

        return (self.hairCardGrp + '|' + self.pathCurve)

    def extrudeTube(self, pathInst, auto=True):  # Creates Curve Tube from pathInst
        self.pathInst = mc.filterExpand(pathInst, sm=9)[0]

        if not self.pathInst:
            MESSAGE.warningInView('Select nurbs or bezier curve')
            return 0

        spans = mc.getAttr(self.pathInst + '.spans')
        self.ldiv = 10
        self.refine = 20
        if auto:
            self.ldiv = spans * 2 if spans <= 10 else spans
            self.refine = 20 if spans <= 20 else spans

        # Breaking if connected
        try:
            mc.disconnectAttr(self.pathInst + '.sx', self.pathInst + '.sy')
        except BaseException:
            pass
        try:
            mc.disconnectAttr(self.pathInst + '.sx', self.pathInst + '.sz')
        except BaseException:
            pass

        # Checking the stored scale factor
        scaleFactor = self.sf
        if mc.attributeQuery('scaleFactor', n=self.pathInst, ex=1) and WIDGETS['keepCurveAttributes'].isChecked():
            scaleFactor = mc.getAttr(self.pathInst + '.scaleFactor')

        # Creating a profile
        self.profileInst = mc.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, n="profileCurve_inst#",
                                     s=8, r=1 * scaleFactor, tol=0.01, nr=(0, 1, 0))
        mc.makeIdentity(self.pathInst, n=0, s=1, r=1, t=1, apply=True, pn=1)
        curveOrigin = mc.pointPosition(self.pathInst + '.cv[0]', w=1)
        mc.xform(self.pathInst, ws=1, piv=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))
        mc.move(0, 0, 0, self.pathInst, rpr=1, ws=1)
        mc.makeIdentity(self.pathInst, n=0, s=1, r=1, t=1, apply=True, pn=1)
        mc.nurbsToPolygonsPref(polyType=1, vType=1, format=2, uType=1, vNumber=10, uNumber=3)
        self.hairCard = mc.extrude(self.profileInst[0], self.pathInst, upn=1, ch=True, rotation=0,
                                   ucp=1, n='geoTube#', fpt=1, scale=1, et=2, rn=False, rsp=1, po=1)[0]

        # Turning off inherit transform
        mc.setAttr(self.hairCard + '.inheritsTransform', 0)

        mc.xform(self.hairCard, t=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))
        self.pathCurve = str(mc.rename(mc.duplicate(self.pathInst, ilf=1, rr=1)[0], 'pathCurve#'))
        pathInstShape = mc.ls(self.pathInst, s=1, dag=1, l=1)[0]
        self.nurbsTesselate = mc.listConnections(mc.ls(self.hairCard, s=1, dag=1, l=1)[0], s=True, d=False)[0]
        self.extrude = mc.listConnections(self.nurbsTesselate, s=True, d=False)[0]
        mc.setAttr(self.extrude + '.useProfileNormal', 1)

        # Connecting

        mc.connectAttr(self.pathCurve + '.translate', self.hairCard + '.translate', f=1)
        mc.connectAttr(self.pathCurve + '.rotate', self.hairCard + '.rotate', f=1)
        mc.connectAttr(self.pathCurve + '.scale', self.hairCard + '.scale', f=1)
        mc.connectAttr(self.pathCurve + '.scaleX', self.pathCurve + '.scaleY', f=1)
        mc.connectAttr(self.pathCurve + '.scaleX', self.pathCurve + '.scaleZ', f=1)
        mc.connectAttr(self.pathCurve + '.rotatePivot', self.hairCard + '.rotatePivot', f=1)
        mc.connectAttr(self.pathCurve + '.scalePivot', self.hairCard + '.scalePivot', f=1)
        mc.connectAttr(self.pathCurve + '.rotatePivotTranslate', self.hairCard + '.rotatePivotTranslate', f=1)
        mc.connectAttr(self.pathCurve + '.scalePivotTranslate', self.hairCard + '.scalePivotTranslate', f=1)
        mc.connectAttr(pathInstShape + '.editPoints[0]', self.profileInst[0] + '.translate', f=1)
        mc.connectAttr(pathInstShape + '.editPoints[0]', self.extrude + '.pivot', f=1)

        # Moving path curve to original position

        mc.xform(self.pathCurve, ws=1, t=(curveOrigin[0], curveOrigin[1], curveOrigin[2]))

        # Attribute addition
        mc.addAttr(self.pathCurve, ln="lengthDivisions", dv=self.ldiv, smx=500, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln="widthDivisions", dv=7, smx=53, at='long', min=4, k=1)
        mc.addAttr(self.pathCurve, ln="Orientation", smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln="Twist", smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln="WidthX", dv=1, smx=20, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln="WidthZ", dv=1, smx=20, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln="Taper", dv=1, smx=5, at='double', min=0, k=1)
        mc.connectAttr(self.pathCurve + ".lengthDivisions", self.nurbsTesselate + ".vNumber", f=1)
        mc.connectAttr(self.pathCurve + ".widthDivisions", self.nurbsTesselate + ".uNumber", f=1)
        mc.connectAttr(self.pathCurve + ".Orientation", self.profileInst[0] + ".rotateY", f=1)
        mc.connectAttr(self.pathCurve + ".Twist", self.extrude + ".rotation", f=1)
        mc.connectAttr(self.pathCurve + ".WidthX", self.profileInst[0] + ".scaleX", f=1)
        mc.connectAttr(self.pathCurve + ".WidthZ", self.profileInst[0] + ".scaleZ", f=1)
        mc.connectAttr(self.pathCurve + ".Taper", self.extrude + ".scale", f=1)

        self.addRefine()
        self.addAutoRefine()
        self.addPolyNormal()
        self.addUVs()
        self.addSolidify()
        self.addMessage()
        self.addScaleFactor()
        self.addDynamicDivisions()
        self.setCurveThickness()
        self.hideNodes()
        self.group('curveTube#')

        return (self.hairCardGrp + '|' + self.pathCurve)

    ### Curve Warp Creation Methods ###

    def warpCard(self, pathCurve, auto=True):  # Creates New Curve Warp Card from inputCurve
        self.pathCurve = mc.filterExpand(pathCurve, sm=9)
        if not self.pathCurve:
            MESSAGE.warningInView('Select at least one curve')
            return 0

        self.pathCurve = mc.rename(self.pathCurve, 'pathCurve#')
        self.pathCurveShape = mc.ls(self.pathCurve, dag=1, s=1, l=1)[0]
        spans = mc.getAttr(self.pathCurveShape + '.spans')
        self.ldiv = 10
        self.refine = 20
        if auto:
            self.ldiv = spans * 2 if spans <= 10 else spans
            self.refine = 20 if spans <= 20 else spans

        # Breaking
        try:
            mc.disconnectAttr(self.pathCurve + '.sx', self.pathCurve + '.sy')
        except BaseException:
            pass
        try:
            mc.disconnectAttr(self.pathCurve + '.sx', self.pathCurve + '.sz')
        except BaseException:
            pass

        # Checking the stored scale factor
        scaleFactor = self.sf
        if mc.attributeQuery('scaleFactor', n=self.pathCurve, ex=1) and WIDGETS['keepCurveAttributes'].isChecked():
            scaleFactor = mc.getAttr(self.pathCurve + '.scaleFactor')

        # Creating path and profile curves
        self.pathInst = mc.curve(d=3, p=[(0, -0.0001, 0), (1.666667 * scaleFactor, 0, 0), (5 * scaleFactor, 0, 0),
                                         (10 * scaleFactor, 0, 0), (15 * scaleFactor, 0, 0), (18.333333 * scaleFactor, 0, 0),
                                         (20 * scaleFactor, 0, 0)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], n='pathCurve_inst#')
        mc.rebuildCurve(self.pathInst, s=30)

        self.profileInst = mc.curve(
            p=[(0, 0, -2.5 * scaleFactor), (0, 0.5 * scaleFactor, -1.666667 * scaleFactor), (0, 1 * scaleFactor, 0),
               (0, 0.5 * scaleFactor, (1.666667 * scaleFactor)), (0, 0, (2.5 * scaleFactor))], k=[0, 0, 0, 1, 2, 2, 2], d=3,
            n='profileCurve_inst#')

        mc.setAttr(self.profileInst + '.sy', 4)

        mc.nurbsToPolygonsPref(polyType=1, vType=1, format=2, uType=1, vNumber=10, uNumber=3)
        extrudeCmd = mc.extrude(self.profileInst, self.pathInst, upn=1, ch=True, rotation=0, ucp=1, n='geoCard#', fpt=1,
                                scale=1, et=2, rn=False, rsp=1, po=1)

        self.hairCard = extrudeCmd[0]
        self.extrude = extrudeCmd[1]
        self.nurbsTesselate = mc.listConnections(self.extrude, s=False, d=True, et=1, t='nurbsTessellate')[0]

        # Creating deformers

        latticeDivisions = 10

        self.lattice = mc.lattice(self.hairCard, dv=[latticeDivisions, 2, 2], oc=True, ldv=[2, 2, 2], ol=1)
        mc.move(0, 0, 0, self.lattice[1] + '.scalePivot', self.lattice[1] + '.rotatePivot', a=1)

        points = []
        for i in range(latticeDivisions):
            points.append(mc.pointPosition(self.lattice[1] + '.pt[%s][1][0]' % (i), l=1))

        self.twist = mc.nonLinear(self.hairCard, type='twist')
        mc.setAttr(self.twist[1] + '.rz', 90)
        mc.move(0, 0, 0, self.twist, a=1, y=1)

        # Creating warp

        self.curveWarp = mc.deformer(ignoreSelected=1, type='curveWarp', n='curveWarp#')[0]
        mc.deformer(self.curveWarp, e=1, g=self.hairCard)
        mc.connectAttr(self.pathCurveShape + '.worldSpace[0]', self.curveWarp + '.inputCurve')
        mc.setAttr(self.curveWarp + '.alignmentMode', 2)

        # Turning off inherit transform

        mc.setAttr(self.hairCard + '.inheritsTransform', 0)
        mc.setAttr(self.extrude + '.useProfileNormal', 1)
        if MAYA_VER >= 2018:
            mc.setAttr(self.curveWarp + '.samplingAccuracy', 0.333)
            mc.addAttr(self.pathCurve, ln='samplingAccuracy', dv=0.333, smx=2, at='double', min=0.001, k=1)
            mc.connectAttr(self.pathCurve + '.samplingAccuracy', self.curveWarp + '.samplingAccuracy')
        mc.setAttr(self.curveWarp + '.twistRotation', 720)

        # Adding and connecting main attributes

        mc.addAttr(self.pathCurve, ln='lengthDivisions', dv=self.ldiv, smx=500, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln='widthDivisions', dv=3, smx=11, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln='Orientation', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Twist', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='invTwist', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Width', dv=1, smx=5, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='LengthLock', at='enum', dv=0, en="Locked:Unlocked:", k=1)
        mc.addAttr(self.pathCurve, ln='Length', dv=1, smx=30, smn=-30, at='double', k=1)
        mc.addAttr(self.pathCurve, ln='Offset', dv=0, smx=1, smn=-1, at='double', min=-30, max=30, k=1)
        mc.addAttr(self.pathCurve, ln='Taper', dv=1, smx=5, at='double', min=0, k=1)
        mc.addAttr(self.pathCurve, ln='Profile', smn=-2, dv=0, at='double', smx=2, k=1)
        mc.addAttr(self.pathCurve, ln='profileSmoothing', dv=2, at='long', min=2, max=30, k=0)
        mc.addAttr(self.pathCurve, ln='profileMagnitude', dv=1, at='double', min=-2, max=2, k=0)

        if not mc.attributeQuery('initialLatticePoints', n=self.pathCurve, ex=1):
            mc.addAttr(self.pathCurve, ln='initialLatticePoints', dt='double3', m=1)
        for i in range(len(points)):
            mc.setAttr(self.pathCurve + '.initialLatticePoints[%s]' % i, *points[i], type='double3')

        if not mc.attributeQuery('latticeMessage', n=self.pathCurve, ex=1):
            mc.addAttr(self.pathCurve, ln='latticeMessage', at='message', k=0)
        mc.addAttr(self.lattice[1], ln='latticeMessage', at='message', k=0)

        mc.connectAttr(self.pathCurve + '.lengthDivisions', self.nurbsTesselate + '.vNumber', f=1)
        mc.connectAttr(self.pathCurve + '.widthDivisions', self.nurbsTesselate + '.uNumber', f=1)
        mc.connectAttr(self.pathCurve + '.Twist', self.twist[0] + '.startAngle', f=1)
        mc.connectAttr(self.pathCurve + '.invTwist', self.twist[0] + '.endAngle', f=1)
        mc.connectAttr(self.pathCurve + '.Width', self.profileInst + '.scaleZ', f=1)
        mc.connectAttr(self.pathCurve + '.Taper', self.extrude + '.scale', f=1)
        mc.connectAttr(self.pathCurve + '.Profile', self.profileInst + '.scaleY', f=1)
        mc.connectAttr(self.pathCurve + '.LengthLock', self.curveWarp + '.keepLength', f=1)
        mc.connectAttr(self.pathCurve + '.Length', self.curveWarp + '.lengthScale', f=1)
        mc.connectAttr(self.pathCurve + '.Offset', self.curveWarp + '.offset', f=1)
        mc.connectAttr(self.pathCurve + '.latticeMessage', self.lattice[1] + '.latticeMessage', f=1)
        mc.connectAttr(self.pathCurve + '.profileSmoothing', self.lattice[0] + '.localInfluenceS', f=1)
        mc.connectAttr(self.pathCurve + '.profileMagnitude', self.lattice[0] + '.envelope', f=1)

        # Fix Twist connections for Maya 2020.4
        twistHandle = mc.listRelatives(self.twist, c=1, pa=1)
        connectionCheck = mc.isConnected(self.twist[0] + '.startAngle', twistHandle[0] + '.startAngle')
        if not connectionCheck:
            mc.connectAttr(self.twist[0] + '.startAngle', twistHandle[0] + '.startAngle', f=1)
            mc.connectAttr(self.twist[0] + '.endAngle', twistHandle[0] + '.endAngle', f=1)

        # Fix Lattice connection for Maya 2020.4
        if MAYA_VER == 2020:
            ffd = mc.listConnections(self.pathCurve + '.profileMagnitude', s=0, d=1)
            origGeo = mc.listConnections(ffd[0] + '.originalGeometry[0]', s=1, d=0, p=1)
            mc.disconnectAttr(origGeo[0], ffd[0] + '.originalGeometry[0]')

        # Twist Magnitude and Orientation Sum

        mc.addAttr(self.pathCurve, ln='Magnitude', dv=0.5, at='double', h=1)
        ex = '''
        {2}.rx = {1}.Orientation + {1}.rx;
        {0}.rotation = 360 * (1 - {1}.Magnitude);
        {0}.twistRotation = 720 * {1}.Magnitude;
        '''.format(self.curveWarp, self.pathCurve, self.profileInst)
        self.magnExpr = mc.expression(ae=0, s=ex, n='twistOrienCalc#')

        self.addRefine(True)
        self.addAutoRefine()
        self.addPolyNormal()
        self.addUVs()
        self.addSolidify()
        self.addMessage()
        self.addScaleFactor()
        self.addDynamicDivisions()
        self.setCurveThickness()
        self.hideNodes()
        self.clearTweakNode()
        self.group('warpCard#')

        return (self.hairCardGrp + '|' + self.pathCurve)

    def warpTube(self, pathCurve, auto=True):  # Creates New Curve Warp Tube from inputCurve
        self.pathCurve = mc.filterExpand(pathCurve, sm=9)[0]
        if not self.pathCurve:
            MESSAGE.warningInView('Select at least one curve')
            return 0
        self.pathCurve = mc.rename(self.pathCurve, 'pathCurve#')
        self.pathCurveShape = mc.ls(self.pathCurve, dag=1, s=1, l=1)[0]
        spans = mc.getAttr(self.pathCurveShape + '.spans')
        self.ldiv = 10
        self.refine = 20
        if auto:
            self.ldiv = spans * 2 if spans <= 10 else spans
            self.refine = 20 if spans <= 20 else spans

        try:
            mc.disconnectAttr(self.pathCurve + '.sx', self.pathCurve + '.sy')
        except BaseException:
            pass
        try:
            mc.disconnectAttr(self.pathCurve + '.sx', self.pathCurve + '.sz')
        except BaseException:
            pass

        # Checking the stored scale factor
        scaleFactor = self.sf
        if mc.attributeQuery('scaleFactor', n=self.pathCurve, ex=1) and WIDGETS['keepCurveAttributes'].isChecked():
            scaleFactor = mc.getAttr(self.pathCurve + '.scaleFactor')

        # Creating path and profile curves
        self.pathInst = mc.curve(d=3, p=[(0, -0.0001, 0), (1.666667 * scaleFactor, 0, 0), (5 * scaleFactor, 0, 0),
                                         (10 * scaleFactor, 0, 0), (15 * scaleFactor, 0, 0), (18.333333 * scaleFactor, 0, 0),
                                         (20 * scaleFactor, 0, 0)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], n='pathCurve_inst#')
        mc.rebuildCurve(self.pathInst, s=30)

        self.profileInst = mc.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, n="profileCurve_inst#", s=8, r=1 * scaleFactor, tol=0.01,
                                     nr=(0, 1, 0))[0]

        mc.nurbsToPolygonsPref(polyType=1, vType=1, format=2, uType=1, vNumber=10, uNumber=7)
        extrudeCmd = mc.extrude(self.profileInst, self.pathInst, upn=1, ch=True, rotation=0, ucp=1, n='geoTube#', fpt=1,
                                scale=1, et=2, rn=False, rsp=1, po=1)

        self.hairCard = extrudeCmd[0]
        self.extrude = extrudeCmd[1]
        self.nurbsTesselate = mc.listConnections(self.extrude, s=False, d=True, et=1, t='nurbsTessellate')[0]

        # Creating curveWarp deformer

        self.curveWarp = mc.deformer(ignoreSelected=1, type='curveWarp', n='curveWarp#')[0]
        mc.deformer(self.curveWarp, e=1, g=self.hairCard)
        mc.connectAttr(self.pathCurveShape + '.worldSpace[0]', self.curveWarp + '.inputCurve')

        # Turning off inherit transform

        mc.setAttr(self.hairCard + '.inheritsTransform', 0)
        mc.setAttr(self.extrude + '.useProfileNormal', 1)

        if MAYA_VER >= 2018:
            mc.setAttr(self.curveWarp + '.samplingAccuracy', 0.333)
            mc.addAttr(self.pathCurve, ln='samplingAccuracy', dv=0.333, smx=2, at='double', min=0.001, k=1)
            mc.connectAttr(self.pathCurve + '.samplingAccuracy', self.curveWarp + '.samplingAccuracy')

        mc.setAttr(self.curveWarp + '.twistRotation', 720)

        # Adding and connecting main attributes

        mc.addAttr(self.pathCurve, ln='lengthDivisions', dv=self.ldiv, smx=500, at='long', min=2, k=1)
        mc.addAttr(self.pathCurve, ln='widthDivisions', dv=7, smx=53, at='long', min=4, k=1)
        mc.addAttr(self.pathCurve, ln='Orientation', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Twist', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln="WidthX", dv=1, smx=5, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln="WidthZ", dv=1, smx=5, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='LengthLock', at='enum', dv=0, en="Locked:Unlocked:", k=1)
        mc.addAttr(self.pathCurve, ln='Length', dv=1, smx=30, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='Offset', dv=0, smx=1, smn=-1, at='double', min=-30, max=30, k=1)
        mc.addAttr(self.pathCurve, ln='Taper', dv=1, max=1.9, at='double', min=0, k=1)
        mc.connectAttr(self.pathCurve + '.lengthDivisions', self.nurbsTesselate + '.vNumber', f=1)
        mc.connectAttr(self.pathCurve + '.widthDivisions', self.nurbsTesselate + '.uNumber', f=1)
        mc.connectAttr(self.pathCurve + '.Twist', self.extrude + '.rotation', f=1)
        mc.connectAttr(self.pathCurve + '.Taper', self.extrude + '.scale', f=1)
        mc.connectAttr(self.pathCurve + '.LengthLock', self.curveWarp + '.keepLength', f=1)
        mc.connectAttr(self.pathCurve + '.Length', self.curveWarp + '.lengthScale', f=1)
        mc.connectAttr(self.pathCurve + '.Offset', self.curveWarp + '.offset', f=1)

        # Twist Magnitude

        mc.addAttr(self.pathCurve, ln='Magnitude', dv=0.5, at='double', h=1)
        ex = '''
        {2}.rx = {1}.Orientation + {1}.rx;
        {0}.rotation = 360 * (1 - {1}.Magnitude);
        {0}.twistRotation = 720 * {1}.Magnitude;
        '''.format(self.curveWarp, self.pathCurve, self.profileInst)
        self.magnExpr = mc.expression(ae=0, s=ex, n='twistOrienCalc#')
        # Handling Width to Scale Switch

        scaleEx = '''
        if(({0}.WidthX >= 5 && {0}.WidthZ >= 5))
        {{
            {1}.scaleZ = 5;
            {1}.scaleX = 5;
            {2}.maxScale = abs({0}.WidthZ - 5) + abs({0}.WidthX - 5) + 2;
        }}
        else if (({0}.WidthX >= 5))
        {{
            {1}.scaleX = 5;
            {1}.scaleZ = {0}.WidthZ;
            {2}.maxScale = abs({0}.WidthX - 5) + 2;
        }}
        else if (({0}.WidthZ >= 5))
        {{
            {1}.scaleZ = 5;
            {1}.scaleX = {0}.WidthX;
            {2}.maxScale = abs({0}.WidthZ - 5) + 2;
        }}
        else
        {{
            {2}.maxScale = 2;
            {1}.scaleX = {0}.WidthX;
            {1}.scaleZ = {0}.WidthZ;
        }}
        '''.format(self.pathCurve, self.profileInst, self.curveWarp)
        self.scaleExpr = mc.expression(ae=0, s=scaleEx, n='scaleManagement#')

        self.addRefine(True)
        self.addAutoRefine()
        self.addPolyNormal()
        self.addUVs()
        self.addSolidify()
        self.addMessage()
        self.addScaleFactor()
        self.addDynamicDivisions()
        self.setCurveThickness()
        self.hideNodes()
        self.clearTweakNode()
        self.group('warpTube#')

        return (self.hairCardGrp + '|' + self.pathCurve)

    def bind(self, hk=None):  # TODO: Check hotkey command # Attaches selected geo to selected curve
        self.initialize()
        # Sort for geoWarp
        self.ldiv = 10
        self.refine = 20

        sel = mc.ls(sl=1, tr=1)
        if not sel or len(sel) < 2:
            MESSAGE.warningInView(
                'Select one curve and one geometry or Select one target curve and any number of curveCards/Tubes')
            return 0

        curves = mc.filterExpand(sel, sm=9)
        geo = mc.filterExpand(sel, sm=12)

        # Add gsmessage
        for crv in curves:
            if not mc.attributeQuery('gsmessage', n=crv, ex=1):
                mc.addAttr(crv, ln='gsmessage', at='message', k=0)

        if not getOption('massBindOption'):
            self.singleBind(sel, geo, hk)
        else:
            # Filter active curves
            activeCurves = []
            inactiveCurves = []
            for curve in curves:
                if (mc.attributeQuery('Orientation', n=curve, ex=1) and
                        mc.connectionInfo(curve + '.Orientation', isSource=1)):
                    activeCurves.append(curve)
                else:
                    inactiveCurves.append(curve)
            if not geo:
                progress = utils.ProgressBar('Binding', len(inactiveCurves))
                try:
                    for i in range(len(inactiveCurves)):
                        progress.tick(1)
                        passedCurves = activeCurves + [inactiveCurves[i]]
                        self.singleBind(passedCurves, None, True)
                except Exception as e:
                    LOGGER.exception(e)
                finally:
                    progress.end()
            else:
                progress = utils.ProgressBar('Binding', len(inactiveCurves))
                try:
                    for i in range(len(inactiveCurves)):
                        progress.tick(1)
                        passedGeo = mc.duplicate(geo[0])
                        passedCurves = [inactiveCurves[i]]
                        self.singleBind(passedCurves, passedGeo, True)
                except Exception as e:
                    LOGGER.exception(e)
                finally:
                    progress.end()

    def singleBind(self, curves, geometry=None, hk=None):
        grpName = 'bindGeo#'

        sel = curves
        self.pathCurve = []
        self.geo = []

        self.pathCurve = mc.filterExpand(curves, sm=9)
        self.geo = geometry

        isCurveWarp = False
        origGroups = []
        targetCurve = None
        sourceCurves = []

        if not self.geo:
            # Sort for curveWarp
            isCurveWarp = True
            grpName = 'bindGroup#'
            for crv in sel:
                attr = attributes.getAttr(crv, 1, 1)
                if 'Orientation' in attr and mc.connectionInfo(crv + '.Orientation', isSource=1):
                    sourceCurves.append(crv)
                else:
                    targetCurve = crv
            if not sourceCurves or not targetCurve:
                MESSAGE.warningInView('Wrong selection')
                return 0

            self.pathCurve = targetCurve

            # Duplicating the source curves if needed
            mod = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
            if getOption('bindDuplicatesCurves') or getOption('massBindOption') or mod:
                sourceCurves = duplicateCurve(sourceCurves)

            # Original Groups
            for curve in sourceCurves:
                if (mc.attributeQuery('Orientation', n=curve, ex=1) and
                        mc.connectionInfo(curve + '.Orientation', isSource=1)):
                    origGroups += mc.listRelatives(curve, p=1, pa=1)

            # Adding source curves to a new group
            hairGrp = self.currentLayerInd()
            curveAddToLayer(hairGrp, inputCurves=sourceCurves)

            # Connect message
            for crv in sourceCurves:
                try:
                    mc.connectAttr(self.pathCurve + ".gsmessage", crv + '.gsmessage', f=1)
                except BaseException:
                    LOGGER.info('"gsmessage" attribute not found. Possibly legacy curve.')

            # Flip original UVs before bind
            if getOption('bindFlipUVs'):
                for crv in sourceCurves:
                    if mc.attributeQuery('flipUV', n=crv, ex=1):
                        mc.setAttr(crv + '.flipUV', not mc.getAttr(crv + '.flipUV'))

            # Center and average pivots
            wsPivX = list()
            wsPivY = list()
            wsPivZ = list()
            lsPiv = list()
            tr = list()
            mc.xform(sourceCurves, cpc=1)
            for ele in sourceCurves:
                wsPiv = mc.xform(ele, q=1, rp=1, ws=1)
                wsPivX.append(wsPiv[0])
                wsPivY.append(wsPiv[1])
                wsPivZ.append(wsPiv[2])
                lsPiv.append(mc.xform(ele, q=1, rp=1))
                tr.append(mc.xform(ele, q=1, t=1))
            wsPivX = sum(wsPivX) / len(wsPivX)
            wsPivY = sum(wsPivY) / len(wsPivY)
            wsPivZ = sum(wsPivZ) / len(wsPivZ)

            mc.xform(sourceCurves, piv=[wsPivX, wsPivY, wsPivZ], wd=1, ws=1)

            mc.move(0, 0, 0, sourceCurves, rpr=1)
            findGeo = []
            for part in sourceCurves:
                findGeo.append(selectPart(2, True, part)[0])

            if len(findGeo) > 1:
                unite = mc.polyUnite(findGeo, ch=1, muv=1, n='warpCard#')
                mc.rename(unite[1], 'gsUniteNode#')
                self.geo = unite[0]
            else:
                tempNode = mc.createNode('mesh')
                unite = mc.polyUnite([findGeo[0], tempNode], ch=1, muv=1, n='warpCard#')
                mc.rename(unite[1], 'gsUniteNode#')
                self.geo = unite[0]
                mc.delete(mc.listRelatives(mc.listRelatives(tempNode, p=1, pa=1), p=1, pa=1))

            shader = utils.getShader(self.geo)
            for key in shader:
                mc.sets(shader[key], e=1, fe=key, nw=1)
            mc.select(self.geo, r=1)
        else:
            self.pathCurve = self.pathCurve[0]
            self.geo = self.geo[0]
            mc.makeIdentity(self.geo, a=1, t=1, r=1, s=1, n=0, pn=1)
            mc.makeIdentity(self.pathCurve, a=1, t=1, r=1, s=1, n=0, pn=1)
            mc.makeIdentity(self.pathCurve, a=0, t=1, r=1, s=1, n=0, pn=1)

        # Cleaning previous attrs (Replace with remembering attrs)
        prevAttrs = attributes.getAttr(self.pathCurve)
        graphAttrs = {}
        for attr in attributes.graphAttributes:
            if mc.attributeQuery(attr, n=self.pathCurve, ex=1):
                graphAttrs[attr] = mc.getAttr(self.pathCurve + '.' + attr)
        for attr in attributes.attrList | attributes.checkBoxes | attributes.uvAttr:
            if mc.attributeQuery(attr, n=self.pathCurve, ex=1):
                mc.deleteAttr(self.pathCurve + '.' + attr)

        # Main warp
        if not isCurveWarp:
            mc.select(self.pathCurve, self.geo, r=1)
        if MAYA_VER <= 2017:
            mel.eval('MoveTool;')
        mel.eval('BakeCustomPivot;')
        attributes.deleteAttr(self.pathCurve)
        self.pathCurve = mc.rename(self.pathCurve, 'pathCurve#')
        self.geo = mc.rename(self.geo, 'geoCard#')

        self.polyNormalNode = mc.polyNormal(self.geo, ch=1, unm=0, nm=1)[0]

        self.curveWarp = mc.deformer(ignoreSelected=1, type='curveWarp', n='curveWarp#')[0]
        mc.deformer(self.curveWarp, e=1, g=self.geo)
        mc.connectAttr(self.pathCurve + '.worldSpace[0]', self.curveWarp + '.inputCurve')

        mc.setAttr(self.geo + '.inheritsTransform', 0)
        if MAYA_VER >= 2018:
            mc.setAttr(self.curveWarp + '.samplingAccuracy', 0.333)
            mc.addAttr(self.pathCurve, ln='samplingAccuracy', dv=0.333, smx=2, at='double', min=0.001, k=1)
            mc.connectAttr(self.pathCurve + '.samplingAccuracy', self.curveWarp + '.samplingAccuracy')
        mc.setAttr(self.curveWarp + '.twistRotation', 720)

        # Optionally flip axis and normals and change orientation
        axisFlipDefault = 0
        orientationDefault = 0
        reverseNormalsDefault = 1
        if getOption('bindFlipUVs'):
            axisFlipDefault = 1
            orientationDefault = 90
            reverseNormalsDefault = 0

        mc.addAttr(self.pathCurve, ln='Axis', dv=0, at='enum', en="Auto:X:Y:Z:", k=1)
        mc.addAttr(self.pathCurve, ln='AxisFlip', dv=axisFlipDefault, at='bool', k=1)
        mc.addAttr(self.pathCurve, ln='Orientation', smn=-360, dv=orientationDefault, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='Width', dv=2, smx=5, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='LengthLock', at='enum', dv=0, en="Locked:Unlocked:", k=1)
        mc.addAttr(self.pathCurve, ln='Length', dv=1, smx=200, at='double', min=0.001, k=1)
        mc.addAttr(self.pathCurve, ln='Offset', dv=0, smx=1, smn=-1, at='double', min=-30, max=30, k=1)
        mc.addAttr(self.pathCurve, ln="reverseNormals", dv=reverseNormalsDefault, en="reverse:off:", at="enum", k=1)

        mc.connectAttr(self.pathCurve + '.AxisFlip', self.curveWarp + '.flipAxis')
        mc.connectAttr(self.pathCurve + '.Width', self.curveWarp + '.maxScale')
        mc.connectAttr(self.pathCurve + '.LengthLock', self.curveWarp + '.keepLength')
        mc.connectAttr(self.pathCurve + '.Length', self.curveWarp + '.lengthScale')
        mc.connectAttr(self.pathCurve + '.Offset', self.curveWarp + '.offset')
        mc.connectAttr(self.pathCurve + ".reverseNormals", self.polyNormalNode + ".normalMode", f=1)

        # Twist Magnitude

        mc.addAttr(self.pathCurve, ln='Magnitude', dv=0.5, at='double', h=1)
        expr = '''
        {0}.rotation = 360 * (1 - {1}.Magnitude) + {1}.Orientation;
        {0}.twistRotation = 720 * {1}.Magnitude;
        {0}.alignmentMode = {1}.Axis + 1;
        '''.format(self.curveWarp, self.pathCurve)
        self.magnExpr = mc.expression(ae=0, s=expr, n='twistMagnitudeCalc#')

        self.addRefine(True)
        self.addAutoRefine()

        # Set prev attributes
        if WIDGETS['keepCurveAttributes'].isChecked():
            for attr in graphAttrs:
                values = graphAttrs[attr]
                if attr == 'profileCurve':
                    updateLattice(values, self.pathCurve)
                else:
                    rebuildCurve = mc.listConnections(self.pathCurve + '.curveSmooth')[0]
                    warp = mc.listConnections(rebuildCurve + '.outputCurve')[0]
                    graphValues = utils.fromStringToDouble2(values)
                    utils.setDouble2Attr(warp, attr, graphValues)
            attributes.setAttr(self.pathCurve, prevAttrs)

        self.setCurveThickness()
        self.group(grpName, True)

        if isCurveWarp:
            origCurves = mc.group(origGroups, n='origCurves#')
            origCurvesGrp = mc.parent(origCurves, self.hairCardGrp)
            mc.setAttr(origCurvesGrp[0] + '.visibility', 0)

        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()

        mc.select(self.hairCardGrp + '|' + self.pathCurve, r=1)
        resetCurvePivotPoint(self.hairCardGrp + '|' + self.pathCurve)

    def unbind(self):
        self.initialize()
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel:
            sel = mc.filterExpand(mc.ls(hl=1, o=1), sm=9)
        if not sel:
            MESSAGE.warningInView('Select at least one compatible curve (Bound/Warp curves or geometry)')
            return
        previousCurves = []
        newSel = []
        for obj in sel:
            initialGroup = selectPart(0, True, obj)
            origGeometry = selectPart(2, True, obj)
            if not origGeometry:
                continue
            shader = utils.getShader(origGeometry)
            topGroup = mc.listRelatives(initialGroup, p=1, pa=1)
            origCurvesGrp = selectPart(3, True, obj)
            if not origCurvesGrp:  # If orig objects are geometry
                if not mc.attributeQuery('Axis', n=obj, ex=1):
                    LOGGER.info('%s is not a bound group. Skipping.' % obj)
                    continue
                mc.editDisplayLayerMembers("defaultLayer", origGeometry, nr=1)
                newGeo = []
                if topGroup:
                    newGeo = mc.parent(origGeometry, topGroup)
                    previousCurves.append(mc.parent(mc.duplicate(obj), topGroup))
                else:
                    newGeo = mc.parent(origGeometry, w=1)
                    previousCurves.append(mc.parent(mc.duplicate(obj), w=1))
                mc.delete(initialGroup)
                mc.delete(newGeo, ch=1)
                newSel.append(newGeo[0])
            else:  # If orig objects are curves
                origGroups = mc.listRelatives(origCurvesGrp, c=1, pa=1)
                newCards = []
                if not origGroups:
                    LOGGER.info('%s is not a bound card/geo. Skipping' % obj)
                    continue
                if topGroup:
                    newCards = mc.parent(origGroups, topGroup)
                    previousCurves.append(mc.parent(mc.duplicate(obj), topGroup))
                else:
                    newCards = mc.parent(origGroups, w=1)
                    previousCurves.append(mc.parent(mc.duplicate(obj), w=1))
                mc.delete(initialGroup)
                for card in newCards:
                    geo = selectPart(2, True, card)
                    nextNode = mc.listRelatives(geo, c=1, pa=1)
                    i = 0
                    while mc.nodeType(nextNode) != 'mesh':
                        i += 1
                        if i >= 100:
                            break
                        nextNode = mc.listRelatives(nextNode, c=1, pa=1)
                    mc.setAttr(nextNode[0] + '.intermediateObject', 0)
                    transformNode = mc.listRelatives(nextNode, p=1, pa=1)
                    transformNode = mc.parent(transformNode, card)
                    connections = mc.listConnections(geo, d=0, s=1, p=1)
                    for connection in connections:
                        attr = connection.split('.')[1]
                        target = '%s.%s' % (transformNode[0], attr)
                        if mc.attributeQuery(attr, n=transformNode[0], ex=1):
                            mc.connectAttr(connection, target, f=1)
                    # NOTE: Rerouting connections manually to avoid node deletions (Autodesk bug in 2022, 2023)
                    geoShape = mc.listRelatives(geo, c=1, pa=1)
                    if geoShape:
                        nurbsTesselate = mc.listConnections(geoShape[0] + '.inMesh', p=1)
                        destConnections1 = mc.listConnections(geoShape[0] + '.worldMesh[0]', p=1)
                        destConnections2 = mc.listConnections(geoShape[0] + '.outMesh', p=1)
                        if nurbsTesselate and destConnections1 and destConnections2:
                            for destCon in destConnections1 + destConnections2:
                                mc.connectAttr(nurbsTesselate[0], destCon, f=1)
                    mc.delete(geo)
                    transformNode = mc.rename(transformNode, geo)
                    mc.sets(transformNode, forceElement=list(shader.keys())[0])
                    mc.setAttr(transformNode + '.v', 1)
                    curve = selectPart(1, True, card)
                    layerID = getCurveLayer(curve[0])
                    curveAddToLayer(layerID, inputCurves=curve)
                    if getOption('bindFlipUVs'):
                        if mc.attributeQuery('flipUV', n=curve[0], ex=1):
                            mc.setAttr(curve[0] + '.flipUV', not mc.getAttr(curve[0] + '.flipUV'))
                    newSel.append(curve[0])
        for curve in previousCurves:
            mc.editDisplayLayerMembers("defaultLayer", curve, nr=1)
            toggleColor.resetSingleCurve(curve)
            mc.rename(curve, 'unboundCurve#')
        mc.select(newSel)

    ### Curve Creation Modules ###

    def addRefine(self, output=None):
        inst = None
        if output:
            output = self.curveWarp + '.inputCurve'
            inst = self.pathCurve
        else:
            output = self.extrude + '.path'
            inst = self.pathInst

        self.rebuildCurve = mc.createNode('rebuildCurve')
        mc.setAttr(self.rebuildCurve + '.keepRange', 2)
        mc.addAttr(self.pathCurve, ln='curveRefine', smn=-1, dv=self.refine, at='long', smx=300, k=1)
        mc.addAttr(self.pathCurve, ln='curveSmooth', dv=0, smx=10, at='double', min=-0, k=1)
        mc.connectAttr(inst + '.worldSpace[0]', self.rebuildCurve + '.inputCurve', f=1)
        mc.connectAttr(self.rebuildCurve + '.outputCurve', output, f=1)
        mc.connectAttr(self.pathCurve + '.curveRefine', self.rebuildCurve + '.spans', f=1)
        mc.connectAttr(self.pathCurve + '.curveSmooth', self.rebuildCurve + '.smooth', f=1)

    def addPolyNormal(self):
        self.polyNormalNode = mc.polyNormal(self.hairCard, ch=1, nm=2)[0]
        self.polySoftEdge = mc.polySoftEdge(self.hairCard, ch=1, a=180)[0]
        mc.addAttr(self.pathCurve, ln="reverseNormals", dv=1, en="reverse:off:", at="enum", k=1)
        mc.addAttr(self.pathCurve, ln="surfaceNormals", dv=180, smx=180, at='double', min=-0, k=1)
        mc.connectAttr(self.pathCurve + ".reverseNormals", self.polyNormalNode + ".normalMode", f=1)
        mc.connectAttr(self.pathCurve + ".surfaceNormals", self.polySoftEdge + ".angle", f=1)

    def addUVs(self):
        self.polyFlipUV = mc.polyFlipUV(self.hairCard, ch=True, up=True, pu=0.5, pv=0.5)[0]
        self.polyMoveUV_root = mc.polyMoveUV(self.hairCard, ch=True, pvu=0.5, pvv=0)[0]
        self.polyMoveUV_mid = mc.polyMoveUV(self.hairCard, ch=True, pvu=0.5, pvv=0.5)[0]

        mc.setAttr(self.polyFlipUV + '.usePivot', 1)
        mc.setAttr(self.polyFlipUV + '.pivotU', 0.5)
        mc.setAttr(self.polyFlipUV + '.pivotV', 0.5)

        mc.addAttr(self.pathCurve, ln="flipUV", dv=1, en="flip:off:", at="enum", k=1)
        mc.addAttr(self.pathCurve, ln='moveU', smn=-1, dv=0, at='double', smx=1, k=1)
        mc.addAttr(self.pathCurve, ln='moveV', smn=-1, dv=0, at='double', smx=1, k=1)
        mc.addAttr(self.pathCurve, ln='rotateUV', smn=-360, dv=0, at='double', smx=360, k=1)
        mc.addAttr(self.pathCurve, ln='scaleU', smn=0, dv=1, at='double', smx=5, k=1)
        mc.addAttr(self.pathCurve, ln='scaleV', smn=0, dv=1, at='double', smx=5, k=1)

        uv_rotate = '''
        {1}.pivotU = ({0}.translateU + 0.5);
        {1}.pivotV = ({0}.translateV + 0.5);
        '''.format(self.polyMoveUV_root, self.polyMoveUV_mid)
        self.uvExpr = mc.expression(ae=0, n='UV_Rotation#', s=uv_rotate)

        mc.connectAttr(self.pathCurve + '.flipUV', self.polyFlipUV + '.nodeState', f=1)
        mc.connectAttr(self.pathCurve + '.moveU', self.polyMoveUV_root + '.translateU', f=1)
        mc.connectAttr(self.pathCurve + '.moveV', self.polyMoveUV_root + '.translateV', f=1)
        mc.connectAttr(self.pathCurve + '.rotateUV', self.polyMoveUV_mid + '.rotationAngle', f=1)
        mc.connectAttr(self.pathCurve + '.scaleU', self.polyMoveUV_root + '.scaleU', f=1)
        mc.connectAttr(self.pathCurve + '.scaleV', self.polyMoveUV_root + '.scaleV', f=1)

    def addSolidify(self):
        self.solidifyNode = mc.createNode('polyExtrudeFace')
        self.solidifyChoice = mc.createNode('choice')
        mc.addAttr(self.pathCurve, ln='solidify', dv=0, at='bool', k=1)
        mc.addAttr(self.pathCurve, ln='solidifyThickness', smn=0, dv=.25, at='double', smx=10, k=1)
        mc.addAttr(self.pathCurve, ln='solidifyDivisions', smn=0, dv=0, at='long', smx=10, k=1)
        mc.addAttr(self.pathCurve, ln='solidifyScaleX', smn=-10, dv=1, at='double', smx=10, k=1)
        mc.addAttr(self.pathCurve, ln='solidifyScaleY', smn=-10, dv=1, at='double', smx=10, k=1)
        mc.addAttr(self.pathCurve, ln='solidifyOffset', smn=-10, dv=0, at='double', smx=10, k=1)
        mc.addAttr(self.pathCurve, ln='solidifyNormals', smn=0, dv=30, at='double', smx=180, k=1)
        mc.setAttr(self.solidifyNode + '.inputComponents', 1, 'f[*]', type='componentList')
        mc.connectAttr(self.hairCard + '.worldMatrix[0]', self.solidifyNode + '.manipMatrix', f=1)
        mc.connectAttr(self.polyMoveUV_mid + '.output', self.solidifyChoice + '.input[0]', f=1)
        mc.connectAttr(self.polyMoveUV_mid + '.output', self.solidifyNode + '.inputPolymesh', f=1)
        mc.connectAttr(self.solidifyNode + '.output', self.solidifyChoice + '.input[1]', f=1)
        mc.connectAttr(self.solidifyChoice + '.output', self.hairCard + '.inMesh', f=1)
        mc.connectAttr(self.pathCurve + '.solidify', self.solidifyChoice + '.selector', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyThickness', self.solidifyNode + '.localTranslateZ', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyDivisions', self.solidifyNode + '.divisions', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyScaleX', self.solidifyNode + '.localScaleX', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyScaleY', self.solidifyNode + '.localScaleY', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyOffset', self.solidifyNode + '.offset', f=1)
        mc.connectAttr(self.pathCurve + '.solidifyNormals', self.solidifyNode + '.smoothingAngle', f=1)

    def addMessage(self):
        if not mc.attributeQuery('gsmessage', n=self.pathCurve, ex=1):
            mc.addAttr(self.pathCurve, ln='gsmessage', at='message', k=0)

    def hideNodes(self):
        nodes = [
            self.nurbsTesselate,
            self.curveWarp,
            self.polyFlipUV,
            self.polyMoveUV_mid,
            self.polyMoveUV_tip,
            self.polyMoveUV_root,
            self.solidifyNode,
            self.solidifyChoice,
            self.extrude,
            self.magnExpr,
            self.scaleExpr,
            self.uvExpr,
            self.rebuildCurve,
            self.polyNormalNode,
            self.polySoftEdge,
            self.lattice,
            self.twist,
            self.curveInfoNode,
            self.dynamicDivisionsCalculate,
            self.autoRefineCalculate,
        ]
        assetList = []
        for node in nodes:
            if node:
                if isinstance(node, list):
                    for n in node:
                        if mc.objExists(n):
                            assetList.append(n)
                            mc.setAttr(n + '.isHistoricallyInteresting', 0)
                else:
                    if mc.objExists(node):
                        assetList.append(node)
                        mc.setAttr(node + '.isHistoricallyInteresting', 0)

    def setCurveThickness(self):
        shape = mc.ls(self.pathCurve, dag=1, s=1, l=1)[0]
        mc.setAttr(shape + '.lineWidth', self.globalThickness)

    def addScaleFactor(self):
        # Delete the attribute if saving is not checked
        if not WIDGETS['keepCurveAttributes'].isChecked():
            if mc.attributeQuery('scaleFactor', n=self.pathCurve, ex=1):
                mc.deleteAttr(self.pathCurve + '.scaleFactor')
        # Add the attribute
        if not mc.attributeQuery('scaleFactor', n=self.pathCurve, ex=1):
            mc.addAttr(self.pathCurve, ln='scaleFactor', at='double', dv=self.sf)
            mc.setAttr(self.pathCurve + '.scaleFactor', self.sf)

    def addDynamicDivisions(self, curve=None, tesselateNode=None):
        if not curve:
            curve = self.pathCurve
        if not tesselateNode:
            tesselateNode = self.nurbsTesselate
        curveShape = mc.listRelatives(curve, c=1, typ='nurbsCurve')
        if not curveShape:
            return
        curveShape = curveShape[0]
        self.curveInfoNode = mc.createNode('curveInfo', n='dynamicDivisionsInfo#', ss=1)
        mc.connectAttr(curveShape + '.worldSpace[0]', self.curveInfoNode + '.inputCurve', f=1)
        if not mc.attributeQuery('dynamicDivisions', n=curve, ex=1):
            mc.addAttr(curve, ln='dynamicDivisions', dv=0, at='bool', k=1)
        mc.disconnectAttr(curve + '.lengthDivisions', tesselateNode + '.vNumber')

        if not mc.attributeQuery('scaleFactor', n=curve, ex=1):
            mc.addAttr(curve, ln='scaleFactor', at='double', dv=self.sf)

        if not mc.attributeQuery('dynamicDivMult', n=curve, ex=1): # NOTE: In case we need this in the future
            mc.addAttr(curve, ln='dynamicDivMult', at='double', dv=1.0, min=0.01, max=1000, k=1)

        expr = '''
        if ({2}.dynamicDivisions)
        {{
            {0}.vNumber = {1}.arcLength * {2}.lengthDivisions * 0.05 * {2}.dynamicDivMult / {2}.scaleFactor;
        }}
        else
        {{
            {0}.vNumber = {2}.lengthDivisions;
        }}
        '''.format(tesselateNode, self.curveInfoNode, curve)
        self.dynamicDivisionsCalculate = mc.expression(ae=0, s=expr, n='dynamicDivisionsCalculate#')

    def addAutoRefine(self, curve=None, rebuildCurve=None):
        """Add automatic rebuild value calculation to existing curveRebuild node"""
        useAutoRefine = True
        if not curve:
            curve = self.pathCurve
            useAutoRefine = mc.optionVar(q="GSCT_useAutoRefineOnNewCurves")
        if not rebuildCurve:
            rebuildCurve = self.rebuildCurve
            useAutoRefine = mc.optionVar(q="GSCT_useAutoRefineOnNewCurves")

        if not mc.attributeQuery('autoRefine', n=curve, ex=1):
            mc.addAttr(curve, ln='autoRefine', dv=useAutoRefine, at='bool', k=1)

        # Check if curveRefine connection is correct
        curveRefineTarget = mc.listConnections(curve + '.curveRefine')
        for node in curveRefineTarget:
            if mc.nodeType(node) == "expression":
                continue
            else:
                mc.disconnectAttr(curve + '.curveRefine', node + '.spans')

        expr = '''
        if ({0}.autoRefine)
        {{
            {1}.keepControlPoints = 1;
        }}
        else
        {{
            {1}.keepControlPoints = 0;
            {1}.spans = {0}.curveRefine;
        }}
        '''.format(curve, rebuildCurve)
        self.autoRefineCalculate = mc.expression(ae=0, s=expr, n='autoRebuildCalculate#')
        return self.autoRefineCalculate

    def clearTweakNode(self):  # TODO: Check if this fix is needed
        pass
        # Possible fix for older Maya versions tweak node issue
        # try:
        #     tweakNode = mc.listConnections(self.hairCard + '.tweakLocation')
        #     if tweakNode:
        #         mc.delete(tweakNode)
        # except:
        #     pass

    def group(self, grpName, fake=False):
        constructionGrp = None
        if fake:
            constructionGrp = mc.createNode('transform', n='instances#')
            self.hairCard = self.geo
        elif self.lattice:
            constructionGrp = mc.group(self.pathInst, self.profileInst, self.lattice, self.twist, n='instances#')
        else:
            constructionGrp = mc.group(self.pathInst, self.profileInst, n='instances#')
        mc.setAttr(constructionGrp + '.inheritsTransform', 0)
        mc.setAttr(constructionGrp + '.tx', lock=True)
        mc.setAttr(constructionGrp + '.ty', lock=True)
        mc.setAttr(constructionGrp + '.tz', lock=True)
        mc.setAttr(constructionGrp + '.rx', lock=True)
        mc.setAttr(constructionGrp + '.ry', lock=True)
        mc.setAttr(constructionGrp + '.rz', lock=True)
        mc.setAttr(constructionGrp + '.sx', lock=True)
        mc.setAttr(constructionGrp + '.sy', lock=True)
        mc.setAttr(constructionGrp + '.sz', lock=True)

        # Layers
        hairGrp = self.currentLayerInd()
        curveGrp, geoGrp, instGrp = utils.getFormattedLayerNames(self.collectionID, hairGrp)

        if mc.objExists(instGrp) != 1:
            utils.createNewDisplayLayer(name=instGrp, objects=constructionGrp)
            mc.setAttr(instGrp + '.displayType', 2)
            mc.setAttr(instGrp + '.visibility', 0)
        else:
            mc.editDisplayLayerMembers((instGrp), constructionGrp, nr=1)
            mc.setAttr(instGrp + '.displayType', 2)
            mc.setAttr(instGrp + '.visibility', 0)

        if mc.objExists(geoGrp) != 1:
            utils.createNewDisplayLayer(name=geoGrp, objects=self.hairCard)
            mc.setAttr(geoGrp + '.displayType', 2)
        else:
            mc.editDisplayLayerMembers(geoGrp, self.hairCard, nr=1)

        if mc.objExists(curveGrp) != 1:
            utils.createNewDisplayLayer(name=curveGrp, objects=self.pathCurve)
        else:
            mc.editDisplayLayerMembers(curveGrp, self.pathCurve, nr=1)

        layerCollections.updateDefaultLayerNode()
        layerCollections.updateCollectionNames()

        # Final Group Lock
        self.hairCardGrp = str(mc.group(self.pathCurve, constructionGrp, self.hairCard, n=grpName))
        mc.setAttr(self.hairCardGrp + '|' + self.hairCard + '.inheritsTransform', 1)  # TODO: Why do we need this?
        mc.setAttr(self.hairCardGrp + '.inheritsTransform', 0)  # TODO: Check if this breaks anything
        mc.setAttr(self.hairCardGrp + '.tx', lock=True)
        mc.setAttr(self.hairCardGrp + '.ty', lock=True)
        mc.setAttr(self.hairCardGrp + '.tz', lock=True)
        mc.setAttr(self.hairCardGrp + '.rx', lock=True)
        mc.setAttr(self.hairCardGrp + '.ry', lock=True)
        mc.setAttr(self.hairCardGrp + '.rz', lock=True)
        mc.setAttr(self.hairCardGrp + '.sx', lock=True)
        mc.setAttr(self.hairCardGrp + '.sy', lock=True)
        mc.setAttr(self.hairCardGrp + '.sz', lock=True)


create = Create("create")


class Sliders:

    def __init__(self, name):
        self.name = name
        self.icons = utils.getFolder.icons()
        self.timer = utils.Timer()
        self.widthLock = False
        self.rebuildDupTrans = list()
        self.rebuildDupShape = list()
        self.rebuildCurveNode = list()
        self.rebuildTargetNode = list()
        self.lastCV = list()
        self.curveRepeat = int()
        self.curveTrigger = int()
        self.sliderCheck = int()
        self.curveCVsName = list()
        self.curveCVs = list()
        self.curveRotate = list()
        self.curveOrientation = list()
        self.curveTwist = list()
        self.curveWidth = list()
        self.curveWidthX = list()
        self.curveWidthZ = list()
        self.curveTaper = list()
        self.curveProfile = list()
        self.curveRandDragSelList = []

    def release(self, *_):  # Close undo chunk on release
        mc.undoInfo(cck=1)
        self.sliderCheck = 0

    def selectCVSlider(self, sliderValue):  # Select CV Slider
        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='gsCVSlider')
            self.sliderCheck = 1
        sel = mc.filterExpand(mc.ls(sl=1, o=1, fl=1, dag=1, s=1), sm=9)
        if not sel:
            sel = mc.filterExpand(mc.ls(hl=1, o=1, fl=1, dag=1, s=1), sm=9)
        if not sel:
            return
        modifier = utils.getMod()
        selectionList = []
        for curve in sel:
            shape = mc.listRelatives(curve, c=1, pa=1, ni=1, s=1, typ='nurbsCurve')
            if not shape:
                continue
            shape = shape[0]
            numCVs = mc.getAttr(shape + '.controlPoints', s=1)
            position = math.floor(numCVs * sliderValue)
            selectionList.append("{}.cv[{}]".format(shape, position))
        if modifier == "Ctrl":
            return
        if modifier == "Alt" or modifier == "Shift+Alt":
            if len(mc.ls(sl=1, fl=1)) <= len(sel):
                return
            mc.select(selectionList, d=1)
        elif modifier == "Shift":
            mc.select(selectionList, add=1)
        else:
            mc.select(selectionList, r=1)

    def rebuildSliderDrag(self, *_):  # Rebuild curve drag command # BUG: Rebuilding to small values can break advanced visibility curve drawing
        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='gsRebuildSlider')
            self.sliderCheck = 1
        slider = mc.intSliderGrp('gsRebuildSlider', q=1, v=1)
        sel = mc.filterExpand(mc.ls(sl=1, o=1, fl=1), sm=9)
        if not sel:
            sel = mc.filterExpand(mc.ls(hl=1, o=1, fl=1), sm=9)
        if not sel:
            return 0
        j = int()
        sha = mc.ls(sel, dag=1, s=1)
        for obj in sha:
            inputPlug = mc.listConnections(obj + '.create', d=0, s=1, p=1)
            if inputPlug:  # Rebuild Algorithm if rebuildCurve node is detected
                if len(self.rebuildDupTrans) <= j or not mc.objExists(self.rebuildDupTrans[j]):
                    target = mc.listConnections(obj + '.worldSpace[1]', d=1, s=0, p=1)
                    nurbsCurve = mc.createNode('nurbsCurve', n='gsTempCurve')
                    mc.setAttr(nurbsCurve + '.dispCV', 1)
                    nurbsCurveTransform = mc.listRelatives(nurbsCurve, p=1, pa=1)
                    mc.setAttr(nurbsCurveTransform[0] + '.hiddenInOutliner', 1)
                    mc.matchTransform(nurbsCurveTransform[0], mc.listRelatives(obj, p=1, pa=1)[0])
                    rebuildCurve = mc.createNode('rebuildCurve')
                    mc.connectAttr(obj + ".worldSpace[1]", rebuildCurve + ".inputCurve", f=1)
                    mc.connectAttr(rebuildCurve + ".outputCurve", nurbsCurve + ".create", f=1)
                    mc.connectAttr(nurbsCurve + '.local', target[0], f=1)
                    utils.addAtIndex(self.rebuildDupTrans, j, nurbsCurveTransform[0])
                    utils.addAtIndex(self.rebuildDupShape, j, nurbsCurve)
                    utils.addAtIndex(self.rebuildCurveNode, j, rebuildCurve)
                    utils.addAtIndex(self.rebuildTargetNode, j, target[0])
                    j += 1
            else:  # Rebuild Algorithm if rebuildCurve node is not detected
                if len(self.rebuildDupTrans) <= j or not mc.objExists(self.rebuildDupTrans[j]):
                    tra = mc.duplicate(obj, rc=1)
                    shp = mc.listRelatives(tra[0], c=1, pa=1)
                    rebuildCurve = mc.createNode('rebuildCurve')
                    mc.setAttr(rebuildCurve + '.keepRange', 1)
                    mc.setAttr(tra[0] + '.hiddenInOutliner', 1)
                    mc.setAttr(rebuildCurve + '.spans', (mc.getAttr(obj + '.spans')))
                    mc.setAttr(rebuildCurve + '.degree', (mc.getAttr(obj + '.degree')))
                    mc.connectAttr(shp[0] + '.worldSpace', rebuildCurve + '.inputCurve', f=1)
                    mc.connectAttr(rebuildCurve + '.outputCurve', obj + '.create', f=1)
                    utils.addAtIndex(self.rebuildDupTrans, j, tra[0])
                    utils.addAtIndex(self.rebuildDupShape, j, shp[0])
                    utils.addAtIndex(self.rebuildCurveNode, j, rebuildCurve)
                    j += 1
                mc.setAttr(obj + '.dispCV', 1)

        for node in self.rebuildCurveNode:
            mc.setAttr(node + '.spans', slider)
        # TODO: Add in v1.3 with different refine modes and auto refine values
        # for curve in sel:
        #     if mc.attributeQuery('curveRefine', n=curve, ex=1):
        #         mc.setAttr(curve + '.curveRefine', 20 if slider <= 20 else 0)
        mc.select(sel, r=1)
        mc.headsUpMessage('[%s]' % slider, s=1)

    def rebuildSliderRelease(self, *_):  # Rebuild curve slider release command
        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='gsRebuildSlider')
            self.sliderCheck = 1
        selTemp = mc.ls(sl=1, o=1, fl=1, dag=1, s=1)
        sel = list()
        for obj in selTemp:
            if utils.attrExists(obj, 'spans'):
                sel.append(obj)
        if len(sel) > 0:
            slider = mc.intSliderGrp('gsRebuildSlider', q=1, v=1)
            if len(self.rebuildDupTrans) == 0:
                for i in range(len(sel)):
                    inputPlug = mc.listConnections(sel[i] + '.create', d=0, s=1, p=1)
                    rebuildCurve = list()
                    if not inputPlug:
                        rebuildCurve = mc.rebuildCurve(sel[i], s=slider, ch=0, kr=1)
                    else:
                        rebuildCurve = mc.rebuildCurve(sel[i], s=slider, ch=1, kr=1)
                        newName = mc.rename(rebuildCurve[1], 'gsRebuildCurveNode#')
                        hist = mc.listHistory(newName)
                        for ele in hist:
                            if 'gsRebuildCurveNode' in ele and ele != newName:
                                mc.delete(ele)
                        mc.rename(newName, 'gsRebuildCurveNode1')
                mc.headsUpMessage('[%s]' % slider, s=1)
            else:
                try:
                    mc.delete(self.rebuildDupTrans)
                except BaseException:
                    pass
                try:
                    mc.delete(self.rebuildDupShape)
                except BaseException:
                    pass
        self.rebuildDupTrans *= 0
        self.rebuildDupShape *= 0
        self.rebuildCurveNode *= 0
        self.rebuildTargetNode *= 0

        for obj in sel:
            try:
                mc.setAttr(obj + '.dispCV', 0)
            except BaseException:
                pass
        mc.select(mc.listRelatives(sel, p=1, pa=1), r=1)

    def rebuildButtonClicked(self):
        self.rebuildSliderDrag()
        self.rebuildSliderRelease()
        self.release()

    def randSliderDrag(self, sldr, *_):
        """Randomize Curve sliders drag"""
        # BUG: Fix width and taper slider to be changed based on the original values, not on some arbitrary ones
        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='curveRandSlider')
            self.sliderCheck = 1
        sel = mc.filterExpand(mc.ls(sl=1, o=1, fl=1), sm=9)
        if not sel:
            sel = mc.filterExpand(mc.ls(hl=1, o=1, fl=1), sm=9)

        if not sel:
            return

        slid = list()
        vect = str()

        for i in range(8):
            slid.append(WIDGETS['curveRandomizeSlider' + str(i)].isChecked())

        if slid[0] == 1 and (sldr == 0 or sldr == -1):
            if self.curveRepeat == 1:
                for i in range(len(self.curveCVsName)):
                    vect = self.curveCVs[i]
                    mc.move(vect[0], vect[1], vect[2], self.curveCVsName[i], a=1)
            lockFirstCV = WIDGETS['gsLockFirstCV'].isChecked()
            lockLastCV = WIDGETS['gsLockLastCV'].isChecked()
            slider = mc.floatSliderGrp('gsCurveCVsRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveCVsRandMulti', q=1, v=1)
            value = slider * mult
            for obj in sel:
                ind = mc.getAttr(obj + '.cp', mi=1)
                CVs = list()
                for i in range(len(ind)):
                    CVs.append(str(obj) + '.cv[' + str(i) + ']')
                    if self.curveTrigger == 0:
                        pp = mc.pointPosition(obj + '.cp[' + str(i) + ']')
                        self.curveCVsName.append(CVs[i])
                        self.curveCVs.append([pp[0], pp[1], pp[2]])
                for i in range(len(CVs)):
                    if (i == 0 or i == 1) and lockFirstCV == 1:
                        continue
                    if i == len(CVs) - 1 and lockLastCV == 1:
                        continue
                    randX = random.uniform(value * -1, value)
                    randY = random.uniform(value * -1, value)
                    randZ = random.uniform(value * -1, value)
                    if not WIDGETS['gsRandAxisX'].isChecked():
                        randX = 0
                    if not WIDGETS['gsRandAxisY'].isChecked():
                        randY = 0
                    if not WIDGETS['gsRandAxisZ'].isChecked():
                        randZ = 0
                    mc.move(randX, randY, randZ, CVs[i], r=1, os=1, wd=1)

        if slid[1] == 1 and (sldr == 1 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveRotationRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveRotationRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if self.curveTrigger == 0:
                    rotX = mc.getAttr(sel[i] + '.rx')
                    rotY = mc.getAttr(sel[i] + '.ry')
                    rotZ = mc.getAttr(sel[i] + '.rz')
                    self.curveRotate.append([rotX, rotY, rotZ])
                if self.curveRepeat == 1:
                    rotate = self.curveRotate[i]
                    mc.setAttr(sel[i] + '.rx', rotate[0])
                    mc.setAttr(sel[i] + '.ry', rotate[1])
                    mc.setAttr(sel[i] + '.rz', rotate[2])
            for obj in sel:
                randX = random.uniform(value * -1, value)
                randY = random.uniform(value * -1, value)
                randZ = random.uniform(value * -1, value)
                if not WIDGETS['gsRandRotateAxisX'].isChecked():
                    randX = 0
                if not WIDGETS['gsRandRotateAxisY'].isChecked():
                    randY = 0
                if not WIDGETS['gsRandRotateAxisZ'].isChecked():
                    randZ = 0
                mc.rotate(randX, randY, randZ, obj, r=1, os=1, fo=1)

        if slid[2] == 1 and (sldr == 2 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveOrientationRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveOrientationRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if self.curveTrigger == 0:
                    self.curveOrientation.append(mc.getAttr(sel[i] + '.Orientation'))
                if self.curveRepeat == 1:
                    mc.setAttr(sel[i] + '.Orientation', self.curveOrientation[i])
            for obj in sel:
                rand = random.uniform(value * -1, value)
                mc.setAttr(obj + '.Orientation', rand)

        if slid[3] == 1 and (sldr == 3 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveTwistRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveTwistRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if self.curveTrigger == 0:
                    self.curveTwist.append(mc.getAttr(sel[i] + '.Twist'))
                if self.curveRepeat == 1:
                    mc.setAttr(sel[i] + '.Twist', self.curveTwist[i])
            for obj in sel:
                rand = random.uniform(value * -1, value)
                mc.setAttr(obj + '.Twist', rand)

        if slid[4] == 1 and (sldr == 4 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveWidthRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveWidthRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if self.curveTrigger == 0:
                    if mc.attributeQuery('Width', n=sel[i], ex=1):
                        self.curveWidth.append(mc.getAttr(sel[i] + '.Width'))
                    else:
                        self.curveWidthX.append(mc.getAttr(sel[i] + '.WidthX'))
                        self.curveWidthZ.append(mc.getAttr(sel[i] + '.WidthZ'))
                if self.curveRepeat == 1:
                    if mc.attributeQuery('Width', n=sel[i], ex=1):
                        mc.setAttr(sel[i] + '.Width', self.curveWidth[i])
                    else:
                        mc.setAttr(sel[i] + '.WidthX', self.curveWidthX[i])
                        mc.setAttr(sel[i] + '.WidthZ', self.curveWidthZ[i])
                rand = random.uniform(0.001, value)
                if mc.attributeQuery('Width', n=sel[i], ex=1):
                    mc.setAttr(sel[i] + '.Width', rand)
                else:
                    mc.setAttr(sel[i] + '.WidthX', rand)
                    if not WIDGETS['gsWidthCheckBoxUniform'].isChecked():
                        rand = random.uniform(0.001, value)
                    mc.setAttr(sel[i] + '.WidthZ', rand)

        if slid[5] == 1 and (sldr == 5 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveTaperRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveTaperRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if self.curveTrigger == 0:
                    self.curveTaper.append(mc.getAttr(sel[i] + '.Taper'))
                if self.curveRepeat == 1:
                    mc.setAttr(sel[i] + '.Taper', self.curveTaper[i])
                rand = random.uniform(0, value)
                mc.setAttr(sel[i] + '.Taper', rand)

        if slid[6] == 1 and (sldr == 6 or sldr == -1):
            slider = mc.floatSliderGrp('gsCurveProfileRand', q=1, v=1)
            mult = mc.floatSliderGrp('gsCurveProfileRandMulti', q=1, v=1)
            value = slider * mult
            for i in range(len(sel)):
                if mc.attributeQuery('Profile', n=sel[i], ex=1):
                    if self.curveTrigger == 0:
                        self.curveProfile.append(mc.getAttr(sel[i] + '.Profile'))
                    if self.curveRepeat == 1:
                        mc.setAttr(sel[i] + '.Profile', self.curveProfile[i])
                    rand = random.uniform(0, value)
                    if WIDGETS['gsProfileCheckBoxNegative'].isChecked():
                        rand = random.uniform(value * -1, value)
                    mc.setAttr(sel[i] + '.Profile', rand)

        if slid[7] == 1 and (sldr == 7 or sldr == -1):
            if not self.curveRandDragSelList:
                self.curveRandDragSelList = sel
            if self.timer.increment(1.0 / 60.0):
                sliderVal = math.ceil(mc.floatSliderGrp('gsCurveSelectRand', q=1, v=1) * len(self.curveRandDragSelList))
                shuffledList = self.curveRandDragSelList
                random.shuffle(shuffledList)
                newSel = []
                for i in range(sliderVal):
                    newSel.append(shuffledList[i])
                if not newSel:
                    mc.select(self.curveRandDragSelList, r=1)
                else:
                    mc.select(newSel, r=1)

        self.curveRepeat = 1
        self.curveTrigger = 1

    def randSliderRelease(self, sldr, *_):  # Randomize Curve slider release
        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='curveRandSlider')
            self.sliderCheck = 1
        sel = mc.ls(sl=1, fl=1, o=1)
        slid = list()
        for i in range(8):
            slid.append(WIDGETS['curveRandomizeSlider' + str(i)].isChecked())

        if slid[0] == 1 and sldr == 0:
            for i in range(len(self.curveCVsName)):
                vect = self.curveCVs[i]
                mc.move(vect[0], vect[1], vect[2], self.curveCVsName[i], a=1)

        if slid[1] == 1 and sldr == 1:
            for i in range(len(sel)):
                rotate = self.curveRotate[i]
                mc.setAttr(sel[i] + ".rx", rotate[0])
                mc.setAttr(sel[i] + ".ry", rotate[1])
                mc.setAttr(sel[i] + ".rz", rotate[2])

        if slid[2] == 1 and sldr == 2:
            for i in range(len(sel)):
                mc.setAttr(sel[i] + '.Orientation', self.curveOrientation[i])

        if slid[3] == 1 and sldr == 3:
            for i in range(len(self.curveTwist)):
                mc.setAttr(sel[i] + '.Twist', self.curveTwist[i])

        if slid[4] == 1 and sldr == 4:
            for i in range(len(sel)):
                if mc.attributeQuery('Width', n=sel[i], ex=1):
                    mc.setAttr(sel[i] + '.Width', self.curveWidth[i])
                else:
                    mc.setAttr(sel[i] + '.WidthX', self.curveWidthX[i])
                    mc.setAttr(sel[i] + '.WidthZ', self.curveWidthZ[i])

        if slid[5] == 1 and sldr == 5:
            for i in range(len(self.curveTaper)):
                mc.setAttr(sel[i] + '.Taper', self.curveTaper[i])

        if slid[6] == 1 and sldr == 6:
            for i in range(len(self.curveProfile)):
                mc.setAttr(sel[i] + '.Profile', self.curveProfile[i])

        if slid[7] == 1 and sldr == 7:
            if self.curveRandDragSelList:
                mc.select(self.curveRandDragSelList, r=1)

        self.curveCVs *= 0
        self.curveCVsName *= 0
        self.curveRotate *= 0
        self.curveOrientation *= 0
        self.curveTwist *= 0
        self.curveWidth *= 0
        self.curveWidthX *= 0
        self.curveWidthZ *= 0
        self.curveTaper *= 0
        self.curveProfile *= 0
        self.curveRandDragSelList *= 0
        self.curveTrigger = 0
        self.curveRepeat = 0

    def curveControlSliderDrag(self, sldr, *_):  # Curve Control slider drag

        if self.sliderCheck == 0:
            mc.undoInfo(ock=1, cn='curveControlSlider')
            self.sliderCheck = 1

        sel = mc.ls(sl=1, dag=1, tr=1)
        if not sel:
            sel = mc.listRelatives(mc.ls(sl=1, o=1), p=1, pa=1)

        if not sel:
            return 0

        sel = list(dict.fromkeys(sel))

        if not self.timer.increment(1.0 / 30.0) and len(sel) > 10:
            return 0

        attr = sldr.getAttributeName()
        value = sldr.getValue()

        for obj in sel:
            lengthDivisoinsAttribute = mc.attributeQuery('lengthDivisions', n=obj, ex=1)
            lengthAttribute = mc.attributeQuery('Length', n=obj, ex=1)
            if not lengthDivisoinsAttribute and not lengthAttribute:
                continue

            if attr == 'lineWidth':
                mc.setAttr(mc.ls(obj, dag=1, s=1)[0] + '.lineWidth', value)
                continue

            if attr == 'WidthX' and WIDGETS['widthLockSwitch'].isChecked():
                try:
                    mc.setAttr(obj + '.' + 'WidthX', value)
                    mc.setAttr(obj + '.' + 'WidthZ', value)
                    WIDGETS['WidthZ'].setValue(value)
                    continue
                except BaseException:
                    continue
            if attr == 'WidthZ' and WIDGETS['widthLockSwitch'].isChecked():
                try:
                    mc.setAttr(obj + '.' + 'WidthX', value)
                    mc.setAttr(obj + '.' + 'WidthZ', value)
                    WIDGETS['WidthX'].setValue(value)
                    continue
                except BaseException:
                    continue

            if mc.attributeQuery(attr, n=obj, ex=1):
                try:
                    mc.setAttr(obj + '.' + attr, value)
                except BaseException:
                    pass

    def curveHighlightSliderDrag(self):
        pass


sliders = Sliders("sliders")


class ToggleColor:

    COLOR_RANGE = (0.1, 1)
    STORAGE_NODE = 'gsColorShaderStorageNode'

    def __init__(self, name):
        self.name = name

    # IO
    def writeColorDict(self, colorDict):
        """Writes a color dict to color storage node"""
        self.checkColorStorageNode()
        mc.setAttr(self.STORAGE_NODE + '.layerColor', str(colorDict), typ='string')

    def readColorDict(self):
        """Reads a color dict from color storage node"""
        self.checkColorStorageNode()
        dictString = mc.getAttr(self.STORAGE_NODE + '.layerColor')
        return eval(dictString)

    def colorEnabled(self):
        # type: () -> bool
        """Is color enabled?"""
        self.checkColorStorageNode()
        return bool(mc.getAttr(self.STORAGE_NODE + '.colorApplied'))

    # Check nodes, materials and attributes

    def checkColorStorageNode(self):
        """Checks if color storage node exists (and has default values)"""
        # Create storage node if not found
        if not mc.objExists(self.STORAGE_NODE):
            mc.scriptNode(n=self.STORAGE_NODE)

        # Add colorApplied attribute if not found
        if not mc.attributeQuery('colorApplied', n=self.STORAGE_NODE, ex=1):
            mc.addAttr(self.STORAGE_NODE, ln='colorApplied', at='bool')
            mc.setAttr(self.STORAGE_NODE + '.colorApplied', False)

        # Add layerColor attribute if not found
        if not mc.attributeQuery('layerColor', n=self.STORAGE_NODE, ex=1):
            mc.addAttr(self.STORAGE_NODE, ln='layerColor', dt='string')
            mc.setAttr(self.STORAGE_NODE + '.layerColor',
                       str({k: self.generateBrightColor() for k in range(80)}), typ='string')
        else:
            colorDict = eval(mc.getAttr(self.STORAGE_NODE + '.layerColor'))
            if len(colorDict) < 80:
                mc.setAttr(self.STORAGE_NODE + '.layerColor',
                           str({k: self.generateBrightColor() for k in range(80)}), typ='string')

        # Add layerName attribute if not found
        if not mc.attributeQuery('layerName', n=self.STORAGE_NODE, ex=1):
            mc.addAttr(self.STORAGE_NODE, ln='layerName', dt='string')
            mc.setAttr(self.STORAGE_NODE + '.layerName', str({k: "" for k in range(80)}), typ='string')
        else:
            if mc.objExists(self.STORAGE_NODE):
                storageNode = mc.getAttr(self.STORAGE_NODE + '.layerName')
                if storageNode:
                    layerNames = eval(storageNode)
                    if len(layerNames) < 80:
                        mc.setAttr(self.STORAGE_NODE + '.layerName', str({k: "" for k in range(80)}), typ='string')

    # Material creation utils
    def getNodeNamesDict(self, layerName):
        """Returns a dict with formatted material node names
        Valid keys: 'engine', 'shader', 'switch', 'checker', 'tiling' """
        namesDict = {n: 'GSCTMAT_{}_{}'.format(layerName, n) for n in
                     ['engine', 'shader', 'switchChecker', 'switchDiffuse', 'switchAlpha', 'checker', 'tiling', 'color']}
        return namesDict

    def deleteColorMaterial(self, layerName):
        """Deletes the named material and all the appropriate nodes"""
        nodes = self.getNodeNamesDict(layerName)
        for node in nodes:
            if mc.objExists(nodes[node]):
                mc.delete(nodes[node])

    def createColorMaterial(self, variantName, originalLayerName=None):
        """Creates a single color material network based on the layerName name"""
        nodes = self.getNodeNamesDict(variantName)
        if not originalLayerName:
            originalLayerName = variantName
        self.deleteColorMaterial(variantName)  # Just in case
        # Create all the nodes mc.shadingNode('place2dTexture', au=1, n=place2d, ss=1)
        shader = mc.shadingNode('lambert', n=nodes['shader'], ss=1, asShader=1)
        engine = mc.sets(r=1, nss=1, em=1, n=nodes['engine'])
        switchChecker = mc.shadingNode('condition', n=nodes['switchChecker'], ss=1, au=1)
        switchDiffuse = mc.shadingNode('condition', n=nodes['switchDiffuse'], ss=1, au=1)
        switchAlpha = mc.shadingNode('condition', n=nodes['switchAlpha'], ss=1, au=1)
        checker = mc.shadingNode('checker', n=nodes['checker'], ss=1, at=1)
        tiling = mc.shadingNode('place2dTexture', n=nodes['tiling'], ss=1, au=1)
        color = mc.shadingNode('colorConstant', n=nodes['color'], ss=1, at=1)
        # Set default attributes
        mc.setAttr(tiling + '.repeatUV', 10, 10, typ='float2')
        mc.setAttr(shader + '.diffuse', 1)
        mc.setAttr(color + '.inColor', random.random(), random.random(), random.random(), typ='double3')
        mc.setAttr(switchAlpha + '.colorIfFalse', 0, 0, 0, typ='float3')
        # Connect stuff together
        mc.connectAttr(tiling + '.outUV', checker + '.uvCoord', f=1)
        mc.connectAttr(tiling + '.outUvFilterSize', checker + '.uvFilterSize', f=1)
        mc.connectAttr(checker + '.outColor', switchChecker + '.colorIfTrue', f=1)
        mc.connectAttr(switchChecker + '.outColor', switchDiffuse + '.colorIfTrue')
        mc.connectAttr(switchDiffuse + '.outColor', shader + '.color', f=1)
        mc.connectAttr(shader + '.outColor', engine + '.surfaceShader', f=1)
        mc.connectAttr(color + '.outColor', checker + '.color1', f=1)
        mc.connectAttr(color + '.outColor', switchChecker + '.colorIfFalse', f=1)
        mc.connectAttr(originalLayerName + '.overrideColorRGB', color + '.inColor')
        mc.connectAttr(switchAlpha + '.outColor', shader + '.transparency')
        # Create messages
        mc.addAttr(engine, ln='gs_shadermessage', at='message')
        return engine

    def checkColorMaterial(self, variantName, originalLayerName=None):
        """
        Checks if appropriately named material exists for the layer.\n
        Also check if material has all the nodes it needs.
        """
        if not originalLayerName:
            originalLayerName = variantName
        nodesDict = self.getNodeNamesDict(variantName)
        if not mc.objExists(nodesDict['engine']):
            # Create from scratch
            self.deleteColorMaterial(variantName)
            self.createColorMaterial(variantName, originalLayerName)
        else:
            # Check if not corrupted
            for node in nodesDict:
                if not mc.objExists(nodesDict[node]):
                    self.deleteColorMaterial(variantName)
                    self.createColorMaterial(variantName, originalLayerName)
                    break
        return nodesDict['engine']

    # Main methods
    def toggleColorVis(self):
        """Toggle colors on Color button click or hotkey"""
        self.checkColorStorageNode()
        if not mc.getAttr(self.STORAGE_NODE + '.colorApplied'):
            currentViewport = mc.playblast(ae=1)
            if currentViewport:
                mc.modelEditor(currentViewport, e=1, displayTextures=1)
            self.enableColors()
        else:
            self.disableColors()
        utils.deferredLp(utils.noUndo(updateMainUI))()  # TODO: Check if this breaks anything (mostly UNDO)

    def onLayerChange(self, curves, targetLayer):
        """Called when curve is moved from layer to layer"""
        if WIDGETS['colorMode'].isChecked():
            geo = selectPart(2, True, curves)
            shadersDict = utils.getShader(geo)
            # Set geometry to original material
            for shader in shadersDict:
                originalShader = mc.listConnections(shader + '.gs_shadermessage')
                if originalShader:
                    mc.sets(shadersDict[shader], e=1, fe=originalShader[0])
                else:
                    mc.sets(shadersDict[shader], e=1, fe='initialShadingGroup')
            # Disable/Enable target layer
            self.disableColors(targetLayer)
            self.enableColors(targetLayer)

    def updateColors(self):
        """
        Update the colors on cards if color mode is on. Runs every time selection changes.\n
        NOTE: Should be as fast as possible
        """
        if not WIDGETS['colorMode'].isChecked():
            return
        allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Geo' in x)]
        # Update colors
        self.checkColorStorageNode()
        colorDict = self.readColorDict()
        for layer in allLayers:
            split = layer.split('_')
            try:
                layerID = int(split[1]) if len(split) == 3 else int(split[2])
            except ValueError:
                error = 'Failed to extract layer ID from layer "{}". Display Layer name is corrupted. Please delete corrupted layers and curves.'.format(layer)
                MESSAGE.warning(error)
                continue
            r, g, b = colorDict[layerID]
            mc.setAttr(layer + '.overrideColorRGB', r, g, b)

    def updateColorOptions(self):
        """Triggered when there is need to change checkered or alpha options"""
        if not WIDGETS['colorMode'].isChecked():
            return
        allMaterialNodes = [x for x in mc.ls() if 'GSCTMAT_' in x]
        isChecker = getOption('checkerPattern')
        isDiffuseOnly = getOption('colorOnlyDiffuse')
        switchNodes = [x for x in allMaterialNodes if '_switchChecker' in x]
        for node in switchNodes:
            mc.setAttr(node + '.firstTerm', int(not isChecker))
        switchNodes = [x for x in allMaterialNodes if '_switchAlpha' in x]
        for node in switchNodes:
            mc.setAttr(node + '.firstTerm', int(not isDiffuseOnly))

    def enableColors(self, oneLayer=None):
        """Enable colors on layers"""
        allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Geo' in x)]
        colorDict = self.readColorDict()
        isChecker = getOption('checkerPattern')
        isDiffuseOnly = getOption('colorOnlyDiffuse')
        if oneLayer:
            allLayers = [oneLayer]
        for layer in allLayers:
            # Get layer ID
            split = layer.split('_')
            try:
                layerID = int(split[1]) if len(split) == 3 else int(split[2])
            except ValueError:
                error = 'Failed to extract layer ID from layer "{}". Display Layer name is corrupted. Please delete corrupted layers and curves.'.format(layer)
                MESSAGE.warning(error)
                continue
            # Get layer colors and set them
            r, g, b = colorDict[layerID]
            mc.setAttr(layer + '.overrideColorRGB', r, g, b)
            # Get all the shaders for geometry in the layer
            layerGeo = mc.editDisplayLayerMembers(layer, q=1, fn=1, nr=1)
            shaders = utils.getShader(layerGeo)
            count = 0
            for shader in shaders:
                # Modify name if there are multiple materials used in one layer
                variantName = layer
                if len(shaders) > 1:
                    variantName = variantName + "_variant{}".format(count)
                    count += 1
                engine = self.checkColorMaterial(variantName, layer)
                # Create and connect shadermessage
                utils.connectMessage(engine, shader, 'gs_shadermessage')
                # Find alpha and color node in the original shader graph and apply it to new color material
                namesDict = self.getNodeNamesDict(variantName)
                colorNode = None
                alphaNode = None
                network = mc.hyperShade(lun=shader)
                for node in network:
                    if mc.nodeType(node) == 'file' and mc.connectionInfo(node + '.outColor', isSource=1):
                        colorNode = node
                        break
                for node in network:
                    if mc.nodeType(node) == 'file' and mc.connectionInfo(node + '.outTransparency', isSource=1):
                        alphaNode = node
                        break
                if colorNode:  # Just to enable UV editor functionality
                    mc.connectAttr(colorNode + '.outColor', namesDict['switchDiffuse'] + '.colorIfFalse', f=1)
                if alphaNode:  # To have transparency with solid color
                    mc.connectAttr(alphaNode + '.outTransparency', namesDict['switchAlpha'] + '.colorIfTrue', f=1)
                # Apply material
                mc.sets(shaders[shader], e=1, fe=engine, nw=1)
                # Options
                if isChecker:
                    mc.setAttr(namesDict['switchChecker'] + '.firstTerm', 0)
                else:
                    mc.setAttr(namesDict['switchChecker'] + '.firstTerm', 1)
                if isDiffuseOnly:
                    mc.setAttr(namesDict['switchAlpha'] + '.firstTerm', 0)
                else:
                    mc.setAttr(namesDict['switchAlpha'] + '.firstTerm', 1)
        mc.setAttr(self.STORAGE_NODE + '.colorApplied', 1)

    def disableColors(self, oneLayer=None):
        """Disable colors on layers"""
        allColorMaterials = [x for x in mc.ls() if 'GSCTMAT_' in x]
        allEngines = [x for x in allColorMaterials if '_engine' in x]
        for engine in allEngines:
            if oneLayer and oneLayer not in engine:
                continue
            originalGeo = mc.listConnections(engine + '.dagSetMembers')
            if mc.attributeQuery('gs_shadermessage', n=engine, ex=1):
                originalShader = mc.listConnections(engine + '.gs_shadermessage')
                if originalShader:
                    mc.sets(originalGeo, e=1, fe=originalShader[0], nw=1)
                    continue
            mc.sets(originalGeo, e=1, fe='initialShadingGroup', nw=1)
        for node in allColorMaterials:
            if oneLayer and oneLayer not in node:
                continue
            if mc.objExists(node):
                mc.delete(node)
        mc.setAttr(self.STORAGE_NODE + '.colorApplied', 0)

    def changeLayerColor(self):
        """Called when layer color picker is modified"""
        sel = mc.ls(sl=1, tr=1)
        clr = mc.colorSliderGrp('gsColorPicker', q=1, rgb=1)
        layerList = []
        for obj in sel:
            selPart = selectPart(2, True, obj)[0]
            conn = mc.listConnections(selPart, s=1, d=0)
            layer = mc.ls(conn, et='displayLayer')[0]
            layerList.append(layer)
        layerList = list(dict.fromkeys(layerList))
        colorDict = self.readColorDict()
        for layer in layerList:
            layerId = re.findall(r'\d+', layer)[0]
            mc.setAttr(layer + '.overrideColorRGB', clr[0], clr[1], clr[2])
            colorDict[int(layerId)] = clr
        self.writeColorDict(colorDict)
        if WIDGETS['syncCurveColor'].isChecked():
            self.syncCurveColors()

    # Other
    def randomizeColors(self, *_):
        """Randomizes colors in color storage node and updates UI colors if needed"""
        colorDict = self.readColorDict()
        for key in colorDict:
            geoLayer = 'curveGrp_%s_Geo' % key
            r, g, b = self.generateBrightColor()
            colorDict[int(key)] = [r, g, b]
            if mc.objExists(geoLayer):
                mc.setAttr(geoLayer + '.overrideColorRGB', r, g, b)
        self.writeColorDict(colorDict)

        if WIDGETS['syncCurveColor'].isChecked():
            self.syncCurveColors()
        if mc.objExists(self.STORAGE_NODE) and mc.getAttr(self.STORAGE_NODE + '.colorApplied'):
            self.updateColors()

    def syncCurveColors(self, manualSync=False, *_):
        """Syncs curve colors to match layer colors"""
        self.checkColorStorageNode()
        colorDict = self.readColorDict()
        sync = WIDGETS['syncCurveColor'].isChecked()
        if manualSync:
            sync = True

        # Generate color dictionary (if needed)
        for i in range(80):
            if colorDict[i] == [0, 0, 0]:
                colorDict[i] = self.generateBrightColor()
        self.writeColorDict(colorDict)

        # Iterate over collections and layers and set colors to curves
        layerCollectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        collectionCount = layerCollectionsWidget.count()
        for collectionID in range(collectionCount):
            collection = "%s_" % collectionID if collectionID > 0 else ""
            for i in range(80):
                curveLayer = 'curveGrp_%s%s_Curve' % (collection, i)
                if not mc.objExists(curveLayer):
                    continue
                curves = mc.editDisplayLayerMembers(curveLayer, q=1, nr=1, fn=1)
                for curve in curves:
                    shape = mc.listRelatives(curve, c=1, typ='nurbsCurve', pa=1)[0]
                    if sync:
                        mc.setAttr(shape + '.overrideEnabled', 1)
                        mc.setAttr(shape + '.overrideRGBColors', 1)
                        mc.setAttr(shape + '.overrideColorRGB', colorDict[i][0], colorDict[i][1], colorDict[i][2])
        curveControlUI.updateUI()

    def resetCurveColors(self, *_):
        """Resets curve colors to default value"""
        self.checkColorStorageNode()
        layerCollectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        collectionCount = layerCollectionsWidget.count()
        for collectionID in range(collectionCount):
            collection = "%s_" % collectionID if collectionID > 0 else ""
            for i in range(80):
                curveLayer = 'curveGrp_%s%s_Curve' % (collection, i)
                if not mc.objExists(curveLayer):
                    continue
                curves = mc.editDisplayLayerMembers(curveLayer, q=1, nr=1, fn=1)
                for curve in curves:
                    shape = mc.listRelatives(curve, c=1, typ='nurbsCurve', pa=1)[0]
                    mc.setAttr(shape + '.overrideEnabled', 0)
        curveControlUI.updateUI()

    def changeCurveColor(self, *_):
        """Called when curve color picker is modified"""
        sync = WIDGETS['syncCurveColor'].isChecked()
        if sync:
            updateMainUI()
            curveControlUI.updateUI()
        else:
            sel = mc.ls(sl=1, dag=1, s=1, typ='nurbsCurve')
            clr = mc.colorSliderGrp('gsCurveColorPicker', q=1, rgb=1)
            for crv in sel:
                if mc.nodeType(crv) != 'nurbsCurve':
                    continue
                if clr != [0, 0, 0]:
                    mc.setAttr(crv + '.overrideEnabled', 1)
                    mc.setAttr(crv + '.overrideRGBColors', 1)
                    mc.setAttr(crv + '.overrideColorRGB', clr[0], clr[1], clr[2])
                else:
                    mc.setAttr(crv + '.overrideEnabled', 0)

    # Utility methods
    def generateBrightColor(self, satMin=0.5, satMax=1.0):
        """Create random bright color and return as RGB tuple"""
        h, s, l = random.random(), random.uniform(satMin, satMax), random.uniform(0.3, 0.7)
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return (r, g, b)

    def resetSingleCurve(self, curve):
        shape = mc.listRelatives(curve, c=1, typ='nurbsCurve', pa=1)[0]
        mc.setAttr(shape + '.overrideEnabled', 0)


toggleColor = ToggleColor("toggleColor")


class CurveControlUI:

    extrudeCard = {
        'lengthDivisions',
        'dynamicDivisions',
        'widthDivisions',
        'Orientation',
        'Twist',
        'Width',
        'Taper',
        'Profile',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'surfaceNormals',
        'reverseNormals',
    }

    extrudeTube = {
        'lengthDivisions',
        'dynamicDivisions',
        'widthDivisions',
        'Orientation',
        'Twist',
        'widthComboSlider',
        'Taper',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'surfaceNormals',
        'reverseNormals',
    }

    warpCard = {
        'lengthDivisions',
        'dynamicDivisions',
        'widthDivisions',
        'Orientation',
        'Twist',
        'invTwist',
        'twistCurveFrame',
        'Width',
        'Taper',
        'widthCurveFrame',
        'LengthLock',
        'Length',
        'Offset',
        'Profile',
        'profileCurveGraph',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'samplingAccuracy',
        'surfaceNormals',
        'reverseNormals',
        'Magnitude'
    }

    warpTube = {
        'lengthDivisions',
        'dynamicDivisions',
        'widthDivisions',
        'Orientation',
        'Twist',
        'twistCurveFrame',
        'widthComboSlider',
        'Taper',
        'widthCurveFrame',
        'LengthLock',
        'Length',
        'Offset',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'samplingAccuracy',
        'surfaceNormals',
        'reverseNormals',
        'Magnitude'
    }

    bind = {
        'axisFrame',
        'editOrigObj',
        'Orientation',
        'twistCurveFrame',
        'Width',
        'widthCurveFrame',
        'LengthLock',
        'Length',
        'Offset',
        'curveRefine',
        'autoRefine',
        'curveSmooth',
        'samplingAccuracy',
        'reverseNormals',
        'Magnitude'
    }

    # Set of all controls
    allControls = extrudeCard \
        | extrudeTube \
        | warpCard \
        | warpTube \
        | bind

    def __init__(self, name):
        self.name = name

    def updateUI(self):
        """Updates all sliders and buttons in Curve Control Window and Connect Graphs"""
        if not mc.workspaceControl(CURVE_CONTROL_NAME, q=1, ex=1):
            return

        # Update advanced visibility window
        advancedVisibility.updateUI()

        # Apply geometry highlight if enabled
        if mc.optionVar(q='GSCT_GeometryHighlightEnabled'):
            utils.noUndo(advancedVisibility.geoHighlight)()

        # Meshes Section
        meshSel = mc.filterExpand(mc.ls(o=1, sl=1), sm=12)

        if meshSel:
            WIDGETS['orientToNormalsFrame'].setVisible(True)
        else:
            WIDGETS['orientToNormalsFrame'].setVisible(False)

        # Curves Section
        sel = mc.filterExpand(mc.ls(o=1, sl=1), sm=9)
        if not sel:
            sel = mc.ls(o=1, hl=1)

        if len(sel) == 0:
            self.hideControls()
            return

        curve = sel[-1]  # Use only last curve to update the UI

        if mc.nodeType(curve) == 'nurbsCurve':
            rel = mc.listRelatives(curve, p=1, pa=1)
            curve = rel[0]

        # Get all attributes from the curve
        self.sliderAttr = attributes.getAttr(curve)

        if 'Orientation' not in self.sliderAttr:
            self.hideControls()
            return

        if not mc.connectionInfo(curve + '.Orientation', isSource=1):
            self.hideControls()
            return

        # Enable orient to normals frame (if curves are selected but not the geo)
        WIDGETS['orientToNormalsFrame'].setVisible(True)

        # Disable prompt
        WIDGETS['selectCurvesPrompt'].setVisible(False)

        # Enable header and footer
        WIDGETS['gsCurveControlHeader'].setEnabled(True)
        WIDGETS['resetControlSliders'].setVisible(True)

        # Update Geometry Color and Layer Number
        try:
            layer = mc.ls(mc.listConnections(selectPart(2, True, curve)[0], s=1, d=0), et='displayLayer')[0]

            rgb = utils.getAttr(layer, 'overrideColorRGB')

            ind = int(re.findall(r'\d+', layer)[0])

            # If RGB is zero, check the storage node
            if rgb == [(0, 0, 0)]:
                colorDict = toggleColor.readColorDict()
                if ind in colorDict:
                    rgb = [colorDict[ind]]
            WIDGETS['gsColorPicker'].setRGBColors(*rgb)
            WIDGETS['gsLayerSelector'].setCurrentIndex(ind)
        except Exception as e:
            WIDGETS['gsLayerSelector'].setCurrentIndex(0)
            WIDGETS['gsColorPicker'].setRGBColors([0, 0, 0])
            LOGGER.exception(e)

        # Update Curve Color
        try:
            shape = mc.ls(curve, dag=1, s=1)[0]
            if mc.getAttr(shape + '.overrideEnabled'):
                curveRGB = utils.getAttr(shape, 'overrideColorRGB')
                WIDGETS['gsCurveColorPicker'].setRGBColors(*curveRGB)
            else:
                WIDGETS['gsCurveColorPicker'].setRGBColors([0, 0, 0])
        except Exception as e:
            WIDGETS['gsCurveColorPicker'].setRGBColors([0, 0, 0])
            LOGGER.exception(e)

        # Update Text Field
        try:
            WIDGETS['selectedObjectName'].setText(selectPart(0, True, curve)[0])
        except BaseException:
            WIDGETS['selectedObjectName'].setText('')

        # Set the dynamic divisions and auto refine false by default
        WIDGETS['dynamicDivisions'].setChecked(False)
        WIDGETS['autoRefine'].setChecked(False)
        WIDGETS['curveRefine'].setEnabled(True)
        WIDGETS['curveSmooth'].setEnabled(True)

        # Update main sliders and checkboxes
        for attr in self.sliderAttr:
            if attr == 'dynamicDivisions' and attr in WIDGETS:
                WIDGETS['dynamicDivisions'].setChecked(bool(mc.getAttr(curve + '.dynamicDivisions')))
                continue

            # Set "Other" frame visibility
            if attr == 'curveRefine' and attr in WIDGETS:
                WIDGETS['otherFrame'].setVisible(True)

            # Update Auto-Refine, Curve Refine and Curve Smooth sliders and toggles
            if attr == 'autoRefine' and attr in WIDGETS:
                WIDGETS['autoRefine'].setChecked(bool(mc.getAttr(curve + '.autoRefine')))
                WIDGETS['curveRefine'].setEnabled(not bool(mc.getAttr(curve + '.autoRefine')))
                WIDGETS['curveSmooth'].setEnabled(not bool(mc.getAttr(curve + '.autoRefine')))
                continue

            # Update Axis switch and Edit Original Obj. checkbox
            if attr == 'Axis' and attr in WIDGETS:
                WIDGETS['Axis'].button(self.sliderAttr['Axis']).setChecked(True)
                rebuildCurve = mc.listConnections(curve + '.curveSmooth', scn=1)[0]
                warp = mc.listConnections(rebuildCurve + '.outputCurve', scn=1)
                WIDGETS['editOrigObj'].setChecked(not mc.getAttr(warp[0] + '.envelope'))
                continue

            # Update Reverse Normals Attribute
            if attr == 'reverseNormals' and attr in WIDGETS:
                WIDGETS['reverseNormals'].setValue(not self.sliderAttr[attr])
                continue

            # Update Flip UV Attribute
            if attr == 'flipUV' and attr in WIDGETS:
                WIDGETS['flipUV'].setValue(not self.sliderAttr[attr])
                continue

            # Update the rest of the attributes
            if attr in WIDGETS:
                WIDGETS[attr].setValue(self.sliderAttr[attr])

        # Check for legacy UV attributes
        if 'rotateTipUV' in self.sliderAttr:
            WIDGETS['rotateTipUV'].setVisible(True)
            WIDGETS['rotateRootUV'].setVisible(True)
        else:
            WIDGETS['rotateTipUV'].setVisible(False)
            WIDGETS['rotateRootUV'].setVisible(False)

        # Update profile graph
        if mc.attributeQuery('latticeMessage', n=curve, ex=1):
            lattice = mc.listConnections(curve + '.latticeMessage')
            if lattice:
                latticeDiv = mc.getAttr(lattice[0] + '.sDivisions')
                if latticeDiv:
                    currentPoints = []
                    if lattice:
                        for i in range(latticeDiv):
                            currentPoints.append(mc.pointPosition(lattice[0] + '.pt[%s][1][0]' % (i), l=1))

                    newPoints = []
                    for i in range(latticeDiv):
                        x = mt.lerp(currentPoints[i][0], 1, 0, 0.5, -0.5)
                        y = mt.lerp(currentPoints[i][1], 1, 0, 1.5, -0.5)
                        newPoints.append((x, y))

                    graphPoints = ''

                    for i in range(latticeDiv):
                        graphPoints += '%s,%s,' % (newPoints[i][0], newPoints[i][1])

                    WIDGETS['profileCurve'].setGraph(graphPoints)
                    if mc.workspaceControl('GSCT_ProfileGraphPopOut', ex=1) and 'profileCurve_large' in WIDGETS:
                        WIDGETS['profileCurve_large'].setGraph(graphPoints)

        # Connect Warp Graphs
        if 'Length' in self.sliderAttr:
            rebuildCurve = mc.listConnections(curve + '.curveSmooth', scn=1)
            if rebuildCurve:
                warp = mc.listConnections(rebuildCurve[0] + '.outputCurve', scn=1)
                if warp:
                    WIDGETS['twistCurve'].connectGraph(warp[0] + '.twistCurve')
                    WIDGETS['scaleCurve'].connectGraph(warp[0] + '.scaleCurve')

                # Connect Large Graphs if exist
                if mc.workspaceControl("GSCT_TwistGraphPopOut", ex=1) and 'twistCurve_large' in WIDGETS:
                    if warp:
                        WIDGETS['twistCurve_large'].connectGraph(warp[0] + '.twistCurve')
                        WIDGETS['Magnitude_large'].setValue(self.sliderAttr['Magnitude'])
                if mc.workspaceControl("GSCT_WidthGraphPopOut", ex=1) and 'scaleCurve_large' in WIDGETS:
                    if warp:
                        WIDGETS['scaleCurve_large'].connectGraph(warp[0] + '.scaleCurve')

        # Show/Hide current controls
        currentControls = False
        uvs = False
        solidify = False

        if 'lengthDivisions' in self.sliderAttr and 'LengthLock' not in self.sliderAttr:
            if 'Width' in self.sliderAttr:
                currentControls = self.extrudeCard
            else:
                currentControls = self.extrudeTube
        elif 'lengthDivisions' in self.sliderAttr and 'LengthLock' in self.sliderAttr:
            if 'Width' in self.sliderAttr:
                currentControls = self.warpCard
            else:
                currentControls = self.warpTube
        elif 'AxisFlip' in self.sliderAttr:
            currentControls = self.bind
        else:
            self.hideControls()
            return 0

        if 'solidify' in self.sliderAttr:
            solidify = True

        if 'moveU' in self.sliderAttr:
            uvs = True

        self.changeControls(currentControls, uvs, solidify)

    def changeControls(self, currentControls, uv=True, solidify=True):
        if not currentControls:
            self.hideControls()
            return 0

        hiddenControls = self.allControls - currentControls
        for key in currentControls:
            if key in WIDGETS:
                WIDGETS[key].setVisible(True)
        for key in hiddenControls:
            if key in WIDGETS:
                WIDGETS[key].setVisible(False)

        WIDGETS['UVFrame'].setVisible(True if uv else False)
        WIDGETS['solidifyFrame'].setVisible(True if solidify else False)

    def hideControls(self):
        for key in self.allControls:
            if key in WIDGETS:
                WIDGETS[key].setHidden(True)
        WIDGETS['gsCurveControlHeader'].setEnabled(False)
        WIDGETS['gsColorPicker'].setRGBColors([0, 0, 0])
        WIDGETS['gsCurveColorPicker'].setRGBColors([0, 0, 0])
        WIDGETS['gsLayerSelector'].setCurrentIndex(0)
        WIDGETS['selectedObjectName'].setText('')
        WIDGETS['otherFrame'].setVisible(False)
        WIDGETS['UVFrame'].setVisible(False)
        WIDGETS['solidifyFrame'].setVisible(False)
        WIDGETS['resetControlSliders'].setVisible(False)
        WIDGETS['selectCurvesPrompt'].setVisible(True)

    def selectOriginalObjects(self):
        """Selects the curves that were attached to the bind curve"""
        sel = mc.ls(sl=1, tr=1)
        if not sel:
            return
        selectionList = []
        for curve in sel:
            if not mc.attributeQuery('gsmessage', n=curve, ex=1):
                continue
            childCards = mc.listConnections(curve + '.gsmessage', d=1, s=0, t='transform', scn=1)
            if not childCards:
                continue
            selectionList += childCards
        if selectionList:
            mc.select(selectionList, r=1)

    def editOriginalObjects(self):
        """Temporarily unhides the original objects from the bind curve"""
        sel = mc.ls(sl=1, tr=1)
        if not sel:
            return
        checkBox = WIDGETS['editOrigObj'].isChecked()
        axisFlip = WIDGETS['AxisFlip'].isChecked()
        for curve in sel:
            try:
                getAttr = attributes.getAttr(curve)
                if 'AxisFlip' in getAttr:
                    warpNode = mc.listConnections(curve + '.Width')[0]
                    message = mc.listConnections(curve + '.gsmessage')
                    if message:
                        grp = mc.listRelatives(mc.listRelatives(message[0], p=1, pa=1), p=1, pa=1)
                        if checkBox:
                            if grp:
                                mc.setAttr(warpNode + '.envelope', 0)
                                mc.setAttr(grp[0] + '.visibility', 1)
                        else:
                            if grp:
                                mc.setAttr(warpNode + '.envelope', 1)
                                mc.setAttr(grp[0] + '.visibility', 0)
                        if axisFlip and mc.attributeQuery('reverseNormals', n=curve, ex=1):
                            mc.setAttr(curve + '.reverseNormals', not mc.getAttr(curve + '.reverseNormals'))
                    elif not message and 'AxisFlip' in getAttr:
                        if checkBox:
                            mc.setAttr(warpNode + '.envelope', 0)
                        else:
                            mc.setAttr(warpNode + '.envelope', 1)
                        if axisFlip and mc.attributeQuery('reverseNormals', n=curve, ex=1):
                            mc.setAttr(curve + '.reverseNormals', not mc.getAttr(curve + '.reverseNormals'))
                    self.updateUI()
            except Exception as e:
                LOGGER.exception(e)


curveControlUI = CurveControlUI("curveControlUI")


class ImportExport:
    """ Import and Export curves """

    def __init__(self, name):
        self.name = name

    def exportCurves(self):
        """Export selected curves into a .curves or .ma file to import later"""
        sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
        if not sel:
            sel = mc.filterExpand(mc.ls(hl=1, o=1), sm=9)
        if not sel:
            MESSAGE.warningInView('Select at least one curve to export')
            return
        mc.select(sel)
        sel = selectPart(0, True)
        if not sel:
            return
        mc.select(sel, r=1)
        mc.select(hi=1)
        filters = "GS Curves (.curves) (*.curves);;Maya ASCII (.ma) (*.ma)"
        dialog = mc.fileDialog2(fileFilter=filters, dialogStyle=2)
        if not dialog:
            return
        mc.file(dialog, force=1, options="v=0;", typ="mayaAscii", pr=1, es=1, de=0)

    def importCurves(self):
        """Import curves from .curve or .ma file that was exported using exportCurves function"""
        filters = "GS Curves (.curves) (*.curves);;Maya ASCII (.ma) (*.ma)"
        dialog = mc.fileDialog2(fileFilter=filters, fm=1, dialogStyle=2, okc='Open')
        if not dialog:
            return
        nodes = mc.file(dialog, i=1, dns=1, rnn=1)
        curveGroups = []
        geoGroups = []
        instGroups = []
        collection = None
        if getOption('importIntoANewCollection') and getOption('showLayerCollectionsMenu'):
            collection = layerCollections.createImportedCurvesCollection()
        for node in nodes:
            if 'curveGrp_' in node and '_Curve' in node:
                curveGroups.append(node)
            if 'curveGrp_' in node and '_Geo' in node:
                geoGroups.append(node)
            if 'curveGrp_' in node and '_Inst' in node:
                instGroups.append(node)
        for group in curveGroups:
            split = group.split("_")
            grpCurves = mc.editDisplayLayerMembers(group, q=1, fn=1)
            try:
                index = int(split[1]) if len(split) == 3 else int(split[2])
            except ValueError:
                error = 'Failed to extract layer ID from layer "{}". Display Layer name is corrupted. Please delete corrupted layers and curves.'.format(group)
                MESSAGE.warning(error)
                continue
            curveAddToLayer(index, inputCurves=grpCurves, targetCollection=collection)
        utils.fixDuplicateNames(nodes)
        # Check if there are some empty groups left after the import
        grps = curveGroups + geoGroups + instGroups
        for grp in grps:
            if mc.objExists(grp) and not mc.editDisplayLayerMembers(grp, q=1, fn=1):
                mc.delete(grp)


importExport = ImportExport("importExport")


class LayerCollections:

    def __init__(self, name):
        self.name = name
        self.copyIndex = None

    ### INTERFACE METHODS ###

    def toggleLayerCollectionsWidget(self):
        """Toggles the visibility of the layer collections widget"""
        if getOption('showLayerCollectionsMenu'):
            WIDGETS['LayerCollectionsLayout'].setHidden(False)
        else:
            WIDGETS['LayerCollectionsLayout'].setHidden(True)
        WIDGETS['layerCollectionsComboBox'].setCurrentIndex(0)
        WIDGETS['LayerLayout'].update()
        WIDGETS['LayerLayout'].parentWidget().update()

    ### PARAMETERS UPDATES ###

    def updateDefaultLayerNode(self):
        """Updates layer collection dict attribute on defaultLayer node based on collections combo box items"""
        if not mc.objExists('defaultLayer'):
            MESSAGE.warning("Default layer not found!")
            return
        if not mc.attributeQuery('gsCollectionsDict', n='defaultLayer', ex=1):
            mc.addAttr('defaultLayer', ln='gsCollectionsDict', dt='string')
        comboBox = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        collectionsDict = {}
        for i in range(1, comboBox.count()):
            collectionsDict.update({i: comboBox.itemText(i)})
        mc.setAttr('defaultLayer.gsCollectionsDict', str(collectionsDict), typ='string')

    def updateCollectionNames(self):
        """Updates all the active collection layers to have a proper name based gsCollectionName attr on curves"""
        collectionSet = utils.getCollectionsSet()
        if not collectionSet:
            return
        allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Curve' in x)]
        filteredLayers = [x for x in allLayers if len(x.split("_")) == 4]
        for c in filteredLayers:
            if not mc.objExists(c):
                continue
            if not mc.attributeQuery('gsCollectionName', n=c, ex=1):
                mc.addAttr(c, ln='gsCollectionName', dt='string')
            collectionID = int(c.split("_")[1])
            collectionName = WIDGETS['layerCollectionsComboBox'].itemText(collectionID)
            mc.setAttr(c + '.gsCollectionName', collectionName, typ='string')

    ### FUNCTIONAL METHODS ###

    def createImportedCurvesCollection(self):
        # type: () -> int
        """Creates and Imported Curves collection and returns its ID"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        collectionId = layerDropdownMenu.findText("ImportedCurves")
        if collectionId == -1:
            layerDropdownMenu.addItem("ImportedCurves")
            collectionId = layerDropdownMenu.count() - 1
        layerDropdownMenu.setCurrentIndex(collectionId)
        return collectionId

    def createLayerCollection(self, exists=False):
        # type: (bool) -> None
        """Create a named layer collection via the plus button on the interface"""
        msg = 'Name already exists.\nEnter unique name:' if exists else 'Enter Collection Name:'
        result = mc.promptDialog(
            title='New Collection',
            message=msg,
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        if result == 'OK':
            name = mc.promptDialog(q=1, t=1)
        else:
            return
        if not name:
            MESSAGE.warningInView("Invalid Name!")
            self.createLayerCollection()
            return
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        if layerDropdownMenu.findText(name) != -1:
            self.createLayerCollection(True)
            return
        layerDropdownMenu.addItem(name)
        layerDropdownMenu.setCurrentIndex(layerDropdownMenu.count() - 1)
        self.updateDefaultLayerNode()
        updateMainUI()

    def deleteLayerCollection(self):
        """Delete currently active layer collection and transfer all the layers to the current-1 collection"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        index = layerDropdownMenu.currentIndex()
        if index == 0:
            return
        name = layerDropdownMenu.itemText(index)
        result = mc.confirmDialog(
            title='Delete Collection',
            message='Delete collection "{}" (#{})?\nAll the layers will be transferred one collection up.'.format(name, index),
            icn='information',
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        if result != 'OK':
            return
        self.transferLayerCollection(index, index - 1)
        layerDropdownMenu.setCurrentIndex(index - 1)
        layerDropdownMenu.removeItem(index)
        self.updateDefaultLayerNode()
        count = layerDropdownMenu.count()
        for i in range(1, count):
            self.transferLayerCollection(index + i, index - 1 + i)
        self.updateDefaultLayerNode()
        updateMainUI()

    def transferLayerCollection(self, sourceIndex, targetIndex):
        # type: (int, int, bool) -> None
        """Transfers all the layers from source collection to the target collection"""
        allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Curve' in x)]
        sourceLayers = []
        for layer in allLayers:
            s = layer.split('_')
            if len(s) == 4 and int(s[1]) == sourceIndex:
                sourceLayers.append(layer)
        for layer in sourceLayers:
            s = layer.split('_')
            targetLayer = s[2] if len(s) == 4 else s[1]
            curves = mc.editDisplayLayerMembers(layer, q=1, fn=1)
            if not curves:
                continue
            curveAddToLayer(targetLayer=targetLayer, inputCurves=curves, targetCollection=targetIndex)

    def mergeUp(self):
        """Transfer all the layers from the current collection up and shifts other collections"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = layerDropdownMenu.currentIndex()
        count = layerDropdownMenu.count()
        if currentIndex > 0:
            upIndex = currentIndex - 1
            self.transferLayerCollection(currentIndex, upIndex)
            layerDropdownMenu.setCurrentIndex(upIndex)
            layerDropdownMenu.removeItem(currentIndex)
            self.updateDefaultLayerNode()
            for i in range(1, count):
                self.transferLayerCollection(currentIndex + i, upIndex + i)
            self.updateDefaultLayerNode()
            updateMainUI()
        else:
            MESSAGE.warningInView('This is the first collection in the list.')

    def mergeDown(self):
        """Transfer all the layers from the current collection down and shift all the collections"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = layerDropdownMenu.currentIndex()
        count = layerDropdownMenu.count()
        if currentIndex == 0:
            MESSAGE.warningInView("Main collection can't be merged.")
            return
        if currentIndex == count - 1:
            MESSAGE.warningInView('This is the last collection in the list.')
            return
        downIndex = currentIndex + 1
        self.transferLayerCollection(currentIndex, downIndex)
        layerDropdownMenu.setCurrentIndex(downIndex)
        layerDropdownMenu.removeItem(currentIndex)
        self.updateDefaultLayerNode()
        for i in range(1, count):
            self.transferLayerCollection(currentIndex + i, currentIndex - 1 + i)
        self.updateDefaultLayerNode()
        updateMainUI()

    def moveDown(self):
        """Moves current collection index down, rearranging the collection"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = layerDropdownMenu.currentIndex()
        count = layerDropdownMenu.count()
        if currentIndex == 0:
            MESSAGE.warningInView("Main collection can't be moved.")
            return
        if currentIndex == count - 1:
            MESSAGE.warningInView('This is the last collection in the list.')
            return
        currentName = layerDropdownMenu.itemText(currentIndex)
        downIndex = currentIndex + 1
        downName = layerDropdownMenu.itemText(downIndex)
        layerDropdownMenu.addItem('GS_TEMP_COLLECTION_DELETE_THIS')
        layerDropdownMenu.setItemText(downIndex, currentName)
        layerDropdownMenu.setItemText(currentIndex, downName)
        self.transferLayerCollection(currentIndex, layerDropdownMenu.count() - 1)
        self.transferLayerCollection(downIndex, currentIndex)
        self.transferLayerCollection(layerDropdownMenu.count() - 1, downIndex)
        layerDropdownMenu.removeItem(layerDropdownMenu.count() - 1)
        self.updateDefaultLayerNode()
        updateMainUI()

    def moveUp(self):
        """Moves current collection index down, rearranging the collection"""
        layerDropdownMenu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = layerDropdownMenu.currentIndex()
        if currentIndex == 0 or currentIndex == 1:
            MESSAGE.warningInView("Main collection can't be moved.")
            return
        currentName = layerDropdownMenu.itemText(currentIndex)
        upIndex = currentIndex - 1
        upName = layerDropdownMenu.itemText(upIndex)
        layerDropdownMenu.addItem('GS_TEMP_COLLECTION_DELETE_THIS')
        layerDropdownMenu.setItemText(upIndex, currentName)
        layerDropdownMenu.setItemText(currentIndex, upName)
        self.transferLayerCollection(currentIndex, layerDropdownMenu.count() - 1)
        self.transferLayerCollection(upIndex, currentIndex)
        self.transferLayerCollection(layerDropdownMenu.count() - 1, upIndex)
        layerDropdownMenu.removeItem(layerDropdownMenu.count() - 1)
        self.updateDefaultLayerNode()
        updateMainUI()

    def rename(self, exists=False):
        menu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = menu.currentIndex()
        if currentIndex == 0:
            MESSAGE.warningInView("Main collection can't be renamed.")
            return
        msg = "Name already exists.\nEnter unique name:" if exists else "Enter New Name:"
        result = mc.promptDialog(
            title='Rename Collection',
            message=msg,
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        if result == 'OK':
            name = mc.promptDialog(q=1, t=1)
        else:
            return
        if not name:
            MESSAGE.warningInView("Invalid Name!")
            self.rename()
            return
        if menu.findText(name) != -1:
            self.rename(True)
            return
        menu.setItemText(currentIndex, name)
        self.updateDefaultLayerNode()
        updateMainUI()

    def clear(self):
        menu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = menu.currentIndex()
        itemName = menu.itemText(currentIndex)
        msg = 'Clearing collection "{}".\nAll the layers and curves in this collection will be deleted.\nAre you sure?'.format(itemName)
        result = mc.confirmDialog(
            title='Clear Collection',
            message=msg,
            icn='warning',
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        if result == 'OK':
            for i in range(80):
                curveGrp, _, _ = utils.getFormattedLayerNames(currentIndex, i)
                if not mc.objExists(curveGrp):
                    continue
                contents = mc.editDisplayLayerMembers(curveGrp, q=1, fn=1)
                if not contents:
                    continue
                for curve in contents:
                    if not mc.objExists(curve):
                        continue
                    if mc.attributeQuery('gsmessage', ex=1, n=curve):
                        if mc.connectionInfo(curve + '.gsmessage', isDestination=1):
                            continue
                    parentGrp = mc.listRelatives(curve, p=1)
                    if parentGrp:
                        mc.delete(parentGrp)
        self.updateDefaultLayerNode()
        updateMainUI()

    def copy(self):
        menu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = menu.currentIndex()
        self.copyIndex = currentIndex
        MESSAGE.warningInView('Layer collection "%s" added to buffer' % menu.itemText(currentIndex))

    def paste(self):
        if self.copyIndex is None:
            return
        menu = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentIndex = menu.currentIndex()
        if self.copyIndex == currentIndex:
            return
        MESSAGE.warningInView('Pasting from collection "%s" to "%s"'
                              % (menu.itemText(self.copyIndex), menu.itemText(currentIndex)))

        allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Curve' in x)]
        sourceLayers = []
        if self.copyIndex == 0:
            sourceLayers = [x for x in allLayers if len(x.split("_")) == 3]
        else:
            for layer in allLayers:
                s = layer.split("_")
                if len(s) == 4 and int(s[1]) == self.copyIndex:
                    sourceLayers.append(layer)
        for layer in sourceLayers:
            s = layer.split("_")
            targetLayer = s[2] if len(s) == 4 else s[1]
            curves = mc.editDisplayLayerMembers(layer, q=1, fn=1)
            if not curves:
                continue
            curves = list(duplicateCurve(customSel=curves))
            curveAddToLayer(targetLayer=targetLayer, inputCurves=curves, targetCollection=currentIndex)
        self.updateDefaultLayerNode()
        self.copyIndex = None


layerCollections = LayerCollections("layerCollections")


class AdvancedVisibility():

    CACHED_GEO = []

    def __init__(self, name):
        self.name = name

    def geoHighlight(self):
        """ Update geometry hilite based on the selected curve """
        # Check if window exists
        if not mc.workspaceControl(CURVE_CONTROL_NAME, q=1, ex=1):
            return
        if not mc.optionVar(q="GSCT_GeometryHighlightEnabled"):
            mc.hilite(self.CACHED_GEO, u=1)
            self.CACHED_GEO = []
            WIDGETS['geometryHighlight'].setChecked(False)
            return
        else:
            WIDGETS['geometryHighlight'].setChecked(True)
        sel = mc.ls(sl=1, dag=1, typ='nurbsCurve')
        if not sel:
            sel = mc.ls(sl=1, o=1, typ='nurbsCurve')
        if not sel:
            sel = mc.ls(hl=1, dag=1, typ='nurbsCurve')
        if sel:
            geo = selectPart(2, True, sel)
            if geo:
                mc.hilite(geo)
                self.CACHED_GEO = geo
            else:
                self.CACHED_GEO = []
        else:
            try:
                mc.hilite(self.CACHED_GEO, u=1)
            except BaseException:
                mc.hilite([], r=1)
            self.CACHED_GEO = []

    def geometryHighlightCommand(self):
        mc.optionVar(iv=["GSCT_GeometryHighlightEnabled", not mc.optionVar(q='GSCT_GeometryHighlightEnabled')])
        self.geoHighlight()

    def createNode(self):
        tr = mc.createNode('transform', n='GSCT_CurveTools_DrawManager', ss=1)
        # Lock transforms for node
        for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'shearXY', 'shearXZ', 'shearYZ']:
            mc.setAttr(tr + '.' + attr, l=1, k=0)
        # Create rest of the network
        mc.createNode('GSCT_CurveTools_DrawManagerNode',
                      n='GSCT_CurveTools_DrawManagerNode', p=tr, ss=1)
        mc.setAttr(tr + ".useOutlinerColor", 1)
        mc.setAttr(tr + ".outlinerColor", 0, 1, 0, typ="double3")
        mc.reorder(tr, r=1)
        self.applySettingsToNode()

    def updateUI(self):
        """Updates UI on selection change"""
        if not all(mc.getClassification("GSCT_CurveTools_DrawManagerNode")):  # Check if node type exists
            return
        button = WIDGETS['curveHighlight']
        frame = WIDGETS['gsCurveHighlightFrame']
        nodes = mc.ls(typ='GSCT_CurveTools_DrawManagerNode')
        if not nodes:
            button.setChecked(False)
            frame.setEnabled(False)
        nodeFound = False
        for node in nodes:
            if mc.referenceQuery(node, inr=1):
                mc.setAttr(node + '.nodeState', 1)
                continue
            nodeFound = True
        if nodeFound:
            WIDGETS['curveHighlight'].setChecked(True)
            WIDGETS['gsCurveHighlightFrame'].setEnabled(True)
        else:
            WIDGETS['curveHighlight'].setChecked(False)
            WIDGETS['gsCurveHighlightFrame'].setEnabled(False)

    def removeUnknownNodes(self):
        """Finds all the nodes that were possibly left out from the previous session"""
        sel = mc.ls(typ="unknownDag")
        for n in sel:
            if "GSCT_CurveTools_DrawManager" in n:
                mc.delete(mc.listRelatives(n, p=1, pa=1))

    def toggleCurveHighlightFromUI(self, hotkey=False):
        """Toggles the nodes in the scene from UI"""
        # Check if there are leftover nodes
        self.removeUnknownNodes()
        # Check if control exists
        if 'curveHighlight' not in WIDGETS:
            from . import ui
            ui.curveControlWorkspace()
            return
        # Check for Maya version and find an appropriate plug-in to load
        button = WIDGETS['curveHighlight']  # type: wrap.Button
        pluginPath = utils.getFolder.plugins()
        winPath = os.path.join(pluginPath, str(MAYA_VER), "cv_manip.mll")
        fallBackPath = os.path.join(pluginPath, "cv_manip.py")
        result = False
        if OS != "mac":
            result = utils.loadCustomPlugin(winPath)
        else:
            result = utils.loadCustomPlugin(fallBackPath)
        # If loading fails, try to load the fallback (python) version instead
        if not result:
            finalResult = utils.loadCustomPlugin(fallBackPath)
            if not finalResult:
                MESSAGE.warning(
                    "Can't load cv_manip plug-in. Check your installation or contact the developer: george.sladkovsky@gmail.com")
                button.setChecked(False)
                return
        # Check if node type exists
        if not all(mc.getClassification("GSCT_CurveTools_DrawManagerNode")):
            button.setChecked(False)
            MESSAGE.warning(
                "No compatible node types found. Please reinstall GS CurveTools or send a bug report: george.sladkovsky@gmail.com")
            return
        # Proceed with node creation/activation
        nodes = mc.ls(typ='GSCT_CurveTools_DrawManagerNode')
        if button.isChecked() if hotkey else not button.isChecked():
            # Delete nodes from scene if found
            for node in nodes:
                if mc.referenceQuery(node, inr=1):
                    mc.setAttr(node + '.nodeState', 1)
                else:
                    mc.delete(mc.listRelatives(node, p=1, pa=1))
        else:
            # Just create a new node
            self.createNode()
        # Check if locator visibility is enabled in the current view
        try:
            currentView = mc.playblast(ae=1)
            mc.modelEditor(currentView, e=1, locators=1)
        except BaseException:
            pass
        self.updateUI()

    # ---- Saving, loading and applying settings ----

    def loadSettingsFromOptionVar(self):
        """Load settings from optionVars and apply them to the interface and to the node"""
        if not mc.workspaceControl(CURVE_CONTROL_NAME, q=1, ex=1):
            return
        # Load ints (bools)
        WIDGETS['curveVisibility'].setChecked(mc.optionVar(q='GSCT_' + 'gsCurveVisibilityToggle'))
        WIDGETS['hullVisibility'].setChecked(mc.optionVar(q='GSCT_' + 'gsHullVisibilityToggle'))
        WIDGETS['lazyUpdate'].setChecked(mc.optionVar(q='GSCT_' + 'gsLazyUpdateToggle'))
        WIDGETS['alwaysOnTop'].setChecked(mc.optionVar(q='GSCT_' + 'gsAlwaysOnTopToggle'))
        WIDGETS['cvDistanceColor'].setChecked(mc.optionVar(q='GSCT_' + 'gsCVDistanceColor'))
        WIDGETS['hullDistanceColor'].setChecked(mc.optionVar(q='GSCT_' + 'gsHullDistanceColor'))
        WIDGETS['curveDistanceColor'].setChecked(mc.optionVar(q='GSCT_' + 'gsCurveDistanceColor'))
        WIDGETS['CVocclusion'].setChecked(mc.optionVar(q='GSCT_' + 'gsEnableCVOcclusion'))
        # Load Floats
        mc.floatSliderGrp('gsPointSizeSlider', e=1, v=(mc.optionVar(q='GSCT_' + 'gsPointSizeSlider')))
        mc.floatSliderGrp('gsCurveWidthSlider', e=1, v=(mc.optionVar(q='GSCT_' + 'gsCurveWidthSlider')))
        mc.floatSliderGrp('gsHullWidthSlider', e=1, v=(mc.optionVar(q='GSCT_' + 'gsHullWidthSlider')))
        WIDGETS['gsDeselectedCVAlpha'].setValue(mc.optionVar(q='GSCT_' + 'gsDeselectedCVAlpha'))
        WIDGETS['gsSelectedCVAlpha'].setValue(mc.optionVar(q='GSCT_' + 'gsSelectedCVAlpha'))
        WIDGETS['gsCurveHighlightAlpha'].setValue(mc.optionVar(q='GSCT_' + 'gsCurveHighlightAlpha'))
        WIDGETS['gsHullHighlightAlpha'].setValue(mc.optionVar(q='GSCT_' + 'gsHullHighlightAlpha'))
        WIDGETS['gsDistanceColorMinValue'].setValue(mc.optionVar(q='GSCT_' + 'gsDistanceColorMinValue'))
        WIDGETS['gsDistanceColorMaxValue'].setValue(mc.optionVar(q='GSCT_' + 'gsDistanceColorMaxValue'))
        # Load Colors
        WIDGETS['gsDeselectedCVColor'].setRGBColors(eval(mc.optionVar(q='GSCT_' + 'gsDeselectedCVColor')))
        WIDGETS['gsSelectedCVColor'].setRGBColors(eval(mc.optionVar(q='GSCT_' + 'gsSelectedCVColor')))
        WIDGETS['gsCurveHighlightColor'].setRGBColors(eval(mc.optionVar(q='GSCT_' + 'gsCurveHighlightColor')))
        WIDGETS['gsHullHighlightColor'].setRGBColors(eval(mc.optionVar(q='GSCT_' + 'gsHullHighlightColor')))
        # String Values
        WIDGETS['gsOccluderMeshName'].setText(mc.optionVar(q='GSCT_' + 'gsOccluderMeshName'))
        self.applySettingsToNode()

    def saveSettingsFromUI(self):
        """Save settings from UI to optionVars"""
        mc.optionVar(fv=['GSCT_' + 'gsPointSizeSlider', mc.floatSliderGrp('gsPointSizeSlider', q=1, v=1)])
        mc.optionVar(fv=['GSCT_' + 'gsCurveWidthSlider', mc.floatSliderGrp('gsCurveWidthSlider', q=1, v=1)])
        mc.optionVar(fv=['GSCT_' + 'gsHullWidthSlider', mc.floatSliderGrp('gsHullWidthSlider', q=1, v=1)])
        mc.optionVar(sv=['GSCT_' + 'gsDeselectedCVColor', str(WIDGETS["gsDeselectedCVColor"].getRGBColors())])
        mc.optionVar(fv=['GSCT_' + 'gsDeselectedCVAlpha', WIDGETS['gsDeselectedCVAlpha'].getValue()])
        mc.optionVar(sv=['GSCT_' + 'gsSelectedCVColor', str(WIDGETS["gsSelectedCVColor"].getRGBColors())])
        mc.optionVar(fv=['GSCT_' + 'gsSelectedCVAlpha', WIDGETS['gsSelectedCVAlpha'].getValue()])
        mc.optionVar(sv=['GSCT_' + 'gsCurveHighlightColor', str(WIDGETS["gsCurveHighlightColor"].getRGBColors())])
        mc.optionVar(fv=['GSCT_' + 'gsCurveHighlightAlpha', WIDGETS['gsCurveHighlightAlpha'].getValue()])
        mc.optionVar(sv=['GSCT_' + 'gsHullHighlightColor', str(WIDGETS["gsHullHighlightColor"].getRGBColors())])
        mc.optionVar(fv=['GSCT_' + 'gsHullHighlightAlpha', WIDGETS['gsHullHighlightAlpha'].getValue()])
        mc.optionVar(iv=['GSCT_' + 'gsCurveVisibilityToggle', WIDGETS['curveVisibility'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsHullVisibilityToggle', WIDGETS['hullVisibility'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsLazyUpdateToggle', WIDGETS['lazyUpdate'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsAlwaysOnTopToggle', WIDGETS['alwaysOnTop'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsCVDistanceColor', WIDGETS['cvDistanceColor'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsHullDistanceColor', WIDGETS['hullDistanceColor'].isChecked()])
        mc.optionVar(iv=['GSCT_' + 'gsCurveDistanceColor', WIDGETS['curveDistanceColor'].isChecked()])
        mc.optionVar(fv=['GSCT_' + 'gsDistanceColorMinValue', WIDGETS['gsDistanceColorMinValue'].getValue()])
        mc.optionVar(fv=['GSCT_' + 'gsDistanceColorMaxValue', WIDGETS['gsDistanceColorMaxValue'].getValue()])
        mc.optionVar(iv=['GSCT_' + 'gsEnableCVOcclusion', WIDGETS['CVocclusion'].isChecked()])
        mc.optionVar(sv=['GSCT_' + 'gsOccluderMeshName', str(WIDGETS["gsOccluderMeshName"].text())])

    def applySettingsToNode(self):
        """Applies user settings from the UI to created node. A bit slow, but works for this."""
        if not all(mc.getClassification("GSCT_CurveTools_DrawManagerNode")):  # Check if node type exists
            return
        nodes = mc.ls(typ='GSCT_CurveTools_DrawManagerNode')
        for node in nodes:
            if mc.referenceQuery(node, inr=1):
                continue
            mc.setAttr(node + '.pointSize', float(mc.floatSliderGrp('gsPointSizeSlider', q=1, v=1)))
            mc.setAttr(node + '.lineWidth', float(mc.floatSliderGrp('gsCurveWidthSlider', q=1, v=1)))
            mc.setAttr(node + '.hullWidth', float(mc.floatSliderGrp('gsHullWidthSlider', q=1, v=1)))
            dpc_r, dpc_g, dpc_b = WIDGETS["gsDeselectedCVColor"].getRGBColors()
            mc.setAttr(node + '.deselectedPointColor', dpc_r, dpc_g, dpc_b, typ='double3')
            mc.setAttr(node + '.deselectedPointAlpha', WIDGETS['gsDeselectedCVAlpha'].getValue())
            spc_r, spc_g, spc_b = WIDGETS["gsSelectedCVColor"].getRGBColors()
            mc.setAttr(node + '.selectedPointColor', spc_r, spc_g, spc_b, typ='double3')
            mc.setAttr(node + '.selectedPointAlpha', WIDGETS['gsSelectedCVAlpha'].getValue())
            crvc_r, crvc_g, crvc_b = WIDGETS["gsCurveHighlightColor"].getRGBColors()
            mc.setAttr(node + '.curveColor', crvc_r, crvc_g, crvc_b, typ='double3')
            mc.setAttr(node + '.curveAlpha', WIDGETS['gsCurveHighlightAlpha'].getValue())
            hc_r, hc_g, hc_b = WIDGETS["gsHullHighlightColor"].getRGBColors()
            mc.setAttr(node + '.hullColor', hc_r, hc_g, hc_b, typ='double3')
            mc.setAttr(node + '.hullAlpha', WIDGETS['gsHullHighlightAlpha'].getValue())
            mc.setAttr(node + '.showCurve', WIDGETS['curveVisibility'].isChecked())
            mc.setAttr(node + '.showHull', WIDGETS['hullVisibility'].isChecked())
            mc.setAttr(node + '.lazyUpdate', WIDGETS['lazyUpdate'].isChecked())
            mc.setAttr(node + '.drawOnTop', WIDGETS['alwaysOnTop'].isChecked())
            mc.setAttr(node + '.useCVDistanceColor', WIDGETS['cvDistanceColor'].isChecked())
            mc.setAttr(node + '.useHullDistanceColor', WIDGETS['hullDistanceColor'].isChecked())
            mc.setAttr(node + '.useCurveDistanceColor', WIDGETS['curveDistanceColor'].isChecked())
            mc.setAttr(node + '.distanceColorMin', WIDGETS['gsDistanceColorMinValue'].getValue())
            mc.setAttr(node + '.distanceColorMax', WIDGETS['gsDistanceColorMaxValue'].getValue())
            mc.setAttr(node + '.useCVOcclusion', WIDGETS['CVocclusion'].isChecked())
            mc.setAttr(node + '.occluderMeshName', WIDGETS['gsOccluderMeshName'].text(), typ='string')

    def selectOccluderFromScene(self):
        mesh = mc.ls(sl=1, tr=1)
        if not mesh:
            return
        for obj in mesh:
            if mc.nodeType(mc.listRelatives(obj, c=1, pa=1)) != "mesh":
                continue
            WIDGETS['gsOccluderMeshName'].setText(obj)
            break
        else:
            MESSAGE.warningInView("No compatible meshes selected. Select a mesh object.")
        self.applySettingsToNode()


advancedVisibility = AdvancedVisibility("advancedVisibility")


### Layers, Interface and Other Updates ###

def updateMainUI(clearLayerCollections=False):
    """Updates main UI controls"""

    # --- Change Layer number ---
    num = 20
    if 'layerRowsActionGroup' in WIDGETS:
        action = WIDGETS['layerRowsActionGroup'].checkedAction()
        if action is not None:
            checkbox = action.objName
            checkboxNum = re.findall(r'\d+', checkbox)[0]
            num = int(checkboxNum) * 10
        else:
            print("Warning: 'layerRowsActionGroup' checkedAction is None.")
            return
    else:
        print("Warning: 'layerRowsActionGroup' not found in WIDGETS")
        return
    active = set(range(int(checkboxNum)))
    allLayers = set(range(8))
    for a in active:
        if 'layerRow%s' % a in WIDGETS:
            WIDGETS['layerRow%s' % a].setHidden(False)
    for a in (allLayers - active):
        WIDGETS['layerRow%s' % a].setHidden(True)
    WIDGETS['curveGrp0'].setNumberOfLayers(num)
    WIDGETS['LayerLayout'].update()
    WIDGETS['LayerLayout'].parentWidget().update()

    # --- Update Layer Collections ---
    comboBox = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
    if clearLayerCollections:
        comboBox.clear()
    if mc.objExists('defaultLayer') and mc.attributeQuery('gsCollectionsDict', n='defaultLayer', ex=1):
        collectionsString = mc.getAttr('defaultLayer.gsCollectionsDict')
        collectionsDict = dict(eval(collectionsString))
        for key in collectionsDict:
            if comboBox.findText(collectionsDict[key]) == -1:
                comboBox.insertItem(key, collectionsDict[key])
    if WIDGETS['layerCollectionsComboBox'].currentIndex() == 0:
        WIDGETS['layerCollectionsMinus'].setEnabled(False)
    else:
        WIDGETS['layerCollectionsMinus'].setEnabled(True)
    updateVisibilityBasedOnActiveCollection()

    # --- Update layer buttons ---
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    for layerID in range(80):
        button = 'curveGrp%s' % layerID
        buttonWidget = WIDGETS[button]
        grpCurve, grpGeo, grpInst = utils.getFormattedLayerNames(collectionID, layerID)
        if not mc.objExists(grpCurve):
            buttonWidget.setStyle('empty')
            continue
        layers = mc.editDisplayLayerMembers(grpCurve, q=1, fn=1)
        if mc.objExists(grpCurve) and mc.objExists(grpGeo) and mc.objExists(grpInst) and layers:
            curve = mc.getAttr(grpCurve + '.visibility')
            geo = mc.getAttr(grpGeo + '.visibility')
            geoEdit = utils.getAttr(grpGeo, 'displayType')
            if not curve and not geo:
                buttonWidget.setStyle('hidden')  # Hidden
            elif (curve and geo and not geoEdit) or (not curve and geo and not geoEdit):
                buttonWidget.setStyle('edit')  # Active + Editable
            elif curve and geo:
                buttonWidget.setStyle('active')  # Active
            elif curve and not geo:
                buttonWidget.setStyle('curve')  # Curve only
            elif geo and not curve:
                buttonWidget.setStyle('geo')  # Geo only
            else:
                buttonWidget.setStyle('empty')
        else:
            buttonWidget.setStyle('empty')

    # --- Update color mode button ---
    if utils.getAttr('gsColorShaderStorageNode', 'colorApplied'):
        WIDGETS['colorMode'].setChecked(True)
    else:
        WIDGETS['colorMode'].setChecked(False)

    # --- Update scale factor window ---
    if mc.workspaceControl(SCALE_FACTOR_UI, q=1, ex=1) and \
            mc.workspaceControl(SCALE_FACTOR_UI, q=1, vis=1):
        sel = mc.ls(sl=1, tr=1, typ='nurbsCurve')
        try:
            if sel and mc.attributeQuery('scaleFactor', n=sel[-1], ex=1):
                scaleFactor = mc.getAttr(sel[-1] + '.scaleFactor')
                if scaleFactor and scaleFactor >= 0.001:
                    WIDGETS['scaleFactorSelectedValue'].setText(str(scaleFactor))
            else:
                WIDGETS['scaleFactorSelectedValue'].setText(str('####'))
        except BaseException:
            if 'scaleFactorSelectedValue' in WIDGETS:
                WIDGETS['scaleFactorSelectedValue'].setText(str('####'))


def onSceneOpenedUpdateLayerCount():
    # Check max layer ID present in the scene
    allLayers = mc.ls(typ="displayLayer")
    filtered = [x for x in allLayers if 'curveGrp_' in x]
    if not filtered:
        return
    layersIDs = []
    for layer in filtered:
        split = layer.split("_")
        try:
            layerID = int(split[1]) if len(split) == 3 else int(split[2])
        except ValueError:
            error = 'Failed to extract layer ID from layer "{}". Display Layer name is corrupted. Please delete corrupted layers and curves.'.format(layer)
            MESSAGE.warning(error)
            continue
        layersIDs.append(layerID)
    maxLayerID = max(layersIDs)

    # Check currently active layer count on the interface
    if 'layerRowsActionGroup' in WIDGETS:
        action = WIDGETS['layerRowsActionGroup'].checkedAction()
        if action is not None:
            checkbox = action.objName
            checkboxNum = re.findall(r'\d+', checkbox)[0]
            activeID = int(checkboxNum) * 10
        else:
            print("Warning: 'layerRowsActionGroup' checkedAction is None.")
            return
    else:
        print("Warning: 'layerRowsActionGroup' not found in WIDGETS")
        return

    # Check the required layer count
    availableIDs = [20, 30, 40, 60, 80]
    availableIDs.append(maxLayerID + 1)
    availableIDs.sort()
    requiredID = availableIDs.index(maxLayerID + 1)
    try:
        requiredLayerNumber = availableIDs[requiredID + 1]
    except Exception as e:
        LOGGER.exception(e)
        return
    if activeID >= requiredLayerNumber:
        return
    WIDGETS['curveGrp0'].setNumberOfLayers(requiredLayerNumber)
    formatControlName = str(requiredLayerNumber)[:1] + "layerRows"
    WIDGETS[formatControlName].setChecked(True)
    updateMainUI()


def saveOptions():  # Save options to optionVar
    LOGGER.info("Saving options")
    qtBooleans = [
        'syncCurveColor',
        'colorizedRegroup',

        'checkerPattern',
        'ignoreLastLayer',
        'syncOutlinerLayerVis',
        'keepCurveAttributes',
        'massBindOption',
        'boundCurvesFollowParent',

        'bindDuplicatesCurves',
        'bindFlipUVs',
        'replacingCurveLayerSelection',
        'populateBlendAttributes',
        'useAutoRefineOnNewCurves',
        'flipUVsAfterMirror',
        'convertInstances',

        'layerNumbersOnly',
        '2layerRows',
        '3layerRows',
        '4layerRows',
        '6layerRows',
        '8layerRows',
        'warpSwitch',
        'enableTooltips',
        'colorOnlyDiffuse',

        'showLayerCollectionsMenu',
        'importIntoANewCollection',
        'ignoreTemplateCollections',
        'groupTemplateCollections',
    ]
    for option in qtBooleans:
        mc.optionVar(iv=['GSCT_' + option, WIDGETS[option].isChecked()])

    # Editor colors
    if 'UVEditorBGColorPicker' in WIDGETS:
        mc.optionVar(sv=['GSCT_UVEditorBGColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorBGColorPicker'].getRGBColors()))])
        mc.optionVar(sv=['GSCT_UVEditorGridColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorGridColorPicker'].getRGBColors()))])
        mc.optionVar(sv=['GSCT_UVEditorFrameColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorFrameColorPicker'].getRGBColors()))])
        mc.optionVar(sv=['GSCT_UVEditorUVCardFillColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorUVCardFillColorPicker'].getRGBColors()))])
        mc.optionVar(sv=['GSCT_UVEditorUVFrameSelectedColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorUVFrameSelectedColorPicker'].getRGBColors()))])
        mc.optionVar(sv=['GSCT_UVEditorUVFrameDeselectedColor',
                         str(utils.colorFrom1to255(WIDGETS['UVEditorUVFrameDeselectedColorPicker'].getRGBColors()))])


def saveScaleFactor(windowName, deleteUI=True):
    sliderValue = mc.floatSliderGrp('GSCT_scaleFactorSlider', q=1, v=1)
    mc.optionVar(fv=('GSCT_globalScaleFactor', sliderValue))

    # Check if scaleFactor node and scale factor attribute exists
    if not mc.objExists('gsScaleFactorStorageNode'):
        mc.scriptNode(n='gsScaleFactorStorageNode')
    if not mc.attributeQuery('scaleFactor', n='gsScaleFactorStorageNode', ex=1):
        mc.addAttr('gsScaleFactorStorageNode', ln='scaleFactor', at='double')

    mc.setAttr('gsScaleFactorStorageNode.scaleFactor', sliderValue)
    if deleteUI:
        mc.deleteUI(windowName)


def getScaleFactor(*_):
    scaleFactor = 1.0
    if mc.objExists('gsScaleFactorStorageNode') and mc.attributeQuery('scaleFactor', n='gsScaleFactorStorageNode', ex=1):
        scaleFactor = mc.getAttr('gsScaleFactorStorageNode.scaleFactor')
    else:
        scaleFactor = mc.optionVar(q=('GSCT_globalScaleFactor'))
    if not scaleFactor or scaleFactor < 0.001:
        MESSAGE.warning("Invalid scale factor. Reverting to default (1.0).")
        scaleFactor = 1.0
    return scaleFactor


def getOption(name):
    return mc.optionVar(q='GSCT_' + name)


def updateLayerThickness():
    """Updates thickness values for all Curves"""
    saveOptions()
    value = mc.optionVar(q='GSCT_globalCurveThickness')
    layerCollectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
    collectionCount = layerCollectionsWidget.count()
    for collectionID in range(collectionCount):
        collection = "%s_" % collectionID if collectionID > 0 else ""
        for layerID in range(80):
            grpCurve = 'curveGrp_%s%s_Curve' % (collection, layerID)
            if not mc.objExists(grpCurve):
                continue
            curves = mc.editDisplayLayerMembers(grpCurve, q=1, fn=1)
            if curves:
                for curve in curves:
                    shape = mc.ls(curve, dag=1, s=1, l=1)[0]
                    mc.setAttr(shape + '.lineWidth', value)
    curveControlUI.updateUI()


def setCurveThickness(curves):
    """Sets curve thickness for provided curves"""
    if not isinstance(curves, list):
        curves = [curves]
    value = mc.optionVar(q='GSCT_globalCurveThickness')
    for crv in curves:
        if isinstance(crv, tuple):
            origShape = mc.ls(crv[0], dag=1, s=1)[0]
            targetShape = mc.ls(crv[1], dag=1, s=1)[0]
            mc.setAttr(targetShape + '.lineWidth', mc.getAttr(origShape + '.lineWidth'))
        else:
            shape = mc.ls(crv, dag=1, s=1)[0]
            mc.setAttr(shape + '.lineWidth', value)


def layerClicked(i):
    """Called when layer button is clicked"""
    mod = utils.getMod()
    if mod == 'Alt':
        toggleLayerVisibility(i)
        updateMainUI()
    elif mod == 'Ctrl+Alt':
        toggleObjVisibility(i, 1)
        updateMainUI()
    elif mod == 'Shift+Ctrl':
        toggleObjVisibility(i, 0)
        updateMainUI()
    elif mod == 'Shift+Alt':
        layersFilterToggle(False, False, "Ctrl")
        toggleLayerVisibility(i)
        updateMainUI()
    elif mod == 'Shift+Ctrl+Alt':
        alwaysOnTopToggleLayer(i)
    else:
        curveLayerSelectObj(i, -1)


def updateScaleFactorWindow():
    if not mc.workspaceControl(SCALE_FACTOR_UI, q=1, ex=1):
        return
    if not mc.workspaceControl(SCALE_FACTOR_UI, q=1, vis=1):
        return

    sel = mc.ls(sl=1, tr=1, typ='nurbsCurve')
    try:
        if sel and mc.attributeQuery('scaleFactor', n=sel[-1], ex=1):
            scaleFactor = mc.getAttr(sel[-1] + '.scaleFactor')
            if scaleFactor and scaleFactor >= 0.001:
                WIDGETS['scaleFactorSelectedValue'].setText(str(scaleFactor))
        else:
            WIDGETS['scaleFactorSelectedValue'].setText(str('####'))
    except BaseException:
        if 'scaleFactorSelectedValue' in WIDGETS:
            WIDGETS['scaleFactorSelectedValue'].setText(str('####'))


def clearLayers(collection=None):
    # type: (str|int) -> None
    """Removes unused layers in selected collection"""
    c = ''
    if collection:
        c = '%s_' % collection
    for i in range(80):
        grpCurve = 'curveGrp_%s%s_Curve' % (c, i)
        grpGeo = 'curveGrp_%s%s_Geo' % (c, i)
        grpInst = 'curveGrp_%s%s_Inst' % (c, i)
        if mc.objExists(grpCurve) and mc.objExists(grpGeo) and mc.objExists(grpInst):
            curves = mc.editDisplayLayerMembers(grpCurve, q=1, fn=1)
            geo = mc.editDisplayLayerMembers(grpGeo, q=1, fn=1)
            instances = mc.editDisplayLayerMembers(grpInst, q=1, fn=1)
            if not curves or not geo or not instances:
                mc.delete(grpCurve)
                mc.delete(grpGeo)
                mc.delete(grpInst)
        else:
            if mc.objExists(grpCurve):
                mc.delete(grpCurve)
            if mc.objExists(grpGeo):
                mc.delete(grpGeo)
            if mc.objExists(grpInst):
                mc.delete(grpInst)


def deleteUnusedLayers(checkButtons=True):
    # type: (bool) -> None
    """Removes unused layers in all collections"""

    collections = utils.getCollectionsSet()
    for i in collections:
        clearLayers(i)
    clearLayers()
    if checkButtons:
        updateMainUI()


def resetSlider():  # Reset Rebuild Curve Slider to default values
    mc.intSliderGrp('gsRebuildSlider', e=1, min=1, max=50, fmx=999, v=1)


def resetControlSliders():  # Reset Curve Control window Sliders to default values
    sliders = curveControlUI.allControls
    for control in sliders:
        if control in WIDGETS:
            slider = WIDGETS[control]
            if "resetMinMax" in dir(slider) and slider.isVisible():
                slider.resetMinMax()


def resetWarpCurvesControls(curve):  # Reset curve control falloffCurveAttr
    if curve == 1:
        mc.falloffCurveAttr('gsCurveControlTwistCurve', e=1, asString="0, 0.5, 0.333, 0.5, 0.667, 0.5, 1, 0.5")
    elif curve == 2:
        mc.falloffCurveAttr('gsCurveControlWidthFalloff', e=1, asString="0, 0.5, 0.333, 0.5, 0.667, 0.5, 1, 0.5")


def curveControlCheckBoxes(box):  # Updates check boxes in Curve Control window
    sel = mc.filterExpand(mc.ls(sl=1, fl=1, o=1), sm=9)
    if not sel:
        curveControlUI.updateUI()
        return 0
    for obj in sel:
        if box == 0:
            if utils.attrExists(obj, 'reverseNormals'):
                mc.setAttr(obj + '.reverseNormals', not WIDGETS['reverseNormals'].isChecked())
        elif box == 1:
            if utils.attrExists(obj, 'reverseNormals'):
                mc.setAttr(obj + '.solidify', WIDGETS['solidify'].isChecked())
        elif box == 2:
            if utils.attrExists(obj, 'LengthLock'):
                mc.setAttr(obj + '.LengthLock', WIDGETS['LengthLock'].isChecked())
        elif box == 3:
            if utils.attrExists(obj, 'flipUV'):
                mc.setAttr(obj + '.flipUV', not WIDGETS['flipUV'].isChecked())


def layersFilterToggle(curve, geo, mod=None, hotkey=False, ignore=None):
    # type: (bool, bool, str|None, bool, None|list[str]) -> None
    """
    Toggles the visibility of the components for all layers (and optionally collections)
    mod - allows to manually pass "Ctrl, Shift etc" hotkey
    hotkey - indicates that the call is a hotkey and should ignore user modifier keys
    ignore - list of ignored hotkey combinations
    """

    if mod is None and not hotkey:
        mod = utils.getMod()

    # Handle ignored hotkeys
    if ignore and mod and mod in ignore:  # TODO: Fix this hotkey-ignore-mod madness
        mod = None

    if mod and (mod in ["Shift", "Shift+Ctrl"]):
        curve = False
        geo = False

    # Handle the hotkey state
    allCollections = False
    if mod and "Ctrl" in mod:
        allCollections = True

    # Handle last layer ignore
    ignoreLastLayer = bool(getOption('ignoreLastLayer'))

    # Sync visibility with the outliner
    outlinerSync = getOption('syncOutlinerLayerVis')

    # Check available collections
    collectionIDs = []
    if allCollections:
        collectionIDs.append('0')
        collectionIDs += list(utils.getCollectionsSet())
    else:
        collectionIDs.append(WIDGETS['layerCollectionsComboBox'].currentIndex())

    # Check for Template Ignore
    if getOption('ignoreTemplateCollections'):
        collectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        currentCollection = collectionsWidget.currentIndex()
        collectionIDs_copy = list(collectionIDs)
        for collection in collectionIDs_copy:
            if "template" in collectionsWidget.itemText(int(collection)).lower() and int(collection) != currentCollection:
                collectionIDs.remove(collection)

    for collection in collectionIDs:
        formattedCollectionID = utils.getFormattedCollectionByID(collection)
        currentLayerNum = WIDGETS['curveGrp0'].LAYERS - 1
        for i in range(80):
            if ignoreLastLayer and i == currentLayerNum:
                continue
            curvesGrp = 'curveGrp_%s%s_Curve' % (formattedCollectionID, i)
            geoGrp = 'curveGrp_%s%s_Geo' % (formattedCollectionID, i)
            instGrp = 'curveGrp_%s%s_Inst' % (formattedCollectionID, i)
            try:
                mc.setAttr(curvesGrp + '.visibility', curve)
                if mc.layerButton(curvesGrp, q=1, ex=1):
                    mc.layerButton(curvesGrp, e=1, lv=curve)
            except BaseException:
                pass
            try:
                mc.setAttr(geoGrp + '.visibility', geo)
                if mc.layerButton(geoGrp, q=1, ex=1):
                    mc.layerButton(geoGrp, e=1, lv=geo)
            except BaseException:
                pass
            try:
                mc.setAttr(instGrp + '.visibility', 0)
                if mc.layerButton(instGrp, q=1, ex=1):
                    mc.layerButton(instGrp, e=1, lv=0)
            except BaseException:
                pass
            if outlinerSync and mc.objExists(curvesGrp):
                groups = []
                layerCurves = mc.editDisplayLayerMembers(curvesGrp, q=1, fn=1)
                if layerCurves:
                    for i in layerCurves:
                        parent = mc.listRelatives(i, p=1, pa=1)
                        if parent:
                            groups += parent
                    if not geo and not curve:
                        for grp in groups:
                            mc.setAttr(grp + '.v', 0)
                    else:
                        for grp in groups:
                            mc.setAttr(grp + '.v', 1)
    updateMainUI()


def applyAxis(axis):
    sel = mc.filterExpand(mc.ls(sl=1, o=1), sm=9)
    if not sel:
        return 0
    for curve in sel:
        if axis == -1:
            if mc.attributeQuery('AxisFlip', n=curve, ex=1):
                mc.setAttr(curve + '.AxisFlip', not mc.getAttr(curve + '.AxisFlip'))
            if mc.attributeQuery('reverseNormals', n=curve, ex=1):
                mc.setAttr(curve + '.reverseNormals', not mc.getAttr(curve + '.reverseNormals'))
            curveControlUI.updateUI()
        elif axis == 0:
            if mc.attributeQuery('Axis', n=curve, ex=1):
                mc.setAttr(curve + '.Axis', 0)
        elif axis == 1:
            if mc.attributeQuery('Axis', n=curve, ex=1):
                mc.setAttr(curve + '.Axis', 1)
        elif axis == 2:
            if mc.attributeQuery('Axis', n=curve, ex=1):
                mc.setAttr(curve + '.Axis', 2)
        elif axis == 3:
            if mc.attributeQuery('Axis', n=curve, ex=1):
                mc.setAttr(curve + '.Axis', 3)


def changeLayerViaOptionMenu():
    layer = WIDGETS['gsLayerSelector'].currentIndex()
    curveAddToLayer(layer)
    if WIDGETS['syncCurveColor'].isChecked():
        toggleColor.syncCurveColors()


def moveLayers(source, target):
    # type: (str, str) -> None
    """Moves the curves from layer to layer within the same collection (via MMB drag)"""
    mc.undoInfo(ock=1, cn='layerDragDropOP')
    try:
        collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
        collection = ''
        if collectionID:
            collection = '%s_' % collectionID
        sourceGrp = re.findall(r'\d+', source)[0]
        targetGrp = re.findall(r'\d+', target)[0]
        curves = mc.editDisplayLayerMembers('curveGrp_%s%s_Curve' % (collection, sourceGrp), q=1, fn=1)
        if utils.getMod() == 'Shift':
            customSel = mc.editDisplayLayerMembers('curveGrp_%s%s_Curve' % (collection, sourceGrp), q=1, fn=1)
            mc.select(customSel, r=1)
            duplicateCurve()
            curveAddToLayer(targetGrp)
        else:
            curveAddToLayer(targetGrp, sourceGrp)
        if curves:
            if mc.objExists('gsColorShaderStorageNode'):
                if mc.getAttr('gsColorShaderStorageNode.colorApplied'):
                    toggleColor.updateColors()
        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()
    except BaseException:
        pass
    mc.undoInfo(cck=1)


### General Functions ###

def subdivideCurve(hk=None):
    sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
    if not sel:
        sel = mc.filterExpand(mc.ls(hl=1, o=1), sm=9)
    if not sel:
        MESSAGE.warningInView('Select at least one compatible card or tube curve.')
        return
    finalCurves = []
    for obj in sel:
        if mc.attributeQuery('Axis', n=obj, ex=1):
            MESSAGE.warning('%s is not compatible with Subdivide Curve command. Skipped.' % obj)
            continue
        geo = selectPart(2, True, obj)
        geo = mc.duplicate(geo)
        mc.sets(geo, forceElement='initialShadingGroup', nw=1)  # set to default material to avoid errors
        subd = mc.polyToSubdiv(geo, ch=0)
        surface = mc.subdToNurbs(subd, ch=0)
        nurbs = mc.listRelatives(surface, c=1, pa=1)
        nurbs = mc.parent(nurbs, w=1)
        mc.rebuildSurface(nurbs, ch=0, rpo=1, rt=6, end=1, kr=1, kcp=0, kc=0, su=16, du=0, sv=5, dv=0, tol=0.01, fr=0,
                          dir=2)
        mc.delete(geo, surface, subd)
        spansU, spansV = mc.getAttr(nurbs[0] + '.spansUV')[0]
        span = 'v' if spansU > spansV else 'u'
        attrs = attributes.getAttr(obj)
        curves = []
        num = mc.intSliderGrp('gsCurvesSlider', q=1, v=1)
        for i in range(0, num):
            x = (float(i) + 1.0) / (float(num) + 1.0)
            if 'WidthX' in attrs:
                x = float(i) / float(num)
            curves.append(mc.duplicateCurve(nurbs[0] + '.%sn[%s]' % (span, x))[0])
        widthValues = {1: 1, 2: 0.666, 3: 0.5, 4: 0.4, 5: 0.333, 6: 0.28, 7: 0.24, 8: 0.213, 9: 0.19, 10: 0.166}
        if 'Width' in attrs:
            attrs['Width'] = attrs['Width'] * widthValues[num]
            attrs['Profile'] = attrs['Profile'] / num
        elif 'WidthX' in attrs:
            attrs['WidthX'] = attrs['WidthX'] * widthValues[num]
            attrs['WidthZ'] = attrs['WidthZ'] * widthValues[num]
        mc.delete(nurbs)
        smoothCurve(curves)
        for curve in curves:
            mc.rebuildCurve(curve, kr=2, s=mc.getAttr(obj + '.spans'))
            if 'Profile' in attrs:
                mc.reverseCurve(curve)
            targetPoints = mc.getAttr(curve + '.cp[:]')
            newCurve = duplicateCurve(customSel=[obj])[0]
            finalCurves.append(newCurve)
            for p in range(0, len(targetPoints)):
                mc.xform('%s.cp[%s]' % (newCurve, p), t=targetPoints[p], wd=1, ws=1)
            attributes.setAttr(newCurve, attrs)
            mc.delete(curve)
        modifier = True if hk == 2 or (hk is None and utils.getMod() == 'Shift') else False
        if not modifier:
            mc.delete(selectPart(0, True, obj))
    mc.select(finalCurves)
    if finalCurves:
        resetCurvePivotPoint()


def cardToCurve():
    """Converts selected geo card to curve or (optionally) Curve Card"""
    sel = mc.filterExpand(mc.ls(sl=1, tr=1, fl=1), sm=12)
    if not sel:
        sel = mc.filterExpand(mc.ls(hl=1, fl=1), sm=12)
    if not sel:
        MESSAGE.warningInView('Select a compatible one sided geometry to convert.')
        return
    finalSel = []
    progress = utils.ProgressBar("Converting cards to curves...", len(sel))
    options = eval(mc.optionVar(q='GSCT_CardToCurveOptions'))

    def getConvertOption(name):
        return options[name] if name in options else True

    currentUnit = mc.currentUnit(q=1, linear=1)
    if currentUnit != "cm" and getConvertOption('gsCardToCurve_profile'):
        mc.confirmDialog(
            title="Unit Warning",
            message="Card to Curve 'Profile' matching is only supported with centimeters (cm) as scene units.\n\n" + 
                    "You are using '{}'.\n\n".format(currentUnit) + 
                    "Disable Profile Attribute matching or switch to centimiters in Maya Settings."
        )
        progress.end()
        return

    for obj in sel:
        if progress.tick(1):
            break
        allFaces = "{}.f[*]".format(obj)
        perimeterEdges = mc.polyListComponentConversion(allFaces, ff=1, te=1, bo=1)
        perimeterVerts = mc.ls(mc.polyListComponentConversion(perimeterEdges, fe=1, tv=1), fl=1)
        cornerVerts = []
        for vert in perimeterVerts:
            expandedEdge = mc.ls(mc.polyListComponentConversion(vert, fv=1, te=1), fl=1)
            if len(expandedEdge) == 2:
                cornerVerts.append(vert)

        if not cornerVerts and len(cornerVerts) != 4:
            MESSAGE.warningInView('Object "{}" is not a one-sided card. Skipping.'.format(obj))
            continue

        # Find closest point to cornerVerts[0]
        closestPoint = None
        om_distance = 0
        om_cornerVert = om.MFloatPoint(mc.pointPosition(cornerVerts[0], w=1))
        for i in range(1, len(cornerVerts)):
            om_otherVert = om.MFloatPoint(mc.pointPosition(cornerVerts[i], w=1))
            om_distance_new = om_cornerVert.distanceTo(om_otherVert)
            if i == 1 or om_distance_new < om_distance:
                om_distance = om_distance_new
                closestPoint = cornerVerts[i]

        # Closest corner verts
        firstCornerVertPair = [cornerVerts[0], closestPoint]
        secondCornerVertPair = list(set(cornerVerts) - set(firstCornerVertPair))

        origFirstCornerDistance = om_cornerVert.distanceTo(om.MFloatPoint(mc.pointPosition(closestPoint, w=1)))
        origSecondCornerDistance = om.MFloatPoint(
            mc.pointPosition(secondCornerVertPair[0], w=1)).distanceTo(om.MFloatPoint(mc.pointPosition(secondCornerVertPair[1], w=1)))

        if len(firstCornerVertPair) != 2 or len(secondCornerVertPair) != 2:
            MESSAGE.warningInView('Object "{}" has wrong topology. Skipped.'.format(obj))
            continue

        # Verts between closest corners
        firstSideVertLoop = utils.polySelectSp(firstCornerVertPair, obj)
        secondSideVertLoop = utils.polySelectSp(secondCornerVertPair, obj)

        # Edges between closest corners if there are no width spans
        firstSideEdgeLoop = mc.ls(mc.polyListComponentConversion(firstCornerVertPair, fv=1, te=1, internal=1), fl=1)
        secondSideEdgeLoop = mc.ls(mc.polyListComponentConversion(secondCornerVertPair, fv=1, te=1, internal=1), fl=1)

        # Edges between closest corners if there ARE width spans
        if not firstSideEdgeLoop:
            firstSideEdgeLoop = mc.ls(mc.polyListComponentConversion(firstSideVertLoop, fv=1, te=1, internal=1), fl=1)
        if not secondSideEdgeLoop:
            secondSideEdgeLoop = mc.ls(mc.polyListComponentConversion(secondSideVertLoop, fv=1, te=1, internal=1), fl=1)

        # Find the first long edge
        # TODO: See if there is a need for those test loops
        testVertLoop1 = utils.polySelectSp([firstCornerVertPair[0], secondCornerVertPair[0]], obj)
        testVertLoop2 = utils.polySelectSp([firstCornerVertPair[0], secondCornerVertPair[1]], obj)
        firstLongEdge = mc.ls(mc.polyListComponentConversion(
            min(testVertLoop1, testVertLoop2, key=lambda v: len(v)), fv=1, te=1, internal=1), fl=1)

        # Open Edges
        edges = mc.ls(mc.polyListComponentConversion(firstCornerVertPair[0], fv=1, te=1), fl=1)
        openEdge = mc.ls(mc.polySelectSp(edges, q=1, loop=1), fl=1)

        # Second long edge
        secondLongEdge = list(set(openEdge) - set(firstLongEdge + firstSideEdgeLoop + secondSideEdgeLoop))

        # Select the longest edges and convert them
        mc.select(firstLongEdge + secondLongEdge, r=1)
        edgeToCurve(enableProgressBar=False)
        curves = mc.ls(sl=1, tr=1)
        pathCurve = None
        if len(curves) >= 2:
            loft = mc.loft(curves, ss=2)
            finalCurve = mc.duplicateCurve(loft[0] + '.u[0.5]', ch=0)
            finalCurve = mc.rename(finalCurve[0], 'convertedCurve#')
            mc.delete(curves, loft)
            pathCurve = finalCurve

        # ------------- Reversing -------------
        if getConvertOption('gsCardToCurve_reverseCurve'):
            pathCurve = mc.reverseCurve(pathCurve, ch=0, rpo=1)[0]

        """Converting to cards, orienting and adjusting to the original (optional)"""
        if not mc.optionVar(q='GSCT_CardToCurveOutputType'):
            # ------------- Converting -------------
            mc.select(pathCurve, r=1)
            if not mc.optionVar(q='GSCT_CardToCurveCardType'):  # Warp
                pathCurve = create.multiple(0, hk=True, progressBar=False, keepAttrs=False)[0]
            else:  # Extrude
                pathCurve = create.multiple(-2, hk=True, progressBar=False, keepAttrs=False)[0]

            if mc.attributeQuery('scaleFactor', n=pathCurve, ex=1):
                scaleFactor = mc.getAttr(pathCurve + '.scaleFactor')
            else:
                scaleFactor = 1.0

            newGeo = selectPart(2, True, pathCurve)[0]
            om_sel = om.MSelectionList()
            om_sel.add(newGeo)
            om_mesh = om.MFnMesh(om_sel.getDagPath(0))
            """Adjust the resulting card to closely match the target geo"""
            # ------------- Orienting -------------
            firstCv = '%s.cv[0]' % pathCurve
            if getConvertOption('gsCardToCurve_orientation'):
                pos = mc.pointPosition(firstCv)
                om_pos = om.MPoint(pos)
                targetClosestPointNormal = utils.getClosestPointAndNormal(obj, pos)[1]
                orientation = pathCurve + '.Orientation'
                prevDiff = 360
                currentDiff = 360
                i = 0
                guesses = []
                while (currentDiff >= 1) and (i <= 5):
                    i += 1
                    currentOrien = mc.getAttr(orientation)
                    om_cardFaceNormal = om_mesh.getClosestPointAndNormal(om_pos, space=om.MSpace.kWorld)[1]
                    currentDiff = om_cardFaceNormal.angle(targetClosestPointNormal) * 180 / math.pi % 360
                    guesses.append((currentDiff, currentOrien))
                    if currentDiff > prevDiff:
                        guess = currentOrien - currentDiff
                    else:
                        guess = currentOrien + currentDiff
                    prevDiff = currentDiff
                    nextOrien = guess
                    mc.setAttr(orientation, nextOrien % 360)
                # Setting the best guess as the final orientation
                finalOrientation = min(guesses, key=lambda t: t[0])[1]
                mc.setAttr(orientation, finalOrientation)

            # ------------- Width -------------
            # BUG: Fix width calculation to be based on the widest part of the card, not on some average value
            if getConvertOption('gsCardToCurve_width'):
                allFaces = "{}.f[*]".format(newGeo)
                perimeterEdges = mc.polyListComponentConversion(allFaces, ff=1, te=1, bo=1)
                perimeterVerts = mc.ls(mc.polyListComponentConversion(perimeterEdges, fe=1, tv=1), fl=1)
                cornerVerts = []
                for vert in perimeterVerts:
                    expandedEdge = mc.ls(mc.polyListComponentConversion(vert, fv=1, te=1), fl=1)
                    if len(expandedEdge) == 2:
                        cornerVerts.append(vert)
                closestPoint = None
                om_distance = 0
                om_cornerVert = om.MFloatPoint(mc.pointPosition(cornerVerts[0], w=1))
                for i in range(1, len(cornerVerts)):
                    om_otherVert = om.MFloatPoint(mc.pointPosition(cornerVerts[i], w=1))
                    om_distance_new = om_cornerVert.distanceTo(om_otherVert)
                    if i == 1 or om_distance_new < om_distance:
                        om_distance = om_distance_new
                        closestPoint = cornerVerts[i]
                # Closest corner verts
                firstCornerVertPair = [cornerVerts[0], closestPoint]
                secondCornerVertPair = list(set(cornerVerts) - set(firstCornerVertPair))
                newFirstCornerDistance = om_cornerVert.distanceTo(om.MFloatPoint(mc.pointPosition(closestPoint, w=1)))
                newWidth = abs(origFirstCornerDistance / newFirstCornerDistance)
                mc.setAttr(pathCurve + '.Width', newWidth)
            # ------------- Taper -------------
            if getConvertOption('gsCardToCurve_taper'):
                taper = origSecondCornerDistance / origFirstCornerDistance
                mc.setAttr(pathCurve + '.Taper', taper)

            # ------------- Twist -------------
            lastCV = '%s.cv[%s]' % (pathCurve, mc.getAttr(pathCurve + '.spans') + 2)
            if getConvertOption('gsCardToCurve_twist'):
                pos = mc.pointPosition(lastCV)
                om_pos = om.MPoint(pos)
                targetClosestPointNormal = utils.getClosestPointAndNormal(obj, pos)[1]
                twist = pathCurve + '.Twist'
                prevDiff = 180
                currentDiff = 180
                i = 0
                guesses = []
                while (currentDiff >= 1) and (i <= 5):
                    i += 1
                    currentTwist = mc.getAttr(twist)
                    om_cardFaceNormal = om_mesh.getClosestPointAndNormal(om_pos, space=om.MSpace.kWorld)[1]
                    currentDiff = om_cardFaceNormal.angle(targetClosestPointNormal) * 180 / math.pi
                    guesses.append((currentDiff, currentTwist))
                    if currentDiff > prevDiff:
                        guess = currentTwist - currentDiff
                    else:
                        guess = currentTwist + currentDiff
                    prevDiff = currentDiff
                    nextTwist = guess
                    mc.setAttr(twist, nextTwist)
                # Setting the best guess as the final orientation
                finalTwist = min(guesses, key=lambda t: t[0])[1]
                mc.setAttr(pathCurve + '.Twist', finalTwist)

            # ------------- Profile -------------
            # TODO: Possibly add profile curve matching for warp cards
            if getConvertOption('gsCardToCurve_profile'):
                # First iteration of profile
                firstCVpos = mc.pointPosition(firstCv, w=1)
                firstCVom_pos = om.MPoint(firstCVpos)
                firstCVtargetClosestPoint = utils.getClosestPointAndNormal(obj, firstCVpos)[0]
                firstProfileDistance = firstCVom_pos.distanceTo(firstCVtargetClosestPoint)
                lastCVpos = mc.pointPosition(lastCV, w=1)
                lastCVom_pos = om.MPoint(lastCVpos)
                lastCVtargetClosestPoint = utils.getClosestPointAndNormal(obj, lastCVpos)[0]
                lastProfileDistance = lastCVom_pos.distanceTo(lastCVtargetClosestPoint)
                maxDist = max(firstProfileDistance, lastProfileDistance)
                mc.setAttr(pathCurve + '.Profile',  maxDist / scaleFactor * 1.4)
                # Additional check in case the card was flipped in the wrong direction
                firstCVtargetClosestPoint_2 = utils.getClosestPointAndNormal(newGeo, firstCVpos)[0]
                lastCVtargetClosestPoint_2 = utils.getClosestPointAndNormal(newGeo, lastCVpos)[0]
                firstTotalDistance = firstCVtargetClosestPoint.distanceTo(firstCVtargetClosestPoint_2)
                lastTotalDistance = lastCVtargetClosestPoint.distanceTo(lastCVtargetClosestPoint_2)
                if firstTotalDistance > firstProfileDistance and lastTotalDistance > lastProfileDistance:
                    mc.setAttr(pathCurve + '.Profile',  mc.getAttr(pathCurve + '.Profile') * -1)

            # ------------- Material transfer -------------
            if getConvertOption('gsCardToCurve_material'):
                mc.sets(newGeo, forceElement=list(utils.getShader(obj))[0])

            # ------------- UV Approximation -------------
            if getConvertOption('gsCardToCurve_UVs'):
                uVals, vVals = mc.polyEvaluate(obj, b2=True)
                uMin, uMax = uVals
                vMin, vMax = vVals
                moveU = abs(uMax - uMin) / 2 + uMin - 0.5
                if getConvertOption('gsCardToCurve_verticalFlip'):
                    mc.setAttr(pathCurve + '.rotateUV', 180)
                    moveV = vMin + (vMax - vMin) - 1
                    mc.setAttr(pathCurve + '.flipUV', not mc.getAttr(pathCurve + '.flipUV'))
                else:
                    moveV = vMin
                if getConvertOption('gsCardToCurve_horizontalFlip'):
                    mc.setAttr(pathCurve + '.flipUV', not mc.getAttr(pathCurve + '.flipUV'))
                scaleU = abs(uMax - uMin)
                scaleV = abs(vMax - vMin)
                mc.setAttr(pathCurve + '.moveU', moveU)
                mc.setAttr(pathCurve + '.moveV', moveV)
                mc.setAttr(pathCurve + '.scaleU', scaleU)
                mc.setAttr(pathCurve + '.scaleV', scaleV)

        if pathCurve:
            finalSel.append(pathCurve)
    progress.end()
    mc.select(finalSel, r=1)
    resetCurvePivotPoint()


def updateLattice(values, customTarget=None):
    # TODO: Add curve fitting for better overall experience with the graph

    selection = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)

    if not selection:
        selection = mc.filterExpand(mc.ls(hl=1, o=1), sm=9)
    if not selection and not customTarget:
        return
    if customTarget:
        selection = [customTarget]

    for sel in selection:
        if not mc.attributeQuery('latticeMessage', n=sel, ex=1):
            continue
        lattice = mc.listConnections(sel + '.latticeMessage')
        if not lattice:
            continue
        else:
            lattice = lattice[0]

        graphValues = utils.fromStringToDouble2(values)

        latticeDiv = mc.getAttr(lattice + '.sDivisions')

        if len(graphValues) != latticeDiv:
            ffd = mc.listConnections(lattice + '.latticeOutput')
            mc.lattice(ffd, e=1, rt=1)
            mc.lattice(ffd, e=1, dv=[len(graphValues), 2, 2])
            latticeDiv = mc.getAttr(lattice + '.sDivisions')
            curveControlUI.updateUI()

        currentPoints = []
        initialPoints = []
        for i in range(latticeDiv):
            currentPoints.append(mc.pointPosition(lattice + '.pt[%s][1][0]' % (i), l=1))
        for i in range(mc.getAttr(sel + '.initialLatticePoints', s=1)):
            initialPoints.append(mc.getAttr(sel + '.initialLatticePoints[%s]' % i)[0])

        newPoints = []

        for i in range(latticeDiv):
            x = mt.lerp(graphValues[i][0], 0.5, -0.5, 1, 0)
            y = mt.lerp(graphValues[i][1], 1.5, -0.5, 1, 0)
            newPoints.append((x, y))

        for i in range(len(newPoints)):
            mc.move(newPoints[i][0], newPoints[i][1], lattice + '.pt[%s][1][0]' % i, xy=1, ls=1)
            mc.move(newPoints[i][0], newPoints[i][1], lattice + '.pt[%s][1][1]' % i, xy=1, ls=1)
            mc.move(newPoints[i][0], newPoints[i][1], lattice + '.pt[%s][0][0]' % i, x=1, ls=1)
            mc.move(newPoints[i][0], newPoints[i][1], lattice + '.pt[%s][0][1]' % i, x=1, ls=1)
        curveControlUI.updateUI()


def getLatticeValues(targetCurve):
    if not mc.attributeQuery('latticeMessage', n=targetCurve, ex=1):
        return
    lattice = mc.listConnections(targetCurve + '.latticeMessage')
    if lattice:
        lattice = lattice[0]
    else:
        return
    latticeDiv = mc.getAttr(lattice + '.sDivisions')
    currentPoints = []
    initialPoints = []
    for i in range(latticeDiv):
        currentPoints.append(mc.pointPosition(lattice + '.pt[%s][1][0]' % (i), l=1))
    for i in range(mc.getAttr(targetCurve + '.initialLatticePoints', s=1)):
        initialPoints.append(mc.getAttr(targetCurve + '.initialLatticePoints[%s]' % i)[0])

    newPoints = []

    for i in range(latticeDiv):
        x = mt.lerp(currentPoints[i][0], 1, 0, 0.5, -0.5)
        y = mt.lerp(currentPoints[i][1], 1, 0, 1.5, -0.5)
        newPoints.append((x, y))
    return newPoints


def equalizeProfileCurve(manual=False):
    if WIDGETS['autoEqualizeSwitchOff'].isChecked() and not manual:
        return
    currentProfile = WIDGETS['profileCurve'].getGraph()
    if currentProfile:
        graphValues = utils.fromStringToDouble2(currentProfile)
        for i in range(len(graphValues)):
            graphValues[i][0] = float(i) / (len(graphValues) - 1)
        newString = utils.fromDouble2ToString(graphValues)
        WIDGETS['profileCurve'].setGraph(newString)
        updateLattice(newString)


def resetProfileCurve():
    currentProfile = WIDGETS['profileCurve'].getGraph()
    if currentProfile:
        graphValues = utils.fromStringToDouble2(currentProfile)
        for i in range(len(graphValues)):
            graphValues[i][1] = 0.5
        newString = utils.fromDouble2ToString(graphValues)
        WIDGETS['profileCurve'].setGraph(newString)
        updateLattice(newString)


def transferProfileCurve(source, target):
    if mc.attributeQuery('latticeMessage', n=target, ex=1) and mc.attributeQuery('latticeMessage', n=source, ex=1):
        lattice = mc.listConnections(source + '.latticeMessage')
        if lattice:
            latticeDiv = mc.getAttr(lattice[0] + '.sDivisions')
            if latticeDiv:
                currentPoints = []
                if lattice:
                    for i in range(latticeDiv):
                        currentPoints.append(mc.pointPosition(lattice[0] + '.pt[%s][1][0]' % (i), l=1))
                newPoints = []
                for i in range(latticeDiv):
                    x = mt.lerp(currentPoints[i][0], 1, 0, 0.5, -0.5)
                    y = mt.lerp(currentPoints[i][1], 1, 0, 1.5, -0.5)
                    newPoints.append((x, y))

                graphPoints = utils.fromDouble2ToString(newPoints)

                updateLattice(graphPoints, target)


def blendProfileCurve(source, target, ratio):
    if mc.attributeQuery('latticeMessage', n=source, ex=1) and mc.attributeQuery('latticeMessage', n=target, ex=1):

        sourceLattice = mc.listConnections(source + '.latticeMessage')
        if sourceLattice:
            sourceLatticeDiv = mc.getAttr(sourceLattice[0] + '.sDivisions')
            sourcePoints = []
            if sourceLatticeDiv:
                if sourceLattice:
                    for i in range(sourceLatticeDiv):
                        point = mc.pointPosition(sourceLattice[0] + '.pt[%s][1][0]' % (i), l=1)
                        x = mt.lerp(point[0], 1, 0, 0.5, -0.5)
                        y = mt.lerp(point[1], 1, 0, 1.5, -0.5)
                        sourcePoints.append((x, y))

            targetLattice = mc.listConnections(target + '.latticeMessage')
            if not targetLattice:
                return None
            targetLatticeDiv = mc.getAttr(targetLattice[0] + '.sDivisions')
            targetPoints = []
            if targetLatticeDiv:
                if targetLattice:
                    for i in range(targetLatticeDiv):
                        point = mc.pointPosition(targetLattice[0] + '.pt[%s][1][0]' % (i), l=1)
                        x = mt.lerp(point[0], 1, 0, 0.5, -0.5)
                        y = mt.lerp(point[1], 1, 0, 1.5, -0.5)
                        targetPoints.append((x, y))

            # Add placeholder nodes if needed
            if sourceLatticeDiv > targetLatticeDiv:
                for i in range(sourceLatticeDiv - targetLatticeDiv):
                    position = 1 / sourceLatticeDiv * (targetLatticeDiv + i)
                    targetPoints.append([position, 0.5])

            blendResult = [[sourcePoints[i][0], mt.lerp(ratio, sourcePoints[i][1], targetPoints[i][1])]
                           for i in range(min(len(sourcePoints), len(targetPoints)))]

            finalPoints = utils.fromDouble2ToString(blendResult)
            return finalPoints


def regroupByLayer(groupCustomCollections=None):
    # type: (None|set) -> None
    """
    Regroup all the curves in all layers and collections in the outliner
    Optionally regroups only passed collection IDs
    """
    def getCustomName(i, nameDict):
        name = 'CT_Layer'
        customLayerName = nameDict[i]
        if customLayerName:
            name = customLayerName
        return name

    templateCollections = []
    if groupCustomCollections:
        collections = set(groupCustomCollections)
    else:
        collections = utils.getCollectionsSet()
        collections.add('0')
        if getOption('groupTemplateCollections'):
            collectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
            for collection in collections.copy():
                if "template" in collectionsWidget.itemText(int(collection)).lower():
                    collections.remove(collection)
                    templateCollections.append(collection)

    toggleColor.checkColorStorageNode()
    counter = 0
    deletedGroupsCounter = 0
    previousGroups = set()
    colorDict = dict(eval(mc.getAttr(toggleColor.STORAGE_NODE + '.layerColor')))
    nameDict = dict(eval(mc.getAttr(toggleColor.STORAGE_NODE + '.layerName')))
    hasCollections = len(collections) > 1
    for c in sorted(list(collections)):
        for i in range(80):  # Iterate over existing groups and layers
            name = getCustomName(i, nameDict)
            if hasCollections:
                name = "%s_%s" % (WIDGETS['layerCollectionsComboBox'].itemText(int(c)).replace(' ', '_'), name)
            layerName = '%s_%s' % (name, i)
            if groupCustomCollections:
                layerName = 'CT_Templates'
            grpCurve = 'curveGrp_%s%s_Curve' % (utils.getFormattedCollectionByID(c), i)
            if not mc.objExists(layerName):  # Create groups if needed
                mc.createNode('transform', n=layerName)
            else:
                if mc.nodeType(layerName) != 'transform':
                    mc.createNode('transform', n=layerName)
            if mc.objExists(grpCurve):
                curves = mc.editDisplayLayerMembers(grpCurve, q=1, fn=1)
                if not curves:
                    continue

                if WIDGETS['colorizedRegroup'].isChecked():
                    getClr = colorDict[i]
                    mc.setAttr(layerName + '.useOutlinerColor', 1)
                    mc.setAttr(layerName + '.outlinerColor', *getClr, typ='float3')
                else:
                    mc.setAttr(layerName + '.useOutlinerColor', 0)

                for curve in curves:
                    curve = mc.ls(curve, l=1)
                    if curve:
                        curve = curve[0]
                    else:
                        continue
                    if mc.attributeQuery('gsmessage', n=curve, ex=1) and mc.connectionInfo(curve + '.gsmessage', id=1):
                        continue
                    counter += 1
                    grp = selectPart(0, True, curve)

                    topGrp = mc.listRelatives(grp, p=1, pa=1)
                    if topGrp:
                        previousGroups.add(topGrp[0])
                        if topGrp[0] != layerName:
                            mc.parent(grp, layerName)
                    else:
                        mc.parent(grp, layerName)
    mc.setAttr(toggleColor.STORAGE_NODE + '.layerColor', str(colorDict), typ='string')

    for ele in previousGroups:  # Delete any previous empty groups that exist
        children = mc.listRelatives(ele, c=1, pa=1)
        if not children:
            deletedGroupsCounter += 1
            mc.delete(ele)
    for c in collections:
        for i in range(80):  # Remove Generated empty groups
            name = getCustomName(i, nameDict)
            if hasCollections:
                name = "%s_%s" % (WIDGETS['layerCollectionsComboBox'].itemText(int(c)).replace(' ', '_'), name)
            layerName = '%s_%s' % (name, i)
            if mc.objExists(layerName) and (mc.nodeType(layerName) == 'transform'):
                rel = mc.listRelatives(layerName, c=1, pa=1)
                if rel and len(rel) == 0:
                    mc.delete(layerName)
                elif not rel:
                    mc.delete(layerName)

    reorderingList = []
    for c in list(collections):
        for i in range(80):  # Reorder groups
            name = getCustomName(i, nameDict)
            if hasCollections:
                name = "%s_%s" % (WIDGETS['layerCollectionsComboBox'].itemText(int(c)).replace(' ', '_'), name)
            if mc.objExists('%s_%s' % (name, i)):
                reorderingList.append('%s_%s' % (name, i))
    for ele in reorderingList:
        mc.reorder(ele, b=1)

    mc.select(cl=1)

    deletedGroupsMsg = ''
    if len(previousGroups) > 0:
        deletedGroupsMsg = ' and deleted %s empty layer(s).' % deletedGroupsCounter
    if templateCollections:
        regroupByLayer(templateCollections)
    if groupCustomCollections:
        MESSAGE.printInView('Regrouped %s templates%s' % (counter, deletedGroupsMsg))
    else:
        MESSAGE.printInView('Regrouped %s curve(s)%s' % (counter, deletedGroupsMsg))


def mirrorHair(axis, flip=False):
    sel = mc.filterExpand(mc.ls(sl=1), sm=9)
    if not sel:
        sel = mc.ls(hl=1, o=1)
    if not sel:
        MESSAGE.warningInView('Select compatible curves.')
        return
    mirrorRadio = WIDGETS['mirrorRadio'].isChecked()
    option = 'Mirroring' if mirrorRadio else 'Flipping'
    if flip:
        option = 'Flipping'
    axisDict = {
        0: [-1, 1, 1],
        1: [1, -1, 1],
        2: [1, 1, -1],
    }
    if option == 'Mirroring':
        newCrv = duplicateCurve(sel)
    else:
        newCrv = sel
    filteredCurves = []
    for crv in newCrv:
        # originalProfile = None
        originalProfileVector = None
        if mc.attributeQuery("Profile", n=crv, ex=1):
            originalProfile = mc.getAttr(crv + '.Profile')
            mc.setAttr(crv + '.Profile', math.copysign(2, originalProfile))
            firstCv = '%s.cv[0]' % crv
            pos = mc.pointPosition(firstCv)
            originalProfileVector = utils.getMiddleVertAndNormal(crv, selectPart(2, True, crv)[0], pos)
            mc.setAttr(crv + '.Profile', originalProfile)
        attrs = utils.resetAndReturnAttrs(crv)
        attrs.append(originalProfileVector)
        # attrs.append(originalProfile)
        filteredCurves.append(attrs)

    if filteredCurves:
        mc.scale(axisDict[axis][0],
                 axisDict[axis][1],
                 axisDict[axis][2],
                 [i[0] for i in filteredCurves],
                 a=1, ws=1, p=[0, 0, 0])

    # Init progress bar
    progress = utils.ProgressBar("Mirroring...", len(filteredCurves))

    # Fix orientation
    for crv in filteredCurves:
        if progress.tick(1):
            break
        curve = crv[0]
        firstCv = '%s.cv[0]' % curve
        pos = mc.pointPosition(firstCv)
        om_pos = om.MPoint(pos)
        targetVec = om.MVector(
            crv[1][0] * axisDict[axis][0],
            crv[1][1] * axisDict[axis][1],
            crv[1][2] * axisDict[axis][2]
        )
        om_sel = om.MSelectionList()
        geo = selectPart(2, True, curve)[0]
        om_sel.add(geo)
        om_mesh = om.MFnMesh(om_sel.getDagPath(0))
        orientation = curve + '.Orientation'
        prevDiff = 360
        currentDiff = 360
        iterator = 0
        maxIterations = 10
        angleTolerance = 0.1

        guesses = []

        while (prevDiff >= angleTolerance) and (iterator <= maxIterations):
            iterator += 1
            om_cardFaceNormal = om_mesh.getClosestPointAndNormal(om_pos, space=om.MSpace.kWorld)[1]
            currentDiff = om_cardFaceNormal.angle(targetVec) * 180.0 / math.pi
            currentOrien = mc.getAttr(orientation)

            guesses.append((currentDiff, currentOrien))

            if currentDiff > prevDiff:
                guess = currentOrien - currentDiff
            else:
                guess = currentOrien + currentDiff
            prevDiff = currentDiff

            mc.setAttr(orientation, guess % 360.0)

        # Setting the best guess as the final orientation
        finalOrientation = min(guesses, key=lambda t: t[0])[1]
        mc.setAttr(orientation, finalOrientation % 360.0)

        # Invert graph
        if crv[6]:
            invertedTwistGraph = crv[6][0]
            widthGraph = crv[6][1]
            if invertedTwistGraph[-1] != 'twistCurve':
                invertedTwistGraph = crv[6][1]
                widthGraph = crv[6][0]
            for i in range(len(invertedTwistGraph) - 1):
                invertedTwistGraph[i] = (invertedTwistGraph[i][0], 1 - invertedTwistGraph[i][1])
            attributes.setMultiInst(crv[0], invertedTwistGraph)  # Inverting Twist Graph
            attributes.setMultiInst(crv[0], widthGraph)  # Setting Width Graph Back

        # Restore parameters
        if crv[2] and crv[2] > 10:
            mc.setAttr(curve + '.lengthDivisions', crv[2])
        if crv[3] and crv[3] > 2:
            mc.setAttr(curve + '.widthDivisions', crv[3])
        if crv[4] and crv[4] != 0:
            mc.setAttr(curve + '.Twist', crv[4] * -1)
        if crv[5] and crv[5] != 0:
            mc.setAttr(curve + '.invTwist', crv[5] * -1)

        # Fix profile if needed
        if crv[7]:
            originalProfile = mc.getAttr(curve + '.Profile')
            mc.setAttr(curve + '.Profile', math.copysign(2, originalProfile))
            firstCvVec = om.MVector(om_pos)

            expectedVertex = om.MVector(
                crv[7][0][0] * axisDict[axis][0],
                crv[7][0][1] * axisDict[axis][1],
                crv[7][0][2] * axisDict[axis][2]
            )
            expectedVector = om.MVector(
                crv[7][1][0] * axisDict[axis][0],
                crv[7][1][1] * axisDict[axis][1],
                crv[7][1][2] * axisDict[axis][2]
            )
            profileClosestVertexAndNormal = utils.getMiddleVertAndNormal(curve, selectPart(2, True, curve)[0], firstCvVec)

            # Checking if normals of the flat card are correct. If not, flip the card 180 deg.
            normalCheck = expectedVector.angle(profileClosestVertexAndNormal[1]) * 180.0 / math.pi
            if abs(normalCheck) >= 90:
                mc.setAttr(curve + ".Orientation", (mc.getAttr(curve + ".Orientation") + 180.0) % 360.0)

            # Checking if the angle between two middle vertices is correct. If not, invert the profile.
            angleBetween = (firstCvVec - expectedVertex).angle(firstCvVec - om.MVector(profileClosestVertexAndNormal[0])) * 180.0 / math.pi
            newProfile = originalProfile * -1 if abs(angleBetween) >= 90 else originalProfile
            mc.setAttr(curve + ".Profile", newProfile)

        # Flip UVs
        if getOption('flipUVsAfterMirror') and mc.attributeQuery('flipUV', n=curve, ex=1):
            mc.setAttr(curve + '.flipUV', not mc.getAttr(curve + '.flipUV'))

        resetCurvePivotPoint()
    progress.end()
    LOGGER.info("Mirror Finished")


def renameSelected():
    sel = sorted(mc.ls(sl=1, tr=1))
    for obj in sel:
        grp = selectPart(0, True, obj)
        if grp:
            try:
                newName = WIDGETS['selectedObjectName'].text()
                mc.rename(grp, newName + '#')
            except BaseException:
                MESSAGE.warning('Some items were skipped')
    curveControlUI.updateUI()


def resetCurvePivotPoint(hk=None, customCurves=None):  # Reset Curve Pivot
    # type: (None|int, None|list[str]|str) -> None
    """Resets pivot point on selected curves or passed as customCurves"""
    if customCurves:
        sel = customCurves
    else:
        sel = mc.filterExpand(mc.ls(sl=1, tr=1, l=1), sm=9)
    if not sel:
        MESSAGE.warningInView('Select at least one Curve')
        return

    # Get modifier
    shift = utils.getMod()
    mod = True if hk == 2 or (hk is None and shift == 'Shift') else False

    for selElement in sel:
        nt = mc.nodeType(mc.listRelatives(selElement, c=1, pa=1))
        if nt != 'nurbsCurve' and nt != 'bezierCurve':
            continue
        mc.select(selElement)
        transforms = mc.xform(selElement, q=1, t=1)
        curve = mc.listRelatives(selElement, c=1, pa=1)
        cvNum = '0'
        if mod:
            cvNum = str(mc.getAttr(selElement + '.controlPoints', s=1) - 1)
        cv = mc.pointPosition((curve[0] + ".cv[" + cvNum + "]"), w=1)
        mc.xform(ws=1, piv=(transforms[0], transforms[1], transforms[2]))
        mc.xform(ws=1, piv=(cv[0], cv[1], cv[2]))
    mc.manipMoveContext('Move', e=1, mode=0)
    mc.manipRotateContext('Rotate', e=1, mode=0)
    mc.manipScaleContext('Scale', e=1, mode=0)
    mc.select(sel)


def selectGeoCurveUV():
    curve = mc.ls(sl=1, tr=1)
    geo = selectPart(2, True, curve[0])[0]
    mc.select(geo, r=1)
    mc.select(curve, add=1)


def toggleGeoEdit():  # Toggle Geometry Edit Hotkey
    value = None
    for i in range(80):
        geo = 'curveGrp_%s_Geo' % i
        if (utils.attrExists(geo, 'displayType')):
            if value is None:
                value = mc.getAttr(geo + '.displayType')
            if value == 2:
                mc.setAttr(geo + '.displayType', 0)
            else:
                mc.setAttr(geo + '.displayType', 2)
    updateMainUI()


def extractCurveGeo(layerNum, checkButtons=True):
    # type: (str|int, bool) -> None
    """Extract Geo from single Layer via marking menu"""

    create.initialize()

    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    collection = utils.getFormattedCollectionByID(collectionID)

    geo = "curveGrp_%s%s_Geo" % (collection, layerNum)
    curve = "curveGrp_%s%s_Curve" % (collection, layerNum)

    if toggleColor.colorEnabled():
        toggleColor.disableColors()

    result = extractGeo(geo, curve, layerNum)
    if not result:
        MESSAGE.warning("Layer is Empty")

    if checkButtons:
        updateMainUI()


def extractGeo(geoLayerName, curveLayerName, layerNum, hideLayer=True):
    # type: (str, str, int, bool) -> list[str]
    """Extracts geo from layer names, optionally hides the original layers"""
    outlinerSync = getOption('syncOutlinerLayerVis')
    if mc.objExists(geoLayerName):
        groups = []
        if outlinerSync:
            layerCurves = mc.editDisplayLayerMembers(curveLayerName, q=1, fn=1)
            if not layerCurves:
                return
            for i in layerCurves:
                parent = mc.listRelatives(i, p=1, pa=1)
                if parent:
                    groups += parent
        if hideLayer:
            if outlinerSync:
                for grp in groups:
                    mc.setAttr(grp + '.v', 0)
            mc.setAttr(geoLayerName + '.visibility', 0)
            mc.setAttr(curveLayerName + '.visibility', 0)
        if mc.layerButton(geoLayerName, q=1, ex=1):
            mc.layerButton(geoLayerName, e=1, lv=0)
        if mc.layerButton(geoLayerName, q=1, ex=1):
            mc.layerButton(geoLayerName, e=1, lv=0)
        sel = mc.editDisplayLayerMembers(geoLayerName, q=1, fn=1)
        sel = mc.filterExpand(sel, sm=12)
        if sel:
            dupList = list()
            for ele in sel:
                dup = mc.duplicate(ele, rc=1)
                dupList.append(dup[0])
                mc.setAttr(dup[0] + '.inheritsTransform', 1)
            mc.editDisplayLayerMembers('defaultLayer', dupList, nr=1)
            split = curveLayerName.split("_")
            collectionID = int(split[1]) if len(split) == 4 else 0
            collectionName = WIDGETS['layerCollectionsComboBox'].itemText(collectionID)
            extracted = 'extractedGeo_%s_%s' % (collectionName, layerNum)
            if mc.objExists(extracted):
                finalGeo = mc.parent(dupList, extracted)
                return [extracted + "|" + x for x in finalGeo]
            else:
                finalGeo = mc.group(dupList, w=1, n=extracted)
                return [finalGeo + "|" + x for x in dupList]
    return []


def extractSelectedCurves(mod=None, hotkey=False):
    # type: (str, bool) -> None
    """Extract geo from selected curves"""

    sel = mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
    if not sel:
        MESSAGE.warningInView('Select at least one Curve')
        return 0

    if not hotkey:
        mod = utils.getMod()

    isColorEnabled = toggleColor.colorEnabled()
    if isColorEnabled:
        toggleColor.disableColors()

    geometry = []
    for part in sel:
        geo = selectPart(2, True, part)
        if geo:
            geo = geo[0]
        else:
            MESSAGE.warningInView('Curve "%s" failed to extract. Check the outliner for any loose curves.' % part)
            continue
        geometry.append(geo)
    geometry = mc.filterExpand(geometry, sm=12)
    if not geometry:
        return
    allGeo = []
    progress = utils.ProgressBar('Extracting Geometry', len(geometry))
    try:
        for geo in geometry:
            progress.tick(1)
            dup = mc.duplicate(geo, rc=1)
            mc.setAttr(dup[0] + '.inheritsTransform', 1)
            mc.editDisplayLayerMembers('defaultLayer', dup[0], nr=1)
            allGeo += dup
    except Exception as e:
        LOGGER.exception(e)
    finally:
        progress.end()

    parentGrp = mc.group(allGeo, w=1, n='extractedGeo_#')
    allGeo = mc.listRelatives(parentGrp, c=1, pa=1)

    if not mod or "Shift" not in mod:
        if len(allGeo) > 1:
            combinedGeo = mc.polyUnite(allGeo, cp=1)
            mc.delete(combinedGeo, ch=1)
        else:
            combinedGeo = mc.parent(allGeo, w=1)
        mc.delete(parentGrp)
        combinedGeo = mc.filterExpand([x for x in combinedGeo if mc.objExists(x)], sm=12)
        allGeo = mc.rename(combinedGeo[-1], 'extractedGeo_#')

    mc.select(allGeo, r=1)

    # Open export dialog
    if mod and "Ctrl" in mod:
        mel.eval("ExportSelection")
        mc.delete(allGeo)
        try:
            mc.delete(parentGrp)
        except BaseException:
            pass

    if isColorEnabled:
        toggleColor.enableColors()

    updateMainUI()


def extractAllCurves(mod=None, hotkey=False):
    # type: (str|None, bool) -> None
    """
    Extracts geo from all layers
    Modifiers:
    Default -> extract geo and combine
    Shift -> extract geo
    Ctrl -> extract geo, combine and open export menu, delete extracted
    Shift+Ctrl -> extract geo and open export menu, delete extracted
    """
    if not hotkey:
        mod = utils.getMod()

    isColorEnabled = toggleColor.colorEnabled()
    if isColorEnabled:
        toggleColor.disableColors()

    numOfLayers = WIDGETS['curveGrp0'].LAYERS - 1
    if not WIDGETS['ignoreLastLayer'].isChecked():
        numOfLayers = WIDGETS['curveGrp0'].LAYERS

    allCollections = utils.getCollectionsSet()
    allCollections.add('0')
    if getOption('ignoreTemplateCollections'):
        collectionsWidget = WIDGETS['layerCollectionsComboBox']  # type: wrap.LayerCollectionWidget
        for collection in allCollections.copy():
            if "template" in collectionsWidget.itemText(int(collection)).lower():
                allCollections.remove(collection)
    allGeo = []
    shouldHideLayers = (mod and "Ctrl" not in mod) or not mod
    progress = utils.ProgressBar('Extracting Geometry', numOfLayers * len(allCollections))
    try:
        for collection in allCollections:
            formattedCollection = utils.getFormattedCollectionByID(collection)
            for i in range(numOfLayers):
                if progress.tick(1):
                    break
                geo = "curveGrp_%s%s_Geo" % (formattedCollection, i)
                curve = "curveGrp_%s%s_Curve" % (formattedCollection, i)
                if mc.objExists(geo) and mc.objExists(curve):
                    allGeo += extractGeo(geo, curve, i, shouldHideLayers)
    except Exception as e:
        LOGGER.debug(e)
    finally:
        progress.end()

    # Delete parent groups
    parentGrps = set(mc.listRelatives(allGeo, p=1))
    if not mod or "Shift" not in mod:
        if len(allGeo) > 1:
            combinedGeo = mc.polyUnite(allGeo, cp=1)
            mc.delete(combinedGeo, ch=1)
            combinedGeo = mc.filterExpand([x for x in combinedGeo if mc.objExists(x)], sm=12)
        else:
            combinedGeo = mc.parent(allGeo, w=1)
        parentGrps = [x for x in parentGrps if mc.objExists(x)]
        if parentGrps:
            mc.delete(parentGrps)
        allGeo = mc.rename(combinedGeo[-1], 'extractedGeo_#')

    mc.select(allGeo, r=1)

    # Open export dialog
    if mod and "Ctrl" in mod:
        mel.eval("ExportSelection")
        mc.delete(allGeo)
        parentGrps = [x for x in parentGrps if mc.objExists(x)]
        if parentGrps:
            mc.delete(parentGrps)
    if isColorEnabled:
        toggleColor.enableColors()

    updateMainUI()


def toggleLayerVisibility(layerNum):  # Toggle Layer Visibility
    outlinerSync = getOption('syncOutlinerLayerVis')
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    collection = utils.getFormattedCollectionByID(collectionID)
    curve = "curveGrp_%s%s_Curve" % (collection, layerNum)
    geo = "curveGrp_%s%s_Geo" % (collection, layerNum)
    inst = "curveGrp_%s%s_Inst" % (collection, layerNum)
    if (utils.attrExists(curve, 'visibility')):
        groups = []
        if outlinerSync:
            layerCurves = mc.editDisplayLayerMembers(curve, q=1, fn=1)
            if not layerCurves:
                MESSAGE.warningInView('Layer is Empty')
                return
            for i in layerCurves:
                parent = mc.listRelatives(i, p=1, pa=1)
                if parent:
                    groups += parent
        current = mc.getAttr(curve + '.visibility')
        if current == 1:
            mc.setAttr(curve + '.visibility', 0)
            if mc.layerButton(curve, q=1, ex=1):
                mc.layerButton(curve, e=1, lv=0)
            mc.setAttr(geo + '.visibility', 0)
            if mc.layerButton(geo, q=1, ex=1):
                mc.layerButton(geo, e=1, lv=0)
            mc.setAttr(inst + '.visibility', 0)
            if mc.layerButton(inst, q=1, ex=1):
                mc.layerButton(inst, e=1, lv=0)
            for grp in groups:
                mc.setAttr(grp + '.v', 0)
        else:
            mc.setAttr(curve + '.visibility', 1)
            if mc.layerButton(curve, q=1, ex=1):
                mc.layerButton(curve, e=1, lv=1)
            mc.setAttr(geo + '.visibility', 1)
            if mc.layerButton(geo, q=1, ex=1):
                mc.layerButton(geo, e=1, lv=1)
            mc.setAttr(inst + '.visibility', 0)
            if mc.layerButton(inst, q=1, ex=1):
                mc.layerButton(inst, e=1, lv=0)
            for grp in groups:
                mc.setAttr(grp + '.v', 1)
    else:
        MESSAGE.warningInView('Layer is Empty')


def toggleObjVisibility(layerNum, obj):
    # type: (str|int, int) -> None
    """Toggle object type visibility in layer"""
    name = str()
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    collection = utils.getFormattedCollectionByID(collectionID)
    if obj == 0:
        name = "curveGrp_%s%s_Curve" % (collection, layerNum)
    elif obj == 1:
        name = "curveGrp_%s%s_Geo" % (collection, layerNum)
    if utils.attrExists(name, 'visibility'):
        current = mc.getAttr(name + '.visibility')
        if current == 1:
            mc.setAttr(name + '.visibility', 0)
            if mc.layerButton(name, q=1, ex=1):
                mc.layerButton(name, e=1, lv=0)
        else:
            mc.setAttr(name + '.visibility', 1)
            if mc.layerButton(name, q=1, ex=1):
                mc.layerButton(name, e=1, lv=1)
    else:
        MESSAGE.warningInView('Layer is Empty')


def curveLayerSelectObj(layerNum, obj, *_):  # Select Object from Layer
    mod = utils.getMod()
    if obj == -1:
        if mod != 'Shift' and mod != 'Ctrl':
            return 0
        else:
            obj = 0
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    collection = utils.getFormattedCollectionByID(collectionID)
    geo = 'curveGrp_%s%s_Geo' % (collection, layerNum)
    curve = 'curveGrp_%s%s_Curve' % (collection, layerNum)
    if mc.objExists(geo):
        sel = mc.ls(sl=1)
        if (obj == 1):
            mc.select(mc.editDisplayLayerMembers(geo, q=1, fn=1))
        if (obj == 0):
            selection = []
            unfilteredCurves = mc.editDisplayLayerMembers(curve, q=1, fn=1)
            if not unfilteredCurves:
                MESSAGE.warningInView('Layer is Empty')
                return
            for ele in unfilteredCurves:
                if mc.attributeQuery('gsmessage', n=ele, ex=1) and mc.connectionInfo(ele + '.gsmessage', id=1):
                    continue
                selection.append(ele)
            mc.select(selection)
        if (not WIDGETS['replacingCurveLayerSelection'].isChecked() or (mod == 'Shift')):
            mc.select(sel, add=1)
    else:
        MESSAGE.warningInView('Layer is Empty')


def curveGeometryEditToggle(layerNum):
    # type: (str|int) -> None
    """Toggle Geo Editing on Layer"""
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    collection = utils.getFormattedCollectionByID(collectionID)
    geo = 'curveGrp_%s%s_Geo' % (collection, layerNum)
    if (utils.attrExists(geo, 'displayType')):
        currentValue = mc.getAttr(geo + '.displayType')
        if currentValue == 2:
            mc.setAttr(geo + '.displayType', 0)
            curveLayerSelectObj(layerNum, 1)
        else:
            mc.setAttr(geo + '.displayType', 2)
    else:
        MESSAGE.warningInView('Layer is Empty')


def curveAddToLayer(targetLayer, sourceLayer=None, inputCurves=None, targetCollection=None):
    # type: (str|int, str|int, list[str], int) -> None
    """Add Selected Curves to Layer"""
    create.initialize()
    collectionID = WIDGETS['layerCollectionsComboBox'].currentIndex()
    if targetCollection is not None:
        collectionID = int(targetCollection)
    curve, geo, inst = utils.getFormattedLayerNames(collectionID, targetLayer)
    sel = mc.ls(sl=1, tr=1)
    if inputCurves:
        sel = inputCurves
    if sourceLayer:
        collection = utils.getFormattedCollectionByID(collectionID)
        sourceLayer = "curveGrp_%s%s_Curve" % (collection, sourceLayer)
        if mc.objExists(sourceLayer):
            sel = mc.editDisplayLayerMembers(sourceLayer, q=1, fn=1)
        else:
            return 0
    origSel = sel
    if sel:
        for ele in sel:
            if ('pathCurve' in ele) or ('geoCard' in ele) or ('geoTube' in ele):
                eleGrp = mc.listRelatives(ele, p=1, pa=1)
                if not eleGrp:
                    MESSAGE.warningInView('Wrong Selection: %s is skipped' % ele)
                    continue
                components = separateComponents(eleGrp[0])
                if not components:
                    continue
                if not mc.objExists(curve):
                    mc.select(cl=1)
                    utils.createNewDisplayLayer(curve)
                if not mc.objExists(geo):
                    utils.createNewDisplayLayer(geo)
                    mc.setAttr(geo + '.enabled', 1)
                    mc.setAttr(geo + '.displayType', 2)
                if not mc.objExists(inst):
                    utils.createNewDisplayLayer(inst)
                    mc.setAttr(inst + '.enabled', 1)
                    mc.setAttr(inst + '.visibility', 0)
                    mc.setAttr(inst + '.displayType', 2)
                mc.editDisplayLayerMembers(curve, components[0], nr=1)
                mc.editDisplayLayerMembers(inst, components[1], nr=1)
                mc.editDisplayLayerMembers(geo, components[2], nr=1)
                if WIDGETS['boundCurvesFollowParent'].isChecked():
                    ele = getAllConnectedCurves(ele)
                    for i in ele:
                        if mc.attributeQuery('gsmessage', n=i, ex=1):
                            if mc.connectionInfo(i + '.gsmessage', isSource=1):
                                childCards = mc.listConnections(i + '.gsmessage', d=1, s=0, t='transform')
                                if childCards:
                                    for card in childCards:
                                        components = separateComponents(selectPart(0, True, card))
                                        mc.editDisplayLayerMembers(curve, components[0], nr=1)
                                        mc.editDisplayLayerMembers(inst, components[1], nr=1)
                                        mc.editDisplayLayerMembers(geo, components[2], nr=1)
            else:
                MESSAGE.warningInView('Wrong Selection: %s is skipped' % ele)
        deleteUnusedLayers()
        layerCollections.updateDefaultLayerNode()
        layerCollections.updateCollectionNames()
        if WIDGETS['syncCurveColor'].isChecked():
            toggleColor.syncCurveColors()
        if WIDGETS['colorMode'].isChecked():
            toggleColor.onLayerChange(sel, geo)
        mc.select(origSel, r=1)
    else:
        MESSAGE.warningInView('Nothing is Selected')


def separateComponents(inputGroup):
    tr = mc.listRelatives(inputGroup, pa=1)
    components = [None, None, None]
    for comp in tr:
        if 'pathCurve' in comp:
            components[0] = comp
        elif 'instances' in comp:
            components[1] = comp
        elif ('geoCard' in comp) or ('geoTube' in comp):
            components[2] = comp
    if len(components) != 3:
        return
    else:
        return components


def getAllConnectedCurves(inputCurves):
    returnCurves = []
    if isinstance(inputCurves, list):
        currentCurves = inputCurves
    else:
        currentCurves = [inputCurves]

    returnCurves = currentCurves

    iterationCurves = currentCurves
    safety = 0
    while iterationCurves:
        safety = safety + 1
        if safety > 50:
            break
        boundCurves = []
        for curve in iterationCurves:
            condition = (mc.attributeQuery('gsmessage', n=curve, ex=1) and
                         mc.connectionInfo(curve + '.gsmessage', isSource=1))
            if condition:
                newCurves = mc.listConnections(curve + '.gsmessage', d=1, s=0, t='transform')
                if newCurves:
                    boundCurves += newCurves
            else:
                continue
        if boundCurves:
            iterationCurves = False
            iterationCurves = boundCurves
            returnCurves += iterationCurves
        else:
            iterationCurves = False
            break

    return returnCurves


def getCurveLayer(curve):
    if not curve:
        return
    layer = mc.listConnections(curve, type='displayLayer')
    layerID = re.findall(r'\d+', layer[0])[0]
    return layerID


def filterBoundCurves(curves):
    if isinstance(curves, list):
        curves = curves
    else:
        curves = [curves]

    filteredCurves = []

    for curve in curves:
        if (mc.attributeQuery('gsmessage', n=curve, ex=1) and
                mc.connectionInfo(curve + '.gsmessage', id=1)):
            continue
        filteredCurves.append(curve)

    return filteredCurves


def duplicateCurve(customSel=None):
    # type: (list[str]|None) -> None
    """Duplicate selected Curves or curves list passed as an argument"""
    create.initialize()
    sel = mc.ls(sl=1, fl=1)
    if customSel:
        sel = customSel
    if not sel:
        MESSAGE.warningInView('Select at least one curve')
        return
    fe = mc.filterExpand(sel, sm=(30, 28))
    if fe:
        obj = mc.ls(sel, o=1)
        sel = []
        for ele in obj:
            rel = mc.listRelatives(ele, p=1, pa=1)
            sel.append(rel[0])
    sel = list(set(sel))
    finalSel = list()
    copyThickness = list()
    mc.select(cl=1)
    if not customSel:
        progressBar = utils.ProgressBar('Duplicating Curves', len(sel))
    try:
        sel = filterBoundCurves(sel)
        try:
            utils.deleteKeys(sel)
        except BaseException:
            pass
        sel = list(set(selectPart(0, True, sel)))  # Filter out duplicates
        for ele in sel:
            if not customSel:
                progressBar.tick(1)
            if ('pathCurve_inst' in ele) or ('profileCurve_inst' in ele):
                ele = mc.listRelatives(ele, p=1, pa=1)[0]
            if any([x in ele for x in ['geoCard', 'pathCurve', 'geoTube', 'instances', 'origCurves']]):
                parent = mc.listRelatives(ele, p=1, pa=1)
                origCrv = None
                for curve in mc.listRelatives(parent, c=1, pa=1):
                    if 'pathCurve' in curve:
                        origCrv = curve
                        break
                dup = mc.duplicate(parent, rr=1, rc=1, un=1)
                dupCrv = None
                for curve in mc.listRelatives(dup, c=1, pa=1):
                    if 'pathCurve' in curve:
                        dupCrv = curve
                        break
                if origCrv and dupCrv:
                    copyThickness.append((origCrv, dupCrv))
                elif dupCrv:
                    copyThickness.append(dupCrv)
                finalSel.append(dupCrv)
            else:
                rel = mc.listRelatives(ele, c=1, pa=1)
                if not rel:
                    continue
                dup = mc.duplicate(ele, rr=1, rc=1, un=1)
                for curve in mc.listRelatives(dup, c=1, pa=1):
                    if 'pathCurve' in curve:
                        copyThickness.append(curve)
                        finalSel.append(curve)
                        break
    except BaseException:
        pass
    finally:
        if not customSel:
            progressBar.end()
    if copyThickness:
        setCurveThickness(copyThickness)
    mc.select(finalSel, r=1)
    return (finalSel)


def deleteSelectedCurves():
    """Deletes selected curves in a safe way. Also deletes other objects"""
    sel = mc.ls(sl=1, tr=1)
    sel = selectPart(0, True, sel)
    if not sel:
        return
    mc.delete(sel)
    print(" ")  # Just to avoid annoying errors during bind curve deletion


def smoothCurve(inputCurves=None):
    """Smoothes selected curve"""
    sel = mc.ls(sl=1)
    if not sel:
        MESSAGE.warningInView('Select at least one curve')
        return 0
    if inputCurves:
        sel = inputCurves
    selCrv = mc.filterExpand(sel, sm=9)
    selCV = mc.filterExpand(sel, sm=28)
    if not selCrv and not selCV:
        MESSAGE.warningInView('Select at least 1 curve to smooth')
        return 0
    if selCV and len(selCV) < 3:
        MESSAGE.warningInView('Select at least 3 CVs to smooth')
        return 0
    mult = 1
    if mc.menuItem('gsSmoothMult3', q=1, rb=1):
        mult = 3
    if mc.menuItem('gsSmoothMult5', q=1, rb=1):
        mult = 5
    if mc.menuItem('gsSmoothMult10', q=1, rb=1):
        mult = 10
    if inputCurves:
        mult = 10
    smoothing = math.ceil((100 - mc.floatSliderGrp('gsFactorSlider', q=1, v=1)) / 20)
    if selCrv:  # If curve is selected
        sel = mc.ls(selCrv, dag=1, s=1)
        for obj in sel:
            CVcount = mc.getAttr(obj + '.cp', s=1)
            if CVcount >= 3:
                for _ in range(0, mult):
                    cPoint = mc.getAttr(obj + '.cp[:]')
                    finalPoints = list()
                    finalPoints.append(tuple(cPoint[0]))
                    firstP = om.MFloatVector(cPoint[0][0], cPoint[0][1], cPoint[0][2])
                    activeP = om.MFloatVector(cPoint[1][0], cPoint[1][1], cPoint[1][2])
                    for i in range(2, CVcount):
                        nextP = om.MFloatVector(cPoint[i][0], cPoint[i][1], cPoint[i][2])
                        activePpos = (activeP + firstP + nextP) / 3
                        for _ in range(1, int(smoothing)):
                            activePpos = (activeP + activePpos) / 2
                        finalPoints.append(tuple([activePpos.x, activePpos.y, activePpos.z]))
                        firstP = activeP
                        activeP = nextP
                    finalPoints.append(tuple(cPoint[-1]))
                    cmd = ('mc.setAttr("' + str(obj) + '.cp[:]"')
                    for i in range(len(finalPoints)):
                        for z in range(3):
                            cmd += (',' + str(finalPoints[i][z]))
                    cmd += ')'
                    eval(cmd)
    else:  # If CVs are selected
        curveDict = dict()
        for cv in selCV:
            obj = mc.ls(cv, o=1)[0]
            CVnum = re.findall(r'\d+', re.findall(r'\[\d+\]', cv)[0])[0]
            if obj in curveDict:
                curveDict[obj].append(int(CVnum))
            else:
                curveDict[obj] = [int(CVnum)]
        for obj in curveDict:
            CVs = curveDict[obj]
            if len(CVs) < 3:
                continue
            CVs.sort()
            CVsFinal = [CVs[0]]
            for i in range(len(CVs) - 1):
                if (int(CVs[i + 1]) - int(CVs[i])) >= 2:
                    break
                CVsFinal.append(CVs[i + 1])
            CVcount = len(CVs)
            if CVcount >= 3:
                for _ in range(0, mult):
                    cPoint = list()
                    for cv in CVsFinal:
                        cPoint.append(mc.getAttr(obj + '.cp[%s]' % cv)[0])
                    finalPoints = list()
                    finalPoints.append(tuple(cPoint[0]))
                    firstP = om.MFloatVector(cPoint[0][0], cPoint[0][1], cPoint[0][2])
                    activeP = om.MFloatVector(cPoint[1][0], cPoint[1][1], cPoint[1][2])
                    for i in range(2, CVcount):
                        nextP = om.MFloatVector(cPoint[i][0], cPoint[i][1], cPoint[i][2])
                        activePpos = (activeP + firstP + nextP) / 3
                        for _ in range(1, int(smoothing)):
                            activePpos = (activeP + activePpos) / 2
                        finalPoints.append(tuple([activePpos.x, activePpos.y, activePpos.z]))
                        firstP = activeP
                        activeP = nextP
                    finalPoints.append(tuple(cPoint[-1]))
                    cmd = ('mc.setAttr("' + str(obj) + '.cp[%s:%s]"' % (CVsFinal[0], CVsFinal[-1]))
                    for i in range(len(finalPoints)):
                        for z in range(3):
                            cmd += (',' + str(finalPoints[i][z]))
                    cmd += ')'
                    eval(cmd)


def extendCurve():  # Extends curve length
    sel = mc.filterExpand(mc.ls(sl=1, fl=1, o=1), sm=9)
    if not sel:
        MESSAGE.warningInView('Select at least one curve')
        return 0
    factor = mc.floatSliderGrp('gsFactorSlider', q=1, v=1)
    if factor < 10:
        factor = 10
    for obj in sel:
        distance = (mc.arclen(obj) * (float(factor) ** .5) / 100) / 10
        getCV = mc.getAttr(obj + '.spans')
        deg = mc.getAttr(obj + '.degree')
        if ((float(factor) ** .5) / 100 > .25):
            getCV += math.ceil(float(factor) / 10)
        mc.extendCurve(obj, et=2, d=(distance * factor), cos=0, em=0, s=0, jn=1, rmk=1, rpo=1)
        mc.rebuildCurve(obj, d=deg, kt=1, rt=0, s=getCV)
    mc.select(sel, r=1)


def reduceCurve():  # Reduces curve length
    sel = mc.ls(sl=1, fl=1, o=1)
    if not sel:
        MESSAGE.warningInView('Select at least one curve')
        return 0
    factor = (mc.floatSliderGrp('gsFactorSlider', q=1, v=1) / 100) ** 1.5
    for obj in sel:
        degree = mc.getAttr(obj + '.degree')
        spans = mc.getAttr(obj + '.spans')
        minimum = mc.getAttr(obj + '.min')
        maximum = mc.getAttr(obj + '.max')
        posRange = maximum - (maximum - minimum) * factor
        invRange = minimum + (maximum - minimum) * factor
        iteration = int(math.floor(invRange))
        if invRange < .05:
            posRange = maximum - (maximum - minimum) * 0.05
        mc.insertKnotCurve(obj + '.u[' + str(posRange) + ']', cos=1, nk=1, ib=0, rpo=1)
        for _ in range(iteration + 1):
            mc.delete(obj + '.ep[' + str(mc.getAttr(obj + '.spans')) + ']')
        try:
            mc.rebuildCurve(obj, s=spans, d=degree, tol=0.0001, rpo=1, rt=0, end=1, kr=1, kcp=0, kep=1, kt=0)
        except BaseException:
            pass
    mc.select(sel, r=1)


def selectPart(selType, justReturn=False, inputObj=None):  # Selects Curve, Geometry or Group
    # type: (int, bool, list|str) -> (None|list)
    """ selType: 0 - Group, 1 - Curve, 2 - Geo , 3 - Bound Curves"""
    sel = mc.ls(sl=1, o=1, fl=1)
    if not sel:
        sel = mc.ls(hl=1, o=1, fl=1)
    if inputObj:
        if isinstance(inputObj, list):
            sel = inputObj
        else:
            sel = [inputObj]
    finSel = list()
    for part in sel:
        if mc.nodeType(part) != 'transform':
            try:
                part = mc.listRelatives(part, p=1, pa=1)[0]
            except BaseException:
                return
        ch = list()
        grp = str()
        if ('pathCurve' in part) or ('instance' in part) or ('geoCard' in part) or ('geoTube' in part):
            grp = mc.listRelatives(part, p=1, pa=1)
            if grp:
                grp = grp[0]
            else:
                return 0
            ch = mc.listRelatives(grp, c=1, pa=1)
        else:
            grp = part
            ch = mc.listRelatives(part, c=1, pa=1)
        if selType == 0:
            finSel.append(grp)
        else:
            if not ch:
                return
            for ele in ch:
                if selType == 1:
                    if 'pathCurve' in ele:
                        finSel.append(ele)
                        break
                elif selType == 2:
                    if ('geoCard' in ele) or ('geoTube' in ele):
                        finSel.append(ele)
                        break
                elif selType == 3:
                    if ('origCurves' in ele):
                        finSel.append(ele)
                        break
    if justReturn:
        return finSel
    mc.select(finSel, r=1)


def groupCurves():  # Groups selected Curves in the Outliner
    selectPart(0)
    name = WIDGETS['gsGroupNameTextField'].text()
    if not name:
        name = 'crvGrp#'
    sel = mc.ls(sl=1, fl=1)
    if len(sel) > 0:
        upGrp = mc.listRelatives(sel[0], p=1, pa=1)
        grp = str()
        if upGrp is None:
            grp = mc.group(sel, n=name)
        else:
            grp = mc.group(sel, n=name, p=upGrp[0])
        mc.connectAttr(grp + '.sx', grp + '.sy', f=1)
        mc.connectAttr(grp + '.sx', grp + '.sz', f=1)
    else:
        MESSAGE.warningInView('Select at least one Curve')


def controlCurveCreate():
    """Creates Control Curve from selected Curves"""
    sel = mc.ls(sl=1, tr=1, fl=1)
    if not sel:
        sel = mc.listRelatives(mc.ls(sl=1, o=1), p=1, pa=1)
    sel = mc.filterExpand(sel, sm=9)
    if not sel:
        MESSAGE.warningInView('No nurbs curves selected')
        return

    # Finding closest points to ref CV
    refCurve = sel[0]
    refCV = "{}.ep[{}]".format(refCurve, 0)
    closestEPs = []
    for curve in sel:
        om_selList = om.MSelectionList()
        om_selList.add(curve)
        om_curve = om.MFnNurbsCurve(om_selList.getDagPath(0))
        om_closestPoint = om_curve.closestPoint(om.MPoint(mc.pointPosition(refCV)), space=om.MSpace.kWorld)
        spans = mc.getAttr(curve + '.spans')
        minmax = mc.getAttr(curve + '.minMaxValue')[0]
        uMid = minmax[1] / 2.0
        finalEP = spans if om_closestPoint[1] > uMid else 0
        closestEPs.append((curve, finalEP))

    # Finding average points between the curves
    spans = mc.getAttr(sel[0] + '.spans')
    step = 1.0 / float(spans + 4)
    pp = []
    u = 0.0
    for _ in range(spans + 5):
        point = om.MFloatVector()
        for curve, ep in closestEPs:
            minmax = mc.getAttr(curve + '.minMaxValue')[0]
            if ep == 0:
                uNorm = minmax[0] + (minmax[1] - minmax[0]) * u
            else:
                uNorm = minmax[1] - (minmax[1] - minmax[0]) * u
            pp0 = mc.pointPosition(curve + '.u[%s]' % uNorm)
            point += om.MFloatVector(pp0[0], pp0[1], pp0[2])
        u += step
        pp.append(point / len(closestEPs))

    # Constructing the curve
    controlCurve = mc.curve(ep=pp, d=3)
    controlCurve = mc.rebuildCurve(controlCurve, kr=2, rt=0, s=spans)[0]
    controlCurve = mc.rename(controlCurve, 'controlCurve#')
    mc.addAttr(controlCurve, ln='isControlCurve', dt='string')

    # Selection list for Warp deformer
    selList = []
    for curve in sel:
        selList.append(curve)
    selList.append(controlCurve)
    mc.select(selList, r=1)

    # Creating Warp deformer
    mel.eval('CreateWrap;')
    mc.setAttr(controlCurve + 'Base.hiddenInOutliner', 1)
    mc.setAttr(controlCurve + '.wrapSamples', 100)
    mc.setAttr(controlCurve + '.dropoff', 20)
    mc.setAttr(mc.ls(controlCurve, dag=1, s=1)[0] + '.lineWidth', 3)
    mc.setAttr(controlCurve + '.overrideEnabled', 1)
    mc.setAttr(controlCurve + '.overrideRGBColors', 1)
    mc.setAttr(controlCurve + '.overrideColorRGB', 0, 1, 0)
    mc.select(controlCurve, r=1)
    resetCurvePivotPoint()
    LOGGER.info('Control Curve Created')
    # mc.evalDeferred(lambda: print(), lp=1)


def controlCurveApply():  # Deletes selected Control Curve and clears History
    sel = mc.ls(sl=1, fl=1, o=1, dag=1, s=1)
    if not len(sel):
        MESSAGE.warningInView('Select Control Curve to Apply')
        return 0
    wraps = mc.listConnections(sel[0], t='wrap', et=1, d=1, s=0)
    if not wraps:
        MESSAGE.warningInView('Select Control Curve to Apply')
        return 0
    back = mc.listConnections(wraps[0], s=1, d=1, et=1, t='nurbsCurve')
    forth = mc.listConnections(back, s=0, d=1, et=1, t='wrap')
    cleanWraps = list(dict.fromkeys(forth))
    curves = mc.listConnections(cleanWraps, s=1, d=0, et=1, t='nurbsCurve')
    cleanCurves = list(dict.fromkeys(curves))
    other = []
    control = []
    for curve in cleanCurves:
        if utils.attrExists(curve, 'isControlCurve'):
            if utils.attrExists(curve, 'wrapSamples') and mc.listConnections(curve + '.wrapSamples'):
                control.append(curve)
            else:
                other.append(curve)
        else:
            other.append(curve)
    mc.delete(other, ch=1)
    mc.delete(control)
    mc.select(other, r=1)


def edgeToCurve(enableProgressBar=True):  # Converts selected edge groups to curves
    sel = mc.ls(sl=1, fl=1)
    sel = mc.filterExpand(sel, sm=32)
    if not sel:
        MESSAGE.warningInView('Select Edges to Convert')
        return 0
    result = str()

    if len(sel) > 1000:
        message = 'Warning!\n\nMore than 1000 edges selected.\nComputation can take a long time ( > 10 seconds)\nContinue?\n\nNote: Selecting smaller edge groups is much faster\n'
        result = mc.confirmDialog(ma='Center', icn='question', t='More than 1000 edges selected', m=message,
                                  button=['OK', 'Cancel'], cancelButton='Cancel', ds='Cancel')
    else:
        result = 'OK'
    if result != 'OK':
        return 0

    # Progress bar init
    if enableProgressBar:
        progressBar = utils.ProgressBar('Converting Edges', len(sel))

    # Sort Edges to Edge Groups
    obj = mc.ls(sl=1, o=1)
    edges = dict()
    for i in range(len(sel)):
        polyInfo = mc.polyInfo(sel[i], ev=1)[0].format()
        polyInfo = polyInfo.split()
        edges[i] = (int(polyInfo[1][0:-1]), int(polyInfo[2]), int(polyInfo[3]))

    finalCollection = list()
    while (len(edges) > 0):
        edgeCollection = list()
        edge = edges.popitem()[1]
        origComp = edge[0]
        # fe0 = edge[1]
        # fe1 = fe0
        fv0 = (edge[1], edge[2])
        fv1 = fv0
        iteration = len(edges)
        for i in range(iteration):
            for key in edges:
                nv = (edges[key][1], edges[key][2])
                if fv0[0] == nv[0] or fv0[0] == nv[1] or fv0[1] == nv[0] or fv0[1] == nv[1]:
                    edgeCollection.append(edges[key][0])
                    # fe0 = edges[key][0]
                    fv0 = (nv[0], nv[1])
                    edges.pop(key)
                    break
                if fv1[0] == nv[0] or fv1[0] == nv[1] or fv1[1] == nv[0] or fv1[1] == nv[1]:
                    edgeCollection.append(edges[key][0])
                    # fe1 = edges[key][0]
                    fv1 = (nv[0], nv[1])
                    edges.pop(key)
                    break
        edgeCollection.append(origComp)
        finalCollection.append(edgeCollection)

        if enableProgressBar and progressBar.tick(len(edgeCollection)):
            return

    if enableProgressBar:
        progressBar.end()

    mode = 3
    if utils.getMod() == "Shift":
        mode = 1

    grp = list()
    mc.select(cl=1)

    # Create cures from edge groups
    for group in finalCollection:
        edgeSelection = list()
        for edge in group:
            edgeSelection.append(obj[0] + '.e[' + str(edge) + ']')
        mc.select(edgeSelection, r=1)
        tmp = mel.eval('string $gsTempPolyToCurve[] = `polyToCurve -form 2 -degree ' + str(
            mode) + ' -conformToSmoothMeshPreview 1`')
        grp.append(tmp[0])
    mc.select(grp, r=1)


def orientToFaceNormals():
    mesh = WIDGETS['gsOrientMeshName'].text()
    if not mesh:
        MESSAGE.warningInView('Add the geo to the Target Field')
        return
    if not mc.objExists(mesh):
        MESSAGE.warningInView('Target Mesh Not Found')
        return
    sel = mc.filterExpand(mc.ls(sl=1, fl=1, o=1), sm=9)
    if not sel:
        MESSAGE.warningInView('Select at least one curve')
        return
    N = WIDGETS['gsIterationsSlider'].getValue()  # Number of iterations per curve
    angleTolerance = WIDGETS['gsMinimumAngle'].getValue()
    isRefresh = WIDGETS['orientRefreshViewport'].isChecked()
    progress = None
    if len(sel) > 10:
        progress = utils.ProgressBar('Orienting Selection', len(sel))
    try:
        for curve in sel:
            if progress and progress.tick(1):
                return
            lDiv = mc.getAttr(curve + '.lengthDivisions') if mc.attributeQuery('lengthDivisions', n=curve, ex=1) else None
            wDiv = mc.getAttr(curve + '.widthDivisions') if mc.attributeQuery('widthDivisions', n=curve, ex=1) else None
            twist = mc.getAttr(curve + '.Twist') if mc.attributeQuery('Twist', n=curve, ex=1) else None
            # invTwist = mc.getAttr(curve + '.invTwist') if mc.attributeQuery('invTwist', n=curve, ex=1) else None
            if lDiv and lDiv > 10:
                mc.setAttr(curve + '.lengthDivisions', 10)
            if wDiv and wDiv > 2:
                try:
                    mc.setAttr(curve + '.widthDivisions', 2)
                except BaseException:
                    pass
            if twist and twist != 0:
                mc.setAttr(curve + '.Twist', 0)
            # if invTwist and invTwist != 0:
            #     mc.setAttr(curve + '.invTwist', 0)

            firstCv = '%s.cv[0]' % curve
            pos = mc.pointPosition(firstCv)
            om_pos = om.MPoint(pos)

            targetClosestPointNormal = utils.getClosestPointAndNormal(mesh, pos)[1]
            om_sel = om.MSelectionList()
            geo = selectPart(2, True, curve)[0]
            om_sel.add(geo)
            om_mesh = om.MFnMesh(om_sel.getDagPath(0))

            orientation = curve + '.Orientation'
            prevDiff = 360
            currentDiff = 360
            i = 0

            guesses = []
            while (currentDiff >= angleTolerance) and (i <= N):
                i += 1
                currentOrien = mc.getAttr(orientation)

                om_cardFaceNormal = om_mesh.getClosestPointAndNormal(om_pos, space=om.MSpace.kWorld)[1]
                currentDiff = om_cardFaceNormal.angle(targetClosestPointNormal) * 180 / math.pi % 360

                guesses.append((currentDiff, currentOrien))

                if currentDiff > prevDiff:
                    guess = currentOrien - currentDiff
                else:
                    guess = currentOrien + currentDiff

                prevDiff = currentDiff
                nextOrien = guess

                mc.setAttr(orientation, nextOrien % 360)

            # Setting the best guess as the final orientation
            finalOrientation = min(guesses, key=lambda t: t[0])[1]
            mc.setAttr(orientation, finalOrientation)

            if lDiv and lDiv > 10:
                mc.setAttr(curve + '.lengthDivisions', lDiv)
            if wDiv and wDiv > 2:
                mc.setAttr(curve + '.widthDivisions', wDiv)
            if twist and twist != 0:
                mc.setAttr(curve + '.Twist', twist)
            # if invTwist and invTwist != 0:
            #     mc.setAttr(curve + '.invTwist', invTwist)
            if isRefresh:
                mc.refresh()

    except Exception as e:
        LOGGER.exception(e)
    finally:
        if progress:
            progress.end()
    curveControlUI.updateUI()


# TODO: Finish this alignment function for 1.3+

def alignTwistToMesh(targetMesh, curve, geo):  # type: (str, str, str) -> None
    """Attempts to align the twist graph to the normals of the target mesh on each step point"""
    if not mc.attributeQuery('Offset', n=curve, ex=1):
        return

    steps = 6 - 1  # How many points to probe along the curve minus the first point
    targetMeshSel = om.MSelectionList()
    targetMeshSel.add(targetMesh)
    fnTargetMesh = om.MFnMesh(targetMeshSel.getDagPath(0))

    geoSel = om.MSelectionList()
    geoSel.add(geo)
    fnGeo = om.MFnMesh(geoSel.getDagPath(0))
    curveSel = om.MSelectionList()
    curveSel.add(curve)
    fnCurve = om.MFnNurbsCurve(curveSel.getDagPath(0))
    k_min, k_max = fnCurve.knotDomain
    try:
        warpNode = mc.ls(mc.listHistory(selectPart(2, True, curve), ac=1, il=0), typ='curveWarp')[0]
    except BaseException:
        return
    sel = mc.ls(sl=1)
    attributes.resetMultiInst(warpNode, 'twistCurve')
    finalList = []
    for i in range(steps + 1):
        if i == 0:
            param = 0.0
            diff = 0.0
            toSet = 0.5
        else:
            param = i * (k_max - k_min) / steps
            pointAtParam = fnCurve.getPointAtParam(param, space=om.MSpace.kWorld)
            geo_p, geo_n, _ = fnGeo.getClosestPointAndNormal(pointAtParam, space=om.MSpace.kWorld)
            target_p, target_n, _ = fnTargetMesh.getClosestPointAndNormal(geo_p, space=om.MSpace.kWorld)
            mc.curve(ws=1, p=[list(geo_p)[:3], list(target_p)[:3]], d=1, n='GS_DEBUG:debugCurve#')
            diff = geo_n.angle(target_n)
            toSet = mt.lerp(diff, 0.5, 1.0, 0, math.pi)
        finalList.append((i / steps, toSet))
    mc.select(sel, r=1)
    finalList.append('twistCurve')
    attributes.setMultiInst(curve, finalList)


def changeLayersToNumbers():
    if WIDGETS['layerNumbersOnly'].isChecked():
        for i in range(10, 20):
            WIDGETS['curveGrp%s' % i].changeLabel(str(i))
    else:
        letter = ord('A')
        letters = [chr(i) for i in range(letter, letter + 10)]
        for i in range(10, 20):
            WIDGETS['curveGrp%s' % i].changeLabel(letters[i - 10])


def setAOSettings(silent=False):
    mc.setAttr('hardwareRenderingGlobals.ssaoAmount', 0)
    mc.setAttr('hardwareRenderingGlobals.ssaoRadius', 1)
    mc.setAttr('hardwareRenderingGlobals.ssaoFilterRadius', 1)
    mc.setAttr('hardwareRenderingGlobals.ssaoSamples', 8)
    if silent:
        return
    MESSAGE.printInView('AO Settings Applied')
    LOGGER.info('AO Amount set to: %s' % 0)
    LOGGER.info('AO Radius set to: %s' % 0)
    LOGGER.info('AO Filter Radius set to: %s' % 1)
    LOGGER.info('AO Samples set to: %s' % 8)


def setTransparencySettings(type=1):
    """
    Type of transparency setup:
    0 - Simple (fast, but less detailed)
    1 - Object Sorting (average performance, better accuracy)
    2 - Depth Peeling (slow, but more accurate)
    """
    if type == 0:
        MESSAGE.printInView('Simple Transparency Settings Applied')
        mc.setAttr('hardwareRenderingGlobals.transparencyAlgorithm', 0)
    elif type == 1:
        MESSAGE.printInView('Object Sorting Transparency Settings Applied')
        mc.setAttr('hardwareRenderingGlobals.transparencyAlgorithm', 1)
    elif type == 2:
        MESSAGE.printInView('Depth Peeling Transparency Settings Applied')
        mc.setAttr('hardwareRenderingGlobals.transparencyAlgorithm', 3)
    mc.setAttr('hardwareRenderingGlobals.transparencyQuality', 1)
    mc.setAttr('hardwareRenderingGlobals.transparentShadow', 1)
    LOGGER.info('Transparency Quality set to: %s' % 1)
    LOGGER.info('Transparent Shadow set to: %s' % 1)


def alwaysOnTopToggle(*_):
    if MAYA_VER >= 2022:
        allCurves = []
        for i in range(80):
            if mc.objExists('curveGrp_%s_Curve' % i):
                curves = mc.editDisplayLayerMembers('curveGrp_%s_Curve' % i, q=1, fn=1)
                if curves:
                    allCurves += curves
        if allCurves:
            firstCurveAttr = 0
            if mc.attributeQuery('alwaysDrawOnTop', n=mc.listRelatives(allCurves[0], c=1, typ='nurbsCurve')[0], ex=1):
                firstCurveAttr = mc.getAttr(allCurves[0] + '.alwaysDrawOnTop')
            for obj in allCurves:
                shape = mc.listRelatives(obj, c=1, typ='nurbsCurve', pa=1)[0]
                if mc.attributeQuery('alwaysDrawOnTop', n=shape, ex=1):
                    mc.setAttr(shape + '.alwaysDrawOnTop', not firstCurveAttr)
    else:
        setAOSettings(silent=True)
        utils.AOToggle()


def collectionVisibilityToggle(cb):
    mc.optionVar(iv=['GSCT_AutoHideCurvesOnInactiveCollections', cb])
    updateVisibilityBasedOnActiveCollection(True)


def updateVisibilityBasedOnActiveCollection(force=None):
    cb = mc.optionVar(q='GSCT_AutoHideCurvesOnInactiveCollections')
    if not cb and not force:
        return
    currentCollection = WIDGETS['layerCollectionsComboBox'].currentIndex()
    allLayers = [x for x in mc.ls(typ='displayLayer') if ('curveGrp_' in x and '_Curve' in x)]
    mainLayers = []
    nonMainLayers = []
    for layer in allLayers:
        split = layer.split("_")
        if len(split) == 3:
            mainLayers.append(layer)
        elif len(split) == 4:
            nonMainLayers.append(layer)
    if cb:
        if currentCollection == 0:
            for layer in mainLayers:
                mc.setAttr(layer + '.visibility', 1)
            for layer in nonMainLayers:
                mc.setAttr(layer + '.visibility', 0)
        else:
            for layer in mainLayers:
                mc.setAttr(layer + '.visibility', 0)
            for layer in nonMainLayers:
                if int(layer.split("_")[1]) != currentCollection:
                    mc.setAttr(layer + '.visibility', 0)
                else:
                    mc.setAttr(layer + '.visibility', 1)


def alwaysOnTopToggleLayer(layer, *_):
    if MAYA_VER >= 2022:
        allCurves = []
        if mc.objExists('curveGrp_%s_Curve' % layer):
            allCurves = mc.editDisplayLayerMembers('curveGrp_%s_Curve' % layer, q=1, fn=1)
        if allCurves:
            firstCurveAttr = 0
            if mc.attributeQuery('alwaysDrawOnTop', n=mc.listRelatives(allCurves[0], c=1, typ='nurbsCurve')[0], ex=1):
                firstCurveAttr = mc.getAttr(allCurves[0] + '.alwaysDrawOnTop')
            for obj in allCurves:
                shape = mc.listRelatives(obj, c=1, typ='nurbsCurve', pa=1)[0]
                if mc.attributeQuery('alwaysDrawOnTop', n=shape, ex=1):
                    mc.setAttr(shape + '.alwaysDrawOnTop', not firstCurveAttr)
        else:
            MESSAGE.warning("Layer is Empty")
    else:
        setAOSettings(silent=True)
        utils.AOToggle()


def convertSelectionTo(targetType):
    # type: (int) -> None
    """
    Converts selected curves to selected targetType
    0 - Warp Card, 1 - Warp Tube, 2 - Extrude Card, 3 - Extrude Tube
    """
    sel = mc.filterExpand(mc.ls(sl=1, fl=1, tr=1), sm=9)
    if not sel:
        MESSAGE.warning('No curves selected.')
        return

    # Init
    dialog = 'Skip'
    compatibleCurves = []
    allCurves = []
    finalCurves = []

    # Check if bound
    sel = [obj for obj in sel if not mc.attributeQuery('Axis', n=obj, ex=1)]
    if not sel:
        MESSAGE.warning('No compatible curves selected.')
        return

    # Check for scale factor
    for obj in sel:
        if not mc.attributeQuery("Orientation", n=obj, ex=1):
            continue
        if mc.attributeQuery("scaleFactor", n=obj, ex=1):
            compatibleCurves.append(obj)
        allCurves.append(obj)

    # Check for dialog result
    if allCurves != compatibleCurves:
        from . import ui
        dialog = ui.scaleFactorConversionDialog()
        if not dialog:
            MESSAGE.warningInView('Operation Cancelled')
            return
    if dialog == 'Skip':
        finalCurves = compatibleCurves
    elif dialog == 'All':
        finalCurves = allCurves

    # Init progress bar
    progress = utils.ProgressBar("Converting Curves", len(finalCurves))

    finalSelection = []
    for curve in sel:
        if progress.tick(1):
            break

        # Find components
        curve = selectPart(1, True, curve)[0]
        geo = selectPart(2, True, curve)[0]
        grp = selectPart(0, True, curve)[0]
        firstCv = '%s.cv[0]' % curve
        firstCvPos = mc.pointPosition(firstCv)
        firstCvVec = om.MVector(firstCvPos)
        om_sel = om.MSelectionList()
        om_sel.add(geo)
        om_mesh = om.MFnMesh(om_sel.getDagPath(0))

        # Get original attributes
        origProfile = None
        if mc.attributeQuery('Profile', n=curve, ex=1):
            origProfile = mc.getAttr(curve + '.Profile')
        origLattice = getLatticeValues(curve)
        origAttrs = attributes.getAttr(curve)
        origGraphs = attributes.getMultiInst(curve)

        # Get original material
        origMaterial = utils.getShader(geo)

        # Get original layer
        layer = mc.listConnections(curve, type='displayLayer')
        originalLayerID = re.findall(r'\d+', layer[0])[0]

        # Get a vertex position closest to the root CV of the curve
        origProfileVert, origProfileVec = utils.getMiddleVertAndNormal(curve, geo, firstCvVec)

        # Resetting attrs before orientation aligning
        utils.resetAttributes(curve, geo)
        _, targetVec, _ = om_mesh.getClosestPointAndNormal(om.MPoint(firstCvPos), space=om.MSpace.kWorld)

        # Duplicating curve
        topGrp = mc.listRelatives(grp, p=1, pa=1)
        duplicatedCurve = mc.duplicate(curve)
        if topGrp:
            duplicatedCurve = mc.parent(duplicatedCurve, topGrp)[0]
        else:
            duplicatedCurve = mc.parent(duplicatedCurve, w=1)[0]
        mc.delete(grp)

        # Cleanup
        mc.select(duplicatedCurve, r=1)
        filteredCurves = []

        # Convert
        if targetType == 0:  # Warp Card
            filteredCurves = create.multiple(0, hk=True, progressBar=False, keepAttrs=False)
        elif targetType == 1:  # Warp Tube
            filteredCurves = create.multiple(1, hk=True, progressBar=False, keepAttrs=False)
        elif targetType == 2:  # Extrude Card
            filteredCurves = create.multiple(-2, hk=True, progressBar=False, keepAttrs=False)
        elif targetType == 3:  # Extrude Tube
            filteredCurves = create.multiple(-1, hk=True, progressBar=False, keepAttrs=False)
        finalSelection.append(filteredCurves[0])

        # Align vars
        curve = filteredCurves[0]
        firstCv = '%s.cv[0]' % curve
        firstCvPos = mc.pointPosition(firstCv)
        firstCvVec = om.MVector(firstCvPos)
        om_pos = om.MPoint(firstCvPos)
        om_sel = om.MSelectionList()
        geo = selectPart(2, True, curve)[0]
        om_sel.add(geo)
        om_mesh = om.MFnMesh(om_sel.getDagPath(0))

        # Iterate align normals
        prevDiff = 360
        currentDiff = 360
        iteration = 0
        iterLimit = 10
        tolerance = 0.1
        guesses = []
        while (currentDiff >= tolerance) and (iteration <= iterLimit):
            _, faceNormal, _ = om_mesh.getClosestPointAndNormal(om_pos, space=om.MSpace.kWorld)
            currentDiff = faceNormal.angle(targetVec) * 180.0 / math.pi
            currentOrien = mc.getAttr(curve + '.Orientation')

            guesses.append((currentDiff, currentOrien))

            if currentDiff > prevDiff:
                guess = currentOrien - currentDiff
            elif currentDiff < prevDiff:
                guess = currentOrien + currentDiff
            else:
                guess = currentOrien
            nextOrien = guess
            prevDiff = currentDiff

            mc.setAttr(curve + '.Orientation', nextOrien % 360.0)
            iteration += 1

        # Setting the best guess as the final orientation
        finalOrientation = min(guesses, key=lambda t: t[0])[1]
        mc.setAttr(curve + '.Orientation', finalOrientation % 360.0)

        # Restore the original attributes
        attributes.setAttr(curve, origAttrs, exclude=["Orientation"])
        if origGraphs:
            for graph in origGraphs:
                attributes.setMultiInst(curve, graph)

        # Fix Profile
        if mc.attributeQuery("Profile", n=curve, ex=1) and origProfileVert and 'Profile' in origAttrs:
            newProfileVert, newProfileVec = utils.getMiddleVertAndNormal(curve, selectPart(2, True, curve)[0], firstCvVec)

            # Checking if normals of the flat card are correct. If not, flip the card 180 deg.
            normalCheck = origProfileVec.angle(newProfileVec) * 180.0 / math.pi
            if abs(normalCheck) >= 90:
                mc.setAttr(curve + ".Orientation", (mc.getAttr(curve + ".Orientation") + 180.0) % 360.0)

            # Checking if the angle between two middle vertices is correct. If not, invert the profile.
            angleBetween = (firstCvVec - origProfileVert).angle(firstCvVec - newProfileVert) * 180.0 / math.pi
            newProfile = origProfile * -1 if abs(angleBetween) >= 90 else origProfile
            mc.setAttr(curve + ".Profile", newProfile)

            # Setting the original Lattice
            if origLattice and mc.attributeQuery("Length", n=curve, ex=1):
                updateLattice(utils.fromDouble2ToString(origLattice), curve)

        # Apply original material
        newGeo = selectPart(2, True, curve)
        if newGeo and origMaterial:
            mc.sets(newGeo[0], forceElement=list(origMaterial)[0])

        # Sort to original layers
        curveAddToLayer(originalLayerID, inputCurves=[curve])

    progress.end()
    mc.select(finalSelection, r=1)


def toggleDynamicDivisions():
    """
    Toggles dynamic divisions on selected curves
    If dynamic node set is not available - create one
    """
    sel = mc.ls(sl=1, tr=1)
    sel = selectPart(1, True, mc.filterExpand(sel, sm=9))
    if not sel:
        return
    for curve in sel:
        if not mc.attributeQuery('lengthDivisions', n=curve, ex=1):
            continue
        divConnections = mc.listConnections(curve + '.lengthDivisions', d=1, scn=1)
        tesselateNode = None
        for targetNode in divConnections:
            if mc.nodeType(targetNode) == 'nurbsTessellate':
                tesselateNode = targetNode
                break
        if tesselateNode:
            create.addDynamicDivisions(curve, tesselateNode)
            mc.setAttr(curve + '.dynamicDivisions', 1)
        else:  # Just toggle the dynamic divisions functionality
            mc.setAttr(curve + '.dynamicDivisions', WIDGETS['dynamicDivisions'].isChecked())


def toggleAutoRefine():
    """
    Toggles automatic curve refinement
    If no auto-refine node found - create one
    """
    sel = mc.ls(sl=1, tr=1)
    sel = selectPart(1, True, mc.filterExpand(sel, sm=9))
    if not sel:
        return
    for curve in sel:
        if not mc.attributeQuery('Orientation', n=curve, ex=1):
            continue
        curveRefineConnection = mc.listConnections(curve + '.curveRefine', d=1, scn=1)
        rebuildCurveNode = None
        for targetNode in curveRefineConnection:
            if mc.nodeType(targetNode) == 'rebuildCurve':
                rebuildCurveNode = targetNode
                break
        if rebuildCurveNode:
            newNode = create.addAutoRefine(curve, rebuildCurveNode)
            mc.setAttr(curve + '.autoRefine', 1)
            mc.setAttr(newNode + '.isHistoricallyInteresting', 0)
            utils.deferredLp(curveControlUI.updateUI)()
        else:  # Just toggle the dynamic auto refine checkbox
            mc.setAttr(curve + '.autoRefine', WIDGETS['autoRefine'].isChecked())
            utils.deferredLp(curveControlUI.updateUI)()
