#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel

def save_setting():
    threshold = cmds.floatSliderGrp(SamePositionSelector_UI_Threshold_FS, q=True, v=True)
    check_bb = cmds.checkBox(SamePositionSelector_UI_CheckBB_CB, q=True, v=True)
    unselect = cmds.checkBox(SamePositionSelector_UI_UnselectBB_CB, q=True, v=True)
    cmds.optionVar(fv=("AriSamePositionS_Threshold", threshold))
    cmds.optionVar(iv=("AriSamePositionS_CheckBB", check_bb))
    cmds.optionVar(iv=("AriSamePositionS_Unselect", unselect))

def vector_much(val_a, val_b, gosa):
    return (val_a[0] <= val_b[0] + gosa and val_a[0] >= val_b[0] - gosa and
            val_a[1] <= val_b[1] + gosa and val_a[1] >= val_b[1] - gosa and
            val_a[2] <= val_b[2] + gosa and val_a[2] >= val_b[2] - gosa)

def check_bounding_box(object_list_name):
    gosa = cmds.floatSliderGrp(SamePositionSelector_UI_Threshold_FS, q=True, v=True)
    object_list_bb_min = [cmds.getAttr(obj + ".boundingBoxMin")[0] for obj in object_list_name]
    object_list_bb_max = [cmds.getAttr(obj + ".boundingBoxMax")[0] for obj in object_list_name]
    
    same_obj_list = []
    for i in range(len(object_list_name)):
        bb_min_a, bb_max_a = object_list_bb_min[i], object_list_bb_max[i]
        local_counter = 0
        for j in range(i + 1, len(object_list_name)):
            if object_list_name[j] in same_obj_list:
                continue
            bb_min_b, bb_max_b = object_list_bb_min[j], object_list_bb_max[j]
            if vector_much(bb_min_a, bb_min_b, gosa) and vector_much(bb_max_a, bb_max_b, gosa):
                if local_counter == 0:
                    same_obj_list.append(object_list_name[i])
                same_obj_list.append(object_list_name[j])
                local_counter += 1
        if local_counter != 0:
            same_obj_list.append(";")
    return same_obj_list

def select_list(obj_list):
    unselect_true = cmds.checkBox(SamePositionSelector_UI_UnselectBB_CB, q=True, v=True)
    first_true = unselect_true
    select_list = []
    for obj in obj_list:
        if obj != ";":
            if first_true:
                first_true = False
                continue
            select_list.append(obj)
        else:
            if unselect_true:
                first_true = True
    cmds.select(select_list)

def same_position_selector_select(*args):
    save_setting()
    bb_true = cmds.checkBox(SamePositionSelector_UI_CheckBB_CB, q=True, v=True)
    gosa = cmds.floatSliderGrp(SamePositionSelector_UI_Threshold_FS, q=True, v=True)
    object_list_name = cmds.ls(sl=True, tr=True)
    object_list_pos = [cmds.xform(obj, q=True, ws=True, piv=True)[:3] for obj in object_list_name]
    
    same_obj_list = []
    for i in range(len(object_list_name)):
        pos_a = object_list_pos[i]
        local_counter = 0
        for j in range(i + 1, len(object_list_name)):
            if object_list_name[j] in same_obj_list:
                continue
            pos_b = object_list_pos[j]
            if vector_much(pos_a, pos_b, gosa):
                if local_counter == 0:
                    same_obj_list.append(object_list_name[i])
                same_obj_list.append(object_list_name[j])
                local_counter += 1
        if local_counter != 0:
            same_obj_list.append(";")
    
    if bb_true:
        same_bounding_box_list = []
        pair_list = []
        for obj in same_obj_list:
            if obj == ";":
                same_bounding_box_list.extend(check_bounding_box(pair_list))
                pair_list = []
            else:
                pair_list.append(obj)
        same_obj_list = same_bounding_box_list
    
    select_list(same_obj_list)

def show():
    global SamePositionSelector_UI_Threshold_FS
    global SamePositionSelector_UI_CheckBB_CB
    global SamePositionSelector_UI_UnselectBB_CB
    
    threshold = 0.01
    check_bb = True
    unselect = True

    if cmds.optionVar(exists="AriSamePositionS_Threshold"):
        threshold = cmds.optionVar(q="AriSamePositionS_Threshold")
    if cmds.optionVar(exists="AriSamePositionS_CheckBB"):
        check_bb = cmds.optionVar(q="AriSamePositionS_CheckBB")
    if cmds.optionVar(exists="AriSamePositionS_Unselect"):
        unselect = cmds.optionVar(q="AriSamePositionS_Unselect")

    window_name = "SamePositionSelector"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    
    window = cmds.window(window_name, title="Same Position Selector", tlb=True, 
                         widthHeight=(300, 150), backgroundColor=(0.25, 0.25, 0.25),
                         sizeable=True)
    
    label_threshold = "Threshold"
    label_check_bb = "Check boundingbox"
    label_unselect = "Unselect first object"
    
    main_layout = cmds.columnLayout(adjustableColumn=True)
    
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(80, 220), adjustableColumn=2, parent=main_layout)
    cmds.text(label=label_threshold)
    SamePositionSelector_UI_Threshold_FS = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=0.1, fieldMinValue=0.0, fieldMaxValue=1000, value=threshold, precision=6)
    cmds.setParent('..')

    cmds.columnLayout(adjustableColumn=True, parent=main_layout)
    SamePositionSelector_UI_CheckBB_CB = cmds.checkBox(label=label_check_bb, value=check_bb)
    SamePositionSelector_UI_UnselectBB_CB = cmds.checkBox(label=label_unselect, value=unselect)
    cmds.setParent('..')

    cmds.separator(height=10, style='in', parent=main_layout)

    cmds.button(label="Select", command=same_position_selector_select, backgroundColor=(0.53, 0.81, 0.98), height=30, parent=main_layout)

    cmds.window(window, edit=True, widthHeight=(300, 150)) 
    cmds.showWindow(window)

if __name__ == "__main__":
    show()