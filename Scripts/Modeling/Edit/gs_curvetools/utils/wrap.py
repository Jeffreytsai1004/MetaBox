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

import re
from functools import partial as pa
from imp import reload

import maya.cmds as mc
import maya.OpenMayaUI as omui
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance

from . import style, tooltips, utils

TOOLTIPS_DICT = tooltips.processTooltips()

reload(utils)
reload(style)
reload(tooltips)

# Holds the names and pointers to all controls
try:
    bool(WIDGETS)  # type: ignore # pylint: disable=used-before-assignment
except BaseException:
    WIDGETS = {}


def getUniqueName(name):
    from ..main import MAIN_WINDOW_NAME
    return (MAIN_WINDOW_NAME + "_" + name)


def wrapControl(name):
    name = omui.MQtUtil.findControl(name)
    return wrapInstance(int(name), QtWidgets.QWidget)


def separator():
    name = omui.MQtUtil.findControl(mc.separator(st='in'))
    return wrapInstance(int(name), QtWidgets.QWidget)

# Layouts


class Layout(QtWidgets.QWidget):

    def __init__(self, parent, objName='', spacing=2,
                 margin=0, margins=[0, 0, 0, 0], vis=True):
        super(Layout, self).__init__()
        if objName:
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        self.__parent = parent
        self.__spacing = spacing
        self.__margin = margin
        self.__margins = margins
        self.__visibility = vis

    def __enter__(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(*self.__margins)
        layout.setMargin(self.__margin)
        layout.setSpacing(self.__spacing)
        layout.addWidget(self)
        self.setVisible(self.__visibility)
        return self

    def __exit__(self, *_):
        self.__parent.addWidget(self)


class Row(QtWidgets.QWidget):

    def __init__(self, parent, objName='', spacing=2, margins=[0, 0, 0, 0]):
        super(Row, self).__init__()
        if objName:
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.__parent = parent
        self.__spacing = spacing
        self.__margins = margins

    def __enter__(self):
        row = QtWidgets.QHBoxLayout(self)
        row.setSpacing(self.__spacing)
        row.setContentsMargins(*self.__margins)
        return self

    def __exit__(self, *_):
        self.__parent.addWidget(self)


class Column(QtWidgets.QWidget):

    def __init__(self, parent, objName='', spacing=2, margins=[0, 0, 0, 0]):
        super(Column, self).__init__()
        if objName:
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        self.__parent = parent
        self.__spacing = spacing
        self.__margins = margins

    def __enter__(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(self.__spacing)
        layout.setContentsMargins(*self.__margins)
        return self

    def __exit__(self, *_):
        self.__parent.addWidget(self)


class Frame(QtWidgets.QFrame):

    def __init__(self, parent, objName='', label=None, spacing=2, margins=[0, 0, 0, 0]):
        super(Frame, self).__init__()

        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.setAutoFillBackground(True)
        self.setGeometry(0, 0, 0, 0)

        self.mainParent = parent
        self.frameSpacing = style.scale(spacing)
        self.frameMargins = style.scale(margins)
        self.frameLabel = label

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setSpacing(self.frameSpacing)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def eventFilter(self, object, event):
        if object is not self.frameButton and event.type() == QtCore.QEvent.ToolTip:
            self.enableTooltip(False)
        elif object is self.frameButton and event.type() == QtCore.QEvent.ToolTip:
            self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))
        return super(Frame, self).eventFilter(object, event)

    def __enter__(self):
        # Layout Button
        self.frameButton = Button(self.layout())
        if self.frameLabel:
            self.frameButton.setLabel(self.frameLabel)
        self.setCollapsible(True)
        self.frameButton.clicked.connect(pa(self.toggleCollapsed))

        # Main Frame for Contents
        self.frameWidget = QtWidgets.QWidget()
        self.frameWidget.setContentsMargins(*self.frameMargins)
        self.frameLayout = QtWidgets.QVBoxLayout(self.frameWidget)
        self.frameLayout.setSpacing(self.frameSpacing)
        self.frameLayout.setContentsMargins(*self.frameMargins)
        self.frameWidget.installEventFilter(self)
        self.frameButton.installEventFilter(self)

        self.frameWidget.setHidden(True)
        self.layout().addWidget(self.frameWidget)
        return self

    def __exit__(self, *_):
        self.mainParent.addWidget(self)

    def getFrameLayout(self):
        return self.frameLayout

    def setCollapsed(self, hidden=False):
        self.frameWidget.setHidden(hidden)
        self.frameButton.setChecked(not hidden)

    def toggleCollapsed(self):
        palette = QtGui.QPalette()
        if self.frameWidget.isVisible():
            self.setFrameStyle(self.NoFrame)
            color = QtGui.QColor(0, 0, 0, 0)
            palette.setColor(QtGui.QPalette.Background, color)
            self.setPalette(palette)
            self.frameWidget.setHidden(True)
            self.frameButton.setChecked(False)
        else:
            self.setFrameStyle(self.Panel | self.Sunken)
            color = QtGui.QColor(0, 0, 0, 30)
            palette.setColor(QtGui.QPalette.Background, color)
            self.setPalette(palette)
            self.frameWidget.setHidden(False)
            self.frameButton.setChecked(True)

    def setCollapsible(self, collapsible):
        if collapsible:
            self.frameButton.setButtonStyle('frame-button')
            self.frameButton.setCheckable(True)
            self.frameButton.setChecked(False)
            self.frameButton.blockSignals(False)
        else:
            self.frameButton.setButtonStyle('frame-button-not-collapsible')
            self.setCollapsed(False)
            self.frameButton.setCheckable(False)
            self.frameButton.setChecked(False)
            self.frameButton.blockSignals(True)

