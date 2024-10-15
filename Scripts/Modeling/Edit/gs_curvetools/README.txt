GS CurveTools installation

1. Copy gs_curvetools folder to {Path to Documents}\Documents\Maya\{Maya Version}\scripts\

	Example of the final folder structure:

	Documents\Maya\2022\scripts\gs_curvetools\fonts
	Documents\Maya\2022\scripts\gs_curvetools\icons
	Documents\Maya\2022\scripts\gs_curvetools\utils
	Documents\Maya\2022\scripts\gs_curvetools\__init__.py
	Documents\Maya\2022\scripts\gs_curvetools\core.py
	Documents\Maya\2022\scripts\gs_curvetools\init.py
	Documents\Maya\2022\scripts\gs_curvetools\LICENSE.txt
	Documents\Maya\2022\scripts\gs_curvetools\main.py	
	Documents\Maya\2022\scripts\gs_curvetools\README.txt

2. Run Maya

3. Copy and paste this line to "Python" command box and press "Enter":

import gs_curvetools.init as ct_init;from imp import reload;reload(ct_init);ct_init.Init();

IMPORTANT: There should be no spaces or tabs before this command!

4. Look for GS tab on your Shelf

5. Click CT UI button to run the menu. Click again to hide the menu.

NOTES:
>> To reset to factory defaults click CT with "refresh" arrow button.
>> To stop all scripts and close the menu press CT DEL button.
>> You can use middle-mouse button drag to move the buttons to any tab.
>> All the hotkeys are available in Hotkey Editor > Custom Scripts > GS > GS_CurveTools.
>> Always repeat initialization steps when updating the plug-in to a new version.
>> You can always repeat initialization steps if you lost control buttons or shelf.
