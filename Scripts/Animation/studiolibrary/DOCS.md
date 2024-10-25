[comment]: # "请通过github查看此页面: https://github.com/krathjen/studiolibrary/blob/master/DOCS.md"

<a name="top"></a>
<img src="./src/studiolibrary/resource/icons/header.png" width="252" height="42"/>

请随意根据需要改进此页面。谢谢。

### 索引

* [如何从代码运行](#jf82ksc)
* [如何进行开发时重新加载](#gw4un1m)
* [如何从代码设置名称和路径](#nc2dokp)

* [如何创建本地和共享库](#k25lyqw)

* [如何创建多个库实例](#ou3nb4z)
* [如何为多个项目创建库](#lvx2med)

* [如何为多个项目设置库](#h2rz6Km)

* [如何调试“加载数据时没有对象匹配”](#zi20df5)
* [如何修复具有未知节点的场景](#ufj2oi4)
* [如何锁定和解锁特定文件夹](#we7zm9m)

* [如何手动安装Studio Library](#qiot1k3)



### 常见问题


另请参阅常见问题解答。

https://github.com/krathjen/studiolibrary/labels/FAQ


<br>



### <a name="jf82ksc"></a> 如何从代码运行


```python
import studiolibrary

studiolibrary.main()
```


[顶部](#top)

<br>


### <a name="gw4un1m"></a> 如何进行开发时重新加载

此代码在加载之前移除所有先前导入的Studio Library模块和缓存。


提示：您还可以在单击货架按钮时按住“Shift”键以重新加载模块。


```python

import studiolibrary
studiolibrary.reload()


import studiolibrary
studiolibrary.main()
```

[顶部](#top)


<br>



### <a name="nc2dokp"></a> 如何从代码设置名称和路径


创建并显示一个名为“MY_PROJECT - Anim”的库，指向自定义路径。

```python
import studiolibrary

studiolibrary.main(name="MY_PROJECT - Anim", path="P:/MY_PROJECT/studiolibrary/anim")

```

[顶部](#top)


<br>


### <a name="k25lyqw"></a> 如何创建本地和共享库


创建并显示一个共享库和一个本地库。


```python
import studiolibrary

studiolibrary.main(name="Local", path="C:/temp/studiolibrary/")

studiolibrary.main(name="Shared", path="P:/shared/studiolibrary/")

```


[顶部](#top)


<br>



### <a name="ou3nb4z"></a> 如何创建多个库实例


在此示例中，我们为动画部门、预览部门和本地临时文件夹创建一个库。

创建三个库并仅显示第三个。您可以通过设置菜单访问其他库。

```python
import studiolibrary

studiolibrary.main(name="Local", path="C:/temp/studiolibrary", show=False)
studiolibrary.main(name="MY_PROJECT - Anim", path="P:/MY_PROJECT/studiolibrary/anim", show=False)
studiolibrary.main(name="MY_PROJECT - Previs", path="P:/MY_PROJECT/studiolibrary/previs")

```


[顶部](#top)


<br>


### <a name="lvx2med"></a> 如何为多个项目创建库


在为多个项目实现Studio Library时，我们可以获取当前项目名称，然后设置名称和路径。

```python
import studiolibrary


# 您可以使用环境变量或内部Python模块来获取项目名称。

project = "MY_PROJECT"


path = "/shared/libraries/" + project + "_Library"

name = project + " Library"

studiolibrary.main(name=name, path=path)
```

[顶部](#top)


<br>

### <a name="h2rz6Km"></a> 如何为多个项目设置库


```python
import studiolibrary

libraries = [
    {"name":"Project1", "path":r"D:\Library_Data", "default":True, "theme":{"accentColor":"rgb(0,200,100)"}},

    {"name":"Project2", "path":r"D:\Library_Data2"},

    {"name":"Temp", "path":r"C:\temp"},

]


studiolibrary.setLibraries(libraries)

studiolibrary.main()

```


[顶部](#top)

<br>

### <a name="zi20df5"></a> 如何调试“加载数据时没有对象匹配”


确保在设置菜单中选中“调试模式”。应用姿势后，它应该在脚本编辑器中打印任何奇怪的行为。这可能会使应用姿势变得更慢。

您可能会看到类似以下内容...


```
// mutils : 找不到匹配的目标对象 ...
// mutils : 加载函数耗时 0.38400 秒 /

```


[顶部](#top)


<br>



### <a name="ufj2oi4"></a> 如何修复具有未知节点的场景

未知节点是因为缺少插件。修复此问题的简单方法是在**Python**脚本编辑器中执行以下代码。另一种方法是找到缺少的插件并确保它已加载。


```python
# 删除当前场景中的所有未知节点

import maya.cmds

n = maya.cmds.ls(type="unknown")

if n:

    maya.cmds.delete(n)
```

[顶部](#top)

<br>


### <a name="we7zm9m"></a> 如何锁定和解锁特定文件夹


```python

import studiolibrary


path= "C:/MY_PROJECT/studiolibrary/anim"
name = "MY_PROJECT - Anim"

superusers = ["kurt.rathjen"]


# 解锁所有文件夹。这是默认行为。
studiolibrary.main(name=name, path=path)


# 除非您是超级用户，否则锁定所有文件夹。
studiolibrary.main(name=name, path=path, superusers=superusers)


# 此命令将仅锁定路径中包含“Approved”一词的文件夹。
studiolibrary.main(name=name, path=path, superusers=superusers, lockFolder="Approved")


# 此命令将锁定所有文件夹，除了路径中包含“Users”或“Shared”一词的文件夹。

studiolibrary.main(name=name, path=path, superusers=superusers, unlockFolder="Users|Shared")

```

[顶部](#top)


<br>

### <a name="qiot1k3"></a> 如何手动安装



#### 下载


从以下链接下载并解压缩studiolibrary.zip文件。

www.studiolibrary.com

#### 安装

1. 解压缩下载的studiolibrary.zip文件。


2. 将下面的`Python代码`复制到Maya Python脚本编辑器中。确保选项卡为Python而不是MEL。

3. 在Python代码中更改路径变量为studiolibrary文件夹。

4. 按`Ctrl + Enter`运行。

5. 将Python代码拖到货架上。


``` python
# Python代码

import os
import sys
   

# 3. 用解压后的`src`位置替换此路径。 

path = r"C:\Users\USER\Downloads\studiolibrary\src"

   

if not os.path.exists(path):
   raise FileNotFoundError(r'源路径不存在！')
   
if path not in sys.path:

    sys.path.insert(0, path)
   

import studiolibrary

studiolibrary.main()

```


[顶部](#top)