# Menu Items:


class Menu:

    def __init__(self, label, parent, tearable=True, collapsible=False):
        self.label = label
        self.parent = parent
        self.tearable = tearable
        self.collapsible = collapsible

    def __enter__(self):
        self.menu = QtWidgets.QMenu(self.label)
        self.menu.setToolTipsVisible(True)
        self.menu.setTearOffEnabled(self.tearable)
        self.menu.setSeparatorsCollapsible(self.collapsible)
        return self.menu

    def __exit__(self, *_):
        self.parent.addMenu(self.menu)


class ActionGroup:

    def __init__(self, objName, parent):
        self.objName = objName
        self.parent = parent

    def __enter__(self):
        self.group = QtWidgets.QActionGroup(self.parent)
        if self.objName:
            self.group.setObjectName(getUniqueName(self.objName))
            WIDGETS[self.objName] = self.group
        return self.group

    def __exit__(self, *_):
        pass


class MenuItem(QtWidgets.QAction):

    def __init__(self, objName, label, parent, checkable=False, checked=False, collection=None):
        super(MenuItem, self).__init__(label, parent)
        self.objName = objName
        self.setCheckable(checkable)
        if checked:
            self.setChecked(checked)
        if self.objName:
            self.setObjectName(getUniqueName(self.objName))
            WIDGETS[self.objName] = self
        if collection:
            self.setActionGroup(collection)
        parent.addAction(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')


def mayaSlider(slider, objName='', layout=None):  # TODO: Need to refactor these function to use one class for wrapping
    slider = wrapInstance(int(omui.MQtUtil.findControl(slider)), QtWidgets.QWidget)
    if objName:
        slider.setObjectName(getUniqueName(objName))
        WIDGETS[objName] = slider
    if layout:
        layout.addWidget(slider)
    return slider


# Buttons

class Button(QtWidgets.QPushButton):  # Maybe change back to the mode without inheritance
    """ Creates a normal button """
    markingPixmap = QtGui.QPixmap(utils.getFolder.icons() + 'marking.png')
    modPixmap = QtGui.QPixmap(utils.getFolder.icons() + 'mod.png')
    resetPixmap = QtGui.QPixmap(utils.getFolder.icons() + 'reset.png')

    def __init__(self, layout=None, objName=''):
        super(Button, self).__init__()
        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        self.buttonStyle = ''
        self.buttonState = 0
        self.buttonLabels = None

        if layout:
            layout.addWidget(self)

        self.setButtonStyle()

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def setLabel(self, text, margins=[0, 0, 0, 0], lineHeight=80):
        text = self._formatText(text, lineHeight=lineHeight)

        self.label = QtWidgets.QLabel(text, self)

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(*style.scale(margins))
        layout.addWidget(self.label)
        self.setLabelStyle()

    def setLabelStyle(self, labelStyle='normal'):
        self.font = QtGui.QFont('Roboto')
        self.label.setFont(self.font)
        if labelStyle == 'normal':
            self.setFontSize(11)
        elif labelStyle == 'small':
            self.setFontSize(10, False)

    def setButtonStyle(self, buttonStyle='normal'):
        if buttonStyle == 'normal':
            self.setStyleSheet(style.buttonNormal)
            self.buttonStyle = 'normal'
        elif buttonStyle == 'active-orange':
            self.setStyleSheet(style.buttonActiveOrange)
            self.buttonStyle = 'active-orange'
        elif buttonStyle == 'active-blue':
            self.setStyleSheet(style.buttonActiveBlue)
            self.buttonStyle = 'active-blue'
        elif buttonStyle == 'active-white':
            self.setStyleSheet(style.buttonActiveWhite)
            self.buttonStyle = 'active-white'
        elif buttonStyle == 'small':
            self.setStyleSheet(style.smallNormal)
            self.buttonStyle = 'small'
        elif buttonStyle == 'small-filled':
            self.setStyleSheet(style.smallFilled)
            self.buttonStyle = 'small-filled'
        elif buttonStyle == 'small-no-border':
            self.setStyleSheet(style.smallNoBorder)
            self.buttonStyle = 'small-no-border'
        elif buttonStyle == 'slider-label':
            self.setStyleSheet(style.sliderLabel)
            self.buttonStyle = 'slider-label'
        elif buttonStyle == 'icon':
            self.setStyleSheet(style.buttonIcon)
            self.buttonStyle = 'icon-button'
        elif buttonStyle == 'frame-button':
            self.setStyleSheet(style.frameButton)
            self.buttonStyle = 'frame-button'
        elif buttonStyle == 'frame-button-not-collapsible':
            self.setStyleSheet(style.frameButtonNotCollapsable)
            self.buttonStyle = 'frame-button-not-collapsible'
        elif buttonStyle == 'small-compound-top-left':
            self.setStyleSheet(style.smallCompoundTopLeft)
            self.buttonStyle = 'small-compound-top-left'
        elif buttonStyle == 'small-compound-top-right':
            self.setStyleSheet(style.smallCompoundTopRight)
            self.buttonStyle = 'small-compound-top-right'
        elif buttonStyle == 'small-filled-compound-bottom':
            self.setStyleSheet(style.smallFilledCompoundBottom)
            self.buttonStyle = 'small-filled-compound-bottom'

    def setIcon(self, icoType):
        iconMod = self.modPixmap
        iconMarking = self.markingPixmap
        self.modLabelMod = QtWidgets.QLabel(self)
        self.modLabelMarking = QtWidgets.QLabel(self)

        mult = 7
        iconMod = iconMod.scaled(style.scale(mult), style.scale(mult), QtCore.Qt.KeepAspectRatio)
        self.modLabelMod.setContentsMargins(*style.scale([2, 2, 0, 0]))
        self.modLabelMod.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.modLabelMod.setPixmap(iconMod)
        self.modLabelMod.setVisible(False)

        iconMarking = iconMarking.scaled(style.scale(mult), style.scale(mult), QtCore.Qt.KeepAspectRatio)
        self.modLabelMarking.setContentsMargins(*style.scale([2, 2, 0, 0]))
        self.modLabelMarking.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.modLabelMarking.setPixmap(iconMarking)
        self.modLabelMarking.setVisible(False)

        if icoType == 'marking-top':
            self.modLabelMarking.setVisible(True)
        elif icoType == 'marking-bottom':
            self.modLabelMarking.setVisible(True)
            self.modLabelMarking.move(*style.scale([0, 16]))
        elif icoType == 'mod-top':
            self.modLabelMod.setVisible(True)
        elif icoType == 'mod-bottom':
            self.modLabelMod.setVisible(True)
            self.modLabelMod.move(*style.scale([0, 17]))
        elif icoType == 'both':
            self.modLabelMod.setVisible(True)
            self.modLabelMarking.setVisible(True)
            self.modLabelMarking.move(*style.scale([1, 13]))
        elif icoType == 'reset':
            iconReset = self.resetPixmap
            iconReset = iconReset.scaled(style.scale(11), style.scale(11), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            super(Button, self).setIcon(iconReset)
        else:
            self.modLabelMod.setVisible(False)
            self.modLabelMarking.setVisible(False)

    def changeIcon(self, icoType):
        if icoType == 'marking':
            self.modLabel.setPixmap(self.markingPixmap)
        elif icoType == 'mod-top':
            self.modLabel.setPixmap(self.modPixmap)
        else:
            self.modLabel.setPixmap(self.markingModPixmap)

    def setIconVisible(self, vis=True):
        self.modLabel.setVisible(vis)

    def setFontSize(self, size, bold=True):
        font = self.label.font()
        font.setPixelSize(style.scale(size))
        if bold:
            font.setBold(bold)
        self.label.setFont(font)

    def setLabelOffset(self, offsetX, offsetY, width=None, height=None):
        if not width:
            width = self.label.geometry().width()
        if not height:
            height = self.label.geometry().height()
        rect = QtCore.QRect(offsetX, offsetY, width, height)
        self.label.setFrameRect(rect)

    def setWidthHeight(self, w=None, h=None):
        if w:
            self.setFixedWidth(style.scale(w))
        if h:
            self.setFixedHeight(style.scale(h))

    def changeText(self, *_):
        rect = self.rect().width()
        _min = style.scale(75)
        _max = style.scale(115)
        if rect < _min and self.buttonState != 0:
            text = self._formatText(self.buttonLabels[0])
            self.label.setText(text)
            self.buttonState = 0
        elif _min <= rect < _max and self.buttonState != 1:
            text = self._formatText(self.buttonLabels[1])
            self.label.setText(text)
            self.buttonState = 1
        elif rect >= _max and self.buttonState != 2 and len(self.buttonLabels) > 2:
            text = self._formatText(self.buttonLabels[2])
            self.label.setText(text)
            self.buttonState = 2

    def setValue(self, value):
        if self.isCheckable():
            self.setChecked(bool(value))

    def addParent(self, parent, stretch=0):
        parent.addWidget(self, stretch)

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def _formatText(self, text, lineHeight=80):
        if lineHeight == 100:
            return text
        if isinstance(text, list):
            self.resizeEvent = self.changeText
            self.buttonLabels = text
            text = text[0]
        text = '<p style="line-height:{1}%;">{0}</p>'.format(text, lineHeight)
        return text


class IconCheckButton(QtWidgets.QPushButton):

    def __init__(self, parent, objName=''):
        super(IconCheckButton, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(style.buttonIcon)
        self.objName = ''
        if objName:
            self.objName = objName
            WIDGETS[objName] = self
            self.setObjectName(getUniqueName(objName))
        self.setCheckable(True)
        self.clicked.connect(self.toggleIcon)
        parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def setChecked(self, checked):
        super(IconCheckButton, self).setChecked(checked)
        self.toggleIcon()

    def setIcons(self, checked, unchecked):
        self.icons = [checked, unchecked]
        self.switchToIcon(0)

    def switchToIcon(self, iconId):
        icon = QtGui.QIcon(self.icons[iconId])
        self.setIcon(icon)

    def setIconWidthHeight(self, w, h):
        self.setFixedSize(QtCore.QSize(style.scale(w), style.scale(h)))
        self.setIconSize(QtCore.QSize(style.scale(w), style.scale(h)))

    def toggleIcon(self):
        if self.isChecked():
            self.switchToIcon(0)
        else:
            self.switchToIcon(1)

# Layers


class Layer(QtWidgets.QPushButton):

    LAYERS = 20

    def __init__(self, objName=None, layout=None):
        super(Layer, self).__init__()

        self.buttonStyle = 'empty'

        self.setMinimumSize(1, 1)
        self.setStyle()

        self.setCheckable(True)

        self.setAcceptDrops(True)

        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        if layout:
            layout.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def setLabel(self, label):
        self.buttonLabel = QtWidgets.QLabel(label, self)
        self.buttonLabel.setStyleSheet(style.layerLabel)
        self.buttonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonLabel.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        buttonLayout = QtWidgets.QHBoxLayout(self)
        buttonLayout.setContentsMargins(0, 0, 0, 0)
        buttonLayout.addWidget(self.buttonLabel)

    def changeLabel(self, text):
        self.buttonLabel.setText(text)

    def setNumberOfLayers(self, num):
        Layer.LAYERS = num

    # Set custom styles
    def setStyle(self, buttonStyle='empty'):
        if self.buttonStyle == 'custom':
            return 0
        if buttonStyle == self.buttonStyle:
            return
        if buttonStyle == 'empty':
            self.setStyleSheet(style.layer('rgba(0,0,0,0)'))
            self.buttonStyle = 'empty'
        elif buttonStyle == 'active':
            self.setStyleSheet(style.layer('#db9456'))
            self.buttonStyle = 'active'
        elif buttonStyle == 'hidden':
            self.setStyleSheet(style.layer('#a1a1a1'))
            self.buttonStyle = 'hidden'
        elif buttonStyle == 'curve':
            self.setStyleSheet(style.layer('#5285a6'))
            self.buttonStyle = 'curve'
        elif buttonStyle == 'geo':
            self.setStyleSheet(style.layer('#25934e'))
            self.buttonStyle = 'geo'
        elif buttonStyle == 'edit':
            self.setStyleSheet(style.layer('\
                qlineargradient(\
                    x1: 0, y1: 0, x2: 1, y2: 1,\
                    stop: 0 #db9456, stop: 0.499 #db9456, stop: 0.501 red,stop: 1 red\
                );'))
            self.buttonStyle = 'edit'

    def colorize(self, isColorized):
        if isColorized:
            self.buttonStyle = 'custom'
        else:
            self.buttonStyle = 'empty'

    def setLayout(self, layout):
        layout.addWidget(self)

    def mousePressEvent(self, event):
        super(Layer, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.MiddleButton:
            drag = QtGui.QDrag(self)
            mimeData = QtCore.QMimeData()
            mimeData.setText(self.objectName())
            drag.setMimeData(mimeData)
            drag.exec_()

    def dragEnterEvent(self, event):
        super(Layer, self).dragEnterEvent(event)
        if event.proposedAction() != QtCore.Qt.MoveAction:
            return
        if event.source().__class__ != Layer:
            return
        event.acceptProposedAction()

    def dropEvent(self, event):
        super(Layer, self).dropEvent(event)
        if event.proposedAction() != QtCore.Qt.MoveAction:
            return
        source = event.source()
        if source != self and source.__class__ == Layer:
            from .. import core
            core.moveLayers(event.mimeData().text(), self.objectName())
            event.acceptProposedAction()

# Sliders


class MayaSlider:

    """ Just a simple wrapper of normal Maya sliders """

    def __init__(self, slider, objName='', layout=None):
        self.slider = wrapInstance(int(omui.MQtUtil.findControl(slider)), QtWidgets.QWidget)
        if objName:
            self.slider.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self.slider
        if layout:
            layout.addWidget(self.slider)


class ControlSlider(QtWidgets.QWidget):

    linkIconTop = QtGui.QPixmap(utils.getFolder.icons() + 'marking.png')
    linkIconBottom = QtGui.QPixmap(utils.getFolder.icons() + 'link_bottom.png')

    def __init__(self, parent=None, objName='', typ='int'):
        super(ControlSlider, self).__init__()

        self.objName = ''
        if objName:
            self.objName = objName
            self.attributeName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.minimum = self.fieldMinimum = 0
        self.maximum = self.fieldMaximum = 0

        self.typ = typ

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.button = Button(self.layout)
        self.button.setButtonStyle('slider-label')
        self.button.setCheckable(True)
        self.button.setAutoFillBackground(True)

        if self.typ == 'int':  # Possibly replace with native sliders for better functionality
            m_slider = mc.intSliderGrp(cw=[(1, 45), (2, 1)], adj=2, f=1)
        else:
            m_slider = mc.floatSliderGrp(cw=[(1, 45), (2, 1)], adj=2, f=1)

        self.slider = wrapInstance(int(omui.MQtUtil.findControl(m_slider)), QtWidgets.QWidget)
        self.layout.addWidget(self.slider)

        self.m_slider = self.slider.objectName()

        if parent:
            parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.button.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.button.setToolTip('')

    def setLabel(self, label):
        self.button.setLabel(label)
        self.button.label.setAlignment(QtCore.Qt.AlignRight)
        self.button.setFixedWidth(style.scale(55))

    def setLabelWidth(self, width):
        self.button.setFixedWidth(style.scale(width))

    def setValue(self, value):
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1, v=value)
        else:
            mc.floatSliderGrp(self.m_slider, e=1, v=value)

    def getValue(self):
        if self.typ == 'int':
            return mc.intSliderGrp(self.m_slider, q=1, v=1)
        else:
            return mc.floatSliderGrp(self.m_slider, q=1, v=1)

    def setDragCommand(self, cmd):
        self.dragCommand = cmd
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1, dc=self.dragCommand)
        else:
            mc.floatSliderGrp(self.m_slider, e=1, dc=self.dragCommand)

    def setReleaseCommand(self, cmd):
        def releaseCommand(*_):
            self.dragCommand()
            cmd()
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1, cc=releaseCommand)
        else:
            mc.floatSliderGrp(self.m_slider, e=1, cc=releaseCommand)

    def getAttributeName(self):
        return self.attributeName

    def setMinMax(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1,
                            min=self.minimum, max=self.maximum,
                            fmn=self.minimum, fmx=self.maximum)
        else:
            mc.floatSliderGrp(self.m_slider, e=1,
                              min=self.minimum, max=self.maximum,
                              fmn=self.minimum, fmx=self.maximum)

    def setFieldMinMax(self, minimum, maximum):
        self.fieldMinimum = minimum
        self.fieldMaximum = maximum
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1, fmn=self.fieldMinimum, fmx=self.fieldMaximum)
        else:
            mc.floatSliderGrp(self.m_slider, e=1, fmn=self.fieldMinimum, fmx=self.fieldMaximum)

    def setPrecision(self, precision):
        if self.typ != 'int':
            mc.floatSliderGrp(self.m_slider, e=1, pre=precision)

    def setStep(self, step):
        if self.typ != 'int':
            mc.floatSliderGrp(self.m_slider, e=1, s=step)

    def resetMinMax(self):
        if self.typ == 'int':
            mc.intSliderGrp(self.m_slider, e=1,
                            fmn=self.fieldMinimum, fmx=self.fieldMaximum,
                            min=self.minimum, max=self.maximum)
        else:
            mc.floatSliderGrp(self.m_slider, e=1,
                              fmn=self.fieldMinimum, fmx=self.fieldMaximum,
                              min=self.minimum, max=self.maximum)

