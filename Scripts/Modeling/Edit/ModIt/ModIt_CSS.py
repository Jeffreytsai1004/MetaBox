#!/usr/bin/env python
# -*- coding: utf-8 -*-

##GLOBAL VARIABLEs
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui


##THEME_SET
USERAPPDIR = cmds.internalVar(userAppDir=True)
VERSION = cmds.about(v=True)
IconPath = os.path.join(USERAPPDIR, VERSION+'/scripts/ModIt/Icons/Theme_Classic/')


# Attention l'ordre est important notamen pour le QPushButton!!
##COLORS SCHEME
### GREY BG : #272727
### GREY Line : #444444
### GREEN : #b3b523
### YELLOW : #c49e19

### GREY MODIT COLOR
  #TABS BG : 292929
  #SECTION BG : 303030
  #BLUE : 29b1ea


## Add                 border: 0px;    to Background to remove border lines
##GLOBAL VARIABLEs
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui



ModIt_CSS = """

                        *{
                background: #303030;
                border: 0px;
                }



                QTabWidget::pane {                    /* Ligne Ar a la suite des tabs */
                    background: #202020;
                }

                QToolTip {
                    background-color : #202020;
                    color : #b7b7b7;
                    font-size: 16px;
                }



                QPushButton{ background-color: #303030; 
                }
                QPushButton:hover{ background-color: #606060; 
                                   border-radius: 3px;
                }
                QPushButton:pressed{ background-color: #282828; 
                }





                QPushButton[objectName^="TABS_BTN_OFF"]{ 
                                background-color :#292929;
                                border-top: 1px solid gray;
                                border-right: 1px solid gray;
                                border-left: 1px solid gray;
                                border-color: #222222; 
                }
                QPushButton[objectName^="TABS_BTN_OFF"]:hover{ 
                                background-color : #181818;
                                border-top: 2px solid gray;
                                border-color: #303030; 
                }
                QPushButton[objectName^="TABS_BTN_OFF"]:pressed{ 
                                background-color : #65BEF1;
                }






                QPushButton[objectName^="StoreSet"]{ 
                                background-color :#292929;
                                border: 1px solid gray;
                                border-color: #222222; 
                }
                QPushButton[objectName^="StoreSet"]:hover{ 
                                background-color :#303030;
                                border: 1px solid gray;
                                border-color: #424242; 
                }
                QPushButton[objectName^="StoreSet"]:pressed{ 
                                background-color : #65BEF1;
                }




                QPushButton[objectName^="AssetIt"]{ 
                                background-color :#222222;
                                border: 1px solid gray;
                                border-color: #222222;
                                color : #65BEF1
                }
                QPushButton[objectName^="AssetIt"]:hover{ 
                                background-color :#303030;
                                border: 1px solid gray;
                                border-color: #424242; 
                }
                QPushButton[objectName^="AssetIt"]:pressed{ 
                                background-color : #65BEF1;
                }





                QPushButton[objectName^="Separator"]{ 
                             background-color: #464646; 
                }



                QComboBox {
                    border: 1px solid gray;
                    border-radius: 4px; 
                    background: #2f2f2f;
                    border-color: #202020;
                    padding: 1px 2px 1px 3px;
                    color: #C2C2C2;
                    font-size: 14px;
                }
                
                QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;

                    border-top-right-radius: 3px;
                    border-bottom-right-radius: 3px;
                }
                
                QComboBox::down-arrow {
                     image: url(""" + IconPath + """Arrow_Down.png);
                     
                }


                QSlider {
                    min-height: 14;
                    max-height: 14;
                }


                QSlider::handle:horizontal {
                background: #65BEF1;
                width: 6px;
                margin-top: -6px;
                margin-bottom: -6px;
                border-radius: 2px;
                min-height: 12;
                max-height: 12;
                }


                QSlider::groove:horizontal {
                background: #242424;
                height: 2px;
                }




                QDoubleSpinBox{
                    background-color: #2f2f2f;
                    border: 1px solid gray;
                    border-color: #202020;
                    border-radius: 4px; 
                    font-size: 14px;

                }
                
                QDoubleSpinBox::focus{
                        border: 1px solid #b3b523;
                        border-color: #65BEF1; 
                        border-radius: 2px;             
                }
                     
                QLineEdit{ 
                   background-color: #262626; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #444444;

                }


                QLineEdit:hover{
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #999999;

                }


                QLineEdit:focus{
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #65BEF1;

                }


  
                QCheckBox::indicator:unchecked {
                        border: 1px solid #385E74;
                }
                QCheckBox::indicator:checked {image: url(""" + IconPath + """Apply.png);
                        border: 1px solid #385E74;
                }

                 



                """

