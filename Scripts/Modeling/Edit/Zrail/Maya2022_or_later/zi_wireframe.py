# //
# //                          AUTHOR
# .-.   .-.-..--.-..-..-..-..-.-..--.-.  .-.-..-..-.-.   .-.-..-. .-..--.
# | |   | | | ~~| | ~.-~ | | ~| | ~~| |  | |~ | | ~| |   | | | ~.-| | ~~
# | |   | | | _ | |.-.~  | |  | | _ `-'..`-'  | |  | |   | | |.-.~| | _
# | |   | | |`-'| | ~.-. | |  | |`-'.-.`'.-.  | |  | |   | | | ~.-| |`-'
# `-' _ `-| | __| |  | | | |  | | __| |  | |  | |  | | _ | | |  | | | __
#    `-'  `-'`--`-'  `-' `-'  `-'`--`-'  `-'  `-'  `-'`-'`-`-'  `-`-'`--'
# //  (contact@vertexture.org)
# //  www.vertexture.org
# //  Please read on the website terms of use and licensing.
# //  Tutorials can be found also
# //
# //                          DATE
# //  25/02/2020
# //
# //                          DESCRIPTION
# // Change mesh surface properties mesh display within the vertexture viewport
# //
# .-----|__|    .--.--.--|__.----.-----.'  _.----.---.-.--------.-----.
# |-- __|  |    |  |  |  |  |   _|  -__|   _|   _|  _  |        |  -__|
# |_____|_______|________|__|__| |_____|__| |__| |___._|__|__|__|_____|
#         |______|
#
# ////////////////////////////////////////////////////////////////////////////////////*/
from PySide2 import QtWidgets, QtCore, QtGui
import zi_Widget.zi_Windows
import zi_UI.ziRessources_rc

import maya.cmds as cmds
from maya.mel import eval

help = """
<html><head/><body><p align="center"><img src=":/vertexture/skin/vertexture/logoHs_color.png"/></p><p><br/><br/></p><p><span style=" font-size:10pt; font-weight:600; color:#7e835a;">ziWireframeViewport </span>displays custom wireframe attributes. </p><p><br/></p><p><span style=" font-size:10pt; font-weight:600;">Surface Color</span><span style=" font-weight:600;"> - </span>change the rgb color of the surface (<span style=" font-size:10pt; font-weight:600;">rgb</span><span style=" font-weight:600;">.</span>a)</p><p><span style=" font-size:10pt; font-weight:600;">Point Color</span> - The color of the selected vertices and soft rich selection (<span style=" font-size:10pt; font-weight:600;">rgb</span><span style=" font-weight:600;">.</span>a).</p><p><span style=" font-size:10pt; font-weight:600;">Backface Color</span><span style=" font-weight:600;">- </span>displayed rgb color of the backfacing surface polygons (<span style=" font-size:10pt; font-weight:600;">rgb</span><span style=" font-weight:600;">.</span>a)</p><p><span style=" font-size:10pt; font-weight:600;">Line Color</span> -This stands for wireframe color itself (<span style=" font-size:10pt; font-weight:600;">rgb</span><span style=" font-weight:600;">.</span>a).</p><p><br/></p><p><span style=" font-size:10pt; font-weight:600;">Surface Alpha</span> - so you can specify the alpha component of the Surface color (rgb.<span style=" font-size:10pt; font-weight:600;">a</span>).</p><p><span style=" font-size:10pt; font-weight:600;">Depth Priority</span> - Actually the Zdeph test for surface and wireframe display. Increasing this value would draw the wireframe ontop of the rest of scene.</p><p><span style=" font-size:10pt; font-weight:600;">Line Width</span>- The thickness of the wireframe.</p><p><span style=" font-size:10pt; font-weight:600;">Point Size </span>- The draw size of the selected vertices.</p><p><br/></p><p><span style=" font-size:10pt; font-weight:600;">Backface Colour </span>- Enable the backfacing polygons display.</p><p><span style=" font-size:10pt; font-weight:600;">Backface Culling </span>- If checked. the polygons facing away the camera won't be displayed.</p><p><span style=" font-size:10pt; font-weight:600;">Override Shading</span>- if checked, the selected mesh geometry will display its polygon surface.</p><p><span style=" font-size:10pt; font-weight:600;">Force Refresh </span>- Permanently calculate the datas. If not checked, the calcul will happen durin the idle state.</p><p><br/></p><p><span style=" font-size:10pt; font-weight:600;">Add Mesh </span>- Set the mesh to take in consideration.</p><p>------------------------------------------------------------</p><p>for more informations and video tutorials, please visit</p><p><a href="www.vertexture.org"><span style=" text-decoration: underline; color:#0000ff;">www.vertexture.org</span></a></p><p align="justify"><br/></p><p align="justify"><br/></p></body></html>

"""
__version__ = 0.98
__tool__ = "ziWireframe"
__author = "VERTEXTURE"

