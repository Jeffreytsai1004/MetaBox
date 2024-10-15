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

import sys
from imp import reload

import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr

from gs_curvetools.plugins import cv_manip_src  # pyright: ignore

reload(cv_manip_src)

# API parameters
maya_useNewAPI = True


# ------------ Init & UnInit Plugin ------------
def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "GeorgeSladkovsky", "1.3.1", "Any")
    try:
        plugin.registerNode(
            "GSCT_CurveTools_DrawManagerNode",
            cv_manip_src.DrawManagerNode.id,
            cv_manip_src.DrawManagerNode.creator,
            cv_manip_src.DrawManagerNode.initialize,
            om.MPxNode.kLocatorNode,
            cv_manip_src.DrawManagerNode.drawDbClassification)
    except BaseException:
        sys.stderr.write("Failed to register node\n")
        raise

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(
            cv_manip_src.DrawManagerNode.drawDbClassification,
            cv_manip_src.DrawManagerNode.drawRegistrantId,
            cv_manip_src.DrawOverride.creator)
    except BaseException:
        sys.stderr.write("Failed to register override\n")
        raise


def uninitializePlugin(obj):
    om.MMessage.removeCallbacks(cv_manip_src.CALLBACK_IDS)
    cv_manip_src.CALLBACK_IDS = []
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterNode(cv_manip_src.DrawManagerNode.id)
    except BaseException:
        sys.stderr.write("Failed to deregister node\n")
        raise

    try:
        omr.MDrawRegistry.deregisterGeometryOverrideCreator(
            cv_manip_src.DrawManagerNode.drawDbClassification,
            cv_manip_src.DrawManagerNode.drawRegistrantId)
    except BaseException:
        sys.stderr.write("Failed to deregister override\n")
        raise
