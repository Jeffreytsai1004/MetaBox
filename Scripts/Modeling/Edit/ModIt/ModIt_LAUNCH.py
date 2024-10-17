#!/usr/bin/env python
# -*- coding: utf-8 -*-

##-------------------------------------------------------------------------- I M P O R T
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.cmds as cmds
import maya.mel as mel
import json
from .Qt import QtWidgets, QtCore, QtCompat
import os
from maya import OpenMayaUI as omui
from functools import partial
# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
##---------------------------------------- Import Modules
import importlib
from . import ModIt_Global
importlib.reload(ModIt_Global)


##-------------------------------------------------------------------------- G L O B A L   V A R
##PATH_SET
PreferencePath = ModIt_Global.PreferencePath
ToolsPath = ModIt_Global.ToolPath

DOCK =(json.load(open(PreferencePath + 'Dockable.json',"r"))['VALUE'])

if DOCK == 0:
    print("MODIT FLOATING MODE")

    open(PreferencePath + 'UI_Adapt_Height.json', "w").write(json.dumps({"VALUE": 660}))
    open(PreferencePath + 'Section_Utilities.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Primitives.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Colors.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Selections.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Mesh.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Sets.json', "w").write(json.dumps({"VALUE": 1}))
    open(PreferencePath + 'Section_Tools.json', "w").write(json.dumps({"VALUE": 1}))


    from . import ModIt_UI
    importlib.reload(ModIt_UI)
    ui = ModIt_UI
    
else:
    print("MODIT DOCKABLE MODE")
    from . import ModIt_UI
    importlib.reload(ModIt_UI)
    ui = ModIt_UI.showUI()


