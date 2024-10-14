#!/usr/bin/env python
# -*- coding: utf-8 -*-

from studiovendor.Qt import QtWidgets

from .groupitem import GroupItem


class ItemDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self):
        """
        This class is used to display data for the items in a ItemsWidget.
        """
        QtWidgets.QStyledItemDelegate.__init__(self)

        self._itemsWidget = None

    def itemsWidget(self):
        """
        Return the ItemsWidget that contains the item delegate.

        :rtype: studioqt.ItemsWidget
        """
        return self._itemsWidget

    def setItemsWidget(self, itemsWidget):
        """
        Set the ItemsWidget for the delegate.

        :type itemsWidget: studioqt.ItemsWidget
        :rtype: None
        """
        self._itemsWidget = itemsWidget

    def sizeHint(self, option, index):
        """
        Return the size for the given index.

        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: QtCore.QSize
        """
        #This will be called for each row.
        item = self.itemsWidget().itemFromIndex(index)

        if isinstance(item, GroupItem):
            return item.sizeHint()

        return self.itemsWidget().itemSizeHint(index)

    def paint(self, painter, option, index):
        """
        Paint performs low-level painting for the given model index.

        :type painter:  QtWidgets.QPainter
        :type option: QtWidgets.QStyleOptionViewItem
        :type index: QtCore.QModelIndex
        :rtype: None
        """
        item = self.itemsWidget().itemFromIndex(index)
        item.paint(painter, option, index)
