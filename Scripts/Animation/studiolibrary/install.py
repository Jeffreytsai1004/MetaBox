#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Drag and drop for Maya 2018+
"""
import os
import sys

import maya.mel as mel
import maya.cmds as cmds


def onMayaDroppedPythonFile(*args, **kwargs):
    """This function is only supported since Maya 2017 Update 3"""
    pass


def  _onMayaDropped():
    """Dragging and dropping this file into the scene executes the file."""
    studiolibrary_path = os.path.dirname(__file__, 'src').replace('\\', '/')
    iconPath = os.path.join(studiolibrary_path, 'studiolibrary', 'resource', 'icons', 'icon.png').replace('\\', '/')

    if not os.path.exists(iconPath):
        raise FileNotFoundError('Cannot find ' + iconPath)

    for path in sys.path:
        if os.path.exists(path + '/studiolibrary/__init__.py'):
            cmds.warning('Studio Library is already installed at ' + path)

    command = '''
# -----------------------------------
# Studio Library
# www.studiolibrary.com
# -----------------------------------

import os
import sys
    
if not os.path.exists(r'{path}'):
    raise FileNotFoundError(r'The source path "{path}" does not exist!')
    
if r'{path}' not in sys.path:
    sys.path.insert(0, r'{path}')
    
import studiolibrary
studiolibrary.main()
'''.format(path=studiolibrary_path)

    shelf = mel.eval('$gShelfTopLevel=$gShelfTopLevel')
    parent = cmds.tabLayout(shelf, query=True, selectTab=True)
    cmds.shelfButton(
        command=command,
        annotation='Studio Library',
        sourceType='Python',
        image=iconPath,
        image1=iconPath,
        parent=parent
    )

    # print("\n// Studio Library has been added to current shelf.")
