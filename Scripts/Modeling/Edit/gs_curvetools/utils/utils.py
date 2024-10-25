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

import cProfile
import functools
import inspect
import itertools
import logging
import math
import os
import pstats
import re
import subprocess
import sys
import traceback

try:
    from collections.abc import Iterable
except BaseException:
    from collections import Iterable

from functools import partial as pa
from functools import wraps
from imp import reload
from os import path

import maya.api.OpenMaya as om
import maya.cmds as mc
import maya.mel as mel

from ..constants import *

gs_curvetools_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')

### Logging ###
class Logger:
    """ Create logger, log and print messages"""

    def __init__(self):
        logFilePath = os.path.join(gs_curvetools_path, 'log.log').replace('\\', '/')  # type: str
        # Check if file already there and its size. Delete if too large.
        if os.path.exists(logFilePath):
            size = os.stat(logFilePath).st_size
            if size >= 1024 * 1024:  # 1 mb max log size
                try:
                    os.remove(logFilePath)
                except BaseException:
                    pass
        # Create logger
        self.logger = logging.getLogger("GS_CurveTools")
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        # File handler
        fileLog = logging.FileHandler(filename=logFilePath, encoding='utf-8')
        fileLog.set_name("File Output")
        fileLog.setLevel(logging.DEBUG)
        # Console handler
        consoleLog = logging.StreamHandler(stream=sys.stdout)
        consoleLog.set_name("Console Output")
        consoleLog.setLevel(logging.INFO)
        # Formatter
        fileFormatter = logging.Formatter(
            fmt='[%(asctime)s,%(msecs)03d | %(levelname)5.5s | %(module)8.8s | %(lineno)5d]: %(funcName)s() : %(message)s',
            datefmt='%H:%M:%S')
        consoleFormatter = logging.Formatter(
            fmt='[GS CurveTools|%(levelname)s]: %(message)s')
        fileLog.setFormatter(fileFormatter)
        consoleLog.setFormatter(consoleFormatter)
        # Add handlers to the logger
        self.logger.handlers = []
        self.logger.addHandler(fileLog)
        self.logger.addHandler(consoleLog)

    def inView(self, message):
        """ InView Message """
        self.logger.debug(message)
        mc.inViewMessage(smg=str(message), pos='topCenter', f=1, fit=50, fot=50)

    def warning(self, message):
        """ Print Warning Message """
        self.logger.error(message)
        trace = traceback.format_stack(limit=2)
        self.logger.debug(trace[0].splitlines()[0].strip())
        mc.warning(message)

    def warningInView(self, message):
        """ Print Warning and InView message """
        self.logger.error(message)
        trace = traceback.format_stack(limit=2)
        self.logger.debug(trace[0].splitlines()[0].strip())
        mc.warning(message)
        mc.inViewMessage(smg=message, pos='topCenter', f=1, fit=50, fot=50)

    def printInView(self, message):
        """ Print to Script Editor and InView message """
        self.logger.info(message)
        mc.inViewMessage(smg=message, pos='topCenter', f=1, fit=50, fot=50)

    def openLogFile(self):
        if OS == "mac":
            self.warning('Opening log file is not supported on Mac. Please open it manually from gs_curvetools folder:')
            self.warning('{}'.format(path.join(gs_curvetools_path, 'log.log').replace('\\', '/')))
            return
        subprocess.call('notepad "{}"'.format(path.join(gs_curvetools_path, 'log.log').replace('\\', '/')), creationflags=0x00000008)


logger = Logger()

MESSAGE = logger
LOGGER = logger.logger


# Some version specific compatibility stuff
if sys.version_info >= (3, 0):
    from io import StringIO
    fixedWraps = wraps
else:
    # Old python import for StringIO
    from io import BytesIO as StringIO

    # Legacy wraps for python 2.7 to fix some errors
    def wrapsSafely(obj, attr_names=functools.WRAPPER_ASSIGNMENTS):
        return wraps(obj, assigned=itertools.ifilter(functools.partial(hasattr, obj), attr_names))
    fixedWraps = wrapsSafely


### Decorators ###

def deferred(func):
    """Deferred execution"""
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        try:
            mc.evalDeferred(pa(func, *args, **kwargs))
        except Exception as e:
            LOGGER.exception(e)
    return wrapper


def deferredLp(func):
    """Deferred execution (lowest priority)"""
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        try:
            rv = mc.evalDeferred(pa(func, *args, **kwargs), lp=1)
        except Exception as e:
            LOGGER.exception(e)
        return rv
    return wrapper


def executeNext(func):
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        try:
            mc.evalDeferred(pa(func, *args, **kwargs), en=1)
        except Exception as e:
            LOGGER.exception(e)
    return wrapper


def parseMelCommand(pythonCmd, *args, **_):
    """ Convert python function call to MEL compatible call with all the args"""
    if inspect.ismethod(pythonCmd):
        instName = pythonCmd.__self__.name
    else:
        instName = False
    module = pythonCmd.__module__
    function = pythonCmd.__name__
    arguments = "({})".format(','.join(str(x) if not isinstance(x, str) else "'{}'".format(str(x)) for x in args))
    if instName:
        cmd = "{}.{}.{}{}".format(module, instName, function, arguments)
    else:
        cmd = "{}.{}{}".format(module, function, arguments)
    melCommand = 'python("import {};{}");'.format(module, cmd)
    return melCommand


def undo(func):
    """ Safe Undo Open/Close Chunk """
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        funcName = str(func.__name__)
        mc.undoInfo(ock=1, cn=funcName)
        rv = None
        try:
            rv = func(*args, **kwargs)
            try:
                mc.repeatLast(
                    ac=parseMelCommand(func, *args, **kwargs),
                    acl=funcName
                )
            except Exception as e:
                LOGGER.exception(e)
        except Exception as e:
            LOGGER.exception(e)
        finally:
            mc.undoInfo(cck=1)
        return rv
    return wrapper


def noUndo(func):
    """ Safe "State Without Flush" """
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        mc.undoInfo(swf=0)
        rv = None
        try:
            rv = func(*args, **kwargs)
        except Exception as e:
            LOGGER.exception(e)
        finally:
            mc.undoInfo(swf=1)
        return rv
    return wrapper


### Time classes ###


class Timer:
    """ Timer """
    t0 = 0

    @classmethod
    def increment(cls, sec):
        cls.t = mc.timerX()
        if cls.t >= cls.t0 + sec:
            cls.t0 = cls.t
            return True
        else:
            return False


### Debug ###


class Profiler():

    def __init__(self):
        self.pr = cProfile.Profile()
        self.pr.enable()

    def end(self):
        self.pr.disable()
        s = StringIO()
        sort = 'tottime'
        ps = pstats.Stats(self.pr, stream=s).sort_stats(sort)
        ps.print_stats()
        print(s.getvalue())  # pylint: disable=print-statement


