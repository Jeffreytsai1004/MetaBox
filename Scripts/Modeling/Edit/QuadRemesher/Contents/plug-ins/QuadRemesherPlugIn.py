# Add possibility to have a plugin in the package.. adds more possibilities for load/reload/re-install icon...

import sys
import maya.api.OpenMaya as om
import maya.mel as mel

import struct # for unpack

verboseDebug = False

def maya_useNewAPI():
	"""
	The presence of this function tells Maya that the plugin produces, and
	expects to be passed, objects created using the Maya Python API 2.0.
	"""
	pass



# --------------------------------------- PlugIn -------------------------------------

# Initialize the plug-in : 
def initializePlugin(plugin):
	if (verboseDebug):
		sys.stdout.write(' -------- Initialize QuadRemesher plugin \n')

	# set plugin version:
	try:
		pluginFn = om.MFnPlugin(plugin)
		pluginFn.version = "1.0.1"
	except:
		a=1
	
	# install the ShelfButton the first time and if not already installed
	mel.eval('QuadRemesher_shelf')


# Uninitialize the plug-in
def uninitializePlugin(plugin):
	if (verboseDebug):
		sys.stdout.write(' -- UnInitialize QuadRemesher plugin !\n')
