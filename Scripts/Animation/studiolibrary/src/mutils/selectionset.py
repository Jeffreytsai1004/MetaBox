#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

import mutils

try:
    import maya.cmds
except Exception:
    import traceback
    traceback.print_exc()


logger = logging.getLogger(__name__)


def saveSelectionSet(path, objects, metadata=None):
    """
    Convenience function for saving a selection set to the given disc location.
    
    :type path: str
    :type objects: list[str]
    :type metadata: dict or None
    :type args: list
    :type kwargs: dict
    :rtype: SelectionSet 
    """
    selectionSet = SelectionSet.fromObjects(objects)

    if metadata:
        selectionSet.updateMetadata(metadata)

    selectionSet.save(path)

    return selectionSet


class SelectionSet(mutils.TransferObject):

    def load(self, objects=None, namespaces=None, **kwargs):
        """
        Load/Select the transfer objects to the given objects or namespaces.
        
        :type objects: list[str] or None
        :type namespaces: list[str] or None
        :type kwargs:
        """
        validNodes = []
        dstObjects = objects
        srcObjects = self.objects()

        self.validate(namespaces=namespaces)

        matches = mutils.matchNames(
                srcObjects,
                dstObjects=dstObjects,
                dstNamespaces=namespaces
        )

        for srcNode, dstNode in matches:
            # Support for wild cards eg: ['*_control'].
            if "*" in dstNode.name():
                validNodes.append(dstNode.name())
            else:
                # Remove the first pipe in-case the object has a parent.
                dstNode.stripFirstPipe()

                # Try to get the short name. Much faster than the int
                # name when selecting objects.
                try:
                    dstNode = dstNode.toShortName()

                except mutils.NoObjectFoundError as error:
                    logger.debug(error)
                    continue

                except mutils.MoreThanOneObjectFoundError as error:
                    logger.debug(error)

                validNodes.append(dstNode.name())

        if validNodes:
            maya.cmds.select(validNodes, **kwargs)

            # Return the focus to the Maya window
            maya.cmds.setFocus("MayaWindow")
        else:
            text = "No objects match when loading data. " \
                   "Turn on debug mode to see more details."

            raise mutils.NoMatchFoundError(text)

    def select(self, objects=None, namespaces=None, **kwargs):
        """
        Convenience method for any classes inheriting SelectionSet.
        
        :type objects: str
        :type namespaces: list[str]
        :rtype: None
        """
        SelectionSet.load(self, objects=objects, namespaces=namespaces, **kwargs)
