#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studiovendor.Qt import QtGui
from studiovendor.Qt import QtWidgets

import mutils


__all__ = ["FrameRangeMenu", "showFrameRangeMenu"]


class FrameRangeAction(QtWidgets.QAction):
    def __init__(self, *args):
        super(FrameRangeAction, self).__init__(*args)

        self._frameRange = (0, 100)

    def frameRange(self):
        return self._frameRange

    def setFrameRange(self, frameRange):
        self._frameRange = frameRange


class FrameRangeMenu(QtWidgets.QMenu):

    def __init__(self, parent=None):
        super(FrameRangeMenu, self).__init__(parent)

        action = FrameRangeAction("From Timeline", self)
        action.setFrameRange(mutils.playbackFrameRange())
        self.addAction(action)

        action = FrameRangeAction("From Selected Timeline", self)
        action.setFrameRange(mutils.selectedFrameRange())
        self.addAction(action)

        action = FrameRangeAction("From Selected Objects", self)
        action.setFrameRange(mutils.selectedObjectsFrameRange())
        self.addAction(action)


def showFrameRangeMenu():
    """
    Show the frame range menu at the current cursor position.

    :rtype: QtWidgets.QAction
    """
    menu = FrameRangeMenu()
    position = QtGui.QCursor().pos()
    action = menu.exec_(position)
    return action


if __name__ == "__main__":
    action = showFrameRangeMenu()
    print(action.frameRange())
