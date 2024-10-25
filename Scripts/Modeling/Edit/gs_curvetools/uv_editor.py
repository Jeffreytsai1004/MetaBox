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

import random
from functools import partial as pa

import shiboken2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from .utils import gs_math as mt
from .utils import utils
from .utils.wrap import WIDGETS

# Buttons
LMB = Qt.LeftButton
RMB = Qt.RightButton
MMB = Qt.MiddleButton
ALT = Qt.AltModifier
CTRL = Qt.ControlModifier
SHIFT = Qt.ShiftModifier
NO_MOD = Qt.NoModifier
SCENE_W = 2000
SCENE_H = 2000

# Texture cache
CACHE = {}


class Editor(QtWidgets.QGraphicsView):
    """
    UV Editor View Main Widget

    """

    signal_mousePress = QtCore.Signal(object)
    signal_mouseMove = QtCore.Signal(object)
    signal_mouseRelease = QtCore.Signal(object)
    signal_keyPress = QtCore.Signal(object, object)
    signal_functionKeyPress = QtCore.Signal(object)
    signal_uvDrawEnd = QtCore.Signal()
    signal_zoomChangeEvent = QtCore.Signal()
    signal_forcedTextureMapUpdate = QtCore.Signal()

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.currentAction = 'NONE'
        self.controllerMode = 'SELECT'
        self.scaleMode = 'H'
        self.initialMousePos = QtCore.QPoint(0, 0)
        self.UVDict = dict()
        self.textureItem = None
        self.diffusePath = ''
        self.alphaPath = ''
        self.storedAlpha = None

    def init(self):
        # Init scene
        self.mainScene = EditorScene(self)
        self.mainScene.setSceneRect(-SCENE_H / 2, -SCENE_W / 2, SCENE_H, SCENE_W)
        self.setScene(self.mainScene)

        # Set initial Flags
        self.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.setRenderHint(QtGui.QPainter.TextAntialiasing, True)
        self.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        self.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self.setResizeAnchor(self.AnchorViewCenter)
        self.setTransformationAnchor(self.AnchorUnderMouse)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Initial scaling and centering
        self.centerOn(50, -50)
        self.scale(8, 8)
        self.focusView()

        # Selection Rect Initialization
        self.selectionRect = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)

        # Mouse Line Init
        self.mouseLine = MouseLine()
        self.mousePoints = [0, 0, 0, 0]
        self.mainScene.addItem(self.mouseLine)

        # Custom mouse cursor
        self.customCursor = Cursor()
        self.customCursor.sizeVerticalCursor()
        self.mainScene.addItem(self.customCursor)

        # Rotation Circle
        self.rotationCircle = RotationCircle()
        self.mainScene.addItem(self.rotationCircle)

        # Initialize mouse variables
        self.previousMouseDelta = 0
        self.zoomDirection = 0

        # Draw Origin Dot
        originBrush = QtGui.QBrush()
        originBrush.setStyle(Qt.SolidPattern)
        originBrush.setColor(QtGui.QColor(255, 0, 0))
        originPen = QtGui.QPen()
        originPen.setWidth(0)
        self.originDot = self.mainScene.addEllipse(-5, -5, 10, 10, pen=originPen, brush=originBrush)
        self.originDot.setFlag(self.originDot.ItemIgnoresTransformations, True)

    def changeColor(self,
                    colorBG=(36, 36, 36),
                    colorGrid=(50, 50, 50),
                    colorFrame=(160, 75, 75),
                    uvColorBG=(96, 100, 160),
                    uvColorSelected=(255, 255, 255),
                    uvColorDeselected=(128, 128, 128)):
        if self.mainScene:
            self.mainScene.colorBG = (list(colorBG) + [255])
            self.mainScene.colorGrid = (list(colorGrid) + [255])
            self.mainScene.colorFrame = (list(colorFrame) + [128])
            UVItem.bgColor = QtGui.QColor(*(list(uvColorBG) + [1]))
            UVItem.selectedColor = QtGui.QColor(*(list(uvColorSelected) + [255]))
            UVItem.deselectedColor = QtGui.QColor(*(list(uvColorDeselected) + [255]))
            for uv in self.getAllUVs():
                uv.bgColor = QtGui.QColor(*(list(uvColorBG) + [1]))
                uv.selectedColor = QtGui.QColor(*(list(uvColorSelected) + [255]))
                uv.deselectedColor = QtGui.QColor(*(list(uvColorDeselected) + [255]))
            self.mainScene.update()

    def getCurrentTexture(self):
        return self.textureItem

    def toggleAlpha(self, enable):
        if self.textureItem:
            if enable:
                self.textureItem.enableAlpha()
            else:
                self.textureItem.disableAlpha()

    def setTexture(self, diffuse, alpha=None, coverage=(1.0, 1.0), translation=(0, 0)):
        self.removeTexture()
        self.diffusePath = diffuse
        self.alphaPath = alpha

        self.textureItem = self.createTextureItem(self.diffusePath, self.alphaPath, coverage, translation)

        if not self.textureItem:
            return 'NoTexture'
        if not (self.textureItem.customPixmap.width() > 0 and
                self.textureItem.customPixmap.height() > 0):
            return 'ZeroTexture'

        self.setTextureItem(self.textureItem)

        return 'Success'

    def createTextureItem(self, diffusePath, alphaPath, coverage, translation):
        # Using cached TextureItem (or creating new one)
        diffuseTime = QtCore.QFileInfo(diffusePath).lastModified()
        alphaTime = None
        if alphaPath:
            alphaTime = QtCore.QFileInfo(alphaPath).lastModified()
        shouldUpdate = True
        if diffusePath in CACHE and shiboken2.isValid(CACHE[diffusePath][0]):  # pylint: disable=maybe-no-member
            shouldUpdate = False
            # Update if Diffuse texture has different timestamp
            if CACHE[diffusePath][1] != diffuseTime:
                shouldUpdate = True
            # Update if Alpha was added
            if not CACHE[diffusePath][2] and alphaTime:
                shouldUpdate = True
            # Update if Alpha was removed
            if not alphaTime and CACHE[diffusePath][2]:
                shouldUpdate = True
            # Update if Alpha has different timestamp
            if CACHE[diffusePath][2] and CACHE[diffusePath][2] != alphaTime:
                shouldUpdate = True
            # Update if coverage or translation changed
            if CACHE[diffusePath][0].customCoverage != coverage or CACHE[diffusePath][0].customTranslation != translation:
                shouldUpdate = True
        if shouldUpdate:
            textureItem = TextureItem(diffusePath, alphaPath, coverage, translation)
            CACHE[diffusePath] = (textureItem, diffuseTime, alphaTime)
            if 'UVEditorTransparencyToggle' in WIDGETS:
                if WIDGETS['UVEditorTransparencyToggle'].isChecked():
                    textureItem.enableAlpha()
                else:
                    textureItem.disableAlpha()
        else:
            textureItem = CACHE[diffusePath][0]
        return textureItem

    def setTextureItem(self, textureItem):
        if textureItem:
            textureItem.setScale(
                1.0 / (max(textureItem.customPixmap.width(),
                           textureItem.customPixmap.height())) * 100)
            textureItem.setOffset(0, -100.0 / textureItem.scale())

            # Avoid multiple connections when setting textures
            try:
                self.signal_zoomChangeEvent.disconnect()
            except Exception:
                pass
            try:
                self.signal_forcedTextureMapUpdate.disconnect()
            except Exception:
                pass

            # Connecting signals
            self.signal_zoomChangeEvent.connect(textureItem.updatePixmap)
            self.signal_forcedTextureMapUpdate.connect(pa(textureItem.updatePixmap, True))

            self.mainScene.addItem(textureItem)
            textureItem.updatePixmap(forceUpdate=True)

            return 'Success'

    def removeTexture(self):
        for item in self.items():
            if isinstance(item, TextureItem):
                self.mainScene.removeItem(item)

    def createUV(self, name):
        if name in self.UVDict:
            try:
                self.mainScene.removeItem(self.UVDict[name])
            except BaseException:
                pass
        self.UVDict[name] = UVItem(name)
        self.mainScene.addItem(self.UVDict[name])
        return self.UVDict[name]

    def purgeUVs(self):
        for uv in self.UVDict:
            self.mainScene.removeItem(self.UVDict[uv])
        self.UVDict.clear()

    def getUVs(self):
        returnDict = dict()
        selection = [i.name for i in self.getAllUVs(selected=True)]
        for uv in self.UVDict:
            if uv in selection:
                returnDict[uv] = self.UVDict[uv].getAttrs()
        return returnDict

    def wheelEvent(self, event):
        # Wheel Zoom
        self.setTransformationAnchor(self.AnchorUnderMouse)
        self.currentAction = 'ZOOM'
        zoomIncrement = 0.1
        if event.delta() > 0:
            if self.transform().m11() >= 500:
                zoomIncrement = 0
            zoom = 1 + zoomIncrement
        else:
            if self.transform().m11() <= 1:
                zoomIncrement = 0
            zoom = 1 - zoomIncrement
        self.scale(zoom, zoom)
        self.currentAction = 'NONE'
        self.signal_forcedTextureMapUpdate.emit()

    def initializeMouseLine(self):
        if self.currentAction in ['SCALE', 'ROTATE']:
            self.mouseLine.setVisible(True)
            self.mouseLine.setPoints(*self.mousePoints)
        else:
            self.mouseLine.setVisible(False)

    def initializeRotationCircle(self):
        if self.currentAction == 'ROTATE':
            self.rotationCircle.setVisible(True)
            self.rotationCircle.rotationRect.moveCenter(
                self.rotationCircle.mapFromScene(self.mousePoints[0], self.mousePoints[1])
            )
        else:
            self.rotationCircle.setVisible(False)

    def mousePressEvent(self, event):
        # TODO: Improve selection mode. Should select only one card if clicked, just like in Move mode.
        self.signal_mousePress.emit(event)
        self.setTransformationAnchor(self.AnchorUnderMouse)
        button = event.button()
        mod = event.modifiers()

        # Switching between controller flags
        items = self.getAllUVs()
        if self.controllerMode in ['SELECT', 'ROTATE', 'SCALE']:
            for item in items:
                item.setFlag(item.ItemIsMovable, False)
        else:
            for item in items:
                item.setFlag(item.ItemIsMovable, True)

        # Initializing controllers:

        # Scale controller
        if self.controllerMode == 'SCALE' and button == LMB:
            self.currentAction = 'SCALE'

            items = self.getAllUVs(selected=True)
            if items:
                lastItem = items[-1]

                self.setCursor(Qt.BlankCursor)
                self.customCursor.setPos(self.mapToScene(event.pos()))
                self.customCursor.setVisible(True)

                if self.scaleMode == 'V':
                    self.customCursor.setRotation(lastItem.rotation())
                    A = lastItem.mapToScene(lastItem.mainRect.bottomLeft())
                    B = lastItem.mapToScene(lastItem.mainRect.bottomRight())
                else:
                    self.customCursor.setRotation(lastItem.rotation() + 90)
                    A = lastItem.mapToScene(lastItem.yAxisLine.p1().toPoint())
                    B = lastItem.mapToScene(lastItem.yAxisLine.p2().toPoint())

                P = self.mapToScene(event.pos())
                finalPoint = mt.projectPoint(A, B, P)
                self.initLength = QtCore.QLineF(P, finalPoint).length()

                scenePos = self.mapToScene(event.pos())
                self.mousePoints = [
                    finalPoint.x(),
                    finalPoint.y(),
                    scenePos.x(),
                    scenePos.y()
                ]
                self.initializeMouseLine()
            for item in items:
                item.initXScale()
                item.initYScale()

            self.initialMousePos = event.pos()
            self.setInteractive(False)

        # Rotation controller
        elif self.controllerMode == 'ROTATE' and button == LMB:
            self.currentAction = 'ROTATE'

            self.setCursor(Qt.BlankCursor)
            self.customCursor.setPos(self.mapToScene(event.pos()))
            self.customCursor.setVisible(True)

            items = self.getAllUVs(selected=True)
            if items:
                scenePos = self.mapToScene(event.pos())
                self.mousePoints = [
                    items[-1].rotatePivot.x(),
                    items[-1].rotatePivot.y(),
                    scenePos.x(),
                    scenePos.y()
                ]
                self.initializeMouseLine()
                self.initializeRotationCircle()
            self.initAngle = self.mouseLine.mouseLine.angleTo(self.scene().xLine)
            self.customCursor.setRotation(self.initAngle)
            self.setInteractive(False)

        # Move controller
        elif self.controllerMode == 'MOVE' and button == LMB:
            self.currentAction = 'MOVE'
            self.setCursor(Qt.SizeAllCursor)

        # Draw UV controller
        elif self.controllerMode == 'DRAW' and button == LMB:
            self.setCursor(Qt.CrossCursor)
            self.selectionRect.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
            self.currentAction = 'DRAW'
            self._startSelection(event.pos())
            self.setInteractive(False)

        # Zoom using drag
        elif button == RMB and mod == ALT:
            self.currentAction = 'ZOOM'
            self.initialMousePos = event.pos()
            self.zoomInitialPos = event.pos()
            self.setInteractive(False)

        # Panning the view
        elif button == MMB:
            self.currentAction = 'PAN'
            self.previousPosition = event.pos()
            self.setCursor(Qt.ClosedHandCursor)
            self.setInteractive(False)

        # Selection Rect
        elif button == LMB and (mod == CTRL or mod == NO_MOD):
            self.currentAction = 'SELECT'
            self._startSelection(event.pos())
            self.setInteractive(False)

        # Click selection
        elif button == LMB and (mod == CTRL and mod == CTRL | SHIFT):
            self.currentAction = 'SELECT_ADD'
            self._startSelection(event.pos())
            self.setInteractive(False)

        # Click remove selection
        elif button == LMB and mod == CTRL:
            self.currentAction = 'SELECT_REMOVE'
            self._startSelection(event.pos())
            self.setInteractive(False)

        # Click toggle selection
        elif button == LMB and mod == SHIFT:
            self.currentAction = 'SELECT_TOGGLE'
            self._startSelection(event.pos())
            self.setInteractive(False)

        # Default action
        else:
            self.setCursor(Qt.ArrowCursor)
            self.currentAction = 'NONE'

        super(Editor, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not self.isActiveWindow():
            self.activateWindow()
        if not self.hasFocus():
            self.setFocus()

        self.initializeMouseLine()
        self.initializeRotationCircle()

        # Move controller drag
        if self.currentAction == 'MOVE':
            pass

        # Scale controller drag
        elif self.currentAction == 'SCALE':
            # Updating the mouse line position
            self.scenePos = self.mapToScene(event.pos())

            # Calculating delta scale
            delta = self.initialMousePos - event.pos()

            # Applying scale to items
            items = self.getAllUVs(selected=True)
            if items:
                self.customCursor.setPos(self.mapToScene(event.pos()))

                lastItem = items[-1]
                if self.scaleMode == 'V':
                    A = lastItem.mapToScene(lastItem.mainRect.bottomLeft())
                    B = lastItem.mapToScene(lastItem.mainRect.bottomRight())
                else:
                    A = lastItem.mapToScene(lastItem.yAxisLine.p1().toPoint())
                    B = lastItem.mapToScene(lastItem.yAxisLine.p2().toPoint())

                P = self.mapToScene(event.pos())
                finalPoint = mt.projectPoint(A, B, P)
                length = QtCore.QLineF(P, finalPoint).length()
                if self.scaleMode == 'V':
                    for item in items:
                        item.changeYScale(length - self.initLength)
                else:
                    for item in items:
                        item.changeXScale(length - self.initLength)

                self.mousePoints = [
                    finalPoint.x(),
                    finalPoint.y(),
                    self.scenePos.x(),
                    self.scenePos.y()
                ]

        # Rotate controller drag
        elif self.currentAction == 'ROTATE':
            self.scenePos = self.mapToScene(event.pos())
            items = self.getAllUVs(selected=True)

            if items:
                self.customCursor.setPos(self.mapToScene(event.pos()))
                self.mousePoints = [
                    items[-1].rotatePivot.x(),
                    items[-1].rotatePivot.y(),
                    self.scenePos.x(),
                    self.scenePos.y()
                ]
                self.initializeMouseLine()

            currentAngle = self.mouseLine.mouseLine.angleTo(self.scene().xLine)
            for item in items:
                angleDelta = mt.angleDiff(currentAngle, self.initAngle)
                newRotation = item.initRotation + angleDelta
                self.customCursor.setRotation(currentAngle)
                if event.modifiers() == SHIFT:
                    newRotation = int(newRotation)
                    if not abs(newRotation) % 15:
                        item.setRotation(newRotation)
                else:
                    item.setRotation(newRotation)

        # UV drawing update
        elif self.currentAction == 'DRAW':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )

        # Zooming using drag
        elif self.currentAction == 'ZOOM':
            self.setCursor(Qt.SizeHorCursor)

            delta = self.zoomInitialPos.x() - event.pos().x()
            if self.previousMouseDelta > delta:
                self.zoomDirection = 1
            elif self.previousMouseDelta < delta:
                self.zoomDirection = -1
            else:
                if self.zoomDirection == -1:
                    self.zoomDirection = -1
                else:
                    self.zoomDirection = 1
            self.previousMouseDelta = delta

            # Zoom factor
            zoomAmount = 0.015
            if self.zoomDirection == 1:
                if self.transform().m11() >= 500:
                    zoomAmount = 0
                zoom = 1 + zoomAmount
            else:
                if self.transform().m11() <= 1:
                    zoomAmount = 0
                zoom = 1 - zoomAmount

            # Zooming and centering on clicked point
            self.setTransformationAnchor(self.AnchorViewCenter)
            initPoint = self.mapToScene(self.initialMousePos)
            self.scale(zoom, zoom)
            afterPoint = self.mapToScene(self.initialMousePos)
            pointDelta = afterPoint - initPoint

            self.setTransformationAnchor(self.NoAnchor)
            self.translate(pointDelta.x(), pointDelta.y())

            self.signal_zoomChangeEvent.emit()

        # Panning the view
        elif self.currentAction == 'PAN':
            delta = self.previousPosition - event.pos()
            self.previousPosition = event.pos()
            self.translate(self.pos().x() + delta.x(),
                           self.pos().y() + delta.y())

        # Creating selection rectangle
        elif self.currentAction in ['SELECT', 'SELECT_ADD', 'SELECT_REMOVE', 'SELECT_TOGGLE']:
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )

        # Default Action
        else:
            self.currentAction = 'NONE'

        if self.controllerMode == 'DRAW':
            self.setCursor(Qt.CrossCursor)

        super(Editor, self).mouseMoveEvent(event)

        # Emit move signal
        if self.currentAction in ['MOVE', 'ROTATE', 'SCALE']:
            self.signal_mouseMove.emit(event)

    def mouseReleaseEvent(self, event):

        self.customCursor.setVisible(False)

        # Zooming
        if self.currentAction == 'ZOOM':
            # Reset the zoom
            self.setCursor(Qt.ArrowCursor)
            self.zoomDirection = 0
            self.signal_forcedTextureMapUpdate.emit()

        # Panning the view
        elif self.currentAction == 'PAN':
            # Reset the panning
            self.setCursor(Qt.ArrowCursor)

        # UV Drawing
        elif self.currentAction == 'DRAW':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )
            painterPath = self._releaseSelection()
            origGeo = self.selectionRect.geometry()
            geo = self.mapToScene(origGeo).boundingRect()
            self.drawUV(geo)
            self.selectionRect.setStyle(QtWidgets.QStyleFactory.create('adskdarkflatui'))

        # Click selection
        elif self.currentAction == 'SELECT':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )
            painterPath = self._releaseSelection()
            self.scene().setSelectionArea(painterPath)

        # Click add selection
        elif self.currentAction == 'SELECT_ADD':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )
            painterPath = self._releaseSelection()
            for item in self.scene().items(painterPath):
                item.setSelected(True)

        # Click remove selection
        elif self.currentAction == 'SELECT_REMOVE':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )
            painterPath = self._releaseSelection()
            for item in self.scene().items(painterPath):
                item.setSelected(False)

        # Click toggle selection
        elif self.currentAction == 'SELECT_TOGGLE':
            self.selectionRect.setGeometry(
                QtCore.QRect(self.selectionOrigin, event.pos()).normalized()
            )
            painterPath = self._releaseSelection()
            for item in self.scene().items(painterPath):
                if item.isSelected():
                    item.setSelected(False)
                else:
                    item.setSelected(True)

        self.initAngle = self.mouseLine.mouseLine.angleTo(self.scene().xLine)
        for item in self.getAllUVs(selected=True):
            item.initRotation = item.rotation()

        self.mouseLine.setVisible(False)
        self.rotationCircle.setVisible(False)

        self.currentAction = 'NONE'
        self.setInteractive(True)
        self.setCursor(Qt.ArrowCursor)

        self.scene().update()
        self.signal_mouseRelease.emit(event)

        super(Editor, self).mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        # Filter all key press events
        key = event.key()
        mod = event.modifiers()
        if event.type() == QtCore.QEvent.KeyPress:
            self.setCursor(Qt.ArrowCursor)
            if key == Qt.Key_F:
                self.focusView()
                self.signal_forcedTextureMapUpdate.emit()
            elif key == Qt.Key_I:
                self.signal_functionKeyPress.emit('I')
            elif key == Qt.Key_H:
                self.signal_functionKeyPress.emit('H')
            elif key == Qt.Key_A:
                self.signal_functionKeyPress.emit('A')
            elif key == Qt.Key_V:
                self.signal_functionKeyPress.emit('V')
            elif key == Qt.Key_X:
                self.signal_functionKeyPress.emit('X')
            elif key == Qt.Key_O:
                self.signal_functionKeyPress.emit('O')
            elif key == Qt.Key_S:
                self.signal_functionKeyPress.emit('S')
            elif key == Qt.Key_Q:
                self.controllerMode = 'SELECT'
            elif key == Qt.Key_W:
                self.controllerMode = 'MOVE'
            elif key == Qt.Key_E:
                self.controllerMode = 'ROTATE'
            elif key == Qt.Key_R:
                if self.controllerMode == 'SCALE':
                    self.scaleMode = 'H' if self.scaleMode == 'V' else 'V'
                self.controllerMode = 'SCALE'
            elif key == Qt.Key_D:
                self.controllerMode = 'DRAW'
            elif key == Qt.Key_Z and mod == CTRL:
                super(Editor, self).keyPressEvent(event)
            elif key == Qt.Key_Y and mod == CTRL:
                super(Editor, self).keyPressEvent(event)
            for item in self.getAllUVs(selected=True):
                item.update()
        elif mod == CTRL:
            pass
        else:
            super(Editor, self).keyPressEvent(event)
        self.signal_keyPress.emit(self.controllerMode, self.scaleMode)

    def controllerModeChange(self, mode, direction=None):
        self.controllerMode = mode
        if direction:
            self.scaleMode = direction
        for item in self.getAllUVs(selected=True):
            item.update()

    def _startSelection(self, pos):
        self.selectionOrigin = pos
        self.selectionRect.setGeometry(QtCore.QRect(self.selectionOrigin, QtCore.QSize()))
        self.selectionRect.show()

    def _releaseSelection(self):
        painterPath = QtGui.QPainterPath()
        rect = self.mapToScene(self.selectionRect.geometry())
        painterPath.addPolygon(rect)
        self.selectionRect.hide()
        return painterPath

    def focusView(self):
        items = self.getAllUVs()
        selectedItems = self.getAllUVs(selected=True)
        finalRect = None

        if selectedItems:
            finalRect = selectedItems[0].sceneBoundingRect()
            for i in range(1, len(selectedItems)):
                finalRect |= selectedItems[i].sceneBoundingRect()
            finalRect.adjust(-2, -2, 2, 2)
            self.fitInView(finalRect, Qt.KeepAspectRatio)
        elif items:
            finalRect = items[0].sceneBoundingRect()
            for i in range(1, len(items)):
                finalRect |= items[i].sceneBoundingRect()
            if self.textureItem:
                finalRect |= self.textureItem.sceneBoundingRect()
            else:
                finalRect |= QtCore.QRectF(0, 0, 100, -100)
            finalRect.adjust(-2, -2, 2, 2)
            self.fitInView(finalRect, Qt.KeepAspectRatio)

        self.signal_zoomChangeEvent.emit()

    def randomizeUVs(self, mod):
        selectedItems = set(self.getAllUVs(selected=True))
        finalList = []
        while selectedItems:
            ele = selectedItems.pop()
            same = set()
            same.add(ele)
            for item in selectedItems:
                if ele.getAttrs() == item.getAttrs():
                    same.add(item)
            selectedItems = selectedItems - same
            finalList.append(list(same))

        groups = [(len(x), x[0].getAttrs()) for x in finalList]
        flattenedList = [element for sublist in finalList for element in sublist]
        random.shuffle(flattenedList)
        if mod:
            for i in range(len(groups)):
                flattenedList[0].moveUV(
                    x=groups[i][1]['moveU'],
                    y=groups[i][1]['moveV'],
                    rot=groups[i][1]['rotateUV'],
                    sx=groups[i][1]['scaleU'],
                    sy=groups[i][1]['scaleV']
                )
                flattenedList.pop(0)
            for item in flattenedList:
                randI = random.randint(0, len(groups) - 1)
                item.moveUV(
                    x=groups[randI][1]['moveU'],
                    y=groups[randI][1]['moveV'],
                    rot=groups[randI][1]['rotateUV'],
                    sx=groups[randI][1]['scaleU'],
                    sy=groups[randI][1]['scaleV']
                )
        else:
            for group in groups:
                applied = []
                for i in range(group[0]):
                    flattenedList[i].moveUV(
                        x=group[1]['moveU'],
                        y=group[1]['moveV'],
                        rot=group[1]['rotateUV'],
                        sx=group[1]['scaleU'],
                        sy=group[1]['scaleV']
                    )
                    applied.append(flattenedList[i])
                flattenedList = list(set(flattenedList) - set(applied))

    def verticalFlipUV(self):
        items = self.getAllUVs(selected=True)
        for item in items:
            pre = item.mapToScene(item.mainRect.topLeft())
            item.setRotation((item.rotation() + 180) % 360)
            post = item.mapToScene(item.mainRect.bottomRight())
            delta = post - pre
            item.setPos(item.pos() - delta)
            item.initRotation = item.rotation()

    def resetUV(self):
        for item in self.getAllUVs(selected=True):
            item.resetRect()

    def drawUV(self, rect):
        x = rect.center().x() - 50
        y = rect.bottom()
        sx = (rect.right() - rect.left()) / 100.0
        sy = -(rect.top() - rect.bottom()) / 100.0
        if sx > 0.02 or sy > 0.02:
            for item in self.getAllUVs(selected=True):
                if item.isVisible():
                    item.setRotation(0)
                    item.setPos(QtCore.QPointF(x, y))
                    item.setXScale(sx)
                    item.setYScale(sy)
        self.signal_uvDrawEnd.emit()

    def getAllUVs(self, selected=False):
        # type: (bool) -> list[UVItem]
        UVs = []
        for item in self.scene().items():
            if isinstance(item, UVItem):
                if selected:
                    if item.isSelected():
                        UVs.append(item)
                    else:
                        continue
                else:
                    UVs.append(item)
        return UVs


