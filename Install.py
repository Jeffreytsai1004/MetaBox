#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===================================== 1. Module Imports =====================================
# Standard library imports
import os
import sys
import webbrowser

# Maya imports
import maya.mel as mel
import maya.cmds as cmds
import maya.OpenMayaUI as omui

# Qt imports
from PySide2 import QtWidgets, QtGui, QtCore
from shiboken2 import wrapInstance

#===================================== 2. Global Variables =====================================
# Path configurations
try:
    ROOT_PATH = os.path.dirname(INSTALL_PATH)
except NameError:
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# Tool information
TOOL_NAME = "MetaBox"
TOOL_VERSION = "Beta v1.0.0"
TOOL_AUTHOR = "Virtuos"
TOOL_LANG = 'en_US'
SCRIPTS_PATH = os.path.join(ROOT_PATH, "Scripts")
ICONS_PATH = os.path.join(ROOT_PATH, "icons")
TOOL_ICON = os.path.join(ICONS_PATH, "logo.png")
DEFAULT_ICON = "commandButton.png"
TOOL_HELP_URL = f"http://10.72.61.59:3000/ArtGroup/{TOOL_NAME}/wiki"
TOOL_WSCL_NAME = "ToolBoxWorkSpaceControl"
MOD_FILE_NAME = f"{TOOL_NAME}.mod"
MAIN_SCRIPT_NAME = f"{TOOL_NAME}.py"

# UI Style configurations
BUTTON_STYLE = """
    QPushButton {
        background-color: #D0D0D0;
        color: #303030;
        border-radius: 10px;
        padding: 5px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #E0E0E0;
    }
    QPushButton:pressed {
        background-color: #C0C0C0;
    }
"""

MESSAGE_BUTTON_STYLE = """
    QPushButton {
        background-color: #B0B0B0;
        color: #303030;
        border-radius: 10px;
        padding: 5px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #C0C0C0;
    }
    QPushButton:pressed {
        background-color: #A0A0A0;
    }
"""

#===================================== 3. Utility Functions =====================================
def maya_main_window():
    """Get Maya main window as QWidget"""
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

