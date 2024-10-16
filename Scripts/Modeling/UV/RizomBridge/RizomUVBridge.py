import os, platform, subprocess, sys

if sys.version_info.minor < 11:
    # Maya 2024 and earlier
    from PySide2 import QtGui
    from PySide2 import QtWidgets, QtCore
    from shiboken2 import wrapInstance
else:
    # Maya 2025
    from PySide6 import QtGui
    from PySide6 import QtWidgets, QtCore
    from shiboken6 import wrapInstance

if sys.version_info.major == 3:
    # Python 3
    from . import scriptlist
elif sys.version_info.major == 2:
    # Python 2
    import scriptlist

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from maya import OpenMayaUI as omui
import maya.OpenMaya as om

import maya.cmds as cmds
import maya.mel as mel
import xml.dom.minidom as xml  # For XML settings

DEBUG = False
PRNT_STRING = "<RizomUV Bridge>"

# om.MGlobal.displayError('ERROR!')

class Settings():
    def __init__(self):
        self.config_path = os.path.join('%s/RizomBridge' % os.getenv('APPDATA'))
        config_file = 'uisettings.xml'

        # TODO: Create a unique id for the lua script tied to the Maya instance.
        # rizom_script_path = tempfile.gettempdir() + os.sep + "MayaRizomBridgeScript.lua"
        rizom_script_path = os.path.join(self.config_path, "MayaRizomBridgeScript.lua")
        self.rizom_script_path = rizom_script_path.replace('\\', '/')

        self.apppath = None
        self.config_file_path = os.path.join(self.config_path, config_file)
        self.check_config_exists(self.config_path)

        try:
            self.read_settings()
        except:
            print("<RizomUV Bridge> Failed to read settings, creating new xml file.")
            self.set_defaults()
            self.save_xml()
            self.read_settings()

        self.reset_export_path()

    def reset_export_path(self):
        self.exportFile = os.path.join(self.config_path, self.objname)
        self.exportFile = self.exportFile.replace('\\', '/')

    def read_settings(self):
        doc = xml.parse(self.config_file_path)

        ui_app = doc.getElementsByTagName("Application")[0]
        self.apppath 		= ui_app.getAttribute("apppath")
        self.objname 		= ui_app.getAttribute("objname")
        self.upaxis 		= ui_app.getAttribute("upaxis")
        self.loaduvs 		= self.str_to_bool(ui_app.getAttribute("loaduvs"))
        self.useuvlink	    = self.str_to_bool(ui_app.getAttribute("useuvlink"))
        self.fixuvnames	    = self.str_to_bool(ui_app.getAttribute("fixuvnames"))
        self.usecustompath  = self.str_to_bool(ui_app.getAttribute("usecustompath"))
        self.custompath     = ui_app.getAttribute("custompath")

        ui_packer = doc.getElementsByTagName("Packer")[0]
        self.quality 		= int(ui_packer.getAttribute("quality"))
        self.mutations 		= int(ui_packer.getAttribute("mutations"))
        self.margin 		= int(ui_packer.getAttribute("margin"))
        self.spacing 		= int(ui_packer.getAttribute("spacing"))
        self.resolution		= int(ui_packer.getAttribute("resolution"))
        self.initscaleavg 	= self.str_to_bool(ui_packer.getAttribute("initscaleavg"))
        self.autofit 		= self.str_to_bool(ui_packer.getAttribute("autofit"))

    def set_defaults(self):
        self.objname = "MayaRizomExport.fbx"
        self.upaxis = "Y"
        self.loaduvs = True
        self.useuvlink = True
        self.fixuvnames = False
        self.usecustompath = False
        self.custompath = ""

        self.quality = 2
        self.mutations = 256
        self.margin = 2
        self.spacing = 2
        self.resolution = 1024
        self.initscaleavg = True
        self.autofit = True
        self.apppath = self.findall_rizom_installs()[-1]
        pass

    def save_xml(self):
        print(PRNT_STRING, "Saving settings to disk: {}".format(self.config_file_path))
        doc = xml.Document()
        root_element = doc.createElement("RizomBridge")

        element_application = doc.createElement("Application")
        element_application.setAttribute("apppath", str(self.apppath))
        element_application.setAttribute("objname", str(self.objname))
        element_application.setAttribute("upaxis", str(self.upaxis))
        element_application.setAttribute("loaduvs", str(self.loaduvs))
        element_application.setAttribute("useuvlink", str(self.useuvlink))
        element_application.setAttribute("fixuvnames", str(self.fixuvnames))
        element_application.setAttribute("usecustompath", str(self.usecustompath))
        element_application.setAttribute("custompath", str(self.custompath))

        element_packer = doc.createElement("Packer")
        element_packer.setAttribute("quality", str(self.quality))
        element_packer.setAttribute("mutations", str(self.mutations))
        element_packer.setAttribute("margin", str(self.margin))
        element_packer.setAttribute("spacing", str(self.spacing))
        element_packer.setAttribute("resolution", str(self.resolution))
        element_packer.setAttribute("initscaleavg", str(self.initscaleavg))
        element_packer.setAttribute("autofit", str(self.autofit))

        doc.appendChild(root_element)
        root_element.appendChild(element_application)
        root_element.appendChild(element_packer)
        doc.writexml(open(self.config_file_path, 'w'), indent="  ", addindent="  ", newl='\n')

    def check_config_exists(self, config_path):
        print(PRNT_STRING, "Checking for config file:{}".format(self.config_file_path))

        if not os.path.exists(config_path):
            os.makedirs(config_path)
        if not os.path.exists(self.config_file_path):
            print(PRNT_STRING, "Config not found.")
            self.set_defaults()
            self.save_xml()
        else:
            print(PRNT_STRING, "Config found.")

    def findall_rizom_installs(self):
        """ Returns list of all rizom.exe in registry that exist on disk """
        try:        
            import winreg
        except:
            self.manual_locate_rizom()
            return [self.apppath]

        key_path = "SOFTWARE\\Rizom Lab\\"
        parent_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        installs = []
        i = 0
        while i < 1000:
            try:
                key = winreg.EnumKey(parent_key, i)
                try:
                    exe_path = winreg.QueryValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path + key),
                                                 "rizomuv.exe") + ".exe"
                except FileNotFoundError:
                    exe_path = ""
                if os.path.exists(exe_path):
                    installs.append(exe_path.replace("\\", "/"))

            except WindowsError:
                break
            i += 1
        print (PRNT_STRING, "Found RizomUV installs in Windows Registry:")
        for inst in sorted(installs):
            print(" ..", inst)
        return sorted(installs)
    
    def manual_locate_rizom(self):
        om.MGlobal.displayWarning("Could not locate rizomuv.exe: %s" % self.apppath)
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Locate rizomuv.exe', 'C:/Program Files/Rizom Lab/', "Executable (*.exe)")

        self.apppath = fname[0]
        self.appver = self.get_version()
        self.save_xml()

    def get_version(self):
        """ Return version number as list as read from the folder name, eg. [2022, 2] """
        return os.path.dirname(self.apppath).split()[-1].split('.')

    def check_lua_path(self):
        if not os.path.exists(self.rizom_script_path):
            with open(self.rizom_script_path, 'w') as f:
                if DEBUG: print(PRNT_STRING, "Creating blank lua file at", self.rizom_script_path)
                f.write('')

    def str_to_bool(self, s):
        if s == 'True':
            return True
        else:
            # Return False for everything else, otherwise it might return None which will cause a crash.
            return False


class RizomUVBridgeWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, rootWidget=None, *args, **kwargs):
        super(RizomUVBridgeWindow, self).__init__()

        """
        if not os.path.exists(config_path):
            reset_config()
        if DEBUG: print("<RizomUV Bridge>", config_path)
        Config.read(config_path)
        """
        self.conf = Settings()
        self.conf.check_lua_path()

        # self.rizomPath = self.conf.apppath
        print("Rizom Path:", self.conf.apppath)
        self.setWindowTitle("Bridge")

        self.sj_num_selchange = cmds.scriptJob(parent=self.objectName(), event=['SelectionChanged', self.ui_update_uvchannels])

        # self.setMinimumSize(200, 300)
        self.resize(250, 300)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()
        self.validate_export_path()
        self.exported_objects = []
        self.ui_update_uvchannels()
        self.cleanse_namespaces()

        if not os.path.exists(self.conf.apppath):
            self.conf.manual_locate_rizom()
            v = self.conf.get_version()
            self.btn_run.setText('Run RizomUV {}.{}'.format(v[0], v[1]))

        rizom_link_path = os.path.dirname(self.conf.apppath) + '/RizomUVLink'
        self.port = None
        if rizom_link_path not in sys.path:
            sys.path.append(os.path.dirname(self.conf.apppath) + '/RizomUVLink')
        try:
            from RizomUVLink import CRizomUVLink
            self.link = CRizomUVLink()
        except:
            self.link = None


    # noinspection PyAttributeOutsideInit
    def create_widgets(self):
        v = ".".join(self.conf.get_version())
        self.btn_run = QtWidgets.QPushButton('Run RizomUV {}'.format(v), self)
        self.btn_export = QtWidgets.QPushButton('Export', self)
        self.btn_import = QtWidgets.QPushButton('Import', self)
        self.cbx_use_link = QtWidgets.QCheckBox('Attempt to use CRizomUVLink', self)
        self.cbx_use_link.setChecked(self.conf.useuvlink)
        self.cbx_fix_set_names = QtWidgets.QCheckBox('Fix UV set names on Import', self)
        self.cbx_fix_set_names.setChecked(self.conf.fixuvnames)
        self.cbx_custom_path = QtWidgets.QCheckBox('Use custom path for fbx', self)
        self.cbx_custom_path.setChecked(self.conf.usecustompath)
        self.field_custom_path = QtWidgets.QLineEdit("C:/")
        self.field_custom_path.setText(self.conf.custompath)

        # Export settings widgets
        self.radioAxisY = QtWidgets.QRadioButton('Y')
        self.radioAxisZ = QtWidgets.QRadioButton('Z')
        if self.conf.upaxis == 'Y':
            self.radioAxisY.setChecked(True)
        else:
            self.radioAxisZ.setChecked(True)

        self.cbx_keepuv = QtWidgets.QCheckBox('Load Existing UVs', self)
        self.cbx_keepuv.setChecked(self.conf.loaduvs)

        self.combo_scripts = QtWidgets.QComboBox(self)
        self.combo_scripts.addItem("No Script")
        for s in scriptlist.scripts:
            self.combo_scripts.addItem(s[1])

        # Utilities widgets
        self.btn_fix_shell_normals = QtWidgets.QPushButton('Set UV border edges to Hard')
        self.btn_edit_settings = QtWidgets.QPushButton('Open settings folder')

        self.combo_pack_uvset = QtWidgets.QComboBox(self)
        #
        self.btn_pack = QtWidgets.QPushButton('Export and Pack UVs', self)
        self.combo_pack_quality = QtWidgets.QComboBox(self)
        self.combo_pack_quality.addItems(['Low', 'Normal', 'High', 'Higher', 'Ultra'])
        self.combo_pack_quality.setCurrentIndex(self.conf.quality)
        #
        self.slider_pack_uvmap = QtWidgets.QSlider(QtCore.Qt.Orientation(1))
        self.slider_pack_uvmap.setMinimum(0)
        self.slider_pack_uvmap.setMaximum(5)
        self.slider_pack_uvmap.setValue(1)

        self.label_uvmap = QtWidgets.QLabel("1")

        self.dspin_pack_mutations = QtWidgets.QSpinBox()
        self.dspin_pack_mutations.setSingleStep(1)
        self.dspin_pack_mutations.setRange(1, 1000)
        self.dspin_pack_mutations.setWrapping(False)
        self.dspin_pack_mutations.setValue(self.conf.mutations)
        #
        self.dspin_pack_resolution = QtWidgets.QSpinBox()
        self.dspin_pack_resolution.setSingleStep(8)
        self.dspin_pack_resolution.setRange(8, 8192)
        self.dspin_pack_resolution.setWrapping(False)
        self.dspin_pack_resolution.setValue(self.conf.resolution)
        #
        self.dspin_pack_margin = QtWidgets.QSpinBox()
        self.dspin_pack_margin.setSingleStep(1)
        self.dspin_pack_margin.setWrapping(False)
        self.dspin_pack_margin.setValue(self.conf.margin)
        #
        self.dspin_pack_spacing = QtWidgets.QSpinBox()
        self.dspin_pack_spacing.setSingleStep(1)
        self.dspin_pack_spacing.setWrapping(False)
        self.dspin_pack_spacing.setValue(self.conf.spacing)
        #
        self.cbx_initial_scale_avg = QtWidgets.QCheckBox("Use 'Avarage' Initial Scale", self)
        self.cbx_initial_scale_avg.setChecked(self.conf.initscaleavg)
        #
        self.cbx_layout_scaling = QtWidgets.QCheckBox("Layout: Auto Fit", self)
        self.cbx_layout_scaling.setChecked(self.conf.autofit)

        pass

    # noinspection PyAttributeOutsideInit
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        grp_layout = QtWidgets.QVBoxLayout()
        grp_layout.addWidget(self.btn_run)
        grp_layout.addWidget(self.btn_export)
        grp_layout.addWidget(self.btn_import)
        grp_layout.addWidget(self.cbx_use_link)
        grp_layout.addWidget(self.cbx_fix_set_names)
        #hor_layout = QtWidgets.QHBoxLayout()
        grp_layout.addWidget(self.cbx_custom_path)
        grp_layout.addWidget(self.field_custom_path)
        #grp_layout.addLayout(hor_layout)

        # grp_layout.addWidget(self.btn_edit)
        grp = QtWidgets.QGroupBox("UV Operations")
        grp.setLayout(grp_layout)
        main_layout.addWidget(grp)

        # Export Settings
        grp_layout = QtWidgets.QVBoxLayout()
        grp_layout.addWidget(self.cbx_keepuv)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("Scripts"))
        hor_layout.addWidget(self.combo_scripts)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("Up Axis"))
        hor_layout.addWidget(self.radioAxisY)
        hor_layout.addWidget(self.radioAxisZ)
        grp_layout.addLayout(hor_layout)

        grp = QtWidgets.QGroupBox("Export Settings")
        grp.setLayout(grp_layout)
        main_layout.addWidget(grp)

        # Utilites
        grp_layout = QtWidgets.QVBoxLayout()
        grp_layout.addWidget(self.btn_fix_shell_normals)
        grp_layout.addWidget(self.btn_edit_settings)
        # hor_layout = QtWidgets.QHBoxLayout()
        # hor_layout.addWidget(self.btn_uvl_edges)
        # grp_layout.addLayout(hor_layout)

        grp = QtWidgets.QGroupBox("Utilities")
        grp.setLayout(grp_layout)
        main_layout.addWidget(grp)

        # UV Packer
        grp_layout = QtWidgets.QVBoxLayout()
        grp = QtWidgets.QGroupBox("UV Packer")

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(self.btn_pack)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("UV Set to pack"))
        hor_layout.addWidget(self.combo_pack_uvset)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("Packing Quality"))
        hor_layout.addWidget(self.combo_pack_quality)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("Mutations"))
        hor_layout.addWidget(self.dspin_pack_mutations)
        hor_layout.addWidget(QtWidgets.QLabel("Resolution"))
        hor_layout.addWidget(self.dspin_pack_resolution)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(QtWidgets.QLabel("Margin"))
        hor_layout.addWidget(self.dspin_pack_margin)
        hor_layout.addWidget(QtWidgets.QLabel("Spacing"))
        hor_layout.addWidget(self.dspin_pack_spacing)
        grp_layout.addLayout(hor_layout)

        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(self.cbx_initial_scale_avg)
        grp_layout.addLayout(hor_layout)
        hor_layout = QtWidgets.QHBoxLayout()
        hor_layout.addWidget(self.cbx_layout_scaling)
        grp_layout.addLayout(hor_layout)

        grp_layout.addStretch()
        grp.setLayout(grp_layout)
        main_layout.addWidget(grp)
        pass

    def create_connections(self):
        self.btn_run.clicked.connect(self.riz_run)
        self.btn_export.clicked.connect(self.riz_export)
        self.btn_import.clicked.connect(self.riz_import)
        self.btn_fix_shell_normals.clicked.connect(fix_shell_border_normals)
        self.btn_edit_settings.clicked.connect(self.browse_settings_location)
        self.cbx_custom_path.stateChanged.connect(self.validate_export_path)
        self.field_custom_path.textEdited.connect(self.validate_export_path)

        self.cbx_keepuv.stateChanged.connect(self.set_config)
        self.slider_pack_uvmap.valueChanged.connect(self.ui_pack_update_labels)

        self.radioAxisY.clicked.connect(self.set_config)
        self.radioAxisZ.clicked.connect(self.set_config)
        # self.combo_scripts.currentIndexChanged.connect(self.ui_toggle_roundtrip_option)

        self.dspin_pack_mutations.valueChanged.connect(self.set_config)
        self.dspin_pack_resolution.valueChanged.connect(self.set_config)
        self.dspin_pack_margin.valueChanged.connect(self.set_config)
        self.dspin_pack_spacing.valueChanged.connect(self.set_config)
        self.cbx_layout_scaling.stateChanged.connect(self.set_config)
        self.cbx_use_link.stateChanged.connect(self.set_config)
        self.cbx_fix_set_names.stateChanged.connect(self.set_config)

        self.btn_pack.clicked.connect(self.riz_pack)
        return    

    def riz_run(self):
        # Confirm application path
        if not os.path.exists(self.conf.apppath):
            self.manual_locate_rizom()

        if self.link and self.cbx_use_link.isChecked():
            self.port = self.link.RunRizomUV()
            print(f"{PRNT_STRING} RizomUV {self.link.RizomUVVersion()} link established. Now listening to commands on TCP port: {str(self.port)}")

            # Enable UI relevant only for RizomUV Link
            # self.btn_uvl_edges.setEnabled(True)
            # self.btn_uvl_edges.setStyleSheet("background-color: {}; color: white".format("#ef4000"))
        else:
            # Use original method if link is not working.
            print(PRNT_STRING, "RizomUV link not available. Communicating using LUA script file.")
            cmd = '"' + self.conf.apppath + '" -cf "' + self.conf.rizom_script_path + '"'
            print(cmd)

            if platform.system() == "Windows":
                self.sp = subprocess.Popen(cmd, shell=True)
            else:
                self.sp = subprocess.Popen(["open", "-a", self.conf.apppath, "-cf", self.conf.rizom_script_path])

        self.btn_export.setEnabled(True)
        return

    def riz_pack(self):
        # Export model with no script loaded,
        # Also tell Rizom not to load the model in the riz_export function
        # because it sometimes does not have time to load before we overwrite the lua file with these commands.
        current_uv = self.combo_pack_uvset.currentText()
        # current_uv_index = self.combo_pack_uvset.currentIndex()

        exported = self.riz_export(False, False)
        if not exported:
            return

        # Construct LUA code from GUI options
        cmd = ''
        # Common repeated text chunk
        cmd_properties_prefix = 'ZomIslandGroups({Mode="SetGroupsProperties", WorkingSet="Visible", MergingPolicyString="A_ADD|AIB_ADD_A_VALUE_B|B_CLONE", GroupPaths={ "RootGroup" }, '

        # Load model
        cmd += 'ZomLoad({File={Path="'+self.conf.exportFile+'", ImportGroups=true, XYZUVW=true, UVWProps=true}})\n'

        # cmd += 'ZomUvset({Mode="SetCurrent", Name="Channel%s"})\n' % str(self.label_uvmap.text())
        cmd += 'ZomUvset({Mode="SetCurrent", Name="%s"})\n' % current_uv
        # cmd += 'ZomSet({Path = "Vars.Viewport.ViewportUV.WorkingSet", Value = "Visible&Flat"})\n'

        # cmd += 'ZomSet({Path="Prefs.PackOptions.MapResolution", Value=%i})\n' % self.dspin_pack_resolution.value()
        cmd += cmd_properties_prefix + 'Properties={Pack={Rotate={Step=90}}}})\n'
        cmd += cmd_properties_prefix + 'Properties={Pack={Rotate={Mode=0}}}})\n'

        margin = float(self.dspin_pack_margin.value()) / self.dspin_pack_resolution.value()
        spacing = float(self.dspin_pack_spacing.value()) / self.dspin_pack_resolution.value()
        cmd += cmd_properties_prefix + 'Properties={Pack={SpacingSize=%f}}})\n' % spacing
        cmd += cmd_properties_prefix + 'Properties={Pack={MarginSize=%f}}})\n' % margin

        quality = [128, 256, 512, 1024, 2048]
        cmd += cmd_properties_prefix + 'Properties={Pack={Resolution=%i}}})\n' % quality[self.combo_pack_quality.currentIndex()]
        cmd += cmd_properties_prefix + 'Properties={Pack={MaxMutations=%i}}})\n' % self.dspin_pack_mutations.value()

        init_scale = 0
        if self.cbx_initial_scale_avg.isChecked():
            init_scale = 2

        layout_scale = 0
        if self.cbx_layout_scaling.isChecked():
            layout_scale = 2

        cmd += 'ZomSet({Path="Prefs.PackOptions.__ScalingMode", Value=%i})\n' % init_scale
        cmd += 'ZomSave({File={Path="c:/users/root/appdata/local/temp/MayaRizomExport.fbx", UVWProps=true}, __UpdateUIObjFileName=true})\n'

        cmd += 'ZomIslandGroups({Mode="DistributeInTilesEvenly", WorkingSet="Visible&Flat", MergingPolicyString="A_ADD|AIB_ADD_A_VALUE_B|B_CLONE", UseTileLocks=true, UseIslandLocks=true})\n'
        cmd += 'ZomPack({RootGroup="RootGroup", WorkingSet="Visible&Flat", ProcessTileSelection=false, RecursionDepth=1, Translate=true, LayoutScalingMode=%i, Scaling={Mode=%i}})\n' % (layout_scale, init_scale)

        if DEBUG:
            print(cmd)
        self.write_to_lua_file(cmd)
        return

    def fbx_export(self):
        # FBX Export
        if not cmds.pluginInfo("fbxmaya", loaded=True, query=True):
            cmds.loadPlugin("fbxmaya")

        cmds.undoInfo(openChunk=True)
        mel.eval('ConvertInstanceToObject;')  # This is the only command that is important to undo.
        mel.eval('FBXExportSmoothingGroups -v true;')
        mel.eval('FBXExportTriangulate -v false;')
        mel.eval('FBXExportSmoothMesh -v false;')
        mel.eval('FBXExportUpAxis {};'.format(self.conf.upaxis))
        print('FBXExport -s -f "{}";'.format(self.conf.exportFile))
        mel.eval('FBXExport -s -f "{}";'.format(self.conf.exportFile))
        try:
            cmds.undo()
        except RuntimeError as RE:
            # There are no more commands to undo
            pass

        # End FBX Export
        return

    def riz_export(self, use_script=True, load_model=True):
        # displaySmoothness -divisionsU 0
        self.exported_objects = cmds.ls(selection=True, tr=True)

        # Exit preview smooth, because the FBXExportSmoothMesh option is not always respected by the exporter.
        cmds.displaySmoothness(du=0, dv=0, pw=4, ps=0, po=1)

        if self.cbx_custom_path.isChecked() and not self.field_custom_path.text() == self.conf.custompath:
            self.set_config()

        if self.link and self.cbx_use_link.isChecked():
            print("Rizom Link version", self.link.Version())

            # FBX Export
            self.fbx_export()
            if not self.port:
                self.riz_run()

            params = {
                "File.Path": self.conf.exportFile,
                "File.XYZUVW": True,  # 3D + UV data loaded (use File.XYZ instead to load 3D data only)
                "File.UVWProps": True,  # UVs properties such as pinning, texel density settings etc... will be loaded
                "File.ImportGroups": True,  # Island group hierarchy will be loaded
                "__Focus": True,  # Focus viewports on the loaded mesh
                # "Data.UseImportedUVWPolygons": False,
            }

            self.link.Load(params)

            if DEBUG: print(f"{PRNT_STRING} EXPORTED TO:", self.conf.exportFile)
            cmds.select(self.exported_objects)

            # Enable import button if it was disabled.
            self.btn_import.setEnabled(True)
        else:
            # Classic Method #
            print(f"{PRNT_STRING} Exporting model")
            self.cleanse_namespaces()  # Agressive cleanse
            if not self.exported_objects:
                return False

            # Delete history in case their are empty groups that would be removed by this action.
            # Otherwise they would be cleared during import and we have an object count missmatch.
            cmds.bakePartialHistory()
            cmd = ''

            # Export Options
            if load_model:
                if self.cbx_keepuv.isChecked():
                    cmd += 'ZomLoad({File={Path="'+self.conf.exportFile+'", ImportGroups=true, XYZUVW=true, UVWProps=true}})\n'
                else:
                    cmd += 'ZomLoad({File={Path="'+self.conf.exportFile+'", ImportGroups=true, XYZ=true}, NormalizeUVW=true})\n'

            # Add scripts
            if self.combo_scripts.currentIndex() and use_script is True:
                script_name = scriptlist.scripts[self.combo_scripts.currentIndex()-1][0]
                script_path = os.path.join(os.path.dirname(__file__), 'lua_scripts/%s' % script_name)
                with open(script_path, 'r') as lua_script:
                    cmd += lua_script.read()

            if DEBUG: print(f"{PRNT_STRING} {cmd}")

            # FBX Export
            self.fbx_export()

            if DEBUG: print(f"{PRNT_STRING} EXPORTED TO: {self.conf.exportFile}")
            cmds.select(self.exported_objects)

            self.write_to_lua_file(cmd)
            self.btn_import.setEnabled(True)
        return True

    def riz_import(self):
        if not os.path.exists(self.conf.exportFile):
            om.MGlobal.displayError("Could not locate exported file: %s" % self.conf.exportFile)
            self.btn_import.setEnabled(False)

        if self.cbx_use_link.isChecked():
            if self.link:
                try:
                    self.link.Save({"File.Path": self.conf.exportFile})
                except RuntimeError as RE:
                    cmds.error('Could not send Save command to Rizom over Python Link. Was it enabled when you exported?')

        # FBX Import
        namespace = ':RIZOMUV'
        if not cmds.namespace(ex=namespace):
            cmds.namespace(add=namespace)
        cmds.namespace(set=namespace)
        
        mel.eval('FBXImportMode -v add;')
        mel.eval('FBXImport -f "{}";'.format(self.conf.exportFile))
        # END FBX Import

        imported_objects = cmds.ls('RIZOMUV:*', long=True, type="transform")
        original_matches = []
        for riz_obj in imported_objects:
            print ("Imported object name", riz_obj)
            original = riz_obj.replace('RIZOMUV:', '')
            original_matches.append(original)

            # List UV sets of each item, skip if it has none. This is simply to exclude objects like group nodes.
            original_uvsets = cmds.polyUVSet(original, allUVSets=True, q=True)
            if not original_uvsets:
                print(f"Object {riz_obj} has no UVSets. Will not attempt UV Transfer")
                continue

            imported_uvsets = cmds.polyUVSet(riz_obj, allUVSets=True, q=True)

            if original_uvsets:
                # Check names #
                if self.cbx_fix_set_names.isChecked():
                    for i in range(len(original_uvsets)):
                        try:
                            if not original_uvsets[i] == imported_uvsets[i]:
                                cmds.polyUVSet(riz_obj, rename=True, uvSet=imported_uvsets[i], newUVSet=original_uvsets[i])
                        except IndexError:
                            # This can happen due to a weird Maya bug that I don't understand where the object has more
                            # uvSets listed with the polyUVSet comman, than it has in the UV Set Editor
                            print ("UV Set Index Error. Objects don't seem to have the same amount of UV sets")
                            print("Original UV Sets:", original_uvsets, original)
                            print("Imported UV Sets:", imported_uvsets, riz_obj)
                            pass
                try:
                    #cmds.polyTransfer(original, ao=riz_obj, ch=False, uv=True)
                    cmds.polyTransfer(original, ao=riz_obj, ch=False, vc=False, v=False, uv=True)
                except RuntimeError as rt:
                    print ("<RizomUV Bridge> Could not transfer UVs from", riz_obj, "to", original)
                if DEBUG: print ("<RizomUV Bridge> Transfering UVs from", riz_obj, "to", original)

        cmds.select(original_matches)
        cmds.bakePartialHistory()
        cmds.delete(':RIZOMUV:*')
        cmds.namespace(rm=':RIZOMUV')

        return

    def riz_link(self):
        """
        Establishes link with RizomUV. Even though this is just a single line, I want it in a function to refresh UI.
        """
        pass

    def browse_settings_location(self):
        os.startfile(os.path.dirname(self.conf.config_file_path))

    def ui_pack_update_labels(self):
        print("Value changed")
        self.label_uvmap.setText(str(self.slider_pack_uvmap.value()))

    def ui_update_uvchannels(self):
        sel_obj = cmds.ls(sl=True, tr=True)
        if not sel_obj:
            self.combo_pack_uvset.clear()
            return

        uvsets = cmds.polyUVSet(sel_obj[0], allUVSets=True, q=True)
        current_set = cmds.polyUVSet(sel_obj[0], cuv=True, q=True)
        if uvsets:
            print (uvsets)
            self.combo_pack_uvset.clear()
            self.combo_pack_uvset.addItems(uvsets)
            self.combo_pack_uvset.setCurrentIndex(uvsets.index(current_set[0]))

    def validate_export_path(self):
        if self.cbx_custom_path.isChecked():
            if not os.path.exists(self.field_custom_path.text()):
                self.btn_import.setEnabled(False)
                self.btn_export.setEnabled(False)
                self.field_custom_path.setStyleSheet("color: red")
                return
            else:
                self.conf.exportFile = os.path.join(self.conf.custompath, self.conf.objname)
                self.btn_import.setEnabled(True)
                self.btn_export.setEnabled(True)
                self.field_custom_path.setStyleSheet("color: white")
        else:
            self.conf.reset_export_path()
            self.field_custom_path.setStyleSheet("color: grey")
            self.btn_import.setEnabled(True)
            self.btn_export.setEnabled(True)

        print(self.conf.exportFile)

    def cleanse_namespaces(self):
        """ Step One --
            Try to delete all existing RIZOMUV namespaces until it fails, this should get rid of stacked instances like
            RIZOMUV:RIZOMUV:RIZOMUV
        """
        fail = False
        while(not fail):
            try:
                cmds.namespace(rm=':RIZOMUV', mnr=True)
            except:
                fail = True

        """ Step Two -- 
            In one scene I got the namespaces had gotten renamed to RIZOMUV1, RIZOMUV2, RIZOMUV3 etc
            so this finds any leftoverrs and deletes them.
        """
        # existing_ns = cmds.namespaceInfo(listNamespace=True, listOnlyNamespaces=True)
        # for entry in existing_ns:
        # 	if 'RIZOMUV' in entry:
        # 		cmds.namespace(rm=entry, mnr=True)
        #
        # return

        """ Step Two, updated --
            Let's try to remove other namespaces than simply RIZOM as having others can prevent the import from working
        """
        c = cmds.listRelatives(ad=True)
        if not c:
            return

        for obj in c:
            ns_split = obj.split(':')
            if len(ns_split)>1:
                result = cmds.confirmDialog(m="Selected objects have namespaces assigned. \n"
                                            "These must go before you can use the tool correctly\n"
                                            "Should I delete them for you? (Including on unselected objects)\n\n"
                                            "Namespace on object: \n%s" % ns_split[0], button=['Remove', 'Cancel'])
                if result == 'Remove':
                    cmds.namespace(rm=ns_split[0], mnr=True)
                else:
                    return
        return

    def write_to_lua_file(self, command):
        with open(self.conf.rizom_script_path, 'w') as f:
            f.write(command)
            print("<RIZOM> Wrote command to lua file:", self.conf.rizom_script_path)
            for line in command.split("\n"):
                print("\t", line)
        return

    def set_config(self):
        self.conf.loaduvs = self.cbx_keepuv.isChecked()

        if self.radioAxisY.isChecked():
            self.conf.upaxis = "Y"
        else:
            self.conf.upaxis = "Z"

        self.conf.mutations = self.dspin_pack_mutations.value()
        self.conf.resolution = self.dspin_pack_resolution.value()
        self.conf.margin = self.dspin_pack_margin.value()
        self.conf.spacing = self.dspin_pack_spacing.value()
        self.conf.autofit = self.cbx_layout_scaling.isChecked()
        self.conf.fixuvnames = self.cbx_fix_set_names.isChecked()
        self.conf.useuvlink = self.cbx_use_link.isChecked()
        self.conf.usecustompath = self.cbx_custom_path.isChecked()
        self.conf.custompath = self.field_custom_path.text()

        self.conf.save_xml()

    def closeEvent(self, event):
        self.conf.save_xml()


