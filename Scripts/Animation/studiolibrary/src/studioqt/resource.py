#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from studioqt import QtGui
from studioqt import Icon
from studioqt import Pixmap


PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
RESOURCE_DIRNAME = os.path.join(DIRNAME, "resource")


def get(*args):
    """
    This is a convenience function for returning the resource path.

    :rtype: str 
    """
    return Resource().get(*args)


def icon(*args, **kwargs):
    """
    Return an Icon object from the given resource name.
    :rtype: str 
    """
    return Resource().icon(*args, **kwargs)


def pixmap(*args, **kwargs):
    """
    Return a Pixmap object from the given resource name.
    :rtype: str 
    """
    return Resource().pixmap(*args, **kwargs)


class Resource(object):
    DEFAULT_DIRNAME = RESOURCE_DIRNAME

    def __init__(self, *args):
        """"""
        dirname = ""

        if args:
            dirname = os.path.join(*args)

        if os.path.isfile(dirname):
            dirname = os.path.dirname(dirname)

        self._dirname = dirname or self.DEFAULT_DIRNAME

    def dirname(self):
        """
        :rtype: str
        """
        return self._dirname

    def get(self, *args):
        """
        Return the resource path for the given args.

        :rtype: str
        """
        return os.path.join(self.dirname(), *args)

    def icon(self, name, extension="png", color=None):
        """
        Return an Icon object from the given resource name.

        :type name: str
        :type extension: str
        :rtype: QtGui.QIcon
        """
        p = self.pixmap(name, extension=extension, color=color)
        return Icon(p)

    def pixmap(self, name, scope="icons", extension="png", color=None):
        """
        Return a Pixmap object from the given resource name.

        :type name: str
        :type scope: str
        :type extension: str
        :rtype: QtWidgets.QPixmap
        """
        if os.path.exists(name):
            path = name
        else:
            path = self.get(scope, name + "." + extension)

        p = Pixmap(path)

        if color:
            p.setColor(color)

        return p
