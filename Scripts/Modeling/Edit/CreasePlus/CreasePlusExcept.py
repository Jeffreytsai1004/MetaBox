import maya.api.OpenMaya as om


def cPexcept(excepstr=""):
    om.MGlobal.displayError(excepstr)
    return Exception(excepstr)