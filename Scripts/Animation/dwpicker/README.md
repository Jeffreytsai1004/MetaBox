# Dreamwall Picker

适用于 Autodesk Maya 2017（或更高版本）的动画选择器

作者：Lionel Brouyère, Olivier Evers
> 该工具是 Hotbox Designer（Lionel Brouyère）的一个分支。
> 一个跨 DCC 的菜单、标记菜单和热盒设计器。
> https://github.com/luckylyk/hotbox_designer

### 功能
- 简单快速的选择器创建。
- 导入 2022 年之前完成的 AnimSchool 选择器。
- 将选择器存储在 Maya 场景中。
- 高级选择器编辑器。
- 执行 AnimSchool 选择器的所有功能以及更多功能...
<center><img src="https://raw.githubusercontent.com/DreamWall-Animation/dwpicker/main/screenshots/picker.gif" alt="drawing" align="center" width="250"/> <img src="https://s10.gifyu.com/images/createbuttons.gif" alt="drawing" align="center" width="400"/>
<img src="https://raw.githubusercontent.com/DreamWall-Animation/dwpicker/main/screenshots/editor.gif" alt="drawing" align="center" width="370"/>

### 安装
将名为 "dwpicker" 的文件夹（不是 dwpicker-main）放入 Maya 脚本文件夹中

| 操作系统 | 路径                                                  |
| ------   | ------                                                |
| Linux    | ~/<用户名>/maya/scripts                               |
| Windows  | \Users\<用户名>\Documents\maya\scripts                |
| Mac OS X | ~<用户名>/Library/Preferences/Autodesk/maya/scripts   |

### 如何运行

```python
import dwpicker
dwpicker.show()
```

### 常见问题

#### 它能在 Maya 2025 上运行吗？
可以！（自版本 0.11.2 起）

#### 我的绑定包含多个命名空间或嵌套命名空间。
此功能当前不支持。选择器旨在提供单级命名空间的灵活性，允许一个选择器在场景中为同一绑定的多个实例服务。切换选择器的命名空间很简单。然而，尽管我们努力保持这种灵活性，但我们尚未找到支持嵌套命名空间的简单方法。虽然有潜在的解决方案，但它们看起来都相当复杂，难以为用户理解和实现。也许将来会有一个绝妙的主意出现，但目前，这个功能不在我们的计划中。我们欢迎您提出任何建议！

#### 为什么我不能使用相对路径来存储我的图像文件？
当您打开选择器时，它会将文件直接导入场景中，失去原始路径引用。我们选择导入数据而不是直接引用它们，因为许多动画师更喜欢为他们的特定镜头需求自定义选择器（例如，为特定镜头添加道具或约束按钮）。这种方法使得使用相对路径变得复杂。

#### 如何在我将选择器分享给其他人时保留图像，而他们的文件存储在其他地方？
尽管不支持相对路径，但与其他 Maya 路径属性类似，您可以在路径中包含环境变量。设置自定义环境变量可能很复杂。因此，我们建议使用一个默认变量：DWPICKER_PROJECT_DIRECTORY，可在选择器首选项窗口中使用。

如果您将 DWPICKER_PROJECT_DIRECTORY 配置为 `c:/my_pickers`，并且您有一个图像路径为：
`c:/my_pickers/my_character/background.png`，可以这样输入以使路径动态化：`$DWPICKER_PROJECT_DIRECTORY/my_character/background.png`
当您从 UI 中选择文件时，它会自动创建包含变量的路径。

### 支持
最好在 GitHub 页面上发布问题。\
如果您没有 GitHub 帐户，可以发送邮件至 `brouyere |a| dreamwall.be`。\
请在邮件主题中以 ***[dwpicker]*** 开头。（请注意，使用这种方式回复的延迟可能会更长）。