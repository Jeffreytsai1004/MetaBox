"""
You can use this script for any commercial or non-commercial projects. You're not allowed to sell this script.
Author - Petar3D
Initial Release Date - 10.05.2023
Version - 1.0 (10.05.2023)
Version - 2.0 (02.11.2023) - Current

Description - Tool that allows you to build a temporary IK/FK setup on any rig, while preserving animation. Example - You select the controls for you arm FK chain (Shoulder, Elbow, Wrist),
and then click the "FK to IK" button to apply an IK setup on top of your original FK controls. You can also isolate the code from the UI so you can put it into a marking menu or on the shelf.
"""

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
#from math import isclose
from sys import exit

##################################################################################################################################################################################################################

# GENERAL FUNCTIONS
def get_timeline_start_end():  # ---------- DONE
    timeline_start = cmds.playbackOptions(min=True, q=True)
    timeline_end = cmds.playbackOptions(max=True, q=True)
    return timeline_start, timeline_end

def filter_list_unpack_brackets(*list):  # IF LIST HAS 1 ITEM, WE RETURN IT AS ITEM[0] TO REMOVE THE BRACKETS
    new_list = [item if len(item) > 1 else item[0] for item in list]
    return new_list

def create_control(name):
    points = [(-1, 0, -0), (1, 0, 0), (0, 0, 0), (0, 0, -1), (0, 0, 1), (0, 0, 0), (0, -1, 0), (0, 1, 0)]
    temp_control = cmds.curve(n=name, d=1, p=points)
    return temp_control

def apply_euler_filter(controls):
    apply_key_reducer = cmds.checkBoxGrp("ApplyKeyReducer_CheckBox", q=True, v1=True)
    key_reducer_intensity = cmds.floatFieldGrp("Intensity_FloatField", q=True, v1=True)
    for control in controls:
        cmds.select(control)
        cmds.filterCurve(control + ".translate", control + ".rotate", f="euler")
        if apply_key_reducer:
            cmds.filterCurve(control + ".translate", f="keyReducer", startTime=timeline_start, endTime=timeline_end, pm=1, pre=key_reducer_intensity)
            cmds.filterCurve(control + ".rotate", f="keyReducer", startTime=timeline_start, endTime=timeline_end, pm=1, pre=key_reducer_intensity + 10)

def hide_attributes(type, *controls):  # ---------- DONE
    for item in controls:
        for attr in ["." + type + "X", "." + type + "Y", "." + type + "Z"]:
            cmds.setAttr(item + attr, k=False, l=True, cb=False)

def hide_controls(*controls): # ---------- DONE
    for control in controls:
        cmds.setAttr(control + ".v", 0)

def set_control_color(objects, color):
    for obj in objects:
        cmds.setAttr(obj + ".overrideEnabled", 1)
        cmds.setAttr(obj + ".overrideColor", color)

def set_control_thickness(objects, value):
    for obj in objects:
        cmds.setAttr(obj + ".lineWidth", value)

def set_form_layout_coordinates(form_layout, name, top_coordinates, left_coordinates): # ---------- DONE
    #ADJUSTS THE POSITION OF THE UI FEATURES
    cmds.formLayout(form_layout, edit=True, attachForm=[(name, "top", top_coordinates), (name, "left", left_coordinates)])

def documentation():
    cmds.showHelp("https://petarpehchevski3d.gumroad.com/l/ikfkswitcher", a=True)

def assist_message(message, time, to_exit=True): # ---------- DONE
    #POPS UP A MESSAGE ON THE USER'S SCREEN TO INFORM THEM OF SOMETHING
    cmds.inViewMessage(amg="<hl>" + message + "<hl>", pos='midCenter', fade=True, fst=time, ck=True)
    if to_exit:
        exit()

def get_constraint_attribute(constraint_type):
    #SETS A KEY ON THE START AND END OF THE TIMELINE, SO THAT WE ENSURE THERE'S A BLEND NODE ALL THE TIME. IF THERE'S NO KEY BEFORE ADDING THE SETUP, THE SCRIPT WON'T APPLY A SWITCH ON THE BLEND NODE
    temp_attribute = []
    if constraint_type == "orient":
        temp_attribute = "rotate"
    elif constraint_type == "point":
        temp_attribute = "translate"
    elif constraint_type == "parent":
        temp_attribute = ["translate", "rotate"]
    return temp_attribute

def get_locked_attributes(control, attribute):   # ---------- OPTIMIZE
    #CHECK WHICH ATTRIBUTES ON THE CONTROL ARE LOCKED, SO AS TO KNOW WHICH ONES TO SKIP WHEN APPLYING CONSTRAINTS
    if attribute == "parent":
        translate_attributes = [".translateX", ".translateY", ".translateZ"]
        rotate_attributes = [".rotateX", ".rotateY", ".rotateZ"]

        locked_translate = [attr.lower()[-1:]   for attr in translate_attributes    if cmds.getAttr(control + attr, lock=True)]
        locked_rotate = [attr.lower()[-1:]   for attr in rotate_attributes    if cmds.getAttr(control + attr, lock=True)]

        locked_attributes = [locked_translate, locked_rotate]
    else:
        attributes = ["." + attribute + "X", "." + attribute + "Y", "." + attribute + "Z"]
        locked_attributes = [attr.lower()[-1:]   for attr in attributes    if cmds.getAttr(control + attr, lock=True)]

    return locked_attributes

def constraint(parent, child, type, mo=True): # ---------- DONE
    #CONSTRAINT SYSTEM
    try:
        locked_attributes = get_locked_attributes(child, type)
        if type == "parent":
            constraint = cmds.parentConstraint(parent, child, maintainOffset = mo, skipTranslate = locked_attributes[0], skipRotate = locked_attributes[1])
        if type == "translate":
            constraint = cmds.pointConstraint(parent, child, maintainOffset = mo, skip = locked_attributes)
        if type == "rotate":
            constraint = cmds.orientConstraint(parent, child, maintainOffset = mo, skip = locked_attributes)
    except RuntimeError:
        assist_message("Error: Your selected controls are already being influenced by some other source.", 5000)

    return constraint[0]

def check_negative_time_range(timelineStart, timelineEnd):
    # PREVENTS THE USER FROM APPLYING THE SETUP IN A NEGATIVE RANGE TIMELINE
    if timelineStart < 0 or timelineEnd < 0:
        assist_message("Error: You can't apply a locator setup on a negative time-range", 5000, True)

def get_timeline_range():
    aTimeSlider = mel.eval('$tmpVar=$gPlayBackSlider')
    timeline_start, timeline_end = cmds.timeControl(aTimeSlider, q=True, rangeArray=True)
    if 1 < (timeline_end - timeline_start):
        to_isolate_timeline = True
        timeline_end = timeline_end - 1
    else:
        to_isolate_timeline = False
        timeline_start, timeline_end = get_timeline_start_end()

    return timeline_start, timeline_end, to_isolate_timeline

####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######
def divide_influence(curve, first_value, second_value):
    cmds.setKeyframe(curve, t=(timeline_start, timeline_end), value=first_value)
    cmds.setKeyframe(curve, t=(timeline_start - 1, timeline_end + 1), value=second_value)

def get_constraint_blend_index(constraint, control):
    # WE'RE TRYING TO FIND THE INDEX AT THE END OF THE CONSTRAINT'S WEIGHT ATTRIBUTE. BECAUSE THERE COULD BE MANY CONSTRAINTS APPLIED ON THE SAME OBJECT, WE CAN'T ALWAYS KNOW WHAT THAT NUMBER WILL BE
    for item in cmds.listConnections(constraint, c=True):
        if "{0}.{1}W".format(constraint, control) in item:
            constraint_index = item[-1:]
    last_three_characters = constraint[-3:]
    blend_index = "".join([i for i in last_three_characters if i.isdigit()]) # SOMETIMES THE BLEND INDEX MAY BE 10, OR WHATEVER NUMBER, SO WE TAKE THE LAST 3 STRING AND SEE IF THEY'RE AN INT, IF THEY ARE WE CONCATENATE THEM
    return constraint_index, blend_index

def check_if_referenced(original_control, temp_control):
    # IF THE RIG IS REFERENCED, WE STORE THE NAME OF THE TEMP LOCATOR WITHOUT THE NAMESPACE, BECAUSE THE CONSTRAINT WE'LL INFLUENCE DON'T HAVE THE NAMESPACE INSIDE
    if cmds.referenceQuery(original_control, isNodeReferenced=True) or ":" in original_control:
        temp_control = temp_control.split(":")[-1:][0]
    return temp_control

def set_key_frame(constraint_type, control):
    temp_attribute = get_constraint_attribute(constraint_type.lower())
    # CHECKS TO SEE IF ORIGINAL CONTROL HAS ANY KEYS ON CURVES ALREADY, IF NOT IT PLACES THEM TO ACTIVATE THE BLEND INDEX
    if cmds.keyframe(control, at=temp_attribute, q=True) == None:
        cmds.setKeyframe(control, t=(timeline_start - 1, timeline_end + 1), at=temp_attribute)
    else:
        cmds.setKeyframe(control, t=(timeline_start - 1, timeline_end + 1), at=temp_attribute, i=True)

def isolate_constraint(constraints, temp_controls, original_controls, constraint_type):
    for constraint, temp_control, original_control in zip(constraints, temp_controls, original_controls):
        temp_control = check_if_referenced(original_control, temp_control)

        set_key_frame(constraint_type, original_control)

        constraint_index, blend_index = get_constraint_blend_index(constraint, temp_control)
        divide_influence(constraint + "." + temp_control + "W" + constraint_index, 1, 0)
        divide_influence(original_control + ".blend" + constraint_type + blend_index, 1, 0)

def isolate_visibility(controls, first_value, second_value):
    for control in controls:
        temp_shape_nodes = cmds.listRelatives(control, shapes=True, children=True, pa=True)
        if temp_shape_nodes != None:
            for temp_shape_node in temp_shape_nodes:
                divide_influence(temp_shape_node + ".v", first_value, second_value)

def delete_visibility_keys(*original_controls):
    if influence_visibility:
        for original_control in original_controls:
            temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
            if temp_shape_nodes != None:
                for temp_shape_node in temp_shape_nodes:
                    cmds.cutKey(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", option="keys")

####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######
####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######

######### CLEAR REDUNDANT KEYS ##########

def remove_unnecessary_keys(controls, attributes):
    tolerance = 0.000002
    for control in controls:
        for attr in attributes:
            for frame in range(int(timeline_start) + 1, int(timeline_end)):
                current_value = cmds.keyframe(control, q=True, t=(frame, frame), at=attr, eval=True)[0]
                previous_value = cmds.keyframe(control, q=True, t=(frame - 1, frame - 1), at=attr, eval=True)[0]
                #next_value = cmds.keyframe(control, q=True, t=(frame + 1, frame + 1), at=attr, eval=True)[0]
                if abs(current_value - previous_value) <= max(1e-09 * max(abs(current_value), abs(previous_value)), tolerance):
                    cmds.cutKey(control, time=(int(frame), int(frame)), at=attr, option="keys")

                # if isclose(current_value, previous_value, abs_tol=tolerance):
                #     cmds.cutKey(control, time=(int(frame), int(frame)), at=attr, option="keys")


################# APPLY TO BOTH ##############
def check_if_setup_exists(controls): # DONE
    for control in controls:
        if cmds.objExists(control + "_temp_IK_Name*") or cmds.objExists(control + "_temp_FK_Name*"):
            assist_message("Error: One or more selected controls are part of a pre-existing setup somewhere else on the timeline.", 5000)

def create_name_reference_groups(contents, suffix):   # ---------- DONE
    # #CREATES EMPTY GROUPS AS PROXIES FOR REFERENCING THE ACTUAL CONTROLS LATER ON
    timeline_mode_keyword = "ISR" if specific_timeline_mode == True else "NIF"

    # BECAUSE SOME NAMES HAVE DASH IN THE MIDDLE IF THEY'RE NOT UNIQUE NAMES, WE HAVE TO REPLACE IT WITH A NEW KEYWORD "_SEPARATOR_" FOR WHEN REFERENCING IT BACK WHEN BAKING.
    new_contents = [obj.replace("|", "_dash_")   if "|" in obj    else obj    for obj in contents]
    reference_grps = [cmds.group(n=obj + suffix + "_" + timeline_mode_keyword + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)), em=True)  for obj in new_contents]
    return reference_grps

