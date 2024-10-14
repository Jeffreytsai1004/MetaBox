#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the Scripts directory
scripts_dir = os.path.dirname(os.path.dirname(current_dir))

# Add the Scripts and Animation directories to sys.path if they're not already there
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)
if current_dir not in sys.path:
    sys.path.append(current_dir)

print(f"aTools __init__.py - Current directory: {current_dir}")
print(f"aTools __init__.py - sys.path: {sys.path}")

# Import aTools submodules
try:
    from . import animTools
    print("Attempting to import animTools")
    from . import commonMods
    print("Attempting to import commonMods")
    from . import generalTools
    print("Attempting to import generalTools")

    print("Successfully imported aTools main submodules")

    # Import specific submodules
    from animTools.animBar import animBarUI
    from animTools import animationCrashRecovery, framePlaybackRange, jumpToSelectedKey
    from commonMods import animMod, aToolsMod, commandsMod, uiMod, utilMod
    from generalTools import aToolsClasses, aToolsGlobals, generalToolsUI, hotkeys, offlineInstall, tumbleOnObjects
    print("Successfully imported aTools specific submodules")

except ImportError as e:
    print(f"Warning: Unable to import aTools submodules: {str(e)}")
    print(f"Current sys.path: {sys.path}")

# Print debug information
print(f"aTools successfully imported. Current directory: {current_dir}")
print(f"sys.path: {sys.path}")