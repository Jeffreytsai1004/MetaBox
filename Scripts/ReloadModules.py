import sys
import importlib
import os
from maya import cmds

def get_all_py_files(start_path):
    """
    递归获取指定目录下所有的 .py 文件
    返回: 包含所有 .py 文件路径的列表
    """
    py_files = []
    for root, dirs, files in os.walk(start_path):
        # 跳过 __pycache__ 目录
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                full_path = os.path.join(root, file)
                # 转换为模块路径格式
                rel_path = os.path.relpath(full_path, start_path)
                module_path = os.path.splitext(rel_path)[0].replace(os.sep, '.')
                module_path = module_path.replace("Scripts.", "")
                py_files.append(module_path)
    return py_files

def reload_metabox():
    """
    重新加载 MetaBox 及其所有相关模块
    """
    try:
        # 关闭现有的 MetaBox 窗口
        if cmds.workspaceControl("ToolBoxWorkSpaceControl", exists=True):
            cmds.deleteUI("ToolBoxWorkSpaceControl", control=True)

        # 获取 Scripts 根目录
        SCRIPTS_PATH = os.path.dirname(os.path.dirname(__file__))
        print(SCRIPTS_PATH)
        
        # 获取所有 .py 文件的模块路径
        modules_to_reload = get_all_py_files(SCRIPTS_PATH)
        # 按模块层级排序，确保先重新加载底层模块
        modules_to_reload.sort(key=lambda x: len(x.split('.')))
        print(modules_to_reload)

        print("开始重新加载模块...")
        
        # 重新加载所有模块
        reloaded_modules = set()
        for module_name in modules_to_reload:
            try:
                if module_name in sys.modules:
                    module = sys.modules[module_name]
                    importlib.reload(module)
                    reloaded_modules.add(module_name)
                    print(f"已重新加载模块: {module_name}")
            except Exception as e:
                print(f"重新加载模块 {module_name} 时出错: {str(e)}")

        print(f"\n成功重新加载 {len(reloaded_modules)} 个模块")
        
        # 最后重新加载并显示 MetaBox
        if 'MetaBox' in sys.modules:
            importlib.reload(sys.modules['MetaBox'])
        from MetaBox import show
        show()
        
        print("\nMetaBox 已成功重新加载！")

    except Exception as e:
        error_msg = f"重新加载 MetaBox 时发生错误: {str(e)}"
        print(error_msg)
        cmds.warning(error_msg)

def reload_all():
    """
    执行重新加载并打印分隔线
    """
    print("\n" + "="*50)
    print("开始重新加载 MetaBox 及其所有模块")
    print("="*50 + "\n")
    reload_metabox()
    print("\n" + "="*50)
    print("重新加载完成")
    print("="*50 + "\n")

# 执行重新加载
# if __name__ == "__main__":
    # reload_all()


