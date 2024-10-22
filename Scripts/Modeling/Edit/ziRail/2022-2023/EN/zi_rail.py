#                      __                  __
# ___  __ ____________/  |_  ____ ___  ___/  |_ __ _________  ____
# \  \/ _/ __ \_  __ \   ___/ __ \\  \/  \   __|  |  \_  __ _/ __ \
#  \   /\  ___/|  | \/|  | \  ___/ >    < |  | |  |  /|  | \\  ___/
#   \_/  \___  |__|   |__|  \___  /__/\_ \|__| |____/ |__|   \___  >
#            \/                 \/      \/                       \/
#
#
#
#                FILE
# Associated with ziRail_<version>.mll
#
#               AUTHOR
# (contact@vertexture.org)
# www.vertexture.org
# Please read on the website terms of use and licensing.
# Tutorials can be found also
#
#                DATE
#            01/05/2020 (created)
#
#             DESCRIPTION
# Retopo tool
#
#                             _               _  __
#                     ____   (_)_____ ____ _ (_)/ /
#                    /_  /  / // ___// __ `// // /
#                     / /_ / // /   / /_/ // // /
#                    /___//_//_/    \__,_//_//_/(The rail)
#
#
#                      .:~~~~^^^:..
#                     .~7?JY55PGBBGGGPYJ7~.
#                  .^!????JY5GBB#&&&&&&&&&B57.
#                 :~!777!!?JY5PG###&&&&&&&&&#P!
#               ..^~:^~!!~~J5PPPGGB##&@@@##&&##5^
#              .:..^^:^^^^:^PGGGP5J7~!?PBB5PG5J??!.
#             .... .. .....:YGP7:      ^7?P5?~   .:.
#            . .:.      .. :77:         ~77YPJ^    ..
#              ..:.....    ^7~          ^7777: .....~:
#              ...::::::..^~JP7:.....^7JPPY!.   ~JJ7??.
#              ...::::.::.~?7J5GBG5YP5?JB#Y^    ^BB?YYY!.
#                  .:~^:..~7!~JGBYG&#BYJYBB7.  :.5BPBB#B~
#                ... .::.      ^7Y?JPB##BGBBPJ?JJP#B&GJJ~
#                                :: .:!YP5YJPGPY5PYP5?:
#                   ..                 :!!!:~5JJ7B5GB5Y~
#                .::.                    .:~.!5?:~~:!~~5^
#             .. .^:.                   ....  ^        :^
#                  ..   .^:.    .                   ..
#                 ..::: .:^~^:. .                 . ..
#                 . .:^:^~  :~^ :.           ...^~7~^7:
#                     ..     :!^:7^.    ..:^:~!:7~!^~!~
#                         ..  .^.:J?!:..   .  :   .  .J7
#                         .^. :^. :JPYJJ77~^: :^^!!^~!JY^
#                          .:^!^...:75GBGPP5Y7~?Y5555YJY?.
#                           :^^.  ..:!JYPYJ!7Y5GBB5YPBPJ!.
#                                      .^~~~~~~!J5J~^!^.
#
# pylint: disable=relative-import
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=superfluous-parens
# pylint: disable=line-too-long
# pylint: disable=deprecated-lambda
# pylint: disable=missing-docstring
# pylint: disable=empty-docstring
# pylint: disable=bad-continuation
# pylint: disable=no-self-use
# //////////////////////////////////////////////////////////////////////////*/
import re
import sys

import zi_UI.ziRessources_rc
import zi_Widget.zi_Windows
import zi_UI.zi_RailUI

import zi_wireframe

import maya.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel

from PySide2 import QtWidgets, QtCore, QtGui

from pdb import set_trace as db


HELPSTR = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"> <html><head><meta name="qrichtext" content="1" /><style type="text/css"> p, li { white-space: pre-wrap; } </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;"> <p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;"><br /></p> <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">\n</p> <p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/vertexture/skin/vertexture/logoHs_color.png" /></p> <p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; color:#7e835a;">ziRail </span>creates patch polygons along your strokes. These strokes are drawn directly on a mesh. By doing so, creating polygons become intuitiv. This can be used as a companion tool for retopology tasks. </p> <p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">For more informations and video tutorials, please visit https://vertexture.org</p> <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;"><br /></p> <p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; font-style:italic;">Please support us and rate this tool on gumroad</span></p> <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;"><br /></p></body></html>

