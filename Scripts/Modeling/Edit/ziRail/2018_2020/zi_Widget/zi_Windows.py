#                      __                  __
# ___  __ ____________/  |_  ____ ___  ___/  |_ __ _________  ____
# \  \/ _/ __ \_  __ \   ___/ __ \\  \/  \   __|  |  \_  __ _/ __ \
#  \   /\  ___/|  | \/|  | \  ___/ >    < |  | |  |  /|  | \\  ___/
#   \_/  \___  |__|   |__|  \___  /__/\_ \|__| |____/ |__|   \___  >
#            \/                 \/      \/                       \/
#
# //  (contact@vertexture.org)
# //  www.vertexture.org
# //  Please read on the website terms of use and licensing. Tutorials can be found also
# //
# //
# ////////////////////////////////////////////////////////////////////////////////////*/
import math
import sys
import os

import maya.cmds as cmds
import maya.OpenMayaUI as apiUI

import shiboken2
from PySide2 import QtWidgets, QtCore, QtGui


_winback = (38, 40, 43, 250)
_buttback = (40, 40, 46, 255)
_tabback = (47, 48, 54, 255)
_textforce = (190, 190, 193, 130)
_lineback = (16, 18, 25, 255)
_labelfor = (85, 85, 90, 100)

_gradTop = (27, 73, 135, 15)
_gradBot = (48, 147, 215, 75)

_butthov = (38, 50, 65, 160)
_frame = (235, 235, 0, 25)

_style = '''
QWidget{{
    background-color: rgba{buttback};
    color : rgba{buttback};
}}

QTabBar{{
    background-color: rgba{buttback};
    color : rgba{textforce};
}}

QDoubleSpinBox{{
    background-color: rgba{buttback};
    color: rgba{textforce};
}}

QSpinBox{{
    background-color: rgba{buttback};
    color: rgba{textforce};
}}

QRadioButton{{
    background-color: rgba{buttback};
    color: rgba{textforce};
}}

QGroupBox, ziCollapse{{
    background-color: rgba{buttback};
    color: rgba{textforce};

}}

QGroupBox::title{{
padding-left: 9999px;
padding-right: 9999px;
}}

QMenuBar{{
    background-color: rgba{buttback};
}}

QMainWindow{{
    background-color: rgba{lineback};
}}

QPushButton:pressed{{
    background-color: rgba{textforce};
}}

QLabel{{
    color: rgba{labelfor};
}}

QCheckBox{{
    color: rgba{labelfor};
}}

QFrame{{
    background-color: rgba{tabback};
    color: rgba{textforce};
}}


QPushButton, QCheckBox, QComboBox{{
    background-color: rgba{buttback};
    color: rgba{textforce};
    border-radius: 1px 1px 1px 1px;
    border-color: rgba{lineback};
    height: 22px;
    border-width:1px;

}}

QPushButton:hover, QCheckBox:hover, QComboBox:hover{{

    border-radius: 2px 2px 2px 2px;

    background-color: rgba{butthov};
    border-radius: 1px 1px 1px 1px;
    border-color: rgba{textforce};
    color: rgba(255, 255, 255, 255);
}}

QPushButton:checked{{
    background-color: qlineargradient(spread:pad, x1:0.035533, y1:0, x2:0.248838, y2:1, stop:0 rgba{gradtop}, stop:1 rgba{gradbot});
    border-radius: 2px 2px 2px 2px;
}}

QLineEdit{{
    background-color: rgba{tabback};
    color: rgba{textforce};
}}

QTreeWidget:item:selected{{
    background: rgba{butthov};
    color: rgba{textforce};
}}

QTreeWidget{{
    color: rgba{textforce};
    background-color: rgba{tabback};
    show-decoration-selected: 0;
}}
;'''.format(
    winback=_winback,
    tabback=_tabback,
    buttback=_buttback,
    textforce=_textforce,
    lineback=_lineback,
    labelfor=_labelfor,
    gradtop=_gradTop,
    gradbot=_gradBot,
    butthov=_butthov
)


root = ":/vertexture/skin/vertexture"


def getMayaWin(widPtr=None):

    winPtr = apiUI.MQtUtil.mainWindow()

    if widPtr:
        winPtr = widPtr

    if not winPtr:
        raise Exception('could find MayaWindow Pointer')

    if int(sys.version_info.major) > 2:
        pointer = int(winPtr)
    else:
        pointer = long(winPtr)

    return shiboken2.wrapInstance(pointer, QtWidgets.QWidget)


def getViewPortWidget():

    view = apiUI.M3dView.active3dView()
    return (getMayaWin(widPtr=view.widget()))


