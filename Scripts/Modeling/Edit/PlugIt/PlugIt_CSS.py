##GLOBAL VARIABLEs
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds as mc
import maya.mel as mel
import json
import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
#THEME_SET
USERAPPDIR = mc.internalVar(userAppDir=True)
VERSION = mc.about(v=True)
IconPath = os.path.join(USERAPPDIR, VERSION+'/scripts/PlugIt/Icons/Theme_Classic/')
### GREY BG : #272727
### GREY Line : #444444
### GREEN : #b3b523
### YELLOW : #c49e19
###BLUE
  #Cyan :      A2D5D8
  #Blue Soft : 65BEF1

PlugIt_CSS = """
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
                   background-color: #242424; 
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







                QScrollBar:vertical {
                     background: #1d1d1d;
                     width: 12px;
                }

                  
  
                QScrollBar::handle:vertical {
                        background: #363636;
                        border-radius: 2px;
                }



                 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                     background: #1d1d1d;
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
                        background: #292929;
                        border: 1px solid #202020;
                        border-radius: 2px;
                        border-color: #222222; 
                        min-width: 14ex;/* taille du Tab Largeur */
                        padding: 5px;/* taille du Tab Hauteur */
                        color: #5d5d5d
                }
                QTabBar::tab:hover {
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242;              
                }
                QTabBar::tab:selected {
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242; 
                        border-radius: 2px;
                        color: #a7a7a7;             
                }







                QPushButton[objectName^="StoreSet"]{ 
                        background-color :#323232;
                        border: 1px solid gray;
                        border-color: #222222; 
                        color: #5d5d5d;
                }
                QPushButton[objectName^="StoreSet"]:hover{ 
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242; 
                }
                QPushButton[objectName^="StoreSet"]:pressed{ 
                        background-color : #65BEF1;
                }
                QPushButton[objectName^="StoreSet"]:disabled{ 
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242; 
                        border-radius: 2px;
                        color: #a7a7a7;     
                }
            


                QPushButton[objectName^="MasterBtn"]{ 
                        background-color :#323232;
                        border: 1px solid gray;
                        border-color: #222222; 
                        color: #888888;
                }
                QPushButton[objectName^="MasterBtn"]:hover{ 
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242; 
                        color: #a4a4a4;
                }
                QPushButton[objectName^="MasterBtn"]:pressed{ 
                        background-color : #65BEF1;
                }
                QPushButton[objectName^="MasterBtn"]:disabled{ 
                        background-color :#303030;
                        border: 1px solid gray;
                        border-color: #424242; 
                        border-radius: 2px;
                        color: #a7a7a7;     
                }
            






























                QSlider {
                    min-height: 8;
                    max-height: 8;
                }


                QSlider::handle:horizontal {
                background: #65BEF1;
                width: 16;
                margin-top: -2px;
                margin-bottom: -2px;
                border-radius: 1px;
                min-height: 8;
                max-height: 8;
                }



                QSlider::groove:horizontal {
                background: #323232;
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
                             background-color: rgba(0,125,0,0);
                             border: 1px solid gray; 
                             border-color: #202020;
                             
                }
                QPushButton[objectName^="Items"]:hover{ 
                            background-color: #cbcbcb;
                            border: 2px solid gray; 
                            border-color: #cbcbcb;
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




                QPushButton[objectName^="CleanScene"]{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #f74803; 
                                color : #f74803; 
                }

                QPushButton[objectName^="CleanScene"]:hover{ 
                                background-color : #252525;
                                border: 1px solid gray; 
                                border-color: #ff7741; 
                                color : #ff7741; 
                }

                QPushButton[objectName^="CleanScene"]:pressed{ 
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
                    font-size:13px;
                    color : #909090; 
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
                    border: 1px solid gray;
                    border-radius: 3px; 
                    background: #242424;
                    border-color: #444444;
                    padding: 1px 2px 1px 3px;
                    min-width: 6px;
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

                QComboBox QListView::item{
                    background-color: #65BEF1;
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
                
                
                
                QCheckBox::indicator:unchecked {
                        border: 1px solid #3482af;
                }
                QCheckBox::indicator:checked {image: url(""" + IconPath + """Apply.png);
                        border: 1px solid #65BEF1;
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

