# Scripts/Animation/AdvancedSkeleton/launch.py

import maya.cmds as cmds
import maya.mel as mel
import os
import logging
from .adv_install import is_installed, install

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('AdvancedSkeleton')

def asMayaVersionAsFloat():
    return float(cmds.about(version=True))

def asGetScriptLocation():
    return os.path.dirname(os.path.realpath(__file__))

def asFL(frame_layout):
    try:
        is_collapsed = cmds.frameLayout(frame_layout, query=True, collapse=True)
        cmds.optionVar(intValue=(frame_layout, int(is_collapsed)))
        
        if not is_collapsed:
            if frame_layout == "asPreparationFrameLayout":
                update_preparation_frame()
            elif frame_layout == "asBodyFrameLayout":
                update_body_frame()
            elif frame_layout == "asFaceFrameLayout":
                update_face_frame()
            elif frame_layout == "asPoseFrameLayout":
                update_pose_frame()
    except Exception as e:
        logger.error(f"Error in asFL: {str(e)}")

def update_preparation_frame():
    pass

def update_body_frame():
    pass

def update_face_frame():
    pass

def update_pose_frame():
    pass

def create_preparation_content(parent):
    cmds.columnLayout(adjustableColumn=True, parent=parent)
    
    model_frame = cmds.frameLayout(label="Model", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Model Clean", command=lambda x: safe_mel_eval('asModelCleaner'))
    cmds.button(label="Model Check", command=lambda x: safe_mel_eval('asModelCheckerUI'))
    cmds.setParent('..')
    
    rig_frame = cmds.frameLayout(label="Rig", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="New Scene", command=lambda x: cmds.file(new=True, force=True))
    cmds.button(label="Reference", command=lambda x: mel.eval('asReferenceBrowser 1'))
    cmds.setParent('..')

def create_body_content(parent):
    cmds.columnLayout(adjustableColumn=True, parent=parent)
    
    fit_frame = cmds.frameLayout(label="Fit", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.optionMenu(label="FitSkeletons:")
    cmds.menuItem(label="biped")
    cmds.menuItem(label="quadruped")
    cmds.button(label="Import", command=lambda x: mel.eval('asFitSkeletonImport'))
    cmds.button(label="AutoPlace", command=lambda x: mel.eval('asFitAutoPlace'))
    cmds.setParent('..')
    
    edit_frame = cmds.frameLayout(label="Edit", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="IK-Label:")
    cmds.optionMenu(label="Label Type:")
    cmds.menuItem(label="Root")
    cmds.menuItem(label="Spine")
    cmds.menuItem(label="Arm")
    cmds.menuItem(label="Leg")
    cmds.button(label="Add", command=lambda x: mel.eval('asAddFitJointLabel'))
    cmds.button(label="Remove", command=lambda x: mel.eval('asRemoveFitJointLabel'))
    cmds.setParent('..')
    
    build_frame = cmds.frameLayout(label="Build", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Build AdvancedSkeleton", command=lambda x: mel.eval('asReBuildAdvancedSkeleton'))
    cmds.setParent('..')

def create_face_content(parent):
    cmds.columnLayout(adjustableColumn=True, parent=parent)
    
    pre_frame = cmds.frameLayout(label="Pre", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Face Model Check", command=lambda x: mel.eval('asFaceModelCheck'))
    cmds.optionMenu(label="Rig Type:")
    cmds.menuItem(label="Joints")
    cmds.menuItem(label="BlendShapes")
    cmds.menuItem(label="Mixed")
    cmds.checkBox(label="Game Engine")
    cmds.setParent('..')
    
    fit_frame = cmds.frameLayout(label="Fit", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Create EyeBall", command=lambda x: mel.eval('asCreateFaceFit EyeBall "" 0 0 1 ""'))
    cmds.button(label="Create EyeLid", command=lambda x: mel.eval('asCreateFaceFit EyeLid "Main" 1 1 0 ""'))
    cmds.setParent('..')
    
    build_frame = cmds.frameLayout(label="Build", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Build AdvancedFace", command=lambda x: mel.eval('asBuildAdvancedFace'))
    cmds.setParent('..')

def create_pose_content(parent):
    cmds.columnLayout(adjustableColumn=True, parent=parent)
    
    driving_systems_frame = cmds.frameLayout(label="Driving Systems", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Create Driving System", command=lambda x: mel.eval('asDsCreate'))
    cmds.button(label="Edit", command=lambda x: mel.eval('asDsAutoFindAndEdit'))
    cmds.button(label="Delete", command=lambda x: mel.eval('asDsDelete'))
    cmds.setParent('..')
    
    corrective_shapes_frame = cmds.frameLayout(label="Corrective Shapes", collapsable=True, parent=parent)
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Create Corrective Shape", command=lambda x: mel.eval('asCreateCorrectiveShape'))
    cmds.button(label="Edit", command=lambda x: mel.eval('asEditCorrectiveShape'))
    cmds.button(label="Delete", command=lambda x: mel.eval('asDeleteCorrectiveShape'))
    cmds.setParent('..')

def safe_mel_eval(command):
    try:
        return mel.eval(command)
    except RuntimeError as e:
        logger.error(f"Error executing MEL command '{command}': {str(e)}")
        return None

def launch():
    if not is_installed():
        print("AdvancedSkeleton is not installed. Installing now...")
        install()
    
    try:
        # 检查单位
        current_unit = cmds.currentUnit(query=True, linear=True)
        if current_unit != "cm":
            result = cmds.confirmDialog(title='Unit Check', 
                                        message='AdvancedSkeleton requires "cm" units. Switch now?',
                                        button=['Yes','No'], 
                                        defaultButton='Yes', 
                                        cancelButton='No', 
                                        dismissString='No')
            if result == 'Yes':
                cmds.currentUnit(linear='cm')
        
        # 设置动画混合选项
        anim_blending_opt = cmds.optionVar(query='animBlendingOpt')
        if anim_blending_opt != 1:
            cmds.optionVar(intValue=('animBlendingOpt', 1))
            logger.info("\"Animation Blending Option\" now switched to On.")
        
        # 检查Maya版本并设置关节方向
        maya_version = asMayaVersionAsFloat()
        if maya_version >= 2012:
            if cmds.manipMoveContext('Move', exists=True):
                try:
                    if cmds.manipMoveContext('Move', query=True, orientJointEnabled=True):
                        cmds.manipMoveContext('Move', edit=True, orientJointEnabled=False)
                except:
                    pass

        # 获取脚本位置
        script_location = os.path.dirname(os.path.abspath(__file__))
        mel_file = os.path.join(script_location, "AdvancedSkeleton5.mel")
        
        logger.info(f"Script location: {script_location}")
        logger.info(f"MEL file path: {mel_file}")
        logger.info(f"MEL file exists: {os.path.exists(mel_file)}")

        if os.path.exists(mel_file):
            # 使用原始字符串和双引号来避免转义问题
            mel_command = r'source "{}"'.format(mel_file.replace('\\', '/'))
            logger.info(f"MEL command: {mel_command}")
            mel.eval(mel_command)
            logger.info("AdvancedSkeleton5.mel sourced successfully.")
        else:
            logger.error(f"Cannot find AdvancedSkeleton5.mel at {mel_file}")
            return

        # 创建UI
        if cmds.window('AdvancedSkeletonWindow', exists=True):
            cmds.deleteUI('AdvancedSkeletonWindow')
        
        if cmds.dockControl('AdvancedSkeletonDockControl', exists=True):
            cmds.deleteUI('AdvancedSkeletonDockControl')

        window = cmds.window('AdvancedSkeletonWindow', title='AdvancedSkeleton 5')
        main_layout = cmds.formLayout()
        scroll_layout = cmds.scrollLayout(parent=main_layout)
        column_layout = cmds.columnLayout(adjustableColumn=True, parent=scroll_layout)

        # 添加框架布局
        preparation_frame = cmds.frameLayout(label="Preparation", collapsable=True, 
                                             collapse=cmds.optionVar(query="asPreparationFrameLayout"),
                                             parent=column_layout, 
                                             collapseCommand=lambda: asFL('asPreparationFrameLayout'),
                                             expandCommand=lambda: asFL('asPreparationFrameLayout'))
        create_preparation_content(preparation_frame)

        body_frame = cmds.frameLayout(label="Body", collapsable=True, 
                                      collapse=cmds.optionVar(query="asBodyFrameLayout"),
                                      parent=column_layout,
                                      collapseCommand=lambda: asFL('asBodyFrameLayout'),
                                      expandCommand=lambda: asFL('asBodyFrameLayout'))
        create_body_content(body_frame)

        face_frame = cmds.frameLayout(label="Face", collapsable=True, 
                                      collapse=cmds.optionVar(query="asFaceFrameLayout"),
                                      parent=column_layout,
                                      collapseCommand=lambda: asFL('asFaceFrameLayout'),
                                      expandCommand=lambda: asFL('asFaceFrameLayout'))
        create_face_content(face_frame)

        pose_frame = cmds.frameLayout(label="Pose", collapsable=True, 
                                      collapse=cmds.optionVar(query="asPoseFrameLayout"),
                                      parent=column_layout,
                                      collapseCommand=lambda: asFL('asPoseFrameLayout'),
                                      expandCommand=lambda: asFL('asPoseFrameLayout'))
        create_pose_content(pose_frame)

        # 设置主布局
        cmds.formLayout(main_layout, edit=True,
                        attachForm=[(scroll_layout, 'top', 0),
                                    (scroll_layout, 'left', 0),
                                    (scroll_layout, 'right', 0),
                                    (scroll_layout, 'bottom', 0)])

        # 显示窗口
        cmds.showWindow(window)

        # 调用MEL中的AdvancedSkeleton5函数
        mel.eval('AdvancedSkeleton5()')

        logger.info("AdvancedSkeleton launched successfully.")
    except Exception as e:
        logger.error(f"Error launching AdvancedSkeleton: {str(e)}")

if __name__ == "__main__":
    launch()