class Frameless(QtWidgets.QMainWindow, QtCore.QObject):

    prevSize = QtCore.QSize()
    offset = QtCore.QPoint()
    prev = QtCore.QPoint()
    previous = False
    geoAttr = "geo"
    miniSize = 28

    wheeled = QtCore.Signal(int)

    def __init__(self, parent=getMayaWin()):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.dock = ""
        self.movable = True
        self.actions = []

        self.setContentsMargins(0, 0, 0, 0)
        self.setMouseTracking(True)
        self.setStatusBar(None)
        self.setSheet()

        self.factoryDark = QtWidgets.QStyleFactory.create("fusion")
        self.factoryLgth = QtWidgets.QStyleFactory.create("Oxygen")

    def mouseMoveEvent(self, event):

        if event.buttons() == QtCore.Qt.MidButton:

            if not self.movable:
                return

            if not self.previous:
                self.prev = event.globalPos()
                self.offset = event.pos()
                self.previous = True
                return

            out = event.globalPos() - self.prev
            self.move(self.prev - self.offset + out)

        if event.buttons() == QtCore.Qt.RightButton:

            if not self.previous:
                self.prev = event.globalPos()
                self.prevSize = self.size()
                self.previous = True
                return

            out = event.globalPos() - self.prev

            self.resize(self.prevSize.width() + out.x(),
                        self.prevSize.height() + out.y())

    def mouseReleaseEvent(self, event):

        self.previous = False
        self.clicked = False
        self.on = False

    def wheelEvent(self, event):
        self.wheeled.emit(event.delta())

    def setGlobalKey(self, key, func, repeat=False):
        """Description

        :Param key(None): desc.
        :Param func(None): desc.

        :Return (None): desc.
        """
        action = QtWidgets.QAction(self)
        action.setShortcut(QtGui.QKeySequence(key))
        action.triggered.connect(func)
        action.setAutoRepeat(repeat)

        getMayaWin().addAction(action)
        self.actions.append(action)

    def setSheet(self):
        self.setStyleSheet(_style)

    def closeDockEvent(self, func=None):
        """The specified function call when closing with dock
        """
        if func:
            func()

        self.saveGeo()

    def setDock(self,
                obj,
                title,
                name,
                allowed=["left", "right"],
                floated=True,
                closeEventFunction=None):

        self.dock = name

        if cmds.dockControl(self.dock, exists=True):
            cmds.deleteUI(self.dock, control=True)

        cmds.dockControl(self.dock,
                         area="right",
                         content=obj.objectName(),
                         label=title,
                         floating=floated,
                         allowedArea=allowed,
                         fixedHeight=False,
                         vcc=lambda x: self.closeDockEvent(closeEventFunction))

    def hideEvent(self, event):
        """The last call function during the app closing
        """
        self.saveGeo()

    def closeEvent(self, event):
        """The close event whithout dock
        """
        if cmds.dockControl(self.dock, exists=True):
            cmds.deleteUI(self.dock, control=True)

        self.saveGeo()

    def killKeys(self):
        """Called from subclass in order to cleanup the keys actions
        """
        for action in self.actions:
            getMayaWin().removeAction(action)

        self.actions = []

    def addBar(self,
               help,
               toolname="",
               simple=False,
               url="www.vertexture.org"):

        self.bar = QtWidgets.QToolBar()
        self.butTheme = QtWidgets.QPushButton('')
        self.butWindo = QtWidgets.QPushButton('')
        self.butAbout = QtWidgets.QPushButton('')

        self.logo = VertextureLogo(url=url)
        self.logo.setPixmap(QtGui.QPixmap('%s/logoHs_color.png' % root))

        self.butAbout.setIcon(self.pmap('%s/bar/questiongrey.png' % root))
        self.butWindo.setIcon(self.pmap('%s/bar/framegrey.png' % root))
        self.butTheme.setIcon(self.pmap('%s/bar/darkgrey.png' % root))

        self.bar.setMinimumHeight(self.miniSize)
        self.bar.setMaximumHeight(self.miniSize)
        self.bar.setFloatable(False)
        self.bar.setMovable(False)

        self.logo.setMaximumWidth(120)
        map(lambda x: x.setMinimumHeight(self.miniSize - 4),
            (self.butTheme, self.butWindo, self.butAbout))

        map(lambda x: x.setIconSize(QtCore.QSize(28, 28)),
            (self.butTheme, self.butWindo, self.butAbout))

        self.butTheme.setCheckable(True)
        self.butWindo.setCheckable(True)

        self.butTheme.clicked.connect(self.themeEvent)
        self.butWindo.clicked.connect(self.windoEvent)
        self.butAbout.clicked.connect(lambda: self.aboutEvent(help))

        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )

        self.bar.addWidget(self.logo)
        self.bar.addWidget(spacer)

        if not simple:
            self.bar.addWidget(self.butTheme)
            # self.bar.addWidget(self.butWindo)

        self.bar.addWidget(self.butAbout)

        self.addToolBar(self.bar)
        self.addToolTips()

        self.restoreBarButtons()

    def addToolTips(self):
        """Description
        """
        self.butTheme.setToolTip("Change the theme to dark or light")
        self.butWindo.setToolTip("Restore/remove the window frame ")
        self.butAbout.setToolTip("bring more information about the app")

    def restoreBarButtons(self):
        """Description
        """
        table = {self.butTheme: 'theme', self.butWindo: "window"}

        for key, value in table.items():

            if hasattr(self, "settings"):
                stored = self.settings.load(value)

                if stored:
                    key.setChecked(eval(stored.capitalize()))
                    key.clicked.emit()

    def saveGeo(self):
        """Description
        """
        mainframe = self

        if self.dock:
            mainframe = self.parent()

        if hasattr(self, "settings"):
            self.settings.saveGeo(mainframe.geometry())

    def restoreGeo(self, minVal=0):

        mainframe = self

        if hasattr(self, "dock"):

            if self.dock:
                mainframe = self.parent()

        self.settings = Settings(self.objectName())

        thisgeo = QtCore.QRect(self.settings.geo)

        mainframe.setGeometry(self.settings.geo)
        self.settings.saveGeo(self.settings.geo)

        self.update()

    def windoEvent(self):
        """Description
        """
        if self.sender().isChecked():
            self.setWindowFlags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

        else:
            self.setWindowFlags(QtCore.Qt.Window)

        self.settings.save('window', self.sender().isChecked())
        self.show()

    def themeEvent(self, dark=False):
        """Description
        """
        butts = [self.butTheme, self.butWindo, self.butAbout]

        # -- darkTheme
        if self.sender().isChecked() or dark:

            self.setStyle(self.factoryDark)

            self.centralWidget().setStyleSheet("")
            self.setStyleSheet(_style)

            for butt in butts or []:

                butt.setStyleSheet("""
                    .QWidget{{
                    background-color: rgba(16,18,25,255);
                    }}
                    """)

        # -- lightTheme
        else:
            self.setStyle(self.factoryLgth)

            sty = """
                QPushButton{
                    border-style: solid;
                    height: 21px;
                    border-width:1px;
                    border-radius:2px;

                    border-color: #777777;
                    background-color: #5d5d5d;
                    color: #DDDDDD;
                }

                QPushButton:hover{
                    border-color: #999999;
                    color: #FFFFFF;
                }

                QGroupBox:hover{
                    color: rgb(0, 255, 0);
                }

                """

            self.setStyleSheet(sty)

            for butt in butts or []:
                butt.setMaximumHeight(self.miniSize - 6)
                butt.setFlat(True)

        if self.sender():

            for but in self.sender().parent().findChildren(QtWidgets.QPushButton) or []:
                but.setStyleSheet("\
                    QPushButton{background-color: rgba(255,255,0,0);}")

        if hasattr(self, "settings"):
            self.settings.save('theme', self.sender().isChecked())

    def pmap(self, path):

        pix = QtGui.QPixmap(path)
        pixresized = pix.scaled(self.miniSize - 10, self.miniSize - 10)
        return QtGui.QIcon(pixresized)

    def aboutEvent(self, help):
        """Description
        """
        logopath = '%s/logoHs_color.png' % root
        about = AboutWin(help)
        about.size(400, 800)
        about.setWindowTitle("Manual Reference")
        about.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(logopath)))
        about.setStyleSheet("")
        about.show()

# ====================================================================
# ====================================================================


class OpenGl(Frameless, QtCore.QObject):

    def __init__(self, parent=getMayaWin()):
        QtWidgets.QMainWindow.__init__(self, parent)
        pass


# ====================================================================
# ====================================================================
# ====================================================================
# ====================================================================

class Confirmation(QtWidgets.QWidget, QtCore.QObject):

    _output = str()

    returned = QtCore.Signal(tuple)

    _result = str()

    def __init__(self, genre="path",
                 label="",
                 infos="",
                 boomrang="",
                 placeHolder="",
                 object=None,
                 parent=None):

        QtWidgets.QWidget.__init__(self, parent)

        self.placeHolder = placeHolder
        self.boomrang = boomrang
        self.object = object
        self.label = label
        self.infos = infos
        self.genre = genre
        self.setWin()

        self.setPrefs()
        self.setConnections()

        self.mainPop.show()

    def setConnections(self):
        self.okButton.clicked.connect(self.apply)
        self.cancelButton.clicked.connect(self.ignore)
        self.input.returnPressed.connect(self.apply)
        self.input.installEventFilter(self)

    def eventFilter(self, obj, event):

        if obj == self.input:
            if (event.type() == QtCore.QEvent.KeyPress or
                    event.type() == QtCore.QEvent.KeyRelease):

                self.checkInput()
                obj.event(event)
                return True

        return False

    def __repr__(self):
        return self._result

    def checkInput(self):
        self.log.clear()

        text = str(self.input.text())

        if self.genre == "path":
            if not os.path.exists(text):
                self.okButton.setHidden(True)
                self.log.setText("\'{}\' does not exist".format(text))

            else:
                self.log.setText("status ok".format())
                self.okButton.setHidden(False)

    def ignore(self):

        self.returned.emit(tuple())
        self.mainPop.close()

    def apply(self):
        self.checkInput()
        path = str(self.input.text())
        self.returned.emit((path, self.boomrang))

        self._result = path
        self.mainPop.close()

    def setPrefs(self):
        self.notice.setAlignment(QtCore.AlignHCenter | QtCore.AlignVCenter)
        self.log.setAlignment(QtCore.AlignHCenter | QtCore.AlignVCenter)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.okButton.setHidden(True)

        self.mainPop.setWindowModality(QtCore.WindowModal)

        if self.placeHolder:
            self.input.setText(self.placeHolder)
            self.checkInput()

    def setWin(self):

        self.mainPop = Frameless()

        self.notice = QtWidgets.QLabel(self.label)
        self.input = QtWidgets.QLineEdit("")
        self.log = QtWidgets.QLabel(self.infos)

        self.okButton = QtWidgets.QPushButton("Confirm", self)
        self.cancelButton = QtWidgets.QPushButton("Ignore", self)

        mainLayout = QtWidgets.QVBoxLayout(self)
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.hlayout = QtWidgets.QHBoxLayout(self)

        self.vlayout.addWidget(self.notice)
        self.vlayout.addWidget(self.input)
        self.vlayout.addWidget(self.log)

        self.hlayout.addWidget(self.okButton)
        self.hlayout.addWidget(self.cancelButton)

        self.setLayout(mainLayout)
        mainLayout.addLayout(self.vlayout)
        mainLayout.addLayout(self.hlayout)

        self.mainPop.setCentralWidget(self)


