import maya.cmds as cmds
def run():
    cmds.upAxis(axis='y')
    cmds.delete("DHIhead:spine_04", "Lights", "export_geo_GRP", "head_grp")
    cmds.rename("rig", "body_rig")
    cmds.rename("geometry_grp", "body_geometry_grp")
    body_grp_lock = cmds.listRelatives('body_grp', allDescendents=True, type='transform')
    for obj in body_grp_lock:
        cmds.setAttr(obj + '.translateX', lock=False)
        cmds.setAttr(obj + '.translateY', lock=False)
        cmds.setAttr(obj + '.translateZ', lock=False)
        cmds.setAttr(obj + '.rotateX', lock=False)
        cmds.setAttr(obj + '.rotateY', lock=False)
        cmds.setAttr(obj + '.rotateZ', lock=False)
        cmds.setAttr(obj + '.scaleX', lock=False)
        cmds.setAttr(obj + '.scaleY', lock=False)
        cmds.setAttr(obj + '.scaleZ', lock=False)
    correctiveCube = cmds.polyCube()[0]
    cmds.parent('root_drv', correctiveCube)
    cmds.rotate(-90,0,0,correctiveCube,relative=True)
    cmds.parent('root_drv',world=True)
    cmds.delete(correctiveCube)

    save_path = cmds.fileDialog2(fileMode=0, caption="Save Maya Scene", fileFilter="Maya Binary (*.mb)")[0]

    cmds.file(rename=save_path)
    cmds.file(save=True, type='mayaBinary')
