#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds

def XrayJoint():
    result = cmds.modelEditor('modelPanel4', q=True, jx=True)
    cmds.modelEditor('modelPanel4', e=True, jx=not result)