def profile(func):
    """Profiles the execution speed of the function or method"""
    @fixedWraps(func)
    def wrapper(*args, **kwargs):
        p = Profiler()
        rv = func(*args, **kwargs)
        p.end()
        return rv
    return wrapper


class DebugDraw:

    timer = Timer()

    @staticmethod
    def returnMaterial(color):
        matName = 'GS_DEBUG_Material_{}_{}_{}'.format(
            str(color[0]).replace('.', ''),
            str(color[1]).replace('.', ''),
            str(color[2]).replace('.', '')
        )
        if not mc.objExists(matName):
            lambert = mc.shadingNode('lambert', asShader=1, n=matName, ss=1)
            mc.setAttr(lambert + '.color', color[0], color[1], color[2])
            mc.setAttr(lambert + '.incandescence', color[0], color[1], color[2])
            mc.setAttr(lambert + '.ambientColor', color[0], color[1], color[2])
            mc.setAttr(lambert + '.transparency', 0.5, 0.5, 0.5)
            lambert_set = mc.sets(r=1, nss=1, em=1, n=matName + '_set')
            mc.connectAttr(lambert + '.outColor', lambert_set + '.surfaceShader')
            return lambert_set
        else:
            lambert_set = mc.listConnections(matName + '.outColor', t='shadingEngine')[0]
            return lambert_set

    @classmethod
    def sceneCleanup(cls, ignoreTimer=False):
        # Don't cleanup the scene if multiple objects are created at the same time
        if not cls.timer.increment(5) and not ignoreTimer:
            return
        allNodes = mc.ls()
        for node in allNodes:
            if 'GS_DEBUG_' in node and mc.objExists(node) and mc.nodeType(node) == 'transform':
                mc.delete(node)

    @classmethod
    def setGeoStyle(cls, geo, color):
        # type: (list[tuple[str, str]], tuple[float, float, float]) -> None
        """ Apply debug render style to list of transforms """
        if not isinstance(geo, list) and not isinstance(geo, tuple):
            geo = [geo]
        for tr in geo:
            mc.setAttr(tr + '.overrideEnabled', 1)
            mc.setAttr(tr + '.overrideDisplayType', 2)
            mc.setAttr(tr + '.overrideRGBColors', 1)
            mc.setAttr(tr + '.overrideColorA', 0)
            mat = cls.returnMaterial(color)
            mc.sets(tr, e=1, fe=mat, nw=1)

    @classmethod
    def sphere(cls, center, radius=0.1, dir=(0, 1, 0), color=(0, 1, 0), label=''):
        cls.sceneCleanup()
        center = (center[0], center[1], center[2])
        sphere = mc.polySphere(n="GS_DEBUG_Sphere#", ax=dir, r=radius, sx=8, sy=8, ch=0, o=1, cuv=0)
        mc.move(center[0], center[1], center[2], sphere, xyz=1)
        cls.setGeoStyle(sphere, color)
        if label:
            mc.headsUpMessage(label, o=sphere[0], time=100, vp=1)

    @classmethod
    def arrow(cls, origin=(0, 0, 0), target=(1, 0, 0), size=0.1, color=(0, 1, 0), label=''):
        cls.sceneCleanup()
        origSel = mc.ls(sl=1)
        origin = (origin[0], origin[1], origin[2])
        target = (target[0], target[1], target[2])
        cylinderTransform, cylinderCreator = mc.polyCylinder(n='GS_DEBUG_Arrow#', ch=1, ax=(0, 1, 0), r=0.1, h=1, sh=1, sc=1, sa=8)
        pyramidTransform, pyramidCreator = mc.polyPyramid(ch=1, ax=(0, 1, 0), w=1, ns=4)

        mc.setAttr(pyramidTransform + '.inheritsTransform', 0)
        multX = mc.createNode('multDoubleLinear')
        mc.setAttr(multX + '.input2', 0.3)
        mc.connectAttr(cylinderTransform + '.scaleX', multX + '.input1', f=1)
        mc.connectAttr(multX + '.output', pyramidTransform + '.scaleX')
        multZ = mc.createNode('multDoubleLinear')
        mc.setAttr(multZ + '.input2', 0.3)
        mc.connectAttr(cylinderTransform + '.scaleZ', multZ + '.input1', f=1)
        mc.connectAttr(multZ + '.output', pyramidTransform + '.scaleZ')
        add = mc.createNode('addDoubleLinear')
        mc.connectAttr(cylinderTransform + '.scaleX', add + '.input1')
        mc.connectAttr(cylinderTransform + '.scaleZ', add + '.input2')
        divide = mc.createNode('multDoubleLinear')
        mc.setAttr(divide + '.input2', .5)
        mc.connectAttr(add + '.output', divide + '.input1')
        mc.connectAttr(divide + '.output', pyramidTransform + '.scaleY')
        mc.setAttr(pyramidCreator + '.heightBaseline', -1)
        mc.setAttr(cylinderCreator + '.heightBaseline', -1)
        mc.select(cylinderTransform + '.vtx[17]', pyramidTransform, r=1)
        mc.pointOnPolyConstraint(w=1)
        mc.parent(pyramidTransform, cylinderTransform)
        mc.move(origin[0], origin[1], origin[2], cylinderTransform, xyz=1)
        locator = mc.spaceLocator(p=(0, 0, 0))
        mc.xform(locator, cp=1, t=target, a=1)
        aim = mc.aimConstraint(locator, cylinderTransform, aim=(0, 1, 0))
        dist = mc.createNode('distanceBetween')
        mc.connectAttr(locator[0] + '.translate', dist + '.point1')
        mc.connectAttr(cylinderTransform + '.translate', dist + '.point2')
        mult = mc.createNode('multDoubleLinear')
        mc.connectAttr(divide + '.output', mult + '.input1')
        mc.setAttr(mult + '.input2', -0.7)
        subtract = mc.createNode('addDoubleLinear')
        mc.connectAttr(mult + '.output', subtract + '.input2')
        mc.connectAttr(dist + '.distance', subtract + '.input1')
        mc.connectAttr(subtract + '.output', cylinderTransform + '.scaleY')
        mc.setAttr(cylinderTransform + ".sx", size)
        mc.setAttr(cylinderTransform + ".sz", size)
        cls.setGeoStyle([pyramidTransform, cylinderTransform], color)
        mc.delete(aim, locator)
        mc.select(cylinderTransform, r=1)
        mc.select(origSel, r=1)
        if label:
            mc.headsUpMessage(label, o=cylinderTransform, time=100, vp=1)


### Misc utils ###


