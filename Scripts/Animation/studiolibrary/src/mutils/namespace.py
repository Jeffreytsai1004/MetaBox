#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

try:
    import maya.cmds
except ImportError:
    traceback.print_exc()


__all__ = [
    "getAll",
    "getFromDagPath",
    "getFromDagPaths",
    "getFromSelection",
]


def getFromDagPaths(dagPaths):
    """
    :type dagPaths: list[str]
    :rtype: list[str]
    """
    namespaces = []

    for dagPath in dagPaths:
        namespace = getFromDagPath(dagPath)
        namespaces.append(namespace)

    return list(set(namespaces))


def getFromDagPath(dagPath):
    """
    :type dagPath: str
    :rtype: str
    """
    shortName = dagPath.split("|")[-1]
    namespace = ":".join(shortName.split(":")[:-1])
    return namespace


def getFromSelection():
    """
    :rtype: list[str]
    """
    dagPaths = maya.cmds.ls(selection=True)
    return getFromDagPaths(dagPaths)


def getAll():
    """
    Get all the available namespaces in the scene
    
    :rtype: list[str] 
    """
    IGNORE_NAMESPACES = ['UI', 'shared']

    namespaces = maya.cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True)
    namespaces = list(set(namespaces) - set(IGNORE_NAMESPACES))
    namespaces = sorted(namespaces)

    return namespaces
