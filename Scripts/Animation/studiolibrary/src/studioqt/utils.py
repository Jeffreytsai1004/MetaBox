#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
import logging
import contextlib

import studioqt
from studioqt import QtCore
from studioqt import QtCompat
from studioqt import QtWidgets


__all__ = [
    "app",
    "fadeIn",
    "fadeOut",
    "loadUi",
    "isAltModifier",
    "isShiftModifier",
    "isControlModifier",
    "InvokeRepeatingThread",
]

logger = logging.getLogger(__name__)


class InvokeRepeatingThread(QtCore.QThread):
    """
    A convenience class for invoking a method to the given repeat rate.
    """

    triggered = QtCore.Signal()

    def __init__(self, repeatRate, *args):
        QtCore.QThread.__init__(self, *args)

        self._repeatRate = repeatRate

    def run(self):
        """
        The starting point for the thread.
        
        :rtype: None 
        """
        while True:
            QtCore.QThread.sleep(self._repeatRate)
            self.triggered.emit()


@contextlib.contextmanager
def app():
    """
    
    .. code-block:: python
        import studioqt

        with studioqt.app():
            widget = QWidget(None)
            widget.show()

    :rtype: None
    """
    app_ = None

    isAppRunning = bool(QtWidgets.QApplication.instance())
    if not isAppRunning:
        app_ = QtWidgets.QApplication(sys.argv)
        installFonts()

    yield None

    if not isAppRunning:
        sys.exit(app_.exec_())


def uiPath(cls):
    """
    Return the ui path for the given widget class.
    
    :type cls: type
    :rtype: str
    """
    name = cls.__name__
    path = inspect.getfile(cls)
    dirname = os.path.dirname(path)

    path = dirname + "/resource/ui/" + name + ".ui"

    if not os.path.exists(path):
        path = dirname + "/ui/" + name + ".ui"

    if not os.path.exists(path):
        path = dirname + "/" + name + ".ui"

    return path


def loadUi(widget, path=None):
    """
    .. code-block:: python
        import studioqt

        class Widget(QtWidgets.QWidget):
            def __init__(self)
                super(Widget, self).__init__()
                studioqt.loadUi(self)

        with studioqt.app():
            widget = Widget()
            widget.show()

    :type widget: QWidget or QDialog
    :type path: str
    :rtype: None
    """
    if not path:
        path = uiPath(widget.__class__)

    cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(path))
        widget.ui = QtCompat.loadUi(path, widget)
    finally:
        os.chdir(cwd)


def isModifier():
    """
    Return True if either the alt key or control key is down.
    
    :rtype: bool 
    """
    return isAltModifier() or isControlModifier()


def isAltModifier():
    """
    Return True if the alt key is down.

    :rtype: bool
    """
    modifiers = QtWidgets.QApplication.keyboardModifiers()
    return modifiers == QtCore.Qt.AltModifier


def isControlModifier():
    """
    Return True if the control key is down.
    
    :rtype: bool
    """
    modifiers = QtWidgets.QApplication.keyboardModifiers()
    return modifiers == QtCore.Qt.ControlModifier


def isShiftModifier():
    """
    Return True if the shift key is down.

    :rtype: bool
    """
    modifiers = QtWidgets.QApplication.keyboardModifiers()
    return modifiers == QtCore.Qt.ShiftModifier


def fadeIn(widget, duration=200, onFinished=None):
    """
    Fade in the given widget using the opacity effect.

    :type widget: QtWidget.QWidgets
    :type duration: int 
    :type onFinished: func
    :rtype: QtCore.QPropertyAnimation 
    """
    widget._fadeInEffect_ = QtWidgets.QGraphicsOpacityEffect()
    widget.setGraphicsEffect(widget._fadeInEffect_)
    animation = QtCore.QPropertyAnimation(widget._fadeInEffect_, "opacity")
    animation.setDuration(duration)
    animation.setStartValue(0.0)
    animation.setEndValue(1.0)
    animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    animation.start()

    if onFinished:
        animation.finished.connect(onFinished)

    widget._fadeIn_ = animation

    return animation


def fadeOut(widget, duration=200, onFinished=None):
    """
    Fade out the given widget using the opacity effect.
    
    :type widget: QtWidget.QWidgets
    :type duration: int
    :type onFinished: func
    :rtype: QtCore.QPropertyAnimation 
    """
    widget._fadeOutEffect_ = QtWidgets.QGraphicsOpacityEffect()
    widget.setGraphicsEffect(widget._fadeOutEffect_)
    animation = QtCore.QPropertyAnimation(widget._fadeOutEffect_, "opacity")
    animation.setDuration(duration)
    animation.setStartValue(1.0)
    animation.setEndValue(0.0)
    animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
    animation.start()

    if onFinished:
        animation.finished.connect(onFinished)

    widget._fadeOut_ = animation

    return animation


def installFonts(path=""):
    """
    Install all the fonts in the given directory path.
    
    :type path: str
    """
    path = path or studioqt.resource.get("fonts")

    path = os.path.abspath(path)
    fontDatabase = QtWidgets.QFontDatabase()

    for filename in os.listdir(path):

        if filename.endswith(".ttf"):

            filename = os.path.join(path, filename)
            result = fontDatabase.addApplicationFont(filename)

            if result > 0:
                logger.debug("Added font %s", filename)
            else:
                logger.debug("Cannot add font %s", filename)
