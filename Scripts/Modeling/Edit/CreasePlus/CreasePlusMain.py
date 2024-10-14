#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
_____ _____  ______           _____ ______     
/ ____|  __ \|  ____|   /\    / ____|  ____|_   
| |    | |__) | |__     /  \  | (___ | |__ _| |_ 
| |    |  _  /|  __|   / /\ \  \___ \|  __|_   _|
| |____| | \ \| |____ / ____ \ ____) | |____|_|  
\_____|_|  \_\______/_/    \_\_____/|______|    

"""

from functools import partial
import math

import os

crease_plus_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
print(crease_plus_dir)
try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    def whatpyside():
        return 2
    
except ImportError:
    try:
        from PySide.QtGui import *
        from PySide.QtCore import *
        def whatpyside():
            return 1   
    except ImportError:
        raise Exception("Couldn't import the PySide module.")
    
import importlib

# from shiboken2 import wrapInstance

# import maya.OpenMayaUI as omui
import maya.api.OpenMaya as om
import maya.cmds as cmds

from . import CreasePlusCore
crepcore = CreasePlusCore

# TODO remove reloads
# crepcore = importlib.reload(crepcore)

maya_useNewAPI = True


def cPgetScreenSz():
    rec = QApplication.desktop().screenGeometry()
    w = rec.width()
    h = rec.height()
    return (w, h)

global_cPscreensize = cPgetScreenSz()
def cPscreenSize():
    global global_cPscreensize
    return global_cPscreensize

def cPsizeRatio(w=None,h=None):
    rw = None
    rh = None
    if w != None :
        rw = float(w) / 1600
    if h != None :
        rh=float(h) / 900
    
    if rw != None and rh != None:
        return (rw,rh)
    elif rw != None:
        return (rw)
    elif rh != None:
        return (rh)
        

def cPmayaMainWindow():
    # mayaPtr = omui.MQtUtil.mainWindow()
    # mayaWindow = wrapInstance(int(mayaPtr), QWidget)
    # return mayaWindow
    try:
        mainWindow = QApplication.activeWindow()
        while True:
            lastWin = mainWindow.parent()
            if lastWin:
                mainWindow = lastWin
            else:
                break
        return mainWindow
    except:
        pass


# def cPmayaScriptDir():
#     return crease_plus_dir

def cPiconDir():
    icon_dir = crease_plus_dir + '/Icons/'
    return icon_dir

# global_maya_script_dir = cmds.internalVar(usd=True)
# global_icons_dir = global_maya_script_dir + 'Icons/'


def icoStr(iconame):
    # global global_icons_dir
    # return global_icons_dir + 'crep_' + iconame + '_ico.png'
    return cPiconDir() + 'crep_' + iconame + '_ico.png'


global_creasePlusMainUi = 'creasePlusMainUi'

global_cPsideshapestyle1 = '''
QWidget {
border: 0px solid #2e3234;
background: #db9456;
font-size: 0px;
border-radius: 0px;
color: #ffffff;
}
'''

global_cPsideshapestyle2 = '''
QWidget {
border: 0px solid #2e3234;
background: #d5703f;
font-size: 0px;
border-radius: 0px;
color: #ffffff;
}
'''

global_cPsideshapestyle3 = '''
QWidget {
border: 0px solid #2e3234;
background: #5ebae9;
font-size: 0px;
border-radius: 0px;
color: #ffffff;
}
'''

global_defInfodic = {
    'toolName': 'SomeTool',
    'toolDesc': 'tool description',
    'toolHelp': 'tool help'
}

class CreasePlusMainPage(QWidget):
    def __init__(self):
        super(CreasePlusMainPage, self).__init__()
        self.mainLay = QVBoxLayout()
        self.setLayout(self.mainLay)
        self.layout().setContentsMargins(2, 2, 2, 2)


class CreasePlusInfopop(QDialog):
    def __init__(self, parent=None):
        super(CreasePlusInfopop, self).__init__(parent)

        self.setStyleSheet(''' 
QWidget {
border: 2px solid #66696c;
background: #202122;
border-radius: 4px;
color: #ffffff;
}
''')

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup
                            | Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowOpacity(1)

        self.mainLay = QVBoxLayout()
        self.setLayout(self.mainLay)
        self.mainLay.setSpacing(1)
        self.mainLay.setContentsMargins(8, 8, 8, 8)

        self.titleico = QLabel()
        self.titleico.setStyleSheet('''
QWidget {
border: 0px solid #2e3234;
background: transparent;
font-size: 14px;
border-radius: 0px;
color: #ffffff;
}''')
        self.mainLay.addWidget(self.titleico)

        self.description = QLabel()
        self.description.setAlignment(Qt.AlignLeft)
        self.description.setStyleSheet('''
QWidget {
border: 0px solid #2e3234;
background: #454545;
font-size: 12px;
border-radius: 4px;
color: #ffffff;
}
''')
        self.mainLay.addWidget(self.description)

    def resizeEvent(self, event):
        super(CreasePlusInfopop, self).resizeEvent(event)

        radius = 5.0
        painterpath = QPainterPath()
        painterpath.addRoundedRect(QRectF(self.rect()), radius, radius)
        maskedRegion = QRegion(painterpath.toFillPolygon().toPolygon())
        self.setMask(maskedRegion)


class CreasePlusBtn(QWidget):

    pressed = Signal()
    global global_defInfodic

    def __init__(
            self,
            pmap=QPixmap(),
            lbl='',
            infobubble=None,
            infodic=global_defInfodic,
            parent=None,
    ):

        super(CreasePlusBtn, self).__init__(parent)

        self.setStyleSheet('''
                           QWidget {border: 0px solid #ffffff;background: #444444;border-radius: 0px;color: #ffffff;
                           }\nQWidget :hover {border: 0px solid #ffffff;background: #5e7876;border-radius: 3px;color: #ffffff;
                           }''')

        self.infoBubble = infobubble
        self.infodic = infodic

        self.mainLay = QVBoxLayout()
        self.setLayout(self.mainLay)
        self.mainLay.setSpacing(0)
        self.mainLay.setContentsMargins(2, 2, 2, 2)

        self.btn = QPushButton()
        self.btn.setStyleSheet('''
                               QWidget {border: 0px solid #ffffff;background: transparent;border-radius: 0px;color: #ffffff;
                               }''')
        
        self.btn.setIcon(pmap)
        self.btn.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.MinimumExpanding)
        self.mainLay.addWidget(self.btn)

    def setPixmap(self, pmap):
        self.btn.setIcon(pmap)

    def setPixmapSize(self, sz):
        self.btn.setIconSize(sz)

    def setInfoDic(self, infodic):
        self.infodic = infodic

        # self.btnLabel.setText(self.infodic["toolName"])

    def mousePressEvent(self, event):
        super(CreasePlusBtn, self).mousePressEvent(event)
        self.pressed.emit()

    def pressedConnect(self, func):
        self.btn.pressed.connect(func)

        # self.pressed.connect(func)

    def enterEvent(self, event):
        super(CreasePlusBtn, self).enterEvent(event)
        if self.infoBubble:
            self.infoBubble.setWindowOpacity(1)

            self.infoBubble.titleico.setText(self.infodic['toolName'])
            self.infoBubble.description.setText(self.infodic['toolDesc'])

    def leaveEvent(self, event):
        super(CreasePlusBtn, self).leaveEvent(event)
        if self.infoBubble:
            self.infoBubble.setWindowOpacity(0)

    def paintEvent(self, event):
        if not isinstance(event, QCloseEvent):
            
            super(CreasePlusBtn, self).paintEvent(event)

            painter = QPainter(self)

            option = QStyleOption()
            if whatpyside() == 1:
                option.initFrom(self)
            else:
                option.init(self)
            style = self.style()
            style.drawPrimitive(QStyle.PE_Widget, option, painter, self)


class CreasePlusSideShape(QWidget):

    pressed = Signal()

    def __init__(self, parent=None):

        super(CreasePlusSideShape, self).__init__(parent)
        self.maskShape = QPixmap()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup
                            | Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowOpacity(1)
        global global_cPsideshapestyle1
        self.setStyleSheet(global_cPsideshapestyle1)

        self.mainLay = QVBoxLayout()
        self.setLayout(self.mainLay)

        self.resize(32, 32)

    def setMaskShape(self, maskshape):
        self.maskShape = maskshape

    def resizeEvent(self, event):
        super(CreasePlusSideShape, self).resizeEvent(event)

        self.resize(self.maskShape.size())
        self.setMask(self.maskShape.mask())

    def mousePressEvent(self, event):
        super(CreasePlusSideShape, self).mousePressEvent(event)
        self.pressed.emit()

def creaseplusclosethefucknwinbefoh(clientobj = None):
    global global_creasePlusMainUi
    if cmds.window(global_creasePlusMainUi,ex=True):
        # print("hey here!")
        cmds.deleteUI(global_creasePlusMainUi, wnd=True)


class CreasePlusMain(QWidget):

    gripsz = cPsizeRatio(w=10) * cPscreenSize()[0]
    gripszMarg = (2, 2)

    numPages = 3

    def __init__(self, parent=None):

        super(CreasePlusMain, self).__init__(parent)

        self.noOpacity = False
        self.origw = 35
        self.origh = 370
        self.hostApp = parent
        self.countDown = 50
        global global_creasePlusMainUi
        self.setObjectName(global_creasePlusMainUi)
        
        self.setStyleSheet('''
                           QWidget {border: 0px solid #ffffff;background: #444444;border-radius: 0px;color: #ffffff;
                           }''')

        self.pageIndex = 0
        self.pages = [
            CreasePlusMainPage() for i in range(CreasePlusMain.numPages)
        ]
        self.pageBtns = {}
        self.oldPos = QPoint()
        self.resizing = False
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        # register callbacks
        self.mayaCallbacks = []
        cbid = om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeNew, creaseplusclosethefucknwinbefoh)
        self.mayaCallbacks.append(cbid)
        cbid = om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeOpen, creaseplusclosethefucknwinbefoh)
        self.mayaCallbacks.append(cbid)
        cbid = om.MSceneMessage.addCallback(om.MSceneMessage.kMayaExiting, creaseplusclosethefucknwinbefoh)
        self.mayaCallbacks.append(cbid)
        
        # 
        closeAction = QAction(
            'Close', self, shortcut='Alt+F4', triggered=self.close)
        self.addAction(closeAction)

        self.setWindowTitle('CreasePlus')

        self.mainLay = QGridLayout()
        self.setLayout(self.mainLay)

        self.mainLay.setContentsMargins(2, 16, 2, 16)
        self.mainLay.setVerticalSpacing(4)
        self.menuBar = QMenuBar()
        self.menuBar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.mainLay.addWidget(self.menuBar, 0, 0)

        self.spaceitm1 = QSpacerItem(0, cPsizeRatio(h=20) * cPscreenSize()[1], QSizePolicy.Ignored,
                                     QSizePolicy.MinimumExpanding)
        self.mainLay.addItem(self.spaceitm1, 1, 0)

        self.doMenus()

        self.hoverDelay = 0
        self.infoBubble = CreasePlusInfopop(parent=self)
        self.nextWid = CreasePlusSideShape(parent=self)
        self.nextWid.pressed.connect(self.onClick_next)


        nextWidSize = cPsizeRatio(w=10) * cPscreenSize()[0]
        self.nextWid.setMaskShape(
            QPixmap(icoStr('next')).scaled(nextWidSize, nextWidSize, Qt.IgnoreAspectRatio,
                                           Qt.SmoothTransformation))

        self.timer = QTimer()
        self.timer.timeout.connect(self.opacityModifier)
        self.timer.start(self.countDown)

        self.doFirstPage()
        self.doSecondPage()
        self.doThirdPage()

        self.stackedWidget = QStackedWidget()
        for page in self.pages:
            self.stackedWidget.addWidget(page)
        self.mainLay.addWidget(self.stackedWidget, 2, 0)

        self.infoBubble.show() 
        self.infoBubble.setWindowOpacity(0)
        self.nextWid.show()
        
        self.mainRecRatio = (cPsizeRatio(w=self.origw), cPsizeRatio(h=self.origh))
        w = self.mainRecRatio[0] * cPscreenSize()[0]
        h = self.mainRecRatio[1] * cPscreenSize()[1]
        self.setMaximumWidth(w)
        self.setMinimumWidth(w)

        # print((self.maximumWidth() )

        self.resize(w, h)


    def doMenus(self):

        deleteCpAttrsAc = QAction(
            'Clean Attributes', self, triggered=crepcore.cPcleanAttrs)
        
        
        cleanHBevelLiveAc = QAction(
            'Clean HBevel Live', self, triggered=crepcore.creasePlusBakeHBL)
        
        toggleLastAc = QAction(
            'Toggle Last', self, triggered=crepcore.creasePlusLastCtx)
        transferHBevelAc = QAction(
            'Transfer HBevel',
            self,
            triggered=crepcore.creasePlusTransferHBevel)
        invkCreaseSetAc = QAction(
            'Crease Set Editor', self, triggered=crepcore.cPshowCreaseEd)

        self.miscMenu = QMenu('Miscs', self)
        self.miscMenu.setIcon(QPixmap(icoStr('menu')))
        self.miscMenu.addAction(cleanHBevelLiveAc)
        self.miscMenu.addAction(toggleLastAc)
        self.miscMenu.addAction(transferHBevelAc)
        self.miscMenu.addAction(deleteCpAttrsAc)
        self.miscMenu.addAction(invkCreaseSetAc)

        self.menuBar.addMenu(self.miscMenu)

    def opacityOverride(self, o):
        if self.noOpacity == False:
            self.setWindowOpacity(o)
        else:
            self.setWindowOpacity(1)
    def opacityModifier(self):

        # curpage = self.pages[self.stackedWidget.currentIndex()]

        try:
            if self.underMouse():
                self.timer.stop()
            else:

                if not self.timer.isActive():
                    self.timer.start()
                if self.hoverDelay >= self.countDown:
                    self.hoverDelay = 0
                    self.opacityOverride(0.1)
                    self.timer.stop()
                else:
                    self.hoverDelay += 1
                    opacity = 1.0 - float(self.hoverDelay) / float(
                        self.countDown)
                    self.opacityOverride(max(0.1, opacity))
        except:

            try:
                self.timer.stop()
            except:
                pass

    def reposNextWid(self):

        # pass

        spaceitmLeft = self.spaceitm1.geometry().topLeft()
        spaceitmHeight = abs(
            self.spaceitm1.geometry().bottomLeft().y() - spaceitmLeft.y())
        self.nextWid.move(
            self.mapToGlobal(self.rect().topRight()).x(),
            self.mapToGlobal(spaceitmLeft + QPoint(
                0, spaceitmHeight / 2 - self.nextWid.height() * 0.25)).y())

    
    def doFirstPage(self):

        pageLay = self.pages[0].layout()
        pageLay.setSpacing(0)

        numbtns = 12

        listBtns = []
        
        icosz = cPsizeRatio(w=20) * cPscreenSize()[0]
        for i in range(numbtns):
            listBtns.append(CreasePlusBtn(infobubble=self.infoBubble))
            listBtns[i].setPixmapSize(QSize(icosz, icosz))

        i = 0
        
        listBtns[i].setPixmap(QPixmap(icoStr('bool')))
        listBtns[i].setInfoDic({
            'toolName': 'Bool Op',
            'toolDesc': 'Performs non destructive boolean.'
        })
        listBtns[i].pressedConnect(partial(crepcore.creasePlusBool, False))
        i += 1


        listBtns[i].setPixmap(QPixmap(icoStr('panelbool')))
        listBtns[i].setInfoDic({
            'toolName': 'Panel Bool',
            'toolDesc': 'Performs panel bool operation.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusPanelBool)
        i += 1
        


        # 

        listBtns[i].setPixmap(QPixmap(icoStr('smoothangle')))
        listBtns[i].setInfoDic({
            'toolName':
            'Smooth 30',
            'toolDesc':
            'Fixes and Smooths normals by a 30 degree angle.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusSmooth30)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('displayhe')))
        listBtns[i].setInfoDic({
            'toolName': 'Display HardEdges',
            'toolDesc': 'Toggles display of hard edges.'
        })
        listBtns[i].pressedConnect(
            partial(crepcore.creasePlusDisplayHardEdges, 0))
        i += 1
        
        listBtns[i].setPixmap(QPixmap(icoStr('bevel')))
        listBtns[i].setInfoDic({
            'toolName':
            'HBevel',
            'toolDesc':
            'Bevels hard edges , based on selection.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusHBevel)
        i += 1
        #
        

        listBtns[i].setPixmap(QPixmap(icoStr('bevellive')))
        listBtns[i].setInfoDic({
            'toolName':
            'HBevel Live',
            'toolDesc':
            'HBevel as a node, with a cage mesh (interactive).'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusHBevelLive)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('shapeshifter')))
        listBtns[i].setInfoDic({
            'toolName':
            'Shape Shifter',
            'toolDesc':
            'Calls ShapeShifter script (3rd party).'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusShapeShifter)
        i += 1

        
        

        listBtns[i].setPixmap(QPixmap(icoStr('meshslicer')))
        listBtns[i].setInfoDic({
            'toolName':
            'Mesh Slicer',
            'toolDesc':
            'Slices the mesh in x,y,z direction based on camera , with a curve.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCurveSlice)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('hardedge')))
        listBtns[i].setInfoDic({
            'toolName': 'Sel HardEdges',
            'toolDesc': 'Selects hard edges.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusSelHardEdges)
        i += 1
        
        

        listBtns[i].setPixmap(QPixmap(icoStr('mirror')))
        listBtns[i].setInfoDic({
            'toolName': 'Mirror',
            'toolDesc': 'Mirrors selected meshes.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusMirror)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('uv')))
        listBtns[i].setInfoDic({
            'toolName': 'Make UV',
            'toolDesc': "Makes UV's based on hard edges."
        })
        listBtns[i].pressedConnect(crepcore.creasePlusMakeUv)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('zbrush')))
        listBtns[i].setInfoDic({
            'toolName':
            'Goz',
            'toolDesc':
            'Exports selection in Zbrush without ngons.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusGoz)
        i += 1

        for btn in listBtns:
            pageLay.addWidget(btn)

        self.pageBtns['page1'] = listBtns

    def doSecondPage(self):
        pageLay = self.pages[1].layout()
        pageLay.setSpacing(0)

        numbtns = 8

        listBtns = []

        icosz = cPsizeRatio(w=20) * cPscreenSize()[0]
        for i in range(numbtns):
            listBtns.append(CreasePlusBtn(infobubble=self.infoBubble))
            listBtns[i].setPixmapSize(QSize(icosz, icosz))

        i = 0
        listBtns[i].setPixmap(QPixmap(icoStr('crease')))
        listBtns[i].setInfoDic({
            'toolName': 'Crease1',
            'toolDesc': 'Applies first creasing preset.'
        })
        listBtns[i].pressedConnect(partial(crepcore.creasePlusCreasePreset, 1))
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('crease')))
        listBtns[i].setInfoDic({
            'toolName': 'Crease2',
            'toolDesc': 'Applies second creasing preset.'
        })
        listBtns[i].pressedConnect(partial(crepcore.creasePlusCreasePreset, 2))
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('crease')))
        listBtns[i].setInfoDic({
            'toolName': 'Crease3',
            'toolDesc': 'Applies third creasing preset.'
        })
        listBtns[i].pressedConnect(partial(crepcore.creasePlusCreasePreset, 3))
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('weighttool')))
        listBtns[i].setInfoDic({
            'toolName':
            'Creasing Tool',
            'toolDesc':
            'Invokes the interactive creasing tool.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusWeigthTool)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('displayhe')))
        listBtns[i].setInfoDic({
            'toolName': 'NoCrease',
            'toolDesc': 'Remove creasing on selection.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusNocrease)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('hardedge')))
        listBtns[i].setInfoDic({
            'toolName':
            'Smooth SG',
            'toolDesc':
            'Subdivides based on smoothing groups (retains hard edges shape).'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusSmoothGroupsSubD)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('physcrease')))
        listBtns[i].setInfoDic({
            'toolName':
            'Physical Crease',
            'toolDesc':
            'Adds edge loops around selection or hard edges.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusPhysicalCrease)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('subd')))
        listBtns[i].setInfoDic({
            'toolName': 'Smooth',
            'toolDesc': 'Invokes subdivision smooth preset.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusSubDpreset)
        i += 1

        for btn in listBtns:
            pageLay.addWidget(btn)

        self.pageBtns['page2'] = listBtns

    def doThirdPage(self):
        pageLay = self.pages[2].layout()
        pageLay.setSpacing(0)

        numbtns = 7

        listBtns = []
   
        icosz = cPsizeRatio(w=20) * cPscreenSize()[0]
        for i in range(numbtns):
            listBtns.append(CreasePlusBtn(infobubble=self.infoBubble))
            listBtns[i].setPixmapSize(QSize(icosz, icosz))
        
        i = 0
        listBtns[i].setPixmap(QPixmap(icoStr('curvedraw')))
        listBtns[i].setInfoDic({
            'toolName':
            'Draw Curve',
            'toolDesc':
            'Enter linear curve drawing context.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusDrawCurve)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curvepoly')))
        listBtns[i].setInfoDic({
            'toolName': 'Curve To Polygon',
            'toolDesc': 'Makes polygon out of curve.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCurveToPolyCmd)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curveclose')))
        listBtns[i].setInfoDic({
            'toolName': 'Close Curve',
            'toolDesc': 'Closes Curve(s).'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCloseCurve)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curvebevel')))
        listBtns[i].setInfoDic({
            'toolName': 'Bevel Curve',
            'toolDesc': 'Bevels Curve Cv.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCurveBevelCmd)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curveint')))
        listBtns[i].setInfoDic({
            'toolName': 'Curve Cuts',
            'toolDesc': 'Cuts curve with selected curves.'
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCurveIntersect)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curveattach')))
        listBtns[i].setInfoDic({
            'toolName':
            'Curve Attach',
            'toolDesc':
            "Attaches two curves at joining/close CV's."
        })
        listBtns[i].pressedConnect(crepcore.creasePlusAttachCurve)
        i += 1

        listBtns[i].setPixmap(QPixmap(icoStr('curvemult')))
        listBtns[i].setInfoDic({
            'toolName':
            'Curve Multiply',
            'toolDesc':
            "Rebuilds to double the number of CV's"
        })
        listBtns[i].pressedConnect(crepcore.creasePlusCurveDoubleCvs)
        i += 1

        for btn in listBtns:
            pageLay.addWidget(btn)

        self.pageBtns['page3'] = listBtns

    
    def onClick_leftSqr(self):
        self.setWindowOpacity(1)
        self.noOpacity = not self.noOpacity 
        
    def onClick_eye(self):
        # print("eye clicked")
        # cmds.select("pCube*", r=True)
        crepcore.creasePlusToggleBoolGhost()

    def onClick_next(self): 
        # print("next clicked")

        self.pageIndex = (self.pageIndex + 1) % CreasePlusMain.numPages
        
        global global_cPsideshapestyle1
        global global_cPsideshapestyle2
        global global_cPsideshapestyle3
        
        if self.pageIndex == 0 : 
            self.nextWid.setStyleSheet(global_cPsideshapestyle1)
        elif self.pageIndex == 1 : 
            self.nextWid.setStyleSheet(global_cPsideshapestyle2)
        elif self.pageIndex == 2 : 
            self.nextWid.setStyleSheet(global_cPsideshapestyle3)
            
        self.stackedWidget.setCurrentIndex(self.pageIndex)

    def mouseInEye(self, mousePos):

        icosz = cPsizeRatio(w=17) * cPscreenSize()[0]
        spaceitmLeft = self.spaceitm1.geometry().topLeft()
        spaceitmHeight = abs(
            self.spaceitm1.geometry().bottomLeft().y() - spaceitmLeft.y())
        minx = self.width() / 2 - icosz / 2
        miny = spaceitmLeft.y() + spaceitmHeight / 2 - icosz / 2
        return mousePos.x() > minx and mousePos.x(
        ) < minx + icosz and mousePos.y() > miny and mousePos.y(
        ) < miny + icosz * 0.75



    def mouseInLeftSqr(self, mousePos):
        return mousePos.x() < CreasePlusMain.gripsz + CreasePlusMain.gripszMarg[0] and mousePos.y(
        ) > self.height() - CreasePlusMain.gripsz - CreasePlusMain.gripszMarg[1]
    
    def mouseInGrip(self, mousePos):
        return mousePos.x() > self.width() - CreasePlusMain.gripsz - CreasePlusMain.gripszMarg[0] and mousePos.y(
        ) > self.height() - CreasePlusMain.gripsz - CreasePlusMain.gripszMarg[1]

    def mouseInCloseSqr(self, mousePos):
        return mousePos.x() > self.width() - CreasePlusMain.gripsz - CreasePlusMain.gripszMarg[0] and mousePos.y(
        ) < CreasePlusMain.gripsz + CreasePlusMain.gripszMarg[1]

    def mousePressEvent(self, event):
        super(CreasePlusMain, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.resizing = False
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            if self.mouseInEye(event.pos()):
                self.onClick_eye()
            elif self.mouseInGrip(event.pos()):
                self.oldPos = event.pos()
                self.resizing = True
            elif self.mouseInLeftSqr(event.pos()):
                self.onClick_leftSqr()
            elif self.mouseInCloseSqr(event.pos()):
                event.accept()
                self.close()
            event.accept()

    def enterEvent(self, event):
        super(CreasePlusMain, self).enterEvent(event)
        
        
        self.hoverDelay = 0

        # curpage = self.pages[self.stackedWidget.currentIndex()]

        self.setWindowOpacity(1)

        # if self.mouseInCloseSqr(QCursor.pos()):
        #     self.infoBubble.titleico.setText('dummy')
        #     self.infoBubble.description.setText('dummydesc')
        #     self.infoBubble.setWindowOpacity(1)

        # print("enter")

    def leaveEvent(self, event):
        super(CreasePlusMain, self).leaveEvent(event)
        self.infoBubble.setWindowOpacity(0)
        
        if self.timer:
            if not self.timer.isActive():

                # print("leave, restart timer...")

                self.timer.start(self.countDown)

    def mouseMoveEvent(self, event):
        super(CreasePlusMain, self).mouseMoveEvent(event)
        if event.buttons() == Qt.LeftButton:
            if self.resizing:
                delta = event.pos() - self.oldPos
                self.oldPos = event.pos()
                self.setMaximumWidth(16777215)
                self.resize(self.width() + delta.x(),
                            self.height() + delta.y())
                event.accept()
                self.updateGeometry()
            else:

                self.move(event.globalPos() - self.dragPosition)
                self.reposNextWid()
                event.accept()

    def resizeEvent(self, event):
        super(CreasePlusMain, self).resizeEvent(event)

        radius = 2.0
        painterpath = QPainterPath()
        painterpath.addRoundedRect(QRectF(self.rect()), radius, radius)
        maskedRegion = QRegion(painterpath.toFillPolygon().toPolygon())
        self.setMask(maskedRegion)

    def paintEvent(self, event):

        super(CreasePlusMain, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(0.3)
        
        
        painter.drawRoundedRect(
            self.width() - CreasePlusMain.gripsz -
            CreasePlusMain.gripszMarg[0],
            self.height() - CreasePlusMain.gripsz -
            CreasePlusMain.gripszMarg[1],
            CreasePlusMain.gripsz,
            CreasePlusMain.gripsz,
            1,
            1)
        
        painter.setPen(Qt.NoPen)
        painter.setOpacity(1)
        painter.setBrush(QColor(32+7,32+7,32+7))

        painter.drawRoundedRect(
            CreasePlusMain.gripszMarg[0],
            self.height() - CreasePlusMain.gripsz - CreasePlusMain.gripszMarg[1],
            CreasePlusMain.gripsz,
            CreasePlusMain.gripsz, 3,3)


        painter.setOpacity(1)
        painter.setPen(Qt.NoPen)

        # nextico = QPixmap(icoStr("next"))
        # icosz = CreasePlusMain.gripsz
        # painter.drawPixmap(CreasePlusMain.gripszMarg[0], self.height()-icosz-CreasePlusMain.gripszMarg[1],
        # nextico.scaled(icosz, icosz, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

        closeico = QPixmap(icoStr('close'))
        icosz = CreasePlusMain.gripsz
        painter.drawPixmap(self.width() - icosz - CreasePlusMain.gripszMarg[0],
                           CreasePlusMain.gripszMarg[1],
                           closeico.scaled(icosz, icosz, Qt.IgnoreAspectRatio,
                                           Qt.SmoothTransformation))

        eyeico = QPixmap(icoStr('eye'))
        icosz = cPsizeRatio(w=17) * cPscreenSize()[0]
        
        try:
            self.spaceitm1
        except:
            start()
            return None
        spaceitmLeft = self.spaceitm1.geometry().topLeft()
        spaceitmHeight = abs(
            self.spaceitm1.geometry().bottomLeft().y() - spaceitmLeft.y())
        painter.drawPixmap(self.width() / 2 - icosz / 2,
                           spaceitmLeft.y() + spaceitmHeight / 2 - icosz / 2,
                           eyeico.scaled(icosz, icosz, Qt.IgnoreAspectRatio,
                                         Qt.SmoothTransformation))

        infbubx = self.mapToGlobal(self.rect().topRight()).x() + 4
        self.infoBubble.resize(0, 0)
        self.infoBubble.move(infbubx, QCursor.pos().y())
        
        self.reposNextWid()

    def closeEvent(self, event):
        super(CreasePlusMain, self).closeEvent(event)

        # print("CLOSEEVENT")
        try:
            self.mayaCallbacks
        except:
            pass
        else:
            for cb in self.mayaCallbacks:
                om.MMessage.removeCallback(cb)
        
        try:
            self.timer
        except:
            pass
        else:
            self.timer.stop()
            self.timer = None
        # self.infoBubble.close()
        # self.nextWid.close()

    def dummy(self):
        print(('dummy'))



def start():
    # self = CreasePlusMain(parent=cPmayaMainWindow())
    # self.show()
    creaseplusclosethefucknwinbefoh()
    
    mywin = CreasePlusMain(parent=cPmayaMainWindow())
    mywin.show()