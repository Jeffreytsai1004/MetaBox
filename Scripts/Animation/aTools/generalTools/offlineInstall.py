import os
import sys
import shutil
from maya import mel, cmds # type: ignore

def install():
    # Get the current path of aTools
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    aTools_path = os.path.normpath(current_dir).replace('\\', '/')

    # Add aTools path to Maya's Python path
    if aTools_path not in sys.path:
        sys.path.append(aTools_path)

    # Create or update userSetup.py file
    maya_app_dir = mel.eval('getenv MAYA_APP_DIR')
    scripts_dir = os.path.join(maya_app_dir, "scripts")
    user_setup_file = os.path.join(scripts_dir, "userSetup.py")

    atools_code = f"""
# Start aTools
import sys
atools_path = r"{aTools_path}"
if atools_path not in sys.path:
    sys.path.append(atools_path)

from maya import cmds
if not cmds.about(batch=True):
    cmds.evalDeferred("from aTools.animTools.animBar import animBarUI; animBarUI.show('launch')", lowestPriority=True)
# End aTools
"""

    # If userSetup.py exists, ensure we don't add duplicate aTools code
    if os.path.exists(user_setup_file):
        with open(user_setup_file, 'r') as f:
            content = f.read()
        if "# Start aTools" not in content:
            with open(user_setup_file, 'a') as f:
                f.write(atools_code)
    else:
        with open(user_setup_file, 'w') as f:
            f.write(atools_code)

    print("aTools has been successfully installed.")

if __name__ == "__main__":
    install()