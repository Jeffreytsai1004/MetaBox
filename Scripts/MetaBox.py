#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2 import QtWidgets, QtCore, QtGui
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
import maya.utils as utils
import importlib
import traceback
import subprocess
import webbrowser
import locale
import sys
import os

# 全局变量声明
# TOOL_PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
MAYA_VERSION = cmds.about(version=True)
TOOL_NAME = "MetaFusion"
# TOOL_ICON = os.path.join(TOOL_PATH, "icons", "logo.png")
TOOL_VERSION = "v1.0.0"
TOOL_AUTHOR = "CGNICO"
CURRENT_LANG = "en_EN"
DNA_PATH = None
WKSP_PATH = None
HelpURL = f"https://gitea.cgnico.com/CGNICO/{TOOL_NAME}/wiki"

class RoundedButton(QtWidgets.QPushButton):
    """
    Custom rounded button class

    Features:
    - Rounded design
    - Custom color and hover effect
    - Bold text
    """
    def __init__(self, text="", icon=None, color="#D0D0D0", hover_color="#E0E0E0", pressed_color="#C0C0C0"):
        super(RoundedButton, self).__init__(text)
        if icon:
            self.setIcon(icon)
            self.setIconSize(QtCore.QSize(24, 24))
        self.setMinimumHeight(30)  # Set minimum height
        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {color}; 
                color: #303030; 
                border-radius: 10px; 
                padding: 5px;
                font-weight: bold;
                text-align: center;
            }}
            QPushButton:hover {{
                background-color: {hover_color}; 
            }}
            QPushButton:pressed {{
                background-color: {pressed_color}; 
            }}
            """
        )
def get_system_encoding():
    encoding = sys.getdefaultencoding()
    if encoding.lower() == 'ascii':
        encoding = locale.getpreferredencoding()
    return encoding

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

LANG = {
    'en_US': {
        "Button1": "Button1",
        "Button2": "Button2"
    },
    'zh_CN': {
        "Button1": "按钮 1",
        "Button2": "按钮 2"
    }
}

class YourToolWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(YourToolWindow, self).__init__(parent)
        self.setWindowTitle(TOOL_NAME)
        self.resize(300, 800)

        # 检查并关闭老的窗口
        existing_windows = cmds.lsUI(windows=True)
        for window in existing_windows:
            if window.startswith(TOOL_NAME):
                cmds.deleteUI(window, window=True)

        # 布局设置
        main_layout = QtWidgets.QVBoxLayout()

        button_group1 = QtWidgets.QHBoxLayout()
        self.button1 = RoundedButton(LANG[CURRENT_LANG]["Button1"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        button_group1.addWidget(self.button1)

        button_group2 = QtWidgets.QHBoxLayout()
        self.button2 = RoundedButton(LANG[CURRENT_LANG]["Button2"], color="#A7C6ED", hover_color="#B2D3F0", pressed_color="#8BB8E0")
        button_group2.addWidget(self.button2)

        main_layout.addLayout(button_group1)
        main_layout.addLayout(button_group2)

        self.setLayout(main_layout)

if __name__ == "__main__":
    maya_main_window_ptr = omui.MQtUtil.mainWindow()
    maya_main_window = wrapInstance(int(maya_main_window_ptr), QtWidgets.QWidget)

    tool_window = YourToolWindow(maya_main_window)
    tool_window.show()