# Falloff curve graph


class FallOffCurve(QtWidgets.QWidget):

    def __init__(self, parent, objName='', attr=True):
        super(FallOffCurve, self).__init__()
        self.objName = objName
        self.attr = attr
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        if self.objName:
            self.setObjectName(getUniqueName(self.objName))
            WIDGETS[self.objName] = self
        if self.attr:
            self.m_graph = mc.falloffCurveAttr(ccw=5, stg=0, h=220, hlc=[0.68, 0.68, 0.68])
        else:
            self.m_graph = mc.falloffCurve(ccw=5, stg=0, h=220, hlc=[0.68, 0.68, 0.68])
        self.graph = wrapInstance(int(omui.MQtUtil.findControl(self.m_graph)), QtWidgets.QWidget)
        self.graph.setStyleSheet('*{background-color:rgba(0,0,0,0);}')
        self.layout.addWidget(self.graph)

        parent.addWidget(self)

    def connectGraph(self, path):
        if self.attr:
            mc.falloffCurveAttr(self.m_graph, e=1, at=path)
        else:
            mc.falloffCurve(self.m_graph, e=1, at=path)

    def changeCommand(self, command):
        if self.attr:
            mc.falloffCurveAttr(self.m_graph, e=1, cc=command)
        else:
            mc.falloffCurve(self.m_graph, e=1, cc=command)

    def getGraph(self):
        if self.attr:
            return mc.falloffCurveAttr(self.m_graph, q=1, asString=1)
        else:
            return mc.falloffCurve(self.m_graph, q=1, asString=1)

    def setGraph(self, string):
        if self.attr:
            mc.falloffCurveAttr(self.m_graph, e=1, asString=string)
        else:
            mc.falloffCurve(self.m_graph, e=1, asString=string)

    def resetGraph(self, custom=None):
        defaults = r"0, 0.5, 0.333, 0.5, 0.667, 0.5, 1, 0.5"
        if custom:
            defaults = custom
        if self.attr:
            mc.falloffCurveAttr(self.m_graph, e=1, asString=defaults)
        else:
            mc.falloffCurve(self.m_graph, e=1, asString=defaults)