class Prefs(QtWidgets.QWidget, QtCore.QObject):

    prefsChanged = QtCore.Signal(str)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWin()
        self.show()

    def setWin(self):

        self.mainPop = Frameless()


class ZiToolTip(QtWidgets.QWidget, QtCore.QObject):

    hovered = QtCore.Signal()

    def __init__(self, wid, subtitle, notice, gifpath, speed=100):
        QtWidgets.QWidget.__init__(self, None)

        self.thmbSze = 140
        self.width = 230
        self.height = 150

        self.notice = notice
        self.wid = wid

        self.subtitle = """<span style=" font-size:10pt; font-weight:600; color:#7e835a;">{}<span>""".format(
            subtitle)
        self.movie = None
        self.thmb = None
        self.thmbType = "gif"

        self.mainPop = Frameless()
        self.mainPop.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.mainPop.setStyleSheet("")

        self.setThumb(gifpath, speed)
        self.setWin()

        self.wid.installEventFilter(self)

    def setThumb(self, path, speed):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        self.thmb = QtWidgets.QLabel()

        if os.path.splitext(path)[-1].lower() == ".gif":

            self.thmbType = "animated"
            self.movie = QtGui.QMovie(path)

            self.movie.setSpeed(speed)
            self.movie.setCacheMode(QtGui.QMovie.CacheAll)
            self.movie.setFormat(QtCore.QByteArray(b"GIF"))

            self.thmb.setMovie(self.movie)

            self.movie.setScaledSize(QtCore.QSize(self.thmbSze, self.thmbSze))
            self.movie.start()

        else:

            self.thmbType = "fixed"
            self.thmb.setPixmap(QtGui.QPixmap(path))

    def eventFilter(self, obj, event):

        if obj == self.wid:

            if event.type() == QtCore.QEvent.Enter:
                self.mainPop.show()

            if (event.type() == QtCore.QEvent.HoverMove or
                    event.type() == QtCore.QEvent.Enter):

                self.mainPop.move(QtGui.QCursor.pos() + self.detectScreenpos())

            if event.type() == QtCore.QEvent.Leave:
                self.mainPop.close()

            event.accept()

        return False

    def detectScreenpos(self):

        mayaScreenRect = getMayaWin().geometry()
        cursorPos = QtGui.QCursor.pos()

        offset = QtCore.QPoint()
        width, height = (self.size().width(), self.size().height())
        h = 10

        # -- Acts on x alignment, could have the same approach for y
        if (cursorPos.x() + width) > mayaScreenRect.width():
            offset = QtCore.QPoint(-width, h)

        else:
            offset = QtCore.QPoint(10, h)

        return offset

    def setWin(self):

        self.mainPop.setStyleSheet("")
        self.notice = QtWidgets.QLabel(self.notice)
        self.notice.setMaximumWidth(150)

        sub = QtWidgets.QLabel(self.subtitle)
        sub.setTextFormat(QtCore.Qt.RichText)

        mainLayout = QtWidgets.QHBoxLayout()

        self.vlayout1 = QtWidgets.QVBoxLayout()
        self.vlayout2 = QtWidgets.QVBoxLayout()

        if self.thmbType == "animated":
            if self.movie.isValid():
                self.vlayout1.addWidget(self.thmb)

        if self.thmbType == "fixed":
            if self.thmb:
                self.vlayout1.addWidget(self.thmb)

        if self.subtitle.__len__() > 77:
            self.vlayout1.addWidget(sub)

        self.vlayout2.addWidget(self.notice)

        self.setLayout(mainLayout)
        mainLayout.addLayout(self.vlayout1)
        mainLayout.addLayout(self.vlayout2)

        self.mainPop.setCentralWidget(self)
        self.notice.setWordWrap(True)
        sub.setWordWrap(True)

        self.mainPop.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(self.width, self.height)
        self.setStyleSheet("")

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)

        margin = 4
        x, y = (self.size().width(), self.size().height())

        self.mainRect = QtGui.QPainterPath()
        self.mainRect.addRoundedRect(margin,
                                     margin,
                                     x - (margin * 2),
                                     y - (margin * 2),
                                     1, 1)

        painter.setPen(QtGui.QPen(QtGui.QColor(126, 131, 90), 2))
        painter.drawPath(self.mainRect)

        painter.end()


class ZiInvertButton(QtWidgets.QWidget, QtCore.QObject):
    """A inverted display label, with a clicked signal
    """

    clicked = QtCore.Signal()

    def __init__(self, label='Title', parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMouseTracking(True)

        self._label = label

        self.hovered = False
        self._on = False

        self._light = 170
        self._border = 5

        self._fillColor = QtGui.QColor(126, 131, 90)

    @property
    def light(self):
        return self._light

    @light.setter
    def light(self, value):
        self._light = value
        self.update()

    @property
    def label(self):
        return str(self._label)

    @label.setter
    def label(self, value):
        self._label = value
        self.update()

    @property
    def border(self):
        return self._border

    @border.setter
    def border(self, value):
        self._border = value
        self.update()

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, value):
        self._on = value
        self.update()

    @property
    def fillColor(self):
        return self._fillColor

    @fillColor.setter
    def fillColor(self, value):
        self._fillColor = value
        self.update()

    def mouseMoveEvent(self, event):

        if QtCore.QRectF(0, 0,
                         self.size().width(),
                         self.size().height()).contains(event.pos()):

            self.hovered = True

        else:
            self.hovered = False

        self.repaint()

    def leaveEvent(self, event):
        self.hovered = False
        self.update()

    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:
            self.on = False if self.on is True else True
            self.clicked.emit()
            self.update()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)

        font = QtGui.QFont('MS Sans Serif', 8, QtGui.QFont.Light)

        borderBrush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 245))

        textPath = QtGui.QPainterPath()
        textPath.addText(0, 0, font, self.label)

        bound = textPath.boundingRect()
        w = self.size().width()
        h = self.size().height()
        margingx = (w - bound.width()) * .5
        margingy = (h - bound.height()) * .5

        textPath.translate(margingx, margingy + bound.height())

        # -- border
        if self.hovered:
            painter.setPen(borderBrush.color())
        else:
            painter.setPen(QtGui.QColor(77, 77, 77))

        if self.on:
            textBrush = self.palette().window()
            painter.setBrush(QtGui.QBrush(self.fillColor))
        else:
            textBrush = QtGui.QBrush(QtGui.QColor(200, 200, 200, 245))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        painter.drawRoundedRect(0, 0, w - 1, h - 1, self.border, self.border)

        # -- text
        painter.setBrush(textBrush)
        painter.setPen(textBrush.color())
        painter.drawPath(textPath)

        painter.end()


class InteractiveText(QtWidgets.QTextBrowser, QtCore.QObject):
# class InteractiveText(QtWidgets.QTextEdit, QtCore.QObject):
    """Send a dblClick signal with the text double clicked
    """

    rightClick = QtCore.Signal()
    dblClick = QtCore.Signal(str)
    midClick = QtCore.Signal()

    def __init__(self, parent=None):
        QtWidgets.QTextBrowser.__init__(self, parent)

    def mouseDoubleClickEvent(self, event):
        QtWidgets.QTextBrowser.mouseDoubleClickEvent(self, event)

        cursor = self.textCursor()

        if cursor.hasSelection():
            text = cursor.selectedText()

            self.dblClick.emit(text)

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.MidButton:
            self.midClick.emit()

        if event.buttons() == QtCore.Qt.RightButton:
            self.rightClick.emit()