def GetMayaWidget():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def fix_shell_border_normals():
    obj_list = cmds.ls(sl=True, o=True)
    all_final_borders = []

    for sub_obj in obj_list:
        cmds.select(sub_obj, r=True)

        cmds.polyNormalPerVertex(ufn=True)
        cmds.polySoftEdge(sub_obj, a=180, ch=1)
        print("Soften all")

        # Select object UVs
        cmds.select(sub_obj + '.map[*]')
        mel.eval('polySelectBorderShell 1;')
        uv_border = cmds.polyListComponentConversion(te=True, internal=True)
        uv_border = cmds.ls(uv_border, fl=True)
        final_border = []

        # Magical filter
        for curEdge in uv_border:
            edge_uvs = cmds.polyListComponentConversion(curEdge, tuv=True)
            edge_uvs = cmds.ls(edge_uvs, fl=True)

            if len(edge_uvs) > 2:
                final_border.append(curEdge)

        cmds.polySoftEdge(final_border, a=0, ch=1)
        all_final_borders.append(final_border)

    cmds.select(cl=True)
    for sel_l in all_final_borders:
        cmds.select(sel_l, add=True)
    cmds.hilite(obj_list)

def run():
    scriptJobs = cmds.scriptJob(listJobs=True)
    for sj in scriptJobs:
        if "RizomBridge" in sj:
            print(PRNT_STRING, "Killing preexisting scriptJob:", sj)
            cmds.scriptJob(kill=int(sj.split(':')[0]))

    d = RizomUVBridgeWindow()
    d.show(dockable=True)


if __name__ == "__main__":
    run()

