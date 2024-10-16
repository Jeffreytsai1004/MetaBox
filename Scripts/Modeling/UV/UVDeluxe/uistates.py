#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os
import maya.cmds as mc

version = 120

class UiStates():
    file = 'config.uvd'
    filepath = os.path.join(os.path.dirname(__file__), file)

    def __init__(self):
        self.version = version
        #Window
        self.widthHeight = (1150,700)
        self.collapseFrame0 = False
        self.collapseFrame1 = True
        self.collapseFrame2 = True
        self.collapseFrame3 = True
        self.collapseFrame4 = True
        self.collapseFrame5 = True
        self.collapseFrame6 = True
        self.collapseFrame7 = True
        self.collapseFrame8 = True

        #Settings
        #self.textureSize        = (5,5)
        #self.forgetTextureSize  = False
        self.detectTextureSize  = True
        self.retainCS  = mc.texMoveContext('texMoveContext',q=True,scr=True)
        self.matchDist = 0.05

        #Quicksnap
        self.snapPath = mc.workspace(q=True,rd=True)

    @staticmethod
    def pickleDump(uis):
        with open(UiStates.filepath, 'wb') as datafile:
            pickle.dump(uis, datafile)

    @staticmethod
    def pickleLoad():
        if os.path.exists(UiStates.filepath):
            print("%s found, loading settings." % UiStates.file)
            try:
                with open(UiStates.filepath, 'rb') as datafile:
                    uis = pickle.load(datafile)
            except EOFError:
                print("Warning: The file is empty or corrupted.")
                os.remove(UiStates.filepath)
                return UiStates()
            except Exception as e:
                print(f"Error loading settings: {e}")
                os.remove(UiStates.filepath)
                return UiStates()
            try:
                pickledVer = uis.version
                if pickledVer < version:
                    os.remove(UiStates.filepath)
                    return UiStates()
            except:
                os.remove(UiStates.filepath)
                return UiStates()
            return uis
        else:
            return UiStates()


    def setUiState(self):
        #Window
        self.widthHeight    = mc.window('UVDeluxe',query=True,wh=True)
        self.collapseFrame0 = mc.frameLayout('layout_Settings',     query=True, cl=True)
        self.collapseFrame1 = mc.frameLayout('layout_Mover',        query=True, cl=True)
        self.collapseFrame2 = mc.frameLayout('layout_Scaler',       query=True, cl=True)
        self.collapseFrame3 = mc.frameLayout('layout_Ratio',        query=True, cl=True)
        self.collapseFrame4 = mc.frameLayout('layout_Straighten',   query=True, cl=True)
        self.collapseFrame5 = mc.frameLayout('layout_Align',        query=True, cl=True)
        self.collapseFrame6 = mc.frameLayout('layout_QuickSnap',    query=True, cl=True)
        self.collapseFrame7 = mc.frameLayout('layout_MatchUV',      query=True, cl=True)
        self.collapseFrame8 = mc.frameLayout('layout_SelectionSets',query=True, cl=True)

        self.detectTextureSize  = mc.checkBox   ('DTR',             query=True, v=True)

        self.retainCS = mc.texMoveContext('texMoveContext',q=True,scr=True)
        #Qucksnap
        self.snapPath = mc.textField("pathField",query=True,text=True)
        ''' Dump '''
        UiStates.pickleDump(self)