def create_temp_grp(suffix, control_name, controls_to_group): # DONE
    temp_group = cmds.group(*controls_to_group, n=control_name + suffix)
    #cmds.lockNode(temp_group)

def match_rotation_order(parent, child):  # ---------- DONE
    # MATCHES THE ROTATION ORDER FROM THE ORIGINAL SELECTIONS ONTO THE TEMPORARY SETUP CONTROLS
    original_rotation_order = cmds.getAttr(parent + ".rotateOrder")
    cmds.setAttr(child + ".rotateOrder", original_rotation_order)

def match_control_scale(parent, children):
    # SCALE UP AN OBJECT TO ANOTHER ONE'S BOUNDING BOX SCALE, INCASE IT'S BEEN FREEZE-TRANSFORMED. THIS WAY THE USER DOESN'T HAVE TO MANUALLY ADJUST THE SIZE
    children = cmds.ls(children, flatten=True)
    if cmds.objectType(parent) == "joint":
        parentShapeNode = parent
    else:
        parentShapeNode = cmds.listRelatives(parent, shapes=True, children=True, pa=True)[0]

    xMin, yMin, zMin, xMax, yMax, zMax = cmds.exactWorldBoundingBox(parentShapeNode)
    parentDistanceX, parentDistanceY, parentDistanceZ = [xMax - xMin, yMax - yMin, zMax - zMin]

    for child in children:
        xMin, yMin, zMin, xMax, yMax, zMax = cmds.exactWorldBoundingBox(child)
        childDistanceX, childDistanceY, childDistanceZ = [xMax - xMin, yMax - yMin, zMax - zMin]

        # WE QUERY THE ORIGINAL SCALE OF THE LOCATOR
        originalX, originalY, originalZ = cmds.xform(child, q=True, s=True, r=True)

        divisionX, divisionY, divisionZ = [parentDistanceX / childDistanceX, parentDistanceY / childDistanceY, parentDistanceZ / childDistanceZ]

        # WE GET THE FINAL SCALE HERE, WE TAKE THE LONGEST NUMBER AND APPLY THAT TO ALL SCALE AXIS
        largestAxis = max([originalX * divisionX, originalY * divisionY, originalZ * divisionZ]) * 3
        newScale = [largestAxis, largestAxis, largestAxis]
        if cmds.objectType(parent) == "joint":
            if cmds.currentUnit(q=True) == "cm":
                cmds.xform(child, scale=(40, 40, 40))
            else:
                cmds.xform(child, scale=(0.7, 0.7, 0.7))
        else:
            cmds.xform(child, scale=newScale)


def check_anim_layer(controls):
    root_layer = cmds.animLayer(q=True, r=True)
    if root_layer:
        layer_list = cmds.animLayer(root_layer, q=True, c=True)
        if layer_list != None:
            for layer in layer_list:
                attribute_list = cmds.animLayer(layer, q=True, attribute=True)
                if attribute_list != None:
                    for attr in attribute_list:
                        for obj in controls:
                            if obj in attr:
                                assist_message("Warning: A control you've selected is in an anim layer. This may mess up the baking process and give bad results", 6000, False)

################# APPLY TO BOTH ##############

############# CREATE IK CONTROLS #################
def get_original_fk_controls(): # ---------- DONE
    fk_ctrls = cmds.ls(sl=True)
    if len(fk_ctrls) != 3:
        assist_message("Incorrect number of controls selected. To apply an IK setup, you need to select 3 FK controls, in order of parent to child.", 4000)
    cmds.select(cl=True)
    return fk_ctrls

def create_ik_joints(parent_ctrl, middle_ctrl, child_ctrl): # ---------- DONE
    parent_jnt = cmds.joint(n=parent_ctrl + "_temp_jnt")
    middle_jnt = cmds.joint(n=middle_ctrl + "_temp_jnt")
    child_jnt = cmds.joint(n=child_ctrl + "_temp_jnt")

    return parent_jnt, middle_jnt, child_jnt

def create_ik_controls(middle_ctrl, child_ctrl): # ---------- DONE
    ik_ctrl = create_control(child_ctrl + "_ik_ctrl" + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)))
    pole_vector_ctrl = create_control(middle_ctrl + "_pole_vector_ctrl" + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)))
    match_control_scale(child_ctrl, [ik_ctrl, pole_vector_ctrl])

    return ik_ctrl, pole_vector_ctrl


def create_ik_handle(parent_jnt, child_jnt, ik_ctrl):  # ---------- DONE
    # SETS PREFERRED ANGLE ON THE TEMP JOINT CHAIN, APPLIES AN IK HANDLE ON IT
    cmds.joint(parent_jnt, e=True, spa=True, ch=True)
    temp_IK_Handle = cmds.ikHandle(n=ik_ctrl + "_ikHandle1", sj=parent_jnt, ee=child_jnt)[0]
    cmds.matchTransform(temp_IK_Handle, child_jnt)
    return temp_IK_Handle

def create_temp_ik_controls(): # DONE
    # STORES ORIGINAL SELECTED FK CONTROLS INTO VARIABLES
    parent_ctrl, middle_ctrl, child_ctrl = fk_ctrls = get_original_fk_controls()
    check_if_setup_exists([parent_ctrl, middle_ctrl, child_ctrl])
    check_anim_layer(fk_ctrls)

    delete_visibility_keys(parent_ctrl, middle_ctrl, child_ctrl)
    # CREATES TEMPORARY IK JOINTS AND CONTROLS
    parent_jnt, middle_jnt, child_jnt = ik_jnts = create_ik_joints(parent_ctrl, middle_ctrl, child_ctrl)
    ik_ctrl, pole_vector_ctrl = ik_ctrls = create_ik_controls(middle_ctrl, child_ctrl)

    # CREATES EMPTY GROUPS FOR REFERENCING THE ORIGINAL CONTROLS WHEN BAKING/DELETING SETUPS
    ik_reference_grps = create_name_reference_groups([parent_ctrl, middle_ctrl, child_ctrl], "_temp_IK_Name")

    # STORES WHOLE SETUP IN GROUP
    create_temp_grp("_temp_IK_Group", parent_ctrl, [parent_jnt, ik_ctrl, pole_vector_ctrl, ik_reference_grps])

    return fk_ctrls, ik_jnts, ik_ctrls
############# CREATE IK CONTROLS #################



############## CREATES REVERSE CONSTRAINT SETUP/ POSITIONS THE CONTROLS IN PLACE ##################

# SNAPS THE TEMP CONTROLS TO THE POSITION OF THE ORIGINAL CONTROLS, BAKES THE ANIMATION DATA, THEN DELETES CONSTRAINTS
def create_reverse_constraint_setup_ik(parent, child):
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)
    match_rotation_order(parent, child)

    # POSITIONS THE NEW CONTROLS
    if "pole_vector_ctrl" not in child: ################## DON'T LIKE HOW I HAVE TO ADD THESE EXTRA CONDITIONALS IN HERE #####################
        cmds.matchTransform(child, parent, position=True, rotation=True)

    if "jnt" in child:
        cmds.makeIdentity(child, apply=True, t=True, r=True, s=True)

    # CONSTRAINTS ORIGINAL CONTROLS TO TEMPORARY, BAKES THE TEMP TO INHERIT ANIM DATA, DELETES CONSTRAINT, CONSTRAINTS TEMPORARY TO ORIGINAL
    temp_constraint = constraint(parent, child, "parent")
    cmds.bakeResults(child, t=(timeline_start, timeline_end), sb=bake_interval)
    cmds.delete(temp_constraint)

    if "pole_vector_ctrl" not in child:
        temp_constraint = constraint(child, parent, "rotate")

    return temp_constraint

def get_vector(position): # ---------- DONE
    return om.MVector(position[0], position[1], position[2])

def get_pole_vector_position(parent_jnt, middle_jnt, child_jnt): # ---------- DONE
    vector_parent = get_vector(cmds.xform(parent_jnt, q=True, t=True, ws=True))
    vector_middle = get_vector(cmds.xform(middle_jnt, q=True, t=True, ws=True))
    vector_child = get_vector(cmds.xform(child_jnt, q=True, t=True, ws=True))

    parent_to_child_vector = (vector_child - vector_parent)
    parent_to_middle_vector = (vector_middle - vector_parent)

    scale_value = (parent_to_child_vector * parent_to_middle_vector) / (parent_to_child_vector * parent_to_child_vector)
    parent_to_child_middle_point = parent_to_child_vector * scale_value + vector_parent

    parent_to_middle_length = (vector_middle - vector_parent).length()
    middle_to_child_length = (vector_child - vector_middle).length()
    total_length = parent_to_middle_length + middle_to_child_length

    pole_vector_position = (vector_middle - parent_to_child_middle_point).normal() * total_length + vector_middle

    return pole_vector_position

def set_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl, pole_vector_ctrl):
    for frame in range(int(timeline_start), int(timeline_end) + 1):
        cmds.currentTime(int(frame))
        pole_vector_position = get_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl)
        cmds.move(pole_vector_position.x, pole_vector_position.y, pole_vector_position.z, pole_vector_ctrl)
        cmds.setKeyframe(pole_vector_ctrl, time=(frame, frame), at="translate")


def set_temp_ik_controls_position(fk_ctrls, ik_jnts, ik_ctrls):
    parent_ctrl, middle_ctrl, child_ctrl = fk_ctrls
    ik_ctrl, pole_vector_ctrl = ik_ctrls
    parent_jnt, middle_jnt, child_jnt = ik_jnts

    # JOINTS
    temp_constraint = [create_reverse_constraint_setup_ik(parent, child)   for parent, child in zip(fk_ctrls, ik_jnts)]

    # IK CTRL
    ik_orient_constraint = create_reverse_constraint_setup_ik(child_jnt, ik_ctrl)

    # POLE-VECTOR
    set_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl, pole_vector_ctrl)
    #create_reverse_constraint_setup_ik(middle_jnt, pole_vector_ctrl)

    return temp_constraint, ik_orient_constraint
############## CREATES REVERSE CONSTRAINT SETUP/ POSITIONS THE CONTROLS IN PLACE ##################


