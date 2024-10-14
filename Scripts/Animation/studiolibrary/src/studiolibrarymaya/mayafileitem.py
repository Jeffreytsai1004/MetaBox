#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE: Make sure you register this item in the config.
"""

import os
import logging

import maya.cmds

from studiolibrarymaya import baseitem


logger = logging.getLogger(__name__)


class MayaFileItem(baseitem.BaseItem):

    NAME = "Maya File"
    TYPE = NAME
    EXTENSION = ".mayafile"
    ICON_PATH = os.path.join(os.path.dirname(__file__), "icons", "file.png")

    def transferPath(self):
        return self.path() + "/mayafile.ma"

    def loadSchema(self, **kwargs):
        """
        Get the schema used for loading the example item.

        :rtype: list[dict]
        """
        return []

    def load(self, **kwargs):
        """
        The load method is called with the user values from the load schema.

        :type kwargs: dict
        """
        logger.info("Loading %s %s", self.path(), kwargs)

        maya.cmds.file(
            self.transferPath(),
            i=True,
            type="mayaAscii",
            options="v=0;",
            preserveReferences=True,
            mergeNamespacesOnClash=False,
        )

    def saveSchema(self, **kwargs):
        """
        Get the schema used for saving the example item.

        :rtype: list[dict]
        """
        return [
            # The 'name' field and the 'folder' field are both required by
            # the BaseItem. How this is handled may change in the future.
            {
                "name": "folder",
                "type": "path",
                "layout": "vertical",
                "visible": False,
            },
            {
                "name": "name",
                "type": "string",
                "layout": "vertical"
            },
            {
                "name": "objects",
                "type": "objects",
                "layout": "vertical"
            },
        ]

    def save(self, **kwargs):
        """
        The save method is called with the user values from the save schema.

        :type kwargs: dict
        """
        logger.info("Saving %s %s", self.path(), kwargs)

        super(MayaFileItem, self).save(**kwargs)

        maya.cmds.file(
            self.transferPath(),
            type="mayaAscii",
            options="v=0;",
            preserveReferences=True,
            exportSelected=True
        )