class EditorScene(QtWidgets.QGraphicsScene):
    """
    UV Editor Scene

    """

    def __init__(self, parent=None):
        super(EditorScene, self).__init__(parent)
        self.colorBG = (36, 36, 36, 255)
        self.colorGrid = (50, 50, 50, 128)
        self.colorFrame = (160, 75, 75, 255)

    def drawBackground(self, painter, rect):
        # Draw background
        self.gridSpacing = 10

        self._brush = QtGui.QBrush()
        self._brush.setStyle(Qt.SolidPattern)
        self._brush.setColor(QtGui.QColor(*self.colorBG))

        leftLine = rect.left() - rect.left() % self.gridSpacing
        topLine = rect.top() - rect.top() % self.gridSpacing

        painter.fillRect(rect, self._brush)

        lines = []
        i = int(leftLine)
        while i < int(rect.right()):
            lines.append(QtCore.QLineF(i, rect.top(), i, rect.bottom()))
            i += self.gridSpacing

        u = int(topLine)
        while u < int(rect.bottom()):
            lines.append(QtCore.QLineF(rect.left(), u, rect.right(), u))
            u += self.gridSpacing

        # Draw Grid Lines
        gridPen = QtGui.QPen()
        gridPen.setColor(QtGui.QColor(*self.colorGrid))
        gridPen.setWidth(0)
        painter.setPen(gridPen)
        painter.drawLines(lines)

        # Draw Axis Lines
        axisPen = QtGui.QPen()
        axisPen.setColor(QtGui.QColor(*self.colorFrame))
        axisPen.setWidth(0)
        self.xLine = QtCore.QLineF(rect.left(), 0, rect.right(), 0)
        self.yLine = QtCore.QLineF(0, rect.top(), 0, rect.bottom())
        xEndLine = QtCore.QLineF(rect.left(), -100, rect.right(), -100)
        yEndLine = QtCore.QLineF(100, rect.top(), 100, rect.bottom())
        painter.setPen(axisPen)
        painter.drawLines([self.xLine, self.yLine, xEndLine, yEndLine])


