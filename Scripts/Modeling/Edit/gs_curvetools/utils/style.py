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

import math
from imp import reload

import maya.cmds as mc

from . import utils

reload(utils)

# Scaling

MULT = 1
if mc.about(mac=True):
    MULT = 1
else:
    MULT = mc.mayaDpiSetting(q=1, rsv=1)
    # mult = 1


def scale(a):
    # types (int\float) -> (float)
    if isinstance(a, list):
        return [i * MULT for i in a]
    else:
        return a * MULT


# Fonts
NORMAL_FONT = 11 * MULT
SMALL_FONT = 10 * MULT

# Normal Button
BUTTON_HEIGHT = 24 * MULT
BORDER_RADIUS = 4 * MULT
BORDER_WIDTH = 2 * MULT
BACKGROUND_COLOR = 'rgb(93,93,93)'
PRESSED_BACKGROUND_COLOR = 'rgb(128,128,128)'
HOVER_BACKGROUND_COLOR = 'rgb(100,100,100)'

# Active Button (Orange)
ORANGE = 'rgb(219,148,86)'
ORANGE_HOVER = 'rgb(225,155,90)'
ORANGE_PRESSED = 'rgb(235,170,105)'

# Active Button (Blue)
BLUE = 'rgb(82,133,166)'
BLUE_HOVER = 'rgb(95,145,185)'

# Active Button (White)
BORDER_WIDTH_WHITE = 2 * MULT

# Small Button
SMALL_BORDER_RADIUS = 4 * MULT
SMALL_BORDER_WIDTH = 1 * MULT
SMALL_BORDER_COLOR = 'rgb(93,93,93)'
SMALL_BACKGROUND_COLOR = 'rgba(93,93,93,0)'
SMALL_PRESSED_COLOR = 'rgba(128,128,128,255)'
SMALL_HOVER_COLOR = 'rgb(100,100,100)'

# Layer/Set Button
LAYER_BOTTOM_PADDING = 1 * MULT
LAYER_BORDER_RADIUS = 4 * MULT
LAYER_HEIGHT = 16 * MULT
LAYER_BORDER_WIDTH = 1 * MULT

# Images/Icons
DROP_DOWN_ARROW_IMAGE = utils.getFolder.icons() + 'drop-down-arrow.png'

### Regular Buttons ###

buttonNormal = '''
    QPushButton {{
        background-color: {bg_clr};
        border-radius: {br};
        min-height: {h}px;
        max-height: {h}px;
    }}
    QPushButton:pressed {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked {{
        background-color: {ac_bg_clr};
    }}
    QPushButton:hover {{
        background-color: {h_bg_clr};
    }}
}}
'''.format(br=int(BORDER_RADIUS),
           h=int(BUTTON_HEIGHT),
           bg_clr=str(BACKGROUND_COLOR),
           pr_bg_clr=str(PRESSED_BACKGROUND_COLOR),
           h_bg_clr=str(HOVER_BACKGROUND_COLOR),
           ac_bg_clr=BLUE)

