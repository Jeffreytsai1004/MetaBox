
'''
from importlib import reload
import Rename
reload(Rename)
Rename.UI()
'''
from Modeling.Manage import Rename
# this text can be entered from the script editor and can be made into a button

import maya.cmds as cmds # type: ignore

def UI():
	
	global SelectName
	global RenameText

	global StartValue
	global PaddingValue
	global NumberCheck

	global RemoveFirst
	global RemoveEnd

	global PrefixText
	global SuffixText

	global SearchText
	global ReplaceText
	global SRCheck
	
	#UI Width
	sizeX = 240
	version = "v1.0"
	if cmds.window("RenameWin", exists=True):
		cmds.deleteUI("RenameWin", window=True)
	
	#Creating UI
	igEzRenamWin = cmds.window("RenameWin", title="Rename Tool "+version, width=sizeX+6, height=385, mnb = True, mxb = False, sizeable = False)
	
	#Creating interface elements
	mainLayout = cmds.columnLayout("mainColumnLayout", width = sizeX, adjustableColumn=False, co = ["both",2])

	#Select All Button
	cmds.separator(h=5, style = "none", parent = mainLayout)
	cmds.button(label = "Select All", w=sizeX, h=25, c=SelectAll, ann = "Select ALL objects in scene")
	cmds.separator(h=5, style = "none", parent = mainLayout)

	#Select by Name
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 25), (2, 60)], cs = [(5,5), (5,5)])
	cmds.button(label = "Select by Name", w=sizeX/3, h=25, c=SelectName, align = "Center", ann="Select objects by name")
	SelectName = cmds.textField(w = sizeX*0.646, ann="Select by Name \n Use * after and/or before the text to select by prefix/suffix \n Example: *_grp")
	cmds.separator(w = sizeX, h=15, style = "in", parent = mainLayout)
	
	#Rename and Number
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)])
	#Rename Field
	cmds.text(label="  Rename:", font = "boldLabelFont", w = sizeX/4, align="left", ann="Write the name you want to rename the objects selected")
	RenameText = cmds.textField(w = sizeX*0.75, ann="Write the name you want to rename the objects selected")
	
	#Start Field
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)])
	cmds.text(label="  Start:", font = "boldLabelFont", w = sizeX/4, align="left")
	StartValue = cmds.textField(w = sizeX/4, tx="1", ann="Write the Start value for the sequence")
	#Padding Field
	cmds.text(label="  Padding:", font = "boldLabelFont", w = sizeX/4, align="left")
	PaddingValue = cmds.textField(w = sizeX/4, tx="2", ann="Write the Padding value for the numbers")
	#Number Letters
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)])
	cmds.text(label="", font = "boldLabelFont", w = sizeX/4-2, align="left")
	NumberCheck = cmds.radioButtonGrp(labelArray2=[ 'Numbers', 'Letters'], numberOfRadioButtons=2, w=sizeX, h=20, sl=1, cw = ([1,120]))
	#ButtonRename and Number
	cmds.separator(h=5, style = "none", parent = mainLayout)
	cmds.button(label = "Rename and Number", w=sizeX, h=25, c=RenameNumber, align = "Center", parent = mainLayout)
	cmds.separator(w = sizeX, h=15, style = "in", parent = mainLayout)

	#RemoveCharacter
	#Remove First/Last
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 25), (2, 60)], cs = [(5,5)])
	cmds.text(label="  Remove:", font = "boldLabelFont", w = sizeX/3-12, align="left")
	cmds.button(label = "First Char->", w=sizeX/3, h=25, c=lambda *args: Rename.Remove(True), align = "Center")
	cmds.button(label = "<-Last Char", w=sizeX/3, h=25, c=lambda *args: Rename.Remove(False), align = "Center")
	cmds.separator(h=5, style = "none", parent = mainLayout)

	#Remove pasted__
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 25), (2, 60)], cs = [(90,90)])
	cmds.text(label="  ", font = "boldLabelFont", w = sizeX/3-12, align="left")
	cmds.button(label = "pasted__", w=sizeX/3, h=25, c=RemovePasted, align = "Center")

	#Remove UI
	cmds.separator(h=5, style = "none", parent = mainLayout)
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 25), (2, 60)], cs = [(8.5,8.5)])
	RemoveFirst = cmds.textField(w = sizeX/5, tx="0", ann="Write the amount of characters you want to delete on text beginning")
	cmds.button(label = "-", w=25, h=25, c=lambda *args: Rename.RemoveChar('begin'), align = "Center", ann="Delete on text beginning")
	cmds.button(label = "Remove", w=sizeX/4, h=25, c=lambda *args: Rename.RemoveChar('all'), align = "Center", ann="Delete on text beginning and ending")
	cmds.button(label = "-", w=25, h=25, c=lambda *args: Rename.RemoveChar('end'), align = "Center", ann="Delete on text ending")
	RemoveEnd = cmds.textField(w = sizeX/5, tx="3", ann="Write the amount of characters you want to delete on text ending")
	cmds.separator(w = sizeX, h=15, style = "in", parent = mainLayout)
	
	#Suffix
	#Control Suffix
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	cmds.text(label="  Prefix:", font = "boldLabelFont", w = sizeX/4-10, align="left", ann="Write the prefix")
	PrefixText = cmds.textField(w = sizeX/2.5+33, tx="prefix_", ann="Write the prefix")
	cmds.button(label = "Add", w=sizeX/4-10, h=25, c=lambda *args: Rename.PrefixSuffix(False), align = "Center")
	cmds.separator(h=5, style = "none", parent = mainLayout)
	#Group Suffix
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	cmds.text(label="  Suffix:", font = "boldLabelFont", w = sizeX/4-10, align="left", ann="Write the suffix")
	SuffixText = cmds.textField(w = sizeX/2.5+33, tx="_suffix", ann="Write the suffix")
	cmds.button(label = "Add", w=sizeX/4-10, h=25, c=lambda *args: Rename.PrefixSuffix(True), align = "Center")
	cmds.separator(w = sizeX, h=15, style = "in", parent = mainLayout)

	#Prefix
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	cmds.button(label = "_Grp", w=sizeX/5-4, h=25, c=lambda *args: Rename.Suffix('_Grp'), align = "Center", ann = "Add Grp suffix") 
	cmds.button(label = "_Geo", w=sizeX/5-4, h=25, c=lambda *args: Rename.Suffix('_Geo'), align = "Center", ann = "Add Geo suffix")
	cmds.button(label = "_Ctrl", w=sizeX/5-4, h=25, c=lambda *args: Rename.Suffix('_Ctrl'), align = "Center", ann = "Add Ctrl suffix")
	cmds.button(label = "_Jnt", w=sizeX/5-4, h=25, c=lambda *args: Rename.Suffix('_Jnt'), align = "Center", ann = "Add Jnt suffix")
	cmds.button(label = "_Drv", w=sizeX/5-4, h=25, c=lambda *args: Rename.Suffix('_Drv'), align = "Center", ann = "Add Drv suffix")
	cmds.separator(w = sizeX, h=15, style = "in", parent = mainLayout)
	
	#Search and Replace
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	cmds.text(label="  Search:", font = "boldLabelFont", w = sizeX/4-10, align="left", ann="Write the text to search")
	SearchText = cmds.textField(w = sizeX/2+100, ann="Write the text to search")
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	cmds.text(label="  Replace:", font = "boldLabelFont", w = sizeX/4-10, align="left", ann="Write the text to replace")
	ReplaceText = cmds.textField(w = sizeX/2+100, ann="Write the text to replace")
	cmds.rowColumnLayout( numberOfRows=1, w=sizeX, parent=mainLayout, rowHeight=[(1, 20), (2, 60)], cs = [(5,5)])
	SRCheck = cmds.radioButtonGrp(labelArray3=[ 'Selected', 'Hierarchy', 'All'], numberOfRadioButtons=3, w=sizeX, h=20, sl=1, cw = ([1,95],[2,95],[3,95]))
	cmds.button(label = "Apply", w=sizeX, h=25, c=SearchReplace, align = "Center", parent = mainLayout)
	cmds.separator(h=5, style = "none", parent = mainLayout)
	
	#Show UI:
	cmds.showWindow(igEzRenamWin)

