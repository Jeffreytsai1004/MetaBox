import os
import sys
import webbrowser
import maya.mel as mel
from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

TOOLBOX_NAME = "MetaBox"
TOOLBOX_ICON = "MetaBox.png"
TOOLBOX_HELP_URL = "https://www.google.com"

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class RoundedButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super(RoundedButton, self).__init__(text)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #D0D0D0;
                color: #303030;
                border-radius: 10px;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #C0C0C0;
            }
            """
        )

class InstallDialog(QtWidgets.QDialog):

    # Widgets
    
    def __init__(self, parent=maya_main_window()):
        CURRENT_PATH = self.get_script_path()
        ICON_PATH = os.path.abspath(os.path.join(CURRENT_PATH, "Icons", TOOLBOX_ICON).replace("\\", "/"))
        super(InstallDialog, self).__init__(parent)
        self.setWindowTitle(f"{TOOLBOX_NAME} Installation")
        self.setFixedSize(220, 120)
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        else:
            print(f"Warning: Custom icon file '{ICON_PATH}' does not exist, will use default icon.")
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.new_shelf_toggle = QtWidgets.QCheckBox("MetaBox Installation")
        self.install_button = RoundedButton("Install " + TOOLBOX_NAME)
        self.uninstall_button = RoundedButton("Uninstall " + TOOLBOX_NAME)

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 2, 10, 5)
        main_layout.setSpacing(5)

        toggle_layout = QtWidgets.QHBoxLayout()
        toggle_layout.setSpacing(5)

        label = QtWidgets.QLabel("Welcome to "+TOOLBOX_NAME+"!")
        label.setStyleSheet("font-size: 11px; padding: 0px; margin: 0px;")
        toggle_layout.addWidget(label)
        toggle_layout.addStretch()
        
        main_layout.addLayout(toggle_layout)
        main_layout.addWidget(self.install_button)
        main_layout.addWidget(self.uninstall_button)

        self.install_button.setFixedHeight(30)
        self.uninstall_button.setFixedHeight(30)

    def create_connections(self):
        self.install_button.clicked.connect(self.install_metabox)
        self.uninstall_button.clicked.connect(self.uninstall_metabox)

    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QtWidgets.QWhatsThis.leaveWhatsThisMode()
            self.open_help_url()
            return True
        return QtWidgets.QDialog.event(self, event)
    
    def open_help_url(self):
        webbrowser.open(TOOLBOX_HELP_URL)
        QtWidgets.QApplication.restoreOverrideCursor()

    def closeEvent(self, event):
        super(InstallDialog, self).closeEvent(event)

    def helpEvent(self, event):
        self.open_help_url()
        event.accept()

    def create_styled_message_box(self, title, text):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        # Set button style
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
    
    def install(self):
        msg_box = self.create_styled_message_box(
            "Confirm Installation",
            f"Are you sure you want to install {TOOLBOX_NAME}?"
        )
        result = msg_box.exec_()
        
        if result == QtWidgets.QMessageBox.Yes:
            self.close()
            self.install_metabox()

    def uninstall(self):
        msg_box = self.create_styled_message_box(
            "Confirm Uninstallation",
            f"Are you sure you want to uninstall {TOOLBOX_NAME}?"
        )
        result = msg_box.exec_()
        
        if result == QtWidgets.QMessageBox.Yes:
            self.close()
            self.uninstall_metabox()

    # PATHS
    def get_script_path(self):
        MEL_SCRIPT = mel.eval('getenv("MAYA_SCRIPT_NAME")')
        if MEL_SCRIPT and os.path.exists(MEL_SCRIPT):
            return os.path.dirname(MEL_SCRIPT)
        for path in sys.path:
            POSSIBLE_PATH = os.path.join(path, "Install.py")
            if os.path.exists(POSSIBLE_PATH):
                return os.path.dirname(POSSIBLE_PATH)
        return os.getcwd()
    
    # MOD FILE
    def create_mod_file(self):
        CURRENT_PATH = self.get_script_path()
        MAYA_APP_DIR = cmds.internalVar(userAppDir=True)
        MODULES_DIR = os.path.join(MAYA_APP_DIR, "modules")

        print(f"Current path: {CURRENT_PATH}")
        print(f"Maya application directory: {MAYA_APP_DIR}")
        print(f"Modules directory: {MODULES_DIR}")

        if not os.path.exists(MODULES_DIR):
            print(f"Creating modules directory: {MODULES_DIR}")
            os.makedirs(MODULES_DIR)
        else:
            print("Modules directory already exists")

        MOD_CONTENT = f"""+ MetaBox 1.0 {CURRENT_PATH}
        scripts: {os.path.join(CURRENT_PATH, "Scripts")}
        """
        MOD_FILE_PATH = os.path.join(MODULES_DIR, "MetaBox.mod")
        if os.path.exists(MOD_FILE_PATH):
            with open(MOD_FILE_PATH, 'r') as f:
                existing_content = f.read()
            if existing_content.strip() == MOD_CONTENT.strip():
                print("Existing .mod file content is correct, no update needed")
                return
            else:
                print("Existing .mod file content is incorrect, will update")
        print(f"Creating/updating .mod file: {MOD_FILE_PATH}")

        try:
            with open(MOD_FILE_PATH, "w") as f:
                f.write(MOD_CONTENT)
            print(".mod file created/updated successfully")
        except Exception as e:
            print(f"Error creating/updating .mod file: {e}")

        if os.path.exists(MOD_FILE_PATH):
            print(f".mod file successfully created/updated: {MOD_FILE_PATH}")
        else:
            print(f"Warning: .mod file could not be created/updated: {MOD_FILE_PATH}")

    def uninstall_mod_file(self):
        MAYA_APP_DIR = cmds.internalVar(userAppDir=True)
        MOD_FILE_PATH = os.path.join(MAYA_APP_DIR, "modules", "MetaBox.mod")
        # First check if the mod file exists, if so, delete it
        if os.path.exists(MOD_FILE_PATH):
            try:
                os.remove(MOD_FILE_PATH)
                print("MetaBox.mod file deleted")
            except Exception as e:
                print(f"Error deleting MetaBox.mod file: {e}")
    
    # BUTTONS
    def clean_existing_buttons(self):
        if cmds.shelfLayout("MetaBox", exists=True):
            buttons = cmds.shelfLayout("MetaBox", query=True, childArray=True) or []
            for btn in buttons:
                if cmds.shelfButton(btn, query=True, exists=True):
                    label = cmds.shelfButton(btn, query=True, label=True)
                    if label == "MetaBox":
                        cmds.deleteUI(btn)
                        print(f"Deleted existing MetaBox button: {btn}")

    def install_metabox(self):
        CURRENT_PATH = self.get_script_path()
        SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_PATH, "Scripts"))
        ICON_PATH = os.path.abspath(os.path.join(CURRENT_PATH, "Icons", "MetaBox.png"))
        MAYA_APP_DIR = cmds.internalVar(userAppDir=True)
        MAYA_VERSION = cmds.about(version=True)

        print(f"Current path: {CURRENT_PATH}")
        print(f"Scripts path: {SCRIPTS_PATH}")
        print(f"sys.path: {sys.path}")
        print(f"Current working directory: {os.getcwd()}")

        # Create mod file
        self.create_mod_file()

        # Ensure Scripts folder exists
        if not os.path.exists(SCRIPTS_PATH):
            print(f"{SCRIPTS_PATH} does not exist, please check the installation")
            return

        # Check if MetaBox.py exists
        META_BOX_FILE = os.path.join(SCRIPTS_PATH, "MetaBox.py")
        if not os.path.exists(META_BOX_FILE):
            print(f"Error: MetaBox.py file does not exist at {META_BOX_FILE}, please check the installation")
            return
        else:
            print(f"MetaBox.py file exists at {META_BOX_FILE}")

        # Ensure Scripts folder is in sys.path
        if SCRIPTS_PATH not in sys.path:
            sys.path.insert(0, SCRIPTS_PATH)
            print(f"Added {SCRIPTS_PATH} to sys.path")

        # Check and create shelf
        shelf_layout = mel.eval('$tmpVar=$gShelfTopLevel')
        if not cmds.shelfLayout("MetaBox", exists=True):
            cmds.shelfLayout("MetaBox", parent=shelf_layout)
            print("Created MetaBox shelf")
        else:
            print("MetaBox shelf already exists")

        # Clean existing buttons
        self.clean_existing_buttons()

        # Use custom icon
        if not os.path.exists(ICON_PATH):
            print(f"Warning: Custom icon file '{ICON_PATH}' does not exist, will use default icon.")
            ICON_PATH = "commandButton.png"
        else:
            print(f"Using custom icon: {ICON_PATH}")

        command = f"""
