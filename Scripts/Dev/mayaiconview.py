
import os
import maya.cmds as cmds

# 全局变量
favorites = []                  # 存储收藏的图标
MAX_FAVORITES = 15              # 收藏夹最大容量
ICON_SIZE = 50                  # 图标大小（像素）
COLUMNS = 15                    # 图标网格的列数
ROWS = 10                       # 图标网格的可见行数
WINDOW_NAME = "mayaIconViewer"  # 窗口名称

def create_icon_viewer():
    """创建并显示图标查看器窗口"""
    window_width = COLUMNS * ICON_SIZE

    # 如果窗口已存在，则删除
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    # 创建主窗口
    cmds.window(WINDOW_NAME, title="Maya 图标查看器", width=window_width)
    main_layout = cmds.columnLayout(adjustableColumn=True)

    # 添加UI元素
    create_ui_elements(window_width)
    update_icons()
    cmds.showWindow(WINDOW_NAME)

def create_ui_elements(width):
    """创建说明文字"""
    cmds.text(label="单击图标复制名称并添加到收藏夹 - 注意：搜索过程可能较慢，请耐心等待", 
              align="center", font="boldLabelFont", width=width)
    cmds.textFieldGrp("searchField", label="搜索:", 
                      columnWidth=[(1, 50), (2, width-70)], 
                      changeCommand=update_icons)
    create_favorites_area()
    create_icon_grid()

def create_favorites_area():
    """创建收藏夹区域"""
    cmds.separator(height=10, style='none')  # 添加一些间距
    cmds.text(label="收藏夹", align='left', font="boldLabelFont")
    cmds.separator(height=5, style='none')  # 再添加一些间距
    
    global favorites_layout
    favorites_layout = cmds.rowLayout(numberOfColumns=MAX_FAVORITES+1, 
                                      columnWidth1=45,
                                      adjustableColumn=2,
                                      columnAttach=[(1, 'left', 0), (2, 'left', 0)],
                                      height=50,
                                      backgroundColor=[0.2, 0.2, 0.2])
    
    # 添加星形图标（不可点击）
    cmds.symbolButton(image="SE_FavoriteStar.png", width=45, height=45, 
                      enable=False, annotation="收藏夹：单击图标可以快速复制名称")
    
    # 创建收藏夹图标位置
    for _ in range(MAX_FAVORITES):
        cmds.symbolButton(parent=favorites_layout, width=45, height=45, visible=False)

    cmds.setParent('..')
    cmds.separator(height=10, style='none')  # 添加底部间距

def create_icon_grid():
    """创建图标网格"""
    global scroll_layout, grid_layout
    scroll_layout = cmds.scrollLayout(horizontalScrollBarThickness=16, 
                                      verticalScrollBarThickness=16)
    grid_layout = cmds.gridLayout(numberOfColumns=COLUMNS, 
                                  cellWidthHeight=(ICON_SIZE, ICON_SIZE))

def update_icons(*args):
    """更新图标显示"""
    search_term = cmds.textFieldGrp("searchField", query=True, text=True).lower()
    
    # 清除现有的图标
    for child in cmds.gridLayout(grid_layout, query=True, childArray=True) or []:
        cmds.deleteUI(child)

    # 添加匹配的图标
    for icon in cmds.resourceManager(nameFilter="*.png"):
        if search_term in icon.lower():
            cmds.symbolButton(parent=grid_layout, image=icon, width=45, height=45,
                              command=lambda x, i=icon: handle_click(i), annotation=icon)

    adjust_layout()

def adjust_layout():
    """调整布局大小"""
    visible_icons = len(cmds.gridLayout(grid_layout, query=True, childArray=True) or [])
    total_rows = -(-visible_icons // COLUMNS)  # 向上取整
    scroll_height = min(total_rows, ROWS) * ICON_SIZE
    cmds.scrollLayout(scroll_layout, edit=True, height=scroll_height)
    cmds.window(WINDOW_NAME, edit=True, height=scroll_height + 180)

def handle_click(icon):
    """处理图标点击事件"""
    copy_to_clipboard(icon)
    add_to_favorites(icon)

def copy_to_clipboard(icon):
    """复制图标名称到剪贴板"""
    os.popen(f'cmd /c echo {icon} | clip')

def add_to_favorites(icon):
    """添加图标到收藏夹"""
    global favorites
    if icon not in favorites:
        if len(favorites) >= MAX_FAVORITES:
            favorites.pop(0)  # 如果收藏夹已满，移除最���的图标
        favorites.append(icon)
        update_favorites()

def update_favorites():
    """更新收藏夹显示"""
    children = cmds.layout(favorites_layout, query=True, childArray=True)
    for i, child in enumerate(children[1:], 1):  # 跳过第一个子元素（星形图标）
        if i <= len(favorites):
            cmds.symbolButton(child, edit=True, image=favorites[i-1], visible=True,
                              command=lambda x, icon=favorites[i-1]: copy_to_clipboard(icon))
        else:
            cmds.symbolButton(child, edit=True, visible=False)

if __name__ == "__main__":
    create_icon_viewer()
