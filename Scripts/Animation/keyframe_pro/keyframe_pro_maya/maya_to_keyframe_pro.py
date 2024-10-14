import datetime
import os
import shutil
import subprocess
import sys
import time
import traceback

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

from keyframe_pro.keyframe_pro_client import KeyframeProClient


class MayaToKeyframePro:

    WINDOW_NAME = "MayaToKeyframeProWindow"
    WINDOW_TITLE = "Keyframe Pro"

    VERSION = "1.0.1"

    KEYFRAME_PRO_PATH = "C:/Program Files/Keyframe Pro/bin/KeyframePro.exe"
    PORT = 18181

    SYNC_SCRIPT_NODE_NAME = "MayaToKeyframeProScriptNode"

    CACHED_TEMP_DIR_OPTION_VAR = "MayaToKeyframeProCachedTempDir"
    COLLAPSE_STATE_OPTION_VAR = "MayaToKeyframeProCollapseState"
    SYNC_OFFSET_OPTION_VAR = "MayaToKeyframeProSyncOffset"
    FROM_RANGE_START_OPTION_VAR = "MayaToKeyframeProFromRangeStart"

    WAIT_FOR_OPEN_DURATION = 1  # Seconds to sleep after trying to open the application

    BUTTON_COLOR_01 = (0.5, 0.5, 0.5)
    BUTTON_COLOR_02 = (0.361, 0.361, 0.361)

    SYNC_ACTIVE_COLOR = (0.0, 0.5, 0.0)

    kpro_client = None

    main_window = None
    sync_layout = None
    viewer_layout = None
    playblast_layout = None

    sync_from_range_start_cb = None
    sync_offset_ifg = None
    playblast_viewer_rbg = None

    @classmethod
    def open_keyframe_pro(cls, application_path=""):
        if not application_path:
            application_path = cls.KEYFRAME_PRO_PATH

        if not application_path:
            om.MGlobal.displayError("Keyframe Pro application path not set.")
        elif not os.path.exists(application_path):
            om.MGlobal.displayError("Keyframe Pro application path does not exist: {0}".format(application_path))
        else:
            try:
                subprocess.Popen(cls.KEYFRAME_PRO_PATH, shell=False, stdin=None, stdout=None, stderr=None)
            except:
                traceback.print_exc()
                om.MGlobal.displayError("Failed to open Keyframe Pro. See script editor for details.")

    @classmethod
    def is_initialized(cls, display_errors=True):
        if not cls.kpro_client:
            cls.kpro_client = KeyframeProClient()

        if cls.kpro_client.connect(port=cls.PORT, display_errors=display_errors):
            if cls.kpro_client.initialize():
                return True
        else:
            if display_errors:
                om.MGlobal.displayError("Connection failed. Application may be closed or the port may be in use ({0}).".format(cls.PORT))

        if display_errors:
            om.MGlobal.displayError("Failed to connect to Keyframe Pro. See script editor for details.")

        return False

    @classmethod
    def toggle_sync(cls):
        if not cls.sync_script_node_exists() and cls.is_initialized():
            cls.create_sync_script_node()
            if cls.sync_script_node_exists():
                cls.update_sync_time()
        else:
            cls.delete_sync_script_node()

        cls.update_sync_state()

    @classmethod
    def update_sync_time(cls):
        if cls.is_initialized():
            frame = cmds.currentTime(q=True) + cls.get_sync_offset()

            if cls.get_from_range_start():
                range = cls.kpro_client.get_range()
                if range:
                    frame += range[0] - 1

            cls.kpro_client.set_frame(frame)

    @classmethod
    def set_viewer_layout(cls, layout):
        if cls.is_initialized():
            cls.kpro_client.set_viewer_layout(layout)

    @classmethod
    def swap_timelines(cls):
        if cls.is_initialized():
            a = cls.kpro_client.get_active_in_viewer(0)
            b = cls.kpro_client.get_active_in_viewer(1)
            if b:
                cls.kpro_client.set_active_in_viewer(b["id"], 0)
            if a:
                cls.kpro_client.set_active_in_viewer(a["id"], 1)

    @classmethod
    def playblast(cls):

        format = cls.get_option_var("playblastFormat", "avi")
        ext = ""
        if format == "avi":
            ext = "avi"
        elif format == "qt":
            ext = "mov"
        else:
            om.MGlobal.displayError("Current playblast format is image. Images are not supported in the current version of Keyframe Pro")
            return

        temp_dir = cls.get_temp_dir()
        if not temp_dir:
            return

        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        name = "blast"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = "{0}/{1}_{2}.{3}".format(temp_dir, name, timestamp, ext)

        clear_cache = cls.get_option_var("playblastClearCache", True)
        show_ornaments = cls.get_option_var("playblastShowOrnaments", False)
        compression = cls.get_option_var("playblastCompression", "none")
        quality = cls.get_option_var("playblastQuality", 70)
        percent = cls.get_option_var("playblastScale", 0.5) * 100
        padding = cls.get_option_var("playblastPadding", 4)
        display_source_size = cls.get_option_var("playblastDisplaySizeSource", 1)
        playblast_width = cls.get_option_var("playblastWidth", 720)
        playblast_height = cls.get_option_var("playblastHeight", 480)

        args = {"format": format,
                "clearCache": clear_cache,
                "viewer": False,
                "showOrnaments": show_ornaments,
                "fp": padding,
                "percent": percent,
                "compression": compression,
                "quality": quality,
                "filename": file_path
                }

        if display_source_size == 2:
            args["widthHeight"] = [cmds.getAttr("defaultResolution.w"), cmds.getAttr("defaultResolution.h")]
        elif display_source_size == 3:
            args["widthHeight"] = [playblast_width, playblast_height]

        playback_slider = mel.eval("$tempVar = $gPlayBackSlider")
        if(cmds.timeControl(playback_slider, q=True, rv=True)):
            range = cmds.timeControl(playback_slider, q=True, ra=True)
            args["startTime"] = range[0]
            args["endTime"] = range[1]

        sound = cmds.timeControl(playback_slider, q=True, sound=True)
        if sound:
            args["sound"] = sound

        file_path = cmds.playblast(**args)
        om.MGlobal.displayInfo(file_path)

        # Open in viewer
        viewer_index = cmds.radioButtonGrp(cls.playblast_viewer_rbg, q=True, select=True) - 1
        if viewer_index <= 1:
            if not cls.is_initialized(False):
                cls.open_keyframe_pro()
                time.sleep(cls.WAIT_FOR_OPEN_DURATION)

                if not cls.is_initialized():
                    om.MGlobal.displayError("Failed to open in viewer. See script editor for details.")
                    return

            if viewer_index >= 0 and viewer_index <= 1:
                # On import, source may be loaded into A. Restore current A if source is to be in B
                source_in_a = None
                if viewer_index > 0:
                    source_in_a = cls.kpro_client.get_active_in_viewer(0)

                # Swap
                source = cls.kpro_client.import_file(file_path)
                if source:
                    cls.kpro_client.set_active_in_viewer(source["id"], viewer_index)
                if source_in_a:
                    cls.kpro_client.set_active_in_viewer(source_in_a["id"], 0)

    @classmethod
    def get_option_var(cls, name, default):
        if cmds.optionVar(exists=name):
            return cmds.optionVar(q=name)
        else:
            return default

    @classmethod
    def open_temp_dir(cls):
        temp_dir = cls.get_temp_dir()
        if temp_dir:
            if sys.platform == "win32":
                os.startfile(temp_dir, 'explore')
            else:
                om.MGlobal.displayError("Open temp dir is not supported on the current platform ({0})".format(sys.platform))

    @classmethod
    def clear_temp_dir(cls):
        result = cmds.confirmDialog(title='Confirm',
                                    message='Clear temporary directory?',
                                    button=['Yes', 'No'],
                                    defaultButton='Yes',
                                    cancelButton='No',
                                    dismissString='No')
        if result == "Yes":
            temp_dir = cls.get_temp_dir()
            if temp_dir:
                errors_occurred = False

                for the_file in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except:
                        om.MGlobal.displayWarning("Failed to remove file: {0}".format(file_path))
                        om.MGlobal.displayWarning("File may be open in an application")
                        errors_occurred = True

                if errors_occurred:
                    om.MGlobal.displayWarning("Unable to remove all files. See script editor for details.")
                else:
                    om.MGlobal.displayInfo("Temporary directory cleared: {0}".format(temp_dir))

    @classmethod
    def get_temp_dir(cls):
        if cls.is_initialized(display_errors=False):
            config = cls.kpro_client.get_config()
            if config:
                cmds.optionVar(sv=[cls.CACHED_TEMP_DIR_OPTION_VAR, config["temp_dir"]])
                return config["temp_dir"]

        temp_dir = cls.get_option_var(cls.CACHED_TEMP_DIR_OPTION_VAR, "")
        if not temp_dir:
            om.MGlobal.displayWarning("Unable to get temporary directory.")

        return temp_dir

    @classmethod
    def sync_script_node_exists(cls):
        return cmds.objExists(cls.SYNC_SCRIPT_NODE_NAME)

    @classmethod
    def create_sync_script_node(cls):
        if not cls.sync_script_node_exists():
            cmds.scriptNode(scriptType=7,
                            beforeScript="try: MayaToKeyframePro.update_sync_time()\nexcept: pass",
                            name=cls.SYNC_SCRIPT_NODE_NAME,
                            sourceType="python")

    @classmethod
    def delete_sync_script_node(cls):
        if cls.sync_script_node_exists():
            cmds.delete(cls.SYNC_SCRIPT_NODE_NAME)

    @classmethod
    def get_sync_offset(cls):
        if cmds.optionVar(exists=cls.SYNC_OFFSET_OPTION_VAR):
            return cmds.optionVar(q=cls.SYNC_OFFSET_OPTION_VAR)
        else:
            return 0

    @classmethod
    def set_sync_offset(cls, value):
        cmds.intFieldGrp(cls.sync_offset_ifg, e=True, value1=value)
        cmds.optionVar(iv=[cls.SYNC_OFFSET_OPTION_VAR, value])
        if (cls.sync_script_node_exists()):
            cls.update_sync_time()

    @classmethod
    def sync_offset_to_current(cls):
        cls.set_sync_offset(-cmds.currentTime(q=True) + 1)

    @classmethod
    def sync_offset_changed(cls):
        cls.set_sync_offset(cmds.intFieldGrp(cls.sync_offset_ifg, q=True, value1=True))

    @classmethod
    def get_from_range_start(cls):
        if cmds.optionVar(exists=cls.FROM_RANGE_START_OPTION_VAR):
            return cmds.optionVar(q=cls.FROM_RANGE_START_OPTION_VAR)
        else:
            return 1

    @classmethod
    def update_from_range_start(cls):
        value = cmds.checkBox(cls.sync_from_range_start_cb, q=True, value=True)
        cmds.optionVar(iv=[cls.FROM_RANGE_START_OPTION_VAR, value])

        if cls.sync_script_node_exists():
            cls.update_sync_time()

    @classmethod
    def get_collapse_state(cls):
        if cmds.optionVar(exists=cls.COLLAPSE_STATE_OPTION_VAR):
            collapse_state = cmds.optionVar(q=cls.COLLAPSE_STATE_OPTION_VAR)
            if len(collapse_state) == 3:
                for value in collapse_state:
                    if value < 0 or value > 1:
                        return [0, 1, 1]

                return collapse_state

        return [0, 1, 1]

    @classmethod
    def update_collapse_state(cls):
        cmds.optionVar(clearArray=cls.COLLAPSE_STATE_OPTION_VAR)
        layouts = [cls.sync_layout, cls.viewer_layout, cls.playblast_layout]
        for layout in layouts:
            collapse = cmds.frameLayout(layout, q=True, cl=True)
            cmds.optionVar(iva=[cls.COLLAPSE_STATE_OPTION_VAR, collapse])

    @classmethod
    def display(cls):

        if cmds.window(cls.WINDOW_NAME, exists=True):
            cmds.deleteUI(cls.WINDOW_NAME, window=True)

        collapse_state = cls.get_collapse_state()

        # ---------------------------------------------------------------------
        # Main layout
        # ---------------------------------------------------------------------
        cls.main_window = cmds.window(cls.WINDOW_NAME, title=cls.WINDOW_TITLE, s=True, tlb=False, rtf=True, mnb=False, mxb=False)
        main_layout = cmds.formLayout(parent=cls.main_window)

        cls.sync_layout = cmds.frameLayout(parent=main_layout,
                                           label="Sync", collapsable=True,
                                           cl=collapse_state[0],
                                           cc=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"),
                                           ec=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"))
        sync_form_layout = cmds.formLayout(parent=cls.sync_layout)

        cls.viewer_layout = cmds.frameLayout(parent=main_layout,
                                             label="Viewer",
                                             collapsable=True,
                                             cl=collapse_state[1],
                                             cc=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"),
                                             ec=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"))
        viewer_form_layout = cmds.formLayout(parent=cls.viewer_layout)

        cls.playblast_layout = cmds.frameLayout(parent=main_layout,
                                                label="Playblast",
                                                collapsable=True,
                                                cl=collapse_state[2],
                                                cc=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"),
                                                ec=lambda *args: cmds.evalDeferred("MayaToKeyframePro.on_collapse_changed()"))
        playblast_form_layout = cmds.formLayout(parent=cls.playblast_layout)

        cmds.formLayout(main_layout, e=True, af=(cls.sync_layout, "top", 0))
        cmds.formLayout(main_layout, e=True, af=(cls.sync_layout, "left", 0))
        cmds.formLayout(main_layout, e=True, af=(cls.sync_layout, "right", 0))

        cmds.formLayout(main_layout, e=True, ac=(cls.viewer_layout, "top", 0, cls.sync_layout))
        cmds.formLayout(main_layout, e=True, af=(cls.viewer_layout, "left", 0))
        cmds.formLayout(main_layout, e=True, af=(cls.viewer_layout, "right", 0))

        cmds.formLayout(main_layout, e=True, ac=(cls.playblast_layout, "top", 0, cls.viewer_layout))
        cmds.formLayout(main_layout, e=True, af=(cls.playblast_layout, "left", 0))
        cmds.formLayout(main_layout, e=True, af=(cls.playblast_layout, "right", 0))

        # ---------------------------------------------------------------------
        # Sync layout
        # ---------------------------------------------------------------------
        cls.sync_offset_ifg = cmds.intFieldGrp(label="Offset: ",
                                               value1=MayaToKeyframePro.get_sync_offset(),
                                               columnWidth2=(40, 48),
                                               cl2=("left", "right"),
                                               cc=lambda *args: MayaToKeyframePro.sync_offset_changed(),
                                               parent=sync_form_layout)

        cls.sync_from_range_start_cb = cmds.checkBox(label="From Range Start",
                                                     value=MayaToKeyframePro.get_from_range_start(),
                                                     cc=lambda *args: MayaToKeyframePro.update_from_range_start(),
                                                     parent=sync_form_layout)

        sync_offset_to_current_btn = cmds.button(label="Current",
                                                 bgc=cls.BUTTON_COLOR_01,
                                                 c=lambda *args: MayaToKeyframePro.sync_offset_to_current(),
                                                 parent=sync_form_layout)

        reset_sync_offset_btn = cmds.button(label="  Reset  ",
                                            bgc=cls.BUTTON_COLOR_01,
                                            c=lambda *args: MayaToKeyframePro.set_sync_offset(0),
                                            parent=sync_form_layout)

        cls.sync_btn = cmds.button(label="SYNC", c=lambda *args: MayaToKeyframePro.toggle_sync(), parent=sync_form_layout)

        top_offset = 1
        bottom_offset = 4
        left_position = 1
        right_position = 99
        spacing = 2
        cmds.formLayout(sync_form_layout, e=True, af=(cls.sync_offset_ifg, "top", top_offset))
        cmds.formLayout(sync_form_layout, e=True, ap=(cls.sync_offset_ifg, "left", 0, left_position))

        cmds.formLayout(sync_form_layout, e=True, af=(sync_offset_to_current_btn, "top", top_offset))
        cmds.formLayout(sync_form_layout, e=True, ac=(sync_offset_to_current_btn, "left", 0, cls.sync_offset_ifg))

        cmds.formLayout(sync_form_layout, e=True, af=(reset_sync_offset_btn, "top", top_offset))
        cmds.formLayout(sync_form_layout, e=True, ac=(reset_sync_offset_btn, "left", spacing, sync_offset_to_current_btn))

        cmds.formLayout(sync_form_layout, e=True, ac=(cls.sync_from_range_start_cb, "top", top_offset, sync_offset_to_current_btn))
        cmds.formLayout(sync_form_layout, e=True, ap=(cls.sync_from_range_start_cb, "left", 0, left_position))

        cmds.formLayout(sync_form_layout, e=True, ac=(cls.sync_btn, "top", 2 * spacing, cls.sync_from_range_start_cb))
        cmds.formLayout(sync_form_layout, e=True, af=(cls.sync_btn, "bottom", bottom_offset))
        cmds.formLayout(sync_form_layout, e=True, ap=(cls.sync_btn, "left", 0, left_position))
        cmds.formLayout(sync_form_layout, e=True, ap=(cls.sync_btn, "right", 0, right_position))

        # ---------------------------------------------------------------------
        # Viewer layout
        # ---------------------------------------------------------------------
        single_viewer_btn = cmds.button(label="Single",
                                        bgc=cls.BUTTON_COLOR_01,
                                        c=lambda *args: MayaToKeyframePro.set_viewer_layout('single'),
                                        parent=viewer_form_layout)

        hori_viewer_btn = cmds.button(label="Horizontal",
                                      bgc=cls.BUTTON_COLOR_01,
                                      c=lambda *args: MayaToKeyframePro.set_viewer_layout('horizontal'),
                                      parent=viewer_form_layout)

        vert_viewer_btn = cmds.button(label=" Vertical ",
                                      bgc=cls.BUTTON_COLOR_01,
                                      c=lambda *args: MayaToKeyframePro.set_viewer_layout('vertical'),
                                      parent=viewer_form_layout)

        swap_timelines_btn = cmds.button(label="Swap Timelines",
                                         bgc=cls.BUTTON_COLOR_01,
                                         c=lambda *args: MayaToKeyframePro.swap_timelines(),
                                         parent=viewer_form_layout)

        cmds.formLayout(viewer_form_layout, e=True, af=(single_viewer_btn, "top", top_offset))
        cmds.formLayout(viewer_form_layout, e=True, ap=(single_viewer_btn, "left", 0, left_position))
        cmds.formLayout(viewer_form_layout, e=True, ap=(single_viewer_btn, "right", 0, 38))

        cmds.formLayout(viewer_form_layout, e=True, af=(hori_viewer_btn, "top", top_offset))
        cmds.formLayout(viewer_form_layout, e=True, ac=(hori_viewer_btn, "left", spacing, single_viewer_btn))
        cmds.formLayout(viewer_form_layout, e=True, ap=(hori_viewer_btn, "right", 0, 68))

        cmds.formLayout(viewer_form_layout, e=True, af=(vert_viewer_btn, "top", top_offset))
        cmds.formLayout(viewer_form_layout, e=True, ac=(vert_viewer_btn, "left", spacing, hori_viewer_btn))
        cmds.formLayout(viewer_form_layout, e=True, ap=(vert_viewer_btn, "right", 0, right_position))

        cmds.formLayout(viewer_form_layout, e=True, ac=(swap_timelines_btn, "top", spacing, single_viewer_btn))
        cmds.formLayout(viewer_form_layout, e=True, af=(swap_timelines_btn, "bottom", bottom_offset))
        cmds.formLayout(viewer_form_layout, e=True, ap=(swap_timelines_btn, "left", 0, left_position))
        cmds.formLayout(viewer_form_layout, e=True, ap=(swap_timelines_btn, "right", 0, right_position))

        # ---------------------------------------------------------------------
        # Playblast layout
        # ---------------------------------------------------------------------
        cls.playblast_viewer_rbg = cmds.radioButtonGrp(label='Open in Viewer:   ',
                                                       labelArray3=['A', 'B', 'None'],
                                                       numberOfRadioButtons=3,
                                                       select=1,
                                                       cw4=(100, 40, 40, 40),
                                                       cl4=("left", "left", "left", "left"),
                                                       parent=playblast_form_layout)

        playblast_btn = cmds.button(label="PLAYBLAST",
                                    bgc=cls.BUTTON_COLOR_01,
                                    c=lambda *args: MayaToKeyframePro.playblast(),  
                                    parent=playblast_form_layout)

        open_temp_dir_btn = cmds.button(label="Open Temp Folder",
                                        bgc=cls.BUTTON_COLOR_01,
                                        c=lambda *args: MayaToKeyframePro.open_temp_dir(),  
                                        parent=playblast_form_layout)

        clear_temp_dir_btn = cmds.button(label="Clear Temp Folder",
                                         bgc=cls.BUTTON_COLOR_01,
                                         c=lambda *args: MayaToKeyframePro.clear_temp_dir(),  
                                         parent=playblast_form_layout)
        
        version_label = cmds.text(label="v{0}".format(cls.VERSION), align="right")

        cmds.formLayout(playblast_form_layout, e=True, af=(cls.playblast_viewer_rbg, "top", top_offset))
        cmds.formLayout(playblast_form_layout, e=True, ap=(cls.playblast_viewer_rbg, "left", 0, left_position))

        cmds.formLayout(playblast_form_layout, e=True, ac=(playblast_btn, "top", spacing, cls.playblast_viewer_rbg))
        cmds.formLayout(playblast_form_layout, e=True, ap=(playblast_btn, "left", 0, left_position))
        cmds.formLayout(playblast_form_layout, e=True, ap=(playblast_btn, "right", 0, right_position))

        cmds.formLayout(playblast_form_layout, e=True, ac=(open_temp_dir_btn, "top", spacing, playblast_btn))
        cmds.formLayout(playblast_form_layout, e=True, ap=(open_temp_dir_btn, "left", 0, left_position))
        cmds.formLayout(playblast_form_layout, e=True, ap=(open_temp_dir_btn, "right", 1, 50))

        cmds.formLayout(playblast_form_layout, e=True, ac=(clear_temp_dir_btn, "top", spacing, playblast_btn))
        cmds.formLayout(playblast_form_layout, e=True, ap=(clear_temp_dir_btn, "left", 1, 50))
        cmds.formLayout(playblast_form_layout, e=True, ap=(clear_temp_dir_btn, "right", 0, right_position))

        cmds.formLayout(playblast_form_layout, e=True, ac=(version_label, "top", spacing, open_temp_dir_btn))
        cmds.formLayout(playblast_form_layout, e=True, ap=(version_label, "right", 0, right_position))

        # ---------------------------------------------------------------------
        # Update and show
        # ---------------------------------------------------------------------
        cls.update_sync_state()
        cls.on_collapse_changed()
        cmds.setFocus(cls.sync_btn)

        cmds.showWindow(cls.main_window)

    @classmethod
    def on_collapse_changed(cls):
        total_height = 0
        layouts = [cls.sync_layout, cls.viewer_layout, cls.playblast_layout]
        for layout in layouts:
            total_height += cmds.frameLayout(layout, q=True, h=True)

        cmds.window(MayaToKeyframePro.main_window, e=True, h=total_height)
        cls.update_collapse_state()

    @classmethod
    def update_sync_state(cls):
        if cls.sync_script_node_exists():
            cmds.button(cls.sync_btn, e=True, bgc=cls.SYNC_ACTIVE_COLOR, label="SYNCED")
        else:
            cmds.button(cls.sync_btn, e=True, bgc=cls.BUTTON_COLOR_01, label="SYNC")


if __name__ == "__main__":
    MayaToKeyframePro.display()