import sys
import os
CURRENT_PATH = r'{CURRENT_PATH}'
SCRIPTS_PATH = os.path.join(CURRENT_PATH, 'Scripts')
if SCRIPTS_PATH not in sys.path:
    sys.path.insert(0, SCRIPTS_PATH)
os.chdir(SCRIPTS_PATH)
try:
    import MetaBox
    MetaBox.show()
except ImportError as e:
    print("Error importing MetaBox:", str(e))
    print("Current path:", CURRENT_PATH)
    print("Scripts path:", SCRIPTS_PATH)
    print("sys.path:", sys.path)
    print("Contents of Scripts folder:", os.listdir(SCRIPTS_PATH))
    """
        # Create new button
        new_button = cmds.shelfButton(
            parent=TOOLBOX_NAME,
            image1=ICON_PATH,
            label=TOOLBOX_NAME,
            command=command,
            sourceType="python",
            annotation=TOOLBOX_NAME+" v1.0",
            noDefaultPopup=True,
            style="iconOnly"
        )

        # Show confirmation dialog before installation
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Confirm Installation")
        msg_box.setText(f"Are you sure you want to install {TOOLBOX_NAME}?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        # Set button style for confirmation dialog
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

        result = msg_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            # Proceed with installation
            # 创建安装成功的提示窗口
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Installation Successful")
            msg_box.setText(f"{TOOLBOX_NAME} has been successfully installed!")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

            # 设置按钮样式
            for button in msg_box.buttons():
                button.setStyleSheet(button_style)

            msg_box.exec_()
        else:
            print("Installation cancelled")

        # Verify installation
        try:
            import_module = __import__(TOOLBOX_NAME)
            print(f"{TOOLBOX_NAME} module imported successfully")
        except ImportError as e:
            print(f"Unable to import {TOOLBOX_NAME} module: {e}")
            print("sys.path:", sys.path)
            print("Scripts folder contents:", os.listdir(SCRIPTS_PATH))

        # Switch to MetaBox shelf
        try:
            current_shelf = cmds.shelfTabLayout("ShelfLayout", query=True, selectTab=True)
            if current_shelf != TOOLBOX_NAME:
                cmds.shelfTabLayout("ShelfLayout", edit=True, selectTab=TOOLBOX_NAME)
                print("Switched to "+TOOLBOX_NAME+" shelf")
            else:
                print("Already on "+TOOLBOX_NAME+" shelf")
        except Exception as e:
            print(f"Error switching to {TOOLBOX_NAME} shelf: {e}")

    def uninstall_metabox(self):
        # Show confirmation dialog before uninstallation
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Confirm Uninstallation")
        msg_box.setText(f"Are you sure you want to uninstall {TOOLBOX_NAME}?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        # Set button style for confirmation dialog
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

        result = msg_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            # Proceed with uninstallation
            CURRENT_PATH = self.get_script_path()
            SCRIPTS_PATH = os.path.join(CURRENT_PATH, "Scripts")
            MAYA_APP_DIR = cmds.internalVar(userAppDir=True)
            MAYA_VERSION = cmds.about(version=True)
            SHELF_FILE_PATH = os.path.join(MAYA_APP_DIR, MAYA_VERSION, "prefs", "shelves", "shelf_" + TOOLBOX_NAME + ".mel")

            # Close MetaBox window
            if cmds.window("MetaBoxWindow", exists=True):
                try:
                    cmds.deleteUI("MetaBoxWindow")
                    print("Closed " + TOOLBOX_NAME + " window")
                except Exception as e:
                    print(f"Error closing {TOOLBOX_NAME} window: {e}")
            else:
                print(TOOLBOX_NAME + " window does not exist, no need to delete")

            # Close docked window
            if cmds.dockControl(TOOLBOX_NAME + "WindowDock", exists=True):
                try:
                    cmds.deleteUI(TOOLBOX_NAME + "WindowDock")
                    print("Closed docked " + TOOLBOX_NAME + " window")
                except Exception as e:
                    print(f"Error closing docked {TOOLBOX_NAME} window: {e}")

            # Delete mod file
            self.uninstall_mod_file()

            # Delete shelf file
            if os.path.exists(SHELF_FILE_PATH):
                try:
                    os.remove(SHELF_FILE_PATH)
                    print(f"Deleted shelf file: {SHELF_FILE_PATH}")
                except Exception as e:
                    print(f"Error deleting shelf file: {e}")
            else:
                print(f"Shelf file does not exist: {SHELF_FILE_PATH}")

            # Delete shelf and buttons
            if cmds.shelfLayout("MetaBox", exists=True):
                try:
                    cmds.deleteUI(TOOLBOX_NAME, layout=True)
                    print("Deleted " + TOOLBOX_NAME + " shelf")
                except Exception as e:
                    print(f"Error deleting {TOOLBOX_NAME} shelf: {e}")
            else:
                print(TOOLBOX_NAME + " shelf does not exist, no need to delete")

            # Check all shelves, delete any MetaBox buttons
            all_shelves = cmds.shelfTabLayout("ShelfLayout", query=True, childArray=True)
            for shelf in all_shelves:
                shelf_buttons = cmds.shelfLayout(shelf, query=True, childArray=True) or []
                for btn in shelf_buttons:
                    if cmds.shelfButton(btn, query=True, exists=True):
                        label = cmds.shelfButton(btn, query=True, label=True)
                        if label == "MetaBox":
                            cmds.deleteUI(btn)
                            print(f"Deleted {TOOLBOX_NAME} button: {btn}")

            # Remove Scripts path from sys.path
            if SCRIPTS_PATH in sys.path:
                sys.path.remove(SCRIPTS_PATH)
                print(f"Removed {SCRIPTS_PATH} from sys.path")

            # Reload shelves to ensure changes take effect
            mel.eval('loadNewShelf "shelf_MetaBox.mel"')
            print("Reloaded shelves")

            # Create uninstallation successful message box
            msg_unintsall_box = QtWidgets.QMessageBox()
            msg_unintsall_box.setWindowTitle("Uninstallation Successful")
            msg_unintsall_box.setText(f"{TOOLBOX_NAME} has been successfully uninstalled!")
            msg_unintsall_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

            # Set button style for success message box
            for button in msg_unintsall_box.buttons():
                button.setStyleSheet(button_style)

            msg_unintsall_box.exec_()
        else:
            print("Uninstallation cancelled")
    
    def uninstall(self, *args):
        result = cmds.confirmDialog(
            title="Confirm Uninstallation",
            message="Are you sure you want to uninstall "+TOOLBOX_NAME+"?",
            button=['Yes', 'No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='No'
        )
        if result == 'Yes':
            cmds.deleteUI(self.window, window=True)
            self.uninstall_metabox()
        else:
            print("Uninstallation cancelled")

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    dialog = InstallDialog()
    dialog.show()
    app.exec_()