AssetIt_CSS = """

                        *{
                background: #272727;
                border: 0px;
                }

                QMenu{ 
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 2px;
                   border-color: #385E74;
                }
           
                QMenu::item{
                    color: #909090;
                }                            
                
                
                QMenu::item:selected{
                    background-color: #262626;
                    color: #65BEF1;
                }                            
                
                  
                
                
                QLineEdit{ 
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #444444;

                }


                QLineEdit:hover{
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #999999;

                }


                QLineEdit:focus{
                   background-color: #222222; 
                   border: 1px solid gray;
                   border-radius: 3px;
                   border-color: #65BEF1;

                }




  
                QScrollBar::handle:vertical {
                        background: #2094D6;
                        border-radius: 3px;
                        
                }

  
                QScrollBar:vertical {
                        width: 12px;

                      }
  
  




                QListWidget{
                    background: #202020;          /* Background de la fenetre Widgets */
                    border: 2px solid #202020;
                    border-radius: 3px;
                    padding: 0px;
                }


                QListView::item:hover{
                    border : 2px solid black;
                    background : green;
                }





                /*QWidget:hover{
                    background: #808080;          
                }*/

                
                
     



                QTabWidget::pane {                    /* Ligne Ar a la suite des tabs */
                    background: #202020;

                }



                QTabBar::tab {
                    background: #282828;
                    border: 1px solid #202020;
                    border-radius: 3px;
                    min-width: 12ex;/* taille du Tab Largeur */
                    padding: 5px;/* taille du Tab Hauteur */
                    color: #909090

                }

                QTabBar::tab:hover {
                    background: #454545;
                    border: 1px solid #202020;
                    border-top: 1px solid #E3E3E3;
                    border-radius: 3px;
                    color: #E3E3E3               
                }


                QTabBar::tab:selected {
                    background: #292929;
                    border: 1px solid #202020;
                    border-top: 1px solid #419ED3;
                    border-radius: 3px;
                    color: #419ED3               
                }







                QSlider {
                    min-height: 12;
                    max-height: 12;
                }


                QSlider::handle:horizontal {
                background: #65BEF1;
                width: 22px;
                margin-top: -4px;
                margin-bottom: -4px;
                border-radius: 2px;
                min-height: 10;
                max-height: 10;
                }



                QSlider::groove:horizontal {
                background: #404040;
                height: 1px;
        
                }





                QToolTip {
                    background-color : #202020;
                    color : #65BEF1;
                    font-size: 16px;
                }



                QPushButton{ background-color: #282828; 

                }
                
                
                QPushButton:hover{ background-color: #404040; 
                                   border-radius: 3px;
                }

                QPushButton:pressed{ background-color: #222222; 

                }


                QPushButton[objectName^="Items"]{ 
                             background-color: #232323; 
                             border: 1px solid gray; 
                             border-color: #202020; 
                }
                
                QPushButton[objectName^="Items"]:hover{ 
                            background-color: #303030;
                            border: 2px solid gray; 
                            border-color: #505050; 
                }

           
                QToolButton{ 
                                color : #404040; 
                }

                QToolButton:hover{ 
                                color : #606060; 
                }


           
           
           
           

                QPushButton[objectName^="AddAsset"]{ 
                                background-color : #222222;
                                color : #808080; 
                }

                QPushButton[objectName^="AddAsset"]:hover{ 
                                background-color : #252525;
                               border: 1px solid gray; 
                                 border-color: #65BEF1; 
                                color : #65BEF1; 
                }

                QPushButton[objectName^="AddAsset"]:pressed{ 
                                background-color : #141414;
                                border: 1px solid gray; 
                                 border-color: #222222; 
                                color : #404040; 
                }





                QPushButton[objectName^="SaveSetting"]:hover{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #FFFFFF;
                                border-radius: 2px; 
                                color : #FFFFFF; 
                }

                QPushButton[objectName^="SaveSetting"]{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #65BEF1; 
                                border-radius: 2px; 
                                color : #65BEF1; 
                }

                QPushButton[objectName^="SaveSetting"]:pressed{ 
                                background-color : #202020;
                                border: 1px solid gray; 
                                border-color: #606060; 
                                border-radius: 2px; 
                                color : #606060; 
                }







                QPushButton[objectName^="CleanFav"]{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #b7842a; 
                                color : #b7842a; 
                }

                QPushButton[objectName^="CleanFav"]:hover{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #FF9B22; 
                                color : #FF9B22; 
                }

                QPushButton[objectName^="CleanFav"]:pressed{ 
                                background-color : #141414;
                                border: 1px solid gray; 
                                 border-color: #222222; 
                                color : #404040; 
                }




                QPushButton[objectName^="Separator"]{ 
                             background-color: #272727; 
                }


                     
                QLineEdit[objectName^="UserLibPathField"]{ 
                        background-color: #222222;
                        color: #65BEF1;
                }
                



                QLabel[objectName^="AssetName"]{
                        background-color : #1E1E1E; 
                        color : #65BEF1;  
                        border: 1px solid gray; 
                        border-color: #353535; 
                        border-radius: 2px; 
                }

                QLabel[objectName^="AssetTitle"]{
                        color : #65BEF1;  
                }


                QLabel[objectName^="ThumbAsset"]{
                        background-color : #232323; 
                        color : #65BEF1;  
                        border: 1px solid gray; 
                        border-color: #383838; 
                        border-radius: 2px; 
                }



                QDoubleSpinBox{
                    font-size:17px;
                    background-color: #242424;
                    width: 60px;
                }
                
                QDoubleSpinBox::focus{
                        border: 1px solid #b3b523;
                        font-size:17px;
                        background-color: #1e1e1e;
                        border-color: #65BEF1; 
                        border-radius: 2px; 
                        width: 60px;             
                }
                       




                QComboBox {
                    border: 2px solid gray;
                    border-radius: 4px; 
                    background: #232323;
                    border-color: #232323;
                    padding: 1px 2px 1px 3px;
                    min-width: 6em;
                    color: #C2C2C2;
                }
                
                QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                 
                    border-top-right-radius: 3px;
                    border-bottom-right-radius: 3px;
                }
                
                QComboBox::down-arrow {
                     image: url(""" + IconPath + """ComboBox_Arrow.png);
                     
                }






                QCheckBox[objectName^="ClayRender"]::indicator:Unchecked:hover{image: url(""" + IconPath + """ClayRender_ON.png);
                        border: 0px solid #444444;
                }     
                QCheckBox[objectName^="ClayRender"]::indicator:checked {image: url(""" + IconPath + """ClayRender_ON.png);
                        border: 0px solid #444444;
                }
                QCheckBox[objectName^="ClayRender"]::indicator:Unchecked {image: url(""" + IconPath + """ClayRender_OFF.png);
                        border: 0px solid #444444;
                }
                QCheckBox[objectName^="ClayRender"]::indicator:checked:hover{image: url(""" + IconPath + """ClayRender_OVER.png);
                        border: 0px solid #444444;
                }
                 
                
                
                QGroupBox {
                    border: 1px solid gray;
                    border-color: #444444;
                    border-radius: 4px; 
                    color : #65BEF1;
                    margin-top: 18px;
                    font-size: 16px;

                }
                
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top left;
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10x;
                    padding: 1px 12px;

                }   


                QRadioButton::indicator::unchecked{ 
                border: 1px solid; 
                border-color: #444444;
                border-radius: 5px;
                background-color: #444444; 
                width: 9px; 
                height: 9px; 
                }
                
                QRadioButton::indicator:unchecked:hover
                {
                border: 1px solid; 
                border-color: #888888;
                border-radius: 5px;
                background-color: #888888; 
                width: 9px; 
                height: 9px; 
                }
                                
                
                
                QRadioButton::indicator::checked{ 
                border: 1px solid; 
                border-color: #65BEF1;
                border-radius: 5px;
                background-color: #65BEF1; 
                width: 9px; 
                height: 9px; 
                }
                
                
     
                
                
                

                """

Maya_CSS = """

                        *{

                }

                QPushButton{ 
                    border: 0px;

                }
                
                
                QPushButton:hover{ background-color: #656565; 

                }

                QPushButton:pressed{ background-color: #303030; 

                }



                """

