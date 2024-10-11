#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import os

WINDOW_NAME = "MorphShape"

class show():
    def __init__(self):
        txt = 'none'
        iconPath = cmds.internalVar(userScriptDir=True)
        print(iconPath)
        buttColor=[0.53, 0.81, 0.98]
        self.baseMesh=None
        win = 'MorphShape'
        if cmds.window(win,exists=True):
            cmds.deleteUI(win)
        window = cmds.window("MorphShape", t=WINDOW_NAME, w=200, h=100)
        cmds.columnLayout('mainColumn',adj = True)
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the icon
        icon_path = os.path.join(current_dir, 'MorphShapeLogo.png')
        
        # Display the icon in the UI
        cmds.image(image=icon_path)
        
        cmds.text(l='')
        cmds.text('baseMeshName', l='Ref Mesh : '+ str(self.baseMesh))
        cmds.button(l='Set Reference Mesh', c=self.setBaseMesh, p='mainColumn')
        cmds.text(l='')
        cmds.text(l='Position Old Mesh')
        self.xPos = cmds.intSliderGrp(min=-50, max=50, value=0, step=1 ,field=True,l='xPos')
        self.yPos = cmds.intSliderGrp(min=-50, max=50, value=0, step=1 ,field=True,l='yPos')
        self.zPos = cmds.intSliderGrp(min=-50, max=50, value=0, step=1 ,field=True,l='zPos')
        cmds.text(l='')
        self.strength = cmds.intSliderGrp(min=1, max=100, value=50, step=1 ,field=True,l='strength')
        self.iterations = cmds.intSliderGrp(min=1, max=50, value=3, step=1 ,field=True,l='iterations')
        
        
        cmds.text(l='')
        cmds.button(l='MorphShape',c=self.morph, p='mainColumn', bgc=buttColor)
        cmds.text(l='')
        cmds.showWindow(win)
        

    def morph(self, *args):
        selection = cmds.ls(sl=True)[0]
        cmds.select(self.baseMesh)
        dupBaseMesh = cmds.duplicate(n='Delta')
        cmds.blendShape(selection, dupBaseMesh,n='deltaShape')
        val = cmds.intSliderGrp(self.iterations,q=True,v=True)
        mult = cmds.intSliderGrp(self.strength,q=True,v=True)
        xPos = cmds.intSliderGrp(self.xPos,q=True,v=True)
        yPos = cmds.intSliderGrp(self.yPos,q=True,v=True)
        zPos = cmds.intSliderGrp(self.zPos,q=True,v=True)
        for i in range(val):
            cmds.deltaMush(dupBaseMesh,si=mult)
            #fix jaggies with secondary delta mush
            cmds.deltaMush(dupBaseMesh,si=3)
        cmds.blendShape( 'deltaShape', edit=True, w=[0,1.0] )
        cmds.delete(dupBaseMesh, constructionHistory = True)
        pos = cmds.xform(selection, q=1, t=True, ws=True)
        cmds.xform(dupBaseMesh,t=pos)
        cmds.xform(selection, t=[xPos,yPos,zPos], r=True)
        cmds.select(dupBaseMesh)
        
    def setBaseMesh(self, *args):
        self.baseMesh = cmds.ls(sl=True)[0]
        cmds.text('baseMeshName',e=True,l='Ref Mesh : '+ str(self.baseMesh))
    
if __name__ == "__main__":
    show()