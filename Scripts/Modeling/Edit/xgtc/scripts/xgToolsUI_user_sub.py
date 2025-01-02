import maya.cmds as cmd
import maya.mel as mel
import xgToolsUtility_user

def xgToolsUI():
    window1 = 'xgToolsUI_user_sub_window'

    if cmd.window(window1,q=1,ex=1):
        cmd.deleteUI(window1)

    cmd.window(window1,t='Groomer`s Tool')
    cmd.columnLayout(adj=1)
    xgToolsUtility_user.xgtToolUtilityTab('authorized')

    cmd.window(window1,e=1,w=100,h=100)
    cmd.showWindow(window1)