def stopUI(state=False):
    from .. import core
    windows = [
        core.MAIN_WINDOW_NAME,
        core.CURVE_CONTROL_NAME,
        core.UV_EDITOR_NAME,
        core.SCALE_FACTOR_UI,
        'GSCT_RandomizeCurvePopOut',
        'GSCT_AttributesFilterPopOut',
        'GSCT_TwistGraphPopOut',
        'GSCT_WidthGraphPopOut',
        'GSCT_CurveThicknessWindow',
        'GSCT_LayerEditorWindow',
        'GSCT_CustomLayerColorsWindow',
        'GSCT_OrientToNormalsWindow',
        'GSCT_CardToCurvePopOut',
    ]

    # Delete advanced visibility node
    if all(mc.getClassification("GSCT_CurveTools_DrawManagerNode")):
        sel = mc.ls(typ="GSCT_CurveTools_DrawManagerNode")
        for n in sel:
            if "GSCT_CurveTools_DrawManager" in n:
                mc.delete(mc.listRelatives(n, p=1, pa=1))

    # Delete workspaces
    for window in windows:
        if MAYA_VER <= 2017:
            if mc.workspaceControl(window, q=1, ex=1):
                mc.workspaceControl(window, e=1, floating=1)
                mc.deleteUI(window)
            return 0

        if mc.workspaceControl(window, q=1, ex=1):
            if mc.workspaceControl(window, q=1, vis=1):
                if mc.workspaceControl(window, q=1, fl=1):
                    mc.workspaceControl(window, e=1, clp=False)
                    mc.workspaceControl(window, e=1, cl=1)
                elif mc.workspaceControl(window, q=1, clp=1):
                    mc.workspaceControl(window, e=1, clp=False)
                    mc.workspaceControl(window, e=1, cl=1)
                else:
                    mc.workspaceControl(window, e=1, cl=1)
            mc.deleteUI(window)
        if state:
            if mc.workspaceControlState(window, q=1, ex=1):
                LOGGER.info("Deleting window state for %s" % window)
                mc.workspaceControlState(window, r=1)


@deferred
def resetUI():
    resetOptionVars()
    if MAYA_VER >= 2018:
        stopUI(True)

    # Reload all files
    from importlib import import_module
    files = [
        '.constants',
        '.core',
        '.main',
        '.ui',
        '.uv_editor',
        '.utils.gs_math',
        '.utils.style',
        '.utils.tooltips',
        '.utils.utils',
        '.utils.wrap',
    ]
    modules = {}
    for file in files:
        modules[file] = import_module(file, 'gs_curvetools')
    for module in modules:
        reload(modules[module])

    # Run main function
    if '.main' in modules:
        modules['.main'].main()
    else:
        try:
            from .. import main
            main.main()
        except ImportError as e:
            LOGGER.exception(e)
            raise ImportError('Main not found!')


def resetOptionVars():
    mc.optionVar(fv=["GSCT_globalScaleFactor", 1])
    mc.optionVar(fv=["GSCT_globalCurveThickness", -1])
    mc.optionVar(iv=['GSCT_warpSwitch', 1])
    mc.optionVar(iv=["GSCT_syncCurveColor", 0])
    mc.optionVar(iv=['GSCT_colorOnlyDiffuse', 1])
    mc.optionVar(iv=["GSCT_colorizedRegroup", 0])
    mc.optionVar(iv=["GSCT_checkerPattern", 0])
    mc.optionVar(iv=["GSCT_ignoreLastLayer", 1])
    mc.optionVar(iv=["GSCT_ignoreTemplateCollections", 1])
    mc.optionVar(iv=["GSCT_groupTemplateCollections", 1])
    mc.optionVar(iv=["GSCT_syncOutlinerLayerVis", 1])
    mc.optionVar(iv=["GSCT_keepCurveAttributes", 1])
    mc.optionVar(iv=["GSCT_massBindOption", 0])
    mc.optionVar(iv=["GSCT_boundCurvesFollowParent", 1])
    mc.optionVar(iv=["GSCT_bindDuplicatesCurves", 0])
    mc.optionVar(iv=["GSCT_bindFlipUVs", 1])
    mc.optionVar(iv=["GSCT_populateBlendAttributes", 1])
    mc.optionVar(iv=["GSCT_convertInstances", 1])
    mc.optionVar(iv=["GSCT_replacingCurveLayerSelection", 1])
    mc.optionVar(iv=["GSCT_flipUVsAfterMirror", 1])
    mc.optionVar(iv=["GSCT_useAutoRefineOnNewCurves", 1])
    mc.optionVar(iv=["GSCT_layerNumbersOnly", 0])
    mc.optionVar(iv=['GSCT_2layerRows', 1])
    mc.optionVar(iv=['GSCT_3layerRows', 0])
    mc.optionVar(iv=['GSCT_4layerRows', 0])
    mc.optionVar(iv=['GSCT_6layerRows', 0])
    mc.optionVar(iv=['GSCT_8layerRows', 0])
    mc.optionVar(iv=['GSCT_UVBugMessageDismissed', 0])
    mc.optionVar(iv=['GSCT_UVEditorTransparencyToggle', 0])
    mc.optionVar(iv=['GSCT_UVEditorAlphaOnly', 0])
    mc.optionVar(iv=['GSCT_enableTooltips', 1])
    mc.optionVar(iv=['GSCT_showLayerCollectionsMenu', 1])
    mc.optionVar(iv=['GSCT_importIntoANewCollection', 0])
    mc.optionVar(iv=['GSCT_AutoHideCurvesOnInactiveCollections', 0])
    mc.optionVar(sv=['GSCT_UVEditorBGColor', "(36, 36, 36)"])
    mc.optionVar(sv=['GSCT_UVEditorGridColor', "(50, 50, 50)"])
    mc.optionVar(sv=['GSCT_UVEditorFrameColor', "(160, 75, 75)"])
    mc.optionVar(sv=['GSCT_UVEditorUVFrameSelectedColor', "(255, 255, 255)"])
    mc.optionVar(sv=['GSCT_UVEditorUVFrameDeselectedColor', "(128, 128, 128)"])
    mc.optionVar(sv=['GSCT_UVEditorUVCardFillColor', "(96, 100, 160)"])
    mc.optionVar(sv=['GSCT_AttributesFilter', "{'Orientation': False}"])
    mc.optionVar(iv=['GSCT_CardToCurveOutputType', 0])
    mc.optionVar(iv=['GSCT_CardToCurveCardType', 0])
    mc.optionVar(iv=['GSCT_GeometryHighlightEnabled', 0])
    mc.optionVar(
        sv=['GSCT_CardToCurveOptions',
            "{'gsCardToCurve_horizontalFlip': False, 'gsCardToCurve_verticalFlip': False}"]
    )
    # Advanced visibility options
    mc.optionVar(fv=['GSCT_' + 'gsPointSizeSlider', 10.5])
    mc.optionVar(fv=['GSCT_' + 'gsCurveWidthSlider', 4.0])
    mc.optionVar(fv=['GSCT_' + 'gsHullWidthSlider', 3.0])
    mc.optionVar(sv=['GSCT_' + 'gsDeselectedCVColor', "[1, 0, 0]"])
    mc.optionVar(fv=['GSCT_' + 'gsDeselectedCVAlpha', 1.0])
    mc.optionVar(sv=['GSCT_' + 'gsSelectedCVColor', "[0, 1, 0]"])
    mc.optionVar(fv=['GSCT_' + 'gsSelectedCVAlpha', 1.0])
    mc.optionVar(sv=['GSCT_' + 'gsCurveHighlightColor', "[0, 0, 1]"])
    mc.optionVar(fv=['GSCT_' + 'gsCurveHighlightAlpha', 1.0])
    mc.optionVar(sv=['GSCT_' + 'gsHullHighlightColor', "[0.5, 0, 0.5]"])
    mc.optionVar(fv=['GSCT_' + 'gsHullHighlightAlpha', 1.0])
    mc.optionVar(iv=['GSCT_' + 'gsCurveVisibilityToggle', 1])
    mc.optionVar(iv=['GSCT_' + 'gsHullVisibilityToggle', 0])

    mc.optionVar(iv=['GSCT_' + 'gsLazyUpdateToggle', 0])
    mc.optionVar(iv=['GSCT_' + 'gsAlwaysOnTopToggle', 1])

    mc.optionVar(iv=['GSCT_' + 'gsCVDistanceColor', 1])
    mc.optionVar(iv=['GSCT_' + 'gsHullDistanceColor', 1])
    mc.optionVar(iv=['GSCT_' + 'gsCurveDistanceColor', 1])
    mc.optionVar(fv=['GSCT_' + 'gsDistanceColorMinValue', 0.25])
    mc.optionVar(fv=['GSCT_' + 'gsDistanceColorMaxValue', 1.0])

    mc.optionVar(iv=['GSCT_' + 'gsEnableCVOcclusion', 0])
    mc.optionVar(sv=['GSCT_' + 'gsOccluderMeshName', ""])