kDoublesWire = {"Surface Alpha": 'ziCutSa',
                "Line Width": 'ziCutLw',
                "Depth Priority": 'ziCutDp',
                "Point Size": 'ziCutPs',
                "Mesh Display Limit": "ziCutLimit",
                }

kDoublesCut = {
    # -- ziCut options got removed, it has its own properties.mel
    # "Split Threshold": 'ziSplitThres',
    # "Angle Limit": 'ziAngleLimit'
}

kDoubles = dict(kDoublesWire)
kDoubles.update(kDoublesCut)

kColors = {"Surface Color": ['ziCutSurfCr', 'ziCutSurfCg', 'ziCutSurfCb'],
           "Line Color": ["ziCutLineCr", "ziCutLineCg", "ziCutLineCb"],
           "Point Color": ["ziCutPtCr", "ziCutPtCg", "ziCutPtCb"],
           "Backface Color": ["ziCutBackCr", "ziCutBackCg", "ziCutBackCb"]
           }

kChecks = {"Override Shading": 'ziCutShading',
           "Backface Culling": 'ziCutBackf',
           "Force Refresh": 'ziCutUpdate',
           "Backface Colour": 'ziCutBackfc',
           }

attrContinuity = "ziCutContinuity"

NAMEPLUGS = ["ziWireframeViewport", "ziCut"]
kIncrement = 100
DEBUG = False


class OptVar(object):

    def __init__(self):
        pass

    def load(self, obj):
        """Description
        """
        for suffix, typ in zip(["_line", "_slider"], [str, float]):

            for name in kDoubles.keys():
                widget = obj.findWidget(name, suffix)

                if not widget:
                    continue

                obj.setVar(widget, typ, name)

        for key, values in kColors.items():

            if key == "Backface Color":
                widget = obj.findWidget(key, "_color")
                obj.setColor(widget, self.backfColor)

            if key == "Surface Color":
                widget = obj.findWidget(key, "_color")
                obj.setColor(widget, self.surfColor)

            if key == "Line Color":
                widget = obj.findWidget(key, "_color")
                obj.setColor(widget, self.lineColor)

            if key == "Point Color":
                widget = obj.findWidget(key, "_color")
                obj.setColor(widget, self.pointColor)

        for key, value in kChecks.items():

            widget = obj.findWidget(key, "_check")
            outputState = self.getValue(kChecks[key], False)
            widget.setChecked(outputState)

    def getValue(self, value, default):
        """Description
        """
        result = default

        if cmds.optionVar(exists=value):
            result = cmds.optionVar(q=value)

        return result

    @property
    def lineContinuity(self):
        return self.getValue(attrContinuity, 0)

    @property
    def lineWidth(self):
        return self.getValue(kDoubles["Line Width"], 2.0)

    @property
    def surfaceAlpha(self):
        return self.getValue(kDoubles["Surface Alpha"], 0.3)

    @property
    def pointSize(self):
        return self.getValue(kDoubles["Point Size"], 5.0)

    @property
    def refresh(self):
        return self.getValue(kDoubles["Point Size"], 5.0)

    @property
    def backface(self):
        attr = kChecks["Backface Culling"]
        return cmds.optionVar(q=attr) if cmds.optionVar(ex=attr) else True

    @property
    def depth(self):
        return self.getValue(kDoubles["Depth Priority"], 900)

    @property
    def spiltT(self):
        return self.getValue(kDoubles["Split Threshold"], 0.02)

    @property
    def angleL(self):
        return self.getValue(kDoubles["Angle Limit"], 150)

    @property
    def vertL(self):
        return self.getValue(kDoubles["Vertices Limit"], 50000)

    @property
    def dispLimit(self):
        return self.getValue(kDoubles["Mesh Display Limit"], 150000)

    @property
    def surfColor(self):
        return (self.getValue('ziCutSurfCr', 0.014),
                self.getValue('ziCutSurfCg', 0.014),
                self.getValue('ziCutSurfCb', 0.17)
                )

    @property
    def backfColor(self):
        return (self.getValue('ziCutBackCr', 0.17),
                self.getValue('ziCutBackCg', 0.014),
                self.getValue('ziCutBackCb', 0.017)
                )

    @property
    def lineColor(self):

        return (self.getValue('ziCutLineCr', 0.08),
                self.getValue('ziCutLineCg', 0.06),
                self.getValue('ziCutLineCb', 0.17)
                )

    @property
    def pointColor(self):

        return (self.getValue('ziCutPtCr', 0.61),
                self.getValue('ziCutPtCg', 0.61),
                self.getValue('ziCutPtCb', 0.13)
                )

    @property
    def meshName(self):
        varname = "ziCutMeshName"
        return cmds.optionVar(q=varname) if cmds.optionVar(ex=varname) else ""

    def clear(self):

        for var in kDoubles.items() + kChecks.items():
            cmds.optionVar(remove=var)

        for vars in kColors.items():
            for var in vars:
                cmds.optionVar(remove=var)