#CREATES A TEMPORARY IK SET-UP BY SELECTING EXISTING FK CONTROLS
def fk_to_ik():
    global timeline_start, timeline_end, specific_timeline_mode, influence_visibility
    influence_visibility = cmds.checkBoxGrp("influence_visibility", q=True, v1=True)
    clear_keys = cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)
    cmds.autoKeyframe(state=True)

    timeline_start, timeline_end, specific_timeline_mode = get_timeline_range()
    check_negative_time_range(timeline_start, timeline_end)
    ###### CREATE CONTROLS ######
    [parent_ctrl, middle_ctrl, child_ctrl], [parent_jnt, middle_jnt, child_jnt], [ik_ctrl, pole_vector_ctrl] = fk_ctrls, ik_jnts, ik_ctrls = create_temp_ik_controls()
    ###### REPOSITION CONTROLS ######
    temp_constraints, ik_orient_constraint = set_temp_ik_controls_position(fk_ctrls, ik_jnts, ik_ctrls)

    # CREATES IK HANDLE, ADDS POLE VECTOR CONSTRAINTz
    cmds.currentTime(timeline_start)
    temp_ik_handle = create_ik_handle(parent_jnt, child_jnt, ik_ctrl)
    cmds.parent(temp_ik_handle, ik_ctrl, s=True)
    pole_vector_constraint = cmds.poleVectorConstraint(pole_vector_ctrl, temp_ik_handle)

    # MAKES THE IK SETUP WORLD-SPACE - WHEN SHOULDER ROTATES THE IK TRANSLATES BUT DOESN'T ROTATE
    point_constraint = constraint(parent_ctrl, parent_jnt, "translate")

    ####### ISOLATE VISIBILITY ######
    if specific_timeline_mode:
        if influence_visibility:
            isolate_visibility([parent_ctrl, middle_ctrl, child_ctrl], 0, 1)
        isolate_visibility([ik_ctrl, pole_vector_ctrl], 1, 0)
        ####### ISOLATE CONSTRAINT ######
        isolate_constraint(temp_constraints, ik_jnts, fk_ctrls, "Orient")
    else:
        if influence_visibility:
            for original_control in fk_ctrls:
                temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
                if temp_shape_nodes != None:
                    for temp_shape_node in temp_shape_nodes:
                        if cmds.getAttr(temp_shape_node + ".v", se=True) == True or cmds.getAttr(temp_shape_node + ".v", l=True) == True:
                            cmds.setAttr(temp_shape_node + ".v", 0)


    #isolate_constraint([ik_orient_constraint], [ik_ctrl], [child_jnt], "Orient")
    #isolate_constraint([point_constraint], [parent_ctrl], [parent_jnt], "Point")

    ############################# - DONE - #############################

    #CLEAN-UP   # - COULD MAKE INTO ITS OWN FUNCTION
    hide_controls(parent_jnt, temp_ik_handle)
    cmds.cutKey(pole_vector_ctrl, t=(timeline_start, timeline_end), at="rotate", option="keys")
    hide_attributes("rotate", pole_vector_ctrl)
    hide_attributes("scale", ik_ctrl, pole_vector_ctrl)
    set_control_color(ik_ctrls, 18)
    set_control_thickness(ik_ctrls, 2)
    #set_control_thickness([ik_ctrl, pole_vector_ctrl], 2)
    #cmds.keyTangent(ik_ctrls, e=True, itt="auto", ott="auto")
    apply_euler_filter(ik_ctrls)
    if clear_keys:
        remove_unnecessary_keys([ik_ctrl], ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"])
        remove_unnecessary_keys([pole_vector_ctrl], ["translateX", "translateY", "translateZ"])

    cmds.select(ik_ctrl)


################ GET ORIGINAL CONTROLS ####################
def get_original_ik_controls():
    ik_ctrls = cmds.ls(sl=True)
    if len(ik_ctrls) != 2:
        assist_message("Incorrect number of controls selected. To apply an FK setup, you need to select the Pole Vector first and then the IK Control, in order.", 4000)
    cmds.select(cl=True)
    return ik_ctrls

def get_ik_handle(pole_vector): # ----- NOT DONE, ADD MORE CONDITIONALS
    #FROM THE POLE VECTOR, WE DERIVE THE SELECTION OF THE PARENT AND MIDDLE JOINT THAT THE IK HANDLE INFLUENCES, AND STORE THEM IN VARIABLES
    cmds.select(pole_vector, hi=True)
    pole_vector_hierarchy = cmds.ls(sl=True)

    for obj in pole_vector_hierarchy:
        poleVectorConstraint = cmds.listConnections(obj, type = "poleVectorConstraint")
        ik_handle = cmds.listConnections(poleVectorConstraint, type = "ikHandle")
        if ik_handle != None:
            break
    if ik_handle == None:
        keywords = "_".join(pole_vector.split("_")[:3])
        ik_handle = cmds.ls(keywords + "*", type="ikHandle")
    if ik_handle == None:
        keywords = "_".join(pole_vector.split("_")[:2])
        ik_handle = cmds.ls(keywords + "*", type="ikHandle")

    if ik_handle == None or len(ik_handle) == 0:
        assist_message("Couldn't obtain IK handle from the rig. Selection order must be Pole Vector first, then IK control. If that doesn't work, this feature is incompatible with this rig.", 4000)
    return ik_handle[0]

def get_ik_handle_joints(ik_handle):
    parent_jnt, middle_jnt = cmds.ikHandle(ik_handle, q=True, jl=True)
    return parent_jnt, middle_jnt

def get_original_controls():
    # SEPARATES THE SELECTED CONTROLS INTO THEIR OWN VARIABLES
    pole_vector, ik_ctrl = get_original_ik_controls()
    check_if_setup_exists([pole_vector, ik_ctrl])
    ik_handle = get_ik_handle(pole_vector)
    parent_jnt, middle_jnt = get_ik_handle_joints(ik_handle)

    return pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt
################ GET ORIGINAL CONTROLS ####################

################ CREATE TEMP CONTROLS ####################
def create_fk_controls(*controls):
    fk_ctrls = [create_control(control + "_temp_FK_CTRL") for control in controls]
    fk_ctrls_grps = [cmds.group(fk_ctrl, n=fk_ctrl + "_GRP") for fk_ctrl in fk_ctrls]
    return filter_list_unpack_brackets(fk_ctrls_grps, fk_ctrls)

def create_parent_hierarchy_offsets_controls(offsets, controls):
    # SHIFTS THE OFFSETS ELEMENTS SO THAT THE SECOND OFFSET MATCHES THE FIRST CONTROL AND WE PROPERLY PARENT THEM
    for offset, control in zip((offsets[1:] + offsets[:1])[:-1], controls[:-1]):
        cmds.parent(offset, control)

def create_new_fk_controls(pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt):
    # CREATE 3 TEMP LOCATORS, ADD A GROUP ON TOP OF THEM AND PARENT THEM TO EACH OTHER
    fk_ctrls_grps, fk_ctrls = create_fk_controls(parent_jnt, middle_jnt, ik_ctrl, pole_vector)
    temp_parent_FK_CTRL_GRP, temp_middle_FK_CTRL_GRP, temp_child_FK_CTRL_GRP, temp_poleVector_CTRL_GRP = fk_ctrls_grps
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls
    match_control_scale(ik_ctrl, [temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL])

    create_parent_hierarchy_offsets_controls(fk_ctrls_grps, fk_ctrls)
    cmds.parent(temp_poleVector_CTRL_GRP, temp_parent_FK_CTRL) # THE PREVIOUS FUNCTION DOESN'T PLACE THE TEMP POLE VECTOR UNDER THE RIGHT PARENT, SO HERE WE ADJUST THAT

    # CREATES NAME REFERENCE GROUPS FOR ALL ORIGINAL CONTROLS THAT NEED TO BE BAKED WHEN DELETING THE SETUP, PLACES ALL THE CONTENTS IN A NEW TEMP GROUP
    reference_grps = create_name_reference_groups([ik_ctrl, pole_vector, ik_handle], "_temp_FK_Name")
    create_temp_grp("_temp_FK_Group", parent_jnt, [temp_parent_FK_CTRL_GRP, reference_grps])

    return fk_ctrls_grps, fk_ctrls
################ CREATE TEMP CONTROLS ####################

################# CREATES THE REVERSE CONSTRAINT SETUP ##################

#SNAPS THE TEMP CONTROLS TO THE POSITION OF THE ORIGINAL CO NTROLS, BAKES THE ANIMATION DATA, THEN DELETES CONSTRAINTS
def create_reverse_constraint_setup_fk(parent, group, child):
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)

    cmds.matchTransform(group, parent, position=True, rotation=True)
    temp_constraint = constraint(parent, child, "parent", True)

    cmds.bakeResults(child, t=(timeline_start, timeline_end), simulation=False, sb=bake_interval)
    cmds.delete(temp_constraint)

def reverse_constraints_fk(fk_ctrls, ik_ctrl, pole_vector, parent_jnt, middle_jnt):
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls
    # REVERSE CONSTRAINT FROM THE TEMP CONTROLS TO THE ORIGINALS
    parent_constraint = constraint(temp_parent_FK_CTRL, parent_jnt, "rotate")
    middle_constraint = constraint(temp_middle_FK_CTRL, middle_jnt, "rotate")
    child_constraint = constraint(temp_child_FK_CTRL, ik_ctrl, "parent")

    point_constraint = constraint(parent_jnt, temp_parent_FK_CTRL, "translate")  # WHEN YOU ROTATE CLAVICLE, NEW PARENT CONTROL TRANSLATES
    parent_constraint_two = constraint(temp_middle_FK_CTRL, temp_poleVector_CTRL, "parent")  # MAKES THE NEW POLE VECTOR FOLLOW THE PARENT CONTROL
    point_constraint_two = constraint(temp_poleVector_CTRL, pole_vector, "translate")  # MAKES THE OG POLE VECTOR FOLLOW THE NEW ONE

    return parent_constraint, middle_constraint, child_constraint, point_constraint, parent_constraint_two, point_constraint_two
################# CREATES THE REVERSE CONSTRAINT SETUP ##################


#CREATES A TEMPORARY FK SET-UP BY SELECTING EXISTING IK CONTROLS
def ik_to_fk():
    global timeline_start, timeline_end, specific_timeline_mode, influence_visibility
    influence_visibility = cmds.checkBoxGrp("influence_visibility", q=True, v1=True)
    clear_keys = cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)

    cmds.autoKeyframe(state=True)
    timeline_start, timeline_end, specific_timeline_mode = get_timeline_range()
    check_negative_time_range(timeline_start, timeline_end)

    pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt = get_original_controls()
    check_anim_layer([pole_vector, ik_ctrl])
    delete_visibility_keys(pole_vector, ik_ctrl)

    fk_ctrls_grps, fk_ctrls = create_new_fk_controls(pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt)
    temp_parent_FK_CTRL_GRP, temp_middle_FK_CTRL_GRP, temp_child_FK_CTRL_GRP, temp_poleVector_CTRL_GRP = fk_ctrls_grps
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls

    match_rotation_order(ik_ctrl, temp_parent_FK_CTRL)
    match_rotation_order(ik_ctrl, temp_middle_FK_CTRL)
    match_rotation_order(ik_ctrl, temp_child_FK_CTRL)
    ############################# - DONE - #############################


    create_reverse_constraint_setup_fk(parent_jnt, temp_parent_FK_CTRL_GRP, temp_parent_FK_CTRL)
    create_reverse_constraint_setup_fk(middle_jnt, temp_middle_FK_CTRL_GRP, temp_middle_FK_CTRL)
    create_reverse_constraint_setup_fk(ik_ctrl, temp_child_FK_CTRL_GRP, temp_child_FK_CTRL)
    create_reverse_constraint_setup_fk(pole_vector, temp_poleVector_CTRL_GRP, temp_poleVector_CTRL) # THIS LOCATOR LACHES ONTO THE OG POLE VECTOR - SO WE KNOW HOW TO BAKE THE OG POLE VECTOR IN THE END

    parent_constraint, middle_constraint, child_constraint, point_constraint, parent_constraint_two, point_constraint_two = reverse_constraints_fk(fk_ctrls, ik_ctrl, pole_vector, parent_jnt, middle_jnt)

    # ISOLATE VISIBILITY #
    if specific_timeline_mode:
        if influence_visibility:
            isolate_visibility([ik_ctrl, pole_vector], 0, 1)
        isolate_visibility([temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL], 1, 0)
        # ISOLATE CONSTRAINT
        isolate_constraint([parent_constraint, middle_constraint], [temp_parent_FK_CTRL, temp_middle_FK_CTRL], [parent_jnt, middle_jnt], "Orient")
        isolate_constraint([child_constraint], [temp_child_FK_CTRL], [ik_ctrl], "Parent")

        isolate_constraint([point_constraint], [parent_jnt], [temp_parent_FK_CTRL], "Point")
        isolate_constraint([parent_constraint_two], [temp_middle_FK_CTRL], [temp_poleVector_CTRL], "Parent")
        isolate_constraint([point_constraint_two], [temp_poleVector_CTRL], [pole_vector], "Point")
        divide_influence(ik_handle + ".ikBlend", 0, 1)
    else:
        cmds.setAttr(ik_handle + ".ikBlend", 0)
        if influence_visibility:
            for original_control in [ik_ctrl, pole_vector]:
                temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
                if temp_shape_nodes != None:
                    for temp_shape_node in temp_shape_nodes:
                        if cmds.getAttr(temp_shape_node + ".v", se=True) == True or cmds.getAttr(temp_shape_node + ".v", l=True) == True:
                            cmds.setAttr(temp_shape_node + ".v", 0)

    #CLEAN-UP
    hide_controls(temp_poleVector_CTRL)
    cmds.cutKey(fk_ctrls, t=(timeline_start, timeline_end), at="translate", option="keys")
    hide_attributes("translate", temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL)
    hide_attributes("scale", temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL)
    set_control_color(fk_ctrls, 17)
    set_control_thickness(fk_ctrls, 2)

    #cmds.keyTangent(fk_ctrls, e=True, itt="auto", ott="auto")

    apply_euler_filter(fk_ctrls)
    if clear_keys:
        remove_unnecessary_keys(fk_ctrls, ["rotateX", "rotateY", "rotateZ"])

    cmds.select(ik_handle)

