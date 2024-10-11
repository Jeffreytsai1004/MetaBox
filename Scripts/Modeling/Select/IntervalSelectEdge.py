#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel

def select_edges():
    num_edges_selected = cmds.filterExpand(expand=True, selectionMask=32)
    size_components = len(num_edges_selected) if num_edges_selected else 0
    
    if size_components == 0:
        cmds.error("Select at least one edge before running the script.")
    elif size_components == 1:
        mel.eval('polySelectEdgesEveryN "edgeRing" 2')
        print("1 cycle mode selected.")
    elif size_components == 2:
        mel.eval('polySelectEdgesEveryN "edgeRing" 4')
        print("2 cycle modes selected.")
    elif size_components == 3:
        mel.eval('polySelectEdgesEveryN "edgeRing" 6')
        print("3 cycle modes selected.")
    elif size_components == 4:
        mel.eval('polySelectEdgesEveryN "edgeRing" 8')
        print("4 cycle modes selected.")
    elif size_components == 5:
        mel.eval('polySelectEdgesEveryN "edgeRing" 10')
        print("5 cycle modes selected.")
    elif size_components == 6:
        mel.eval('polySelectEdgesEveryN "edgeRing" 12')
        print("6 cycle modes selected.")
    elif size_components == 7:
        mel.eval('polySelectEdgesEveryN "edgeRing" 14')
        print("7 cycle modes selected.")
    elif size_components == 8:
        mel.eval('polySelectEdgesEveryN "edgeRing" 16')
        print("8 cycle modes selected.")
    elif size_components > 8:
        cmds.error("Please select 8 or fewer edges.")

def create_select_edges_window():
    window_name = "IntervalSelectEdges"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)
    
    window = cmds.window(window_name, title="Interval Select Edges", toolbox=True, 
                         widthHeight=(300, 150), 
                         sizeable=True,
                         backgroundColor=(0.25, 0.25, 0.25))
    
    main_layout = cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Select edge(s) and click Execute", height=50, width=250, parent=main_layout)
    cmds.button(label="Select", command=lambda x: select_edges(), width=250, height=30, backgroundColor=(0.53, 0.81, 0.98), parent=main_layout)
    
    cmds.window(window, edit=True, widthHeight=(300, 150))  # Set the window size again after creating contents
    cmds.showWindow(window)

# Add a new function as the entry point for the module
def show():
    create_select_edges_window()

# If the script is run directly (not imported as a module), show the window
if __name__ == "__main__":
    show()