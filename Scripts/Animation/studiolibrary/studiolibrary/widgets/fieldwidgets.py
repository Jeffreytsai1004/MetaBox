# Copyright 2019 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. This library is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

import re
import logging
import functools

from studioqt import QtGui, QtCore, QtWidgets

import studioqt


from . import colorpicker


logger = logging.getLogger(__name__)


def toTitle(name):
    """Convert camel case strings to title strings"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).title()


class FieldWidget(QtWidgets.QFrame):

    """The base widget for all field widgets.
    
    Examples:
        
        data = {
            'name': 'startFrame',
            'type': 'int'
            'value': 1,
        }
        
        fieldWidget = FieldWidget(data)
        
    """
    valueChanged = QtCore.Signal()

    DefaultLayout = "horizontal"

    def __init__(self, parent=None, data=None):
        super(FieldWidget, self).__init__(parent)

        self._data = data or {}
        self._error = False
        self._widget = None
        self._default = None
        self._required = None
        self._errorLabel = None
        self._menuButton = None
        self._actionResult = None

        self.setObjectName("fieldWidget")

        direction = self._data.get("layout", self.DefaultLayout)

        if direction == "vertical":
            layout = QtWidgets.QVBoxLayout(self)
        else:
            layout = QtWidgets.QHBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setContentsMargins(0, 0, 0, 0)

        self._label = QtWidgets.QLabel(self)
        self._label.setObjectName('label')
        self._label.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred,
        )

        layout.addWidget(self._label)

        self._layout2 = QtWidgets.QHBoxLayout(self)
        layout.addLayout(self._layout2)

        if direction == "vertical":
            self._label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        else:
            self._label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

    def label(self):
        """
        Get the label widget.
        
        :rtype: QtWidgets.QLabel 
        """
        return self._label

    def state(self):
        """
        Get the current state of the data.
        
        :rtype: dict
        """
        return {
            "name": self._data["name"],
            "value": self.value()
        }

    def data(self):
        """
        Get the data for the widget.
        
        :rtype: dict 
        """
        return self._data

    def title(self):
        """
        Get the title to be displayed for the field.
        
        :rtype: str 
        """
        data = self.data()

        title = data.get("title", "") or data.get("name", "")
        if title:
            title = toTitle(title)

        if self.isRequired():
            title += '*'

        return title

    def setData(self, data):
        """
        Set the current state of the field widget using a dictionary.
        
        :type data: dict
        """
        state = data

        self.blockSignals(True)

        items = state.get('items')
        if items is not None:
            self.setItems(items)

        value = state.get('value')
        default = state.get('default')

        # Must set the default before value
        if default is not None:
            self.setDefault(default)
        elif value is not None:
            self.setDefault(value)

        if value is not None and value != self.value():
            try:
                self.setValue(value)
            except TypeError as error:
                logger.exception(error)

        enabled = state.get('enabled')
        if enabled is not None:
            self.setEnabled(enabled)
            self._label.setEnabled(enabled)

        hidden = state.get('hidden')
        if hidden is not None:
            self.setHidden(hidden)

        required = state.get('required')
        if required is not None:
            self.setRequired(required)

        error = state.get('error')
        if error is not None:
            self.setError(error)

        toolTip = state.get('toolTip')
        if toolTip is not None:
            self.setToolTip(toolTip)
            self.setStatusTip(toolTip)

        style = state.get("style")
        if style is not None:
            self.setStyleSheet(style)

        title = self.title() or ""
        self.setText(title)

        label = state.get('label')
        if label is not None:

            text = label.get("name")
            if text is not None:
                self.setText(text)

            visible = label.get('visible')
            if visible is not None:
                self.label().setVisible(visible)

        # Menu Items
        actions = state.get('actions')
        if actions is not None:
            self._menuButton.setVisible(True)

        # Menu Button
        menu = state.get('menu')
        if menu is not None:
            text = menu.get("name")
            if text is not None:
                self._menuButton.setText(text)

            visible = menu.get("visible", True)
            self._menuButton.setVisible(visible)

        self._data.update(data)

        self.refresh()

        self.blockSignals(False)

    def setError(self, message):
        """
        Set the error message to be displayed for the field widget.
        
        :type message: str
        """
        self._error = True if message else False

        self._data["error"] = message

        if self._error:
            self._errorLabel.setText(message)
            self._errorLabel.setHidden(False)
            self.setToolTip(message)
        else:
            self._errorLabel.setText("")
            self._errorLabel.setHidden(True)
            self.setToolTip(self.data().get('toolTip'))

        self.refresh()

    def setText(self, text):
        """
        Set the label text for the field widget.
        
        :type text: str 
        """
        self._label.setText(text)

    def setValue(self, value):
        """
        Set the value of the field widget.
        
        Will emit valueChanged() if the new value is different from the old one.
        
        :type value: object
        """
        self.emitValueChanged()

    def value(self):
        """
        Get the value of the field widget.
        
        :rtype: object
        """
        raise NotImplementedError('The method "value" needs to be implemented')

    def setItems(self, items):
        """
        Set the items for the field widget.
        
        :type items: list[str]
        """
        raise NotImplementedError('The method "setItems" needs to be implemented')

    def reset(self):
        """Reset the field widget back to the defaults."""
        self.setState(self._data)

    def setRequired(self, required):
        """
        Set True if a value is required for this field.
        
        :type required: bool
        """
        self._required = required
        self.setProperty('required', required)
        self.setStyleSheet(self.styleSheet())

    def isRequired(self):
        """
        Check if a value is required for the field widget.
        
        :rtype: bool
        """
        return bool(self._required)

    def setDefault(self, default):
        """
        Set the default value for the field widget.
        
        :type default: object
        """
        self._default = default

    def default(self):
        """
        Get the default value for the field widget.
        
        :rtype: object
        """
        return self._default

    def isDefault(self):
        """
        Check if the current value is the same as the default value.
        
        :rtype: bool
        """
        return self.value() == self.default()

    def emitValueChanged(self, *args):
        """
        Emit the value changed signal.
        
        :type args: list
        """
        self.valueChanged.emit()
        self.refresh()

    def setWidget(self, widget):
        """
        Set the widget used to set and get the field value.
        
        :type widget: QtWidgets.QWidget
        """
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.setContentsMargins(0, 0, 0, 0)
        widgetLayout.setSpacing(0)

        self._widget = widget
        self._widget.setParent(self)
        self._widget.setObjectName('widget')
        self._widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred,
        )

        self._menuButton = QtWidgets.QPushButton("...")
        self._menuButton.setHidden(True)
        self._menuButton.setObjectName("menuButton")
        self._menuButton.clicked.connect(self._menuCallback)
        self._menuButton.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Expanding,
        )

        widgetLayout.addWidget(self._widget)
        widgetLayout.addWidget(self._menuButton)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._errorLabel = QtWidgets.QLabel(self)
        self._errorLabel.setHidden(True)
        self._errorLabel.setObjectName("errorLabel")
        self._errorLabel.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred,
        )

        layout.addLayout(widgetLayout)
        layout.addWidget(self._errorLabel)

        self._layout2.addLayout(layout)

    def _menuCallback(self):
        callback = self.data().get("menu", {}).get("callback", self.showMenu)
        callback()

    def _actionCallback(self, callback):
        """
        Wrap schema callback to get the return value.
        
        :type callback: func 
        """
        self._actionResult = callback()

    def showMenu(self):
        """Show the menu using the actions from the data."""
        menu = QtWidgets.QMenu(self)
        actions = self.data().get("actions", [])

        for action in actions:

            name = action.get("name", "No name found")
            callback = action.get("callback")

            func = functools.partial(self._actionCallback, callback)

            action = menu.addAction(name)
            action.triggered.connect(func)

        point = QtGui.QCursor.pos()
        point.setX(point.x() + 3)
        point.setY(point.y() + 3)

        # Reset the action results
        self._actionResult = None

        menu.exec_(point)

        if self._actionResult is not None:
            self.setValue(self._actionResult)

    def widget(self,):
        """
        Get the widget used to set and get the field value.
        
        :rtype: QtWidgets.QWidget
        """
        return self._widget

    def refresh(self):
        """Refresh the style properties."""
        direction = self._data.get("layout", self.DefaultLayout)

        self.setProperty("layout", direction)
        self.setProperty('default', self.isDefault())
        self.setProperty('error', self._error)

        self.setStyleSheet(self.styleSheet())


class Label(QtWidgets.QLabel):

    """A custom label which supports elide right."""

    def __init__(self, *args):
        super(Label, self).__init__(*args)
        self._text = ''

    def setText(self, text):
        """
        Overriding this method to store the original text.
        
        :type text: str
        """
        self._text = text
        QtWidgets.QLabel.setText(self, text)

    def resizeEvent(self, event):
        """Overriding this method to modify the text with elided text."""
        metrics = QtGui.QFontMetrics(self.font())
        elided = metrics.elidedText(self._text, QtCore.Qt.ElideRight, self.width())
        QtWidgets.QLabel.setText(self, elided)


class LabelFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(LabelFieldWidget, self).__init__(*args, **kwargs)

        widget = Label(self)
        widget.setAlignment(QtCore.Qt.AlignVCenter)
        widget.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.setWidget(widget)

    def value(self):
        """
        Get the value of the label.
        
        :rtype: str 
        """
        return unicode(self.widget().text())

    def setValue(self, value):
        """
        Set the value of the label.
        
        :type value: str 
        """
        self.widget().setText(value)
        super(LabelFieldWidget, self).setValue(value)


class StringFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(StringFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QLineEdit(self)
        widget.textChanged.connect(self.emitValueChanged)
        self.setWidget(widget)

    def value(self):
        """
        Get the value of the widget.
        
        :rtype: unicode 
        """
        return unicode(self.widget().text())

    def setValue(self, value):
        """
        Set the string value for the widget.
        
        :type value: unicode 
        """
        self.widget().setText(value)
        super(StringFieldWidget, self).setValue(value)


class PathFieldWidget(StringFieldWidget):
    def __init__(self, *args, **kwargs):
        super(PathFieldWidget, self).__init__(*args, **kwargs)

    def setData(self, data):
        """
        Overriding this method to add a browse to folder button.

        :type data: dict
        """
        if "menu" not in data:
            data["menu"] = {
                "callback": self.browse
            }

        super(PathFieldWidget, self).setData(data)

    def browse(self):
        """Open the file dialog."""
        path = self.value()
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Browse Folder",
            path
        )
        if path:
            self.setValue(path)


class TextFieldWidget(FieldWidget):

    DefaultLayout = "Vertical"

    def __init__(self, *args, **kwargs):
        super(TextFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QTextEdit(self)
        widget.textChanged.connect(self.emitValueChanged)
        self.setWidget(widget)

    def value(self):
        """
        Get the text value of the text edit.
        
        :rtype: unicode 
        """
        return unicode(self.widget().toPlainText())

    def setValue(self, value):
        """
        Set the text value for the text edit.
        
        :type value: unicode 
        """
        self.widget().setText(value)
        super(TextFieldWidget, self).setValue(value)


class IntFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(IntFieldWidget, self).__init__(*args, **kwargs)

        validator = QtGui.QIntValidator(-50000000, 50000000, self)

        widget = QtWidgets.QLineEdit(self)
        widget.setValidator(validator)
        widget.textChanged.connect(self.emitValueChanged)
        self.setWidget(widget)

    def value(self):
        """
        Get the int value for the widget.
        
        :rtype: int 
        """
        value = self.widget().text()
        if value.strip() == '':
            value = self.default()

        return int(str(value))

    def setValue(self, value):
        """
        Set the int value for the widget.
        
        :type value: int
        """
        if value == '':
            value = self.default()

        self.widget().setText(str(int(value)))


class BoolFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(BoolFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QCheckBox(self)
        widget.stateChanged.connect(self.emitValueChanged)

        self.setWidget(widget)

        inline = self.data().get("inline")
        if inline:
            self.label().setText("")
            self.widget().setText(self.title())

    def value(self):
        """
        Get the value of the checkbox.
        
        :rtype: bool 
        """
        return bool(self.widget().isChecked())

    def setValue(self, value):
        """
        Set the value of the checkbox.
        
        :type value: bool 
        """
        self.widget().setChecked(value)
        super(BoolFieldWidget, self).setValue(value)


class RangeFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(RangeFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QFrame(self)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(3)
        widget.setLayout(layout)

        validator = QtGui.QIntValidator(-50000000, 50000000, self)

        self._minwidget = QtWidgets.QLineEdit(self)
        self._minwidget.setValidator(validator)
        self._minwidget.textChanged.connect(self.emitValueChanged)
        widget.layout().addWidget(self._minwidget)

        self._maxwidget = QtWidgets.QLineEdit(self)
        self._maxwidget.setValidator(validator)
        self._maxwidget.textChanged.connect(self.emitValueChanged)
        widget.layout().addWidget(self._maxwidget)

        self.setWidget(widget)

    def value(self):
        """
        Get the current range.
        
        :rtype: list[int] 
        """
        min = int(float(self._minwidget.text() or "0"))
        max = int(float(self._maxwidget.text() or "0"))

        return min, max

    def setValue(self, value):
        """
        Set the current range.
        
        :type value: list[int] 
        """
        minValue, maxValue = int(value[0]), int(value[1])

        self._minwidget.setText(str(minValue))
        self._maxwidget.setText(str(maxValue))

        super(RangeFieldWidget, self).setValue(value)


class EnumFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(EnumFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QComboBox(self)
        widget.currentIndexChanged.connect(self.emitValueChanged)

        self.setWidget(widget)

    def value(self):
        """
        Get the value of the combobox.
        
        :rtype: unicode 
        """
        return unicode(self.widget().currentText())

    def setState(self, state):
        """
        Set the current state with support for editable.
        
        :type state: dict
        """
        super(EnumFieldWidget, self).setState(state)

        editable = state.get('editable')
        if editable is not None:
            self.widget().setEditable(editable)

    def setValue(self, item):
        """
        Set the current value of the combobox.
        
        :type item: unicode 
        """
        self.setCurrentText(item)

    def setCurrentText(self, text):
        """
        This method supports Qt4 and Qt5 when settings the current text.

        :type text: str
        """
        index = self.widget().findText(text, QtCore.Qt.MatchExactly)
        if index != -1:
            self.widget().setCurrentIndex(index)
        else:
            logger.warning("Cannot set the value for field %s", self.name())

    def setItems(self, items):
        """
        Set the current items of the combobox.
        
        :type items: list[unicode]
        """
        self.widget().clear()
        self.widget().addItems(items)


class SeparatorFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(SeparatorFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QLabel(self)
        widget.setObjectName('widget')
        widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )

        self.setWidget(widget)

        self.label().hide()

    def setValue(self, value):
        """
        Set the current text of the separator.
        
        :type value: unicode 
        """
        self.widget().setText(value)

    def value(self):
        """
        Get the current text of the combobox.
        
        :rtype: unicode 
        """
        return self.widget().text()


class SliderFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(SliderFieldWidget, self).__init__(*args, **kwargs)

        widget = QtWidgets.QSlider(self)
        widget.setOrientation(QtCore.Qt.Horizontal)
        widget.setObjectName('widget')
        widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )
        widget.valueChanged.connect(self.emitValueChanged)

        self.setWidget(widget)

    def setValue(self, value):
        """
        Set the current value for the slider.
        
        :type value: int 
        """
        self.widget().setValue(value)

    def value(self):
        """
        Get the current value for the slider.
        
        :rtype: int
        """
        return self.widget().value()


class ColorFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(ColorFieldWidget, self).__init__(*args, **kwargs)

        self._value = "rgb(100,100,100)"

        widget = colorpicker.ColorPickerWidget()
        widget.setObjectName('widget')
        widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )
        widget.colorChanged.connect(self._colorChanged)
        self.setWidget(widget)

    def setData(self, data):
        """
        Overriding this method to add support for a "colors" key.

        :type data: dict
        """
        colors = data.get("colors")
        if colors:
            self.widget().setColors(colors)

        super(ColorFieldWidget, self).setData(data)

    def _colorChanged(self, color):
        """
        Triggered when the color changes from the color browser.
        
        :type color: QtGui.QColor
        """
        self.setValue(color)
        self.emitValueChanged()

    def setValue(self, value):
        """
        Set the current value for the slider.
        
        :type value: str 
        """
        self.widget().setCurrentColor(value)

    def value(self):
        """
        Get the current value for the slider.
        
        :rtype: str 
        """
        return self.widget().currentColor()


class ImageFieldWidget(FieldWidget):

    def __init__(self, *args, **kwargs):
        super(ImageFieldWidget, self).__init__(*args, **kwargs)

        self._value = ""
        self._pixmap = None

        widget = QtWidgets.QLabel(self)
        self.setStyleSheet("min-height: 32px;")
        widget.setScaledContents(False)
        widget.setObjectName('widget')
        widget.setAlignment(QtCore.Qt.AlignHCenter)

        self.setWidget(widget)
        self.layout().addStretch()

    def setValue(self, value):
        """
        Set the path on disc for the image.

        :type value: str 
        """
        self._value = value
        self._pixmap = QtGui.QPixmap(value)
        self.update()

    def value(self):
        """
        Get the path on disc for the image.

        :rtype: str 
        """
        return self._value

    def resizeEvent(self, event):
        """
        Called when the field widget is resizing.

        :type event: QtCore.QEvent
        """
        self.update()

    def update(self):
        """Update the image depending on the size."""
        if self._pixmap:
            width = self.widget().height()
            transformation = QtCore.Qt.SmoothTransformation

            if self.widget().width() > self.widget().height():
                pixmap = self._pixmap.scaledToWidth(width, transformation)
            else:
                pixmap = self._pixmap.scaledToHeight(width, transformation)

            self.widget().setPixmap(pixmap)
            self.widget().setAlignment(QtCore.Qt.AlignLeft)
