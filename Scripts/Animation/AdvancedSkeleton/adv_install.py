# Scripts/Animation/AdvancedSkeleton/install.py

import maya.cmds as cmds
import maya.mel as mel
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('AdvancedSkeleton')

# 定义全局变量
asBuilding = 0
asRebuilding = 0
asFaceIsResetting = 0
asFitModeScriptJobNr4 = 0
asFitModeScriptJobNr5 = 0
asSkipConfirm = 0

def asMayaVersionAsFloat():
    """获取Maya版本号"""
    return float(cmds.about(version=True))

def load_wb_delta_mush_deformer():
    """根据Maya版本加载wbDeltaMushDeformer模块"""
    maya_version = asMayaVersionAsFloat()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    wb_delta_mush_dir = os.path.join(script_dir, "AdvancedSkeleton5Files", "modules", "wbDeltaMushDeformer").replace("\\", "/")
    
    # 确定适用的Maya版本文件夹
    if maya_version >= 2016.5:
        version_folder = "2016.5"
    elif maya_version >= 2016:
        version_folder = "2016"
    elif maya_version >= 2015:
        version_folder = "2015"
    elif maya_version >= 2014:
        version_folder = "2014"
    elif maya_version >= 2013:
        version_folder = "2013"
    else:
        version_folder = "2012"

    # 构建插件��径
    plugin_dir = os.path.join(wb_delta_mush_dir, version_folder, "plug-ins")
    
    # 根据操作系统选择正确的插件文件
    if sys.platform == "win32":
        plugin_file = "wbDeltaMushDeformer.mll"
    elif sys.platform == "darwin":
        plugin_file = "wbDeltaMushDeformer.bundle"
    else:  # 假设其他平台是Linux
        plugin_file = "wbDeltaMushDeformer.so"
    
    plugin_path = os.path.join(plugin_dir, plugin_file)
    
    if os.path.exists(plugin_path):
        try:
            cmds.loadPlugin(plugin_path)
            print(f"Successfully loaded wbDeltaMushDeformer for Maya {maya_version}")
            
            # 加载MEL脚本
            mel_script = os.path.join(wb_delta_mush_dir, version_folder, "scripts", "AEwbDeltaMushTemplate.mel").replace("\\", "/")
            if os.path.exists(mel_script):
                mel.eval(f'source "{mel_script}"')
                print(f"Loaded AEwbDeltaMushTemplate.mel for Maya {maya_version}")
            else:
                print(f"AEwbDeltaMushTemplate.mel not found for Maya {maya_version}")
        except Exception as e:
            print(f"Failed to load wbDeltaMushDeformer for Maya {maya_version}: {str(e)}")
    else:
        print(f"wbDeltaMushDeformer plugin not found for Maya {maya_version}")

    # 添加模块路径到Maya模块路径
    module_file = os.path.join(script_dir, "AdvancedSkeleton5Files", "modules", "wbDeltaMushDeformer.mod").replace("\\", "/")
    if os.path.exists(module_file):
        maya_module_path = mel.eval('getenv "MAYA_MODULE_PATH"')
        module_dir = os.path.dirname(module_file)
        if module_dir not in maya_module_path:
            mel.eval(f'putenv "MAYA_MODULE_PATH" "{module_dir};{maya_module_path}"')
            print(f"Added {module_dir} to MAYA_MODULE_PATH")

def is_installed():
    return cmds.menu('AdvancedSkeletonMenu', exists=True)

def install():
    global asBuilding, asRebuilding, asFaceIsResetting, asFitModeScriptJobNr4, asFitModeScriptJobNr5, asSkipConfirm

    if is_installed():
        print("AdvancedSkeleton is already installed.")
        return
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # 添加脚本路径到Maya的脚本路径
    maya_script_path = mel.eval('getenv "MAYA_SCRIPT_PATH"')
    if script_dir not in maya_script_path:
        mel.eval(f'putenv "MAYA_SCRIPT_PATH" "{script_dir};{maya_script_path}"')
    
    # 检查并设置单位为厘米
    current_unit = cmds.currentUnit(query=True, linear=True)
    if current_unit != "cm":
        result = cmds.confirmDialog(
            title='Confirm', 
            message=f'Units currently set to: "{current_unit}"\nAdvancedSkeleton requires "cm".\nClick OK to switch',
            button=['Ok', 'Cancel'],
            defaultButton='Ok',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        if result == 'Ok':
            cmds.currentUnit(linear='cm')
            print("Units switched to cm.")
    else:
        print("Units already set to cm.")

    # 设置动画混合选项
    if not cmds.optionVar(query='animBlendingOpt'):
        cmds.optionVar(intValue=('animBlendingOpt', 1))
        print("// \"Animation Blending Option\" now switched to On.")

    # 检查Maya版本并设置关节方向
    maya_version = asMayaVersionAsFloat()
    if maya_version >= 2012:
        if cmds.manipMoveContext('Move', exists=True):
            try:
                if cmds.manipMoveContext('Move', query=True, orientJointEnabled=True):
                    cmds.manipMoveContext('Move', edit=True, orientJointEnabled=False)
            except:
                pass

    # 设置显示层全局设置
    cmds.editDisplayLayerGlobals(useCurrent=False)

    # 重置一些全局变量
    asBuilding = 0
    asRebuilding = 0
    asFitModeSkip = 0
    asSkipConfirm = 0

    # 创建必要的脚本作业
    if asFitModeScriptJobNr4 == 0:
        asFitModeScriptJobNr4 = cmds.scriptJob(runOnce=True, event=("SceneOpened", "asSceneOpened()"))
    if asFitModeScriptJobNr5 == 0:
        asFitModeScriptJobNr5 = cmds.scriptJob(event=("Undo", "asUpdateButtonEnables();asFaceUpdateInfo(1);"))

    # 创建菜单项
    if not cmds.menu('AdvancedSkeletonMenu', exists=True):
        main_window = mel.eval('$temp=$gMainWindow')
        cmds.menu('AdvancedSkeletonMenu', label='AdvancedSkeleton', parent=main_window)
        cmds.menuItem(label='Launch AdvancedSkeleton', command='import Scripts.Animation.AdvancedSkeleton.adv_launch as as_launch; as_launch.launch()')
    
    # 设置版本信息
    try:
        if not cmds.objExists('Main'):
            cmds.createNode('transform', name='Main')
        
        if not cmds.attributeQuery('version', node='Main', exists=True):
            cmds.addAttr('Main', longName='version', attributeType='double')
        
        cmds.setAttr('Main.version', lock=True, keyable=False)
        cmds.setAttr('Main.version', asMayaVersionAsFloat())
    except Exception as e:
        print(f"Error setting version information: {str(e)}")

    # 加载wbDeltaMushDeformer
    load_wb_delta_mush_deformer()

    print("AdvancedSkeleton installed successfully.")

if __name__ == "__main__":
    install()