class Win(zi_Widget.zi_Windows.Frameless):

    def __init__(self, dockable, show=True):
        super(Win, self).__init__()

        self.var = OptVar()

        self.loadPlugin()
        self.setWinLayout()
        self.setConnections()
        self.setWin()

        self.var.load(self)
        self.reloadSet()

        self.restoreTheme()

        if show:
            self.show(dockable=dockable)

    def setWin(self):
        """Description
        """
        self.addBar(help,
            __tool__,
            False,
           "https://vertexture.org/?source=mayapp",
           miniSize=36
           )

        title = "%s %s" % (__name__, __version__)
        self.setWindowTitle(title)

        self.setMaximumSize(600, 900)
        self.setMinimumSize(100, 100)
        self.setGeometry(600, 300, 260, 590)

        geo = self.geometry()
        x, y = [geo.x(), geo.y()]

        x = 0 if x < 0 else x
        y = 0 if y < 0 else y

        self.setGeometry(x, y, geo.width(), geo.height())

        if not cmds.objExists(self.var.meshName):
            self.findWidget("Backface Culling", "_check").setChecked(True)
            return

        attr = "%s.overrideShading" % self.var.meshName

        self.findWidget("Override Shading", "_check").setChecked(
            cmds.getAttr(attr))

        attr = "%s.backfaceCulling" % self.var.meshName

        if self.isMesh():
            value = True if cmds.getAttr(attr) == 3 else False
            self.findWidget("Backface Culling", "_check").setChecked(value)

        self.restoreGeo()

    def setConnections(self):
        """Description
        """
        for k in kDoubles.keys():
            self.findWidget(k, "_slider").valueChanged.connect(self.slid2Line)

        for k in kDoubles.keys():
            self.findWidget(k, "_line").editingFinished.connect(self.line2Slid)

        for k in kColors.keys():
            self.findWidget(k, "_color").clicked.connect(self.defineColor)

        for k in kChecks.keys():
            self.findWidget(k, "_check").clicked.connect(self.setCheck)

        self.ziUnlock.changedValue.connect(self.unlock)

    def loadPlugin(self):
        """Description
        """
        version = cmds.about(v=True)
        for plug in NAMEPLUGS:

            name = "{name}_{ver}".format(name=plug, ver=version)

            if not cmds.pluginInfo(name, q=True, loaded=True):
                try:
                    cmds.loadPlugin(name)
                except:
                    pass

    def unlock(self):
        """Description
        """
        panels = cmds.getPanel(type="modelPanel")

        for panel in panels or []:

            if self.ziUnlock.value == "ON":
                cmd = "setRendererAndOverrideInModelPanel $gViewport2 %s %s"
                eval(cmd % ("VertextureViewport", panel))

            if self.ziUnlock.value == "OFF":
                cmd = "setRendererInModelPanel $gViewport2 %s"
                eval(cmd % (panel))

    def setWidgetCheck(self, name, value):
        self.findWidget(name, "_check").setChecked(value)

    def setWidgetLine(self, name, value):

        self.findWidget(name, "_slider").setValue(value * kIncrement)
        self.findWidget(name, "_line").setText(str(value))

    def setWidgetcolor(self, name, value):
        """Description

        :Param name:
        :Type name:

        :Param value:
        :Type value:
        """
        obj = self.findWidget(name, '_color')
        self.setColor(obj, value)

        for i in list(range(3)):
            cmds.optionVar(fv=(kColors[name][i], value[i]))

    def allViews(self):
        """Description
        """
        state = True if self.sender().isChecked() else False
        cmds.optionVar(iv=("ziAView", state))
        cmds.refresh()

    def addItems(self):

        items = self.getItems()

        for sel in self.getSelMeshes():

            if sel in items:
                continue

            item = QtWidgets.QTreeWidgetItem([sel])
            self.tree.addTopLevelItem(item)

        self.updateSet()

    def reloadSet(self):
        """Description
        """
        attr = "zisetnode"

        for node in cmds.ls(typ="objectSet"):

            if cmds.attributeQuery(attr, ex=True, node=node):
                for member in cmds.sets(node, q=True) or []:
                    item = QtWidgets.QTreeWidgetItem([member])
                    self.tree.addTopLevelItem(item)

    def removeItems(self):
        """Description
        """
        # -- get rid of selected item mesh
        for item in self.tree.selectedItems():
            index = self.tree.indexFromItem(item).row()
            self.tree.takeTopLevelItem(index)
            self.clearGeoAttributes(item.text(0))

        self.updateSet()

    def clearItems(self):
        list(map(lambda item: self.clearGeoAttributes(item), self.getItems()))

        self.tree.clear()
        self.updateSet()

    def updateSet(self):
        """Description
        """
        itemsNames = self.getItems()
        msg = self.tree.setHeaderLabel
        amount = itemsNames.__len__()
        token = "Meshes" if amount > 1 else "Mesh"

        if itemsNames:
            setName = self.createSet()
            self.populateSet(setName, itemsNames)
            msg("FX applied on {} {}".format(amount, token))

        else:
            if cmds.objExists("ziSet"):
                cmds.delete("ziSet")
                msg("FX applied on Selected Mesh")

        cmds.refresh()

    def populateSet(self, setname, itemsNames):
        """Description
        """
        cmds.sets(edit=True, clear=setname)

        for item in itemsNames:
            cmds.sets(item, edit=True, forceElement=setname)

        self.tree.setHeaderLabel("Meshes Display")

    def createSet(self):
        """Description
        """
        attr = "zisetnode"
        setname = ""

        for node in cmds.ls(typ="objectSet"):
            if cmds.attributeQuery(attr, ex=True, node=node):
                setname = node
                break

        if not setname:
            setname = cmds.createNode("objectSet", n="ziSet")

        if not cmds.attributeQuery(attr, ex=True, node=setname):
            cmds.addAttr(setname, shortName="zsn", longName=attr)

        return setname

    def reset(self):
        """Description
        """
        self.setWidgetcolor("Surface Color", [0.014, 0.014, 0.17])
        self.setWidgetcolor("Backface Color", [0.17, 0.014, 0.014])
        self.setWidgetcolor("Line Color", [0.005, 0.005, 0.01])
        self.setWidgetcolor("Point Color", [0.61, 0.61, 0.13])

        self.setWidgetLine("Depth Priority", 990.0)
        self.setWidgetLine("Surface Alpha", 0.5)
        self.setWidgetLine("Line Width", 2.0)
        self.setWidgetLine("Point Size", 5)
        self.setWidgetLine("Mesh Display Limit", 150000)

        self.setWidgetCheck("Backface Culling", True)
        self.setWidgetCheck("Backface Colour", False)
        self.setWidgetCheck("Force Refresh", True)

        for geo in self.shapeToProcess():

            if not cmds.objExists(geo):
                continue

            self.findWidget("Backface Culling", "_check").setChecked(True)
            cmds.setAttr("%s.backfaceCulling" % geo, 3)

            self.findWidget("Override Shading", "_check").setChecked(False)
            cmds.setAttr("%s.overrideShading" % geo, False)
            cmds.setAttr("%s.overrideEnabled" % geo, True)

        cmds.refresh(cv=True, f=True)

    def setCheck(self):
        """Description
        """
        geos = self.shapeToProcess()

        if not geos:
            return

        checked = self.sender().isChecked()

        for geo in geos:

            if "Shading" in self.sender().objectName():
                attr = "%s.overrideEnabled" % geo
                cmds.setAttr(attr, 1)

                attr = "%s.overrideShading" % geo
                cmds.setAttr(attr, checked)

            if "culling" in self.sender().objectName().lower():
                cmds.optionVar(iv=("ziCutBackf", checked))
                attr = "%s.backfaceCulling" % geo

                bfState = 3 if checked else 0
                cmds.setAttr(attr, bfState)

            if "refresh" in self.sender().objectName().lower():
                cmds.optionVar(iv=("ziCutUpdate", checked))

            if "colour" in self.sender().objectName().lower():
                cmds.optionVar(iv=("ziCutBackfc", checked))

        cmds.refresh(cv=True, f=True)

    def defineColor(self):
        """Description
        """
        sender = self.sender()
        colors = self.getColor(sender)
        self.setColor(sender, colors)

        name = sender.objectName().split("_")

        for i in list(range(3)):
            cmds.optionVar(fv=(kColors[name[0]][i], colors[i]))

        cmds.refresh(cv=True, f=True)

    def getColor(self, widget):
        """Description
        """
        butColor = self.butColor(widget)
        color = QtWidgets.QColorDialog().getColor(butColor)

        if not color.isValid():
            color = butColor

        r, g, b, a = color.getRgbF()
        return (r, g, b)

    def setColor(self, widget, colors):
        """Description

        :Param  colors:
        :Type  colors:
        """
        # pow(x , 1/2.2)
        widget.setColor(list(map(lambda x: x * 255, colors)))
        cmds.refresh(cv=True, f=True)

    def butColor(self, widget):
        """Description

        :Param widget:
        :Type widget:
        """
        color = widget.color
        return QtGui.QColor(*color)

    def slid2Line(self):
        """Description
        """
        target = self.sender().objectName().split("_")
        value = float(self.sender().value()) / kIncrement
        self.findWidget(target[0], "_line").setText(str(value))

        cmds.optionVar(fv=(kDoubles[target[0]], value))
        cmds.refresh(cv=True, f=True)

    def line2Slid(self):
        """Description
        """
        target = self.sender().objectName().split("_")
        value = float(self.sender().text()) * kIncrement
        self.findWidget(target[0], "_slider").setValue(value)

    def createTitle(self, mainLayout, txt):
        """Description

        :Param txt:
        :Type txt:
        """
        title = QtWidgets.QLabel(txt.title())
        title.setMinimumHeight(20)
        title.setAlignment(QtCore.Qt.AlignCenter)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(title)
        mainLayout.addLayout(hlayout)

    def createButton(self, mainlayout, layout, label, func, checkable=False):
        """Description

        :Param layout:
        :Type layout:

        :Param label:
        :Type label:

        :Param  func:
        :Type  func:
        """
        butt = QtWidgets.QPushButton(label.title())
        butt.setMinimumHeight(20)

        layout.addWidget(butt)

        if mainlayout:
            mainlayout.addLayout(layout)

        butt.clicked.connect(func)

        if checkable:
            butt.setCheckable(True)

    def createLabel(self, txt):
        """Description

        :Param txt:
        :Type txt:
        """
        label = QtWidgets.QLabel(txt.title())
        label.setFixedWidth(100)
        label.setAlignment(QtCore.Qt.AlignRight)
        label.setObjectName("%s_label" % txt)

        return label

    def createColor(self, txt):
        """Description

        :Param  txt:
        :Type  txt:
        """
        color = ColorButt()
        color.setObjectName("%s_color" % txt)

        color.setMaximumWidth(80)
        color.setMinimumHeight(18)
        color.setTxt(txt)

        return color

    def createSlider(self, txt):
        """Description

        :Param txt:
        :Type txt:
        """
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setObjectName("%s_slider" % txt)

        if txt == "Surface Alpha":
            slider.setMaximum(1.0 * kIncrement)

        if txt == "Line Width":
            slider.setMaximum(6.0 * kIncrement)

        if txt == "Depth Priority":
            slider.setMaximum(2000 * kIncrement)

        if txt == "Split Threshold":
            slider.setMaximum(0.4 * kIncrement)

        if txt == "Angle Limit":
            slider.setMaximum(200 * kIncrement)

        if txt == "Point Size":
            slider.setMaximum(20 * kIncrement)

        if txt == "Mesh Display Limit":
            slider.setMaximum(500000 * kIncrement)

        return slider

    def createCheckBox(self, txt):
        """Description

        :Param  txt:
        :Type  txt:
        """
        box = QtWidgets.QCheckBox("")
        box.setObjectName("%s_check" % txt)

        return box

    def createLine(self, txt):
        """Description
        """
        line = QtWidgets.QLineEdit("-0")
        line.setMaximumWidth(60)
        line.setObjectName("%s_line" % txt)

        return line

    def setVar(self, widget, typ, name):
        """Description

        :Param  name:
        :Type  name:
        """
        func = None

        if typ == str:
            func = widget.setText

        if typ == float:
            func = widget.setValue

        if "Point Size" in name:
            func(typ(self.var.pointSize * kIncrement))

        if "Surface Alpha" in name:
            func(typ(self.var.surfaceAlpha * kIncrement))

        if "Line Width" in name:
            func(typ(self.var.lineWidth * kIncrement))

        if "Depth Priority" in name:
            func(typ(self.var.depth * kIncrement))

        if "Split Threshold" in name:
            func(typ(self.var.spiltT * kIncrement))

        if "Angle Limit" in name:
            func(typ(self.var.angleL * kIncrement))

        if "Mesh Display Limit" in name:
            func(typ(self.var.dispLimit * kIncrement))

    def findWidget(self, name, suffix):
        """Description
        """
        reg = QtCore.QRegExp(r'%s%s' % (name, suffix))
        widget = self.findChildren(QtWidgets.QWidget, reg)

        return widget[0] or None

    def createSeparator(self, layout):
        """Description
        """
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line)

    def createSplitter(self, layout):
        """Description
        """
        splitter = QtWidgets.QSplitter()
        layout.addWidget(splitter)

    def shapeToProcess(self):

        out = []
        items = self.getItems()

        if not items:
            out = [self.var.meshName]

        else:
            for item in items:
                shapes = cmds.listRelatives(item, shapes=True)
                if shapes:
                    out.append(shapes[0])

        return out

    def isMesh(self, unknown=None):

        currentMesh = self.var.meshName

        if not currentMesh and not unknown:
            return False

        if unknown:
            currentMesh = unknown

        if cmds.nodeType(currentMesh) == "objectSet":
            return False

        shapes = cmds.listRelatives(currentMesh, shapes=True)

        if not shapes:
            return False

        if cmds.nodeType(shapes[0]) == "mesh":
            return True

        return False

    def getItems(self):

        out = []
        for x in list(range(self.tree.topLevelItemCount())):
            out.append(self.tree.topLevelItem(x).text(0))

        return out

    def getSelMeshes(self):
        """Description
        """
        out = []

        # -- get rid of selected scene mesh
        for sel in cmds.ls(sl=True, o=True):

            if self.isMesh(sel):
                out.append(sel)

        return out

    def lineStyle(self, value):
        """Description
        """
        cmds.optionVar(iv=["ziCutContinuity", value])
        cmds.refresh()

    def clearGeoAttributes(self, meshTransform):
        """Change display attributes on the shape

        :Param meshTransform(str): could be shape or a transform
        :Return (None): desc.
        """
        shapes =[]

        if not cmds.nodeType(meshTransform) == "mesh":
            shapes = cmds.listRelatives(meshTransform, shapes=True)

        else:
            shapes = [meshTransform]

        if shapes:
            cmds.setAttr("%s.backfaceCulling" % shapes[0], 3)
            cmds.setAttr("%s.overrideShading" % shapes[0], True)
            cmds.setAttr("%s.overrideEnabled" % shapes[0], False)

    def updateSelection(self):
        """No script job for now, can be quite consuming
        """
        sels = cmds.ls(sl=True, o=True)

        if not sels:
            return

        shapes = cmds.listRelatives(sels[0], shapes=True)

        if shapes:

            if cmds.nodeType(shapes[0]) == "mesh":
                value = cmds.getAttr("%s.overrideShading" % shapes[0])
                self.findWidget("Override Shading", "_check").setChecked(value)

                value = cmds.getAttr("%s.backfaceCulling" % self.shapes[0])
                value = True if value == 3 else False

                self.findWidget("Backface Culling", "_check").setChecked(value)

    def setWinLayout(self):
        """Description
        """
        self.mainWin = self
        self.mainWin.setObjectName("ziWireframe")

        wid = QtWidgets.QScrollArea(self.mainWin)

        wid.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        wid.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        wid.setWidgetResizable(True)

        mLayout = QtWidgets.QVBoxLayout(wid)

        self.createSeparator(mLayout)

        self.ziUnlock = ZiUnlockSlider("ON", "OFF", "VIEWPORT")
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.ziUnlock)
        mLayout.addLayout(hlayout)

        self.createSeparator(mLayout)

        for label in kColors.keys():

            widgets = []
            hlayout = QtWidgets.QHBoxLayout()

            widgets.append(self.createLabel(label))
            widgets.append(self.createColor(label))

            for widget in widgets:
                hlayout.addWidget(widget)
                mLayout.addLayout(hlayout)

        self.createSeparator(mLayout)

        self.createTitle(mLayout, "Wireframe Properties")

        for label in kDoublesWire.keys():

            widgets = []
            hlayout = QtWidgets.QHBoxLayout()

            widgets.append(self.createLabel(label))
            widgets.append(self.createLine(label))
            widgets.append(self.createSlider(label))

            for widget in widgets:
                hlayout.addWidget(widget)
                mLayout.addLayout(hlayout)

        hlay = QtWidgets.QHBoxLayout()
        lineLab = QtWidgets.QLabel("Line Style ")
        lineslid = QtWidgets.QSlider()
        lineslid.setMaximum(19)
        lineslid.setOrientation(QtCore.Qt.Horizontal)

        hlay.addWidget(lineLab)
        hlay.addWidget(lineslid)

        lineslid.valueChanged.connect(self.lineStyle)

        mLayout.addLayout(hlay)

        self.createSeparator(mLayout)

        for label in kChecks:

            widgets = []
            hlayout = QtWidgets.QHBoxLayout()

            widgets.append(self.createLabel(label))
            widgets.append(self.createCheckBox(label))

            for widget in widgets:
                hlayout.addWidget(widget)
                mLayout.addLayout(hlayout)

        self.createButton(mLayout,
                          mLayout,
                          "all views display",
                          self.allViews,
                          1)

        self.createSeparator(mLayout)

        # # # # # # # # # # # # # # # # # # # #
        # # # # # # # # # # # # # # # # # # # #

        treeFrame = QtWidgets.QFrame()
        treeFrame.setMinimumHeight(50)
        treeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.tree = QtWidgets.QTreeWidget(treeFrame)
        self.tree.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tree.setHeaderLabel("Meshes Display")

        # self.tree = QtWidgets.QAbstractScrollArea(treeFrame)
        # self.tree.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # self.tree.setHeaderLabel("Meshes Display")

        Vlayout = QtWidgets.QVBoxLayout(treeFrame)
        Vlayout.addWidget(self.tree)
        Vlayout.setContentsMargins(1,1,1,1)

        hlayoutTree = QtWidgets.QHBoxLayout()
        self.createButton(None, hlayoutTree, "add", self.addItems)
        self.createButton(None, hlayoutTree, "remove", self.removeItems)
        self.createButton(None, hlayoutTree, "clear", self.clearItems)

        Vlayout.addLayout(hlayoutTree)
        mLayout.addWidget(treeFrame)

        hlayout = QtWidgets.QHBoxLayout()
        self.createButton(mLayout, hlayout, "reset", self.reset)

        wid.setLayout(mLayout)
        self.mainWin.setCentralWidget(wid)