def fixMaya2020UVs():
    success = 0
    total = 0
    for i in range(80):
        try:
            group = 'curveGrp_%s_Geo' % i
            if mc.objExists(group):
                geometry = mc.editDisplayLayerMembers(group, q=1, fn=1, nr=1)
                for geo in geometry:
                    total += 1
                    allUVNodes = list()
                    history = mc.listHistory(geo, il=0)
                    for node in history:
                        if mc.nodeType(node) == 'polyMoveUV':
                            allUVNodes.append(node)
                    for node in allUVNodes:
                        mc.setAttr(node + '.inputComponents', 1, 'map[*]', type='componentList')
                    success += 1
        except BaseException:
            pass
    additionalMessage = ''
    if success != total:
        additionalMessage = ' Some cards were not fixed!'
    MESSAGE.printInView('Fixed %s/%s Cards.%s' % (success, total, additionalMessage))


def fixMaya2020Twist():
    dialog = mc.confirmDialog(
        title='Fix Maya 2020.4 Twist',
        message='This command will fix Maya 2020.4 Twist Attribute Bug\n\
Only use it if you have issues with Twist and Inv.Twist Attributes\n\n\
Proceed?',
        button=['Yes', 'No'],
        defaultButton='Yes',
        cancelButton='No',
        dismissString='No',
        icon='information'
    )
    if dialog == 'No':
        return
    success = 0
    total = 0
    for i in range(80):
        try:
            group = 'curveGrp_%s_Curve' % i
            if mc.objExists(group):
                curve = mc.editDisplayLayerMembers(group, q=1, fn=1, nr=1)
                for crv in curve:
                    if mc.attributeQuery('invTwist', n=crv, ex=1):
                        total += 1
                        twist = mc.listConnections(crv + '.invTwist', d=1, scn=1)
                        twistHandle = mc.listConnections(twist[0] + '.deformerData', s=1, scn=1)
                        twistHandleShape = mc.listRelatives(twistHandle[0], c=1, pa=1)
                        connectionCheck = mc.isConnected(twist[0] + '.startAngle', twistHandleShape[0] + '.startAngle')
                        if not connectionCheck:
                            mc.connectAttr(twist[0] + '.startAngle', twistHandleShape[0] + '.startAngle', f=1)
                            mc.connectAttr(twist[0] + '.endAngle', twistHandleShape[0] + '.endAngle', f=1)
                            success += 1
        except BaseException:
            pass
    MESSAGE.printInView('Fixed %s/%s Cards.' % (success, total))


def fixMaya2020Unbind():
    dialog = mc.confirmDialog(
        title='Fix Maya 2020.4 Unbind',
        message='This command will fix Maya 2020.4 Unbind Function Bug\n\
Only use it if you have issues with Unbind Function\n\n\
Proceed?',
        button=['Yes', 'No'],
        defaultButton='Yes',
        cancelButton='No',
        dismissString='No',
        icon='information'
    )
    if dialog == 'No':
        return

    success = 0
    total = 0
    for i in range(80):
        try:
            group = 'curveGrp_%s_Curve' % i
            if mc.objExists(group):
                curve = mc.editDisplayLayerMembers(group, q=1, fn=1, nr=1)
                for crv in curve:
                    if mc.attributeQuery('profileMagnitude', n=crv, ex=1):
                        total += 1
                        ffd = mc.listConnections(crv + '.profileMagnitude', s=0, d=1)
                        origGeo = mc.listConnections(ffd[0] + '.originalGeometry[0]', s=1, d=0, p=1)
                        if origGeo:
                            mc.disconnectAttr(origGeo[0], ffd[0] + '.originalGeometry[0]')
                            success += 1
        except BaseException:
            pass
    MESSAGE.printInView('Fixed %s/%s Cards.' % (success, total))


class GetFolder:
    """ Get various folders from Maya """

    def scripts(self):
        return mc.internalVar(usd=1)

    def root(self):
        return path.join(gs_curvetools_path, '')

    def fonts(self):
        return path.join(gs_curvetools_path, 'fonts', '')

    def icons(self):
        return path.join(gs_curvetools_path, 'icons', '')

    def plugins(self):
        return path.join(gs_curvetools_path, 'plugins', '')


getFolder = GetFolder()


def attrExists(obj, attr):
    """ Check if attribute exists """
    if mc.objExists(obj):
        if mc.attributeQuery(attr, n=obj, ex=1):
            return 1
        else:
            return 0
    else:
        return 0


def getAttr(obj, attr):
    """ Check if obj exist, check if attr exist, return attr """
    if mc.objExists(obj):
        if mc.attributeQuery(attr, n=obj, ex=1):
            return mc.getAttr(obj + '.' + attr)
        else:
            return None
    else:
        return None


class ProgressBar():
    """Progress bar for Maya UI"""

    def __init__(self, name, maxValue):
        self.mainProgressBar = mel.eval('$tmp = $gMainProgressBar')
        self.end()
        mc.progressBar(self.mainProgressBar, edit=True, beginProgress=True, isInterruptable=True,
                       status=name, minValue=0, maxValue=maxValue)

    def tick(self, step):
        """ Returns "True" if ESC is pressed """
        if mc.progressBar(self.mainProgressBar, query=True, isCancelled=True):
            self.end()
            MESSAGE.warning('Function is Cancelled!')
            return True
        mc.progressBar(self.mainProgressBar, edit=True, step=step)
        return False

    def end(self):
        mc.progressBar(self.mainProgressBar, edit=True, endProgress=True)


