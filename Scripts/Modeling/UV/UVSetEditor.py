#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds

# Define minimum window width and height
MIN_WINDOW_WIDTH = 300  # Increased from 200 to 300
MIN_WINDOW_HEIGHT = 300

# Function: Get and display UV sets
def refresh_uv_sets():
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Please select an object first.")
        return

    selected_object = selection[0]
    uv_sets = cmds.polyUVSet(selected_object, query=True, allUVSets=True)
    cmds.textScrollList('uvList', edit=True, removeAll=True)
    for uv_set in uv_sets:
        cmds.textScrollList('uvList', edit=True, append=uv_set)

# Function: Switch UV set
def switch_uv_set(*args):
    selected_uv_set = cmds.textScrollList('uvList', query=True, selectItem=True)
    if selected_uv_set:
        selected_object = cmds.ls(selection=True)
        if selected_object:
            selected_object = selected_object[0]
            # Switch current UV set
            cmds.polyUVSet(selected_object, currentUVSet=True, uvSet=selected_uv_set[0])
            print(f"Switched to UV set: {selected_uv_set[0]}")
        else:
            cmds.warning("Please select an object.")
    else:
        cmds.warning("Please select a UV set.")

# Function: Delete selected UV set
def delete_selected_uv_set():
    selected_uv_set = cmds.textScrollList('uvList', query=True, selectItem=True)
    if selected_uv_set:
        cmds.polyUVSet(delete=True, uvSet=selected_uv_set[0])
        refresh_uv_sets()

# Function: Rename selected UV set
def rename_selected_uv_set(new_name):
    selected_uv_set = cmds.textScrollList('uvList', query=True, selectItem=True)
    if selected_uv_set:
        if new_name:
            cmds.polyUVSet(rename=True, newUVSet=new_name, uvSet=selected_uv_set[0])
            refresh_uv_sets()
            cmds.textFieldGrp('newNameField', edit=True, text='')  # Clear input field content
        else:
            cmds.warning("Please enter a new name.")
    else:
        cmds.warning("Please select a UV set first.")

# Function: Create new UV set
def create_new_uv_set(new_name):
    if new_name:
        cmds.polyUVSet(create=True, uvSet=new_name)
        refresh_uv_sets()
        cmds.textFieldGrp('newNameField', edit=True, text='')  # Clear input field content
    else:
        cmds.warning("Please enter a name for the new UV set.")

# Function: Set UV set 1 name
def set_uv_set1_name(*args):
    selected_uv_set = cmds.textScrollList('uvList', query=True, selectItem=True)
    if selected_uv_set:
        cmds.textFieldGrp("uvSet1", edit=True, text=selected_uv_set[0])
    else:
        cmds.warning("Please select a UV set first.")

# Function: Set UV set 2 name
def set_uv_set2_name(*args):
    selected_uv_set = cmds.textScrollList('uvList', query=True, selectItem=True)
    if selected_uv_set:
        cmds.textFieldGrp("uvSet2", edit=True, text=selected_uv_set[0])
    else:
        cmds.warning("Please select a UV set first.")

# Function: UV set swap
def UVsetSwap(*args):
    UVname1 = cmds.textFieldGrp("uvSet1", query=True, text=True)
    UVname2 = cmds.textFieldGrp("uvSet2", query=True, text=True)
    cmds.polyUVSet(query=True, allUVSets=True)
    cmds.polyUVSet(create=True, uvSet='TempUV')
    cmds.polyUVSet(copy=True, nuv='TempUV', uvSet=UVname1)
    cmds.polyUVSet(copy=True, nuv=UVname1, uvSet=UVname2)
    cmds.polyUVSet(copy=True, nuv=UVname2, uvSet='TempUV')
    cmds.polyUVSet(delete=True, uvSet='TempUV')
    refresh_uv_sets()   # Refresh list after execution

def UVsetReorder(*args):
    UVname1 = cmds.textFieldGrp("uvSet1", query=True, text=True)
    UVname2 = cmds.textFieldGrp("uvSet2", query=True, text=True)
    print("Reorder object is " + UVname1 + " + " + UVname2)
    cmds.polyUVSet(reorder=True, uvSet=UVname1, newUVSet=UVname2)
    UVobj = cmds.ls(sl=True)
    cmds.select(UVobj)
    refresh_uv_sets()   # Refresh list after execution

# Function: UV set transfer
def get_object_name(*args):
    # Get currently selected object and fill its name in the text field
    selected = cmds.ls(sl=True)
    if selected:
        cmds.textField('objectNameField', edit=True, text=selected[0])
    else:
        cmds.warning("No object selected.")

def set_uv(*args):
    # Get source and target objects, perform UV transfer, and clean up history
    source_object = cmds.textField('objectNameField', query=True, text=True)
    target_object = cmds.ls(sl=True)
    if not source_object or not target_object:
        cmds.warning("Please ensure both source and target objects are selected.")
        return
    target_object = target_object[0]
    sample_space_dict = {'World': 0, 'Local': 1, 'UV': 5, 'Component': 4}
    sample_space = cmds.radioCollection('sampleSpaceRadio', query=True, select=True)
    sample_space = cmds.radioButton(sample_space, query=True, label=True)
    sample_space = sample_space_dict.get(sample_space, 0)
    cmds.transferAttributes(source_object, target_object, transferPositions=0, transferNormals=0, transferUVs=2, transferColors=0, sampleSpace=sample_space, searchMethod=3)
    cmds.delete(target_object, constructionHistory=True)  # Clean up history

