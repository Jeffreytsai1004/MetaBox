#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import sys



def onMayaDroppedPythonFile(*args):
    run()



#Let's you batch import:
def run(*args):
    if CheckForBonusTools:
        multipleFilters =  'All native importable files (*.3ds *.abc *.ass *.at *.catpart *.dae *.fbx *.igs *.iges *.jt *.ma *.mb *.obj *.prt *.sat *.step *.stp *.wire);; Maya binary (*.mb);; Maya Ascii (*.ma);; WIRE_ATF (*.wire);; Obj (*.obj);; FBX (*.fbx);; DAE_FBX (*.dae);; Alembic Cache (*.abc);; Atom (*.atom);; Step (*.stp *.step);; IGES_ATF (*.igs *.iges);; ASS (*.ass);; 3DS Max (*.3ds);; CATIAV5_ATF (*.catpart);; JT_ATF (*.jt);; SAT_ATF (*.sat);; NX_ATF (*.prt)'
    else:
        multipleFilters =  'All native importable files (*.abc *.ass *.at *.catpart *.dae *.fbx *.igs *.iges *.jt *.ma *.mb *.obj *.prt *.sat *.step *.stp *.wire);; Maya binary (*.mb);; Maya Ascii (*.ma);; WIRE_ATF (*.wire);; Obj (*.obj);; FBX (*.fbx);; DAE_FBX (*.dae);; Alembic Cache (*.abc);; Atom (*.atom);; Step (*.stp *.step);; IGES_ATF (*.igs *.iges);; ASS (*.ass);; 3DS Max (*.3ds);; CATIAV5_ATF (*.catpart);; JT_ATF (*.jt);; SAT_ATF (*.sat);; NX_ATF (*.prt)'
    files = cmds.fileDialog2(caption = 'Choose files to import', ds = 2, fileMode = 4, okCaption = 'Import', fileFilter = multipleFilters, hideNameEdit = False)
    
    # 添加检查以确保 files 有效
    if not files or not isinstance(files, list) or len(files) == 0:
        cmds.warning('未选择任何文件，导入操作已取消。')
        return  # 直接返回，避免后续代码执行

    for x in files:
        if any(y in x for y in ['.ma', '.MA']):
            fileType = 'mayaAscii'
            options = ''
            ImportFiles(fileType, x, options)
            
        if any(y in x for y in ['.mb', '.MB']):
            fileType = 'mayaBinary'
            options = ''
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.wire', '.WIRE']):
            fileType = 'WIRE_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.obj', '.OBJ']):
            fileType = 'OBJ'
            options = 'mo=0'
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.fbx', '.FBX']):
            fileType = 'FBX'
            options = ''
            LoadPlugin('fbxmaya')
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.dae', '.DAE']):
            fileType = 'DAE_FBX'
            options = ''
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.abc', '.ABC']):
            fileType = 'Alembic'
            options = ''
            LoadPlugin('AbcImport')
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.atom', '.ATOM', '.at', '.AT']):
            fileType = 'atomImport'
            options = ''
            LoadPlugin('atomImportExport')
            ImportFiles(fileType, x, options)


        if any(y in x for y in ['.step', '.STEP', '.stp', '.STP']):
            fileType = 'STEP_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['igs.', '.IGS', '.iges', '.IGES']):
            fileType = 'IGES_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['.ass', '.ASS']):
            fileType = 'ASS'
            options = ''
            LoadPlugin('mtoa')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['.3ds', '.3DS']):
            fileType = '3ds'
            options = ''
            if CheckForBonusTools:
                LoadPlugin('3ds')
                ImportFiles(fileType, x, options)


        if any(y in x for y in['.catpart', '.CATPART']):
            fileType = 'CATIAV5_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['.jt', '.JT']):
            fileType = 'JT_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['.sat', '.SAT']):
            fileType = 'SAT_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)


        if any(y in x for y in['.prt', '.PRT']):
            fileType = 'NX_ATF'
            options = ''
            LoadPlugin('ATFPlugin')
            ImportFiles(fileType, x, options)



def CheckForBonusTools(*args):
    for x in sys.path:
        if 'MayaBonusTools' in x:
            return True
    return False



def LoadPlugin(plugin, *args):
        if not cmds.pluginInfo(plugin, query = True, loaded = True):
            try:
                cmds.loadPlugin(plugin)
                sys.stdout.write('Plugin "' + plugin + '" loaded.\n')
            except(RuntimeError):
                cmds.warning('Could not find "' + plugin + '" plugin or could not load it. Open the Plugin Manager and make sure Maya recognized the plugin and try again.\n')



def ImportFiles(fileType, file, options, *args):
    namespace = file.split('/')
    namespace = namespace[-1].split('.')
    namespace = namespace[0]
    try:
        cmds.file(str(file), i = True, type = fileType, ignoreVersion = True, mergeNamespacesOnClash = False, namespace = namespace, options = options)
        sys.stdout.write('Imported "' + str(file) + '".\n')
    except(UnicodeEncodeError):
        sys.stdout.write('Either the directory path or the file name have some special characters.\n')
        sys.stdout.write('The names will be changed.\n')
        cmds.file(file, i = True, type = fileType, ignoreVersion = True, mergeNamespacesOnClash = False, namespace = namespace, options = options)
        sys.stdout.write('Imported "' + file + '".\n')
    except(ImportError):
        cmds.warning('Could not import ' + file + '. Maybe you dont have the requiered permissions to the folder.\n')



if __name__ == '__main__':
    if not cmds.about(batch = True):
        run()