def objectExists(obj):
    """ Check if object exists """
    if obj and len(obj):
        return mc.objExists(obj[0])
    else:
        return 0


def addAtIndex(addTo, index, add):
    """ Adds to source list at index. If list is empty, appends. """
    if len(addTo) <= index:
        addTo.append(add)
    else:
        addTo[index] = add


def getClosestPointAndNormal(targetMesh, pointPos=(0, 0, 0)):
    """
    (targetMesh, givenPointPosition) -> (MPoint, MVector, int)

    Returns a tuple containing the closest point on the mesh to the given point,
    the normal at that point, and the ID of the face in which that point lies.
    """
    pointPos = om.MPoint(pointPos)
    sel = om.MSelectionList()
    sel.add(targetMesh)
    fnMesh = om.MFnMesh(sel.getDagPath(0))

    pointAndNormal = fnMesh.getClosestPointAndNormal(pointPos, space=om.MSpace.kWorld)
    return pointAndNormal


def getClosestVertexAndNormal(targetMesh, pointPos=(0, 0, 0)):
    # type: (str, om.MVector | om.MPoint) -> tuple[om.MPoint, float, str, int, om.MVector]
    """
    returns: (vertPos, vertDist, vertName, vertIndex, faceNormal)

    Returns a tuple containing the closest to the pointPos vert on the mesh, the distance
    between this vert and pointPos, vertex name and vertex index
    """
    pos = om.MPoint(pointPos)
    sel = om.MSelectionList()
    sel.add(targetMesh)
    fn_mesh = om.MFnMesh(sel.getDagPath(0))

    index = fn_mesh.getClosestPoint(pos, space=om.MSpace.kWorld)[1]
    faceNormal = fn_mesh.getPolygonNormal(index, space=om.MSpace.kWorld)
    faceVerts = fn_mesh.getPolygonVertices(index)

    vertexDistances = ((vertex, fn_mesh.getPoint(vertex, om.MSpace.kWorld).distanceTo(pos))
                       for vertex in faceVerts)
    vertIndex, vertDistance = min(vertexDistances, key=lambda t: t[1])
    vertPosition = fn_mesh.getPoint(vertIndex, om.MSpace.kWorld)
    vertName = "{}.vtx[{}]".format(targetMesh, vertIndex)

    return (vertPosition, vertDistance, vertName, vertIndex, faceNormal)


def resetAttributes(inputCurve, inputGeo):
    # type: (str, str) -> None
    """
    Resets attributes to a default state suitable for mirroring and orientation adjustment
    """
    from .. import core

    if mc.attributeQuery('lengthDivisions', n=inputCurve, ex=1):
        mc.setAttr(inputCurve + '.lengthDivisions', 10)
        try:
            mc.setAttr(inputCurve + '.widthDivisions', 3)
        except BaseException:
            mc.setAttr(inputCurve + '.widthDivisions', 5)
    if mc.attributeQuery('Profile', n=inputCurve, ex=1):
        mc.setAttr(inputCurve + '.Profile', 0)
        core.updateLattice("0, 0.5, 0.333, 0.5, 0.667, 0.5, 1, 0.5", inputCurve)
    if mc.attributeQuery('Twist', n=inputCurve, ex=1):
        mc.setAttr(inputCurve + '.Twist', 0)
    # if mc.attributeQuery('invTwist', n=inputCurve, ex=1):
    #     mc.setAttr(inputCurve + '.invTwist', 0)
    if mc.attributeQuery('Length', n=inputCurve, ex=1):
        targetNode = mc.ls(mc.listHistory(inputGeo, ac=1, il=0), typ='curveWarp')[0]
        core.attributes.resetMultiInst(targetNode, 'scaleCurve')
        core.attributes.resetMultiInst(targetNode, 'twistCurve')


def resetAndReturnAttrs(curve):
    # type: (str) -> tuple[str, om.MVector, int, int, float, float, list[list[str]]]
    """
    Resets the attributes on a curve and returns original values as a list:

    returns [curve, origVec, lengthDivisions, widthDivisions, twist, invTwist, graphs]
    """
    from .. import core
    crvAttr = core.attributes.getAttr(curve)
    lengthDivisions = crvAttr['lengthDivisions'] if 'lengthDivisions' in crvAttr else None
    widthDivisions = crvAttr['widthDivisions'] if 'widthDivisions' in crvAttr else None
    twist = crvAttr['Twist'] if 'Twist' in crvAttr else None
    invTwist = crvAttr['invTwist'] if 'invTwist' in crvAttr else None

    if lengthDivisions and lengthDivisions > 10:
        mc.setAttr(curve + '.lengthDivisions', 10)
    if widthDivisions and widthDivisions > 2:
        try:
            mc.setAttr(curve + '.widthDivisions', 2)
        except BaseException:
            mc.setAttr(curve + '.widthDivisions', 4)
    if twist and twist != 0:
        mc.setAttr(curve + '.Twist', 0)
    if invTwist and invTwist != 0:
        mc.setAttr(curve + '.invTwist', 0)

    firstCv = '%s.cv[0]' % curve
    pos = mc.pointPosition(firstCv)
    geo = core.selectPart(2, True, curve)[0]

    graphs = None
    if mc.attributeQuery('Length', n=curve, ex=1):
        targetNode = mc.ls(mc.listHistory(geo, ac=1, il=0), typ='curveWarp')[0]
        graphs = core.attributes.getMultiInst(curve)
        core.attributes.resetMultiInst(targetNode, 'scaleCurve')
        core.attributes.resetMultiInst(targetNode, 'twistCurve')

    origVec = getClosestPointAndNormal(geo, pos)[1]
    return [curve, origVec, lengthDivisions, widthDivisions, twist, invTwist, graphs]


def getMiddleVertAndNormal(inputCurve, inputGeo, inputFirstCv):
    # type: (str, str, om.MVector) -> tuple[om.MVector, om.MVector]
    """Returns the middle profile vert of the card and normals of the flat card"""

    from .. import core

    # Getting original values
    origAttrs = core.attributes.getAttr(inputCurve)
    origGraphs = core.attributes.getMultiInst(inputCurve)
    origLattice = core.getLatticeValues(inputCurve)

    # Reset attributes
    resetAttributes(inputCurve, inputGeo)

    # Set a new temporary values
    if mc.attributeQuery('Profile', n=inputCurve, ex=1):
        mc.setAttr(inputCurve + ".Profile", 0)
    if origLattice:
        core.updateLattice("0, 0.5, 0.333, 0.5, 0.667, 0.5, 1, 0.5", inputCurve)
    mc.setAttr(inputCurve + '.lengthDivisions', 10)
    if mc.attributeQuery('Width', n=inputCurve, ex=1):
        mc.setAttr(inputCurve + '.widthDivisions', 3)
    else:
        mc.setAttr(inputCurve + '.widthDivisions', 5)

    # Get closest vert and normal value
    closestVertAndNormal = getClosestVertexAndNormal(inputGeo, inputFirstCv)

    # Get a position value for the closest vert
    if mc.attributeQuery('Profile', n=inputCurve, ex=1):
        profileScale = 2 * mc.getAttr(inputCurve + '.Width')
        if mc.attributeQuery('scaleFactor', n=inputCurve, ex=1):
            profileScale *= mc.getAttr(inputCurve + '.scaleFactor')
        mc.setAttr(inputCurve + '.Profile', math.copysign(profileScale, origAttrs['Profile']))
    vertexPos = mc.pointPosition("{}.vtx[{}]".format(inputGeo, closestVertAndNormal[3]))

    # Set the original attributes back
    core.attributes.setAttr(inputCurve, origAttrs)
    if origGraphs:
        for graph in origGraphs:
            core.attributes.setMultiInst(inputCurve, graph)
    if origLattice:
        core.updateLattice(fromDouble2ToString(origLattice), inputCurve)

    return (om.MVector(vertexPos), closestVertAndNormal[4])


