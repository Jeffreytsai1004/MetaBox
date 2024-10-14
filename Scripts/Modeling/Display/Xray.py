#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds

def Xray():
    result = cmds.modelEditor('modelPanel4', q=True, xr=True)
    cmds.modelEditor('modelPanel4', e=True, xr=not result)