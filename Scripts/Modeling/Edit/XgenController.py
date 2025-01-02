#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jerry Tsai
# @Site : Zoroot
import xgenm as xg
import xgenm.xgGlobal as xgg
import xgenm.XgExternalAPI as xge
import maya.cmds as cmds
# 定义设置头发宽度默认值
hairwidth = 0.1000
hairwidthmax = 0.5000
hairwidthmin = 0.0050
hairwithstep = 0.0001
# 定义窗口的函数
def create_window():
    global hairwidth
    global hairwidthmax
    global hairwidthmin
    global hairwithstep
    # 创建窗口
    window = cmds.window(title="Hair Width", iconName='Hair Width', widthHeight=(600, 100))
    # 创建窗口的布局
    cmds.columnLayout(adjustableColumn=True)
    # 创建最大值最小值输入框，可编辑，设置最大值最小值输入框的值
    cmds.floatFieldGrp('SetMinMax', label='Set Min and Max', numberOfFields=2, value1=hairwidthmin, value2=hairwidthmax, changeCommand=update)
    # 创建Hair Width滑块，设置最大值最小值输入框的值，步长，设置滑块的值
    cmds.floatSliderGrp('SetHairWidth', label='Set Hair Width', field=True, minValue=hairwidthmin, maxValue=hairwidthmax, fieldMinValue=hairwidthmin, fieldMaxValue=hairwidthmax, value=hairwidth, step=hairwithstep, changeCommand=update)
    # 设置宽度表达式
    set_width_expression(hairwidth)
    # 显示窗口
    cmds.showWindow(window)
# 定义更新函数
def update(*args):
    # 获取参数
    hairwidthmin = cmds.floatFieldGrp('SetMinMax', query=True, value1=True)
    hairwidthmax = cmds.floatFieldGrp('SetMinMax', query=True, value2=True)
    hairwidth = cmds.floatSliderGrp('SetHairWidth', query=True, value=True)
    # 定义最大值与最小值的范围个规则
    if hairwidthmin > hairwidthmax:
        hairwidthmin = hairwidthmax
    elif hairwidthmax < hairwidthmin:
        hairwidthmax = hairwidthmin
    elif hairwidthmin == hairwidthmax:
        hairwidthmax = hairwidthmin + 0.0001
    # 定义最大值最小值输入框均为0~1之间
    if hairwidthmin < 0:
        hairwidthmin = 0
    if hairwidthmax < 0:
        hairwidthmax = 0
    if hairwidthmin > 1:
        hairwidthmin = 1
    if hairwidthmax > 1:
        hairwidthmax = 1
    # 定义滑块的值在最大值最小值之间
    if hairwidth < hairwidthmin:
        hairwidth = hairwidthmin
    elif hairwidth > hairwidthmax:
        hairwidth = hairwidthmax
    # 定义滑块的值为正数
    if hairwidth < 0:
        hairwidth = 0
    # 回调参数
    cmds.floatFieldGrp('SetMinMax', edit=True, value1=hairwidthmin, value2=hairwidthmax)
    cmds.floatSliderGrp('SetHairWidth', edit=True, minValue=hairwidthmin, maxValue=hairwidthmax, fieldMinValue=hairwidthmin, fieldMaxValue=hairwidthmax, value=hairwidth)
    # 设置宽度表达式
    set_width_expression(hairwidth)
    print("Set the Description Primitive Attributes : ")
    print(" Min : " + str(hairwidthmin) + " Max : " + str(hairwidthmax) + " Width: " + str(hairwidth))
# 定义设置宽度表达式的函数
def set_width_expression(hairwidth):
    hairwidthmin = cmds.floatFieldGrp('SetMinMax', query=True, value1=True)
    hairwidthmax = cmds.floatFieldGrp('SetMinMax', query=True, value2=True)
    hairwidth = cmds.floatSliderGrp('SetHairWidth', query=True, value=True)
    # 将hairwith转换为字符串
    hairwidth_str = str(hairwidth)
    # 将最大值最小值转换为字符串
    hairwidthmax_str = str(hairwidthmax)
    hairwidthmin_str = str(hairwidthmin)
    # 获取被选中的物体
    selectedobject = cmds.ls(selection=True)
    print(hairwidth)
    if not selectedobject:
        ERROR_MESSAGE = "No object selected"
        cmds.warning(ERROR_MESSAGE)
        cmds.confirmDialog(title='Warning', message=ERROR_MESSAGE, button=['OK'], defaultButton='OK') 
    else:
        if xgg.Maya:
            # palette 是collection，先用palettes 获取collections
            palettes = xg.palettes()
            # 筛选出被选中的palette
            palettes = [palette for palette in palettes if palette in selectedobject]
            # 筛选出被选中的Desciption
            descriptions = xg.descriptions()
            descriptions = [description for description in descriptions if description in selectedobject]
            # 设置新的快读表达式
            new_width_expression = "$a=", hairwidth_str + ";#" + hairwidthmax_str + "," + hairwidthmin_str
            # 当palettes为空时，将被选中的Desciption的父级collection筛选出来，加入到palettes中
            if palettes == []:
                # 将被选中的Desciption筛选出来
                for description in descriptions:
                    # 将被选中的Desciption的父级collection筛选出来
                    if description in selectedobject:
                        # 将被选中的Desciption的父级collection加入到palettes中
                        palettes.append(xg.palette(description))
                        # 将palettes转换为集合，去除重复的collection
                        palettes = list(set(palettes))
            if palettes != [] and descriptions == []:
                # 选择的是collection
                for palette in palettes:
                    # 获取collection下的所有Desciption
                    descriptions = xg.descriptions(palette)
            if palettes == [] and descriptions == []:
                print("No xGen collection or description selected")
            print("Current selected hair collection : " + str(palettes))
            print("Current selected hair description : " + str(descriptions))
            # 设置宽度表达式
 

# if __name__ == "__main__":
#     # 创建窗口
#     create_window()