class ZiUnlockSlider(QtWidgets.QWidget, QtCore.QObject):
    """Display a iphone's slider like
    """

    try:
        changedValue = QtCore.Signal(str)
    except:
        changedValue = QtCore.Signal(str)

    def __init__(self, text1='ON', text2='OFF', text3='', parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMouseTracking(True)
        self.cur = self.cursor()

        self.textValue = text1
        self.textL = text1
        self.textR = text2
        self.textM = text3

        self.position = QtCore.QPointF()
        self.height = 20

        self.buttGrad = QtGui.QLinearGradient()
        self.textGrad = QtGui.QLinearGradient()
        self.backgGrad = QtGui.QLinearGradient()

        self.colorR = QtGui.QColor(190, 190, 190, 205)
        self.colorL = QtGui.QColor(60, 60, 60, 205)
        self.poly = QtGui.QPolygonF()

        self.setMinimumHeight(self.height)
        self.hover = False

    @property
    def value(self):
        return self.textValue

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:

            # -- pixmap.contains added
            if self.buttPath.contains(event.pos()):
                self.setCursor(QtCore.Qt.PointingHandCursor)
                event.accept()

    def mouseMoveEvent(self, event):

        self.hover = False

        if event.buttons() == QtCore.Qt.LeftButton:
            self.position = event.pos()

        self.update()

    def mouseReleaseEvent(self, event):

        # -- left
        if self.position.x() > self.size().width() * .5:
            self.position = QtCore.QPoint(self.size().width(), 0)
            self.colorL = QtGui.QColor(190, 190, 190, 205)
            self.colorR = QtGui.QColor(60, 60, 60, 205)

            self.textValue = self.textL
            self.changedValue.emit(self.textL)

        # -- right
        else:
            self.colorR = QtGui.QColor(190, 190, 190, 205)
            self.colorL = QtGui.QColor(60, 60, 60, 205)

            self.textValue = self.textR
            self.changedValue.emit(self.textR)

            self.position = QtCore.QPoint(0, 0)

        self.setCursor(self.cur)
        self.update()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)

        buttsize = self.size().width() * .5

        self.buttPath = QtGui.QPainterPath()
        circlePath = QtGui.QPainterPath()
        textMPath = QtGui.QPainterPath()
        textPath = QtGui.QPainterPath()
        backPath = QtGui.QPainterPath()

        buttpos = self.position.x() - (buttsize * .5)

        # -- clamping values, so the button does not go outside the boundaries
        if buttpos < 0:
            buttpos = 0

        if buttpos > self.size().width() - buttsize:
            buttpos = self.size().width() - buttsize

        # -- background
        backPath.addRoundedRect(QtCore.QRectF(
            0, 0, self.size().width(), self.height), 3, 3)

        self.backgGrad.setColorAt(0.00, QtGui.QColor(20, 20, 20, 205))
        self.backgGrad.setColorAt(0.45, QtGui.QColor(25, 25, 25, 205))
        self.backgGrad.setColorAt(0.5, QtGui.QColor(10, 10, 10, 205))
        self.backgGrad.setColorAt(1.0, QtGui.QColor(35, 35, 35, 205))
        self.backgGrad.setStart(QtCore.QPointF(0, 0))
        self.backgGrad.setFinalStop(QtCore.QPointF(0, self.height))

        painter.setBrush(self.backgGrad)
        painter.setPen(QtGui.QPen(QtGui.QColor(20, 20, 20, 255)))
        painter.drawPath(backPath)

        # -- texts
        font = QtGui.QFont('Lato', self.height * .5)
        textPath.addText(QtCore.QPointF(len(self.textL) * self.size().width() * .1,
                                        self.height * .75),
                         font,
                         self.textL)

        textPath.addText(QtCore.QPointF(len(self.textR) * self.size().width() * .23,
                                        self.height * .75),
                         font,
                         self.textR)

        self.textGrad.setStart(QtCore.QPointF(0, 0))
        self.textGrad.setFinalStop(QtCore.QPointF(buttsize * 2, 0))

        self.textGrad.setColorAt(0.48, self.colorL)
        self.textGrad.setColorAt(0.50, QtGui.QColor(80, 80, 80, 255))  # -- mid
        self.textGrad.setColorAt(0.52, self.colorR)  # -- right

        painter.setBrush(self.textGrad)
        painter.setPen(QtGui.QPen(self.textGrad, 0))
        painter.drawPath(textPath)

        # -- circle
        painter.setBrush(self.backgGrad)
        painter.setPen(QtGui.QPen(self.backgGrad, 0))

        # -- butt
        baseColor = QtGui.QColor(128, 129, 138, 255)
        self.buttGrad.setColorAt(0.00, baseColor.lighter(40))
        self.buttGrad.setColorAt(0.45, baseColor.lighter(45))
        self.buttGrad.setColorAt(0.50, baseColor.lighter(30))
        self.buttGrad.setColorAt(1.00, baseColor.lighter(55))
        self.buttGrad.setStart(QtCore.QPointF(0, 0))
        self.buttGrad.setFinalStop(QtCore.QPointF(0, self.height))

        self.buttPath.addRoundedRect(QtCore.QRectF(0, 0, buttsize,
                                                   self.height), 3, 3)

        self.buttPath.translate(buttpos, 0)

        painter.setBrush(self.buttGrad)
        painter.setPen(QtGui.QPen(QtGui.QColor(20, 20, 20, 255)))
        painter.drawPath(self.buttPath)

        # -- if mouse over the button
        if self.hover:
            hoverGrad = QtGui.QRadialGradient(
                QtCore.QPointF(buttpos + (buttsize * .5), self.height * .5),
                self.height * .7)

            hoverGrad.setColorAt(.81, QtGui.QColor(170, 170, 170, 255))
            hoverGrad.setColorAt(1, QtGui.QColor(160, 160, 160, 255))

            painter.setBrush(hoverGrad)
            painter.setPen(QtGui.QPen(hoverGrad, 1))

        else:
            painter.setBrush(self.backgGrad)
            painter.setPen(QtGui.QPen(self.backgGrad, 1))

        # -- circle
        if not self.textM:
            circlePath.addEllipse(QtCore.QPointF(buttpos + (buttsize * .5),
                                                 self.height * .5),
                                  self.height * .4,
                                  self.height * .4)

            painter.drawPath(circlePath)

        # -- specified text
        if self.textM:
            textMPath.addText(QtCore.QPointF(0, 0), font, self.textM)
            bound = textMPath.boundingRect()

            textMPath.translate(
                buttpos + (buttsize * .5) - (bound.right() * .5),
                self.height * .75)

            painter.drawPath(textMPath)



