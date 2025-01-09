import os
import subprocess
from pathlib import Path
import maya.cmds as cmds

def create_folder_link(src_path, dst_path):
    """
    创建文件夹符号链接
    
    Args:
        src_path: 源文件夹路径
        dst_path: 目标链接路径
        
    Returns:
        bool: 是否创建成功
    """
    try:
        src = Path(src_path)
        dst = Path(dst_path)
        
        if not src.exists():
            print(f"找不到 QuadRemesher: {src}")
            return 0
            
        if dst.exists():
            print(f"QuadRemesher 已安装: {dst}")
            return 1
            
        # 创建父目录
        dst.parent.mkdir(parents=True, exist_ok=True)
        
        # 创建符号链接
        if os.name == 'nt':  # Windows
            cmd = f'mklink /j "{dst}" "{src}"'

            subprocess.run(cmd, shell=True, check=True)
        else:  # Linux/Mac
            os.symlink(src, dst)

        cmds.confirmDialog(title="QuadRemesher", message=u"成功安装 QuadRemesher, 重启 Maya 后生效！", button="OK")
        
        return 2
        
    except Exception as e:
        print(f"创建符号链接失败: {e}")
        return 0

def quick_install():
    src = Path(__file__).parent.parent.parent
    dst = r"C:\ProgramData\Autodesk\ApplicationPlugins\QuadRemesher" 
    print(src, dst)
    
    return create_folder_link(src, dst)
