# -*- coding: latin-1 -*-
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import maya.cmds as mc
import os, json
import maya.mel as mel
import shutil

from . import PlugIt_UI
from . import PlugIt_Global
import importlib
importlib.reload(PlugIt_Global)





# Special cases for different Maya versions
try:
    from shiboken2 import wrapInstance
except ImportError:
    from shiboken import wrapInstance

from maya import OpenMayaUI as omui


ASSET_FAVOURITES_PATH = PlugIt_Global.ASSET_FAVOURITES_PATH
##PATH_SET
IconPath = PlugIt_Global.IconsPathThemeClassic
PreferencePath = PlugIt_Global.PreferencePath
TOOLS_PATH = PlugIt_Global.ToolsPath

Click_pref = json.load(open(PreferencePath + 'Pref_Click.json', "r"))
PREF_CLICK = (Click_pref['CLICK'])
if PREF_CLICK == 0:
    ClickIndex = 0
if PREF_CLICK == 1:
    ClickIndex = 1

FOLDER_PATH = ""

quickPlug_ScriptJob = 1111

class PlugIt_ListWidget(QListWidget):
    """           LE WIDGET QUI LISTE LES ASSETS         """
    def __init__(self, path, parent):
        super(PlugIt_ListWidget, self).__init__()
        self.parent=parent # just for updating favoutites
        self.path = path
        self.iconSize = 168
        self.buffer = 4
        self.buttons = []
        self.isFavOrResearch = False # bool: si la QListWidget sera utilisée pour les favoris ou la recherche
        self.setViewMode(QListWidget.IconMode)
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)
        self.setGridSize(QSize(self.iconSize + self.buffer, self.iconSize + self.buffer))
        self.setSortingEnabled(0)
        self.verticalScrollBar().setSingleStep(20)

        self.populate()


    def populate(self):
        try:    # tab normal            si self.path est un DOSSIER
            folderList = os.listdir(self.path)
            self.createsButtonsFromFileList(folderList= folderList)

        except: # favoris               si self.path est une LISTE DE FICHIERS
            folderList = self.path
            folderList = json.loads(folderList)
            self.isFavOrResearch = True
            self.createsButtonsFromFileList(folderList=folderList)

    def createsButtonsFromFileList(self, folderList):
        # crée les bouttons grâce a la liste des chemins de tous les assets a afficher
        icon_list = []

        for folder in folderList:
            if not self.isFavOrResearch:
                icon_list.append(folder+"/"+folder+".png")
            else:
                icon_list.append(folder)

        for icon in icon_list:
            item = QListWidgetItem()
            item.setFlags(Qt.ItemFlag.NoItemFlags)
            item.setSizeHint(QSize(400, 400))
            self.addItem(item)

            if self.isFavOrResearch:
                pixPath = icon

            else:
                pixPath = self.path + "/" + icon


            button = PlugIt_Button(pixPath, self, item)
            icon = QIcon(pixPath)
            button.setFlat(True)
            button.setIconSize(QSize(self.iconSize, self.iconSize))
            button.setObjectName("Items")
            #button.setContentsMargins(200, 200, 200, 200)
            button.setIcon(icon)
            self.buttons.append(button)

            self.setItemWidget(item, button)