class TextureItem(QtWidgets.QGraphicsPixmapItem):
    """
    Creates a texture item for background use in UV Editor
    """

    def __init__(self, pixmapPath, alphaPath=None, coverage=(1.0, 1.0), offset=(0, 0)):
        super(TextureItem, self).__init__()
        self.UPDATE = True
        self.pixmapPath = pixmapPath
        self.alphaPath = alphaPath
        self.storedAlpha = None
        self.timer = utils.Timer()
        self.origPixmap = QtGui.QPixmap()
        self.customPixmap = QtGui.QPixmap()
        self.customCoverage = coverage
        self.coverageW = self.customCoverage[0]
        self.coverageH = self.customCoverage[1]
        self.customTranslation = offset
        self.translationX = self.customTranslation[0]
        self.translationY = self.customTranslation[1]
        self.createPixmap()

    def createPixmap(self):
        self.image = QtGui.QImage(self.pixmapPath)
        if self.alphaPath:
            alphaChannel = QtGui.QImage(self.alphaPath)
            self.storedAlpha = self.alphaPath
            if self.pixmapPath == self.alphaPath:
                alphaChannel = QtGui.QImage(self.alphaPath).convertToFormat(self.image.Format_Alpha8)
                if WIDGETS['UVEditorAlphaOnlyToggle'].isChecked():
                    self.image = self.image.alphaChannel().convertToFormat(self.image.Format_RGB888)
                else:
                    self.image = self.image.convertToFormat(self.image.Format_RGBA8888)
            else:
                alphaChannel = QtGui.QImage(self.alphaPath)
                if WIDGETS['UVEditorAlphaOnlyToggle'].isChecked():
                    self.image = alphaChannel.convertToFormat(self.image.Format_RGB888)
            self.image.setAlphaChannel(alphaChannel)
        else:
            self.image = self.image.convertToFormat(self.image.Format_RGBX8888)

        self.origPixmap.convertFromImage(self.image)
        self.setTransformationMode(Qt.SmoothTransformation)
        self.customPixmap.convertFromImage(self.image)
        self.setPixmap(self.customPixmap)
        self.updatePixmap(forceUpdate=True)

    def updatePixmap(self, forceUpdate=False):
        timer = self.timer.increment(1.0 / 5.0)
        if forceUpdate:
            timer = True
        if not timer:
            return
        self.customPixmap = self.origPixmap
        scene = self.scene()
        if self.customPixmap.width() and self.customPixmap.height():
            if scene:
                sceneRect = self.boundingRect()
                l = scene.parent().mapToGlobal(self.mapToScene(sceneRect.topLeft()).toPoint())
                r = scene.parent().mapToGlobal(self.mapToScene(sceneRect.topRight()).toPoint())
                w_o = (r - l) * scene.parent().transform().m11()
                x = w_o.x()
                if x <= 0:
                    x = 100
                self.mult = self.customPixmap.height() / float(x)
            else:
                self.mult = 1.0
            if self.mult < 1:
                self.mult = 1.0
            scale = 1.0 / (max(self.customPixmap.width(),
                               self.customPixmap.height())) * 100 * self.mult
            self.setScale(scale)
            resMax = max(self.customPixmap.width(), self.customPixmap.height())
            # resMin = min(self.customPixmap.width(), self.customPixmap.height())
            aspectWidth = (self.customPixmap.width() / float(resMax)) * (1.0 / self.coverageW)
            aspectHeight = (self.customPixmap.height() / float(resMax)) * (1.0 / self.coverageH)
            # print(aspectWidth, aspectHeight)
            pixWidth = self.customPixmap.width() / float(self.mult * aspectWidth)
            pixHeight = self.customPixmap.height() / float(self.mult * aspectHeight)
            # self.customPixmap = self.customPixmap.scaledToHeight(pixHeight, Qt.SmoothTransformation)
            self.customPixmap = self.customPixmap.scaled(
                QtCore.QSize(pixWidth, pixHeight),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.SmoothTransformation)
            self.setOffset(self.translationX * 100.0 / self.scale(),
                           (-100.0 * self.coverageH + self.translationY * -100.0) / self.scale())
            self.setPixmap(self.customPixmap)

    def enableAlpha(self):
        if self.storedAlpha:
            self.alphaPath = self.storedAlpha
            self.createPixmap()
            self.updatePixmap(True)

    def disableAlpha(self):
        if self.alphaPath:
            self.storedAlpha = self.alphaPath
            self.alphaPath = ''
            self.createPixmap()
            self.updatePixmap(True)


