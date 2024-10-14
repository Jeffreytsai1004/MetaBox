#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


__version__ = "2.4.15"

_config = None
_resource = None


PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
RESOURCE_PATH = os.path.join(DIRNAME, "resource")


class Config(dict):
    """
    A custom config parser for passing JSON files.
    
    We use this instead of the standard ConfigParser as the JSON format
    can support list and dict types.
    
    This parser can also support comments using the following style "//"
    """

    @staticmethod
    def paths():
        """
        Return all possible config paths.
        
        :rtype: list[str] 
        """
        cwd = os.path.dirname(__file__)
        paths = [os.path.join(cwd, "config", "default.json")]

        path = os.environ.get("STUDIO_LIBRARY_CONFIG_PATH")
        path = path or os.path.join(cwd, "config", "config.json")

        if not os.path.exists(path):
            cwd = os.path.dirname(os.path.dirname(cwd))
            path = os.path.join(cwd, "config", "config.json")

        if os.path.exists(path):
            paths.append(path)

        return paths

    def read(self):
        """Read all paths and overwrite the keys with each successive file."""
        self.clear()

        for path in self.paths():
            lines = []

            with open(path) as f:
                for line in f.readlines():
                    if not line.strip().startswith('//'):
                        lines.append(line)

            data = '\n'.join(lines)
            if data:
                self.update(json.loads(data))


def config():
    """
    Read the config data for the current environment.

    :rtype: Config 
    """
    global _config

    if not _config:
        _config = Config()
        _config.read()

    return _config


def version():
    """
    Return the current version of the Studio Library

    :rtype: str
    """
    return __version__


def resource():
    """
    Return a resource object for getting content from the resource folder.

    :rtype: studioqt.Resource
    """
    global _resource

    if not _resource:
        _resource = studioqt.Resource(RESOURCE_PATH)

    return _resource


import studioqt

from studiolibrary.utils import *
from studiolibrary.library import Library
from studiolibrary.libraryitem import LibraryItem
from studiolibrary.librarywindow import LibraryWindow
from studiolibrary.main import main

import studiolibrary.folderitem

# Wrapping the following functions for convenience
app = studioqt.app
