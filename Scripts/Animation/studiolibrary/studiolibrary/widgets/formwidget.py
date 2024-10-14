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

from . import fieldwidgets


__all__ = [
    "FormWidget",
    "FormDialog",
    "FIELD_WIDGET_REGISTRY"
]


logger = logging.getLogger(__name__)


FIELD_WIDGET_REGISTRY = {
    "int": fieldwidgets.IntFieldWidget,
    "bool": fieldwidgets.BoolFieldWidget,
    "enum": fieldwidgets.EnumFieldWidget,
    "text": fieldwidgets.TextFieldWidget,
    "path": fieldwidgets.PathFieldWidget,
    "image": fieldwidgets.ImageFieldWidget,
    "label": fieldwidgets.LabelFieldWidget,
    "range": fieldwidgets.RangeFieldWidget,
    "color": fieldwidgets.ColorFieldWidget,
    "string": fieldwidgets.StringFieldWidget,
    "slider": fieldwidgets.SliderFieldWidget,
    "separator": fieldwidgets.SeparatorFieldWidget
}


def toTitle(name):
    """Convert camel case strings to title strings"""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1 \2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1 \2", s1).title()


class FormWidget(QtWidgets.QFrame):

    accepted = QtCore.Signal(object)
    stateChanged = QtCore.Signal()
    validated = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super(FormWidget, self).__init__(*args, **kwargs)

        self._schema = []
        self._widgets = []
        self._validator = None

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

        self._optionsFrame = QtWidgets.QFrame(self)
        self._optionsFrame.setObjectName("optionsFrame")

        layout = QtWidgets.QVBoxLayout(self._optionsFrame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._optionsFrame.setLayout(layout)

        self._titleWidget = QtWidgets.QPushButton(self)
        self._titleWidget.setCheckable(True)
        self._titleWidget.setObjectName("titleWidget")
        self._titleWidget.toggled.connect(self._titleClicked)
        self._titleWidget.hide()

        self.layout().addWidget(self._titleWidget)
        self.layout().addWidget(self._optionsFrame)

    def _titleClicked(self, toggle):
        """Triggered when the user clicks the title widget."""
        self.setExpanded(toggle)
        self.stateChanged.emit()

    def titleWidget(self):
        """
        Get the title widget.
        
        :rtype: QWidget
        """
        return self._titleWidget

    def setTitle(self, title):
        """
        Set the text for the title widget.
        
        :type title: str
        """
        self.titleWidget().setText(title)

    def setExpanded(self, expand):
        """
        Expands the options if expand is true, otherwise collapses the options.
        
        :type expand: bool
        """
        self._titleWidget.blockSignals(True)

        try:
            self._titleWidget.setChecked(expand)
            self._optionsFrame.setVisible(expand)
        finally:
            self._titleWidget.blockSignals(False)

    def isExpanded(self):
        """
        Returns true if the item is expanded, otherwise returns false.
        
        :rtype: bool
        """
        return self._titleWidget.isChecked()

    def setTitleVisible(self, visible):
        """
        A convenience method for setting the title visible.
        
        :type visible: bool
        """
        self.titleWidget().setVisible(visible)

    def reset(self):
        """Reset all option widgets back to their default value."""
        for widget in self._widgets:
            widget.reset()
        self.validate()

    def setSchema(self, schema, layout=None):
        """
        Set the schema for the widget.
        
        :type schema: list[dict]
        """
        self._schema = schema

        for data in schema:

            cls = FIELD_WIDGET_REGISTRY.get(data.get("type", "label"))

            if not cls:
                logger.warning("Cannot find widget for %s", data)
                continue

            if layout and not data.get("layout"):
                data["layout"] = layout

            widget = cls(data=data)
            widget.setData(data)

            value = data.get("value")
            default = data.get("default")
            if value is None and default is not None:
                widget.setValue(default)

            self._widgets.append(widget)

            callback = functools.partial(self._optionChanged, widget)
            widget.valueChanged.connect(callback)

            self._optionsFrame.layout().addWidget(widget)

    def _optionChanged(self, widget):
        """
        Triggered when the given option widget changes value.
        
        :type widget: FieldWidget 
        """
        self.validate()

    def accept(self):
        """Accept the current options"""
        self.emitAcceptedCallback()

    def closeEvent(self, event):
        super(FormWidget, self).closeEvent(event)

    def hasErrors(self):
        """
        Return True if the form contains any errors.

        :rtype: bool
        """
        for widget in self._widgets:
            if widget.data().get("error"):
                return True
        return False

    def setValidator(self, validator):
        """
        Set the validator for the options.
        
        :type validator: func
        """
        self._validator = validator

    def validator(self):
        """
        Return the validator for the form.

        :rtype: func
        """
        return self._validator

    def validate(self):
        """Validate the current options using the validator."""
        if self._validator:

            fields = self._validator(**self.values())
            if fields is not None:
                self._setState(fields)

            self.validated.emit()

        else:
            logger.debug("No validator set.")

    def setValue(self, name, value):
        """
        Set the value for the given field name and value

        :type name: str
        :type value: object
        """
        widget = self.widget(name)
        widget.setValue(value)

    def value(self, name):
        """
        Get the value for the given widget name.
        
        :type name: str 
        :rtype: object 
        """
        widget = self.widget(name)
        return widget.value()

    def widget(self, name):
        """
        Get the widget for the given widget name.
        
        :type name: str 
        :rtype: FieldWidget 
        """
        for widget in self._widgets:
            if widget.data().get("name") == name:
                return widget

    def options(self):
        options = []
        for widget in self._widgets:
            options.append(widget.data())
        return options

    def optionsToDict(self):
        """
        This method is deprecated.

        :rtype: dict
        """
        return self.values()

    def values(self):
        """
        Get the all the field values indexed by the field name.

        :rtype: dict
        """
        values = {}
        for widget in self._widgets:
            values[widget.data().get("name")] = widget.value()
        return values

    def defaultValues(self):
        """
        Get the all the default field values indexed by the field name.

        :rtype: dict
        """
        values = {}
        for widget in self._widgets:
            values[widget.data().get("name")] = widget.default()
        return values

    def state(self):
        """
        Get the current state.
        
        :rtype: dict 
        """
        options = []

        for widget in self._widgets:
            options.append(widget.state())

        state = {
            "options": options,
            "expanded": self.isExpanded()
        }

        return state

    def setState(self, state):
        """
        Set the current state.
        
        :type state: dict 
        """
        expanded = state.get("expanded")
        if expanded is not None:
            self.setExpanded(expanded)

        options = state.get("options")
        if options is not None:
            self._setState(options)

        self.validate()

    def optionsState(self):
        state = {}
        values = self.values()
        options = self.options()

        for option in options:
            name = option.get("name")
            persistent = option.get("persistent")
            if name and persistent:
                state[name] = values[name]

        return state

    def setStateFromOptions(self, options):
        state = []
        for option in options:
            state.append({"name": option, "value": options[option]})

        self._setState(state)

    def _setState(self, fields):
        """
        Set the state.
        
        :type fields: list[dict]
        """
        for widget in self._widgets:
            widget.blockSignals(True)

        for widget in self._widgets:
            widget.setError("")
            for field in fields:
                if field.get("name") == widget.data().get("name"):
                    widget.setData(field)

        for widget in self._widgets:
            widget.blockSignals(False)

        self.stateChanged.emit()


class FormDialog(QtWidgets.QFrame):

    accepted = QtCore.Signal(object)
    rejected = QtCore.Signal(object)

    def __init__(self, parent=None, form=None):
        super(FormDialog, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

        self._widgets = []
        self._validator = None

        self._title = QtWidgets.QLabel(self)
        self._title.setObjectName('title')
        self._title.setText('FORM')
        self.layout().addWidget(self._title)

        self._description = QtWidgets.QLabel(self)
        self._description.setObjectName('description')
        self.layout().addWidget(self._description)

        self._formWidget = FormWidget(self)
        self._formWidget.setObjectName("formWidget")
        self._formWidget.validated.connect(self._validated)
        self.layout().addWidget(self._formWidget)

        self.layout().addStretch(1)

        buttonLayout = QtWidgets.QHBoxLayout(self)
        buttonLayout.setContentsMargins(0, 0, 0, 0)
        buttonLayout.setSpacing(0)

        self.layout().addLayout(buttonLayout)

        buttonLayout.addStretch(1)

        self._acceptButton = QtWidgets.QPushButton(self)
        self._acceptButton.setObjectName('acceptButton')
        self._acceptButton.setText('Submit')
        self._acceptButton.clicked.connect(self.accept)

        self._rejectButton = QtWidgets.QPushButton(self)
        self._rejectButton.setObjectName('rejectButton')
        self._rejectButton.setText('Cancel')
        self._rejectButton.clicked.connect(self.reject)

        buttonLayout.addWidget(self._acceptButton)
        buttonLayout.addWidget(self._rejectButton)

        if form:
            self.setSettings(form)
        # buttonLayout.addStretch(1)

    def _validated(self):
        """Triggered when the form has been validated"""
        self._acceptButton.setEnabled(not self._formWidget.hasErrors())

    def acceptButton(self):
        """
        Return the accept button.

        :rtype: QWidgets.QPushButton
        """
        return self._acceptButton

    def rejectButton(self):
        """
        Return the reject button.

        :rtype: QWidgets.QPushButton
        """
        return self._rejectButton

    def validateAccepted(self, **kwargs):
        """
        Triggered when the accept button has been clicked.

        :type kwargs: The values of the fields
        """
        self._formWidget.validator()(**kwargs)

    def validateRejected(self, **kwargs):
        """
        Triggered when the reject button has been clicked.

        :type kwargs: The default values of the fields
        """
        self._formWidget.validator()(**kwargs)

    def setSettings(self, settings):

        self._settings = settings

        title = settings.get("title")
        if title is not None:
            self._title.setText(title)

        callback = settings.get("accepted")
        if not callback:
            self._settings["accepted"] = self.validateAccepted

        callback = settings.get("rejected")
        if not callback:
            self._settings["rejected"] = self.validateRejected

        description = settings.get("description")
        if description is not None:
            self._description.setText(description)

        validator = settings.get("validator")
        if validator is not None:
            self._formWidget.setValidator(validator)

        layout = settings.get("layout")

        schema = settings.get("schema")
        if schema is not None:
            self._formWidget.setSchema(schema, layout=layout)

    def accept(self):
        """Call this method to accept the dialog."""
        callback = self._settings.get("accepted")
        if callback:
            callback(**self._formWidget.values())
        self.close()

    def reject(self):
        """Call this method to rejected the dialog."""
        callback = self._settings.get("rejected")
        if callback:
            callback(**self._formWidget.defaultValues())
        self.close()


STYLE = """

FormWidget QWidget {
    /*font-size: 12px;*/
    text-align: left;
}

FieldWidget {
    min-height: 16px;
    margin-bottom: 3px;
}

FieldWidget[layout=vertical] #label {
    margin-bottom: 4px;
}

FieldWidget[layout=horizontal] #label {
    margin-left: 4px;
}

FieldWidget #menuButton {
    margin-left: 4px;
    border-radius: 2px;
    min-width: 25px;
    max-height: 25px;
    text-align: center;
    background-color: rgb(0,0,0,20);
}

FieldWidget #label {
    min-width: 72px;
    color: rgb(FOREGROUND_COLOR_R, FOREGROUND_COLOR_G, FOREGROUND_COLOR_B, 100);
}

FormWidget #titleWidget {
    font-size: 12px;
    padding: 2px;
    padding-left: 5px;
    background-color: rgb(255, 255, 255, 20);
    border-bottom: 0px solid rgb(255, 255, 255, 20);
}

FormWidget #titleWidget:checked {
    background-color: rgb(255, 255, 255, 5);
}

FormWidget #optionsFrame {
    margin: 2px;
}

FieldWidget QComboBox {
    border: 1px solid transparent;
}
"""


def example():
    """
    import studiolibrary
    studiolibrary.reload()
    
    import studiolibrary
    studiolibrary.widgets.formwidget.example()
    """
    import studiolibrary
    image = studiolibrary.resource().get("icons", "icon.png")

    schema = [
        {
            "name": "name",
            "value": "Face.anim",
            "type": "string",
        },
        {
            "name": "objects",
            "value": "125 objects",
            "type": "label",
        },
        {
            "name": "sep1",
            "type": "separator",
        },
        {
            "name": "color",
            "type": "color",
        },
        {
            "name": "blend",
            "type": "slider",
        },
        {
            "name": "Bake",
            "type": "bool",
        },
        {
            "name": "image",
            "type": "image",
            "value": image
        },
        {
            "name": "frameRange",
            "type": "range"
        },
        {
            "name": "option",
            "type": "enum",
            "items": ["Test1", "Test2", "Test4"]
        },
        {
            "name": "comment",
            "value": "this is a comment",
            "type": "text",
            "layout": "vertical"
        },
    ]

    def validator(**fields):
        print(fields)

    w = FormWidget()
    w.setValidator(validator)
    w.setSchema(schema)
    w.setStyleSheet(STYLE)
    w.show()

    return w


if __name__ == "__main__":
    import studioqt
    with studioqt.app():
        w = example()