buttonNormalBlueBorder = '''
QPushButton
{{
    background-color: {bg_clr};
    border-radius: {br};
    border-color: {borderBlue};
    border-style: solid;
    border-width: {bw}px;
    padding: -{bw}px;
    min-height: {h}px;
    max-height: {h}px;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    background-color: {ac_bg_clr};
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(BORDER_RADIUS),
           h=int(BUTTON_HEIGHT),
           bw=int(BORDER_WIDTH),
           bg_clr=str(BACKGROUND_COLOR),
           pr_bg_clr=str(PRESSED_BACKGROUND_COLOR),
           h_bg_clr=str(HOVER_BACKGROUND_COLOR),
           borderBlue=str(BLUE),
           ac_bg_clr=BLUE)

buttonIcon = '''
    QPushButton
    {{
        background-color: none;
        border-radius: {br}px;
        border:none;
    }}
    QPushButton:checked
    {{
        background-color: none;
        border:none;
    }}
    QPushButton:pressed
    {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked:pressed
    {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked:hover
    {{
        background-color: {h_bg_clr};
    }}
    QPushButton:hover
    {{
        background-color: {h_bg_clr};
    }}
}}
'''.format(br=int(BORDER_RADIUS / 2),
           h=int(BUTTON_HEIGHT),
           bg_clr=str(BACKGROUND_COLOR),
           pr_bg_clr=str(PRESSED_BACKGROUND_COLOR),
           h_bg_clr=str(HOVER_BACKGROUND_COLOR),
           ac_bg_clr=BLUE)

buttonActiveOrange = '''
QPushButton
{{
    background-color: {bg_clr};
    border-radius: {br}px;
    min-height: {h}px;
    max-height: {h}px;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(BORDER_RADIUS),
           h=int(BUTTON_HEIGHT),
           bg_clr=ORANGE,
           pr_bg_clr=str(ORANGE_PRESSED),
           h_bg_clr=str(ORANGE_HOVER),
           ac_bg_clr=BLUE)

buttonActiveBlue = '''
QPushButton
{{
    background-color: {bg_clr};
    border-radius: {br}px;
    min-height: {h}px;
    max-height: {h}px;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(BORDER_RADIUS),
           h=int(BUTTON_HEIGHT),
           bg_clr=BLUE,
           pr_bg_clr=str(PRESSED_BACKGROUND_COLOR),
           h_bg_clr=str(HOVER_BACKGROUND_COLOR),
           ac_bg_clr=BLUE)

buttonActiveWhite = '''
QPushButton
{{
    background-color: {bg_clr};
    border-radius: {br}px;
    border-width: {bw}px;
    border-color: white;
    border-style: solid;
    padding: -{bw}px;
    min-height: {h}px;
    max-height: {h}px;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:hover
{{
    background-color: {bg_clr};
}}
'''.format(br=int(BORDER_RADIUS),
           h=int(BUTTON_HEIGHT),
           bw=int(BORDER_WIDTH_WHITE),
           bg_clr=ORANGE,
           pr_bg_clr=str(PRESSED_BACKGROUND_COLOR))

frameButton = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: {bw}px;
    border-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
    border-top-left-radius: {br}px;
    border-top-right-radius: {br}px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}}
QPushButton:disabled
{{
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
}}
'''.format(br=4 * MULT,
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           ac_bg_clr=BLUE)

frameButtonNotCollapsable = '''
QPushButton
{{
    background-color: {bg_clr};
    border-style: solid;
    border-width: {bw}px;
    border-top-left-radius: {br}px;
    border-top-right-radius: {br}px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}}
'''.format(br=4 * MULT,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=BACKGROUND_COLOR)

smallNormal = '''
    QPushButton {{
        background-color: {bg_clr};
        border-width: {bw}px;
        border-radius: {br}px;
        border-color: {br_clr};
        border-style: solid;
    }}
    QPushButton:pressed {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked {{
        background-color: {ac_bg_clr};
        border-color: lightgrey;
        border-style: solid;
        border-width: {bw}px;
    }}
    QPushButton:disabled {{
        border-style: none;
    }}
    QPushButton:disabled:checked {{
        background-color: {bg_clr};
        border-style: none;
    }}
    QPushButton:hover {{
        background-color: {h_bg_clr};
    }}
    QPushButton:checked:hover {{
        background-color: {h_bg_checked_clr};
    }}
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=SMALL_BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           h_bg_checked_clr=BLUE_HOVER,
           ac_bg_clr=BLUE)

smallFilled = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: {bw}px;
    border-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
}}
QPushButton:disabled
{{
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           ac_bg_clr=BLUE)

smallFilledBlue = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: {bw}px;
    border-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
}}
QPushButton:disabled
{{
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=BLUE,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=BLUE,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=BLUE_HOVER,
           ac_bg_clr=BLUE)

smallNoBorder = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: 0px;
    border-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    color: rgb(255,0,0)
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
}}
QPushButton:disabled
{{
    color: rgb(255,0,0);
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=SMALL_BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           ac_bg_clr=BLUE)

sliderLabel = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: 0px;
    border-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {bg_clr};
}}
QPushButton:checked
{{
    color: rgb(255,0,0)
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
}}
QPushButton:disabled
{{
    color: rgb(255,0,0);
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=SMALL_BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           ac_bg_clr=BLUE)

### Compound Buttons ###

smallCompoundTopLeft = '''
    QPushButton {{
        background-color: {bg_clr};
        border-width: {bw}px;
        border-top-left-radius: {br}px;
        border-top-right-radius: 0px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
        border-color: {br_clr};
        border-style: solid;
    }}
    QPushButton:pressed {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked {{
        background-color: {ac_bg_clr};
        border-color: lightgrey;
        border-style: solid;
        border-width: {bw}px;
    }}
    QPushButton:disabled {{
        border-style: none;
    }}
    QPushButton:disabled:checked {{
        background-color: {bg_clr};
        border-style: none;
    }}
    QPushButton:hover {{
        background-color: {h_bg_clr};
    }}
    QPushButton:checked:hover {{
        background-color: {h_bg_checked_clr};
    }}
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=SMALL_BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           h_bg_checked_clr=BLUE_HOVER,
           ac_bg_clr=BLUE)

smallCompoundTopRight = '''
    QPushButton {{
        background-color: {bg_clr};
        border-width: {bw}px;
        border-top-left-radius: 0px;
        border-top-right-radius: {br}px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
        border-color: {br_clr};
        border-style: solid;
    }}
    QPushButton:pressed {{
        background-color: {pr_bg_clr};
    }}
    QPushButton:checked {{
        background-color: {ac_bg_clr};
        border-color: lightgrey;
        border-style: solid;
        border-width: {bw}px;
    }}
    QPushButton:disabled {{
        border-style: none;
    }}
    QPushButton:disabled:checked {{
        background-color: {bg_clr};
        border-style: none;
    }}
    QPushButton:hover {{
        background-color: {h_bg_clr};
    }}
    QPushButton:checked:hover {{
        background-color: {h_bg_checked_clr};
    }}
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=SMALL_BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           h_bg_checked_clr=BLUE_HOVER,
           ac_bg_clr=BLUE)

smallFilledCompoundBottom = '''
QPushButton
{{
    background-color: {bg_clr};
    border-width: {bw}px;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: {br}px;
    border-bottom-right-radius: {br}px;
    border-color: {br_clr};
    border-style: solid;
}}
QPushButton:pressed
{{
    background-color: {pr_bg_clr};
}}
QPushButton:checked
{{
    background-color: {ac_bg_clr};
    border-color: lightgrey;
    border-style: solid;
    border-width: {bw}px;
}}
QPushButton:disabled
{{
    border-style: none;
}}
QPushButton:disabled:checked
{{
    background-color: {bg_clr};
    border-style: none;
}}
QPushButton:hover
{{
    background-color: {h_bg_clr};
}}
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           bg_clr=BACKGROUND_COLOR,
           pr_bg_clr=SMALL_PRESSED_COLOR,
           h_bg_clr=SMALL_HOVER_COLOR,
           ac_bg_clr=BLUE)

### Layer Button ###


def layer(background_color='rbga(0,0,0,0)', outline='rgb(93,93,93)'):

    styleSheet = '''
        QPushButton
        {{
            background-color: {bg};
            border-width: {bw}px;
            border-color: {bc};
            border-style: solid;
            min-height: {h}px;
            max-height: {h}px;
            padding: -{bw}px;
        }}
        QPushButton:hover
        {{
            border-width: {bw}px;
            border-color: {bc_hover};
            border-style: solid;
        }}
        QPushButton:pressed
        {{
            border-width: {bw}px;
            border-color: {bc_checked};
            border-style: solid;
        }}
        QPushButton:checked
        {{
            background-color: {bg};
            border-width: {bw}px;
            border-color: {bc_checked};
            border-radius: {radius};
            border-style: solid;
            min-height: {h}px;
            max-height: {h}px;
            padding: -{bw}px;
        }}
        QPushButton:checked:hover
        {{
            border-width: {bw}px;
            border-color: {bc_checked};
            border-style: solid;
        }}
        '''.format(bw=math.ceil(LAYER_BORDER_WIDTH),
                   h=math.ceil(LAYER_HEIGHT),
                   bg=background_color,
                   bc=outline,
                   bc_hover=ORANGE,
                   radius=BORDER_RADIUS,
                   bc_checked='white')

    return styleSheet

### Labels ###


subDLabel = '''
QLabel
{{
    color : {orange};
}}
'''.format(orange=ORANGE)

layerLabel = '''
QLabel
{{
    font: {weight} {f_size}px;
    padding-bottom: {p}px;
}}
'''.format(f_size=int(NORMAL_FONT),
           weight='bold',
           p=int(LAYER_BOTTOM_PADDING))

### Input Fields ###

inputField = '''
QSpinBox
{
    border-style: solid;
    border-radius: 4px;
}
'''

### Combo Box ###

smallComboBox = '''
QComboBox
{{
    background-color: {bg_clr};
    border-radius: {br}px;
}}
QComboBox:hover
{{
    background-color: {bc_hover};
}}
QComboBox:on
{{
    border-top-left-radius: {br}px;
    border-top-right-radius: {br}px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}}
QComboBox::drop-down
{{
    background-color: {bg_clr};
    border-radius: {br}px;
    width: {drop_down_width};
}}
QComboBox::down-arrow
{{
    image: url("{path}");
    width: {icon_size}px;
    height: {icon_size}px;
}}
'''.format(br=int(SMALL_BORDER_RADIUS),
           br_clr=SMALL_BORDER_COLOR,
           bg_clr=BACKGROUND_COLOR,
           bw=int(SMALL_BORDER_WIDTH),
           path=DROP_DOWN_ARROW_IMAGE,
           icon_size=int(scale(8)),
           bc_hover=HOVER_BACKGROUND_COLOR,
           drop_down_width=int(scale(16)))