def SelectAll(*args):
	cmds.select(ado=True, hi = True)
	selection = cmds.ls(selection=True, sn=True)
	selectionAdd = []

	#Old select all code version
	"""for objs in selection:
		children = cmds.listRelatives(objs, c=True, f =True)
		print "Children01:", children
		shapes = cmds.listRelatives(objs, s=True, f = True)
		print "Shapes:", shapes
		
		if not children == None:
			if not shapes == None:
				for s in shapes:
					children.remove(s)
			
			for chi in children:
				
				children2 = cmds.listRelatives(chi, c=True, f = True)
				print "CHildren02:", children2

				if not children2 == None:
					for chi2 in children2:
						children.append(chi2)
				
				selectionAdd.append(chi)

		

	for objs in selectionAdd:
		cmds.select(objs, add=True)"""

def SelectName(*args):
	cmds.select(cl=True)
	name = cmds.textField(SelectName, text = 1, q=True)
	try:
		selection = cmds.ls(name, l = True)
	except:
		cmds.warning("Object Don't Exist")

	for objs in selection:
		cmds.select(objs, add=True)

def RenameNumber(*args):

	number = cmds.textField(StartValue, text = 1, q=True)
	number = int(number)
	
	padding = cmds.textField(PaddingValue, text = 1, q=True)
	padding = int(padding)

	NumberLetters = cmds.radioButtonGrp(NumberCheck, q=True, select=True)
	
	newName = cmds.textField(RenameText, text = 1, q=True)

	selection = cmds.ls(selection=True, sn=True)
	
	lettersList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	#Number suffix
	y = 0
	
	for obj in selection: 
		try:
			#Teste if has duplicate mesh with the same name on the scene and return the name without parents
			trueName = testDuplicateName(obj)
			#Save the original name
			oldName = trueName

			#If true use numbers, else use letters
			if NumberLetters == 1:
				zeros = ""
				for x in range(int(padding)):
					if len(str(number)) <= x:
						zeros = zeros+"0"
				
				#Create the newName and rename
				name = newName+"_"+"{:0>"+str(padding)+"}"
				newNameList = name.format(number)
				cmds.rename(obj, name.format(number))

			else:
				newNameList = newName+"_"+lettersList[y]
				cmds.rename(obj, newName+"_"+lettersList[y])
				if y < len(lettersList)-1:
					y+=1
				else:
					y=0

			#For to rename all the oldNames on list to newNames
			for x in range(len(selection)):
				newParentName = selection[x].replace(oldName, newNameList)
				selection[x] = newParentName
		except:
			pass
		
		number = int(number+1)