class AboutWin(QtWidgets.QWidget, QtCore.QObject):
    """Display a widown with html
    """

    def __init__(self, text, parent=None):
        super(AboutWin, self).__init__(parent)

        self.main = Frameless()
        self.doc = InteractiveText()
        self.doc.document().setDefaultStyleSheet(
            "p,li { white-space: pre-wrap; }")

        self.doc.setHtml(text)
        self.doc.setReadOnly(True)

        self.lay = QtWidgets.QVBoxLayout()
        self.lay.addWidget(self.doc)
        self.setLayout(self.lay)

        self.main.setCentralWidget(self)
        self.main.setStyleSheet("")

        self.main.show()

    def setContent(self, txt):
        self.doc.setHtml(txt)

    def setWindowTitle(self, title):
        """Set the title of the windown
        """
        self.main.setWindowTitle(title)

    def size(self, x=470, y=170):
        """Reset the size of the window
        """
        self.main.resize(x, y)



class ziFrame(QtWidgets.QFrame, QtCore.QObject):

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)

        self.pixup = QtGui.QPixmap("/layer/arrow_up.png" & root)
        self.pixdn = QtGui.QPixmap("/layer/arrow_dn.png" & root)
        self.collapeBtn = QtWidgets.QPushButton()
        self.collapeBtn.setIcon(QtGui.QIcon(self.pixdn))

        self.setWidget()

    def setWidget(self):

        self.hlayout = QtWidgets.QHBoxLayout()
        self.addWidget(self.collapeBtn)

    def addWidget(self, widget):
        self.layout().addWidget(widget)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.HighQualityAntialiasing)

    #     self.w = self.size().width()
    #     self.h = self.size().height()

    #     radius = 2
    #     position = QRect(self.w - 35, 5, 20, 20)

    #     painter.setPen(QPen(QColor(255, 255, 0), 3))
    #     painter.drawPixmap(position, self.pixup)
    #     painter.drawText(self.w * .5, self.h * .5, "dedede")

    #     # painter.drawRoundedRect(self.w - 35, 5, 30, 20, radius, radius, )
    #     painter.end()


class ziCollapse(QtWidgets.QGroupBox, QtCore.QObject):

    collapsed = QtCore.Signal(bool)

    def __init__(self, url, parent=None):
        QtWidgets.QGroupBox.__init__(self, parent)
        self.open = True
        self.inside = False

        self.setContentsMargins(0, 0, self.width(), 20)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:

            if self.inside:
                self.collapse()
                self.collapsed.emit(self.inside)

    def mouseMoveEvent(self, event):

        self.inside = False

        if QtCore.QRect(self.width()*.33, 0,
                        self.width()*.33, 10).contains(event.pos()):

            self.inside = True
            self.setCursor(QtCore.Qt.ClosedHandCursor)

            if self.open:
                stSheet = "\nQGroupBox{color: rgb(255,255,255);font-weight: bold;}"
                self.setStyleSheet(stSheet)

        if not self.inside:
            self.setCursor(QtCore.Qt.ArrowCursor)

            if self.open:
                self.setStyleSheet("")

    def collapse(self):

        self.open = not self.open

        map(lambda x: x.setVisible(self.open),
            self.findChildren(QtWidgets.QWidget))

        stSheet = "" if self.open else "QGroupBox{ color: rgb(126,131,90);}"
        self.setStyleSheet(stSheet)


class VertextureLogo(QtWidgets.QLabel, QtCore.QObject):

    def __init__(self, url="https://vertexture.org/?source=mayapp", parent=None):
        QtWidgets.QLabel.__init__(self, parent)

        self.url = url
        self.setCursor(QtCore.Qt.DragMoveCursor)

    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:
            import webbrowser
            webbrowser.open(self.url, new=2)


class Settings(QtCore.QObject):

    def __init__(self, name):
        self.qsettings = QtCore.QSettings('Vertexture', name)

    def clear(self):
        self.qsettings.clear()

    def save(self, attr, value):
        self.qsettings.setValue(attr, value)

    def saveGeo(self, geo):

        self.save("x", geo.x())
        self.save("y", geo.y())
        self.save("width", geo.width())
        self.save("height", geo.height())

    @property
    def geo(self):

        x = self.load("x")
        y = self.load("y")
        h = self.load("width")
        w = self.load("height")

        if x and y and h and w:
            return QtCore.QRect(int(x), int(y), int(h), int(w))
        else:
            return QtCore.QRect(0, 0, 500, 500)

    def load(self, attr):

        if self.qsettings.contains(attr):
            return self.qsettings.value(attr)