def ensure_directory(directory_path):
    """Ensure directory exists, create if not"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")
    return directory_path

def get_maya_modules_dir():
    """Get Maya modules directory path"""
    maya_app_dir = cmds.internalVar(userAppDir=True)
    return ensure_directory(os.path.join(maya_app_dir, "modules"))

#===================================== 4. UI Component Classes =====================================
class SetButton(QtWidgets.QPushButton):
    """Custom styled button for installation interface"""
    def __init__(self, text):
        super(SetButton, self).__init__(text)
        self.setStyleSheet(BUTTON_STYLE)

#===================================== 5. Main Window Class =====================================
class InstallDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(InstallDialog, self).__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize and setup UI components"""
        self.setWindowTitle(f"{TOOL_NAME} Installation")
        self.setFixedSize(220, 120)
        self.setup_window_icon()
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def setup_window_icon(self):
        """Setup window icon if available"""
        if os.path.exists(TOOL_ICON):
            self.setWindowIcon(QtGui.QIcon(TOOL_ICON))
        else:
            print(f"Warning: Icon file not found: {TOOL_ICON}")

    #----------------- 5.1 UI Methods -----------------
    def create_widgets(self):
        self.new_shelf_toggle = QtWidgets.QCheckBox(f"{TOOL_NAME} Installation")
        self.install_button = SetButton("Install " + TOOL_NAME) 
        self.uninstall_button = SetButton("Uninstall " + TOOL_NAME)

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 2, 10, 5)
        main_layout.setSpacing(5)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setSpacing(5)

        welcome_label = QtWidgets.QLabel("Welcome to " + TOOL_NAME + "!")
        welcome_label.setStyleSheet("font-size: 11px; padding: 0px; margin: 0px;")
        header_layout.addWidget(welcome_label)
        header_layout.addStretch()

        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.install_button)
        main_layout.addWidget(self.uninstall_button)

        self.install_button.setFixedHeight(30)
        self.uninstall_button.setFixedHeight(30)

    def create_connections(self):
        self.install_button.clicked.connect(self.install)
        self.uninstall_button.clicked.connect(self.uninstall)

    def create_styled_message_box(self, title, text):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        button_style = """
        QPushButton {
            background-color: #B0B0B0;
            color: #303030;
            border-radius: 10px;
            padding: 5px;
            font-weight: bold;
            min-width: 80px;
        }
        QPushButton:hover {
            background-color: #C0C0C0;
        }
        QPushButton:pressed {
            background-color: #A0A0A0;
        }
        """
        
        for button in msg_box.buttons():
            button.setStyleSheet(button_style)
        
        return msg_box
    
    #----------------- 5.2 Event Handler Methods -----------------
    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QtWidgets.QWhatsThis.leaveWhatsThisMode()
            self.open_help_url()
            return True
        return QtWidgets.QDialog.event(self, event)
    
    def closeEvent(self, event):
        """Handle window close event"""
        try:
            super(InstallDialog, self).closeEvent(event)
        except Exception as e:
            print(f"Error closing window: {e}")
            event.accept()

    def helpEvent(self, event):
        self.open_help_url()
        event.accept()

    #----------------- 5.3 Utility Methods -----------------
    def open_help_url(self):
        webbrowser.open(TOOL_HELP_URL)
        QtWidgets.QApplication.restoreOverrideCursor()

    def get_script_path(self):
        maya_script = mel.eval('getenv("MAYA_SCRIPT_NAME")')
        if maya_script and os.path.exists(maya_script):
            return os.path.dirname(maya_script)
            
        for sys_path in sys.path:
            install_path = os.path.join(sys_path, "install.py")
            if os.path.exists(install_path):
                return os.path.dirname(install_path)
                
        return os.getcwd()
    
    #----------------- 5.4 Installation Methods -----------------
    def install(self):
        """Handle install request with error handling"""
        if not self._validate_paths():
            return

        msg_box = self.create_styled_message_box(
            "Confirm Installation",
            f"Are you sure you want to install {TOOL_NAME}?"
        )
        if msg_box.exec_() == QtWidgets.QMessageBox.Yes:
            try:
                self.install_tool()
                self.close()
            except Exception as e:
                error_msg = f"Error during installation: {e}"
                print(error_msg)
                QtWidgets.QMessageBox.critical(self, "Error", error_msg)

    def uninstall(self, *args):
        """Handle uninstall request"""
        msg_box = self.create_styled_message_box(
            "Confirm Uninstallation",
            f"Are you sure you want to uninstall {TOOL_NAME}?"
        )
        
        if msg_box.exec_() == QtWidgets.QMessageBox.Yes:
            try:
                self.uninstall_tool()
                self.close()
            except Exception as e:
                error_msg = f"Error during uninstallation: {e}"
                print(error_msg)
                QtWidgets.QMessageBox.critical(self, "Error", error_msg)
        else:
            print("Uninstallation cancelled")

    def create_mod_file(self):
        """Create or update the .mod file for Maya"""
        modules_dir = get_maya_modules_dir()
        mod_content = f"""+ {TOOL_NAME} 1.0 {ROOT_PATH}
        scripts: {SCRIPTS_PATH}
        """
        mod_file_path = os.path.join(modules_dir, MOD_FILE_NAME)
        self._write_mod_file(mod_file_path, mod_content)

    def _write_mod_file(self, file_path, content):
        """Helper method to write .mod file"""
        try:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Successfully created/updated: {file_path}")
        except Exception as e:
            error_msg = f"Error writing .mod file: {e}"
            print(error_msg)
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)

    def uninstall_mod_file(self):
        modules_dir = get_maya_modules_dir()
        mod_file_path = os.path.join(modules_dir, MOD_FILE_NAME)
        if os.path.exists(mod_file_path):
            try:
                os.remove(mod_file_path)
                print(f"{TOOL_NAME}.mod file deleted")
            except Exception as e:
                print(f"Error deleting {TOOL_NAME}.mod file: {e}")
    
    def clean_existing_buttons(self):
        if cmds.shelfLayout(TOOL_NAME, exists=True):
            buttons = cmds.shelfLayout(TOOL_NAME, query=True, childArray=True) or []
            for btn in buttons:
                if cmds.shelfButton(btn, query=True, exists=True):
                    label = cmds.shelfButton(btn, query=True, label=True) 
                    if label == TOOL_NAME:
                        cmds.deleteUI(btn)
                        print(f"Deleted existing {TOOL_NAME} button: {btn}")

    def install_tool(self):
        """Install the tool to Maya"""
        if not os.path.exists(SCRIPTS_PATH):
            print(f"Error: Scripts path does not exist: {SCRIPTS_PATH}")
            return

        main_script = os.path.join(SCRIPTS_PATH, MAIN_SCRIPT_NAME)
        if not os.path.exists(main_script):
            print(f"Error: Main script file not found: {main_script}")
            return

        # Add scripts path to Python path
        if SCRIPTS_PATH not in sys.path:
            sys.path.insert(0, SCRIPTS_PATH)

        # Create shelf and button
        self._create_shelf_button()
        self.create_mod_file()
        
        # 切换到新创建的工具架
        try:
            cmds.shelfTabLayout("ShelfLayout", edit=True, selectTab=TOOL_NAME)
            print(f"Switched to {TOOL_NAME} shelf")
        except Exception as e:
            print(f"Error switching to {TOOL_NAME} shelf: {e}")
        
        self._show_install_success_message()

    def _create_shelf_button(self):
        """Create shelf button for the tool"""
        shelf_layout = mel.eval('$tmpVar=$gShelfTopLevel')
        
        # Create shelf if not exists
        if not cmds.shelfLayout(TOOL_NAME, exists=True):
            cmds.shelfLayout(TOOL_NAME, parent=shelf_layout)
        
        # Clean existing buttons
        self.clean_existing_buttons()

        # Create new button
        icon_path = TOOL_ICON if os.path.exists(TOOL_ICON) else DEFAULT_ICON
        
        command = self._get_shelf_button_command()
        
        cmds.shelfButton(
            parent=TOOL_NAME,
            image1=icon_path,
            label=TOOL_NAME,
            command=command,
            sourceType="python",
            annotation=f"{TOOL_NAME} {TOOL_VERSION}",
            noDefaultPopup=True,
            style="iconOnly"
        )

    def _get_shelf_button_command(self):
        """Get the command string for shelf button"""
        return f"""
import sys
import os
SCRIPTS_PATH = r'{SCRIPTS_PATH}'
if SCRIPTS_PATH not in sys.path:
    sys.path.insert(0, SCRIPTS_PATH)
os.chdir(SCRIPTS_PATH)
try:
    import {TOOL_NAME}
    {TOOL_NAME}.show()
except ImportError as e:
    print("Error importing {TOOL_NAME}:", str(e))
    print("Scripts path:", SCRIPTS_PATH)
    print("sys.path:", sys.path)
    print("Contents of Scripts folder:", os.listdir(SCRIPTS_PATH))
"""

    def uninstall_tool(self):
        """Uninstall the tool from Maya"""
        window_name = f"{TOOL_NAME}Window"
        dock_name = f"{TOOL_NAME}WindowDock"
        shelf_file = f"shelf_{TOOL_NAME}.mel"

        if cmds.window(window_name, exists=True):
            try:
                cmds.deleteUI(window_name)
            except Exception as e:
                print(f"Error closing {TOOL_NAME} window: {e}")

        if cmds.dockControl(dock_name, exists=True):
            try:
                cmds.deleteUI(dock_name)
            except Exception as e:
                print(f"Error closing docked {TOOL_NAME} window: {e}")

        self.uninstall_mod_file()

        # 移除工具架之前先获取当前工具架
        current_shelf = cmds.shelfTabLayout("ShelfLayout", query=True, selectTab=True)

        # 删除工具架和按钮
        if cmds.shelfLayout(TOOL_NAME, exists=True):
            try:
                cmds.deleteUI(TOOL_NAME, layout=True)
            except Exception as e:
                print(f"Error deleting {TOOL_NAME} shelf: {e}")

        self._clean_all_shelf_buttons()

        # 从Python路径中移除
        if SCRIPTS_PATH in sys.path:
            sys.path.remove(SCRIPTS_PATH)

        # 删除工具架文件
        shelf_path = os.path.join(
            cmds.internalVar(userAppDir=True),
            cmds.about(version=True),
            "prefs",
            "shelves",
            f"shelf_{TOOL_NAME}.mel"
        )
        
        if os.path.exists(shelf_path):
            try:
                os.remove(shelf_path)
            except Exception as e:
                print(f"Error deleting shelf file: {e}")

        # 如果当前工具架是被删除的工具架，切换到其他工具架
        if current_shelf == TOOL_NAME:
            shelves = cmds.shelfTabLayout("ShelfLayout", query=True, childArray=True)
            if shelves and len(shelves) > 0:
                cmds.shelfTabLayout("ShelfLayout", edit=True, selectTab=shelves[0])

        self._show_uninstall_success_message()

    def _clean_all_shelf_buttons(self):
        """Clean up all shelf buttons related to the tool"""
        all_shelves = cmds.shelfTabLayout("ShelfLayout", query=True, childArray=True) or []
        for shelf in all_shelves:
            shelf_buttons = cmds.shelfLayout(shelf, query=True, childArray=True) or []
            for btn in shelf_buttons:
                if cmds.shelfButton(btn, query=True, exists=True):
                    if cmds.shelfButton(btn, query=True, label=True) == TOOL_NAME:
                        cmds.deleteUI(btn)

    def _show_uninstall_success_message(self):
        """Show uninstallation success message"""
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Uninstallation Successful")
        msg_box.setText(f"{TOOL_NAME} has been successfully uninstalled!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

        for button in msg_box.buttons():
            button.setStyleSheet(MESSAGE_BUTTON_STYLE)

        msg_box.exec_()

    def _show_install_success_message(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Installation Successful")
        msg_box.setText(f"{TOOL_NAME} has been successfully installed!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        for button in msg_box.buttons():
            button.setStyleSheet(MESSAGE_BUTTON_STYLE)
        msg_box.exec_()

    def _validate_paths(self):
        """Validate all required paths exist"""
        paths = {
            "Root": ROOT_PATH,
            "Scripts": SCRIPTS_PATH,
            "Icons": ICONS_PATH
        }
        
        for name, path in paths.items():
            if not os.path.exists(path):
                error_msg = f"Error: {name} path does not exist: {path}"
                print(error_msg)
                QtWidgets.QMessageBox.critical(self, "Error", error_msg)
                return False
        return True

    def _log(self, message, error=False):
        """Log messages with timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        if error:
            QtWidgets.QMessageBox.critical(self, "Error", message)

    def _load_mel_shelf(self):
        """Load mel shelf file with error handling"""
        try:
            mel.eval(f'loadNewShelf "shelf_{TOOL_NAME}.mel"')
        except Exception as e:
            self._log(f"Error loading shelf file: {e}", error=True)

#===================================== 6. Main Function =====================================
def main():
    """Main entry point for the installer"""
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    dialog = InstallDialog()
    dialog.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

