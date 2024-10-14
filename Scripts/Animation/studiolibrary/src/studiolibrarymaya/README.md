# Studio Library 项目

项目用于加载和保存数据。


### 姿势项目

保存和加载姿势项目

```python
from studiolibrarymaya import poseitem

path = "/AnimLibrary/Characters/Malcolm/malcolm.pose"
objects = maya.cmds.ls(selection=True) or []
namespaces = []

# 保存姿势项目
poseitem.save(path, objects=objects)

# 加载姿势项目
poseitem.load(path, objects=objects, namespaces=namespaces, key=True, mirror=False)
```

### 动画项目

保存和加载动画项目

```python
from studiolibrarymaya import animitem

path = "/AnimLibrary/Characters/Malcolm/malcolm.anim"
objects = maya.cmds.ls(selection=True) or []

# 保存动画项目
animitem.save(path, objects=objects, frameRange=(0, 200), bakeConnected=False)

# 加载动画项目
animitem.load(path, objects=objects, option="replace all", connect=False, currentTime=False)
```

加载多个命名空间的动画

```python
from studiolibrarymaya import animitem
animitem.load(path, namespaces=["character1", "character2"], option="replace all")
```

### 镜像表项目

保存和加载镜像表

```python
from studiolibrarymaya import mirroritem

path = "/AnimLibrary/Characters/Malcolm/malcolm.mirror"
objects = maya.cmds.ls(selection=True) or []

# 保存镜像表项目
mirroritem.save(path, objects=objects, leftSide="Lf", rightSide="Rf")

# 加载镜像表项目
mirroritem.load(path, objects=objects, namespaces=[], option="swap", animation=True, time=None)
```

### 选择集项目

保存和加载选择集

```python
from studiolibrarymaya import setsitem

path = "/AnimLibrary/Characters/Malcolm/malcolm.set"
objects = maya.cmds.ls(selection=True) or []

# 保存选择集项目
setsitem.save(path, objects=objects)

# 加载选择集项目
setsitem.load(path, objects=objects, namespaces=[])
```


### Maya 文件项目（开发中）

保存和加载 Maya 文件项目

此项目可用于加载和保存任何 Maya 节点。例如：
定位器和几何体。

```python
from studiolibrarymaya import mayafileitem

path = "/AnimLibrary/Characters/Malcolm/malcolm.mayafile"
objects = maya.cmds.ls(selection=True) or []

# 将项目保存到磁盘
mayafileitem.save(path, objects=objects)

# 从磁盘加载项目
mayafileitem.load(path)
```

### 示例项目

如果您想创建一个自定义项目以保存和加载不同数据类型，请查看 [exampleitem.py](exampleitem.py)

在开发新项目时，您可以在架子图标上“Shift + 点击”，这将重新加载所有 Studio Library 模块，包括您对项目的更改。

确保使用 [配置文件](../studiolibrary/config/default.json) 中的 "itemRegistry" 键或通过调用 `studiolibrary.registerItem(cls)` 注册任何新项目。