class ziScrub(QtWidgets.QWidget, QtCore.QObject):
    """Text displaying different value with a move drag
    """

    fuzzed = QtCore.Signal(str)
    hovered = QtCore.Signal(str)
    changed = QtCore.Signal(float)
    scrubed = QtCore.Signal(float)
    released = QtCore.Signal(float)
    leave = QtCore.Signal()

    family = 'MS Sans Serif'

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMouseTracking(True)

        self.parent = parent
        self.index = 0  # -- to del for families

        self.mainPath = QtGui.QPainterPath()
        self.text = 'Property'
        self.weight = 'light'
        self._value = 0

        self._min = 0
        self._max = 100

        self.textColor = QtGui.QColor(255, 255, 255, 255).darker(140)
        self.wasFloat = False
        self.clicked = False
        self.openKey = False
        self.waiting = False
        self.fontSize = 10
        self._data = False
        self.count = int()
        self.prev = False
        self.on = False
        self.step = 1
        self.raw = 0

        self.set_type("int")
        self.font = QtGui.QFont()
        self.sign = 0

        self.ephemere = False

        self._opacity = 255
        self._knobHeigth = .3
        self._knobColor = self.textColor

        self.setMinimumHeight(20)

    def copy(self, geo):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        dupObj = ziScrub(getViewPortWidget())

        dupObj.value = self.value
        dupObj.index = self.index
        dupObj.text = self.text

        dupObj.setGeometry(geo[0] - self.value,
                           geo[1] - (self.geometry().height() * .5),
                           self.geometry().width(),
                           self.geometry().height()
                           )

        dupObj.changed.connect(lambda: self.setValue(dupObj.value))

        return dupObj

    def set_type(self, typ):

        if typ == 'int':
            self.int, self.float, self.string = [True, False, False]

        if typ == 'float':
            self.int, self.float, self.string = [False, True, False]

        if typ == 'string':
            self.int, self.float, self.string = [False, False, True]

    def set_behaviors(self,
                      text,
                      max,
                      min,
                      value,
                      typ="int",
                      weight="normal",
                      fontsize=10
                      ):

        self.max = max
        self.min = min
        self.text = text
        self.value = value
        self.value2raw(value)
        self.set_type(typ)
        self.weight = weight

    @classmethod
    def setSize(cls, value):
        cls.fontSize = value

    @classmethod
    def setFont(cls, value):
        cls.family = value

    @classmethod
    def setHeight(cls, value):
        cls.setMaximumHeight(value)

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, min):
        self._min = min

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, max):
        self._max = max

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.update()

    @property
    def fontSize(self):
        return self._fontSize

    @fontSize.setter
    def fontSize(self, value):
        self._fontSize = value
        self.update()

    @property
    def w(self):
        return self.size().width()

    @property
    def h(self):
        return self.size().height()

    @property
    def textColor(self):
        return self._txtcolor

    @textColor.setter
    def textColor(self, value):
        self._txtcolor = value

    @property
    def step(self):
        return self._inc

    @step.setter
    def step(self, value):
        self._inc = value

    @property
    def data(self):
        return self._data

    @property
    def knobColor(self):
        return self._knobColor

    @knobColor.setter
    def knobColor(self, value):
        self._knobColor = QtGui.QColor(*value)

    @data.setter
    def data(self, value):
        self._data = value
        self.int, self.float, self.string = [False, False, False]

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):

        if value == 'light':
            self._weight = QtGui.QFont.Light

        if value == 'normal':
            self._weight = QtGui.QFont.Normal

        if value == 'demiBold':
            self._weight = QtGui.QFont.DemiBold

        if value == 'bold':
            self._weight = QtGui.QFont.Bold

        if value == 'black':
            self._weight = QtGui.QFont.Black

        self.update()

    @property
    def value(self):
        return self._value

    def raw2value(self, raw):
        res = self.min + ((raw / 100.0) * (self.max - (self.min)))
        self._value = self.max if res > self.max else res
        self._value = self.min if res < self.min else res

        self.value = res

    def value2raw(self, value):
        self.raw = (value - self.min) / float((self.max - (self.min))) * 100
        self.repaint()

    @value.setter
    def value(self, value):

        if self.string:
            self._value = str(value)
            self.update()
            return

        if self.data:
            self._value = value

            self.update()
            return

        # -- if specific datas (i.e 8,16,32)
        else:
            if self._data:

                if value in self._data:
                    ind = self.data.index(value)

                    if self.value > value:
                        self._value = self.data[ind - 1]
                        return

                    if self.value < value:
                        if len(self.data) > ind + 1:
                            self._value = self.data[ind + 1]
                            return
            elif value == '':
                self._value = value
                return

            # -- int or float
            else:
                self._value = value

        self.changed.emit(self._value)
        self.value2raw(value)
        self.update()

    def setValue(self, value):
        """Description

        :Param var(None): desc.
        :Return (None): desc.
        """
        self.value = value

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.clicked = True
            self.prev = False

            self.openKey = True
            self.waiting = True

            # self._value = '_'

            self.update()
            event.accept()

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Enter \
                or event.key() == QtCore.Qt.Key_Escape \
                or event.key() == QtCore.Qt.Key_Return:
            self.openKey = False

            if self.wasFloat:
                self.wasFloat = False
                self.set_type('float')
                self.value = round(float(self.value), 2)

            self.scrubed.emit(self.value)

            self.update()
            event.accept()
            return

        # -- correcting by deleting previous keystroke
        if event.key() == QtCore.Qt.Key_Backspace:
            if isinstance(self.value, str):
                self.value = self.value[:-1]
                if len(self.value) < 2:
                    self.value = ''

            elif isinstance(self.value, int):
                self.value = int(str(self.value)[:-1])

            elif isinstance(self.value, float):
                self.value = float(str(self.value)[:-1])

            self.update()
            event.accept()
            return

        # -- typing
        if self.openKey:

            if self.value == '_':
                try:
                    self.value = str(event.text()) if self.string\
                        else int(event.text())
                except ValueError:
                    pass
            else:
                newValue = '{}{}'.format(self.value, event.text())

                try:
                    if self.wasFloat:
                        self.set_type('float')
                    if self.string:
                        self.value = str(newValue)
                    if self.int:
                        self.value = int(newValue)
                    if self.float:
                        if event.text() == '.':
                            self.set_type('string')
                            self.value = str(newValue)
                            self.wasFloat = True
                        else:
                            self.value = float(newValue)
                except ValueError:
                    pass

                self.fuzzed.emit(str(self.value))

            self.update()
            event.accept()

    def mouseDoubleClickEvent(self, event):

        if self.data:
            return

    def mouseMoveEvent(self, event):

        if self.mainPath.boundingRect().contains(event.pos()):
            self.hovered.emit(self.toolTip())
            self.on = True
        else:
            self.on = False

        if self.clicked:

            current = event.pos()
            self.raw = current.x() / float(self.w) * 100

            self.raw = 100 if self.raw > 100 else self.raw
            self.raw = 0 if self.raw < 0 else self.raw

            self.raw2value(self.raw)

        self.repaint()

    def leaveEvent(self, event):
        self.on = False
        self.update()

        if self.ephemere:
            self.close()
            self.deleteLater()

        self.leave.emit()

    def mouseReleaseEvent(self, event):

        self.clicked = False
        self.sign = 0

        self.released.emit(self.value)
        self.update()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.begin(self)

        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        self.mainPath = QtGui.QPainterPath()

        # 0 --->> w
        xpos = self.raw / 100.0 * (self.w)

        xpos = self.w if xpos > self.w else xpos
        xpos = 0 if xpos < 0 else xpos

        # -- background, set explicitly here as opaque
        painter.setBrush(QtGui.QBrush(QtGui.QColor(51, 51, 54, self._opacity)))
        painter.drawRoundedRect(0, 0, self.w - 1, self.h - 1, 2, 2)

        # -- jauge
        if self.on:

            gradJauge = QtGui.QLinearGradient(0, 0, xpos, self.h)
            coloJauge = QtGui.QColor(126, 131, 90, 255)

            coloJauge.setAlpha(0)
            gradJauge.setColorAt(0.3, coloJauge)
            coloJauge.setAlpha(255)
            gradJauge.setColorAt(1, coloJauge)

            painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
            painter.setBrush(QtGui.QBrush(gradJauge))
            painter.drawRoundedRect(4, self.h * .2,
                                    xpos - 4,
                                    self.h * .6, 3, 3)

            painter.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        # -- bottom line
        gradient = QtGui.QLinearGradient(0, 0, self.w, self.h)
        gradColor = self.textColor
        blankColor = QtGui.QColor(self.textColor).darker(290)

        if self.on:
            gradColor = self.textColor.lighter(190)
            blankColor = blankColor.lighter(190)

        if self.sign > 0:
            gradColor = QtGui.QColor(gradColor.red(), 0, 0)

        if self.sign < 0:
            gradColor = QtGui.QColor(0, 0, gradColor.blue())

        if self.sign == 0:
            gradColor = QtGui.QColor(gradColor.red(),
                                     gradColor.green(),
                                     gradColor.blue())

        gradColor.setAlpha(0)
        gradient.setColorAt(0, gradColor)

        gradColor.setAlpha(255)
        gradient.setColorAt(0.35, gradColor)
        gradient.setColorAt(0.65, gradColor)

        gradColor.setAlpha(0)
        gradient.setColorAt(1, gradColor)
        gradColor.setAlpha(255)

        painter.setPen(QtGui.QPen(gradient, 1.0))
        painter.drawLine(0, self.h * .8, self.w, self.h * .8)

        # -- border
        painter.setPen(QtGui.QPen(blankColor, 1.0))
        self.mainPath.addRoundedRect(0, 0, self.w - 1, self.h - 1, 2, 2)
        painter.drawPath(self.mainPath)

        # -- text
        self.font.setPointSize(self.fontSize)
        self.font.setWeight(self.weight)
        self.font.setFamily(self.family)
        painter.setFont(self.font)

        painter.setPen(QtGui.QPen(self.textColor.darker(120), 1.0))

        othervalue = "{:.2f}".format(float(self.value))
        value = int(self.value) if self.int is True else othervalue

        painter.drawText(7, self.h * .7, "{} {}".format(self.text, value))

        # -- knob
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        knobColor = self.knobColor

        knobColor.setAlpha(80)
        painter.setBrush(knobColor)

        knobRadius = 12
        painter.drawEllipse(xpos - (knobRadius * .5),
                            self.h * self._knobHeigth,
                            knobRadius, knobRadius)

        knobColor.setAlpha(255)
        painter.setBrush(knobColor)

        knobRadius = knobRadius * .6
        painter.drawEllipse(xpos - (knobRadius * .5),
                            (self.h * self._knobHeigth) + knobRadius * .5,
                            knobRadius, knobRadius)

        painter.end()


