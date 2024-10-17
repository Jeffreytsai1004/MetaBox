##--------------------------------------------------------------------------
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
from ..Qt import QtWidgets, QtCore, QtCompat
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
import mtoa.core as core
from functools import partial

# Special cases for different Maya versions
from shiboken2 import wrapInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget

from .. import ModIt_Global

##______________________GLOBAL VAR
##PATH_SET
IconPath = ModIt_Global.IconsPathThemeClassic
PreferencePath = ModIt_Global.PreferencePath

WIN_DISPLAY_SIZE =(json.load(open(PreferencePath + 'WinSize.json',"r"))['VALUE'])




class CollapsibleHeader(QtWidgets.QWidget):
    COLLAPSED_PIXMAP = QtGui.QPixmap(IconPath + "Arrow_Collapse")
    EXPANDED_PIXMAP = QtGui.QPixmap(IconPath + "Arrow_Down")

    clicked = QtCore.Signal()

    def __init__(self, text, parent=None):
        super(CollapsibleHeader, self).__init__(parent)

        self.setAutoFillBackground(True)
        self.set_background_color(True)

        self.icon_label = QtWidgets.QLabel()
        self.icon_label.setFixedWidth(self.COLLAPSED_PIXMAP.width())

        self.text_label = QtWidgets.QLabel()
        self.text_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(4, 4, 4, 0)
        self.main_layout.setSpacing(12) # DISTANCE du TITRE de la FLECHE
        self.main_layout.addWidget(self.icon_label)
        self.main_layout.addWidget(self.text_label)

        self.set_text(text)
        self.set_expanded(False)

    def set_text(self, text):
        self.text_label.setText("<b>{0}</b>".format(text))
        if WIN_DISPLAY_SIZE == 1: #150%
            self.text_label.setFont(QtGui.QFont('Candara', 6))

    def set_background_color(self, color):
        if not color:
            color = QtWidgets.QPushButton().palette().color(QtGui.QPalette.Button)

        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, color)
        self.setPalette(palette)

    def is_expanded(self):
        return self._expanded

    def set_expanded(self, expanded):
        self._expanded = expanded

        if (self._expanded):
            self.icon_label.setPixmap(self.EXPANDED_PIXMAP)
        else:
            self.icon_label.setPixmap(self.COLLAPSED_PIXMAP)

    def mousePressEvent(self, event):
        self.clicked.emit()  # pylint: disable=E1101


class CollapsibleWidget(QtWidgets.QWidget):
    collapsed_signal = QtCore.Signal(bool)

    def __init__(self, text, parent=None):
        super(CollapsibleWidget, self).__init__(parent)

        self.header_wdg = CollapsibleHeader(text)
        self.header_wdg.clicked.connect(self.on_header_clicked)  # pylint: disable=E1101

        self.Body_wdg = QtWidgets.QWidget()
        self.Body_wdg.setContentsMargins(0, 0, 0, 0)

        self.MAIN_lyt = QtWidgets.QVBoxLayout(self.Body_wdg)
        self.MAIN_lyt.setContentsMargins(0, 0, 0, 0)


        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.header_wdg)
        self.main_layout.addWidget(self.Body_wdg)


        self.set_expanded(False)

    def add_widget(self, widget):
        self.MAIN_lyt.addWidget(widget)

    def add_layout(self, layout):
        self.MAIN_lyt.addLayout(layout)

    def set_expanded(self, expanded):
        self.header_wdg.set_expanded(expanded)
        self.Body_wdg.setVisible(expanded)
        self.collapsed_signal.emit(expanded)

    def set_header_background_color(self, color):
        self.header_wdg.set_background_color(color)

    def on_header_clicked(self):
        self.set_expanded(not self.header_wdg.is_expanded())
        # TestDialog.btnAction(self)
