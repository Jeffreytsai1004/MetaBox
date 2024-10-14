#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import maya.OpenMayaUI as omui
except ImportError as error:
    print(error)

from studioqt import QtCore
from studioqt import QtWidgets


try:
    from shiboken2 import wrapInstance
except ImportError:
    try:
        from shiboken import wrapInstance
    except ImportError as error:
        print(error)


from .framerangemenu import FrameRangeMenu
from .framerangemenu import showFrameRangeMenu
from .modelpanelwidget import ModelPanelWidget
from .thumbnailcapturedialog import *
from .thumbnailcapturemenu import ThumbnailCaptureMenu


def mayaWindow():
    """
    Return the Maya main window as a QMainWindow object.
    
    :rtype: QMainWindow
    """
    mainWindowPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mainWindowPtr), QtWidgets.QMainWindow)


def makeMayaStandaloneWindow(w):
    """
    Make a standalone window, though parented under Maya's mainWindow.

    The parenting under Maya's mainWindow is done so that the QWidget will 
    not auto-destroy itself when the instance variable goes out of scope.
    """
    # Parent under the main Maya window
    w.setParent(mayaWindow())

    # Make this widget appear as a standalone window
    w.setWindowFlags(QtCore.Qt.Window)
    w.raise_()
    w.show()