"""

PLUGERROR = """
Cannot load plugin {} please make sure the *.mll file is in the correct folder or the license is valid, tutorial videos can be found at www.vertexture.org
"""

__version__ = 0.955
__tool__ = "ziRail"
__author__ = "VERTEXTURE"


NAMEPLUGS = ["ziRail", "ziWireframeViewport"]
ATTRSNAP = "zisnap"
SETNAME = "ziSet"
VERBOSE = False


class Options(object):

    attrMT = 'zi_mergThreshold'
    attrD = 'zi_distancesnap'
    attrDep = 'ziCutDp'
    attrU = 'zi_uspan'
    attrV = 'zi_vspan'
    attrB = 'zi_bdiv'

    attrLayzDis = 'zi_lazyDistance'
    attrLayzIt = 'zi_lazyStrength'
    attrLayzAct = 'zi_lazyActive'

    attrInt = 'zi_railIntens'
    attrRad = 'zi_railRadius'
    attrFrz = 'zi_railFreeze'
    attrTwR = 'zi_railTweakR'

    attrBackf = 'zi_railBackFace'
    attrHints = "zi_railHints"
    attrHelp = "zi_railHelp"

    def __init__(self):
        self._source = None
        self._numjob = int()
        self.sourceShape = ""

        # -- Has to be lower than 1000 to display the helpers correctly
        if self.getAttribute(self.attrDep, 990) > 1000:
            cmds.optionVar(fv=[self.attrDep, 990])
            cmds.warning("Depth Priory was higher than 1000")

    def getAttribute(self, attr, default):

        if cmds.optionVar(exists=attr):
            return cmds.optionVar(q=attr)

        return default

    def clearAttrs(self):

        list(map(lambda x: cmds.optionVar(remove=x), [self.attrMT,
                                                      self.attrD,
                                                      self.attrU,
                                                      self.attrV,
                                                      self.attrB,
                                                      self.attrInt,
                                                      self.attrRad,
                                                      self.attrFrz,
                                                      self.attrTwR,
                                                      self.attrBackf,
                                                      self.attrLayzAct,
                                                      self.attrLayzIt,
                                                      self.attrLayzDis,
                                                      self.attrHelp,
                                                      self.attrHints,
                                                      ]))

    # -- -- -- -- -- -- -- -- -- -- GETTER

    @property
    def numjob(self):
        return self._numjob

    @property
    def source(self):
        return self._source

    @property
    def mergeThreshold(self):
        return self.getAttribute(self.attrMT, 0.001)

    @property
    def distance(self):
        return self.getAttribute(self.attrD, 2.0)

    @property
    def u(self):
        return int(self.getAttribute(self.attrU, 5))

    @property
    def v(self):
        return int(self.getAttribute(self.attrV, 5))

    @property
    def bdiv(self):
        return self.getAttribute(self.attrB, 1)

    @property
    def intensity(self):
        return self.getAttribute(self.attrInt, 50)

    @property
    def radius(self):
        return self.getAttribute(self.attrRad, 50)

    @property
    def freeze(self):
        return self.getAttribute(self.attrFrz, 1)

    @property
    def tweakR(self):
        return self.getAttribute(self.attrTwR, 50)

    @property
    def lazyStrength(self):
        return self.getAttribute(self.attrLayzIt, 2)

    @property
    def lazyDistance(self):
        return self.getAttribute(self.attrLayzDis, 5)

    @property
    def lazyActive(self):
        return self.getAttribute(self.attrLayzAct, 0)

    @property
    def backfaceBrush(self):
        return self.getAttribute(self.attrBackf, 1)

    @property
    def helpDisplay(self):
        return bool(self.getAttribute(self.attrHelp, 1))

    @property
    def hints(self):
        return bool(self.getAttribute(self.attrHints, 0))

    # -- -- -- -- -- -- -- -- -- -- SETTER

    @helpDisplay.setter
    def helpDisplay(self, value):
        cmds.optionVar(iv=[self.attrHelp, value])

    @source.setter
    def sourceShape(self, shape):
        self._source = shape

    @hints.setter
    def hints(self, value):
        cmds.optionVar(iv=[self.attrHints, int(value)])

    @v.setter
    def v(self, value):
        cmds.optionVar(iv=[self.attrV, int(value)])

    @u.setter
    def u(self, value):
        cmds.optionVar(iv=[self.attrU, int(value)])

    @bdiv.setter
    def bdiv(self, value):
        cmds.optionVar(iv=[self.attrB, value])

    @mergeThreshold.setter
    def mergeThreshold(self, value):
        cmds.optionVar(fv=[self.attrMT, value])

    @distance.setter
    def distance(self, value):
        cmds.optionVar(fv=[self.attrD, value])

    @numjob.setter
    def numjob(self, value):
        self._numjob = value

    @intensity.setter
    def intensity(self, value):
        cmds.optionVar(fv=[self.attrInt, value])

    @radius.setter
    def radius(self, value):
        cmds.optionVar(fv=[self.attrRad, value])

    @freeze.setter
    def freeze(self, value):
        cmds.optionVar(iv=[self.attrFrz, value])

    @tweakR.setter
    def tweakR(self, value):
        cmds.optionVar(iv=[self.attrTwR, value])

    @lazyStrength.setter
    def lazyStrength(self, value):
        cmds.optionVar(iv=[self.attrLayzIt, value])

    @lazyDistance.setter
    def lazyDistance(self, value):
        cmds.optionVar(iv=[self.attrLayzDis, value])

    @lazyActive.setter
    def lazyActive(self, value):
        cmds.optionVar(iv=[self.attrLayzAct, value])

    @backfaceBrush.setter
    def backfaceBrush(self, value):
        cmds.optionVar(iv=[self.attrBackf, value])


class Mesh(object):

    def __init__(self, selection=None):
        self.name = selection

    def frozen(self, win):
        """Ensure the mesh has no connection to its transform
        and they are frozen

        :Param win(QDialog): the modal win
        """
        if not cmds.objExists(self.name):
            return

        for trans in ["t", "r"]:
            for axe in ["x", "y", "z"]:

                attr = "%s.%s%s" % (self.name, trans, axe)
                src = cmds.connectionInfo(attr, sourceFromDestination=True)

                if src:
                    cmds.disconnectAttr(src, attr)

                cmds.setAttr(attr, lock=False)

        cmds.makeIdentity(self.name, apply=True, t=1, r=1, s=1, n=0, pn=1)
        win.close()

    def shape(self):
        """
        """
        shapes = cmds.listRelatives(self.name, shapes=True, type='mesh')
        return shapes[0] if shapes else None

    @staticmethod
    def isFreezed(transform):

        if not cmds.getAttr("%s.translate" % transform[0])[0] == (0, 0, 0):
            return False

        if not cmds.getAttr("%s.rotate" % transform[0])[0] == (0, 0, 0):
            return False

        if not cmds.getAttr("%s.scale" % transform[0])[0] == (1, 1, 1):
            return False

        return True

    @staticmethod
    def node(shape, obj):
        """Ensure the zirail and selection network got created

        :Param shape: shape selection
        :Type shape: str()

        :Param obj: the main instanced object
        :Type obj: object()

        """
        if not shape:
            cmds.error("please set the sourceMesh")

        if not cmds.objExists(shape):
            cmds.error("%s does not exists, please set the sourceMesh" % shape)

        nodes = cmds.ls(typ=__tool__)

        for node in nodes:
            if cmds.isConnected("%s.outMesh" % shape, "%s.ziRailMesh" % node):
                return node

        if nodes and shape:
            obj.connect(shape, 'outMesh', nodes[0], 'ziRailMesh')
            return nodes[0]

        obj.createStream()
        return Mesh.node(shape, obj)


class Win(zi_Widget.zi_Windows.Frameless,
          QtCore.QObject,
          zi_UI.zi_RailUI.Ui_ziRailWindow):

    def __init__(self, debug=False, dockable=True, internet=True):
        super(Win, self).__init__()

        self.internet = internet
        self.dockable = dockable
        self.startPos = None
        self.tips = []
        self.ctx = ""

        self.setupUi(self)
        self.opt = Options()
        self.hk = Hotkeys(self)

        self.setConnections()
        self.setIcons()
        self.setWin()

        self.setBackConnections()
        self.debuginstallation(debug)
        self.loadPlugin()

        self.show()


    def setWin(self):
        """Set misc preference for the QMainWindow and QWidgets
        """
        self.addBar(HELPSTR, NAMEPLUGS[0], False,
                    "https://vertexture.org/?source=mayapp")

        self.logo.setPixmap(
            self.logo.pixmap().scaledToWidth(
                90, QtCore.Qt.SmoothTransformation))

        self.hudChk.setChecked(True)

        self.opt.mergeThreshold = 0.001  # -- obsolete value
        cmds.optionVar(iv=["ziCutUpdate", 1])  # -- force refresh

        self.lazySpinStrength.setValue(self.opt.lazyStrength)
        self.lazySpinDist.setValue(self.opt.lazyDistance)
        self.backfBtn.setChecked(self.opt.helpDisplay)
        self.distanceSpin.setValue(self.opt.distance)
        self.lazyBtn.setChecked(self.opt.lazyActive)
        self.freezeBtn.setChecked(self.opt.freeze)
        self.bridgeSpin.setValue(self.opt.bdiv)

        self.forceSlid.setValue(self.opt.intensity)
        self.tweakRadSlid.setValue(self.opt.tweakR)
        self.radiusSlid.setValue(self.opt.radius)

        self.Uspin.setValue(self.opt.u)
        self.Vspin.setValue(self.opt.v)

        self.butTheme.clicked.emit()

        # ------------- set ColorButton widgets
        self.wirefr = zi_wireframe.Win(False)
        optvars = zi_wireframe.OptVar()
        self.wirefr.close()

        self.backColor = self.wirefr.createColor("BackFace")
        self.surfColor = self.wirefr.createColor("Surface")
        self.pointColor = self.wirefr.createColor("Point")
        self.lineColor = self.wirefr.createColor("Line")

        QtWidgets.QPushButton()

        prms = ["Surface Color",
                "Point Color",
                "Line Color",
                "Backface Color"]

        self.colorButtons = [
            self.surfColor,
            self.pointColor,
            self.lineColor,
            self.backColor]

        for btn, param in zip(self.colorButtons, prms):

            btn.setMinimumHeight(22)
            btn.setMaximumWidth(999)
            btn.setMaximumHeight(25)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                              QtWidgets.QSizePolicy.Expanding)

            btn.setTxt(param.split(" ")[0], 50)
            btn.setObjectName(param)

            if btn == self.colorButtons[0]:
                self.colorLayoutTop.addWidget(btn)
                self.wirefr.setColor(btn, optvars.surfColor)
                btn.clicked.connect(lambda: self.defineColor(self.surfColor))

            if btn == self.colorButtons[1]:
                self.colorLayoutBot.addWidget(btn)
                self.wirefr.setColor(btn, optvars.pointColor)
                btn.clicked.connect(lambda: self.defineColor(self.pointColor))

            if btn == self.colorButtons[2]:
                self.colorLayoutBot.addWidget(btn)
                self.wirefr.setColor(btn, optvars.lineColor)
                btn.clicked.connect(lambda: self.defineColor(self.lineColor))

            if btn == self.colorButtons[3]:
                self.colorLayoutTop.addWidget(btn)
                self.wirefr.setColor(btn, optvars.backfColor)
                btn.clicked.connect(lambda: self.defineColor(self.backColor))

        if self.dockable:

            # The Maya dock function can be tricky for unknown reason so far.
            # If such thing happens, It will fail silently.
            try:
                self.setDock(obj=self,
                             title="{} {}(beta)".format(__name__, __version__),
                             name="zirailDock",
                             allowed=["left", "right"],
                             floated=True)

            except:
                cmds.warning("failure, setting dockable feature")
                pass

        self.restoreGeo()
        self.setMargins()

        self.movable = False

        self.tweakBtn.setVisible(False)
        self.freezeBBtn.setVisible(False)

        if not self.opt.helpDisplay:
            self.installTips()
        else:
            self.helpBtn.setChecked(True)

        if self.opt.hints:
            self.hintsBtn.setChecked(True)
            self.setHints()
        else:
            self.hintsBtn.setChecked(False)

    def setMargins(self, margevalue= 10):

        geo = self.geometry()

        if geo.x() < margevalue :
            geo.setX(margevalue)

        if geo.y() < margevalue :
            geo.setY(margevalue)

        self.setGeometry(geo)

    def checkupdate(self):
        """Set the output as a global variable so it loads faster the next time
        to request a html can be slow

        :Return (str): the versionning
        """
        updt = "No update available"

        python3 = True if sys.version_info[0] >= 3 else False

        if python3:
            from urllib import request as urlreq
        else:
            import urllib as urlreq

        try:
            req = urlreq.urlopen(r"https://vertexture.gumroad.com/l/zirail")

        except Exception as e:
            self.updateChk.setText("Error checking update")

            return

        if req:

            page = req.read()

            if python3:
                page = page.decode("utf-8")

            res = re.search(r"Package content\ v(\d.\d+)", page)

            if res:

                if __version__ < float(res.groups()[0]):
                    updt = "A new version is available = %s" % res.groups()[0]

        self.updateChk.setText(updt)
        self.console(updt)

    def event(self, event):
        """clean up to default state while closing the main UI
        """
        if event.type() == QtCore.QEvent.Type.Hide:

            cmds.makeLive(none=True)
            self.clearStateIdle()
            event.accept()

        return False

    def clearAllGeoAttributes(self):

        for trans in cmds.ls(typ="transform"):

            shape = Mesh(trans).shape()

            if not shape:
                continue

            if cmds.objExists("%s.%s" % (shape, ATTRSNAP)):
                self.wirefr.clearGeoAttributes(trans)
                cmds.deleteAttr(shape, at=ATTRSNAP)

    def refresh(self):
        self.refreshColors()

    def slidValue(self, widget):

        if widget == self.forceSlid:
            self.opt.intensity = widget.value()

        if widget == self.tweakRadSlid:
            self.opt.tweakR = widget.value()

        if widget == self.radiusSlid:
            self.opt.radius = widget.value()

        if widget:
            self.console(widget.value())

    def refreshColors(self):
        self.wirefr.setColor(self.surfColor, self.wirefr.var.surfColor)
        self.wirefr.setColor(self.pointColor, self.wirefr.var.pointColor)
        self.wirefr.setColor(self.lineColor, self.wirefr.var.lineColor)

    def defineColor(self, wid):
        colors = self.wirefr.getColor(wid)
        self.wirefr.setColor(wid, colors)

        name = wid.objectName()

        for i in list(range(3)):
            cmds.optionVar(fv=(zi_wireframe.kColors[name][i], colors[i]))

        cmds.refresh(cv=True, f=True)

    def setBackConnections(self):
        """Check if a ziRail connection already exist to set the source mesh
        """
        node = cmds.ls(typ=__tool__)

        if node:

            meshes = cmds.listConnections('%s.ziRailMesh' % node[0])

            if meshes:
                # -- saving the current selection
                prevSelection = cmds.ls(sl=True)

                cmds.select(meshes[0], replace=True)
                self.pickSrcBtn.clicked.emit()
                self.restoreReferenceState()

                cmds.select(prevSelection, replace=True)

    def setIcons(self):
        """Set QPushButton::QIcon images for UI.
        """
        self.viewportBtn.setIcon(QtGui.QIcon(":render_layeredShader.png"))
        self.ziRailLaunchBtn.setIcon(QtGui.QIcon(":birail1Gen.png"))

    def sDelta(self, token):
        """Triggered function when brush hotkeys pressed

        :Param token(str): what brush to trigger
        :Return (None): desc.
        """
        if cmds.contextInfo(self.ctx, exists=True):

            if token == "brushRelaxRadius":
                self.interactiveBrush("brushRelaxRadius")

            if token == "brushRelaxIntens":
                self.interactiveBrush("brushRelaxIntens")

            if token == "brushMoveRadius":
                self.interactiveBrush("brushMoveRadius")

    def setConnections(self):
        """Set QSignals and QSlots for QWidgets
        """
        self.reversBridgBtn.clicked.connect(self.reverseBridge)
        self.pinchSlid.valueChanged.connect(self.setPinch)
        self.slidBtn.clicked.connect(self.resetPinch)

        self.pickSrcBtn.clicked.connect(self.pickSource)

        self.upUBtn.clicked.connect(lambda: self.spansArrow(self.Uspin, 1))
        self.dnUBtn.clicked.connect(lambda: self.spansArrow(self.Uspin, -1))
        self.upVBtn.clicked.connect(lambda: self.spansArrow(self.Vspin, 1))
        self.dnVBtn.clicked.connect(lambda: self.spansArrow(self.Vspin, -1))

        self.lazySpinStrength.valueChanged.connect(self.changeLazyStrength)
        self.lazySpinDist.valueChanged.connect(self.changeLazyDistance)
        self.projSlid.valueChanged.connect(self.changeDistanceSlider)

        self.displayProjBtn.clicked.connect(self.displayProjection)

        self.distanceSpin.valueChanged.connect(self.changeDistance)
        self.bridgeSpin.valueChanged.connect(self.changeBridge)

        self.shaderApplyBtn.clicked.connect(self.applyViewport)
        self.tweakRadSlid.valueChanged.connect(self.setTweakR)
        self.refBox.stateChanged.connect(self.referenceState)
        self.closeStrokeBtn.clicked.connect(self.closeStroke)
        self.viewportBtn.clicked.connect(self.setViewport)

        self.Uspin.valueChanged.connect(lambda: self.spansChanged(self.Uspin))
        self.Vspin.valueChanged.connect(lambda: self.spansChanged(self.Vspin))

        self.freezeBtn.clicked.connect(self.setFreezeBorder)
        self.lazyBtn.clicked.connect(self.changeLazyActive)

        self.relaxBrBtn.clicked.connect(self.relaxBrush)
        self.moveBtn.clicked.connect(self.setMoveBrush)

        self.tweakBtn.clicked.connect(self.tweakMode)
        self.backfBtn.clicked.connect(self.setBackface)
        self.hudChk.stateChanged.connect(self.hudState)

        self.freezeSymBtn.clicked.connect(self.setFreezeMedian)
        self.ziRailLaunchBtn.clicked.connect(self.launching)
        self.symmetryBtn.clicked.connect(self.setSymmetry)

        self.hotkeyBtn.clicked.connect(self.displayHotkeys)
        self.quadBtn.clicked.connect(self.toggleQuadMode)
        self.updateChk.clicked.connect(self.checkupdate)

        self.lockedPinchChk.stateChanged.connect(self.enablePinch)

        list(map(lambda x: x.sliderReleased.connect(lambda: self.slidValue(x)),
                 [self.forceSlid,
                  self.tweakRadSlid,
                  self.radiusSlid]))

        list(map(lambda x: x.clicked.connect(self.setFigure),
                 [self.strokeBtn,
                  self.lineBtn,
                  self.squareBtn,
                  self.circleBtn]))

        self.helpBtn.clicked.connect(self.setTips)
        self.hintsBtn.clicked.connect(self.setHints)

    def setHints(self):
        """Description
        """
        self.opt.hints = self.hintsBtn.isChecked()

        status = "ON"

        # -- OFF
        if self.hintsBtn.isChecked():
            self.hk.deleteTextShortcuts()
            self.hk.unset()

            self.hintsBtn.setText("Enable Hotkeys")
            status = "OFF"


        # -- ON
        else:
            self.hk.reload()
            self.hk.setSequences()
            self.hintsBtn.setText("Disable Hotkeys")


        self.console("hotkeys set to %s" % status)

    def setFreezeMedian(self):
        """Description
        """
        node = self.ziRailNode()

        if not node or not cmds.contextInfo(self.ctx, exists=True):
            return

        value = self.freezeSymBtn.isChecked()
        cmds.ziRailContext(self.ctx, e=True, freezeMedian=value)

        self.console(toStr(value))

    def setSymmetry(self):
        """
        """
        node = self.ziRailNode()
        shape = self.getShape()

        outAttr = "zisymOut"
        inAttr = "zisymIn"

        value = self.symmetryBtn.isChecked()

        # -- failure, deactivate the symmetry
        if not node or not shape:
            self.symmetryBtn.setChecked(False)

            if node:
                cmds.setAttr("%s.symmetry" % node, 0)

            cmds.warning("No mesh selected")
            return

        # -- activate symmetry
        if value:

            cmds.setAttr("%s.symmetry" % node, 1)

            if not cmds.objExists("%s.%s" % (shape, outAttr)):
                cmds.addAttr(shape, longName=outAttr)

            conns = cmds.listConnections("%s.%s" % (shape, outAttr))

            # -- create the instance
            if not conns:
                instances = cmds.instance(shape,
                                          lf=True,
                                          n="%s_sym" % self.getSelZiMesh())

                cmds.scale(-1, 1, 1, instances[0], r=True)

                cmds.addAttr(instances[0], longName=inAttr)
                self.connect(shape, outAttr, instances[0], inAttr)

                setnodes = self.ziSetNode()

                if not setnodes:
                    setnodes = [cmds.createNode("objectSet", n="ziSetSym")]
                    cmds.addAttr(setnodes[0], longName="zisetsym")
                    cmds.addAttr(setnodes[0], longName="zisetnode")

                cmds.sets(instances[0], edit=True, forceElement=setnodes[0])

        # -- deactivate and kill the instances
        if not value:
            cmds.setAttr("%s.symmetry" % node, 0)
            shape = self.getShape()
            instances = cmds.listConnections("%s.%s" % (shape, outAttr))
            cmds.delete(self.ziSetNode())

            if instances:
                cmds.delete(instances)

        self.console(toStr(value))
        cmds.select(shape, replace=True)

    def clearStateIdle(self):
        """Get rid off the override display
        """

        cmd = "setRendererInModelPanel $gViewport2 {}"

        # -- restore viewport 2.0
        for panel in cmds.getPanel(type='modelPanel'):
            mel.eval(cmd.format(panel))

        # -- remove the reference mode
        if self.opt.sourceShape:
            if cmds.objExists(self.opt.sourceShape):
                self.setAsReference(self.opt.sourceShape, 0)

        # -- clear the ziWireframe attributes
        self.clearAllGeoAttributes()

        if cmds.objExists(SETNAME):
            cmds.delete(SETNAME)

    def clearReferenceState(self, mesh):
        """If already a mesh make sure we restore its state
        """
        if not mesh:
            return

        if cmds.objExists(mesh):
            self.refBox.setChecked(False)

    def spansArrow(self, wid, incr):
        """Called function for changing spans u or v direction
        :Param wid: the sender widget
        :Type wid: function obj

        :Param incr: the increment value to set
        :Type incr: int()
        """
        incrementedValue = wid.value() + incr
        wid.setValue(incrementedValue)
        wid.editingFinished.emit()

        if wid == self.Uspin:
            self.opt.u = incrementedValue

        if wid == self.Vspin:
            self.opt.v = incrementedValue

        self.console(self.opt.u, self.opt.v)

    def changeLazyStrength(self):
        self.opt.lazyStrength = int(self.lazySpinStrength.value())
        self.console(self.opt.lazyStrength)

    def changeThreshold(self):
        self.opt.mergeThreshold = float(self.mergeTSpin.value())
        self.console(toStr(self.opt.mergeThreshold))

    def changeLazyDistance(self):
        self.opt.lazyDistance = int(self.lazySpinDist.value())
        self.console(self.opt.lazyDistance)

    def changeDistanceSlider(self):
        if not self.displayProjBtn.isChecked():
            self.displayProjBtn.setChecked(True)

        value = float(self.projSlid.value() / 10.0)
        self.distanceSpin.setValue(value)
        self.changeDistance()

        self.console(value)

    def changeDistance(self):
        self.opt.distance = float(self.distanceSpin.value())
        self.displayProjection()

        self.console(self.opt.distance)

    def changeLazyActive(self):
        self.opt.lazyActive = int(self.lazyBtn.isChecked())
        self.console(toStr(self.opt.lazyActive))

    def setTweakR(self):
        self.opt.tweakR = self.tweakRadSlid.value()
        self.console(self.opt.tweakR)

    def setHelpAttr(self):
        self.opt.helpDisplay = int(self.helpBtn.isChecked())

    def spansChanged(self, senderwidget):
        """Change the u or v spans sudbdivisions of the last created patch
        """

        if senderwidget == self.Uspin:
            self.opt.u = self.Uspin.value()

        if senderwidget == self.Vspin:
            self.opt.v = self.Vspin.value()

        if not self.ctx:
            return

        if self.ziRailNode():
            cmds.ziRailCmd(u=int(self.Uspin.value()),
                           v=int(self.Vspin.value()))

        self.console(self.opt.u, self.opt.v)

    def hudState(self, state):
        """Can be used also for the brush display with the input equal 2
        OpenMaya used so the undo stack is not feed
        """
        node = self.ziRailNode()

        if not node:
            return

        mobj = om.MObject()
        sel = om.MSelectionList()
        sel.add(node)
        sel.getDependNode(0, mobj)

        mfndep = om.MFnDependencyNode(mobj)
        mplug = mfndep.findPlug("displayInfo", False)

        if not mplug.isNull():
            mplug.setShort(state)

        self.console(toStr(state))

    def referenceState(self, state):

        if not cmds.objExists(self.opt.sourceShape):
            cmds.warning("%s does not exists" % self.opt.sourceShape)
            return

        if not self.opt.sourceShape:
            cmds.warning("Please set a source mesh first")
            return

        self.setAsReference(self.opt.sourceShape, state)

    def setAsReference(self, shape, state):
        """Description

        :Param bmesh(str): the source mesh shape
        :Return (None): desc.
        """
        if not cmds.objExists(shape):
            return

        # 2 will activate, otherwise deactive
        overridevalue = True if state == 2 else False

        self.setAttribute(shape, "overrideEnabled", overridevalue)
        self.setAttribute(shape, "overrideDisplayType", state)

        self.console("%s %s" % (shape, toStr(state)))

    def setShading(self, shape, state):
        """set appropriate shading for ziwireframe

        :Param shape(None): desc.
        :Param state(bool): True activate, False deactivate
        :Return (None): desc.
        """
        backfacevalue = 3 if state is True else 0

        self.setAttribute(shape, "backfaceCulling", backfacevalue)
        self.setAttribute(shape, "overrideEnabled", state)
        self.setAttribute(shape, "overrideShading", not state)

    def setAttribute(self, obj, attr, value):

        if not cmds.objExists(obj):
            return

        if not cmds.getAttr("{}.{}".format(obj, attr), lock=True):
            cmds.setAttr('{}.{}'.format(obj, attr), value)

    def restoreReferenceState(self):

        if cmds.objExists(self.opt.sourceShape):

            state = cmds.getAttr('%s.overrideDisplayType' %
                                 self.opt.sourceShape)
            stateStatus = True if state == 2 else False

            self.refBox.setChecked(stateStatus)

    def getShapeSelection(self):
        """Query the current selection
        """
        for sel in cmds.ls(hilite=True) + cmds.ls(sl=True, o=True) or []:

            if cmds.nodeType(sel) == "mesh":
                return sel

            if cmds.nodeType(sel) == "transform":
                shapes = cmds.listRelatives(sel, shapes=True)

                if shapes:
                    if cmds.nodeType(shapes[0]) == "mesh":
                        return shapes[0]

        return None

    def applyViewport(self):
        """Set the Vertexture viewport
        """
        shape = self.getShapeSelection()

        if not shape:
            return

        panels = cmds.getPanel(type="modelPanel")
        for panel in panels or []:

            # -- activate vertexture render
            if self.shaderApplyBtn.isChecked():

                cmd = "setRendererAndOverrideInModelPanel $gViewport2 %s %s"
                mel.eval(cmd % ("VertextureViewport", panel))

                self.setStamp(shape)
                self.setShading(shape, True)

                self.console(panel, "vertextureViewport")

            # -- recover default state
            if not self.shaderApplyBtn.isChecked():

                # -- activate viewport 2.0
                cmd = "setRendererInModelPanel $gViewport2 %s"
                mel.eval(cmd % (panel))
                self.clearAllGeoAttributes()

                self.console(panel, "viewport 2.0")

    def setStamp(self, shape):

        if not cmds.objExists("%s.%s" % (shape, ATTRSNAP)):
            cmds.addAttr(shape, ln=ATTRSNAP, dataType="string")

    def setViewport(self):
        """Open the viewport UI
        :return : the QMainWindow object
        """
        self.loadPlugin()

        wireframewin = zi_wireframe.main()

        if self.butTheme.isChecked():
            wireframewin.setStyleSheet(zi_Widget.zi_Windows._style)
            wireframewin.setStyle(self.factory)

        wireframewin.show()

    def closeStroke(self):
        cmds.ziRailCmd(close=True)
        cmds.makeLive(none=True)
        self.console()

    def tweakMode(self):
        """
        """
        self.relaxBrBtn.setChecked(False)

        if self.tweakBtn.isChecked():
            shape = self.getShape()

            # -- no selection then skipp
            if not shape:
                return

            # -- if tweaknode not created yet, create a new one
            node = self.ziTweakNode()
            if not node:
                node = [cmds.createNode("ziTweakNode", ss=True)]

            # -- make the connections of tweak node
            self.attachTweakNode(shape, node[0])

            # -- switch to component mode and move tool

            mel.eval("""setSelectMode components Components;\
                selectType -smp 1 -sme 0 -smf 0 -smu 0 -pv 1\
                 -pe 0 -pf 0 -puv 0; HideManipulators;\
                  setToolTo $gMove """)

        if not self.tweakBtn.isChecked():
            self.detachTweakNode()

    def tweakFunc(self, geoA, geoB):
        """Description

        :Param geoA: the tweakable geo
        :Type geoA: str()

        :Param geoB: the geo where the tweakable geo got snapped
        :Type geoB: str()

        """
        attribute = "%s.%s" % (geoA, ATTRSNAP)
        res = cmds.getAttr(attribute)

        if not res or not cmds.objExists(attribute):
            self.tweakBtn.setChecked(False)

        cmds.ziTweakCmd(tm=geoB)

    def relaxFreezeBrush(self):
        """Freeze border SLOT
        """
        self.relaxBrBtn.setChecked(True)
        self.relaxBrush()

    def setMoveBrush(self):
        """
        """
        self.setContext()

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, moveBrush=1)

        self.ziRailLaunchBtn.setChecked(False)
        self.console()

    def completion(self):

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, complete=True)

    def interactiveBrush(self, flag):
        """
        """
        winMaya = zi_Widget.zi_Windows.getMayaWin()
        scrub = zi_Widget.zi_Windows.ziScrub(winMaya)
        curPos = winMaya.mapFromGlobal(QtGui.QCursor.pos())

        scrub.changed.connect(lambda x: self.changeScrub(x, flag))
        scrub.released.connect(lambda: self.closeScrub(scrub))
        scrub.leave.connect(lambda: self.closeScrub(scrub))

        scrub.ephemere = True
        maxValue = 100

        if flag == "brushRelaxRadius":

            scrubText = "Relax Radius"

            scrubvalue = self.radiusSlid.value()
            scrubGeo = scrubvalue * 2.0

            self.opt.radius = scrubvalue

            self.hudState(2)

        if flag == "brushRelaxIntens":

            scrubText = "Relax Intensity"

            scrubvalue = self.forceSlid.value()
            scrubGeo = scrubvalue * 2.0

            self.hudState(3)

        if flag == "brushMoveRadius":

            maxValue = 200
            scrubText = "Move Radius"

            scrubvalue = self.tweakRadSlid.value()
            scrubGeo = self.tweakRadSlid.value()

            self.hudState(4)

        scrub.setGeometry(curPos.x() - scrubGeo, curPos.y() - 10, 200, 20)
        scrub.set_behaviors(scrubText, maxValue, 0.1, scrubvalue)

        scrub.show()
        scrub.on = True

    def changeScrub(self, value, brushtype):
        """Description

        :Param value(None): desc.

        :Param brushtype(None): desc.
        :Return (None): desc.
        """
        if cmds.contextInfo(self.ctx, exists=True):

            if brushtype == "brushRelaxRadius":
                cmds.ziRailContext(self.ctx, e=1, rri=value)

            if brushtype == "brushRelaxIntens":
                cmds.ziRailContext(self.ctx, e=1, iri=value)

            if brushtype == "brushMoveRadius":
                cmds.ziRailContext(self.ctx, e=1, rmi=value)

    def closeScrub(self, scrub):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        widget = None
        node = self.ziRailNode()

        brush = cmds.getAttr("%s.displayInfo" % node)

        if brush == 2:
            value = cmds.getAttr("%s.radiusRelaxInteractive" % node)
            widget = self.radiusSlid
            self.radiusSlid.setValue(value)

        if brush == 3:
            value = cmds.getAttr("%s.intensityRelaxInteractive" % node)
            widget = self.forceSlid
            self.forceSlid.setValue(value)

        if brush == 4:
            value = cmds.getAttr("%s.radiusMoveInteractive" % node)
            widget = self.tweakRadSlid
            self.tweakRadSlid.setValue(value)

        self.slidValue(widget)
        self.hudState(1)
        scrub.close()

    def setBackface(self):

        value = True if self.backfBtn.isChecked() else False
        self.opt.backfaceBrush = value

        self.console(toStr(value))

    def relaxBrush(self):
        """Relax CMD
        """
        frz = True if self.freezeBtn.isChecked() else False
        radius = self.radiusSlid.value() * 5.0
        itn = self.forceSlid.value() * 0.0005

        # -- to restore later or interactiv context
        self.opt.radius = self.radiusSlid.value()
        self.opt.intensity = self.forceSlid.value()
        self.opt.freeze = frz

        # -- preserve the tweak node for meshinter optimisation
        if self.ziTweakNode():
            self.detachTweakNode()

        self.tweakBtn.setChecked(False)

        self.setContext()

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, rb=1, rad=radius, i=itn, fr=frz)

        self.ziRailLaunchBtn.setChecked(False)
        self.console()

    def determineFigure(self):

        index = int()

        if self.strokeBtn.isChecked():
            index = 0

        elif self.lineBtn.isChecked():
            index = 1

        elif self.squareBtn.isChecked():
            index = 2

        elif self.circleBtn.isChecked():
            index = 3

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, figure=index)

    def setFigure(self):

        index = int()
        figure = "Stroke"

        if self.sender() == self.strokeBtn:
            self.nodebutton(True, False, False, False)
            index = 0

        if self.sender() == self.lineBtn:
            self.nodebutton(False, True, False, False)
            figure = "Line"
            index = 1

        if self.sender() == self.squareBtn:
            self.nodebutton(False, False, True, False)
            figure = "Square"
            index = 2

        if self.sender() == self.circleBtn:
            self.nodebutton(False, False, False, True)
            figure = "Circle"
            index = 3

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, figure=index)
            self.console(figure)

    def displayProjection(self):

        if not cmds.contextInfo(self.ctx, exists=True):
            return

        if self.displayProjBtn.isChecked():
            cmds.ziRailContext(self.ctx, e=True, dd=self.distanceSpin.value())
        else:
            cmds.ziRailContext(self.ctx, e=True, dd=0)

        self.console(self.distanceSpin.value(),
                     toStr(self.displayProjBtn.isChecked()))

    def setFreezeBorder(self):
        if not cmds.contextInfo(self.ctx, exists=True):
            return

        value = self.freezeBtn.isChecked()
        self.opt.freeze = value
        cmds.ziRailContext(self.ctx, e=True, freeze=value)

        self.console(toStr(value))

    def nodebutton(self, stroke, line, square, circle):

        self.strokeBtn.setChecked(stroke)
        self.lineBtn.setChecked(line)
        self.squareBtn.setChecked(square)
        self.circleBtn.setChecked(circle)

    def setMesh(self):
        """
        """
        if cmds.contextInfo(self.ctx, exists=True):
            cmds.deleteUI(self.ctx)

        self.setContext()

        cmds.setToolTo('selectSuperContext')
        cmds.select(clear=True)

    def initNodes(self):
        """
        """
        tweaknode = self.ziTweakNode()

        if tweaknode:
            cmds.delete(tweaknode)

    def setContext(self):
        """
        """
        freezestate = self.freezeSymBtn.isChecked()

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.setToolTo(self.ctx)

        else:
            self.ctx = cmds.ziRailContext()
            cmds.setToolTo(self.ctx)

        self.determineFigure()

        if freezestate:
            self.freezeSymBtn.setChecked(True)
            self.setFreezeMedian()

        cmds.makeLive(none=True)

    def blank(self, obj, span):
        """
        """
        func = self.disableU if span == "u" else self.disableV
        mode = False if obj.isChecked() else True
        func(mode)

        if span == 'u':
            self.opt.u = 1 if obj.isChecked() else self.Uspin.value()

        if span == 'v':
            self.opt.v = 1 if obj.isChecked() else self.Vspin.value()

    def disableU(self, mode):
        list(map(lambda x: x.setEnabled(mode), [self.upUBtn,
                                                self.dnUBtn,
                                                self.Uspin]))

    def disableV(self, mode):
        list(map(lambda x: x.setEnabled(mode), [self.upVBtn,
                                                self.dnVBtn,
                                                self.Vspin]))

    def changeBridge(self):
        """
        """
        self.opt.bdiv = int(self.bridgeSpin.value())

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, sbl=True)
            self.console(self.opt.bdiv)

    def launching(self):
        """Launch the main context tool
        """
        # -- already in zirailMode
        # if "ziRailContext" in cmds.currentCtx():
        # need to know if it's in brush or relax mode
        # return

        if not cmds.constructionHistory(q=True, tgl=True):
            cmds.error("Please activate the construction history")

        Mesh.node(self.opt.source, self)

        if not cmds.objExists(self.pickSrcBtn.text()):
            self.ziRailLaunchBtn.setChecked(False)
            cmds.error("Please set a Source Mesh")
            return

        if cmds.polyEvaluate(self.opt.source, f=True) > 1000000:
            cmds.warning("The source mesh is a bit too dense, you may decimate\
             it before processing")

        if self.pickSrcBtn.text() in cmds.ls(sl=True):
            cmds.select(clear=True)

        self.detachTweakNode()

        list(map(lambda x: x.setChecked(False),
                 [self.relaxBrBtn, self.tweakBtn]))

        self.refreshColors()
        self.setContext()
        self.displayLocator()

        forceShader()
        self.console()

    def displayLocator(self):
        """The ziRail node is a locator node
        it needs to turn on the locator filter so we can display the strokes
        """
        for panel in cmds.getPanel(type='modelPanel'):
            cmds.modelEditor(panel, e=True, locators=True)

    def reverseBridge(self):

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, reverseBridge=1)
            self.console()

    def popupFreeze(self, sels):
        """After detecting if the mesh is non-freezed, opens a popup window
        :Param sels(list): the current selection
        """

        win = QtWidgets.QDialog(zi_Widget.zi_Windows.getMayaWin())
        win.setWindowModality(QtCore.Qt.WindowModal)
        win.setWindowTitle("freeze transform".title())

        mesh = Mesh(sels[0])
        msg = "\
The specified mesh '%s' needs to have its transforms frozen\n\
(translate, rotate kb to 0 and scales to 1)\n\
\t\tProceed?\n" % sels[0]

        layout = QtWidgets.QVBoxLayout()
        labl = QtWidgets.QLabel(msg)
        labl.setAlignment(QtCore.Qt.AlignCenter)

        box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok |
                                         QtWidgets.QDialogButtonBox.Cancel,
                                         QtCore.Qt.Horizontal)

        box.setCenterButtons(True)
        box.accepted.connect(lambda: self.freezeMesh(mesh, win))
        box.rejected.connect(lambda: win.close())

        layout.addWidget(labl)
        layout.addWidget(box)

        win.setLayout(layout)

        win.show()

    def pickSource(self):
        """Specify the source mesh and make its connections
        """
        sels = cmds.ls(sl=True)

        if not sels:
            cmds.error("invalid selection")

        shape = Mesh(sels[0]).shape()

        if not shape:
            cmds.error("invalid selection")

        if not Mesh.isFreezed(sels):
            self.popupFreeze(sels)
            return

        # -- if a source was previously set, deactivate the attribute
        self.clearReferenceState(self.opt.sourceShape)

        self.opt.sourceShape = shape
        node = Mesh.node(shape, self)

        self.pickSrcBtn.setText(sels[0])
        self.connect(shape, "outMesh", node, "ziRailMesh")

        self.initNodes()
        self.setMesh()

        self.console("-- {}({})".format(sels[0], shape))

    def enablePinch(self, value):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        state = False if value == 0 else True
        self.pinchSlid.setEnabled(state)
        self.console(toStr(state))

    def resetPinch(self):

        self.pinchSlid.setValue(0)
        self.setPinch(0)

        self.console()

    def setPinch(self, value):

        if not self.lockedPinchChk.isChecked():
            return

        if cmds.contextInfo(self.ctx, exists=True):
            cmds.ziRailContext(self.ctx, e=1, pinch=value / 100.0)

        self.pinchSlid.setValue(value)
        self.console(value)

    def setupNetwork(self):
        """Create the networks connection
        """
        if not self.ziRailNode():
            self.createStream()

    def createRailNode(self):
        """Description

        :Return (None): desc.
        """
        node = cmds.createNode(__tool__, n='ziRailShape', ss=True)

        return node

    def restoreSource(self):
        """set the previous source to reinitialize the ziRail node

        :Param var(None): desc.
        :Return (None): desc.
        """

        source = self.pickSrcBtn.text()

        if not cmds.objExists(source):
            return

        prevSelection = cmds.ls(sl=True)

        cmds.select(source, replace=True)
        self.pickSource()

        cmds.select(prevSelection, replace=True)
        self.console("source restored %s" % source)

    def createStream(self):
        """Create the connection and node if not exist
        """
        sels = cmds.ls(sl=True)

        node = ''
        currentNodes = cmds.ls(typ=__tool__)

        if not currentNodes:
            node = self.createRailNode()
            self.restoreSource()
        else:
            node = currentNodes[0]

        if not cmds.nodeType(node) == __tool__:
            cmds.delete(node)
            cmds.error("please load %s plugin" % __tool__)

        if not self.opt.sourceShape:
            cmds.error("Please specify a source mesh first")

        if not cmds.objExists(self.opt.sourceShape):
            cmds.error("please specify a valid source")

        self.connect(self.opt.sourceShape, 'outMesh', node, 'ziRailMesh')
        self.console("\"%s\" connected to %s" % (self.opt.sourceShape, node))

        # -- restoring previous selection
        cmds.select(sels, replace=True)

    def toggleQuadMode(self):

        node = self.ziRailNode()
        subMesh = self.pickSrcBtn.text()

        if not subMesh:
            cmds.warning("no source selected")
            return

        # first initialization, create the graph network and nodes
        if not node:
            self.pickSource()
            railMode()

            return

        # -- switch to railMode
        if "nexQuadDrawCtx" in cmds.currentCtx():

            railMode()
            if cmds.objExists(SETNAME):

                setSel = cmds.sets(SETNAME, q=True)

                if setSel:
                    cmds.select(setSel[0], replace=True)
                    self.applyViewport()

            self.console("ziRail Mode")
            return

        # -- switch to quadDraw
        if cmds.objExists(subMesh):

            prevRetopoSelection = self.getShapeSelection()
            cmds.makeLive(subMesh)

            cmds.select(prevRetopoSelection, replace=True)
            mel.eval('dR_quadDrawTool')

            self.wirefr.createSet()
            cmds.sets(prevRetopoSelection, edit=1, forceElement=SETNAME)
            cmds.optionVar(sv=["ziRail_info1", "QUADDRAW activated"])

            self.console("QuadDraw Mode")

    def ziTweakNode(self):
        """Returns the node of type ziTweakNode in the scene as list or []
        """
        return cmds.ls(typ="ziTweakNode")

    def detachTweakNode(self):
        """
        """
        tweaknode = self.ziTweakNode()
        shape = self.getShape()

        if cmds.objExists(self.opt.sourceShape) and tweaknode and shape:

            disc = self.disconnect

            disc(self.opt.sourceShape,
                 'worldMesh[0]', tweaknode[0], 'scanMesh')
            disc(tweaknode[0], "ziTweakEval", shape, "visibility")
            disc(shape, "worldMesh[0]", tweaknode[0], "lowMesh")

    def linkJob(self, node1, attr1, node2, attr2, connect):
        """Desc
        :Param  node1:
        :Type  node1:

        :Param  attr1:
        :Type  attr1:

        :Param  node2:
        :Type  node2:

        :Param  attr2:
        :Type  attr2:
        """
        self.console("%s.%s  -->> %s.%s" %
                     (node1, attr1, node2, attr2))

        for node in [node1, node2]:

            if not cmds.objExists(node):
                cmds.error("the node %s does not exist" % node)

        male = '.'.join([node1, attr1])
        female = '.'.join([node2, attr2])

        if connect:
            if not cmds.isConnected(male, female):
                cmds.connectAttr(male, female, f=True)

        else:
            if cmds.isConnected(male, female):
                cmds.disconnectAttr(male, female)

    def connect(self, node1, attr1, node2, attr2):
        self.linkJob(node1, attr1, node2, attr2, True)

    def disconnect(self, node1, attr1, node2, attr2):
        self.linkJob(node1, attr1, node2, attr2, False)

    def attachTweakNode(self, shape, node):
        """Set the connections from tweaknode, selections and source
        if tweakNode already exists, reconnect

        :Param shape: the current selection
        :Type shape: str()

        :Param node: the existing tweakNode path or None
        :Type node: str()
        """
        self.connect(self.opt.sourceShape, "worldMesh[0]", node, "scanMesh")
        self.connect(node, "ziTweakEval", shape, "visibility")
        self.connect(shape, "worldMesh[0]", node, "lowMesh")

    def ziSetNode(self):
        ex = cmds.objExists
        return [n for n in cmds.ls(typ="objectSet") if ex("%s.zisetsym" % n)]

    def ziRailNode(self):
        """Get a ziRail node or create one if none
        """
        return Mesh.node(self.opt.source, self)

    def getSelZiMesh(self):

        sel = cmds.ls(sl=True, o=True)

        if sel:
            return cmds.listRelatives(sel[0], parent=True, typ="transform")[0]

    def freezeMesh(self, mesh, win):
        mesh = mesh.frozen(win)
        self.pickSource()

    def getShape(self):
        """
        """
        sels = cmds.ls(hl=True) + cmds.ls(sl=True, o=True)

        for sel in sels:
            if cmds.nodeType(sel) == "mesh":
                return sel

            shapes = cmds.listRelatives(sel, shapes=True)

            if shapes:
                if cmds.nodeType(shapes[0]) == 'mesh':
                    return shapes[0]

        return None

    def loadPlugin(self):
        """
        """
        version = cmds.about(v=True)

        for plug in NAMEPLUGS:
            name = "{name}_{ver}".format(name=plug, ver=version)

            if not cmds.pluginInfo(name, q=True, loaded=True):

                try:
                    cmds.loadPlugin(name)
                    self.console("{} loaded".format(name))

                except Exception as e:
                    print("{} fail loading".format(e))

        return cmds.pluginInfo("{}_{}".format(NAMEPLUGS[0], version), q=1, l=1)

    def setTips(self):
        """Descr
        """
        if self.sender().isChecked():
            self.desinstallTips()
            self.sender().setText("Enable Help")
            self.console("Help set to Off")

        else:
            self.installTips()
            self.sender().setText("Disable Help")
            self.console("Help set to On")

        self.setHelpAttr()

    def desinstallTips(self):
        """Descr
        """
        [tip.wid.removeEventFilter(tip) for tip in self.tips]

    def installTips(self):
        """Descr
        """
        tip = self.tips.append

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.pickSrcBtn,
            "",
            "Set the base mesh for the retopo process, the strokes will be drawn on top of it.\n\
It's usually a scan or a high mesh geometry. \n\
The Transforms have to be frozen (translate to 0 and scale to 1)\n\
If for some reasons you have modified its transforms, topology or morphology), reset this button",
            ":/logo/skin/neon/rabbitHigh.PNG"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.refBox,
            "",
            "Avoid selecting the source mesh while working on the retopo mesh.\n\
The retopo mesh will be set as a reference with its shape attribute.\n\
The attributes are:\n\n <shape>.overrideEnabled\n <shape>.overrideDisplayType",
            ":/gif/skin/vertexture/tips/reference_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.uLabUp,
            "({}) zi_rail.UspanUp()".format(self.hk.kb['uspanUp'][0]),
            "It changes the amount of spans in the U direction.\n\
You can manually enter its value in the field or increment with the arrow button.",
            ":/gif/skin/vertexture/tips/spanu_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.uLabDn,
            "({}) zi_rail.UspanDn()".format(self.hk.kb['uspanDn'][0]),
            "It changes the amount of spans in the U direction.\n\
You can manually enter its value in the field or increment with the arrow button.",
            ":/gif/skin/vertexture/tips/spanu_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.vLabUp,
            "({}) or HOLD SHIFT+MMB\nDrag the mouse horizontaly".format(
                self.hk.kb['vspanUp'][0]),
            "Change the amount of spans in V direction.\n\
The V direction normally stands for the direction following to the rail.\
You can manually enter its value in the field or increment with the arrow button.",
            ":/gif/skin/vertexture/tips/spanv_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.vLabDn,
            "({}) or HOLD SHIFT+MMB\nDrag the mouse horizontaly".format(
                self.hk.kb['vspanDn'][0]),
            "Change the amount of spans in V direction.\n\
The V direction normally stands for the direction following to the rail.\
You can manually enter its value in the field or increment with the arrow button.",
            ":/gif/skin/vertexture/tips/spanv_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.pinchSlid,
            "HOLD SHIFT+LMB\nDrag the mouse vertically",
            "Determines how close are the last edges loops subdivisions to the borders of the newly patch. \
This function is enabled as long as the dashed red and blue lines are displayed. \
If the checkbox is deactivate the pinch will not be apply",
            ":/gif/skin/vertexture/tips/pinch_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.slidBtn,
            "",
            "Set the pinch to its default value (0.5)",
            ""))
        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.projSlid,
            "",
            "A rail is generated then snapped onto the source mesh.\n\
During the snap process, a vertex is considered only if the distance from its position \
and the closest SourceMesh point on surface is smaller than this value. \
A too big value would create artifacts with overlapping surfaces",
            ":/gif/skin/vertexture/tips/projDistance_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.displayProjBtn,
            "",
            "It gives a visual representation of the max ray distance directly in the viewport. \n\
Quite handy for a better adjustement. It's recommended to have it disabled otherwise",
            ":/gif/skin/vertexture/tips/projDistDisplay_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.bridg_lab,
            "HOLD SHIFT+MMB\nDrag the mouse horizontaly",
            "You can create a patch which connects tow border, a bridge. \n\
This widget sets the amount of subdivisions included the in the bridge. \n\
For the sake of the efficiency, you can either scrub the mouse to change its value \
or use the spin widget on the right.",
            ":/gif/skin/vertexture/tips/bridgeSub_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.reversBridgBtn,
            "",
            "The bridge and merge functions study a prefered direction.\n\
This button allows to override this behavior thus reverse the direction \
of the newly created patch before validation. Locator displays will guide in the viewport during the process",
            ":/gif/skin/vertexture/tips/bridgeRevrs_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.closeStrokeBtn,
            "({}) zi_rail.closeStroke()".format(self.hk.kb['closeStrokes'][0]),
            "Strokes can be open or closed.\n\
Closed strokes are convenient for radial shapes like eye orbitals. \n\
Draw the stroke(s) then click this button to close it. \n\
This is a batch function, you can draw all of them then click this button. It will close all the current stroke(s)",
            ":/gif/skin/vertexture/tips/circleStroke_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.hudChk,
            "",
            "Show/hide the Head Up messages at the top of the viewport.",
            ""))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.viewportBtn,
            "",
            "Open the ziWireframe UI.\n\
This interface has custom input to customize the retopo geometry appearance. \n\
Attribute like surface opacity of wireframe color can be set. \
This would greatly help to see through the surfaces while working on overlapping meshes",
            ":/gif/skin/vertexture/tips/shaderWin_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.shaderApplyBtn,
            "({}) zi_rail.toggleShader()".format(
                self.hk.kb['toggleShader'][0]),
            "Activate/Deactivate the ziWireframe functions.",
            ":/gif/skin/vertexture/tips/shaderToggle_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.relaxBrBtn,
            "Hold CTRL+SHIFT+MMB\nthen scrub\n(zi_rail.relax())",
            "This will switch to the relax brush mode.\n\
The vertices included in the brush radius will be modified. Instead of switching to this mode, \
you can simply use the key combinaison (CTRL-SHIFT MMB) to relax interactively in the viewport.",
            ":/gif/skin/vertexture/tips/brushrelax_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.moveBtn,
            "Hold MMB\nthen scrub\n(zi_rail.tweak())",
            "This function moves the vertices in a 2d screen space. \n\
You can either use this button to switch the corresponding mode or drag the MMB. Using this button will deactivate the Rail Mode\
but will maintain the relax mode",
            ":/gif/skin/vertexture/tips/brushmoveSize_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.backfBtn,
            "({}) zi_rail.backface()".format(self.hk.kb['backFaceCulling'][0]),
            "Toggle the backface mode. \n\
Whether the vertices facing toward the camera are considered or not. \
This has effect while brushing.",
            ":/gif/skin/vertexture/tips/backface_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.freezeBtn,
            "({}) zi_rail.freezeBorder()".format(
                self.hk.kb['freezeBorder'][0]),
            "Lock the vertices on the boundaries. \n\
The vertices at the boundaries won't be affected",
            ":/gif/skin/vertexture/tips/frzBorder_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.relaxint_lab,
            "Hold \'{}\'\nthen scrub".format(
                self.hk.kb['brushRelaxIntensity'][0]),
            "Brush Relax Strength value",
            ":/gif/skin/vertexture/tips/brushStrength_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.relaxrad_lab,
            "Hold \'{}\'\nthen scrub".format(
                self.hk.kb['brushRelaxRadius'][0]),
            "Brush Relax Size value",
            ":/gif/skin/vertexture/tips/brushrelaxRad_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.moverad_lab,
            "Hold \'{}\'\nthen scrub".format(self.hk.kb['brushMoveRadius'][0]),
            "Brush Move Size value",
            ":/gif/skin/vertexture/tips/brushmoveSize_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.ziRailLaunchBtn,
            "({}) zi_rail.railMode()".format(self.hk.kb['railMode'][0]),
            "Activate the ziRail mode. \
This is the main mode ready to draw the rail on the source mesh",
            ":/gif/skin/vertexture/tips/railLaucnh_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.lazyBtn,
            "({}) zi_rail.lazyToggle()".format(self.hk.kb['lazyMode'][0]),
            "Activate the lazy mode. Suitable for drawing smooth.",
            ":/gif/skin/vertexture/tips/lazymode_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.lazySpinStrength,
            "",
            "Makes the lazy mode more or less stronger.",
            ":/gif/skin/vertexture/tips/lazymodeStrength_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.lazySpinDist,
            "",
            "The amount of points in the queue affected in the stroke",
            ":/gif/skin/vertexture/tips/lazymodeDistance_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.strokeBtn,
            "",
            "Hand stroke drawing. \n\
Default mode.",
            ":/gif/skin/vertexture/tips/handstroke_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.lineBtn,
            "",
            "Draw a straight line. \n\
Can be use for slice mode also (with SHIFT).",
            ":/gif/skin/vertexture/tips/lineStroke_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.squareBtn,
            "",
            "Draw a Square. \n\
Can be use for slice also. It's closed by nature",
            ":/gif/skin/vertexture/tips/squarestroke_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.circleBtn,
            "",
            "Draw a Circle. \n\
Can be use for slice also. It's closed by nature",
            ":/gif/skin/vertexture/tips/circleStroke_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.symmetryBtn,
            "({}) zi_rail.activeSymmetry()".format(self.hk.kb['symmetry'][0]),
            "Activate the symmetry. \n\
This will create an instance mesh with its x value flipped. ",
            ":/gif/skin/vertexture/tips/symmetry_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.freezeSymBtn,
            "({}) zi_rail.activeMedian()".format(
                self.hk.kb['symmetryMedian'][0]),
            "keep the median vertices at the center of the univers\n\
This ensures that the geometry is ready to be merged. \
Note that the symmetry mode is not necessary. ",
            ":/gif/skin/vertexture/tips/symmetryMedian_low.gif"))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.quadBtn,
            "({}) zi_rail.quadDrawToggle()".format(
                self.hk.kb['quadDrawMode'][0]),
            "Switch from the ziRail mode the Maya's Quad draw tool,\
and vice/versa",
            ""
        ))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.lockedPinchChk, "", "Enable/Disable the pinch attribute", ""))

        tip(zi_Widget.zi_Windows.ZiToolTip(
            self.hotkeyBtn, "", "Hotkeys customization", ""))

    def displayHotkeys(self):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        notice1 = QtWidgets.QLabel("""\