class UVItem(QtWidgets.QGraphicsItem):
    """
    UV Rectangle and controls implementation

    """
    bgColor = QtGui.QColor(96, 100, 160, 1)
    selectedColor = QtGui.QColor(255, 255, 255, 255)
    deselectedColor = QtGui.QColor(128, 128, 128, 255)

    def __init__(self, name=None, x1=0, y1=-100, x2=100, y2=0):
        super(UVItem, self).__init__()

        self.name = name
        self.flip = False
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemIsSelectable, True)
        self.setZValue(1)

        self.initRotation = self.rotation()
        self.initPos = self.pos()

        self.mainRect = QtCore.QRectF(QtCore.QPointF(x1, y1), QtCore.QPointF(x2, y2))

        self.xAxisLine = QtCore.QLineF(0, -50, 100, -50)
        self.yAxisLine = QtCore.QLineF(50, 0, 50, -100)

        self.rotatePivot = QtCore.QPointF(50, -50)
        self.rootPoint = QtCore.QRectF(0, 0, 0, 1)
        self.flipIndication = QtCore.QRectF(0, 0, 0, 1)

        self.setTransformOriginPoint(50, -50)

        self.initXScale()
        self.initYScale()

    def paint(self, painter, *_):
        # Main Rect Painting
        pen = QtGui.QPen()
        if self.isSelected():
            pen.setColor(self.selectedColor)
        else:
            pen.setColor(self.deselectedColor)
        pen.setWidth(2)
        pen.setCosmetic(True)
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(self.bgColor)
        painter.setBrush(brush)
        painter.drawRect(self.mainRect)

        if self.isSelected():
            # Root Point Painting
            self.rootPoint.setWidth(min(5 * self.mainRect.width() / 20, 5))
            self.rootPoint.moveCenter(QtCore.QPointF(50, -.5))
            painter.drawRect(self.rootPoint)

            # Axis Lines Painting
            pen.setStyle(Qt.DashLine)
            pen.setWidthF(0)
            painter.setPen(pen)
            self.updateAxisLines()
            if (self.scene().parent().scaleMode == 'V' and
                    self.scene().parent().controllerMode == 'SCALE'):
                painter.drawLine(self.xAxisLine)
            elif (self.scene().parent().scaleMode == 'H' and
                    self.scene().parent().controllerMode == 'SCALE'):
                painter.drawLine(self.yAxisLine)

        # Flip indicator Painting
        if self.flip:
            brush = QtGui.QBrush()
            brush.setStyle(Qt.SolidPattern)
            brush.setColor(QtGui.QColor(0, 0, 255, 128))
            painter.setBrush(brush)
            pen.setStyle(Qt.SolidLine)
            pen.setWidthF(0)
            painter.setPen(pen)
            self.flipIndication.setWidth(.95)
            self.flipIndication.setHeight(self.flipIndication.width())
            self.flipIndication.moveCenter(QtCore.QPointF(50, -.5))
            painter.drawEllipse(self.flipIndication)

        self.updatePivotPoint()

    def boundingRect(self):
        rect = QtCore.QRectF(self.mainRect)
        rect.adjust(-1, -1, 1, 1)
        return rect

    def shape(self):
        path = QtGui.QPainterPath()
        rect = QtCore.QRectF(self.mainRect)
        rect.adjust(-1, -1, 1, 1)
        path.addRect(rect)
        return path

    def updatePivotPoint(self):
        self.rotatePivot = QtCore.QPointF(50, -50) + self.pos()

    def updateAxisLines(self):
        self.xAxisLine.setLine(
            self.mainRect.left(), self.mainRect.top() / 2,
            self.mainRect.right(), self.mainRect.top() / 2
        )
        self.yAxisLine.setLine(
            50, 0,
            50, self.mainRect.top()
        )

    def initXScale(self):
        self.initLeft = self.mainRect.left()
        self.initRight = self.mainRect.right()

    def initYScale(self):
        self.initTop = self.mainRect.top()

    def moveUV(self, x=None, y=None, rot=None, sx=None, sy=None):
        """ Transform UV object directly from Maya """
        if x is not None and y is not None:
            self.setPos(x * 100, -(y * 100))
        elif x is not None:
            self.setPos(x * 100, self.pos().y())
        elif y is not None:
            self.setPos(self.pos().x(), -(y * 100))
        if rot is not None:
            self.setRotation(rot)
        if sx is not None:
            self.setXScale(sx)
        if sy is not None:
            self.setYScale(sy)

    def changeYScale(self, delta):
        """ Set the scale using controllers """
        self.prepareGeometryChange()
        newTop = self.initTop - delta
        if newTop <= -1:
            self.mainRect.setTop(self.initTop - delta)
            self.mainRect = self.mainRect.normalized()
            self.update()

    def setYScale(self, scale):
        """ Set the scale directly from Maya """
        self.prepareGeometryChange()
        top = round(100 * scale, 14)
        self.mainRect.setTop(-top)
        self.mainRect = self.mainRect.normalized()
        self.update()

    def changeXScale(self, delta):
        """ Set the scale using controllers """
        self.prepareGeometryChange()
        self.mainRect.setLeft(self.initLeft - delta)
        self.mainRect.setRight(self.initRight + delta)
        self.mainRect = self.mainRect.normalized()
        self.update()

    def setXScale(self, scale):
        """ Set the scale directly from Maya """
        self.prepareGeometryChange()
        sl = round((1 - scale) / 2 * 100, 14)
        sr = round((1 - ((1 - scale) / 2)) * 100, 14)
        self.mainRect.setLeft(sl)
        self.mainRect.setRight(sr)
        self.mainRect = self.mainRect.normalized()
        self.update()

    def getAttrs(self):
        attrs = dict()
        attrs['moveU'] = self.pos().x() / 100
        attrs['moveV'] = self.pos().y() / 100 * -1
        attrs['rotateUV'] = self.rotation() * -1
        attrs['scaleU'] = round((100 - (100 - self.mainRect.right()) * 2) / 100, 14)
        attrs['scaleV'] = self.mainRect.top() / 100 * -1
        return attrs

    def resetRect(self):
        self.setPos(0, 0)
        self.setRotation(0)
        self.mainRect = QtCore.QRectF(QtCore.QPointF(0, -100), QtCore.QPointF(100, 0))
        self.update()