class ZiLayer(QtWidgets.QWidget, QtCore.QObject):
    """Photoshop like layer widget
    display a label with icons

    usage:
    lay = Layer()
    lay.setPixFirst(pixmap, pixmap)
    lay.setPixSecond(pixmap, pixmap)
    lay.setThumb(pixmap)
    lay.setLabel(string)
    """

    border = 2
    thumSiz = 22

    DBLClicked = QtCore.Signal(str)
    MMBClicked = QtCore.Signal()
    LMBClicked = QtCore.Signal()
    RMBClicked = QtCore.Signal(str)

    firstClicked = QtCore.Signal()
    secondClicked = QtCore.Signal()
    thumbClicked = QtCore.Signal()
    # labelClicked= QtCore.Signal(str)

    clickedColor = outColor = QtGui.QColor(39, 40, 46)

    def __init__(self, label="", opacity=1, option="", parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setMouseTracking(True)

        self.addPath = QtGui.QPainterPath()
        self.firstOff = QtGui.QPixmap()
        self.firstOn = QtGui.QPixmap()

        self.secondOff = QtGui.QPixmap()
        self.secondOn = QtGui.QPixmap()

        self.thumbOff = QtGui.QPixmap()
        self.thumbOn = QtGui.QPixmap()

        self._selected = False
        self._thumbed = False
        self.hovered = False

        self.thumb = QtGui.QPixmap()
        self.firstPix = QtGui.QPixmap()
        self.secondPix = QtGui.QPixmap()
        self.rect = QtCore.QRect(80, 0,
                                 self.size().width() - 50,
                                 self.size().height())

        self.setMaximumSize(950, 70)
        self.setMinimumSize(100, 45)
        self.insideColor = QtGui.QColor(61, 62, 70)

        self._label = label
        self._option = option
        self._font = QtGui.QFont()
        self.setFont()

        self._scrub = ziScrub(self)

    def setScrubGeo(self, rect):

        if not self.rectSecond:
            return

        self.scrub.setGeometry(
            rect.left(),
            rect.bottom() + self.border,
            self.size().width() - rect.left() - (self.border * 2),
            self.size().height() - rect.height(),
        )

        self.scrub.setFixedHeight(15)
        self.scrub.setSize(7)

    @property
    def scrub(self):
        return self._scrub

    def set_behaviors(self, label="layer1", option=""):

        self.setLabel(label)
        self.option = option

    def setPixFirst(self, openPix, closePix, size=20):

        self.firstOff = closePix.scaled(size, size)
        self.firstOn = openPix.scaled(size, size)

        self.firstPix = self.firstOn

    def setPixSecond(self, openPix, closePix, size=20):

        self.secondOff = closePix.scaled(size, size)
        self.secondOn = openPix.scaled(size, size)

        self.secondPix = self.secondOn

    def setPixThumb(self, onPix, offPix, size=20):

        self.thumbOff = offPix.scaled(size, size)
        self.thumbOn = onPix.scaled(size, size)

        self.thumb = self.thumbOff

    def setLabel(self, label):
        self._label = label

    def swapSecond(self, invert=True, switch='ON'):

        if invert:

            if self.secondPix == self.secondOn:
                self.secondPix = self.secondOff

            else:
                self.secondPix = self.secondOn

        else:
            if switch == 'ON':
                self.secondPix = self.secondOff

            if switch == 'OFF':
                self.secondPix = self.secondOn

        self.update()

    def swapFirst(self, invert=True, switch='ON'):

        if invert:

            if self.firstPix == self.firstOn:
                self.firstPix = self.firstOff

            else:
                self.firstPix = self.firstOn

        else:
            if switch == 'ON':
                self.firstPix = self.firstOff

            if switch == 'OFF':
                self.firstPix = self.firstOn

        self.update()

    def swapThumb(self, invert=True, switch='ON'):

        if invert:
            if self.thumb == self.thumbOn:
                self.thumb = self.thumbOff

            else:
                self.thumb = self.thumbOn

            self.thumbed = False if self.thumb == self.thumbOff else True

        else:
            if switch == 'ON':
                self.thumb = self.thumbOn
                self.thumbed = True

            if switch == 'OFF':
                self.thumb = self.thumbOff
                self.thumbed = False

        self.update()

    @property
    def insideColor(self):
        return self._incolor

    @insideColor.setter
    def insideColor(self, color):
        self._incolor = color

    @property
    def option(self):
        if self._option == '':
            return ''
        return self._option

    @property
    def selected(self):
        return self._selected

    @property
    def thumbed(self):
        return self._thumbed

    @property
    def label(self):
        if self._label:
            return str(self._label)
        else:
            return ''

    @property
    def font(self):
        return self._font

    @property
    def secondIsOn(self):
        value = False if self.secondPix == self.secondOn else True
        return value

    @property
    def firstIsOn(self):
        value = False if self.firstPix == self.firstOff else True
        return value

    @selected.setter
    def selected(self, value):
        self._selected = value
        self.update()

    @property
    def file(self):
        return self._file

    @label.setter
    def label(self, value):
        self._thumbed = value
        self.update()

    @thumbed.setter
    def thumbed(self, value):
        self._thumbed = value
        self.update()

    @option.setter
    def option(self, value):
        self._option = str(value)

    def setFont(self, size=10, weight=25, family="MS Sans Serif"):
        self._font.setPointSize(size)
        self._font.setWeight(weight)
        self._font.setFamily(family)
        self.update()

    def leaveEvent(self, event):
        self.hovered = False
        self.clickedColor = self.outColor
        self.update()

    def mouseDoubleClickEvent(self, event):
        self.DBLClicked.emit(self.label)

    def mouseMoveEvent(self, event):

        if self.contentsRect().contains(event.pos()):
            self.hovered = True
            self.clickedColor = self.insideColor

        else:
            self.hovered = False
            self.clickedColor = self.outColor

        self.update()

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            if self.rectFirst.contains(event.pos()):
                self.swapFirst()
                self.firstClicked.emit()

            if self.rectSecond.contains(event.pos()):
                self.swapSecond()
                self.secondClicked.emit()

            if self.rectTmb.contains(event.pos()):
                self.swapThumb()
                self.thumbClicked.emit()

            if self.rect.contains(event.pos()):
                self._selected = not self._selected
                self.LMBClicked.emit()

            self.update()

        if event.buttons() == QtCore.Qt.RightButton:
            if self.rectFirst.contains(event.pos()):
                self.RMBClicked.emit('first')
                return

            if self.rectSecond.contains(event.pos()):
                self.RMBClicked.emit('second')
                return

            if self.rectTmb.contains(event.pos()):
                self.RMBClicked.emit('thumb')
                return

            if self.rect.contains(event.pos()):
                self.RMBClicked.emit('main')
                return

        if event.buttons() == QtCore.Qt.MidButton:
            self.MMBClicked.emit()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)

        border = self.border
        thumSiz = self.thumSiz

        icoSiz = thumSiz - border
        size = self.size()

        backgGrad = QtGui.QLinearGradient()
        color = QtGui.QColor(50, 50, 50, 100)
        avar = 1.5 if self.selected else 1

        backgGrad.setColorAt(0.00, color.lighter(0 * avar))
        backgGrad.setColorAt(0.45, color.lighter(102 * avar))
        backgGrad.setColorAt(0.5, color.lighter(40 * avar))
        backgGrad.setColorAt(1.0, color.lighter(60 * avar))

        backgGrad.setStart(QtCore.QPointF(0, 0))
        backgGrad.setFinalStop(QtCore.QPointF(0, self.height()))

        # ------------------------------------ BACKGROUND
        painter.setBrush(backgGrad)
        painter.drawRoundedRect(0, 0,
                                size.width() - border,
                                size.height() - border,
                                border, border)

        # ------------------------------------ BORDER
        painter.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        gradient = QtGui.QLinearGradient(0, 0, size.width(), 0)
        gradColor = QtGui.QColor(self.insideColor)

        gradColor.setAlpha(200)
        gradient.setColorAt(0, gradColor)

        gradColor.setAlpha(0)
        gradient.setColorAt(0.35, gradColor)
        gradient.setColorAt(0.65, gradColor)

        gradColor.setAlpha(200)
        gradient.setColorAt(1, gradColor)

        if not self.hovered:
            painter.setPen(QtGui.QPen(QtGui.QBrush(gradient), 1))

        if self.hovered:
            painter.setPen(QtGui.QPen(QtGui.QBrush(
                QtGui.QColor(180, 180, 180)), 1))

        if self.selected:
            painter.setPen(QtGui.QPen(
                QtGui.QBrush(QtGui.QColor(126, 131, 90)), 1))

        painter.drawRoundedRect(0, 0,
                                size.width() - border,
                                size.height() - border,
                                border, border)

        # ------------------------------------ FIRST
        self.rectFirst = QtCore.QRect(border * 2, border, icoSiz, icoSiz)

        if not self.firstPix.isNull():
            painter.drawPixmap(self.rectFirst, self.firstPix)

        # ------------------------------------ SECOND
        self.rectSecond = QtCore.QRect(self.rectFirst.right() + border,
                                       border,
                                       icoSiz,
                                       icoSiz)

        if not self.secondPix.isNull():
            painter.drawPixmap(self.rectSecond, self.secondPix)

        # ------------------------------------ THUMB
        self.rectTmb = QtCore.QRect(self.rectSecond.right() + (icoSiz * .7),
                                    border,
                                    thumSiz,
                                    thumSiz)

        painter.drawPixmap(self.rectTmb, self.thumb)

        self.setScrubGeo(self.rectTmb)

        if not self.hovered:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(153, 153, 155, 200)))

        if self.hovered or self.selected:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(233, 233, 235, 255)))

        painter.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))
        painter.setFont(self.font)
        painter.setPen(QtGui.QPen(QtGui.QColor(153, 153, 155, 255), .5))

        # ------------------------------------ TEXT
        rectText = QtCore.QRect(self.rectTmb.right() + border,
                                self.rectTmb.bottom(),
                                icoSiz,
                                icoSiz)

        painter.drawText(rectText.left(),
                         self.rectTmb.bottom() - self.rectTmb.top(),
                         self.label.capitalize())

        # ----------------------------------- OPTION >> text(option)
        painter.setFont(QtGui.QFont(self.font.family(),
                                    int(self.font.pointSize() * .9),
                                    -1,
                                    True))

        optionPath = QtGui.QPainterPath()
        optionPath.addText(0, 0, self.font, self.option.capitalize())

        painter.drawText(size.width() - (border * 2) - optionPath.boundingRect().width(),
                         self.rectTmb.bottom() - self.rectTmb.top(),
                         self.option.capitalize())


