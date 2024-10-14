#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from maya import mel # type: ignore
from generalTools.aToolsGlobals import aToolsGlobals as G
from commonMods import utilMod
from commonMods import aToolsMod
import importlib

def install(offline=None, unistall=False):    
       
    mayaAppDir      = mel.eval('getenv MAYA_APP_DIR')
    scriptsDir      = "%s%sscripts"%(mayaAppDir, os.sep)
    userSetupFile   = scriptsDir + os.sep + "userSetup.py"  
    newUserSetup    = ""  
    
    
    try:
        with open(userSetupFile, 'r'):
            
            input = open(userSetupFile, 'r')
            lines = input.readlines()  
            
            # clear old aTool codes, if there is any
            write = True
            for n, line in enumerate(lines):        
                if line.find("# start aTools") == 0:
                    write = False
                    
                if write: newUserSetup += line
                    
                if line.find("# end aTools") == 0:
                    write = True
                    
    except IOError:
        newUserSetup    = ""
    
    aToolCode  = "# start aTools\n\nfrom maya import cmds\nif not cmds.about(batch=True):\n\n    # launch aTools_Animation_Bar\n    cmds.evalDeferred(\"from aTools.animTools.animBar import animBarUI; animBarUI.show('launch')\", lowestPriority=True)\n\n# end aTools"    
        
    if not unistall: newUserSetup    += aToolCode
    
    # write user setup file
    output = open(userSetupFile, 'w')
    output.write(newUserSetup)
    output.close()
    
    
    if offline:        
        
        offlineFilePath = offline[0]
        createMelFile   = offline[1]
        offlineFolder   = os.sep.join(offlineFilePath.split(os.sep)[:-1])
        fileModTime     = os.path.getmtime(offlineFilePath)
        
        aToolsMod.saveInfoWithUser("userPrefs", "offlinePath", [offlineFolder, fileModTime]) 
        if createMelFile == True: createOfflineMelFile(offlineFolder, scriptsDir)
    
    
    #open tool
    if not unistall:
        from animTools.animBar import animBarUI; importlib.reload(animBarUI)
        animBarUI.show()
    
        
        
def createOfflineMelFile(offlineFolder, scriptsDir):
    offlineInstallPy    = os.path.join(offlineFolder, "offlineInstall.py").replace("\\", "/")
    offlineInstallMel   = os.path.join(scriptsDir, "aTools_offlineInstall.mel").replace("\\", "/")
    
    # 修改这一部分
    pyContents = utilMod.readFile(offlineInstallPy)
    if isinstance(pyContents, str):
        pyContents = pyContents.split('\n')
    elif not isinstance(pyContents, (list, tuple)):
        pyContents = [str(pyContents)]
    pyContents = "\\n\\".join(pyContents)
    
    melContents         = """python("execfile('%s')")""" % offlineInstallPy.replace("\\", "/")
    
    utilMod.writeFile(offlineInstallMel, melContents)
