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
import base64 as __B64
from datetime import datetime as __DT

import maya.cmds as __mc
from PySide2 import QtWidgets as __QTW


def __getMayaOS():
    """Get Maya version and parent OS"""
    maya = str(__mc.about(api=1))[:4]
    os = str(__mc.about(os=1))
    return [int(maya), os]


MAYA_VER = __getMayaOS()[0]
OS = __getMayaOS()[1]

DEBUG = True

VERSION = __B64.b64decode(b"R1MgQ3VydmVUb29scyB2MS4zLjEKU3R1ZGlvIEVkaXRpb24=").decode('utf-8')

try:
    YEAR = __DT.now().year
except BaseException:
    YEAR = 2023

MAIN_WINDOW_NAME = 'GSCT_CurveTools'
MAIN_WINDOW_LABEL = 'GS CurveTools'
CURVE_CONTROL_NAME = 'GSCT_CurveControl'
CURVE_CONTROL_LABEL = 'GS Curve Control'
UV_EDITOR_NAME = 'GSCT_UVEditor'
UV_EDITOR_LABEL = 'GS Curve Tools UV Editor'
SCALE_FACTOR_UI = 'GSCT_ScaleFactorWindow'

UI_SCRIPT = '''
import gs_curvetools.utils.utils as ct_ut
ct_ut.logger.logger.info("Uninitializing Workspace Control")
maya.cmds.evalDeferred(ct_ut.stopUI)
'''

FIXED_POLICY = __QTW.QSizePolicy(__QTW.QSizePolicy.Fixed,
                                 __QTW.QSizePolicy.Fixed)
PREFERRED_POLICY = __QTW.QSizePolicy(__QTW.QSizePolicy.Preferred,
                                     __QTW.QSizePolicy.Preferred)
EXPANDING_POLICY = __QTW.QSizePolicy(__QTW.QSizePolicy.Expanding,
                                     __QTW.QSizePolicy.Expanding)
