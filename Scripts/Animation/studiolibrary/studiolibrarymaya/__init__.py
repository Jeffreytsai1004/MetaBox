#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

import studiolibrary

import mutils
import studioqt

from .main import main


__encoding__ = sys.getfilesystemencoding()

PATH = str(os.path.abspath(__file__), __encoding__)
DIRNAME = os.path.dirname(PATH).replace('\\', '/')
RESOURCE_DIRNAME = DIRNAME + "/resource"

DEFAULT_FILE_TYPE = "mayaBinary"
SETTINGS_PATH = studiolibrary.localPath("LibraryItem.json")

_resource = None
_settings = None
_mayaCloseScriptJob = None


def readSettings():
    """
    Return the local settings from the location of the SETTING_PATH.

    :rtype: dict
    """
    return studiolibrary.readJson(SETTINGS_PATH)


def saveSettings(data):
    """
    Save the given dict to the local location of the SETTING_PATH.

    :type data: dict
    :rtype: None
    """
    global _settings
    _settings = None

    studiolibrary.updateJson(SETTINGS_PATH, data)


def resetSettings():
    """Remove and reset the item settings."""
    global _settings
    _settings = None
    studiolibrary.removePath(SETTINGS_PATH)


def settings():
    """
    Return the local settings for importing and exporting an animation.

    :rtype: studiolibrary.Settings
    """
    global _settings

    if not _settings:
        _settings = readSettings()

    # Shared options
    _settings.setdefault("namespaces", [])
    _settings.setdefault("namespaceOption", "file")

    _settings.setdefault("iconToggleBoxChecked", True)
    _settings.setdefault("infoToggleBoxChecked", True)
    _settings.setdefault("optionsToggleBoxChecked", True)
    _settings.setdefault("namespaceToggleBoxChecked", True)

    # Anim options
    _settings.setdefault('byFrame', 1)
    _settings.setdefault('fileType', DEFAULT_FILE_TYPE)
    _settings.setdefault('currentTime', False)
    _settings.setdefault('connectOption', False)
    _settings.setdefault('showHelpImage', False)
    _settings.setdefault('pasteOption', "replace")

    # Pose options
    _settings.setdefault("keyEnabled", False)
    _settings.setdefault("mirrorEnabled", False)

    # Mirror options
    _settings.setdefault("mirrorOption", mutils.MirrorOption.Swap)
    _settings.setdefault("mirrorAnimation", True)

    return _settings


def resource():
    """
    :rtype: studioqt.Resource
    """
    global _resource

    if not _resource:
        _resource = studioqt.Resource(RESOURCE_DIRNAME)

    return _resource


def registerItems():
    """
    The following items are registered on import at the bottom of each file.
    
    :rtype: None 
    """
    from studiolibrarymaya import animitem
    from studiolibrarymaya import poseitem
    from studiolibrarymaya import mirroritem
    from studiolibrarymaya import setsitem


def enableMayaClosedEvent():
    """
    Create a Maya script job to trigger on the event "quitApplication".

    Enable the Maya closed event to save the library settings on close

    :rtype: None
    """
    global _mayaCloseScriptJob

    if not _mayaCloseScriptJob:
        event = ['quitApplication', mayaClosedEvent]
        try:
            _mayaCloseScriptJob = mutils.ScriptJob(event=event)
        except NameError as error:
            logging.exception(error)


def mayaClosedEvent():
    """
    Create a Maya script job to trigger on the event "quitApplication".

    :rtype: None
    """
    for libraryWindow in studiolibrary.LibraryWindow.instances():
        libraryWindow.saveSettings()


def setDebugMode(libraryWindow, value):
    """
    Triggered when the user chooses debug mode.

    :type libraryWindow: studiolibrary.LibraryWindow
    :type value: int
    :rtype: None
    """
    if value:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logger_ = logging.getLogger("mutils")
    logger_.setLevel(level)

    logger_ = logging.getLogger("studiolibrarymaya")
    logger_.setLevel(level)


studiolibrary.LibraryWindow.globalSignal.debugModeChanged.connect(setDebugMode)
