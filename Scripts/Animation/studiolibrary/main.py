import os
import sys
import imp

import maya.mel as mel
import maya.cmds as cmds

def studio_library_install():
    current_path = os.path.dirname(__file__)
    filename = os.path.join(current_path, 'install.py')
    imp.load_source('_studioLibraryInstall', filename)

studio_library_install()