class ColorButt(QtWidgets.QWidget, QtCore.QObject):

    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMouseTracking(True)

        self._color = [0, 0, 0]
        self.hover = False

        self._text = ""
        self._darkness = 90

        # self.setMinimumSize(75, 12)

    def mouseMoveEvent(self, event):

        if not QtCore.QRect(self.width() * .25,
                            self.height() * .25,
                            self.width() * .5,
                            self.height() * .5).contains(event.pos()):

            self.hover = False

        else:
            self.hover = True

        self.update()
        return True

    def setColor(self, color):
        self._color = color
        self.update()

    @property
    def color(self):
        return self._color

    def setTxt(self, text, darkness=70):
        self._text = text
        self._darkness = darkness

    @property
    def text(self):

        if int(cmds.about(version=True)) < 2020:
            return str(self._text)

        return self._text

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        # -- convert to 2.2 gammma
        color = QtGui.QColor(pow(self._color[0] / float(255), .454545) * 255,
                             pow(self._color[1] / float(255), .454545) * 255,
                             pow(self._color[2] / float(255), .454545) * 255)

        if self.hover:
            color = color.lighter(150)

        painter.setBrush(QtGui.QBrush(color))
        painter.setPen(color.darker(self._darkness))

        painter.drawRoundedRect(0, 0, self.width(), self.height(), 2, 2)
        painter.drawText(QtCore.QRectF(0, 0, self.width(),
                                       self.height()),
                         QtCore.Qt.AlignCenter, self.text)

        painter.end()


def console(*txt):
    """Description
    """
    if not DEBUG:
        return

    txt = list(map(str, txt))
    print("ziCutDebug{:_>20}".format(' '.join(txt)))


def main(dockable=True, show=True):

    global ziWireframeObj

    try:
        controlName = ziWireframeObj.objectName()+"WorkspaceControl"
        if cmds.workspaceControl(controlName, q=True, ex=True):
            cmds.deleteUI(controlName, control=True)

        ziWireframeObj.deleteLater()

    except:
        pass

    ziWireframeObj = Win(dockable, show)

    return ziWireframeObj

# -- Vtx python version 3
