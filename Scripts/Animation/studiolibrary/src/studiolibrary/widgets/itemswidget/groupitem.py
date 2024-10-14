#!/usr/bin/env python
# -*- coding: utf-8 -*-

import studioqt

from studioqt import QtGui
from studioqt import QtCore
from studioqt import QtWidgets

from .item import Item


class GroupItem(Item):

    DEFAULT_FONT_SIZE = 24

    def __init__(self, *args):
        super(GroupItem, self).__init__(*args)

        self._children = []

        self._font = self.font(0)
        self._font.setBold(True)

        self.setFont(0, self._font)
        self.setFont(1, self._font)
        self.setDragEnabled(False)

    def setChildren(self, children):
        """
        Set the children for the group.

        :type children: list[Item]
        :rtype: None
        """
        self._children = children

    def children(self):
        """
        Return the children for the group.

        :rtype: list[Item]
        """
        return self._children

    def childrenHidden(self):
        """
        Return True if all children are hidden.

        :rtype: bool
        """
        for child in self.children():
            if not child.isHidden():
                return False
        return True

    def updateChildren(self):
        """
        Update the visibility if all children are hidden.

        :rtype: bool
        """
        if self.childrenHidden():
            self.setHidden(True)
        else:
            self.setHidden(False)

    def textAlignment(self, column):
        """
        Return the font alignment for the given column.

        :type column: int
        """
        return QtWidgets.QTreeWidgetItem.textAlignment(self, column)

    def sizeHint(self, column=0):
        """
        Return the size of the item.

        :rtype: QtCore.QSize
        """
        width = self.itemsWidget().width() - 20
        return QtCore.QSize(width, 40 * self.dpi())

    def visualRect(self, option):
        """
        Return the visual rect for the item.

        :type option: QtWidgets.QStyleOptionViewItem
        :rtype: QtCore.QRect
        """
        rect = QtCore.QRect(option.rect)
        rect.setX(10 * self.dpi())
        rect.setWidth(self.sizeHint().width())
        return rect

    def isTextVisible(self):
        """
        Return True if the text is visible.

        :rtype: bool
        """
        return True

    def textSelectedColor(self):
        """
        Return the selected text color for the item.

        :rtype: QtWidgets.QtColor
        """
        return self.itemsWidget().textColor()

    def backgroundColor(self):
        """
        Return the background color for the item.

        :rtype: QtWidgets.QtColor
        """
        return QtGui.QColor(0, 0, 0, 0)

    def backgroundHoverColor(self):
        """
        Return the background color when the mouse is over the item.

        :rtype: QtWidgets.QtColor
        """
        return QtGui.QColor(0, 0, 0, 0)

    def backgroundSelectedColor(self):
        """
        Return the background color when the item is selected.

        :rtype: QtWidgets.QtColor
        """
        return QtGui.QColor(0, 0, 0, 0)

    def paintRow(self, painter, option, index):
        """
        Paint performs low-level painting for the item.

        :type painter: QtWidgets.QPainter
        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: None
        """
        self.setRect(QtCore.QRect(option.rect))

        painter.save()

        try:
            self.paintBackground(painter, option, index)

            if self.isTextVisible():
                self._paintText(painter, option, 1)

            self.paintIcon(painter, option, index)
        finally:
            painter.restore()

    def icon(self, *args):
        """
        Overriding the icon method, so that an icon is not displayed.
        """
        return None

    def paintBackground(self, painter, option, index):
        """
        Draw the background for the item.

        :type painter: QtWidgets.QPainter
        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: None
        """
        super(GroupItem, self).paintBackground(painter, option, index)

        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        visualRect = self.visualRect(option)

        text = self.name()
        metrics = QtGui.QFontMetricsF(self._font)
        textWidth = metrics.width(text)

        padding = (25 * self.dpi())

        visualRect.setX(textWidth + padding)
        visualRect.setY(visualRect.y() + (visualRect.height() / 2))
        visualRect.setHeight(2 * self.dpi())
        visualRect.setWidth(visualRect.width() - padding)

        color = QtGui.QColor(
            self.textColor().red(),
            self.textColor().green(),
            self.textColor().blue(), 10
        )
        painter.setBrush(QtGui.QBrush(color))

        painter.drawRect(visualRect)
