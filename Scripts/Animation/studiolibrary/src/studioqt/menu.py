#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studioqt import QtWidgets


class Menu(QtWidgets.QMenu):

    def __init__(self, *args):
        QtWidgets.QMenu.__init__(self, *args)

    def findAction(self, text):
        """
        Return the action that contains the given text.
        
        :type text: str

        :rtype: QtWidgets.QAction
        """
        for child in self.children():

            action = None

            if isinstance(child, QtWidgets.QMenu):
                action = child.menuAction()
            elif isinstance(child, QtWidgets.QAction):
                action = child

            if action and action.text().lower() == text.lower():
                return action

    def insertAction(self, before, *args):
        """
        Add support for finding the before action by the given string.

        :type before: str  or QtWidget.QAction
        :type args: list

        :rtype: QtWidgets.QAction
        """
        if isinstance(before, str):
            before = self.findAction(before)

        return QtWidgets.QMenu.insertAction(self, before, *args)

    def insertMenu(self, before, menu):
        """
        Add support for finding the before action by the given string.
        
        :type before: str  or QtWidget.QAction
        :type menu: QtWidgets.QMenu
        
        :rtype: QtWidgets.QAction
        """
        if isinstance(before, str):
            before = self.findAction(before)

        QtWidgets.QMenu.insertMenu(self, before, menu)

    def insertSeparator(self, before):
        """
        Add support for finding the before action by the given string.
        
        :type before: str or QtWidget.QAction

        :rtype: QtWidgets.QAction
        """
        if isinstance(before, str):
            before = self.findAction(before)

        return QtWidgets.QMenu.insertSeparator(self, before)
