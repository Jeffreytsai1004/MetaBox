#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

License:
This collection of code named GS CurveTools is a property of George Sladkovsky (Yehor Sladkovskyi)
and can not be copied or distributed without his written permission.

GS CurveTools v1.3.1 Studio
Copyright 2023, George Sladkovsky (Yehor Sladkovskyi)
All Rights Reserved

Autodesk Maya is a property of Autodesk, Inc.

Social Media and Contact Links:

Discord Server:       https://discord.gg/f4DH6HQ
Online Store:         https://sladkovsky3d.artstation.com/store
Online Documentation: https://gs-curvetools.readthedocs.io/
Twitch Channel:       https://www.twitch.tv/videonomad
YouTube Channel:      https://www.youtube.com/c/GeorgeSladkovsky
ArtStation Portfolio: https://www.artstation.com/sladkovsky3d
Contact Email:        george.sladkovsky@gmail.com

"""

import csv
import io
import os
from imp import reload

import maya.cmds as mc
import maya.mel as mel

from .constants import *
from .utils import utils

reload(utils)


def getHotkeys():
    path = os.path.dirname(os.path.realpath(__file__)) + '/utils/hotkeys.csv'
    with io.open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        return list(reader)


class Init:

    def __init__(self):
        if mc.workspaceControl('GSCT_CurveTools', q=1, ex=1):
            utils.stopUI(True)
        if mc.workspaceControlState('GSCT_CurveTools', q=1, ex=1):
            mc.workspaceControlState('GSCT_CurveTools', r=1)

        utils.resetOptionVars()

        # Init Runtime Command
        self.delRuntimeCmds()

        # Get hotkeys from csv file
        hotkeys = getHotkeys()

        for i in range(len(hotkeys)):
            cmd = 'import gs_curvetools\ntry:\n    ' + hotkeys[i][1] + '\nexcept:\n    print("This function requires GS CurveTools.")'
            commandName = 'GSCT_' + hotkeys[i][0].strip().replace(' ', '_')
            if not mc.runTimeCommand(commandName, ex=1):
                mc.runTimeCommand(
                    commandName,
                    c=cmd,
                    ann=hotkeys[i][2],
                    cat=hotkeys[i][3],
                    cl=hotkeys[i][4]
                )
            else:
                mc.runTimeCommand(commandName, e=1, delete=1)
                mc.runTimeCommand(
                    commandName,
                    c=cmd,
                    ann=hotkeys[i][2],
                    cat=hotkeys[i][3],
                    cl=hotkeys[i][4]
                )

        # Shelf
        folder = utils.getFolder.icons()
        shelf = mel.eval('$gsTempShelfTopLevel = $gShelfTopLevel')
        ui = 'import gs_curvetools.main as ct_main\nct_main.main()'
        uiIcon = folder + 'gsCurveToolsIcon_ui.png'
        reset = 'import gs_curvetools.utils.utils as ct_ut\nfrom imp import reload\nreload(ct_ut)\nct_ut.resetUI()'
        resetIcon = folder + 'gsCurveToolsIcon_reset.png'
        stop = 'import gs_curvetools.utils.utils as ct_ut\nfrom imp import reload\nreload(ct_ut)\nct_ut.stopUI()'
        stopIcon = folder + 'gsCurveToolsIcon_stop.png'
        if MAYA_VER <= 2018:
            uiIcon = folder + 'gsCurveToolsIcon_ui_legacy.png'
            resetIcon = folder + 'gsCurveToolsIcon_reset_legacy.png'
            stopIcon = folder + 'gsCurveToolsIcon_stop_legacy.png'
        if mc.tabLayout(shelf, ex=1):
            allTabs = mc.tabLayout(shelf, q=1, tl=1)
            ex = False
            for ele in allTabs:
                if ele == 'GS':
                    ex = True
                    break
            if not ex:
                mel.eval('addNewShelfTab ("GS");')
            mc.tabLayout(shelf, e=1, st='GS')
            buttons = mc.shelfLayout(shelf + '|GS', q=1, ca=1)
            if buttons:
                for button in buttons:
                    if mc.shelfButton(button, q=1, l=1) == 'GS_CurveTools'\
                            or mc.shelfButton(button, q=1, l=1) == 'GS_CurveTools_Reset'\
                            or mc.shelfButton(button, q=1, l=1) == 'GS_CurveTools_Stop':
                        mc.deleteUI(button, ctl=1)
                        mel.eval('shelfTabRefresh;')
            currentShelf = mc.tabLayout(shelf, q=1, st=1)
            mc.setParent(currentShelf)
            mc.shelfButton(style=mc.shelfLayout(currentShelf, query=1, style=1),
                           sourceType="python",
                           label="GS_CurveTools",
                           width=mc.shelfLayout(currentShelf, query=1, cellWidth=1),
                           command=ui,
                           image1=uiIcon,
                           height=mc.shelfLayout(currentShelf, query=1, cellHeight=1),
                           annotation="Toggle GS CurveTools Window")
            mc.shelfButton(style=mc.shelfLayout(currentShelf, query=1, style=1),
                           sourceType="python",
                           label="GS_CurveTools_Reset",
                           width=mc.shelfLayout(currentShelf, query=1, cellWidth=1),
                           command=reset,
                           image1=resetIcon,
                           height=mc.shelfLayout(currentShelf, query=1, cellHeight=1),
                           annotation="GS CurveTools Reset to Defaults")
            mc.shelfButton(style=mc.shelfLayout(currentShelf, query=1, style=1),
                           sourceType="python",
                           label="GS_CurveTools_Stop",
                           width=mc.shelfLayout(currentShelf, query=1, cellWidth=1),
                           command=stop,
                           image1=stopIcon,
                           height=mc.shelfLayout(currentShelf, query=1, cellHeight=1),
                           annotation="GS CurveTools Stop Scripts")
        msg = '<div style="text-align: center;">GS CurveTools Initialized Successfully!\n\
			Welcome!\n</div>\
			<div style="text-align: left;"><img src="%s" width="36" height="32"/> - Launches the menu.\n\
			<span style="color: #5285a6;"><img src="%s" width="36" height="32"/></span> - Resets the menu to default values.\n\
			<span style="color: #5285a6;"><img src="%s" width="36" height="32"/></span> - Closes the menu and stops all background scripts.\n</div>\
			<div style="text-align: center;">To close this message simply click on it.\n\
			Have fun! :)</div>\
			<div>\n</div>\
			<div>\n</div>\
			<div>\n</div>\
			<div>\n</div>\
			<div>\n</div>' % (uiIcon, resetIcon, stopIcon)
        mc.inViewMessage(msg=msg, a=1, pos='topCenter', fade=True, ck=1, fst=60000)

    def __repr__(self):
        return 'GS CurveTools Initialized'

    def delRuntimeCmds(self):
        commands = mc.runTimeCommand(q=1, ca=1)
        for command in commands:
            if 'GSCT_' in command:
                mc.runTimeCommand(command, e=1, delete=1)