##############################################################################################################################################################################
###########################################################################################################################################################################################################
##############################################################################################################################################################################

def get_temporary_setup_selection():
    temp_Selection = cmds.ls(sl=True)
    if len(temp_Selection) == 0:
        assist_message("To delete a temporary setup, you have to select one of its controls.", 2500)
    return temp_Selection

def check_if_correct_selection(temp_Selection):
    if "FK_CTRL" in temp_Selection or "ik_ctrl" in temp_Selection or  "pole_vector_ctrl" in temp_Selection:
        pass
    else:
        assist_message("Incorrect selection: " + temp_Selection + " is not a part of any IK FK setup. To delete a setup, select one of its controls and then click the button.", 4500)

def get_group_selection(selection):
    cmds.select(selection)
    for i in range(6):
        cmds.pickWalk(d="up")
    temp_Group = cmds.ls(sl=True)[0]
    return temp_Group

def delete_visibility_keys_after_bake(original_control):
    temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
    if temp_shape_nodes != None:
        for temp_shape_node in temp_shape_nodes:
            cmds.cutKey(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", option="keys")
            cmds.setKeyframe(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", v=1)


def clean_up(i, attributes, group_Contents):
    global timeline_start, timeline_end
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)
    cmds.autoKeyframe(state=True)

    if group_Contents[i].split("_")[-3:-2][0] == "ISR":
        timeline_start, timeline_end = group_Contents[i].split("_")[-2:]
    else:
        timeline_start, timeline_end = get_timeline_start_end()

    original_control = "_".join(group_Contents[i].split("_")[:-6])
    if "_dash_" in original_control: # FOR IF THE CONTROL DOESN'T HAVE A UNIQUE NAME
        original_control = original_control.replace("_dash_", "|")
    cmds.bakeResults(original_control, t=(timeline_start, timeline_end), at=attributes, pok=True, sb=bake_interval)
    delete_visibility_keys_after_bake(original_control)

    apply_euler_filter([original_control])

    # #SETS VISIBILITY BACK
    # temp_shape_node = cmds.listRelatives(original_control, shapes=True, children=True)[0]
    # cmds.setAttr(temp_shape_node + ".v", 1)

    #YOU STORE THE TANGENT TYPE BEFORE THE BAKE, SO THAT INCASE IT WAS IN STEPPED, WE MAKE THE TANGENT STEPPED AGAIN CUZ OTHERWISE IT MESSES UP THE ELBOW AFTERWARDS
    return original_control

def delete_ik_blend(i, group_Contents):
    original_control = "_".join(group_Contents[i].split("_")[:-6])
    if "_dash_" in original_control:  # FOR IF THE CONTROL DOESN'T HAVE A UNIQUE NAME
        original_control = original_control.replace("_dash_", "|")
    cmds.cutKey(original_control, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="ikBlend", option="keys")
    cmds.setAttr(original_control + ".ikBlend", 1)
    return original_control


def delete_setup():
    clear_keys = cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)
    #BAKES THE PREVIOUS CONTROLS, CLEANS UP THE CURVES, DELETES CURRENT CONTROLS AND BRINGS BACK ORIGINALS
    temp_selection = get_temporary_setup_selection()
    for selection in temp_selection:
        if cmds.objExists(selection):
            check_if_correct_selection(selection)
            temp_group = get_group_selection(selection)
            group_contents = cmds.listRelatives(temp_group)

            if "temp_IK_Group" in temp_group:
                original_controls = [clean_up(i, ["rotate"], group_contents)    for i in range(3,6)]
                if clear_keys:
                    remove_unnecessary_keys(original_controls, ["rotateX", "rotateY", "rotateZ"])
                    # remove_unnecessary_keys([original_controls[0], original_controls[2]], ["rotate"])
                    # remove_unnecessary_keys([original_controls[1]], ["rotateX"])


            elif "temp_FK_Group" in temp_group:
                ik_ctrl, pole_vector_ctrl = [clean_up(i, ["translate", "rotate"], group_contents)    for i in range(1,3)]
                if clear_keys:
                    remove_unnecessary_keys([ik_ctrl], ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"])
                    remove_unnecessary_keys([pole_vector_ctrl], ["translateX", "translateY", "translateZ"])
                ik_handle = delete_ik_blend(3, group_contents)


    #cmds.lockNode(temp_group, l=False)
        if cmds.objExists(temp_group):
            cmds.delete(temp_group)

##############################################################################################################################################################################
###########################################################################################################################################################################################################
##############################################################################################################################################################################


#UI LOGIC
def run():
    if cmds.window("IK_FK_Switcher", ex=True):
        cmds.deleteUI("IK_FK_Switcher")


    cmds.window("IK_FK_Switcher", title="IK/FK Switcher, by Petar3D", wh=[360, 242], s=False)
    cmds.formLayout("ikfk_form_layout", numberOfDivisions=100, w=360, h=242)


    cmds.button("fkToIK_Button", l="FK to IK", recomputeSize = True, bgc=[0.6220035095750363, 0.8836957351033798, 1.0], h = 43, w = 100,  parent ="ikfk_form_layout", command=lambda *args:fk_to_ik(),
    ann="Applies a temporary IK setup on top of your existing FK chain.\nHow to use:  Select 3 FK controls, starting from the parent to the child, then click this button.")
    set_form_layout_coordinates("ikfk_form_layout", "fkToIK_Button", 16, 16)

    cmds.button("ikToFK_Button", l="IK to FK ", recomputeSize = True, bgc=[1.0, 1.0, 0.6220035095750363], h = 43, w = 100,  parent ="ikfk_form_layout", command=lambda *args:ik_to_fk(),
    ann="Applies a temporary FK setup on top of your existing IK chain.\nHow to use:  Select the pole vector and then the IK control, then click this button.")
    set_form_layout_coordinates("ikfk_form_layout", "ikToFK_Button", 16, 131)

    cmds.button("DeleteSetup_Button", l="Delete Setup", recomputeSize = True, bgc=[1.0, 0.6220035095750363, 0.6220035095750363], h = 43, w = 99,  parent ="ikfk_form_layout", command=lambda *args:delete_setup(),
    ann="Deletes the temporary IK/FK setups and brings back the original.\nHow to use:  Select a control from the current setup, then click this button.")
    set_form_layout_coordinates("ikfk_form_layout", "DeleteSetup_Button", 16, 246)


    cmds.checkBoxGrp("ApplyKeyReducer_CheckBox", l="Reduce Keys: ", ncb=1, l1="", cw=(1, 79.5), w=151, vr=False, parent="ikfk_form_layout",
    ann="When the animation bakes across, this feature reduces the amount of keyframes on your curves.")
    set_form_layout_coordinates("ikfk_form_layout", "ApplyKeyReducer_CheckBox", 105, 5)

    cmds.checkBoxGrp("remove_unnecessary_keys", l="Remove Keys With Same Values: ", ncb=1, l1="", cw = (1, 170), w = 190, vr=False, v1=False,  parent ="ikfk_form_layout",
    ann="When ticked on, after the bake, static channels get removed.\nStatic channels are curves like scaleX/Y/Z that get baked but have no changes to them across the timeparent_to_child_vector, so they're redundant and take up space.")
    set_form_layout_coordinates("ikfk_form_layout", "remove_unnecessary_keys", 133, 11)

    # cmds.floatSliderGrp("remove_keys_threshold", l="Threshold: ",  f=True, v=1, cw=(1, 60), w=240, min=1, max=500000,
    #                    parent="ikfk_form_layout",
    #                    ann="The higher the amount, the less keyframes you'll have when applying the key reducer,\nbut you lose out on how precisely the animation gets baked across.")
    # set_form_layout_coordinates("remove_keys_threshold", 210, 30)

    cmds.checkBoxGrp("influence_visibility", l="Hide Original Controls: ", ncb=1, l1="", cw=(1, 128), w=166,
                     vr=False, parent="ikfk_form_layout", v1=True,
                     ann="When ticked on, after the bake, static channels get removed.\nStatic channels are curves like scaleX/Y/Z that get baked but have no changes to them across the timeparent_to_child_vector, so they're redundant and take up space.")
    set_form_layout_coordinates("ikfk_form_layout", "influence_visibility", 160, 9)


    cmds.floatFieldGrp("Intensity_FloatField", l="Intensity: ", numberOfFields=1, v1=1.0,  cw = (1, 52), w = 137, parent ="ikfk_form_layout",
    ann="The higher the amount, the less keyframes you'll have when applying the key reducer,\nbut you lose out on how precisely the animation gets baked across.")
    set_form_layout_coordinates("ikfk_form_layout", "Intensity_FloatField", 102, 110)

    cmds.intFieldGrp("BakeInterval_IntField", l="Bake Interval: ", numberOfFields=1, v1=1, cw=(1, 85.0), w=198, parent="ikfk_form_layout")
    set_form_layout_coordinates("ikfk_form_layout", "BakeInterval_IntField", 75, 1)

    cmds.button("ExtraOptions_Button", l="Extra Options", recomputeSize=True,
                bgc=[0.6220035095750363, 1.0, 0.6656137941557946], h=34, w=90, parent="ikfk_form_layout",
                command=lambda *args:extraOptions())
    set_form_layout_coordinates("ikfk_form_layout", "ExtraOptions_Button", 194, 255)

    cmds.button("ik_fk_documentation", l="Documentation", recomputeSize=True,
                bgc=[0.8, 0.8, 0.8], h=34, w=100, parent="ikfk_form_layout",
                command=lambda *args:documentation())
    set_form_layout_coordinates("ikfk_form_layout", "ik_fk_documentation", 194, 16.5)

    # cmds.separator("Proxy_HRSeparator", hr=True,bgc=[0.6569924467841611, 0.6569924467841611, 0.6569924467841611], style="none", h = 3, w = 394)
    # set_form_layout_coordinates("ikfk_form_layout", "Proxy_HRSeparator", 63, -8)

    cmds.showWindow("IK_FK_Switcher")


def generateCode():
    # YOU SELECT ONE OF THREE OPTIONS FOR WHAT CODE YOU WANT TO ISOLATE FROM THE SCRIPT: FK TO IK, IK TO FK, DELETE SETUP.

    cmds.scrollField("GenerateCodeOutputWindow", e=True, cl=True)

    code = """
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

from sys import exit

bake_interval = """ + str(cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)) + """
apply_key_reducer = """ + str(cmds.checkBoxGrp("ApplyKeyReducer_CheckBox", q=True, v1=True)) + """
key_reducer_intensity = """ + str(cmds.floatFieldGrp("Intensity_FloatField", q=True, v1=True)) + """
clear_keys = """ + str(cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)) + """
influence_visibility = """ + str(cmds.checkBoxGrp("influence_visibility", q=True, v1=True)) + """


##################################################################################################################################################################################################################

# GENERAL FUNCTIONS
def get_timeline_start_end():  # ---------- DONE
    timeline_start = cmds.playbackOptions(min=True, q=True)
    timeline_end = cmds.playbackOptions(max=True, q=True)
    return timeline_start, timeline_end

def filter_list_unpack_brackets(*list):  # IF LIST HAS 1 ITEM, WE RETURN IT AS ITEM[0] TO REMOVE THE BRACKETS
    new_list = [item if len(item) > 1 else item[0] for item in list]
    return new_list

def create_control(name):
    points = [(-1, 0, -0), (1, 0, 0), (0, 0, 0), (0, 0, -1), (0, 0, 1), (0, 0, 0), (0, -1, 0), (0, 1, 0)]
    temp_control = cmds.curve(n=name, d=1, p=points)
    return temp_control

def apply_euler_filter(controls):
    apply_key_reducer = cmds.checkBoxGrp("ApplyKeyReducer_CheckBox", q=True, v1=True)
    key_reducer_intensity = cmds.floatFieldGrp("Intensity_FloatField", q=True, v1=True)
    for control in controls:
        cmds.select(control)
        cmds.filterCurve(control + ".translate", control + ".rotate", f="euler")
        if apply_key_reducer:
            cmds.filterCurve(control + ".translate", f="keyReducer", startTime=timeline_start, endTime=timeline_end, pm=1, pre=key_reducer_intensity)
            cmds.filterCurve(control + ".rotate", f="keyReducer", startTime=timeline_start, endTime=timeline_end, pm=1, pre=key_reducer_intensity + 10)

def hide_attributes(type, *controls):  # ---------- DONE
    for item in controls:
        for attr in ["." + type + "X", "." + type + "Y", "." + type + "Z"]:
            cmds.setAttr(item + attr, k=False, l=True, cb=False)

def hide_controls(*controls): # ---------- DONE
    for control in controls:
        cmds.setAttr(control + ".v", 0)

def set_control_color(objects, color):
    for obj in objects:
        cmds.setAttr(obj + ".overrideEnabled", 1)
        cmds.setAttr(obj + ".overrideColor", color)

def set_control_thickness(objects, value):
    for obj in objects:
        cmds.setAttr(obj + ".lineWidth", value)

def set_form_layout_coordinates(form_layout, name, top_coordinates, left_coordinates): # ---------- DONE
    #ADJUSTS THE POSITION OF THE UI FEATURES
    cmds.formLayout(form_layout, edit=True, attachForm=[(name, "top", top_coordinates), (name, "left", left_coordinates)])

def assist_message(message, time, to_exit=True): # ---------- DONE
    #POPS UP A MESSAGE ON THE USER'S SCREEN TO INFORM THEM OF SOMETHING
    cmds.inViewMessage(amg="<hl>" + message + "<hl>", pos='midCenter', fade=True, fst=time, ck=True)
    if to_exit:
        exit()

def get_constraint_attribute(constraint_type):
    #SETS A KEY ON THE START AND END OF THE TIMELINE, SO THAT WE ENSURE THERE'S A BLEND NODE ALL THE TIME. IF THERE'S NO KEY BEFORE ADDING THE SETUP, THE SCRIPT WON'T APPLY A SWITCH ON THE BLEND NODE
    temp_attribute = []
    if constraint_type == "orient":
        temp_attribute = "rotate"
    elif constraint_type == "point":
        temp_attribute = "translate"
    elif constraint_type == "parent":
        temp_attribute = ["translate", "rotate"]
    return temp_attribute

def get_locked_attributes(control, attribute):   # ---------- OPTIMIZE
    #CHECK WHICH ATTRIBUTES ON THE CONTROL ARE LOCKED, SO AS TO KNOW WHICH ONES TO SKIP WHEN APPLYING CONSTRAINTS
    if attribute == "parent":
        translate_attributes = [".translateX", ".translateY", ".translateZ"]
        rotate_attributes = [".rotateX", ".rotateY", ".rotateZ"]

        locked_translate = [attr.lower()[-1:]   for attr in translate_attributes    if cmds.getAttr(control + attr, lock=True)]
        locked_rotate = [attr.lower()[-1:]   for attr in rotate_attributes    if cmds.getAttr(control + attr, lock=True)]

        locked_attributes = [locked_translate, locked_rotate]
    else:
        attributes = ["." + attribute + "X", "." + attribute + "Y", "." + attribute + "Z"]
        locked_attributes = [attr.lower()[-1:]   for attr in attributes    if cmds.getAttr(control + attr, lock=True)]

    return locked_attributes

def constraint(parent, child, type, mo=True): # ---------- DONE
    #CONSTRAINT SYSTEM
    try:
        locked_attributes = get_locked_attributes(child, type)
        if type == "parent":
            constraint = cmds.parentConstraint(parent, child, maintainOffset = mo, skipTranslate = locked_attributes[0], skipRotate = locked_attributes[1])
        if type == "translate":
            constraint = cmds.pointConstraint(parent, child, maintainOffset = mo, skip = locked_attributes)
        if type == "rotate":
            constraint = cmds.orientConstraint(parent, child, maintainOffset = mo, skip = locked_attributes)
    except RuntimeError:
        assist_message("Error: Your selected controls are already being influenced by some other source.", 5000)


    return constraint[0]

def check_negative_time_range(timelineStart, timelineEnd):
    # PREVENTS THE USER FROM APPLYING THE SETUP IN A NEGATIVE RANGE TIMELINE
    if timelineStart < 0 or timelineEnd < 0:
        assist_message("Error: You can't apply a locator setup on a negative time-range", 5000, True)

def get_timeline_range():
    aTimeSlider = mel.eval('$tmpVar=$gPlayBackSlider')
    timeline_start, timeline_end = cmds.timeControl(aTimeSlider, q=True, rangeArray=True)
    if 1 < (timeline_end - timeline_start):
        to_isolate_timeline = True
        timeline_end = timeline_end - 1
    else:
        to_isolate_timeline = False
        timeline_start, timeline_end = get_timeline_start_end()

    return timeline_start, timeline_end, to_isolate_timeline

####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######
def divide_influence(curve, first_value, second_value):
    cmds.setKeyframe(curve, t=(timeline_start, timeline_end), value=first_value)
    cmds.setKeyframe(curve, t=(timeline_start - 1, timeline_end + 1), value=second_value)

def get_constraint_blend_index(constraint, control):
    # WE'RE TRYING TO FIND THE INDEX AT THE END OF THE CONSTRAINT'S WEIGHT ATTRIBUTE. BECAUSE THERE COULD BE MANY CONSTRAINTS APPLIED ON THE SAME OBJECT, WE CAN'T ALWAYS KNOW WHAT THAT NUMBER WILL BE
    for item in cmds.listConnections(constraint, c=True):
        if "{0}.{1}W".format(constraint, control) in item:
            constraint_index = item[-1:]
    blend_index = constraint[-1:]
    return constraint_index, blend_index

def check_if_referenced(original_control, temp_control):
    # IF THE RIG IS REFERENCED, WE STORE THE NAME OF THE TEMP LOCATOR WITHOUT THE NAMESPACE, BECAUSE THE CONSTRAINT WE'LL INFLUENCE DON'T HAVE THE NAMESPACE INSIDE
    if cmds.referenceQuery(original_control, isNodeReferenced=True) or ":" in original_control:
        temp_control = temp_control.split(":")[-1:][0]
    return temp_control

def set_key_frame(constraint_type, control):
    temp_attribute = get_constraint_attribute(constraint_type.lower())
    # CHECKS TO SEE IF ORIGINAL CONTROL HAS ANY KEYS ON CURVES ALREADY, IF NOT IT PLACES THEM TO ACTIVATE THE BLEND INDEX
    if cmds.keyframe(control, at=temp_attribute, q=True) == None:
        cmds.setKeyframe(control, t=(timeline_start - 1, timeline_end + 1), at=temp_attribute)
    else:
        cmds.setKeyframe(control, t=(timeline_start - 1, timeline_end + 1), at=temp_attribute, i=True)

def isolate_constraint(constraints, temp_controls, original_controls, constraint_type):
    for constraint, temp_control, original_control in zip(constraints, temp_controls, original_controls):
        temp_control = check_if_referenced(original_control, temp_control)

        set_key_frame(constraint_type, original_control)

        constraint_index, blend_index = get_constraint_blend_index(constraint, temp_control)
        divide_influence(constraint + "." + temp_control + "W" + constraint_index, 1, 0)
        divide_influence(original_control + ".blend" + constraint_type + blend_index, 1, 0)

def isolate_visibility(controls, first_value, second_value):
    for control in controls:
        temp_shape_nodes = cmds.listRelatives(control, shapes=True, children=True, pa=True)
        if temp_shape_nodes != None:
            for temp_shape_node in temp_shape_nodes:
                divide_influence(temp_shape_node + ".v", first_value, second_value)

def delete_visibility_keys(*original_controls):
    if influence_visibility:
        for original_control in original_controls:
            temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
            if temp_shape_nodes != None:
                for temp_shape_node in temp_shape_nodes:
                    cmds.cutKey(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", option="keys")

####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######
####### ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ############# ISOLATE ######

######### CLEAR REDUNDANT KEYS ##########

def remove_unnecessary_keys(controls, attributes):
    tolerance = 0.000002
    for control in controls:
        for attr in attributes:
            for frame in range(int(timeline_start) + 1, int(timeline_end)):
                current_value = cmds.keyframe(control, q=True, t=(frame, frame), at=attr, eval=True)[0]
                previous_value = cmds.keyframe(control, q=True, t=(frame - 1, frame - 1), at=attr, eval=True)[0]
                #next_value = cmds.keyframe(control, q=True, t=(frame + 1, frame + 1), at=attr, eval=True)[0]
                if abs(current_value - previous_value) <= max(1e-09 * max(abs(current_value), abs(previous_value)), tolerance):
                    cmds.cutKey(control, time=(int(frame), int(frame)), at=attr, option="keys")

                # if isclose(current_value, previous_value, abs_tol=tolerance):
                #     cmds.cutKey(control, time=(int(frame), int(frame)), at=attr, option="keys")


################# APPLY TO BOTH ##############
def check_if_setup_exists(controls): # DONE
    for control in controls:
        if cmds.objExists(control + "_temp_IK_Name*") or cmds.objExists(control + "_temp_FK_Name*"):
            assist_message("Error: One or more selected controls are part of a pre-existing setup somewhere else on the timeline.", 5000)

def create_name_reference_groups(contents, suffix):   # ---------- DONE
    # #CREATES EMPTY GROUPS AS PROXIES FOR REFERENCING THE ACTUAL CONTROLS LATER ON
    timeline_mode_keyword = "ISR" if specific_timeline_mode == True else "NIF"

    # BECAUSE SOME NAMES HAVE DASH IN THE MIDDLE IF THEY'RE NOT UNIQUE NAMES, WE HAVE TO REPLACE IT WITH A NEW KEYWORD "_SEPARATOR_" FOR WHEN REFERENCING IT BACK WHEN BAKING.
    new_contents = [obj.replace("|", "_dash_")   if "|" in obj    else obj    for obj in contents]
    reference_grps = [cmds.group(n=obj + suffix + "_" + timeline_mode_keyword + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)), em=True)  for obj in new_contents]
    return reference_grps

def create_temp_grp(suffix, control_name, controls_to_group): # DONE
    temp_group = cmds.group(*controls_to_group, n=control_name + suffix)
    #cmds.lockNode(temp_group)

def match_rotation_order(parent, child):  # ---------- DONE
    # MATCHES THE ROTATION ORDER FROM THE ORIGINAL SELECTIONS ONTO THE TEMPORARY SETUP CONTROLS
    original_rotation_order = cmds.getAttr(parent + ".rotateOrder")
    cmds.setAttr(child + ".rotateOrder", original_rotation_order)

def match_control_scale(parent, children):
    # SCALE UP AN OBJECT TO ANOTHER ONE'S BOUNDING BOX SCALE, INCASE IT'S BEEN FREEZE-TRANSFORMED. THIS WAY THE USER DOESN'T HAVE TO MANUALLY ADJUST THE SIZE
    children = cmds.ls(children, flatten=True)
    if cmds.objectType(parent) == "joint":
        parentShapeNode = parent
    else:
        parentShapeNode = cmds.listRelatives(parent, shapes=True, children=True, pa=True)[0]

    xMin, yMin, zMin, xMax, yMax, zMax = cmds.exactWorldBoundingBox(parentShapeNode)
    parentDistanceX, parentDistanceY, parentDistanceZ = [xMax - xMin, yMax - yMin, zMax - zMin]

    for child in children:
        xMin, yMin, zMin, xMax, yMax, zMax = cmds.exactWorldBoundingBox(child)
        childDistanceX, childDistanceY, childDistanceZ = [xMax - xMin, yMax - yMin, zMax - zMin]

        # WE QUERY THE ORIGINAL SCALE OF THE LOCATOR
        originalX, originalY, originalZ = cmds.xform(child, q=True, s=True, r=True)

        divisionX, divisionY, divisionZ = [parentDistanceX / childDistanceX, parentDistanceY / childDistanceY, parentDistanceZ / childDistanceZ]

        # WE GET THE FINAL SCALE HERE, WE TAKE THE LONGEST NUMBER AND APPLY THAT TO ALL SCALE AXIS
        largestAxis = max([originalX * divisionX, originalY * divisionY, originalZ * divisionZ]) * 3
        newScale = [largestAxis, largestAxis, largestAxis]
        if cmds.objectType(parent) == "joint":
            if cmds.currentUnit(q=True) == "cm":
                cmds.xform(child, scale=(40, 40, 40))
            else:
                cmds.xform(child, scale=(0.7, 0.7, 0.7))
        else:
            cmds.xform(child, scale=newScale)


def check_anim_layer(controls):
    root_layer = cmds.animLayer(q=True, r=True)
    if root_layer:
        layer_list = cmds.animLayer(root_layer, q=True, c=True)
        if layer_list != None:
            for layer in layer_list:
                attribute_list = cmds.animLayer(layer, q=True, attribute=True)
                if attribute_list != None:
                    for attr in attribute_list:
                        for obj in controls:
                            if obj in attr:
                                assist_message("Warning: A control you've selected is in an anim layer. This may mess up the baking process and give bad results", 6000, False)
"""

    if cmds.radioButtonGrp("GenerateCodeOptions_RadioB", q=True, select=True) == 1:
        code += """
############# CREATE IK CONTROLS #################
def get_original_fk_controls(): # ---------- DONE
    fk_ctrls = cmds.ls(sl=True)
    if len(fk_ctrls) != 3:
        assist_message("Incorrect number of controls selected. To apply an IK setup, you need to select 3 FK controls, in order of parent to child.", 4000)
    cmds.select(cl=True)
    return fk_ctrls

def create_ik_joints(parent_ctrl, middle_ctrl, child_ctrl): # ---------- DONE
    parent_jnt = cmds.joint(n=parent_ctrl + "_temp_jnt")
    middle_jnt = cmds.joint(n=middle_ctrl + "_temp_jnt")
    child_jnt = cmds.joint(n=child_ctrl + "_temp_jnt")

    return parent_jnt, middle_jnt, child_jnt

def create_ik_controls(middle_ctrl, child_ctrl): # ---------- DONE
    ik_ctrl = create_control(child_ctrl + "_ik_ctrl" + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)))
    pole_vector_ctrl = create_control(middle_ctrl + "_pole_vector_ctrl" + "_" + str(int(timeline_start)) + "_" + str(int(timeline_end)))
    match_control_scale(child_ctrl, [ik_ctrl, pole_vector_ctrl])

    return ik_ctrl, pole_vector_ctrl


def create_ik_handle(parent_jnt, child_jnt, ik_ctrl):  # ---------- DONE
    # SETS PREFERRED ANGLE ON THE TEMP JOINT CHAIN, APPLIES AN IK HANDLE ON IT
    cmds.joint(parent_jnt, e=True, spa=True, ch=True)
    temp_IK_Handle = cmds.ikHandle(n=ik_ctrl + "_ikHandle1", sj=parent_jnt, ee=child_jnt)[0]
    cmds.matchTransform(temp_IK_Handle, child_jnt)
    return temp_IK_Handle

def create_temp_ik_controls(): # DONE
    # STORES ORIGINAL SELECTED FK CONTROLS INTO VARIABLES """
        if len(cmds.ls(sl=True)) == 3:
            fk_ctrls = cmds.ls(sl=True)
            code += """
    parent_ctrl = """  "\"" + fk_ctrls[0] + "\"" """
    middle_ctrl = """ "\"" + fk_ctrls[1] + "\"" """
    child_ctrl = """ "\"" + fk_ctrls[2] + "\"" """
    fk_ctrls = parent_ctrl, middle_ctrl, child_ctrl
    cmds.select(cl=True)
    """
        elif len(cmds.ls(sl=True)) == 0:
            code += """
    parent_ctrl, middle_ctrl, child_ctrl = fk_ctrls = get_original_fk_controls() """
        else:
            assist_message(
                "Incorrect number of controls selected. For a specific IK setup, select 3 FK controls. For a generic setup, have no selections.",
                5000)

        code += """
    check_if_setup_exists([parent_ctrl, middle_ctrl, child_ctrl])
    check_anim_layer(fk_ctrls)

    delete_visibility_keys(parent_ctrl, middle_ctrl, child_ctrl)
    # CREATES TEMPORARY IK JOINTS AND CONTROLS
    parent_jnt, middle_jnt, child_jnt = ik_jnts = create_ik_joints(parent_ctrl, middle_ctrl, child_ctrl)
    ik_ctrl, pole_vector_ctrl = ik_ctrls = create_ik_controls(middle_ctrl, child_ctrl)

    # CREATES EMPTY GROUPS FOR REFERENCING THE ORIGINAL CONTROLS WHEN BAKING/DELETING SETUPS
    ik_reference_grps = create_name_reference_groups([parent_ctrl, middle_ctrl, child_ctrl], "_temp_IK_Name")

    # STORES WHOLE SETUP IN GROUP
    create_temp_grp("_temp_IK_Group", parent_ctrl, [parent_jnt, ik_ctrl, pole_vector_ctrl, ik_reference_grps])

    return fk_ctrls, ik_jnts, ik_ctrls
############# CREATE IK CONTROLS #################



############## CREATES REVERSE CONSTRAINT SETUP/ POSITIONS THE CONTROLS IN PLACE ##################

# SNAPS THE TEMP CONTROLS TO THE POSITION OF THE ORIGINAL CONTROLS, BAKES THE ANIMATION DATA, THEN DELETES CONSTRAINTS
def create_reverse_constraint_setup_ik(parent, child):
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)
    match_rotation_order(parent, child)

    # POSITIONS THE NEW CONTROLS
    if "pole_vector_ctrl" not in child: ################## DON'T LIKE HOW I HAVE TO ADD THESE EXTRA CONDITIONALS IN HERE #####################
        cmds.matchTransform(child, parent, position=True, rotation=True)

    if "jnt" in child:
        cmds.makeIdentity(child, apply=True, t=True, r=True, s=True)

    # CONSTRAINTS ORIGINAL CONTROLS TO TEMPORARY, BAKES THE TEMP TO INHERIT ANIM DATA, DELETES CONSTRAINT, CONSTRAINTS TEMPORARY TO ORIGINAL
    temp_constraint = constraint(parent, child, "parent")
    cmds.bakeResults(child, t=(timeline_start, timeline_end), sb=bake_interval)
    cmds.delete(temp_constraint)

    if "pole_vector_ctrl" not in child:
        temp_constraint = constraint(child, parent, "rotate")

    return temp_constraint

def get_vector(position): # ---------- DONE
    return om.MVector(position[0], position[1], position[2])

def get_pole_vector_position(parent_jnt, middle_jnt, child_jnt): # ---------- DONE
    vector_parent = get_vector(cmds.xform(parent_jnt, q=True, t=True, ws=True))
    vector_middle = get_vector(cmds.xform(middle_jnt, q=True, t=True, ws=True))
    vector_child = get_vector(cmds.xform(child_jnt, q=True, t=True, ws=True))

    parent_to_child_vector = (vector_child - vector_parent)
    parent_to_middle_vector = (vector_middle - vector_parent)

    scale_value = (parent_to_child_vector * parent_to_middle_vector) / (parent_to_child_vector * parent_to_child_vector)
    parent_to_child_middle_point = parent_to_child_vector * scale_value + vector_parent

    parent_to_middle_length = (vector_middle - vector_parent).length()
    middle_to_child_length = (vector_child - vector_middle).length()
    total_length = parent_to_middle_length + middle_to_child_length

    pole_vector_position = (vector_middle - parent_to_child_middle_point).normal() * total_length + vector_middle

    return pole_vector_position

def set_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl, pole_vector_ctrl):
    for frame in range(int(timeline_start), int(timeline_end) + 1):
        cmds.currentTime(int(frame))
        pole_vector_position = get_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl)
        cmds.move(pole_vector_position.x, pole_vector_position.y, pole_vector_position.z, pole_vector_ctrl)
        cmds.setKeyframe(pole_vector_ctrl, time=(frame, frame), at="translate")


def set_temp_ik_controls_position(fk_ctrls, ik_jnts, ik_ctrls):
    parent_ctrl, middle_ctrl, child_ctrl = fk_ctrls
    ik_ctrl, pole_vector_ctrl = ik_ctrls
    parent_jnt, middle_jnt, child_jnt = ik_jnts

    # JOINTS
    temp_constraint = [create_reverse_constraint_setup_ik(parent, child)   for parent, child in zip(fk_ctrls, ik_jnts)]

    # IK CTRL
    ik_orient_constraint = create_reverse_constraint_setup_ik(child_jnt, ik_ctrl)

    # POLE-VECTOR
    set_pole_vector_position(parent_ctrl, middle_ctrl, child_ctrl, pole_vector_ctrl)
    #create_reverse_constraint_setup_ik(middle_jnt, pole_vector_ctrl)

    return temp_constraint, ik_orient_constraint
############## CREATES REVERSE CONSTRAINT SETUP/ POSITIONS THE CONTROLS IN PLACE ##################


#CREATES A TEMPORARY IK SET-UP BY SELECTING EXISTING FK CONTROLS
def fk_to_ik():
    global timeline_start, timeline_end, specific_timeline_mode, influence_visibility
    influence_visibility = cmds.checkBoxGrp("influence_visibility", q=True, v1=True)
    clear_keys = cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)
    cmds.autoKeyframe(state=True)

    timeline_start, timeline_end, specific_timeline_mode = get_timeline_range()
    check_negative_time_range(timeline_start, timeline_end)
    ###### CREATE CONTROLS ######
    [parent_ctrl, middle_ctrl, child_ctrl], [parent_jnt, middle_jnt, child_jnt], [ik_ctrl, pole_vector_ctrl] = fk_ctrls, ik_jnts, ik_ctrls = create_temp_ik_controls()
    ###### REPOSITION CONTROLS ######
    temp_constraints, ik_orient_constraint = set_temp_ik_controls_position(fk_ctrls, ik_jnts, ik_ctrls)

    # CREATES IK HANDLE, ADDS POLE VECTOR CONSTRAINTz
    cmds.currentTime(timeline_start)
    temp_ik_handle = create_ik_handle(parent_jnt, child_jnt, ik_ctrl)
    cmds.parent(temp_ik_handle, ik_ctrl, s=True)
    pole_vector_constraint = cmds.poleVectorConstraint(pole_vector_ctrl, temp_ik_handle)

    # MAKES THE IK SETUP WORLD-SPACE - WHEN SHOULDER ROTATES THE IK TRANSLATES BUT DOESN'T ROTATE
    point_constraint = constraint(parent_ctrl, parent_jnt, "translate")

    ####### ISOLATE VISIBILITY ######
    if specific_timeline_mode:
        if influence_visibility:
            isolate_visibility([parent_ctrl, middle_ctrl, child_ctrl], 0, 1)
        isolate_visibility([ik_ctrl, pole_vector_ctrl], 1, 0)
        ####### ISOLATE CONSTRAINT ######
        isolate_constraint(temp_constraints, ik_jnts, fk_ctrls, "Orient")
    else:
        if influence_visibility:
            for original_control in fk_ctrls:
                temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
                if temp_shape_nodes != None:
                    for temp_shape_node in temp_shape_nodes:
                        if cmds.getAttr(temp_shape_node + ".v", se=True) == True or cmds.getAttr(temp_shape_node + ".v", l=True) == True:
                            cmds.setAttr(temp_shape_node + ".v", 0)


    #isolate_constraint([ik_orient_constraint], [ik_ctrl], [child_jnt], "Orient")
    #isolate_constraint([point_constraint], [parent_ctrl], [parent_jnt], "Point")

    ############################# - DONE - #############################

    #CLEAN-UP   # - COULD MAKE INTO ITS OWN FUNCTION
    hide_controls(parent_jnt, temp_ik_handle)
    cmds.cutKey(pole_vector_ctrl, t=(timeline_start, timeline_end), at="rotate", option="keys")
    hide_attributes("rotate", pole_vector_ctrl)
    hide_attributes("scale", ik_ctrl, pole_vector_ctrl)
    set_control_color(ik_ctrls, 18)
    set_control_thickness(ik_ctrls, 2)
    #set_control_thickness([ik_ctrl, pole_vector_ctrl], 2)
    #cmds.keyTangent(ik_ctrls, e=True, itt="auto", ott="auto")
    apply_euler_filter(ik_ctrls)
    if clear_keys:
        remove_unnecessary_keys([ik_ctrl], ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"])
        remove_unnecessary_keys([pole_vector_ctrl], ["translateX", "translateY", "translateZ"])

    cmds.select(ik_ctrl)

fk_to_ik()
    """
    elif cmds.radioButtonGrp("GenerateCodeOptions_RadioB", q=True, select=True) == 2:
        code += """

################ GET ORIGINAL CONTROLS ####################
def get_original_ik_controls():
    ik_ctrls = cmds.ls(sl=True)
    if len(ik_ctrls) != 2:
        assist_message("Incorrect number of controls selected. To apply an FK setup, you need to select the Pole Vector first and then the IK Control, in order.", 4000)
    cmds.select(cl=True)
    return ik_ctrls

def get_ik_handle(pole_vector): # ----- NOT DONE, ADD MORE CONDITIONALS
    #FROM THE POLE VECTOR, WE DERIVE THE SELECTION OF THE PARENT AND MIDDLE JOINT THAT THE IK HANDLE INFLUENCES, AND STORE THEM IN VARIABLES
    cmds.select(pole_vector, hi=True)
    pole_vector_hierarchy = cmds.ls(sl=True)

    for obj in pole_vector_hierarchy:
        poleVectorConstraint = cmds.listConnections(obj, type = "poleVectorConstraint")
        ik_handle = cmds.listConnections(poleVectorConstraint, type = "ikHandle")
        if ik_handle != None:
            break
    if ik_handle == None:
        keywords = "_".join(pole_vector.split("_")[:3])
        ik_handle = cmds.ls(keywords + "*", type="ikHandle")
    if ik_handle == None:
        keywords = "_".join(pole_vector.split("_")[:2])
        ik_handle = cmds.ls(keywords + "*", type="ikHandle")

    if ik_handle == None or len(ik_handle) == 0:
        assist_message("Couldn't obtain IK handle from the rig. Selection order must be Pole Vector first, then IK control. If that doesn't work, this feature is incompatible with this rig.", 4000)
    return ik_handle[0]

def get_ik_handle_joints(ik_handle):
    parent_jnt, middle_jnt = cmds.ikHandle(ik_handle, q=True, jl=True)
    return parent_jnt, middle_jnt

def get_original_controls():
    # SEPARATES THE SELECTED CONTROLS INTO THEIR OWN VARIABLES
    """
        if len(cmds.ls(sl=True)) == 2:
            ik_ctrls = cmds.ls(sl=True)
            code += """
    pole_vector = """ "\"" + ik_ctrls[0] + "\"" """
    ik_ctrl = """ "\"" + ik_ctrls[1] + "\"" """
    cmds.select(cl=True)
    """
        elif len(cmds.ls(sl=True)) == 0:
            code += """
    pole_vector, ik_ctrl = get_original_ik_controls()
    """
        else:
            assist_message(
                "Incorrect number of controls selected. For a specific FK setup, select the Pole Vector and IK Control in order. For a generic setup, have no selections.",
                5000)
        code += """
    check_if_setup_exists([pole_vector, ik_ctrl])
    ik_handle = get_ik_handle(pole_vector)
    parent_jnt, middle_jnt = get_ik_handle_joints(ik_handle)

    return pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt
################ GET ORIGINAL CONTROLS ####################

################ CREATE TEMP CONTROLS ####################
def create_fk_controls(*controls):
    fk_ctrls = [create_control(control + "_temp_FK_CTRL") for control in controls]
    fk_ctrls_grps = [cmds.group(fk_ctrl, n=fk_ctrl + "_GRP") for fk_ctrl in fk_ctrls]
    return filter_list_unpack_brackets(fk_ctrls_grps, fk_ctrls)

def create_parent_hierarchy_offsets_controls(offsets, controls):
    # SHIFTS THE OFFSETS ELEMENTS SO THAT THE SECOND OFFSET MATCHES THE FIRST CONTROL AND WE PROPERLY PARENT THEM
    for offset, control in zip((offsets[1:] + offsets[:1])[:-1], controls[:-1]):
        cmds.parent(offset, control)

def create_new_fk_controls(pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt):
    # CREATE 3 TEMP LOCATORS, ADD A GROUP ON TOP OF THEM AND PARENT THEM TO EACH OTHER
    fk_ctrls_grps, fk_ctrls = create_fk_controls(parent_jnt, middle_jnt, ik_ctrl, pole_vector)
    temp_parent_FK_CTRL_GRP, temp_middle_FK_CTRL_GRP, temp_child_FK_CTRL_GRP, temp_poleVector_CTRL_GRP = fk_ctrls_grps
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls
    match_control_scale(ik_ctrl, [temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL])

    create_parent_hierarchy_offsets_controls(fk_ctrls_grps, fk_ctrls)
    cmds.parent(temp_poleVector_CTRL_GRP, temp_parent_FK_CTRL) # THE PREVIOUS FUNCTION DOESN'T PLACE THE TEMP POLE VECTOR UNDER THE RIGHT PARENT, SO HERE WE ADJUST THAT

    # CREATES NAME REFERENCE GROUPS FOR ALL ORIGINAL CONTROLS THAT NEED TO BE BAKED WHEN DELETING THE SETUP, PLACES ALL THE CONTENTS IN A NEW TEMP GROUP
    reference_grps = create_name_reference_groups([ik_ctrl, pole_vector, ik_handle], "_temp_FK_Name")
    create_temp_grp("_temp_FK_Group", parent_jnt, [temp_parent_FK_CTRL_GRP, reference_grps])

    return fk_ctrls_grps, fk_ctrls
################ CREATE TEMP CONTROLS ####################

################# CREATES THE REVERSE CONSTRAINT SETUP ##################

#SNAPS THE TEMP CONTROLS TO THE POSITION OF THE ORIGINAL CO NTROLS, BAKES THE ANIMATION DATA, THEN DELETES CONSTRAINTS
def create_reverse_constraint_setup_fk(parent, group, child):
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)

    cmds.matchTransform(group, parent, position=True, rotation=True)
    temp_constraint = constraint(parent, child, "parent", True)

    cmds.bakeResults(child, t=(timeline_start, timeline_end), simulation=False, sb=bake_interval)
    cmds.delete(temp_constraint)

def reverse_constraints_fk(fk_ctrls, ik_ctrl, pole_vector, parent_jnt, middle_jnt):
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls
    # REVERSE CONSTRAINT FROM THE TEMP CONTROLS TO THE ORIGINALS
    parent_constraint = constraint(temp_parent_FK_CTRL, parent_jnt, "rotate")
    middle_constraint = constraint(temp_middle_FK_CTRL, middle_jnt, "rotate")
    child_constraint = constraint(temp_child_FK_CTRL, ik_ctrl, "parent")

    point_constraint = constraint(parent_jnt, temp_parent_FK_CTRL, "translate")  # WHEN YOU ROTATE CLAVICLE, NEW PARENT CONTROL TRANSLATES
    parent_constraint_two = constraint(temp_middle_FK_CTRL, temp_poleVector_CTRL, "parent")  # MAKES THE NEW POLE VECTOR FOLLOW THE PARENT CONTROL
    point_constraint_two = constraint(temp_poleVector_CTRL, pole_vector, "translate")  # MAKES THE OG POLE VECTOR FOLLOW THE NEW ONE

    return parent_constraint, middle_constraint, child_constraint, point_constraint, parent_constraint_two, point_constraint_two
################# CREATES THE REVERSE CONSTRAINT SETUP ##################


#CREATES A TEMPORARY FK SET-UP BY SELECTING EXISTING IK CONTROLS
def ik_to_fk():
    global timeline_start, timeline_end, specific_timeline_mode, influence_visibility
    influence_visibility = cmds.checkBoxGrp("influence_visibility", q=True, v1=True)
    clear_keys = cmds.checkBoxGrp("remove_unnecessary_keys", q=True, v1=True)

    cmds.autoKeyframe(state=True)
    timeline_start, timeline_end, specific_timeline_mode = get_timeline_range()
    check_negative_time_range(timeline_start, timeline_end)

    pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt = get_original_controls()
    check_anim_layer([pole_vector, ik_ctrl])
    delete_visibility_keys(pole_vector, ik_ctrl)

    fk_ctrls_grps, fk_ctrls = create_new_fk_controls(pole_vector, ik_ctrl, ik_handle, parent_jnt, middle_jnt)
    temp_parent_FK_CTRL_GRP, temp_middle_FK_CTRL_GRP, temp_child_FK_CTRL_GRP, temp_poleVector_CTRL_GRP = fk_ctrls_grps
    temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL, temp_poleVector_CTRL = fk_ctrls

    match_rotation_order(ik_ctrl, temp_parent_FK_CTRL)
    match_rotation_order(ik_ctrl, temp_middle_FK_CTRL)
    match_rotation_order(ik_ctrl, temp_child_FK_CTRL)
    ############################# - DONE - #############################


    create_reverse_constraint_setup_fk(parent_jnt, temp_parent_FK_CTRL_GRP, temp_parent_FK_CTRL)
    create_reverse_constraint_setup_fk(middle_jnt, temp_middle_FK_CTRL_GRP, temp_middle_FK_CTRL)
    create_reverse_constraint_setup_fk(ik_ctrl, temp_child_FK_CTRL_GRP, temp_child_FK_CTRL)
    create_reverse_constraint_setup_fk(pole_vector, temp_poleVector_CTRL_GRP, temp_poleVector_CTRL) # THIS LOCATOR LACHES ONTO THE OG POLE VECTOR - SO WE KNOW HOW TO BAKE THE OG POLE VECTOR IN THE END

    parent_constraint, middle_constraint, child_constraint, point_constraint, parent_constraint_two, point_constraint_two = reverse_constraints_fk(fk_ctrls, ik_ctrl, pole_vector, parent_jnt, middle_jnt)

    # ISOLATE VISIBILITY #
    if specific_timeline_mode:
        if influence_visibility:
            isolate_visibility([ik_ctrl, pole_vector], 0, 1)
        isolate_visibility([temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL], 1, 0)
        # ISOLATE CONSTRAINT
        isolate_constraint([parent_constraint, middle_constraint], [temp_parent_FK_CTRL, temp_middle_FK_CTRL], [parent_jnt, middle_jnt], "Orient")
        isolate_constraint([child_constraint], [temp_child_FK_CTRL], [ik_ctrl], "Parent")

        isolate_constraint([point_constraint], [parent_jnt], [temp_parent_FK_CTRL], "Point")
        isolate_constraint([parent_constraint_two], [temp_middle_FK_CTRL], [temp_poleVector_CTRL], "Parent")
        isolate_constraint([point_constraint_two], [temp_poleVector_CTRL], [pole_vector], "Point")
        divide_influence(ik_handle + ".ikBlend", 0, 1)
    else:
        cmds.setAttr(ik_handle + ".ikBlend", 0)
        if influence_visibility:
            for original_control in [ik_ctrl, pole_vector]:
                temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
                if temp_shape_nodes != None:
                    for temp_shape_node in temp_shape_nodes:
                        if cmds.getAttr(temp_shape_node + ".v", se=True) == True or cmds.getAttr(temp_shape_node + ".v", l=True) == True:
                            cmds.setAttr(temp_shape_node + ".v", 0)

    #CLEAN-UP
    hide_controls(temp_poleVector_CTRL)
    cmds.cutKey(fk_ctrls, t=(timeline_start, timeline_end), at="translate", option="keys")
    hide_attributes("translate", temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL)
    hide_attributes("scale", temp_parent_FK_CTRL, temp_middle_FK_CTRL, temp_child_FK_CTRL)
    set_control_color(fk_ctrls, 17)
    set_control_thickness(fk_ctrls, 2)

    #cmds.keyTangent(fk_ctrls, e=True, itt="auto", ott="auto")

    apply_euler_filter(fk_ctrls)
    if clear_keys:
        remove_unnecessary_keys(fk_ctrls, ["rotateX", "rotateY", "rotateZ"])

    cmds.select(temp_parent_FK_CTRL)

ik_to_fk()

"""
    elif cmds.radioButtonGrp("GenerateCodeOptions_RadioB", q=True, select=True) == 3:
        code += """ 

def get_temporary_setup_selection():
    temp_Selection = cmds.ls(sl=True)
    if len(temp_Selection) == 0:
        assist_message("To delete a temporary setup, you have to select one of its controls.", 2500)
    return temp_Selection

def check_if_correct_selection(temp_Selection):
    if "FK_CTRL" in temp_Selection or "ik_ctrl" in temp_Selection or  "pole_vector_ctrl" in temp_Selection:
        pass
    else:
        assist_message("Incorrect selection: " + temp_Selection + " is not a part of any IK FK setup. To delete a setup, select one of its controls and then click the button.", 4500)

def get_group_selection(selection):
    cmds.select(selection)
    for i in range(6):
        cmds.pickWalk(d="up")
    temp_Group = cmds.ls(sl=True)[0]
    return temp_Group

def delete_visibility_keys_after_bake(original_control):
    temp_shape_nodes = cmds.listRelatives(original_control, shapes=True, children=True, pa=True)
    if temp_shape_nodes != None:
        for temp_shape_node in temp_shape_nodes:
            cmds.cutKey(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", option="keys")
            cmds.setKeyframe(temp_shape_node, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="visibility", v=1)


def clean_up(i, attributes, group_Contents):
    global timeline_start, timeline_end
    bake_interval = cmds.intFieldGrp("BakeInterval_IntField", q=True, v1=True)
    cmds.autoKeyframe(state=True)

    if group_Contents[i].split("_")[-3:-2][0] == "ISR":
        timeline_start, timeline_end = group_Contents[i].split("_")[-2:]
    else:
        timeline_start, timeline_end = get_timeline_start_end()

    original_control = "_".join(group_Contents[i].split("_")[:-6])
    if "_dash_" in original_control: # FOR IF THE CONTROL DOESN'T HAVE A UNIQUE NAME
        original_control = original_control.replace("_dash_", "|")
    cmds.bakeResults(original_control, t=(timeline_start, timeline_end), at=attributes, pok=True, sb=bake_interval)
    delete_visibility_keys_after_bake(original_control)

    apply_euler_filter([original_control])

    # #SETS VISIBILITY BACK
    # temp_shape_node = cmds.listRelatives(original_control, shapes=True, children=True)[0]
    # cmds.setAttr(temp_shape_node + ".v", 1)

    #YOU STORE THE TANGENT TYPE BEFORE THE BAKE, SO THAT INCASE IT WAS IN STEPPED, WE MAKE THE TANGENT STEPPED AGAIN CUZ OTHERWISE IT MESSES UP THE ELBOW AFTERWARDS
    return original_control

def delete_ik_blend(i, group_Contents):
    original_control = "_".join(group_Contents[i].split("_")[:-6])
    if "_dash_" in original_control:  # FOR IF THE CONTROL DOESN'T HAVE A UNIQUE NAME
        original_control = original_control.replace("_dash_", "|")
    cmds.cutKey(original_control, time=(int(timeline_start) - 1, int(timeline_end) + 1), at="ikBlend", option="keys")
    cmds.setAttr(original_control + ".ikBlend", 1)
    return original_control


def delete_setup():
    #BAKES THE PREVIOUS CONTROLS, CLEANS UP THE CURVES, DELETES CURRENT CONTROLS AND BRINGS BACK ORIGINALS
    """
        selected_controls = cmds.ls(sl=True)
        if len(selected_controls) > 0:
            for i in range(6):
                cmds.pickWalk(d="up")
            for obj in cmds.ls(sl=True):
                if "temp_IK_Group" in obj or "temp_FK_Group" in obj:
                    pass
                else:
                    assist_message(
                        "Incorrect selection. To generate the code for deleting an IK or FK setup, select one of its controls and then click the button.",
                        4500)
            code += """
    temp_selection = """ + str(selected_controls) + """
                """

        elif len(cmds.ls(sl=True)) == 0:
            code += """
    temp_selection = get_temporary_setup_selection()"""

        code += """
    for selection in temp_selection:
        if cmds.objExists(selection):
            check_if_correct_selection(selection)
            temp_group = get_group_selection(selection)
            group_contents = cmds.listRelatives(temp_group)

            if "temp_IK_Group" in temp_group:
                original_controls = [clean_up(i, ["rotate"], group_contents)    for i in range(3,6)]
                if clear_keys:
                    remove_unnecessary_keys(original_controls, ["rotateX", "rotateY", "rotateZ"])
                    # remove_unnecessary_keys([original_controls[0], original_controls[2]], ["rotate"])
                    # remove_unnecessary_keys([original_controls[1]], ["rotateX"])


            elif "temp_FK_Group" in temp_group:
                ik_ctrl, pole_vector_ctrl = [clean_up(i, ["translate", "rotate"], group_contents)    for i in range(1,3)]
                if clear_keys:
                    remove_unnecessary_keys([ik_ctrl], ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"])
                    remove_unnecessary_keys([pole_vector_ctrl], ["translateX", "translateY", "translateZ"])
                ik_handle = delete_ik_blend(3, group_contents)


    #cmds.lockNode(temp_group, l=False)
        if cmds.objExists(temp_group):
            cmds.delete(temp_group)

delete_setup()

"""

    cmds.scrollField("GenerateCodeOutputWindow", e=True, tx=code)