class ziGraph(QtWidgets.QWidget,
              QtCore.QObject):

    dblClicked = QtCore.Signal((float, float))
    clicked = QtCore.Signal((float, float))

    def __init__(self, attribute, label="property", parent=getMayaWin()):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.gridColor = QtGui.QColor(190, 190, 190, 50)
        self.gradColor = QtGui.QColor(30, 40, 65, 150)
        self.curveColor = QtGui.QColor(126, 131, 90)

        self.clampx = self.clampy = 0

        self._keyframes = []
        self.border = 25

        self.label = ""
        self.attribute = attribute

        self.hoverIndex = -1
        self.hoverPoly = False
        self.holdingKey = False
        self.currentItem = None

        self.prevMouse = QtCore.QPoint()
        self.prevPointPosx = 0
        self.prevPointPosy = 0

        self.pointsPaths = []
        self.points = []

        self.maxTime = cmds.playbackOptions(maxTime=True, q=True)
        self.minTime = cmds.playbackOptions(minTime=True, q=True)
        self.numGrid = int(self.maxTime - self.minTime)
        self.unit = 0

        self.timemouse = 0

        self.storeKeyFrames(attribute, label)
        self.setSize()

    @property
    def time(self):
        return cmds.currentTime(query=True)

    @time.setter
    def time(self, value):
        cmds.currentTime(value, edit=True)

    @property
    def keyframes(self):
        return self._keyframes

    def setCurveColor(self, color):
        self.curveColor = QtGui.QColor(*color)

    def curveValue(self, time):
        """Description

        :Param value(None): desc.
        :Return (None): desc.
        """
        return cmds.getAttr(self.attribute, t=time)

    def storeKeyFrames(self, attribute, label=""):

        self.attribute = attribute

        keyframes = cmds.keyframe(attribute, q=True)

        # -- make sure it has a key, otherwise wont output anything
        if keyframes:
            values = cmds.keyframe(attribute, vc=True, q=True)
            self._keyframes = zip(keyframes, values)

        if not label:
            label = self.attribute

        self.label = label

    def refreshFrames(self, force=True):
        self.storeKeyFrames(self.attribute)

        if force:
            self.update()
            self.setSize()

    def setCurrentPoint(self, item):
        """So the current selected item could be emphazised
        """
        self.currentItem = item

    def setSize(self):
        """Description
        """
        # -- reinit values
        self.clampy = 0
        self.unit = self.width() / (self.maxTime - self.minTime)

        if not self.keyframes:
            return

        for keyf, value in self.keyframes:

            if self.clampx < keyf:
                self.clampx = keyf

            if self.clampy < value:
                self.clampy = value

        self.update()

    def currentMouseTime(self, event):
        return (event.pos().x() / float(self.unit)) + self.minTime

    def selectedFrame(self):

        return (math.floor(self.keyframes[self.hoverIndex][0]),
                math.ceil(self.keyframes[self.hoverIndex][0]))

    def resizeEvent(self, event):
        # -- so we don't have over stretched windows
        self.setSize()

    def mouseReleaseEvent(self, event):
        self.holdingKey = False

    def mouseDoubleClickEvent(self, event):
        # need to fill with the keyframe and its value, fix
        self.dblClicked.emit(0, 0)

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:

            if not self.hoverIndex == -1:
                self.clicked.emit(self.hoverIndex, self.timemouse)

            # -- inset key at the mouse position
            if (event.modifiers() & QtCore.Qt.ControlModifier):
                cmds.setKeyframe(self.attribute,
                                 time=round(self.timemouse),
                                 insert=True)

        if event.buttons() == QtCore.Qt.RightButton:

            if self.hoverIndex == -1:
                return

            # -- inset key at the mouse position
            if (event.modifiers() & QtCore.Qt.ControlModifier):

                cmds.selectKey(self.attribute, clear=True)
                cmds.cutKey(self.attribute,
                            time=(self.selectedFrame()))

    def mouseMoveEvent(self, event):

        self.timemouse = self.currentMouseTime(event)

        if event.buttons() == QtCore.Qt.RightButton:
            cmds.currentTime(round(self.timemouse))

            return

        for i in range(self.pointsPaths.__len__()):

            if not self.holdingKey:

                # self.hoverPoly = False
                # self.hoverIndex = -1
                pass

                if self.pointsPaths[i].contains(event.pos(), QtCore.Qt.OddEvenFill):

                    self.hoverPoly = True
                    self.hoverIndex = i

                    break

        if event.buttons() == QtCore.Qt.LeftButton:

            if not self.hoverIndex == -1:

                if not self.holdingKey:
                    self.prevMouse = event.globalPos()

                    self.prevPointPosx = self._keyframes[self.hoverIndex][0]
                    self.prevPointPosy = self._keyframes[self.hoverIndex][1]

                    self.holdingKey = True

                    return

            if self.holdingKey:

                dist = event.globalPos() - self.prevMouse

                if self.clampy == 0:
                    return

                x = self.prevPointPosx + (dist.x() / self.unit)
                y = self.prevPointPosy - \
                    (dist.y() / (self.size().height() / self.clampy))

                try:
                    cmds.keyframe(self.attribute,
                                  e=True,
                                  a=True,
                                  vc=y,
                                  tc=x,
                                  t=(self._keyframes[self.hoverIndex][0],
                                     self._keyframes[self.hoverIndex][0])
                                  )
                except:
                    pass

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

        if event.key() == QtCore.Qt.Key_Left:
            self.setSize()
            self.update()

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing |
                               QtGui.QPainter.TextAntialiasing)

        # -- BACKGROUND
        gradient = QtGui.QRadialGradient(self.width() * .5,
                                         self.height() * 1,
                                         self.height() * 1,
                                         self.width() * .5,
                                         self.height() * .5)

        gradient.setColorAt(0, self.gradColor.lighter(160))
        gradient.setColorAt(1, self.gradColor.darker(160))
        painter.setBrush(gradient)
        painter.drawRect(0, 0, self.width(), self.height())

        # -- GRIDS
        gridThick = 0.5
        penColor = self.gridColor
        for v in range(int(self.maxTime - self.minTime) * 2):

            if v % 5 == 0:

                painter.setPen(QtGui.QPen(penColor.lighter(190),
                                          gridThick * 1.3
                                          ))

            else:

                painter.setPen(QtGui.QPen(penColor.darker(150),
                                          gridThick * 1.8))

            painter.drawLine(v * self.unit, 0, v *
                             self.unit, self.height() * 1.5)
            painter.drawLine(0, v * self.unit, self.width()
                             * 1.5, v * self.unit)

        if self._keyframes and not self.clampy == 0 and not self.clampx == 0:

            self.coef = (self.height() - self.border) / float(self.clampy)
            self.coefx = (self.width() - self.border) / float(self.clampx)

            self.paintKeys(painter)

        # -- LABEL

        labelPath = QtGui.QPainterPath()
        # labelsize = 24 * (14 * self.label.__len__()) / self.width()
        labelsize = 24

        labelPath.addText(0.0, 0.0,
                          QtGui.QFont('FreeSans', labelsize,
                                      QtGui.QFont.Normal), self.label)

        labelPath.translate(
            (self.width() * .5) - (labelPath.boundingRect().width() * .5),
            (self.height() * 1) - (labelPath.boundingRect().height() * .5)
        )

        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        painter.drawPath(labelPath)

        # -- TIME SLIDER
        painter.drawRoundedRect(
            (self.time * self.unit) - (self.minTime * self.unit),
            0,
            3,
            self.height(),
            1, 1
        )

        # -- STATS
        order = ('attribute',
                 "keyPos",
                 "mousePos",
                 "currentTime",
                 "minTime",
                 'maxTime'
                 )

        stats = {
            order[0]: self.attribute,
            order[1]: self.keyframes[self.hoverIndex][0],
            order[2]: self.timemouse,
            order[3]: self.time,
            order[4]: self.minTime,
            order[5]: self.maxTime,
        }

        for i, value in enumerate(order):

            painter.setPen(QtGui.QPen(self.curveColor, gridThick * 1.3))
            token = "{}: {:.1f}" if isinstance(
                stats[order[i]], float) else "{}: {}"

            painter.drawText(
                self.border * .2,
                self.border * .5 * (i + 1),
                token.format(order[i].capitalize(), stats[order[i]])
            )

    def paintKeys(self, painter):

        self.refreshFrames()

        if self.keyframes.__len__() < 2:
            return

        self.points = []
        self.pointsPaths = []

        line = QtCore.QPoint()
        ptSize = 8

        i = 1
        for key, value in self.keyframes:

            point = QtCore.QPoint((key * self.unit) - (self.minTime * self.unit),
                                  self.height() - (value * self.coef))

            line = QtCore.QPoint((self.keyframes[i][0] * self.unit) - (self.minTime * self.unit),
                                 self.height() - (self.keyframes[i][1] * self.coef))

            self.points.append(QtCore.QPoint(point))

            self.pointsPaths.append(
                QtCore.QRect(
                    point.x() - ptSize,
                    point.y() - ptSize,
                    ptSize * 2,
                    ptSize * 2)
            )

            pen = QtGui.QPen(QtGui.QBrush(self.curveColor.lighter(190)),
                             2,
                             QtCore.Qt.SolidLine,
                             QtCore.Qt.RoundCap,
                             QtCore.Qt.RoundJoin)

            # -- VALUES ON CURVES
            painter.setPen(pen)
            painter.setFont(QtGui.QFont('FreeSans', 8, QtGui.QFont.Normal))
            painter.drawText(point - QtCore.QPoint(10, 5), self.digit(value))

            # -- DRAW LEDGENDS
            painter.setFont(QtGui.QFont('FreeSans', 7, QtGui.QFont.Normal))

            painter.setPen(QtGui.QPen(QtGui.QBrush(
                QtGui.QColor(200, 200, 200, 150)),
                1,
                QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap,
                QtCore.Qt.RoundJoin))

            painter.drawText(point.x(), self.height() - 2, self.digit(key))

            if i < self.keyframes.__len__() - 1:
                i += 1

        # -- CURVE
        solids = []
        solids.append(QtCore.QPointF())

        curve = QtGui.QPainterPath()
        start = self.minTime
        step = .5

        while start < self.maxTime:

            point = QtCore.QPoint(start * self.unit - (self.minTime * self.unit),
                                  self.height() - (self.curveValue(start) * self.coef))

            curve.moveTo(point)
            curve.lineTo(QtCore.QPoint(((start + step) * self.unit) - (self.minTime * self.unit),
                                       self.height() - (self.curveValue(start + step) * self.coef))
                         )

            solids.append(point)
            start += step

        # -- DRAW INSIDE
        solids[0] = QtCore.QPointF(0, self.height())
        solids.append(QtCore.QPointF(line.x(), self.height()))

        colorPoly = QtGui.QLinearGradient(QtCore.QPoint(0, 0),
                                          QtCore.QPoint(0, self.height()))

        polyColor = QtGui.QColor(self.curveColor)
        colorPoly.setColorAt(0, polyColor)
        colorPoly.setColorAt(1, QtGui.QColor(polyColor.red(),
                                             self.curveColor.green(),
                                             self.curveColor.blue(), 5))

        painter.setBrush(QtGui.QBrush(colorPoly))
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        painter.drawPolygon(solids)

        # -- DRAW CURVE
        pen.setWidth(1.5)
        painter.setPen(pen)
        painter.drawPath(curve)

        # -- DRAW POINT ON CURVE
        pen.setWidth(ptSize)
        painter.setPen(pen)
        painter.drawPoints(self.points)

        # -- DRAW HOVERED POINT
        if not self.hoverPoly == -1:

            pen.setColor(QtGui.QColor(255, 255, 255, 255))
            pen.setWidth(ptSize * 1.3)
            painter.setPen(pen)
            painter.drawPoint(self.points[self.hoverIndex])

            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawEllipse(self.points[self.hoverIndex], ptSize, ptSize)

    def digit(self, inputValue):
        """Description
        """
        rounded = round(inputValue, 1)
        return '{: ,}'.format(rounded).replace(',', ' ')

    def noDecimal(self, inputValue):
        return '{: ,}'.format(int(inputValue)).replace(',', ' ')

    def insertKey(self, time):
        """Description

        :Param  time(None): desc.
        :Return (None): desc.
        """
        cmds.setKeyframe(self.attribute, time=time, insert=True)

# -- Vtx python version 2
