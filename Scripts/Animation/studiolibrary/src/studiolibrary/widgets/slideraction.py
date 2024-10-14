#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studiovendor.Qt import QtCore
from studiovendor.Qt import QtWidgets


__all__ = ["SliderAction"]


class SliderWidgetAction(QtWidgets.QFrame):
    pass


class SliderAction(QtWidgets.QWidgetAction):

    def __init__(self, label="", parent=None):
        """
        :type parent: QtWidgets.QMenu
        """
        QtWidgets.QWidgetAction.__init__(self, parent)

        self._widget = SliderWidgetAction(parent)
        self._label = QtWidgets.QLabel(label, self._widget)

        self._slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self._widget)
        self._slider.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        self.valueChanged = self._slider.valueChanged

    def widget(self):
        """
        Return the widget for this action.

        :rtype: QtWidgets.QWidget
        """
        return self._widget

    def label(self):
        """
        Return the QLabel object.

        :rtype: QtWidgets.QLabel
        """
        return self._label

    def slider(self):
        """
        Return the QLabel object.

        :rtype: QtWidgets.QSlider
        """
        return self._slider

    def createWidget(self, menu):
        """
        This method is called by the QWidgetAction base class.

        :type menu: QtWidgets.QMenu
        """
        actionWidget = self.widget()

        actionLayout = QtWidgets.QHBoxLayout(actionWidget)
        actionLayout.setContentsMargins(0, 0, 0, 0)
        actionLayout.addWidget(self.label())
        actionLayout.addWidget(self.slider())
        actionWidget.setLayout(actionLayout)

        return actionWidget
