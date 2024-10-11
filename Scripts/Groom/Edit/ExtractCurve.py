#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel

def run():
    mel.eval('polyToCurve -form 2 -degree 3 -conformToSmoothMeshPreview 1')