def getUnitMult():
    mult = float(mc.convertUnit("1cm", fromUnit="cm", toUnit=mc.currentUnit(q=1, linear=1)))
    print("Current Mult:", mult)
    return mult


def polySelectSp(comps, obj=None):
    # type: (list[str], str) -> list[str]
    """polySelectSp wrapper"""
    if MAYA_VER >= 2023:
        return mc.ls(mc.polySelectSp(comps, q=1, loop=1), fl=1)
    else:
        return selectVertLoop(obj, comps)


def selectVertLoop(obj, comps):
    # type: (str, list[str]) -> list[str]
    """
    Returns vert loop list between two verts on the border
    For older Maya versions that had polySelectSp fail do to that
    """
    if len(comps) != 2:
        raise Exception("Wrong number of input verts")

    allFaces = "{}.f[*]".format(obj)

    def expandToEdges(verts):
        if MAYA_VER == 2018:
            if isinstance(verts, set):
                verts = list(verts)
        return set(mc.ls(mc.polyListComponentConversion(verts, fv=1, te=1), fl=1))

    def expandToVerts(edges):
        if MAYA_VER == 2018:
            if isinstance(edges, set):
                edges = list(edges)
        return set(mc.ls(mc.polyListComponentConversion(edges, fe=1, tv=1), fl=1))

    perimeterEdges = set(mc.ls(mc.polyListComponentConversion(allFaces, ff=1, te=1, bo=1)))
    if MAYA_VER == 2018:
        perimeterEdges = list(perimeterEdges)
    perimeterVerts = set(mc.ls(mc.polyListComponentConversion(perimeterEdges, fe=1, tv=1), fl=1))
    sourceVert = comps[0]  # type: str
    targetVert = comps[1]  # type: str
    pathOne = set()
    pathTwo = set()

    # Initial expand to find two possible paths
    initVerts = expandToVerts(expandToEdges(sourceVert))
    initVerts.remove(sourceVert)
    pathOne.add(initVerts.pop())
    pathTwo.add(initVerts.pop())

    # Check first path
    limit = 1000
    count = 0
    currentVert_one = pathOne.copy().pop()
    pathOne.add(sourceVert)
    currentVert_two = pathTwo.copy().pop()
    pathTwo.add(sourceVert)
    while count < limit:
        count += 1
        # Expand first path
        toEdges_one = expandToEdges(currentVert_one)
        toVerts_one = expandToVerts(toEdges_one)
        nonPerimeterVerts_one = toVerts_one.intersection(perimeterVerts)  # Filter out non-perimeter verts
        nextVert_one = nonPerimeterVerts_one.difference(pathOne)
        pathOne.update(nextVert_one)
        currentVert_one = nextVert_one.pop()
        if targetVert in pathOne:
            return list(pathOne)
        # Expand second path
        toEdges_two = expandToEdges(currentVert_two)
        toVerts_two = expandToVerts(toEdges_two)
        nonPerimeterVerts_two = toVerts_two.intersection(perimeterVerts)  # Filter out non-perimeter verts
        nextVert_two = nonPerimeterVerts_two.difference(pathTwo)
        pathTwo.update(nextVert_two)
        currentVert_two = nextVert_two.pop()
        if targetVert in pathTwo:
            return list(pathTwo)
    return None


def deleteKeysOnAllObjects():
    """Deletes all the keys on all nurbs curve in the scene"""
    for obj in mc.ls(typ='nurbsCurve'):
        deleteKeys(obj)


def deleteKeys(target):
    # type: (list[str]|str) -> None
    """Deletes keys from target curves and their CVs"""
    mc.cutKey(target, cl=1, t=(), hi='both', cp=1, s=1)


def colorFrom255to1(clr):
    if isinstance(clr, Iterable):
        clr = list(clr)
        for i in range(len(clr)):
            if isinstance(clr[i], float) or isinstance(clr[i], int):
                clr[i] = clr[i] / 255.0
        if clr:
            return clr
        else:
            MESSAGE.warning("Invalid color conversion")
    elif isinstance(clr, float) or isinstance(clr, int):
        return clr / 255.0
    else:
        MESSAGE.warning("Invalid color conversion")


def colorFrom1to255(clr):
    if isinstance(clr, Iterable):
        clr = list(clr)
        for i in range(len(clr)):
            if isinstance(clr[i], float) or isinstance(clr[i], int):
                clr[i] = clr[i] * 255.0
        if clr:
            return clr
        else:
            MESSAGE.warning("Invalid color conversion")
    elif isinstance(clr, float) or isinstance(clr, int):
        return clr * 255.0
    else:
        MESSAGE.warning("Invalid color conversion")


def fromStringToDouble2(inputString):
    splitPoints = inputString.split(',')
    splitPoints = filter(None, splitPoints)
    splitPoints = [float(point) for point in splitPoints]
    arrangedValues = [[splitPoints[i], splitPoints[i + 1]] for i in range(0, len(splitPoints), 2)]
    return arrangedValues


def fromDouble2ToString(inputList):
    newString = ''
    for i in range(len(inputList)):
        newString += '%s,%s,' % (inputList[i][0],
                                 inputList[i][1])
    return newString


def setDouble2Attr(node, attr, values):
    for i in range(len(values)):
        mc.setAttr('%s.%s[%s]' % (node, attr, i), values[i][0], values[i][1], typ='double2')


def convertInstanceToObj(objects=list()):
    """ Accepts a list and converts any found instances to objects """
    convert = mc.menuItem('gsConvertInstances', q=1, rb=1)
    finalList = list()
    if not objects:
        return finalList
    for obj in objects:
        if mc.attributeQuery('Orientation', n=obj, ex=1) and mc.connectionInfo(obj + '.Orientation', isSource=1):
            LOGGER.info(obj + ' is skipped. It is a part of existing curveCard/Tube.')
            continue
        par = mc.listRelatives(mc.listRelatives(obj, pa=1, c=1)[0], pa=1, ap=1)
        if len(par) > 1 and convert:
            dup = mc.duplicate(obj)
            mc.delete(obj)
            mc.rename(dup[0], obj)
            LOGGER.info(obj + ' is an instance. Converted to object.')
            finalList.append(obj)
        elif len(par) > 1 and not convert:
            LOGGER.info(obj + ' is skipped. It is an instance.')
        else:
            finalList.append(obj)
    mc.evalDeferred("print(' ')")
    return finalList