def on_window_resize(*args):
    window_name = "UVSetEditor"
    # Get current window size
    current_width = cmds.window(window_name, query=True, width=True)
    current_height = cmds.window(window_name, query=True, height=True)
    
    # Check and limit window size
    if current_width < MIN_WINDOW_WIDTH:
        cmds.window(window_name, edit=True, width=MIN_WINDOW_WIDTH)
    if current_height < MIN_WINDOW_HEIGHT:
        cmds.window(window_name, edit=True, height=MIN_WINDOW_HEIGHT)
    
def show(*args):
    window_name = "UVSetEditor"
    # Check if window exists, if so, delete it
    if cmds.window(window_name, exists=True):
        cmds.deleteUI('UV Set Editor', window=True)
    # Window
    # Create a new window and set its title and initial size
    window = cmds.window(window_name, title=" UV Set Editor", widthHeight=(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT), sizeable=True, tlb=True)  # tlb=True

    cmds.frameLayout(label='UV-Set')
    cmds.columnLayout(adjustableColumn=True)
    # Create a textScrollList control and set the selection change command
    cmds.textScrollList('uvList', numberOfRows=8, allowMultiSelection=False, width=280, selectCommand=switch_uv_set)
    cmds.textFieldGrp('newNameField',  placeholderText='      Enter new name, then click Re to rename', width=280, columnAlign=[1, 'center'] ,columnWidth=[1,280])
    cmds.rowLayout(numberOfColumns=4,
                            columnWidth4=(65, 65, 65, 65),
                            columnAttach4=('both', 'both', 'both', 'both'))
    cmds.button( label='Get', height=32, command=lambda x: refresh_uv_sets(),backgroundColor=(0.53, 0.81, 0.98))
    cmds.button( label='Del', height=32, command=lambda x: delete_selected_uv_set())
    cmds.button( label='New', height=32, command=lambda x: create_new_uv_set(cmds.textFieldGrp('newNameField', query=True, text=True)))
    cmds.button( label='Re', height=32, command=lambda x: rename_selected_uv_set(cmds.textFieldGrp('newNameField', query=True, text=True)))
    cmds.setParent( '..' )

    cmds.setParent('..')  # End current form layout

    cmds.frameLayout(label='UV-Swap')
    cmds.columnLayout(adjustableColumn=True, width=280)
    cmds.text(l='Enter UV set names in "uv1" and "uv2"', h=15)
    cmds.text(l='    UV swap or reorder swap. ', h=15)
    cmds.text(l='', h=5)
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(65, 65, 130), columnAttach3=('both', 'both', 'both'))
    cmds.button(label='Get', height=25, command=set_uv_set1_name, backgroundColor=(0.53, 0.81, 0.98))
    cmds.textFieldGrp("uvSet1", placeholderText='uv1', editable=True, width=200)
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(65, 65, 130), columnAttach3=('both', 'both', 'both'))
    cmds.button(label='Get', height=25, command=set_uv_set2_name, backgroundColor=(0.53, 0.81, 0.98))
    cmds.textFieldGrp("uvSet2", placeholderText='uv2', editable=True, width=200)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 135), (2, 135)])
    cmds.button(label='UV Swap', command=UVsetSwap, backgroundColor=(0.53, 0.81, 0.98))
    cmds.button(label='Reorder Swap', command=UVsetReorder, backgroundColor=(0.53, 0.81, 0.98))

    UVname1 = cmds.textFieldGrp("uvSet1", query=True, text=True)
    UVname2 = cmds.textFieldGrp("uvSet2", query=True, text=True)
    print("Now we have UVset = {}, {}".format(UVname1, UVname2))

    cmds.setParent('..')  # End current form layout

    # Separator
    cmds.separator(height=20, style='in')

    # Create a column layout, all child elements will be vertically arranged
    cmds.frameLayout(label='UV-Transfer')
    cmds.columnLayout(adjustableColumn=True, width=230, height=130)
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(50, 100, 50))
    cmds.button(label='Get', command=get_object_name, backgroundColor=(0.53, 0.81, 0.98), width=45)  # Create a button that calls get_object_name function when clicked
    cmds.textField('objectNameField', enable=False, width=120)  # Create a text field to display the name of the selected object
    cmds.button(label='Set', command=set_uv, backgroundColor=(0.53, 0.81, 0.98), width=45)  # Create a button that calls set_uv function when clicked
    cmds.setParent('..')  # End current form layout

    # cmds.frameLayout(label='Sample Space')
    cmds.text(l='Sample Space:', h=20, align='left')
    form = cmds.formLayout()

    cmds.radioCollection('sampleSpaceRadio')  # Create a radio button group
    rb1 = cmds.radioButton(label='World', select=True)  # Create a radio button
    rb2 = cmds.radioButton(label='Local')
    rb3 = cmds.radioButton(label='UV')
    rb4 = cmds.radioButton(label='Component')
    # Set form layout parameters to keep radio buttons horizontally aligned and centered when window size changes
    cmds.formLayout(form, edit=True, attachForm=[(rb1, 'left', 10), (rb4, 'right', 10)], attachControl=[(rb2, 'left', 5, rb1), (rb3, 'left', 5, rb2), (rb4, 'left', 5, rb3)])
    cmds.setParent('..')  # End current form layout

    cmds.scriptJob(event=["idle", on_window_resize], parent=window)  # Listen for window resize events

    cmds.showWindow(window)  # Show window