# Color picker button


class ColorPicker(QtWidgets.QWidget):

    def __init__(self, objName='', parent=None):
        super(ColorPicker, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.m_colorSlider = mc.colorSliderGrp(objName, rgb=[.5, .5, .5])

        origSlider = wrapInstance(int(omui.MQtUtil.findControl(self.m_colorSlider)), QtWidgets.QWidget)
        self.components = origSlider.children()
        self.colorRect = self.components[1]
        self.layout.addWidget(self.colorRect)
        origSlider.setVisible(False)

        if parent:
            parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def addParent(self, parent, stretch=0):
        parent.addWidget(self, stretch)

    def connectCommand(self, command):
        mc.colorSliderGrp(self.m_colorSlider, e=1, cc=command)

    def connectDragCommand(self, command):
        mc.colorSliderGrp(self.m_colorSlider, e=1, dc=command)

    def resetColors(self):
        mc.colorSliderGrp(self.m_colorSlider, e=1, rgb=[0, 0, 0])

    def setRGBColors(self, clr=[0, 0, 0]):
        mc.colorSliderGrp(self.m_colorSlider, e=1, rgb=clr)

    def getRGBColors(self):
        return mc.colorSliderGrp(self.m_colorSlider, q=1, rgb=1)

    def setHSVColors(self, clr=[0, 0, 0]):
        mc.colorSliderGrp(self.m_colorSlider, e=1, hsv=clr)

    def getHSVColors(self):
        return mc.colorSliderGrp(self.m_colorSlider, q=1, hsv=1)

# Layer selection drop-down menu


class LayerSelector(QtWidgets.QComboBox):

    def __init__(self, objName, parent):
        super(LayerSelector, self).__init__()

        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        symbols = []
        for c in range(ord('a'), ord('j') + 1):
            symbols.append(chr(c).capitalize())
        numbers = [str(i) for i in range(10)]
        numbers2 = [str(i) for i in range(20, 40)]
        numbers3 = [str(i) for i in range(40, 80)]

        self.setContentsMargins(0, 0, 0, 0)
        self.addItems(numbers + symbols + numbers2 + numbers3)

        parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def setCurrentIndex(self, index):
        # Disabling programmatic signal
        self.blockSignals(True)
        super(LayerSelector, self).setCurrentIndex(index)
        self.blockSignals(False)

    def updateLayerList(self):
        self.blockSignals(True)
        from .. import core
        if core.getOption('layerNumbersOnly'):
            for i in range(10, 20):
                self.removeItem(i)
                self.insertItem(i, str(i))
        else:
            letters = [chr(c).capitalize() for c in range(ord('a'), ord('j') + 1)]
            for i in range(10, 20):
                self.removeItem(i)
                self.insertItem(i, str(letters[i - 10]))
        self.blockSignals(False)

    def wheelEvent(self, event):
        super(LayerSelector, self).wheelEvent(event)


class LayerCollectionWidget(QtWidgets.QComboBox):

    def __init__(self, objName, parent=None):
        super(LayerCollectionWidget, self).__init__()

        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        self.setContentsMargins(0, 0, 0, 0)
        if parent:
            parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def clear(self):
        super(LayerCollectionWidget, self).clear()
        self.addItem("Main")


# Line edit input field


class LineEdit(QtWidgets.QLineEdit):

    def __init__(self, objName, parent=None):
        super(LineEdit, self).__init__()

        self.autoFormat = False

        self.objName = ''
        if objName:
            self.objName = objName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.setContentsMargins(0, 0, 0, 0)

        self.editingFinished.connect(self.formatText)

        if parent:
            parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def setAutoFormat(self, shouldFormat):
        self.autoFormat = shouldFormat

    @utils.deferred
    def formatText(self):
        if self.autoFormat:
            newName = self.text()
            if newName:
                if newName[0].isdigit():
                    newName = newName[1:]
                self.setText(re.sub(r"[^0-9a-zA-Z]+", "_", newName))

# Single float field


class FloatField(QtWidgets.QWidget):

    def __init__(self, objName, parent=None, attrName=''):
        super(FloatField, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.objName = ''
        if objName:
            self.objName = objName
            if not attrName:
                self.attributeName = objName
            else:
                self.attributeName = attrName
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.floatField = mc.floatField(min=-10, max=10, pre=1, step=0.25, v=0)

        wrappedField = wrapInstance(int(omui.MQtUtil.findControl(self.floatField)), QtWidgets.QWidget)
        self.layout.addWidget(wrappedField)

        if parent:
            parent.addWidget(self)

        self.enableTooltip(mc.optionVar(q="GSCT_enableTooltips"))

    def enableTooltip(self, enable):
        if enable and self.objName in TOOLTIPS_DICT:
            self.setToolTip(TOOLTIPS_DICT[self.objName])
        else:
            self.setToolTip('')

    def setDragCommand(self, cmd):
        self.dragCommand = cmd
        mc.floatField(self.floatField, e=1, dc=cmd)

    def setReleaseCommand(self, cmd):
        def releaseCommand(*_):
            self.dragCommand()
            cmd()
        mc.floatField(self.floatField, e=1, cc=releaseCommand)

    def getAttributeName(self):
        return self.attributeName

    def getValue(self):
        return mc.floatField(self.floatField, q=1, v=1)

    def setRange(self, minimum, maximum):
        mc.floatField(self.floatField, e=1, min=minimum, max=maximum)

    def setPrecision(self, pre):
        mc.floatField(self.floatField, e=1, pre=pre)

    def setStep(self, step):
        mc.floatField(self.floatField, e=1, step=step)

    def setValue(self, value):
        mc.floatField(self.floatField, e=1, v=value)


class IntField(QtWidgets.QWidget):

    def __init__(self, objName, parent):
        super(IntField, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        if objName:
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self

        self.intField = mc.intField(min=-10, max=10, step=1, v=0)

        wrappedField = wrapInstance(int(omui.MQtUtil.findControl(self.intField)), QtWidgets.QWidget)
        self.layout.addWidget(wrappedField)

        parent.addWidget(self)

    def setRange(self, minimum, maximum):
        mc.intField(self.intField, e=1, min=minimum, max=maximum)

    def setStep(self, step):
        mc.intField(self.intField, e=1, step=step)

    def setValue(self, value):
        mc.intField(self.intField, e=1, v=value)

# Label


class Label(QtWidgets.QLabel):

    def __init__(self, parent=None, objName=None, margins=[0, 0, 0, 0]):
        super(Label, self).__init__()

        if objName:
            self.setObjectName(getUniqueName(objName))
            WIDGETS[objName] = self
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setContentsMargins(*style.scale(margins))
        if parent:
            parent.addWidget(self)

    def addParent(self, parent, stretch=0):
        parent.addWidget(self, stretch)

    def setLabel(self, text, lineHeight=100):
        text = self.__formatText(text, lineHeight=lineHeight)

        self.setText(text)

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.setLabelStyle()

    def setLabelStyle(self, labelStyle='normal'):
        self.font = QtGui.QFont('Roboto')
        self.setFont(self.font)
        if labelStyle == 'normal':
            self.setFontSize(11)
        elif labelStyle == 'small':
            self.setFontSize(10, False)

    def setFontSize(self, size, bold=True):
        font = self.font
        font.setPixelSize(style.scale(size))
        if bold:
            font.setBold(bold)
        self.setFont(font)

    def __formatText(self, text, lineHeight=80):
        if lineHeight == 100:
            return text
        if isinstance(text, list):
            self.resizeEvent = self.changeText
            self.buttonLabels = text
            text = text[0]
        text = '<p style="line-height:{1}%;">{0}</p>'.format(text, lineHeight)
        return text


class UVStandardItem(QtGui.QStandardItem):

    def __init__(self, grpName='', crvName='', fontSize=12, setBold=False, color=[128, 128, 128, 255]):
        super(UVStandardItem, self).__init__()

        self.fnt = QtGui.QFont('Open Sans')
        self.fnt.setBold(setBold)
        self.fnt.setPixelSize(style.scale(fontSize))
        self.curveName = crvName
        self.groupName = grpName

        self.setEditable(False)
        clr = QtGui.QColor(*color)
        self.setForeground(clr)
        self.setFont(self.fnt)
        self.setText(self.groupName)

    def setBold(self, bold=True):
        self.fnt.setBold(bold)
        self.setFont(self.fnt)


class UVItemList(QtWidgets.QTreeView):

    signal_mouseReleased = QtCore.Signal()
    signal_keyPressed = QtCore.Signal()

    def __init__(self, parent=None):
        super(UVItemList, self).__init__()

        self.layout = QtWidgets.QHBoxLayout(self)
        if parent:
            parent.addWidget(self)

        self.treeModel = QtGui.QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()

        self.itemList = []

        self.setModel(self.treeModel)
        self.setHeaderHidden(True)
        self.setAnimated(True)
        self.setIndentation(style.scale(8))
        self.setSelectionMode(self.ExtendedSelection)

    def mouseReleaseEvent(self, event):
        super(UVItemList, self).mouseReleaseEvent(event)
        self.expandSelection()
        self.signal_mouseReleased.emit()

    def keyPressEvent(self, event):
        super(UVItemList, self).keyPressEvent(event)
        self.signal_keyPressed.emit()

    def getSelection(self):
        selectedItems = self.selectedIndexes()
        selectedCurves = []
        for i in selectedItems:
            model = i.model()
            item = model.itemFromIndex(i)
            selectedCurves.append(item.curveName)
        return selectedCurves

    def getItemList(self):
        return self.itemList

    def expandSelection(self):
        indexes = self.selectedIndexes()
        for index in indexes:
            model = index.model()
            item = model.itemFromIndex(index)
            if item.hasChildren():
                for row in range(item.rowCount()):
                    self.selectionModel().select(
                        self.treeModel.index(row, 0, index),
                        self.selectionModel().Select
                    )

    def selectItems(self, items):
        if not items:
            return
        if not isinstance(items, list):
            items = [items]
        for item in items:
            index = item.index()
            self.selectionModel().select(
                index,
                self.selectionModel().Toggle
            )

    def clearItemList(self):
        self.rootNode.removeRows(0, self.treeModel.rowCount())

    def updateItemList(self, inputDict):
        self.itemList *= 0
        self.clearItemList()
        for key in inputDict:
            parent = mc.listRelatives(key, p=1, pa=1)
            rootItem = UVStandardItem(crvName=key, grpName=parent[0])
            self.itemList.append(rootItem)
            self.rootNode.appendRow(rootItem)
            if inputDict[key]:
                rootItem.setBold()
                for item in inputDict[key]:
                    if (mc.attributeQuery('gsmessage', n=item, ex=1) and
                            mc.connectionInfo(item + '.gsmessage', isSource=1)):
                        continue
                    parent = mc.listRelatives(item, p=1, pa=1)
                    subItem = UVStandardItem(crvName=item, grpName=parent[0])
                    self.itemList.append(subItem)
                    rootItem.appendRow(subItem)
        self.expandAll()
        self.selectAll()