def RemoveChar(Type):
	
	first = cmds.textField(RemoveFirst, text = 1, q=True)
	end = cmds.textField(RemoveEnd, text = 1, q=True)

	selection = cmds.ls(selection = True, sn=True)

	for objs in selection:
		#Teste if has duplicate mesh with the same name on the scene
		trueName = testDuplicateName(objs)

		#Save the original name
		oldName = trueName

		if Type == "all":
			name = trueName[:-int(end)]
			name = name[int(first):]

		if Type == "begin":
			name = trueName[int(first):]

		if Type == "end":
			name = trueName[:-int(end)]
		
		try:
			cmds.rename(objs, str(name))
		except:
			pass

		#For to rename all the oldNames on list to newNames
		for x in range(len(selection)):
			newParentName = selection[x].replace(oldName, name)
			selection[x] = newParentName
	

def Remove(Type):
	
	selection = cmds.ls(selection = True, sn = True)

	for objs in selection:
		#Teste if has duplicate mesh with the same name on the scene
		trueName = testDuplicateName(objs)

		#Save the original name
		oldName = trueName

		if Type:
			name = trueName[1:]
		else:
			name = trueName[:-1]

		try:
			cmds.rename(objs, name)
		except:
			pass

		#For to rename all the oldNames on list to newNames
		for x in range(len(selection)):
			newParentName = selection[x].replace(oldName, name)
			selection[x] = newParentName



def RemovePasted(*args):
	
	selection = cmds.ls("pasted__*", sn = True)
	
	for objs in selection:
		#Teste if has duplicate mesh with the same name on the scene
		trueName = testDuplicateName(objs)

		name = trueName[8:]
		try:
			cmds.rename(objs, name)
		except:
			cmds.warning("Don't Exist pasted Objects")

def PrefixSuffix(Suffix):
	prefix = cmds.textField(PrefixText, text = 1, q=True)
	suffix = cmds.textField(SuffixText, text = 1, q=True)

	selection = cmds.ls(selection = True, sn = True)

	for objs in selection:

		#Teste if has duplicate mesh with the same name on the scene
		trueName = testDuplicateName(objs)
		#Save the original name
		oldName = trueName
		
		if Suffix:
			name = str(trueName)+suffix
		else:
			name = prefix+str(trueName)

		try:
			cmds.rename(objs, name)
		except:
			pass
		
		#For to rename all the oldNames on list to newNames
		for x in range(len(selection)):
			newParentName = selection[x].replace(oldName, name)
			selection[x] = newParentName
		

def Suffix(Text):
	
	selection = cmds.ls(selection = True, sn = True)
	
	for objs in selection:
		#Test if has duplicate mesh with the same name on the scene
		trueName = testDuplicateName(objs)

		#Save the original name
		oldName = trueName

		newName = trueName+Text
		try:
			cmds.rename(objs, newName)
		except:
			pass

		#For to rename all the oldNames on list to newNames
		for x in range(len(selection)):
			newParentName = selection[x].replace(oldName, newName)
			selection[x] = newParentName

def SearchReplace(*args):
	
	search = cmds.textField(SearchText, text = 1, q=True)
	replace = cmds.textField(ReplaceText, text = 1, q=True)

	SRMethod = cmds.radioButtonGrp(SRCheck, q=True, select=True)
	
	#Selected search and Replace method
	if SRMethod == 1:
		selection = cmds.ls(selection = True, sn = True)

	#Hierarchy search and Replace method
	if SRMethod == 2:
		cmds.select(hi = True)
		selection = cmds.ls(selection = True, sn = False)
		
	#All search and Replace method
	if SRMethod == 3:
		#Select All DagObjects in scene
		selection = []
		cmds.select(ado = True, hi = True)
		selection = cmds.ls(selection = True, sn=False)

	#for to rename the objects 
	for obj in selection:
		#Teste if has duplicate mesh with the same name on the scene and return the name without parents
		trueName = testDuplicateName(obj)
		#Save the original name
		oldName = trueName
		#Search and replace to create the new name
		newName = trueName.replace(search, replace)
		
		#Rename the object
		try:
			cmds.rename(obj, newName)
		except:
			pass
	
		#For to rename all the oldNames on list to newNames
		for x in range(len(selection)):
			newParentName = selection[x].replace(oldName, newName)
			selection[x] = newParentName

		print("Slecao: ", selection)

		
	
def testDuplicateName(Obj):

	try:
		trueName =  Obj.split("|")
		return trueName[len(trueName)-1]
	except:
		return Obj

