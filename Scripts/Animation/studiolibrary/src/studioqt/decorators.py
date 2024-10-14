#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studiovendor.Qt import QtGui
from studiovendor.Qt import QtCore
from studiovendor.Qt import QtWidgets


def showWaitCursor(fn):

    def wrapped(*args, **kwargs):
        cursor = QtGui.QCursor(QtCore.Qt.WaitCursor)
        QtWidgets.QApplication.setOverrideCursor(cursor)
        try:
            return fn(*args, **kwargs)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    wrapped.__name__ = fn.__name__
    wrapped.__doc__ = fn.__doc__

    return wrapped


def showArrowCursor(fn):

    def wrapped(*args, **kwargs):
        cursor = QtGui.QCursor(QtCore.Qt.ArrowCursor)
        QtWidgets.QApplication.setOverrideCursor(cursor)
        try:
            return fn(*args, **kwargs)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    wrapped.__name__ = fn.__name__
    wrapped.__doc__ = fn.__doc__

    return wrapped