def mergeDicts(dict1, dict2, rd=False):
    """ Merge dictionaries and keep values of common keys in list. rd - remove duplicates """
    dict3 = dict()
    dict3.update(dict1)
    dict3.update(dict2)
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            if isinstance(dict1[key], list) and isinstance(dict2[key], list):
                for geo in dict1[key]:
                    dict3[key].append(geo)
            elif isinstance(dict1[key], list) and not isinstance(dict2[key], list):
                dict3[key] = [dict3[key]] + dict1[key]
            elif not isinstance(dict1[key], list) and isinstance(dict2[key], list):
                dict3[key].append(dict1[key])
            else:
                dict3[key] = [value, dict1[key]]
    if rd:
        for key in dict3:
            if isinstance(dict3[key], list):
                tmp = dict.fromkeys(dict3[key])
                dict3[key] = list(tmp)
    return dict3


def cleanDict(dict0):
    """Removes objects from the dict if they were not found in the scene"""
    for key in dict0:
        tempList = list()
        for geo in dict0[key]:
            if mc.objExists(geo):
                tempList = tempList + [geo]
        dict0[key] = tempList
    return dict0


def getShader(inputGeo):
    """ Returns a dict of shadingEngines from list of geo in format {shader: [geo1,geo2...]} """

    inputGeo = mc.filterExpand(inputGeo, sm=12)
    if not inputGeo:
        return {}

    shaderDict = dict()
    for geo in inputGeo:
        dag = mc.ls(geo, dag=1, s=1)
        shader = mc.listConnections(dag, d=1, s=1, t='shadingEngine')[0]
        shaderDict.setdefault(shader, [])
        shaderDict[shader].append(geo)

    return shaderDict


def connectMessage(source, target, message):
    """Creates messages in both nodes based on message name and connects them source->target\n
    Target node will be a multi-instance message"""
    if source == target:
        return
    if not mc.attributeQuery(message, n=source, ex=1):
        mc.addAttr(source, ln=message, at='message', k=0)
    if mc.attributeQuery(message, n=target, ex=1) and not mc.attributeQuery(message, n=target, m=1):
        mc.deleteAttr('{}.{}'.format(target, message))
    if not mc.attributeQuery(message, n=target, ex=1):
        mc.addAttr(target, ln=message, at='message', k=0, m=1, im=0)
    mc.connectAttr('{}.{}'.format(source, message), '{}.{}'.format(target, message), na=1)


def getMod():
    """ Get modifiers (Shift, Alt, Ctrl and '+' combinations) """
    mods = mc.getModifiers()
    if (mods & 1) > 0 and (mods & 4) > 0 and (mods & 8) > 0:
        return 'Shift+Ctrl+Alt'
    if (mods & 1) > 0 and (mods & 4) > 0:
        return 'Shift+Ctrl'
    if (mods & 1) > 0 and (mods & 8) > 0:
        return 'Shift+Alt'
    if (mods & 4) > 0 and (mods & 8) > 0:
        return 'Ctrl+Alt'
    if (mods & 1) > 0:
        return 'Shift'
    if (mods & 4) > 0:
        return 'Ctrl'
    if (mods & 8) > 0:
        return 'Alt'


def getHotkeyMod(hk, key):
    # type: (int, str) -> bool
    """Gets key modifiers and checks if hotkey was used"""
    return True if hk == 2 or (hk is None and getMod() == key) else False


def fixDuplicateNames(nodes=None):
    """ Fixes duplicate names conflicts in input nodes or all nodes in the scene """
    if not nodes:
        nodes = mc.ls()
    duplicates = [node for node in nodes if '|' in node]
    duplicates.sort(key=lambda obj: obj.count('|'), reverse=True)
    newNames = []
    if not duplicates:
        return []
    for obj in duplicates:
        regEx1 = re.compile("[^|]*$").search(obj)
        shortName = regEx1.group(0)
        regEx2 = re.compile(".*[^0-9]").match(shortName)
        if regEx2:
            stripSuffix = regEx2.group(0)
        else:
            stripSuffix = shortName
        newName = mc.rename(obj, (stripSuffix + "#"))
        newNames.append(newName)
    return newNames


def checkIfBezier(inputCurve):
    if mc.nodeType(mc.listRelatives(inputCurve, c=1, pa=1)) == "bezierCurve":
        origSel = mc.ls(sl=1)
        mc.select(inputCurve, r=1)
        result = mc.bezierCurveToNurbs()
        origSel.append(result[0])
        if result:
            mc.rebuildCurve(result, kr=2, kcp=1, fr=1)
        mc.select(origSel, r=1)
        return result
    return inputCurve


def convertBezierToNurbs():
    sel = mc.ls(sl=1, dag=1, typ="bezierCurve")
    for crv in sel:
        oldConnections = mc.listConnections(crv, c=1, p=1, scn=1)
        try:
            mc.disconnectAttr(oldConnections[0], oldConnections[1])
            mc.select(crv, r=1)
            result = mc.bezierCurveToNurbs()
            mc.connectAttr(oldConnections[0], oldConnections[1])
            if result:
                mc.rebuildCurve(result, kr=2, kcp=1, fr=1)
        except Exception as e:
            LOGGER.exception(e)
            LOGGER.info("Curve %s was not converted" % crv)


@undo
def resetSingleGraph(graph, target=None):
    sel = target if target else mc.filterExpand(mc.ls(sl=1, tr=1), sm=9)
    if not sel:
        sel = mc.filterExpand(mc.listRelatives(mc.ls(sl=1, o=1), p=1, pa=1), sm=9)
    if not sel:
        return
    for curve in sel:
        if mc.attributeQuery('Length', n=curve, ex=1) and mc.connectionInfo(curve + '.Length', isSource=1):
            warp = mc.listConnections(curve + '.Length')
            if warp:
                from .. import core
                from .wrap import WIDGETS
                if graph == 'scale' or graph == 'width':
                    core.attributes.resetMultiInst(warp[0], 'scaleCurve')
                    WIDGETS['scaleCurve'].resetGraph()
                if graph == 'twist':
                    core.attributes.resetMultiInst(warp[0], 'twistCurve')
                    WIDGETS['twistCurve'].resetGraph()