The hotkeys will be activated as long as the main UI is open
or manually disabled with the checkbox. To deactivate the hotkey
persistently, just leave a blank key.""")

        notice2 = QtWidgets.QLabel("""\
Example of available standard keys:
    - "backspace"
    - "escape"
    - "up"
    - "down"
    - "left"
    - "right"
""")

        notice1.setAlignment(QtCore.Qt.AlignHCenter)
        previousKeys = dict(self.hk.kb)

        win = QtWidgets.QDialog(zi_Widget.zi_Windows.getMayaWin())
        win.setWindowModality(QtCore.Qt.WindowModal)
        win.setWindowTitle("%s HotKeys Manager" % __tool__)

        frame = QtWidgets.QFrame()
        frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        mainLay = QtWidgets.QVBoxLayout()
        gridLay = QtWidgets.QGridLayout(frame)

        i = 1
        sortedkeys = sorted(self.hk.kb.items(), key=lambda x: x[1][-1])

        for key, values in sortedkeys:

            label = QtWidgets.QLabel(key[0].capitalize()+key[1:])

            ctrlOn = True if 'ctrl' in values[0].lower() else False
            shftOn = True if 'shift' in values[0].lower() else False
            altOn = True if 'alt' in values[0].lower() else False

            ctrlRad = QtWidgets.QRadioButton("Ctrl")
            shftRad = QtWidgets.QRadioButton("Shift")
            altRad = QtWidgets.QRadioButton("Alt")

            chk = QtWidgets.QCheckBox("")
            chk.setChecked(values[2])

            ctrlRad.setAutoExclusive(False)
            shftRad.setAutoExclusive(False)
            altRad.setAutoExclusive(False)

            ctrlRad.setObjectName("ctrl%d" % i)
            shftRad.setObjectName("shift%d" % i)
            altRad.setObjectName("alt%d" % i)

            ctrlRad.setDown(ctrlOn)
            shftRad.setDown(shftOn)
            altRad.setDown(altOn)

            tokens = values[0].split("+")
            lastToken = tokens[-1]

            line = QtWidgets.QLineEdit(lastToken)

            gridLay.addWidget(chk, i, 0)
            gridLay.addWidget(label, i, 1)
            gridLay.addWidget(ctrlRad, i, 2)
            gridLay.addWidget(shftRad, i, 3)
            gridLay.addWidget(altRad, i, 4)
            gridLay.addWidget(line, i, 5)

            chk.stateChanged.connect(lambda stat,
                                     keyb=key,
                                     labl=label: self.updateKBBox(stat,
                                                                  key=keyb,
                                                                  labw=labl))

            ctrlRad.released.connect(lambda
                                     chkw=chk,
                                     widCtrl=ctrlRad,
                                     widShft=shftRad,
                                     widAlt=altRad,
                                     text=lastToken,
                                     keyb=key: self.updateKB(key=keyb,
                                                             ctrlw=widCtrl,
                                                             shiftw=widShft,
                                                             altw=widAlt,
                                                             text=text))

            shftRad.released.connect(lambda
                                     chkw=chk,
                                     widCtrl=ctrlRad,
                                     widShft=shftRad,
                                     widAlt=altRad,
                                     text=lastToken,
                                     keyb=key: self.updateKB(key=keyb,
                                                             ctrlw=widCtrl,
                                                             shiftw=widShft,
                                                             altw=widAlt,
                                                             text=text))

            altRad.released.connect(lambda
                                    chkw=chk,
                                    widCtrl=ctrlRad,
                                    widShft=shftRad,
                                    widAlt=altRad,
                                    text=lastToken,
                                    keyb=key: self.updateKB(key=keyb,
                                                            ctrlw=widCtrl,
                                                            shiftw=widShft,
                                                            altw=widAlt,
                                                            text=text))

            line.textChanged.connect(lambda text,
                                     chkw=chk,
                                     widCtrl=ctrlRad,
                                     widShft=shftRad,
                                     widAlt=altRad,
                                     keyb=key: self.updateKB(key=keyb,
                                                             ctrlw=widCtrl,
                                                             shiftw=widShft,
                                                             altw=widAlt,
                                                             text=text))

            i += 1

        resetBtn = QtWidgets.QPushButton("Reset")
        qbox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok |
                                          QtWidgets.QDialogButtonBox.Cancel,
                                          QtCore.Qt.Horizontal)

        qbox.setCenterButtons(True)
        qbox.accepted.connect(lambda: win.close())
        qbox.rejected.connect(lambda: self.cancelHotkeys(win, previousKeys))
        resetBtn.clicked.connect(lambda: self.resetHK(win))

        mainLay.addWidget(notice1)
        mainLay.addWidget(notice2)
        mainLay.addWidget(frame)
        mainLay.addWidget(resetBtn)
        mainLay.addWidget(qbox)

        win.setLayout(mainLay)

        if self.butTheme.isChecked():
            win.setStyleSheet(zi_Widget.zi_Windows._style)
            win.setStyle(self.factory)

        win.show()

    def resetHK(self, window):

        self.hk.unset()
        for key in self.hk.kb.keys():
            self.hk.settings.qsettings.remove(key)

        self.hk = Hotkeys(self)
        window.close()

        self.displayHotkeys()

    def cancelHotkeys(self, win, previouskeys):
        self.hk.kb = previouskeys
        win.close()

    def updateKBBox(self, stat, key, labw):

        labw.setEnabled(stat)

        shortstring = self.hk.kb[key][0]

        for seq in self.hk.shortcuts:

            if shortstring == seq.key().toString().lower():
                stateButton = True if stat == 2 else False

                seq.setEnabled(stateButton)

                self.hk.kb[key][2] = stateButton
                self.hk.kb[key] = [self.hk.kb[key][0],
                                   self.hk.kb[key][1],
                                   stateButton,
                                   self.hk.kb[key][-1]]

                break

    def updateKB(self, key, ctrlw=None, shiftw=None, altw=None, text=None):

        textToken = ""

        textToken += "ctrl+" if ctrlw.isChecked() else ""
        textToken += "shift+" if shiftw.isChecked() else ""
        textToken += "alt+" if altw.isChecked() else ""

        textToken += text

        self.hk.unset()

        self.hk.kb[key] = [textToken.lower(),
                           self.hk.kb[key][1],
                           self.hk.kb[key][2],
                           self.hk.kb[key][-1]]

        self.hk.settings.save(key, textToken)
        self.hk.setSequences()

    def console(self, *txt):
        """
        """
        txt = list(map(str, txt))


        self.logLab.setText("({}) {}".format(
            sys._getframe(1).f_code.co_name,
            ", ".join(txt)))

        if VERBOSE:
            print("ziRInfo. {:_>50}".format(' '.join(txt)))

        # //////////////////////////// # ////////////////////////////

    def debuginstallation(self, debug):

        if not debug:
            return

        cmds.scriptEditorInfo(hfn="mayaconsole",
                              writeHistory=True,
                              clearHistoryFile=True)

        btn = QtWidgets.QPushButton("debug")
        self.verticalLayout_2.addWidget(btn)
        btn.clicked.connect(flush)

# ----------------------------------------------- hotkey wrappers


class Hotkeys(object):

    def __init__(self, obj):

        self.obj = obj
        self.shortcuts = []
        self.settings = zi_Widget.zi_Windows.Settings(__tool__)
        self.widgetLists = {
            "brushRelaxRadius": self.obj.relaxrad_lab,
            "brushRelaxIntensity": self.obj.relaxint_lab,
            "brushMoveRadius": self.obj.moverad_lab,

            "vspanUp": self.obj.vLabUp,
            "vspanDn": self.obj.vLabDn,
            "uspanUp": self.obj.uLabUp,
            "uspanDn": self.obj.uLabDn,

            "railMode": self.obj.ziRailLaunchBtn,
            "quadDrawMode": self.obj.quadBtn,

            "symmetry": self.obj.symmetryBtn,
            "symmetryMedian": self.obj.freezeSymBtn,
            "freezeBorder": self.obj.freezeBtn,

            "toggleShader": self.obj.shaderApplyBtn,
            "backFaceCulling": self.obj.backfBtn,

            "closeStrokes": self.obj.closeStrokeBtn,
            "lazyMode": self.obj.lazyBtn,
        }

        self.kb = {

            # -- "optionvar" : [hotkey, command, enabled, displayOrder],

            "brushRelaxRadius": ["b", lambda: obj.sDelta("brushRelaxRadius"), True, 0],
            "brushRelaxIntensity": ["n", lambda: obj.sDelta("brushRelaxIntens"), True, 1],
            "brushMoveRadius": ["m", lambda: obj.sDelta("brushMoveRadius"), True, 2],

            "vspanUp": ["ctrl+up", lambda: VspanUp(), True, 3],
            "vspanDn": ["ctrl+down", lambda: VspanDn(), True, 4],
            "uspanUp": ["ctrl+right", lambda: UspanUp(), True, 5],
            "uspanDn": ["ctrl+left", lambda: UspanDn(), True, 6],

            "railMode": ["ctrl+r", lambda: railMode(), True, 7],
            "quadDrawMode": ["alt+r", lambda: quadDrawToggle(), True, 8],

            "completion": ["enter", lambda: complete(), True, 9],

            "symmetry": ["s", lambda: activeSymmetry(), True, 10],
            "symmetryMedian": ["alt+s", lambda: activeMedian(), True, 11],
            "freezeBorder": ["ctrl+f", lambda: freezeBorder(), True, 12],

            "toggleShader": ["ctrl+t", lambda: toggleShader(), True, 13],
            "backFaceCulling": ["ctrl+b", lambda: backface(), True, 14],

            "closeStrokes": ["alt+c", lambda: closeStroke(), True, 15],
            "lazyMode": ["ctrl+l", lambda: lazyToggle(), True, 16],
        }

        self.reload()
        self.setSequences()

    def reload(self):

        for key, values in self.kb.items():

            settingsvalue = self.settings.load(key)

            if settingsvalue:
                self.kb[key] = [settingsvalue, values[1], values[2]]

    def deleteTextShortcuts(self):

        for key, values in self.widgetLists.items():

            reg = re.search(r"(.+)(\(.+\))", values.text())

            if reg:
                label = reg.groups()[0]
                values.setText(label)


    def setSequences(self):

        self.shortcuts = []
        for key, values in self.kb.items():

            thisShortcut = QtWidgets.QShortcut(
                QtGui.QKeySequence(values[0]), self.obj)

            thisShortcut.setContext(QtCore.Qt.ApplicationShortcut)
            thisShortcut.activated.connect(values[1])
            thisShortcut.setAutoRepeat(False)

            if values[2] == False:
                thisShortcut.setEnabled(False)

            self.setTextShortcuts(key, values[0])
            self.shortcuts.append(thisShortcut)

    def setTextShortcuts(self, key, token):

        if key in self.widgetLists.keys():

            curtext = self.widgetLists[key].text()
            label = "{}({})".format(curtext, token)

            reg = re.search(r"(.+)(\(.+\))", curtext)

            if reg:
                label = "{}({})".format(reg.groups()[0], token)

                if self.obj.hintsBtn.isChecked():
                    label = reg.groups()[0]

            self.widgetLists[key].setText(label)

    def unset(self):

        for shortcut in self.shortcuts:
            shortcut.setEnabled(False)
            shortcut.setContext(QtCore.Qt.WidgetShortcut)
            shortcut.deleteLater()



# -----------------------------------------------  DEBUG FUNCTION
# -----------------------------------------------  DEBUG FUNCTION


    def set_pos(self, nodename, plugname, poses):
        poslist = []
        for i in list(range(poses.length())):
            poslist.append([poses[i].x, poses[i].y, poses[i].z])

        cmds.setAttr("%s.%s" % (nodename, plugname),
                     poses.length(),
                     *poslist,
                     typ="pointArray")

        self.console("poses: {}\nposlist: {}".format(poses.length(), poslist))

    def get_attrs(self, nodename, attrs):

        for attr in attrs:
            print(attr, cmds.getAttr("%s.%s" % (nodename, attr)))

    @ staticmethod
    def loc(pos, name='', size=0.3):
        grpName = 'locs'

        if not cmds.objExists(grpName):
            cmds.createNode('transform', n=grpName)

        node = cmds.spaceLocator(n=name, p=(pos[0], pos[1], pos[2]))[0]

        try:
            cmds.setAttr('%s.localScaleX' % node, size)
            cmds.setAttr('%s.localScaleY' % node, size)
            cmds.setAttr('%s.localScaleZ' % node, size)

        except RuntimeError as e:
            self.console("not enough data %s" % e)

        cmds.delete(node, ch=True)
        cmds.xform(node, cpc=True)
        cmds.parent(node, grpName)

    @ staticmethod
    def locs(pos, name="", sz=0.2):
        [Win.loc(p, "{}_{:02}".format(name, i), sz) for i, p in enumerate(pos)]

    @ staticmethod
    def curv(points):
        poses = list(map(lambda x: (x[0], x[1], x[2]), points))
        cmds.curve(d=1, p=poses)

    @ staticmethod
    def draw(attr, pos):
        cmds.setAttr("ziRailShape.%s" % attr, len(pos), *pos, typ="pointArray")

    @ staticmethod
    def shadow():
        shd1 = cmds.getAttr("ziRailShape.shadowIndices1")
        shd2 = cmds.getAttr("ziRailShape.shadowIndices2")
        shd3 = cmds.getAttr("ziRailShape.shadowIndices2")
        print(shd1.__len__(), shd2.__len__(), shd3.__len__())


def toStr(value):
    return "On" if value else "Off"


def defaultSize():
    ziRailObj.parent().setGeometry(10, 10, 278, 840)

# ----------------------------------------------- hotkey wrappers
# ----------------------------------------------- hotkey wrappers


def railMode():
    ziRailObj.ziRailLaunchBtn.clicked.emit()


def VspanUp():
    ziRailObj.spansArrow(ziRailObj.Vspin, 1)


def VspanDn():
    ziRailObj.spansArrow(ziRailObj.Vspin, -1)


def UspanUp():
    ziRailObj.spansArrow(ziRailObj.Uspin, 1)


def UspanDn():
    ziRailObj.spansArrow(ziRailObj.Uspin, -1)


def closeStrokes():
    cmds.ziRailCmd(close=True)


def relax():
    ziRailObj.relaxBrBtn.setChecked(True)
    ziRailObj.relaxBrBtn.clicked.emit()


def tweak():
    ziRailObj.tweakBtn.setChecked(True)
    ziRailObj.tweakBtn.clicked.emit()


def freezeBorder():
    ziRailObj.freezeBtn.setChecked(not ziRailObj.freezeBtn.isChecked())
    ziRailObj.freezeBtn.clicked.emit()


def forceShader():
    if not ziRailObj.shaderApplyBtn.isChecked():
        toggleShader()
    else:
        ziRailObj.applyViewport()


def toggleShader():
    shaderWidget = ziRailObj.shaderApplyBtn
    shaderWidget.setChecked(not shaderWidget.isChecked())
    shaderWidget.clicked.emit()


def backface():
    ziRailObj.backfBtn.setChecked(not ziRailObj.backfBtn.isChecked())
    ziRailObj.backfBtn.clicked.emit()


def complete():
    ziRailObj.completion()


def activeSymmetry():
    ziRailObj.symmetryBtn.setChecked(not ziRailObj.symmetryBtn.isChecked())
    ziRailObj.setSymmetry()


def activeMedian():
    ziRailObj.freezeSymBtn.setChecked(not ziRailObj.freezeSymBtn.isChecked())
    ziRailObj.setFreezeMedian()


def closeStroke():
    ziRailObj.closeStroke()


def lazyToggle():
    ziRailObj.lazyBtn.setChecked(not ziRailObj.lazyBtn.isChecked())
    ziRailObj.lazyBtn.clicked.emit()


def quadDrawToggle():
    ziRailObj.quadBtn.setChecked(not ziRailObj.quadBtn.isChecked())
    ziRailObj.quadBtn.clicked.emit()

# ----------------------------------------------- hotkey wrappers
# ----------------------------------------------- hotkey wrappers


def qset():
    return QtCore.QSettings(__author__.capitalize(), "licenses")


def setkey(lkey):
    qset().setValue("_".join([__tool__, "lic"]), lkey)


def getkey():
    return qset().value("_".join([__tool__, "lic"]))


def clearkey():
    [qset().remove("_".join([__tool__, suffix])) for suffix in ['lic', 'pub']]


# ----------------------------------------------- license inclusion


def flush():
    """
    """
    cmds.MoveTool()

    plugName = "ziRail_2018"
    rails = cmds.ls(exactType="ziRail")
    patch = cmds.ls(exactType="ziPatchNode")

    if rails: cmds.delete(rails)
    if patch: cmds.delete(patch)


    cmds.flushUndo()

    if cmds.pluginInfo(plugName, q=True, loaded=True):
        cmds.pluginInfo(plugName, e=True, rm=True)
        cmds.unloadPlugin(plugName)


# ----------------------------------------------- MAIN FUNCTION
# ----------------------------------------------- MAIN FUNCTION


def main(debugging=False, dockable=True, internet=True):

    global ziRailObj

    try:
        ziRailObj.deleteLater()

    except BaseException:
        pass

    ziRailObj = Win(debugging, dockable, internet)
    return ziRailObj

# -- Vtx python version 3
