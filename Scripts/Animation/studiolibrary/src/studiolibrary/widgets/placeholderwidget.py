#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studiovendor.Qt import QtWidgets

import studioqt


class PlaceholderWidget(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        studioqt.loadUi(self)