def fixBrokenGraphs():
    sel = mc.filterExpand(mc.ls(typ='nurbsCurve'), sm=9)
    for curve in sel:
        if mc.attributeQuery('Length', n=curve, ex=1) and mc.connectionInfo(curve + '.Length', isSource=1):
            warp = mc.listConnections(curve + '.Length')
            if warp:
                from .. import core
                correctScale = None
                correctTwist = None
                if mc.attributeQuery('scaleCurve', n=curve, ex=1) and mc.attributeQuery('scaleCurve', n=warp[0], ex=1):
                    correctScale = mc.getAttr(curve + '.scaleCurve')
                if mc.attributeQuery('twistCurve', n=curve, ex=1) and mc.attributeQuery('twistCurve', n=warp[0], ex=1):
                    correctTwist = mc.getAttr(curve + '.twistCurve')
                if correctScale:
                    core.attributes.resetMultiInst(warp[0], 'scaleCurve')
                    setDouble2Attr(warp[0], 'scaleCurve', fromStringToDouble2(correctScale))
                if correctTwist:
                    core.attributes.resetMultiInst(warp[0], 'twistCurve')
                    setDouble2Attr(warp[0], 'twistCurve', fromStringToDouble2(correctTwist))


@undo
def convertToNewLayerSystem():
    """Converts from the old layer system to the new one"""
    layers = mc.ls(typ='displayLayer')
    from .. import core
    if mc.objExists(core.toggleColor.STORAGE_NODE):
        mc.delete(core.toggleColor.STORAGE_NODE)
    for layer in layers:
        if 'curveGrp_' in layer:
            connection = mc.listConnections(layer + '.identification', s=1, et=1, t='displayLayerManager', p=1)
            if connection:
                connectionOut = mc.listConnections(layer + '.drawInfo', d=1, scn=1, et=1, t='transform', p=1)
                if connectionOut:
                    newNode = mc.createNode('displayLayer')
                    mc.copyAttr(layer, newNode, ic=0, oc=1, v=1, at=['drawInfo'])
                    mc.delete(layer)
                    mc.rename(newNode, layer)


def createNewDisplayLayer(name=None, objects=None):
    # type: (str, list[str]) -> str
    """
    Creates a new display layer independent from Maya display layer system.

    name: The name of the Layer
    objects: The list of objects to add to the Layer

    returns: Name of the new layer node
    """
    newLayer = mc.createNode('displayLayer')
    if name:
        newLayer = mc.rename(newLayer, name)
    if objects:
        mc.editDisplayLayerMembers(name, objects, nr=1)
    return newLayer


def getFormattedLayerNames(collectionID, layerID):
    # type: (int, int) -> tuple[str, str, str]
    """Gets layer names from the current collection id and layer id"""
    id = ''
    if collectionID:
        id = '%s_' % collectionID
    grpCurve = 'curveGrp_%s%s_Curve' % (id, layerID)
    grpGeo = 'curveGrp_%s%s_Geo' % (id, layerID)
    grpInst = 'curveGrp_%s%s_Inst' % (id, layerID)
    return (grpCurve, grpGeo, grpInst)


def getFormattedCollectionByID(id):
    # type: (int) -> str
    """Returns a formatted collection ID, suitable for string concat"""
    collection = ''
    if int(id) > 0:
        collection = '%s_' % id
    return collection


def getCollectionsSet():
    # type: () -> set
    """Returns active collections indexes in a set"""
    allLayers = mc.ls(typ='displayLayer')
    collections = set()
    for layer in allLayers:
        if 'curveGrp_' in layer and ('_Geo' in layer or '_Curve' in layer or '_Inst' in layer):
            c = layer.split('_')
            if len(c) == 4:
                collections.add(c[1])
    return collections


def AOToggle():
    if (mc.getAttr('hardwareRenderingGlobals.ssaoEnable')):
        mc.setAttr('hardwareRenderingGlobals.ssaoEnable', 0)
    else:
        mc.setAttr('hardwareRenderingGlobals.ssaoEnable', 1)


def disableEcho():
    """ Disable Echo All Commands """
    if mc.commandEcho(q=1, st=1) and not mc.optionVar(q='gsEchoAllCommands'):
        mc.commandEcho(st=0)
        LOGGER.info('Echo All Commands function is disabled for performance reasons.')
        LOGGER.info('To disable this functionality, set internalVariable "gsEchoAllCommands" to 1')
        LOGGER.info('Example(MEL): optionVar -iv "gsEchoAllCommands" 1')


def checkNativePlugins(plugInList, myPluginName):
    """Checks if all the required NATIVE maya plugins are loaded"""
    for plugin in plugInList:
        if mc.pluginInfo(plugin, q=1, loaded=1) == 0:
            try:
                mc.loadPlugin(plugin, qt=1)
                LOGGER.info('{0} plug-in was loaded successfully!'.format(plugin))
            except Exception as e:
                message = 'Warning!\n\nMaya native Plug-in "{0}" was not detected and can\'t be activated.\
                    \nYou can\'t use some of the functionality of {1} without {0} plug-in.\
                    \n\nTry to restart Maya and check your Maya installation.\
                    \n\nNOTE: This error can also be triggered if you have maya Plug-in Manager opened. Try to close it and repeat.'\
                    .format(plugin, myPluginName)
                mc.confirmDialog(
                    title='{0} Plug-in Not Detected'.format(plugin),
                    message=message,
                    button=['OK'],
                    defaultButton='OK',
                    cancelButton='OK',
                    dismissString='OK',
                    icn='critical')
                errorMessage = 'Maya "{0}" plug-in can\'t be loaded. Please check if your Maya install is correct.'.format(plugin)
                LOGGER.exception(e)
                MESSAGE.warning(errorMessage)


def loadCustomPlugin(plugin):
    """Checks if all the required CUSTOM maya plugins are loaded"""
    if mc.pluginInfo(plugin, q=1, loaded=1) == 0:
        split = os.path.split(plugin)
        try:
            mc.loadPlugin(plugin, qt=1)
            LOGGER.info("{0} plug-in was loaded successfully!".format(split[-1]))
            return True
        except BaseException:
            return False
    else:
        return True


def userSetup():
    """ Rewrite userSetup file """
    fileName = mc.internalVar(usd=1) + 'userSetup.mel'
    if os.path.exists(fileName):
        fileID = open(fileName, 'r')
        allLines = fileID.readlines()
        fileID.close()
        newList = list()
        lineDetected = 0
        # Remove old code if any exist
        for i in range(len(allLines)):
            if 'gs_curvetools' not in allLines[i]:
                newList.append(allLines[i])
            else:
                lineDetected = 1
        # Write to userSetup if needed
        if lineDetected == 1:
            LOGGER.info('userSetup.mel was modified successfully!')
            newFileID = open(fileName, 'w')
            newFileID.writelines(newList)
            newFileID.close()


def getDPI():
    return mc.mayaDpiSetting(q=1, sd=1)


def openDocs():
    """ Open User Documentation """
    if OS == "mac":
        os.system('open https://gs-curvetools.readthedocs.io/')
        return 1
    os.system('start https://gs-curvetools.readthedocs.io/')


def openLink(link):
    """ Open User Documentation """
    if OS == "mac":
        os.system('open %s' % link)
        return 1
    os.system('start %s' % link)
