#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import os

def AnimSchoolPicker_install():
    """此脚本将为 AnimSchoolPicker 创建一个架子按钮"""

    os_type = cmds.about(os=True)

    ff = "*.so"  # 这是 Linux 的类型
    ps = "/"     # 这是 Mac 和 Linux 的路径分隔符

    if "mac" in os_type:
        ff = "*.bundle"
    elif "win" in os_type or "win64" in os_type:
        ff = "*.mll"
        ps = "\\"

    # 打开文件对话框以选择插件
    path = cmds.fileDialog2(caption="Select the AnimSchoolPicker plugin:", ff=ff, fileMode=1)

    if len(path) == 1:
        # 构建命令和图标路径
        cmd = "loadPlugin -qt \"{}\";\nAnimSchoolPicker();".format(path[0])
        icon = os.path.dirname(path[0]) + ps + "AnimSchoolLogoIcon.png"

        # 获取当前架子
        gShelfTopLevel = cmds.tabLayout('shelfTabLayout', query=True, selectTab=True)

        if cmds.file(icon, query=True, exists=True):
            cmds.shelfButton(command=cmd, image=icon)
        else:
            cmds.shelfButton(command=cmd, imageOverlayLabel="Pickr")

AnimSchoolPicker_install()