def extraOptions():
    if cmds.window("Extra_Options", ex=True):
        cmds.deleteUI("Extra_Options")

    cmds.window("Extra_Options", title="Extra Options", wh=[344, 242], s=False)
    cmds.formLayout("ikfk_form_layout_extra", numberOfDivisions=100, w=343, h=240)

    cmds.button("Generate_Code_Button", l="Generate Code", recomputeSize=True,
                bgc=[0.6220035095750363, 1.0, 0.7237659266041047], h=44, w=110, parent="ikfk_form_layout_extra",
                command=lambda *args: generateCode(),
                ann="It isolates the code from the UI, so you can put it on a shelf or add it to a marking menu, and you don't have to come back to the UI every time.\nThere's 2 ways to use this.\n"
                    "Specific setup:  If you select the controls in the scene as if you were applying the setup, when you hit generate it'll store the selection into the code, so you don't have to select them every time.\n"
                    "General setup:  If you have nothing selected in the scene and hit generate, it'll produce a generic version of the code, and you'll have to select the controls every time before executing the code, but it's more flexible.\n"
                    "Important note:  Whatever values you have for the settings in the main window, those values will be stored within the code you generate.")
    set_form_layout_coordinates("ikfk_form_layout_extra", "Generate_Code_Button", 17, 16)

    cmds.radioButtonGrp("GenerateCodeOptions_RadioB", vr=True, numberOfRadioButtons=3, en1=True, l1="FK to IK",
                        l2="IK to FK", l3="Delete Setup", parent="ikfk_form_layout_extra")
    cmds.radioButtonGrp("GenerateCodeOptions_RadioB", e=True, select=1)
    set_form_layout_coordinates("ikfk_form_layout_extra","GenerateCodeOptions_RadioB", 11.5, 135)

    cmds.scrollField("GenerateCodeOutputWindow", width=312, height=150)
    set_form_layout_coordinates("ikfk_form_layout_extra", "GenerateCodeOutputWindow", 75, 16)

    cmds.showWindow("Extra_Options")

if __name__ == "__main__":
    run()