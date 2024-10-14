#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from studioqt import Icon
from studioqt import Pixmap

from . import utils


PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
RESOURCE_DIRNAME = os.path.join(DIRNAME, "resource")


def get(*args):
    """
    This is a convenience function for returning the resource path.

    :rtype: str 
    """
    path = os.path.join(RESOURCE_DIRNAME, *args)
    return utils.normPath(path)


def icon(*args, **kwargs):
    """
    Return an Icon object from the given resource name.

    :rtype: str
    """
    path = get("icons", *args)
    return Icon(pixmap(path, **kwargs))


def pixmap(name, scope="icons", extension="png", color=None):
    """
    Return a Pixmap object from the given resource name.

    :type name: str
    :type scope: str
    :type extension: str
    :type color: str
    :rtype: QtWidgets.QPixmap
    """
    if name.endswith(".svg"):
        extension = ""

    path = ""

    if os.path.exists(name):
        path = name

    elif extension:
        path = get(scope, name + "." + extension)
        if not os.path.exists(path):
            path = get(scope, name + ".svg")

    p = Pixmap(path)

    if color:
        p.setColor(color)

    return p
