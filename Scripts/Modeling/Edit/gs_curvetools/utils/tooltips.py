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
import io


def processTooltips():
    # type: () -> dict
    """ Processes the tooltips markdown file and returns a dict {"name": "tooltip", ...} """
    from . import utils
    filePath = '{}gs_curvetools/utils/tooltips.md'.format(utils.getFolder.scripts())
    finalDict = {}
    with io.open(filePath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        title = ""
        tooltip = ""
        commentBlock = False
        for line in lines:
            line = line.strip()
            if not line or "":
                continue

            # Exclude comments
            if "<!--" in line and "-->" in line:
                continue
            if "<!--" in line and not commentBlock:
                commentBlock = True
                continue
            if "-->" in line and commentBlock:
                commentBlock = False
                continue
            if commentBlock:
                continue

            # Process tooltips
            if '#' in line:
                if title and tooltip:
                    finalDict[title] = tooltip.strip()
                title = line.replace("#", "").strip()
                tooltip = ""
            else:
                tooltip += line + "\n"
        # Final title/tooltip pair
        if title and tooltip:
            finalDict[title] = tooltip.strip()
    return finalDict


def toggleCustomTooltipsMain(enable=True):
    # Custom Tooltips that can't be automatically processed from markdown files (mostly Maya sliders)
    from . import wrap
    customTooltips = {
        'gsCurvesSlider': 'Selects the number of added curves.\nUsed by Add Card, Add Tube, Fill and Subdivide functions',
        'gsSelectCVSlider': 'Selects the CVs of the selected curves based on the position of the slider.\n<- Left is root of the curve and right is the tip ->\nModes:\nNormal Drag is single CV selection based on the position of the slider.\nShift+Drag is additive selection.\nAlt+Drag is subtractive selection.\nCtrl+Drag to move the slider without selection change.',
        'gsRebuildSlider': 'Interactively rebuilds the selected curves. Slider controls the target number of CVs.\nNOTE: very small scale curves can have issues with distortion. If it is the case, try using Maya curve rebuild command.',
        'gsFactorSlider': 'Adjusts the intensity of the Smooth slider and the power of Extend and Reduce functions',
    }

    for widget in customTooltips:
        if hasattr(wrap.WIDGETS[widget], "setToolTip") and callable(getattr(wrap.WIDGETS[widget], "setToolTip")):
            if enable:
                wrap.WIDGETS[widget].setToolTip(customTooltips[widget])
            else:
                wrap.WIDGETS[widget].setToolTip('')

def toggleCustomTooltipsCurveControl(enable=True):
    # Custom Tooltips that can't be automatically processed from markdown files (mostly Maya sliders) for Curve Control Window
    from . import wrap
    customTooltips = {
        'gsPointSizeSlider': 'Controls the size of a CV point highlight',
        'gsCurveWidthSlider': 'Controls the width of the curve highlight',
        'gsHullWidthSlider': 'Controls the width of the hull highlight',
    }

    for widget in customTooltips:
        if hasattr(wrap.WIDGETS[widget], "setToolTip") and callable(getattr(wrap.WIDGETS[widget], "setToolTip")):
            if enable:
                wrap.WIDGETS[widget].setToolTip(customTooltips[widget])
            else:
                wrap.WIDGETS[widget].setToolTip('')