class MouseLine(QtWidgets.QGraphicsItem):

    def __init__(self):
        super(MouseLine, self).__init__()
        self.setVisible(False)
        self.setZValue(100)

        # Mouse Line Init
        self.mouseLine = QtCore.QLineF(0, 0, 0, 0)

        # Rotation Pivot Point
        self.pivotPoint = QtCore.QRectF(0, 0, 20, 20)

    def setPoints(self, x1=0, y1=0, x2=0, y2=0):
        scale = self.scene().parent().transform().m11()
        self.prepareGeometryChange()
        self.mouseLine.setLine(x1, y1, x2, y2)
        self.pivotPoint.setWidth(2 / scale * 10)
        self.pivotPoint.setHeight(2 / scale * 10)
        self.pivotPoint.moveCenter(QtCore.QPointF(x1, y1))
        self.update()

    def paint(self, painter, *_):
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(128, 0, 0, 128))
        pen.setCosmetic(True)
        pen.setStyle(Qt.DashLine)
        pen.setWidthF(3)

        painter.setPen(pen)
        painter.drawLine(self.mouseLine)

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(255, 0, 0, 128))
        pen.setCosmetic(True)
        pen.setWidthF(0)

        brush = QtGui.QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QtGui.QColor(255, 0, 0, 128))
        painter.setPen(pen)
        painter.setBrush(brush)

        painter.drawEllipse(self.pivotPoint)

    def boundingRect(self):
        self.bRect = QtCore.QRectF(self.mouseLine.p1(), self.mouseLine.p2()).united(self.pivotPoint)
        return self.bRect.normalized()

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.bRect)
        return path


