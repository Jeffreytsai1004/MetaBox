#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib.request
import subprocess
import maya.cmds as cmds
import maya.mel as mel
import inspect

def get_script_path():
    # Get the path of the currently executing MEL script
    mel_script = mel.eval('getenv("MAYA_SCRIPT_NAME")')
    if mel_script and os.path.exists(mel_script):
        return os.path.dirname(mel_script)

    # If unable to get the path through MEL, try through Python
    for path in sys.path:
        possible_path = os.path.join(path, "Install.py")
        if os.path.exists(possible_path):
            return os.path.dirname(possible_path)

    # If still not found, return a default path
    return os.getcwd()  # Use current working directory as default path

def download_file(url, save_path):
    urllib.request.urlretrieve(url, save_path)

def install_pip():
    get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
    get_pip_path = os.path.join(os.path.expanduser("~"), "get-pip.py")

    print("Downloading get-pip.py...")
    download_file(get_pip_url, get_pip_path)

    print("Installing pip...")
    try:
        subprocess.check_call([sys.executable, get_pip_path, "--user"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pip: {e}")
        return False
    finally:
        if os.path.exists(get_pip_path):
            os.remove(get_pip_path)
    return True

def install_pip_packages():
    packages = [
        "customtkinter",
        "numpy",
        "pandas",
        # Add other packages to install here
    ]

    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--user"])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            return False
    return True

def create_environment():
    current_path = get_script_path()
    scripts_path = os.path.join(current_path, "Scripts")

    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)

    metabox_file = os.path.join(scripts_path, "MetaBox.py")
    if not os.path.exists(metabox_file):
        print("Warning: MetaBox.py file not found in the Scripts folder. Please ensure this file exists and contains the necessary functionality.")
    else:
        print("MetaBox.py file exists in the Scripts folder")

    return True

def create_mod_file():
    current_path = get_script_path()

    # Get the actual Maya documents path
    maya_app_dir = cmds.internalVar(userAppDir=True)
    modules_dir = os.path.join(maya_app_dir, "modules")

    print(f"Current path: {current_path}")
    print(f"Maya application directory: {maya_app_dir}")
    print(f"Modules directory: {modules_dir}")

    if not os.path.exists(modules_dir):
        print(f"Creating modules directory: {modules_dir}")
        os.makedirs(modules_dir)
    else:
        print("Modules directory already exists")

    mod_content = f"""+ MetaBox 1.0 {current_path}
scripts: {os.path.join(current_path, "Scripts")}
"""

    mod_file_path = os.path.join(modules_dir, "MetaBox.mod")

    # Check if mod file already exists
    if os.path.exists(mod_file_path):
        with open(mod_file_path, 'r') as f:
            existing_content = f.read()
        if existing_content.strip() == mod_content.strip():
            print("Existing .mod file content is correct, no update needed")
            return
        else:
            print("Existing .mod file content is incorrect, will update")

    print(f"Creating/updating .mod file: {mod_file_path}")

    try:
        with open(mod_file_path, "w") as f:
            f.write(mod_content)
        print(".mod file created/updated successfully")
    except Exception as e:
        print(f"Error creating/updating .mod file: {e}")

    if os.path.exists(mod_file_path):
        print(f".mod file successfully created/updated: {mod_file_path}")
    else:
        print(f"Warning: .mod file could not be created/updated: {mod_file_path}")

def uninstall_mod_file():
    maya_app_dir = cmds.internalVar(userAppDir=True)
    mod_file_path = os.path.join(maya_app_dir, "modules", "MetaBox.mod")
    # First check if the mod file exists, if so, delete it
    if os.path.exists(mod_file_path):
        try:
            os.remove(mod_file_path)
            print("MetaBox.mod file deleted")
        except Exception as e:
            print(f"Error deleting MetaBox.mod file: {e}")

def clean_existing_buttons():
    if cmds.shelfLayout("MetaBox", exists=True):
        buttons = cmds.shelfLayout("MetaBox", query=True, childArray=True) or []
        for btn in buttons:
            if cmds.shelfButton(btn, query=True, exists=True):
                label = cmds.shelfButton(btn, query=True, label=True)
                if label == "MetaBox":
                    cmds.deleteUI(btn)
                    print(f"Deleted existing MetaBox button: {btn}")

def uninstall_metabox():
    # Get the actual Maya documents path
    maya_app_dir = cmds.internalVar(userAppDir=True)
    maya_version = cmds.about(version=True)
    
    # Define paths
    mod_file_path = os.path.join(maya_app_dir, "modules", "MetaBox.mod")
    shelf_file_path = os.path.join(maya_app_dir, maya_version, "prefs", "shelves", "shelf_MetaBox.mel")

    # Close MetaBox window
    if cmds.window("MetaBoxWindow", exists=True):
        try:
            cmds.deleteUI("MetaBoxWindow")
            print("Closed MetaBox window")
        except Exception as e:
            print(f"Error closing MetaBox window: {e}")
    else:
        print("MetaBox window does not exist, no need to delete")

    # Close docked window
    if cmds.dockControl("MetaBoxWindowDock", exists=True):
        try:
            cmds.deleteUI("MetaBoxWindowDock")
            print("Closed docked MetaBox window")
        except Exception as e:
            print(f"Error closing docked MetaBox window: {e}")

    # Delete mod file
    uninstall_mod_file()

    # Delete shelf file
    if os.path.exists(shelf_file_path):
        try:
            os.remove(shelf_file_path)
            print(f"Deleted shelf file: {shelf_file_path}")
        except Exception as e:
            print(f"Error deleting shelf file: {e}")
    else:
        print(f"Shelf file does not exist: {shelf_file_path}")

    # Delete shelf and buttons
    if cmds.shelfLayout("MetaBox", exists=True):
        try:
            cmds.deleteUI("MetaBox", layout=True)
            print("Deleted MetaBox shelf")
        except Exception as e:
            print(f"Error deleting MetaBox shelf: {e}")
    else:
        print("MetaBox shelf does not exist, no need to delete")

    # Check all shelves, delete any MetaBox buttons
    all_shelves = cmds.shelfTabLayout("ShelfLayout", query=True, childArray=True)
    for shelf in all_shelves:
        shelf_buttons = cmds.shelfLayout(shelf, query=True, childArray=True) or []
        for btn in shelf_buttons:
            if cmds.shelfButton(btn, query=True, exists=True):
                label = cmds.shelfButton(btn, query=True, label=True)
                if label == "MetaBox":
                    cmds.deleteUI(btn)
                    print(f"Deleted MetaBox button: {btn}")

    # Remove Scripts path from sys.path
    current_path = get_script_path()
    scripts_path = os.path.join(current_path, "Scripts")
    if scripts_path in sys.path:
        sys.path.remove(scripts_path)
        print(f"Removed {scripts_path} from sys.path")

    # Reload shelves to ensure changes take effect
    mel.eval('loadNewShelf "shelf_MetaBox.mel"')
    print("Reloaded shelves")

    cmds.confirmDialog(title="Uninstallation Successful", message="MetaBox has been successfully uninstalled!", button=["OK"])

def install_metabox():
    current_path = get_script_path()
    scripts_path = os.path.join(current_path, "Scripts")

    print(f"Current path: {current_path}")
    print(f"Scripts path: {scripts_path}")
    print(f"sys.path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")

    # Create mod file
    create_mod_file()

    # Ensure Scripts folder exists
    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)
        print(f"Created Scripts folder: {scripts_path}")

    # Check if MetaBox.py exists
    metabox_file = os.path.join(scripts_path, "MetaBox.py")
    if not os.path.exists(metabox_file):
        print(f"Error: MetaBox.py file does not exist at {metabox_file}")
        return
    else:
        print(f"MetaBox.py file exists at {metabox_file}")

    # Ensure Scripts folder is in sys.path
    if scripts_path not in sys.path:
        sys.path.insert(0, scripts_path)
        print(f"Added {scripts_path} to sys.path")

    # Check and create shelf
    shelf_layout = mel.eval('$tmpVar=$gShelfTopLevel')
    if not cmds.shelfLayout("MetaBox", exists=True):
        cmds.shelfLayout("MetaBox", parent=shelf_layout)
        print("Created MetaBox shelf")
    else:
        print("MetaBox shelf already exists")

    # Clean existing buttons
    clean_existing_buttons()

    # Use custom icon
    icon_path = os.path.join(current_path, "Icons", "MetaBox.png")
    if not os.path.exists(icon_path):
        print(f"Warning: Custom icon file '{icon_path}' does not exist, will use default icon.")
        icon_path = "commandButton.png"
    else:
        print(f"Using custom icon: {icon_path}")

    command = f"""
import sys
import os
current_path = r'{current_path}'
scripts_path = os.path.join(current_path, 'Scripts')
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)
os.chdir(scripts_path)
try:
    import MetaBox
    MetaBox.show()
except ImportError as e:
    print("Error importing MetaBox:", str(e))
    print("Current path:", current_path)
    print("Scripts path:", scripts_path)
    print("sys.path:", sys.path)
    print("Contents of Scripts folder:", os.listdir(scripts_path))
"""

    # Create new button
    new_button = cmds.shelfButton(
        parent="MetaBox",
        image1=icon_path,
        label="MetaBox",
        command=command,
        sourceType="python",
        annotation="MetaBox v1.0",
        noDefaultPopup=True,
        style="iconOnly"  # Changed to show only icon
    )

    print("Created new MetaBox button")

    # Check if button was created correctly
    if cmds.shelfButton(new_button, query=True, exists=True):
        print("MetaBox button created successfully")
        # Print button properties for verification
        print("Button label:", cmds.shelfButton(new_button, query=True, label=True))
        print("Button image:", cmds.shelfButton(new_button, query=True, image1=True))
    else:
        print("Warning: Failed to create MetaBox button")

    cmds.confirmDialog(title="Installation Successful", message="MetaBox has been successfully installed!", button=["OK"])

    # Verify installation
    try:
        import MetaBox
        print("MetaBox module imported successfully")
    except ImportError as e:
        print(f"Unable to import MetaBox module: {e}")
        print("sys.path:", sys.path)
        print("Contents of Scripts folder:", os.listdir(scripts_path))

    # Switch to MetaBox shelf
    try:
        current_shelf = cmds.shelfTabLayout("ShelfLayout", query=True, selectTab=True)
        if current_shelf != "MetaBox":
            cmds.shelfTabLayout("ShelfLayout", edit=True, selectTab="MetaBox")
            print("Switched to MetaBox shelf")
        else:
            print("Already on MetaBox shelf")
    except Exception as e:
        print(f"Error switching to MetaBox shelf: {e}")

class InstallDialog(object):
    def __init__(self):
        self.window = "MetaBoxInstaller"
        self.title = "MetaBox Installer"
        self.size = (350, 100)  # Changed width from 300 to 350

        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(label="Install MetaBox", command=self.install)
        cmds.button(label="Uninstall MetaBox", command=self.uninstall)
        cmds.showWindow()

    def install(self, *args):
        result = cmds.confirmDialog(
            title="Confirm Installation",
            message="Are you sure you want to install MetaBox?",
            button=['Yes', 'No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='No'
        )
        if result == 'Yes':
            cmds.deleteUI(self.window, window=True)
            install_metabox()
        else:
            print("Installation cancelled")

    def uninstall(self, *args):
        result = cmds.confirmDialog(
            title="Confirm Uninstallation",
            message="Are you sure you want to uninstall MetaBox?",
            button=['Yes', 'No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='No'
        )
        if result == 'Yes':
            cmds.deleteUI(self.window, window=True)
            uninstall_metabox()
        else:
            print("Uninstallation cancelled")

# Execute when script is dragged into Maya
if __name__ == "__main__":
    InstallDialog()