class PlugIt_Button(QPushButton):
    """           ON VA AJOUTER CE BOUTTON POUR CHAQUE ASSET DANS LE PlugIt_ListWidget         """
    def __init__(self, itemPath, parent, itemWidget):
        super(PlugIt_Button, self).__init__()
        self.itemWidget = itemWidget
        self.itemPath = itemPath
        self.parent = parent
        self.assetName = self.itemPath[:-4] # json
        self.assetName = self.assetName[self.assetName.rfind("/") + 1:]
        self.setContextMenuPolicy(Qt.DefaultContextMenu)


    def enterEvent(self, event, action=None):
        pass
        # fonction appelée quand la souris hovers le boutton
        #self.parent.parent.AssetName.setText(self.assetName)

    def leaveEvent(self, event):
        # fonction appelée quand la souris sort du boutton
        #print ("leave")
        pass


    def mousePressEvent(self, QMouseEvent):
        # fonction appelée quand on fait un clic souris (droit ou gauche)

        # si c'est un clic gauche:
        if QMouseEvent.button() == Qt.LeftButton:
            if ClickIndex == 0:
                PlacementMode_pref = json.load(open(PreferencePath + 'DRAGMODE_Widget.json', "r"))
                PLACEMENTMODE = (PlacementMode_pref['VALUE'])

                print("PLACEMENTMODE = " + str(PLACEMENTMODE))

                if PLACEMENTMODE == 0:
                    self.PLUG()

                elif PLACEMENTMODE == 1:
                    self.PLUG_1x1()

                elif PLACEMENTMODE == 2:
                    #Back to ObjectMode
                    mc.SelectVertexMask()
                    mc.SelectToggleMode()
                    mc.select(d=True)

                    self.set_ImportDrag()




            else:
                pass



        # si c'est un clic miliue:
        if QMouseEvent.button() == Qt.MiddleButton:
            pass


        # si c'est un clic droit
        if QMouseEvent.button() == Qt.RightButton:
            ##KNOW FAV TAB
            FavTabpref_path = open(PreferencePath + 'KnowFavTab.json', "r")
            FavTabdata_pref = json.load(FavTabpref_path)
            FavTabPath = (FavTabdata_pref['TAB_ACTIVE_NAME'])




            self.menu = QMenu(self)





            ##____________________________________________________________________// MRB MENU

            # __________________________________________________________SECURE STEP
            secure = QAction(" // " + str(self.assetName) + " // ")
            self.menu.addAction(secure)

            # __________________________________________________________-----
            sep0 = QAction("------------- ")
            self.menu.addAction(sep0)


            # __________________________________________________________ADD FAVORITE : add to favourites, sauf si on est déjà dans le tab favourite
            if FavTabPath == "\u2764":
                mb_RemoveFavorite = QAction("Remove from favourite")
                mb_RemoveFavorite.triggered.connect(self.RemoveFavoriteMenuAction)
                self.menu.addAction(mb_RemoveFavorite)

            else:
                mb_Favorite = QAction("Add to favourite")
                mb_Favorite.triggered.connect(self.AddFavoriteMenuAction)
                self.menu.addAction(mb_Favorite)

            # __________________________________________________________-----
            sep = QAction("------------- ")
            self.menu.addAction(sep)

            # __________________________________________________________OPEN FILE
            mb_OpenFile = QAction("Open File ")
            mb_OpenFile.triggered.connect(self.WARNING_SaveOpen)
            self.menu.addAction(mb_OpenFile)

            # __________________________________________________________OPEN FOLDER
            mb_OpenFolder = QAction("Open Folder ")
            mb_OpenFolder.triggered.connect(self.set_OpenFolder)
            self.menu.addAction(mb_OpenFolder)

            # __________________________________________________________RENAME
            mb_Rename = QAction("Rename ")
            mb_Rename.triggered.connect(self.set_Rename)
            self.menu.addAction(mb_Rename)

            # __________________________________________________________DELETE
            mb_Delete = QAction("Delete ")
            mb_Delete.triggered.connect(self.set_Delete)
            self.menu.addAction(mb_Delete)








            # show the menu
            self.popup = self.menu.exec_(self.mapToGlobal(QMouseEvent.pos()))


    def mouseDoubleClickEvent(self, QMouseEvent):
        if ClickIndex == 1:
            PlacementMode_pref = json.load(open(PreferencePath + 'DRAGMODE_Widget.json', "r"))
            PLACEMENTMODE = (PlacementMode_pref['VALUE'])

            if PLACEMENTMODE == 0:
                self.PLUG()

            elif PLACEMENTMODE == 1:
                self.PLUG_1x1()

            elif PLACEMENTMODE == 2:
                # Back to ObjectMode
                mc.SelectVertexMask()
                mc.SelectToggleMode()
                mc.select(d=True)

                self.set_ImportDrag()

        else:
            pass

    # *****************************************************
    #      UNE FONCTION PAR ACTION DU MENU CLIC DROIT
    # *****************************************************
    def importMenuAction(self):
        mc.file(self.itemPath[:-4] + ".ma", i=True)

    def AddFavoriteMenuAction(self):
        # add to favourite
        favouriteFilePath = ASSET_FAVOURITES_PATH
        with open(favouriteFilePath, 'r+') as file:
            fileContent = file.read()
            JSONtoPYTHON = json.loads(fileContent)

            #check si l'asset est deja en favoris
            if self.itemPath in JSONtoPYTHON:
                mc.warning("this asset is already in your favourites")
                return

            JSONtoPYTHON.append(self.itemPath)
            final = json.dumps(JSONtoPYTHON)

        # update favourite json file for saving
        with open(favouriteFilePath, 'w+') as file:
            file.write(final)

        #update favourite tab
        self.parent.parent.favouritesWidget.createsButtonsFromFileList(folderList=[self.itemPath])
        mc.warning("Asset successfully added to the favourite tab")

    def RemoveFavoriteMenuAction(self):
        favouriteFilePath = ASSET_FAVOURITES_PATH
        with open(favouriteFilePath, 'r+') as file:
            fileContent = file.read()
            JSONtoPYTHON = json.loads(fileContent)


            JSONtoPYTHON.remove(self.itemPath)
            final = json.dumps(JSONtoPYTHON)

            print ("fileContent = " + str(fileContent) )
            print ("JSONtoPYTHON = " + str(JSONtoPYTHON))
            print ("final = " + str(final))

        # update favourite json file for saving
        with open(favouriteFilePath, 'w+') as file:
            file.write(final)


        #update favourite tab
        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        PlugIt_UI.showUI()
        mc.warning("Asset successfully remove to the favourite tab")



    def set_ImportDrag(self):
        #VERIF THERE IS A MESH
        listAllGeometrieScene = mc.ls(type="mesh")
        if listAllGeometrieScene == []:
            PlugIt_Global.WarningWindow("Drag Placement mode need at least one mesh in the scene.", 350)
            return


        #Clean Previous Bug Scene :
        if mc.objExists("Plug_Mesh"):
            mc.delete("Plug_Mesh")
        if mc.objExists("Plug_AllFaces_set"):
            mc.delete("Plug_AllFaces_set")
        if mc.objExists("Plug_EdgeBorder_set"):
            mc.delete("Plug_EdgeBorder_set")
        if mc.objExists("Plug_Selection_set"):
            mc.delete("Plug_Selection_set")


        from . import PlugIt_DragTool
        importlib.reload(PlugIt_DragTool)

        fileMA = self.itemPath.replace(".png" , ".ma")
        print("fileMA = " + str(fileMA))
        PlugIt_DragTool.goPress(fileMA)






    def set_OpenFile(self):
        selectedObject = self.itemPath[:-4]
        mc.file(selectedObject + ".ma", o=True)

    def set_ImportFile(self):
        SaveSize_pref = json.load(open(PreferencePath + 'MultiSize.json', "r"))
        MULTISIZEVALUE = (SaveSize_pref['MULTISIZEVALUE'])

        ImportShaderMode_pref = json.load(open(PreferencePath + 'ImportShader.json', "r"))
        IMPORTSHADERMODE = (ImportShaderMode_pref['IMPORTSHADERMODE'])

        # Clean if previous mode was Drag and still active
        mc.setToolTo('moveSuperContext')
        before = set(mc.ls(assemblies=True, l= True))
        selectedObject = self.itemPath[:-4]

        if IMPORTSHADERMODE == 0:
            shadingNetworksOptVar = mc.optionVar(q='removeDuplicateShadingNetworksOnImport')
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', 1))
            mc.file(selectedObject + ".ma", i=True, removeDuplicateNetworks=True)
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', shadingNetworksOptVar))
        else:
            mc.file(selectedObject + ".ma", i=True)

        after = set(mc.ls(assemblies=True, l= True))
        imported = after.difference(before)

        mc.select(imported)


        if MULTISIZEVALUE != 1.0:
            mc.CreateEmptyGroup()
            mc.rename(self.assetName + '_Ctrl')
            objToPlace = mc.ls(sl=True)
            mc.parent(imported, objToPlace[0])
            mc.select(objToPlace[0])
            mc.makeIdentity(apply=True)
            mc.xform(ws=1, a=1, piv=[0, 0, 0])

            mc.setAttr(objToPlace[0] + ".scaleX", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleY", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleZ", MULTISIZEVALUE)


    def set_ImportReplace(self):
        ##_________________INIT
        SaveSize_pref = json.load(open(PreferencePath + 'MultiSize.json', "r"))
        MULTISIZEVALUE = (SaveSize_pref['MULTISIZEVALUE'])

        ImportShaderMode_pref = json.load(open(PreferencePath + 'ImportShader.json', "r"))
        IMPORTSHADERMODE = (ImportShaderMode_pref['IMPORTSHADERMODE'])




        selection = mc.ls(selection=True, l= True)
        if selection == []:
            PlugIt_Global.WarningWindow("On 'Replace' mode : you should select one Object.", 350)
            return

        ##_________________IMPORT L'ASSET
        before = set(mc.ls(assemblies=True, l= True))
        selectedObject = self.itemPath[:-4]


        if IMPORTSHADERMODE == 0:
            shadingNetworksOptVar = mc.optionVar(q='removeDuplicateShadingNetworksOnImport')
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', 1))
            mc.file(selectedObject + ".ma", i=True, removeDuplicateNetworks=True)
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', shadingNetworksOptVar))
        else:
            mc.file(selectedObject + ".ma", i=True)


        after = set(mc.ls(assemblies=True, l= True))
        imported = after.difference(before)

        ##_______________CREATION DU GROUPE QUI CONTIENT TOUS LES MESH
        mc.CreateEmptyGroup()
        mc.rename(self.assetName + '_Ctrl')
        objToPlace = mc.ls(sl=True)
        mc.parent(imported, objToPlace[0])





        if MULTISIZEVALUE != 1.0:
            mc.setAttr(objToPlace[0] + ".scaleX", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleY", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleZ", MULTISIZEVALUE)
            mc.select(objToPlace[0])
            mc.makeIdentity(apply=True)





        mc.select(objToPlace[0])
        mc.makeIdentity(apply=True)

        allNewSel = []
        #OPERATION DE REPLACEMENT
        if len(selection) > 1:
            for each in selection:
                objDup = mc.duplicate(objToPlace[0])
                mc.matchTransform(objDup[0], each, pos=True, rot=True, scl =True)
                mc.delete(each)
                allNewSel.append(objDup[0])

        else:
            SELECTION = selection
            mc.matchTransform(objToPlace[0], SELECTION, pos=True, rot=True, scl =True)
            mc.delete(SELECTION)

        if len(selection) > 1:
            toAdd = allNewSel.pop(0)
            theGoodSel = allNewSel.append(toAdd)
            #currentSel = mc.ls(sl=True, l=True)
            mc.delete(objToPlace[0])
            print ("allNewSel == " + str(allNewSel))
            print ("theGoodSel == " + str(theGoodSel))
            mc.select(allNewSel)


        else:
            mc.select(objToPlace[0])



        mc.setToolTo('moveSuperContext')
    def set_importAtSelection(self):
        SaveSize_pref = json.load(open(PreferencePath + 'MultiSize.json', "r"))
        MULTISIZEVALUE = (SaveSize_pref['MULTISIZEVALUE'])

        ImportShaderMode_pref = json.load(open(PreferencePath + 'ImportShader.json', "r"))
        IMPORTSHADERMODE = (ImportShaderMode_pref['IMPORTSHADERMODE'])

        selectionCheck = mc.ls(sl=True)
        if selectionCheck == []:
            PlugIt_Global.WarningWindow("On 'Place at Selection' mode : you should select component first.", 350)
            return

        mc.setToolTo('moveSuperContext')
        pos = mc.manipMoveContext('Move', query=True, position=True)
        selection = mc.ls(selection=True, l= True)


        ##_________________IMPORT L'ASSET
        before = set(mc.ls(assemblies=True, l= True))
        selectedObject = self.itemPath[:-4]


        if IMPORTSHADERMODE == 0:
            shadingNetworksOptVar = mc.optionVar(q='removeDuplicateShadingNetworksOnImport')
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', 1))
            mc.file(selectedObject + ".ma", i=True, removeDuplicateNetworks=True)
            mc.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', shadingNetworksOptVar))
        else:
            mc.file(selectedObject + ".ma", i=True)


        after = set(mc.ls(assemblies=True, l= True))
        imported = after.difference(before)

        ##_______________CREATION DU GROUPE QUI CONTIENT TOUS LES MESH
        mc.CreateEmptyGroup()
        mc.rename(self.assetName + '_Ctrl')
        objToPlace = mc.ls(sl=True)
        mc.parent(imported, objToPlace[0])


        if MULTISIZEVALUE != 1.0:
            mc.setAttr(objToPlace[0] + ".scaleX", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleY", MULTISIZEVALUE)
            mc.setAttr(objToPlace[0] + ".scaleZ", MULTISIZEVALUE)
            mc.select(objToPlace[0])
            mc.makeIdentity(apply=True)


        mc.select(objToPlace[0])
        mc.makeIdentity(apply=True)
        mc.xform(ws=1, a=1, piv=[0, 0, 0])



        mc.move(pos[0], pos[1], pos[2], objToPlace)
        constr = mc.normalConstraint(selection, objToPlace, aimVector=(0, 1, 0), worldUpType=0)
        mc.delete(constr)

        mc.select(objToPlace[0])
        mc.setToolTo('moveSuperContext')
    def set_OpenFolder(self):
        selectedObject = self.itemPath[:-4]
        removeEnd = selectedObject.replace("/" + self.assetName, "")
        ItemFolderPath = removeEnd + "/" + self.assetName
        os.startfile(ItemFolderPath)
    def set_Rename(self):
        selectedObject = self.itemPath[:-4]
        removeEnd = selectedObject.replace("/" + self.assetName, "")
        ItemFolderPath = removeEnd + "/" + self.assetName


        from . import PlugIt_Rename
        import importlib
        importlib.reload(PlugIt_Rename)
        PlugIt_Rename.SEND_INFO(str(removeEnd), str(ItemFolderPath))
        PlugIt_Rename.showUI()
    def set_Delete(self):
        selectedObject = self.itemPath[:-4]
        removeEnd = selectedObject.replace("/" + self.assetName, "")
        ItemFolderPath = removeEnd + "/" + self.assetName
        shutil.rmtree(ItemFolderPath)



        # FAV CLEAN List
        itemName = (ItemFolderPath.split("/")[-1]).replace(".png", "")
        print ("itemName = " + itemName)

        favouriteFilePath = ASSET_FAVOURITES_PATH
        with open(favouriteFilePath, 'r+') as file:
            fileContent = file.read()
            FAVLIST = json.loads(fileContent)
            FAVLISTLen = len(FAVLIST)-1

        for each in FAVLIST:
            nameInList = (each.split("/")[-1]).replace(".png", "")
            print ("each = " + each)
            print ("nameInList = " + nameInList)
            if nameInList == itemName:
                if FAVLIST.index(each) == 0:
                    print ("PLACE AT : START")
                    stringToReplace = "'" + str(ItemFolderPath) + "/" + str(itemName) + ".png" +  "'" + ","
                elif FAVLIST.index(each) == FAVLISTLen:
                    print ("PLACE AT : END")
                    stringToReplace = ", " + "'" + str(ItemFolderPath) + "/" + str(itemName) + ".png"  + "'"
                else:
                    print ("PLACE AT : MIDDLE")
                    stringToReplace = "'" + str(ItemFolderPath) + "/" + str(itemName) + ".png" + "'" + ","

                print ("stringToReplace IN DELETE == " + stringToReplace)
                newFAV = str(FAVLIST).replace(str(stringToReplace), "")
                print ("NEW FAV IN DELETE == " + newFAV)
                newFAVtoWritte = newFAV.replace("'", '"')

                # update favourite json file for saving
                with open(favouriteFilePath, 'w+') as file:
                    file.write(newFAVtoWritte)



        from . import PlugIt_UI
        import importlib
        importlib.reload(PlugIt_UI)
        ui = PlugIt_UI.showUI()
    def none (self):
        pass
    def WARNING_SaveOpen(self):
        BackgroundColor = 0.16
        Message = "Save changes before to open?"
        # ________________//
        if mc.window("WarningWindow", exists=True):
            mc.deleteUI("WarningWindow")
        mc.window("WarningWindow", title=' Save Changes ', s=False, vis=True, rtf=False)
        mc.columnLayout(adj=True, rs=3, bgc=[BackgroundColor, BackgroundColor, BackgroundColor])
        mc.separator(h=8, style='none')
        mc.text(l="  " + Message + "  ", al="center")
        mc.separator(h=8, style='none')
        mc.rowColumnLayout( numberOfRows=1 )
        mc.separator(w=10, style='none')
        mc.button(l="Save", c=self.WarningSave, width= 85, h=20)
        mc.separator(w=10, style='none')
        mc.button(l="Don't save", c=self.WarningDontSave, width= 85, h=20)
        mc.separator(w=10, style='none')
        mc.button(l="Cancel", c=self.WarningCancel, width= 85, h=20)
        mc.window("WarningWindow", e=True, wh=(300, 80))

        qw = omui.MQtUtil.findWindow("WarningWindow")
        widget = wrapInstance(int(qw), QWidget)
        icon = QIcon(IconPath + "Windows_Ico_Warning.png")
        widget.setWindowIcon(icon)

        mc.showWindow()
    def WarningSave(self, *args):
        selectedObject = self.itemPath[:-4]
        mc.file(f=True, save=True )
        mc.file(selectedObject + ".ma", o=True, f=True)
        mc.deleteUI("WarningWindow")
    def WarningDontSave(self, *args):
        selectedObject = self.itemPath[:-4]
        mc.file(selectedObject + ".ma", o=True, f=True)
        mc.deleteUI("WarningWindow")
    def WarningCancel(self, *args):
        mc.deleteUI("WarningWindow")

    def autoDetectFace(self):
        selection = mc.ls(sl=True)
        isFace = mc.filterExpand(sm=34)

        if selection == []:
            print("Selection Empty")
        elif len(selection) != 1:
            print("More then 1 len")
        elif isFace == None:
            pass
        else:
            if mc.window("P L U G  -  O p t i o n s", exists=True):
                return

            fileMA = self.itemPath.replace(".png", ".ma")
            from . import PlugIt_Plug
            importlib.reload(PlugIt_Plug)
            PlugIt_Plug.PERFORM_1x1_PLUG(fileMA)





    def PLUG(self):
        MelScript_ExtractFace = TOOLS_PATH + 'wzx_DuplicateFace.mel'

        if mc.window("P L U G  -  O p t i o n s", exists=True):
            return

        selection = mc.ls(sl=True)
        isFace = mc.filterExpand(sm=34)
        oneFace = 0

        if selection == []:
            PlugIt_Global.WarningWindow("You should select faces.", 300)
            return
        elif isFace == None:
            PlugIt_Global.WarningWindow("Not Face component. You should select faces component only.", 400)
            return

        mc.ConvertSelectionToEdgePerimeter()
        numberOfEdges = len(mc.filterExpand(sm=32))
        mc.select(selection)



        if len(isFace) > 9:
            PlugIt_Global.WarningWindow("You can't select more than 9 faces.", 300)
            return

        elif len(selection) != 1:
            selectionObject = mc.ls(hl=True)
            mc.delete(selectionObject, constructionHistory=True)
            saveSelFace = mc.ls(sl=True)

            # ______ Verif Adgacente Faces
            mel.eval('source "' + MelScript_ExtractFace + '"')
            try:
                mc.polySeparate()
                mc.PickWalkUp()
                mc.delete()
                PlugIt_Global.WarningWindow("Be sure to only select one area of adjacent faces.", 600)
                return
            except:
                mc.delete()
                mc.select(saveSelFace)

        else:
            oneFace = 1





        ##__________________________________________________________ V E R I F I C A T I O N
        #SI no selection
        #Si selection pas face
        #Si face number + de 16 edges

        fileMA = self.itemPath.replace(".png", ".ma")
        from . import PlugIt_Plug
        importlib.reload(PlugIt_Plug)
        PlugIt_Plug.PERFORM_PLUG(fileMA, oneFace, numberOfEdges)




    def PLUG_1x1(self):
        
        SCRIPT_JOB_PREVIOUS = (json.load(open(PreferencePath + 'ScriptJob_1x1.json', "r"))['VALUE'])


        print("quickPlug_ScriptJob =" + str(SCRIPT_JOB_PREVIOUS))
        if SCRIPT_JOB_PREVIOUS == 1111:
            quickPlug_ScriptJob = mc.scriptJob(event=["SelectionChanged", self.autoDetectFace])
            open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": quickPlug_ScriptJob}))
        else:
            mc.scriptJob(kill=SCRIPT_JOB_PREVIOUS, force=True)
            quickPlug_ScriptJob = mc.scriptJob(event=["SelectionChanged", self.autoDetectFace])
            open(PreferencePath + 'ScriptJob_1x1.json', "w").write(json.dumps({"VALUE": quickPlug_ScriptJob}))



























