class RotationCircle(QtWidgets.QGraphicsItem):

    def __init__(self):
        super(RotationCircle, self).__init__()
        self.setZValue(100)
        self.setVisible(False)

        # Rect
        self.rotationRect = QtCore.QRectF(0, 0, 20, 20)

        self.rotationRect.moveCenter(self.mapFromScene(QtCore.QPoint(0, 0)))
        self.setTransformOriginPoint(self.rotationRect.center())

    def paint(self, painter, *_):
        scale = self.scene().parent().transform().m11()
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(128, 0, 0, 128))
        pen.setCosmetic(True)
        pen.setWidthF(3)

        painter.setPen(pen)
        self.rotationRect.setWidth(20 / scale * 10)
        self.rotationRect.setHeight(20 / scale * 10)
        painter.drawEllipse(self.rotationRect)

    def boundingRect(self):
        self.bRect = self.rotationRect.normalized()
        return self.bRect

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.bRect)
        return path


class Cursor(QtWidgets.QGraphicsItem):

    def __init__(self):
        super(Cursor, self).__init__()
        self.setFlag(self.ItemIsFocusable, False)
        self.setVisible(False)
        self.setZValue(101)
        self.mainLine = QtGui.QPolygonF()

    def sizeVerticalCursor(self):
        self.mainLine.append(QtCore.QPointF(0.2, -1))
        self.mainLine.append(QtCore.QPointF(1, -1))
        self.mainLine.append(QtCore.QPointF(0, -2))
        self.mainLine.append(QtCore.QPointF(-1, -1))
        self.mainLine.append(QtCore.QPointF(-0.2, -1))

        self.mainLine.append(QtCore.QPointF(-0.2, 1))
        self.mainLine.append(QtCore.QPointF(-1, 1))
        self.mainLine.append(QtCore.QPointF(0, 2))
        self.mainLine.append(QtCore.QPointF(1, 1))
        self.mainLine.append(QtCore.QPointF(0.2, 1))

    def paint(self, painter, *_):
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(0, 0, 0, 255))
        pen.setWidthF(0)
        pen.setCosmetic(True)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawPolygon(self.mainLine)

        scale = self.scene().parent().transform().m11()
        self.setScale(10 / scale)

    def boundingRect(self):
        self.bRect = self.mainLine.boundingRect()
        return self.bRect.normalized()

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.bRect)
        return path


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    editor = Editor()
    editor.init()
    editor.resize(1250, 1250)
    editor.show()

    app.exec_()
