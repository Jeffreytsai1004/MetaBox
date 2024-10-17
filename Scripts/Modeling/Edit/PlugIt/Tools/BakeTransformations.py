import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
from six.moves import range
from collections import Counter, OrderedDict
from functools import partial
from webbrowser import open_new_tab
import six, math


def GetSelection(*args, **kwargs):
	type = kwargs["type"] if "type" in kwargs else "None"
	highlight = kwargs["highlight"] if "highlight" in kwargs else False
	flatten = kwargs["flatten"] if "flatten" in kwargs else False
	allParents = kwargs["allParents"] if "allParents" in kwargs else False

	# Check if there is any args
	if len(args) > 0:
		selection, objects = [], []
		# Get selection & objects from args
		for arg in args:
			selection.extend(arg)
			objects.extend(arg)
	else:
		# Get selection
		if flatten:
			selection = cmds.ls(sl=True, l=True, fl=True)
		else:
			selection = cmds.ls(sl=True, l=True)
		
		objects = list(selection)
		
		# Get highlighted objects
		if highlight:
			objects.extend(cmds.ls(hl=True, l=True))
	
	# Get shapes
	if type == "mesh":
		shapes = cmds.ls(objects, l=True, dag=True, ni=True, o=True, typ="mesh")
	elif type == "geometry" or type == "geo":
		shapes = cmds.ls(objects, l=True, dag=True, ni=True, o=True, g=True)
	elif type == "nurbsCurve" or type == "curve":
		shapes = cmds.ls(objects, l=True, dag=True, ni=True, typ="nurbsCurve")
	elif type == "transform":
		shapes = cmds.ls(objects, l=True, dag=True, ni=True, o=True, typ="transform")
	else:
		shapes = cmds.ls(objects, l=True, dag=True, ni=True, o=True)
	
	# Get objects
	if allParents:
		objects = cmds.listRelatives(shapes, f=True, ap=True, ni=True, typ="transform")
	else:
		objects = cmds.listRelatives(shapes, f=True, p=True, ni=True, typ="transform")
	
	# Remove intermediate objects
	objects = cmds.ls(objects, l=True, ni=True)
	
	# Remove duplicates objects
	if objects is not None:
		objects = list(OrderedDict.fromkeys(objects))
	
	return selection, shapes, objects

def GetComponentType(*args, **kwargs):
	# Create default args
	selection = None
	
	# Load arguments (override default args)
	for i, arg in enumerate(args):
		if i == 0:
			selection = arg
	
	# Load keyworded arguments (override *args)
	for key, value in six.iteritems(kwargs):
		if key == "selection" or key == "sel":
			selection = value
	
	selList = om.MSelectionList()
	
	if selection is not None:
		for each in selection:
			try:
				selList.add(each)
			except:
				pass
	else:
		selList = om.MGlobal.getActiveSelectionList()
	
	filterDict = OrderedDict([("v", om.MFn.kMeshVertComponent), ("eg", om.MFn.kMeshEdgeComponent), ("fc", om.MFn.kMeshPolygonComponent), ("puv", om.MFn.kMeshMapComponent), ("pvf", om.MFn.kMeshVtxFaceComponent), ("cv", om.MFn.kCurveCVComponent)])
	
	for key, filter in six.iteritems(filterDict):
		iter = om.MItSelectionList(selList, filter)
		try:
			if iter.hasComponents() is True:
				return key
		except:
			pass
	
	return None

def Eval(msg, mode='PRINT', deferred=False):
	if deferred is False:
		if mode == 'PRINT':
			from sys import stdout; stdout.write("{}\n".format(msg))
		elif mode == 'INFO':
			om.MGlobal.displayInfo(msg)
		elif mode == 'WARNING':
			om.MGlobal.displayWarning(msg)
		elif mode == 'ERROR':
			om.MGlobal.displayError(msg)
	else:
		if mode == 'PRINT':
			cmds.evalDeferred(r'from sys import stdout; stdout.write("{}\n")'.format(msg))
		elif mode == 'INFO':
			cmds.evalDeferred(r'import maya.api.OpenMaya as om; om.MGlobal.displayInfo("'+msg+'")')
		elif mode == 'WARNING':
			cmds.evalDeferred(r'import maya.api.OpenMaya as om; om.MGlobal.displayWarning("'+msg+'")')
		elif mode == 'ERROR':
			cmds.evalDeferred(r'import maya.api.OpenMaya as om; om.MGlobal.displayError("'+msg+'")')

def Print(object, mode='PRINT', deferred=False):
	if type(object) is not list:
		Eval(object, mode, deferred)
	else:
		for obj in object:
			Eval(obj, mode, deferred)

def IsInstanced(object):
    isInstanced = False
    shapes = cmds.listRelatives(object, f=True, s=True, ni=True)
    if shapes:
        parents = cmds.listRelatives(shapes, f=True, ap=True) or []
        if len(parents) > 1:
            isInstanced = True
    return isInstanced

def getOutlinerList(object=None):
	# If object has a parent, get a list of the childrens
	if object:
		parent = cmds.listRelatives(object, parent=True, fullPath=True)
		if parent:
			return cmds.listRelatives(parent, children=True, type="transform", fullPath=True)
	# Otherwise, get list of assemblies in the scene
	return cmds.ls(long=True, assemblies=True)

def getOutlinerPosition(obj):
	# Check if objects exists
	if cmds.objExists(obj):
		# Make sure it's long names
		obj = cmds.ls(obj, long=True)[0]
		# Get a list of the outliner
		outlinerList = getOutlinerList(obj)
		# Get the position of the object in the outliner
		sourceObjPosition = outlinerList.index(obj)+1
		# Get the position of the object from the bottom of the outliner
		return sourceObjPosition - len(outlinerList)

def crossProduct(v1, v2):
	vector = om.MVector(*v1) ^ om.MVector(*v2)
	return [vector.x, vector.y, vector.z]

def normalizeVector(v1=[1, 0, 0]):
	if isinstance(v1, (list, tuple)) is True and len(v1) >= 3:
		v1 = om.MVector(v1[0], v1[1], v1[2])
		v1.normalize()
		v1 = [v1.x, v1.y, v1.z]
	return v1

def vectorBetweenPoints(point1, point2):
	return normalizeVector([point2[i] - point1[i] for i in range(len(point1))])

def vectorAvg(vectors):
	sum = om.MVector()
	
	for vector in vectors:
		sum += vector
	
	return sum / len(vectors)

def cubicRoot(number):
	return number ** (1 / 3)

def GetVertexPosition(vertex):
	id = int(vertex.split("[")[-1][:-1])
	
	vtxList = om.MSelectionList().add(vertex)
	dagPath = vtxList.getDagPath(0)
	
	vtx_iter = om.MItMeshVertex(dagPath)
	vtx_iter.setIndex(id)
	
	# Get vertex position
	position = vtx_iter.position(space=om.MSpace.kWorld)
	
	return om.MVector(position)

def GetEdgePosition(edge):
	id = int(edge.split("[")[-1][:-1])
	
	edgeList = om.MSelectionList().add(edge)
	dagPath = edgeList.getDagPath(0)
	
	edge_iter = om.MItMeshEdge(dagPath)
	edge_iter.setIndex(id)
	
	# Get edge position
	position = edge_iter.center(space=om.MSpace.kWorld)
	
	return om.MVector(position)

def GetFacePosition(face):
	id = int(face.split("[")[-1][:-1])
	
	faceList = om.MSelectionList().add(face)
	dagPath = faceList.getDagPath(0)
	
	face_iter = om.MItMeshPolygon(dagPath)
	face_iter.setIndex(id)
	
	# Get edge position
	position = face_iter.center(space=om.MSpace.kWorld)
	
	return om.MVector(position)

def GetVertexVectors(vertex):
	space = om.MSpace.kWorld
	id = int(vertex.split("[")[-1][:-1])
	
	vtxList = om.MSelectionList().add(vertex)
	dagPath = vtxList.getDagPath(0)
	
	vtx_iter = om.MItMeshVertex(dagPath)
	vtx_iter.setIndex(id)
	
	# Get vertex normal & position
	normal = vtx_iter.getNormal(space=space)
	position = vtx_iter.position(space=space)
		
	# Get all connected vertices
	cvertices = list(vtx_iter.getConnectedVertices())
	vertices_dict = {}
	
	cvtx_iter = om.MItMeshVertex(dagPath)
	while len(cvertices):
		if cvertices[0] not in vertices_dict:
			cvtx_iter.setIndex(cvertices[0])
			cvtx_position = cvtx_iter.position(space=space)
			edge_v = vectorBetweenPoints(list(position), list(cvtx_position))
			vertices_dict[cvertices[0]] = tuple([round(v, 3) for v in edge_v])
		
		del cvertices[0]
	
	# Get the most common vector
	tangent, vector_count = Counter(vertices_dict.values()).most_common(1)[0]
	
	# If no common vector is found, check for parallel vectors
	if vector_count < 2:
		all_vectors = list(vertices_dict.values())
		parallel_vectors = {k: 1 for k in all_vectors}
		while len(all_vectors) > 0:
			omV = om.MVector(all_vectors[0])
			for ov in all_vectors:
				if ov == all_vectors[0]:
					continue
				if omV.isParallel(om.MVector(ov)):
					parallel_vectors[all_vectors[0]] += 1
					del parallel_vectors[ov]
			del all_vectors[0]
		v = max(parallel_vectors, key=parallel_vectors.get)
		if parallel_vectors[v] > 1:
			tangent, vector_count = v, parallel_vectors[v]
	
	# If no parallel vector is found, use first two points
	if vector_count < 2:
		vtx_id = list(vertices_dict.keys())[0]
	else:
		vtx_id = list(vertices_dict.keys())[list(vertices_dict.values()).index(tangent)]
	
	# Calculate tangent
	cvtx_iter.setIndex(vtx_id)
	cvtx_position = cvtx_iter.position(space=space)
	tangent = vectorBetweenPoints(list(position), list(cvtx_position))
	
	return list(normal), tangent

def GetEdgeVectors(edge):
	space = om.MSpace.kWorld
	
	# Calculate normal from face vertices
	vtxFaces = cmds.polyListComponentConversion(edge, fe=True, tvf=True)
	vtxFaceList = om.MSelectionList()
	for vtxFace in vtxFaces:
		vtxFaceList.add(vtxFace)
	
	normal = om.MVector()
	count = 0
	
	dagPath, component = vtxFaceList.getComponent(0)
	fnMesh = om.MFnMesh(dagPath)
	vtxFace_itr = om.MItMeshFaceVertex(dagPath, component)
	while not vtxFace_itr.isDone():
		faceId = vtxFace_itr.faceId()
		vertexId = vtxFace_itr.vertexId()
		
		normal += fnMesh.getFaceVertexNormal(faceId, vertexId, space=space)
		count += 1
		
		vtxFace_itr.next()
	
	normal = normal / count
	
	# Get tangent
	id = int(edge.split("[")[-1][:-1])
	edgeList = om.MSelectionList().add(edge)
	dagPath = edgeList.getDagPath(0)
	
	edge_iter = om.MItMeshEdge(dagPath)
	edge_iter.setIndex(id)
	
	position = om.MPoint()
	
	vertices = [edge_iter.vertexId(0), edge_iter.vertexId(1)]
	vtx_iter = om.MItMeshVertex(dagPath)
	for vtx in vertices:
		vtx_iter.setIndex(vtx)
		position += vtx_iter.position(space=space)

	avgPos = position / len(vertices)
	tangent = vectorBetweenPoints(list(avgPos), list(edge_iter.point(1, space)))
	
	return list(normal), list(tangent)
	
def GetFaceVectors(face):
	space = om.MSpace.kWorld 
	id = int(face.split("[")[-1][:-1])
	
	faceList = om.MSelectionList().add(face)
	dagPath = faceList.getDagPath(0)
	
	face_iter = om.MItMeshPolygon(dagPath)
	face_iter.setIndex(id)
	
	# Get face normal
	normal = face_iter.getNormal(space=space)
	
	# Get all connected faces that have similar normal
	cfaces = list(face_iter.getConnectedFaces())
	faces_dict = {id: True}
	
	cface_iter = om.MItMeshPolygon(dagPath)
	while len(cfaces):
		if cfaces[0] not in faces_dict:
			cface_iter.setIndex(cfaces[0])
			cface_normal = cface_iter.getNormal(space=space)
			if normal.isEquivalent(cface_normal, 0.01):
				faces_dict[cfaces[0]] = True
				for f in cface_iter.getConnectedFaces():
					if f not in faces_dict:
						cfaces.append(f)
			else:
				faces_dict[cfaces[0]] = False
		
		del cfaces[0]
	
	# Get edge vectors from connected faces
	cfaces = [f for f, value in six.iteritems(faces_dict) if value is True]
	edges_dict = {}
	
	cedge_iter = om.MItMeshEdge(dagPath)
	for f in cfaces:
		cface_iter.setIndex(f)
		cedges = list(cface_iter.getEdges())
		
		for edge in cedges:
			if edge not in edges_dict:
				cedge_iter.setIndex(edge)
				edge_v = vectorBetweenPoints(list(cedge_iter.point(0, space)), list(cedge_iter.point(1, space)))
				edges_dict[edge] = tuple([round(v, 3) for v in edge_v])
		
	# Get the most common vector
	tangent, vector_count = Counter(edges_dict.values()).most_common(1)[0]
	
	# if no common vector is found, check for parallel vectors
	if vector_count < 2:
		all_vectors = list(edges_dict.values())
		parallel_vectors = {k: 1 for k in all_vectors}
		while len(all_vectors) > 0:
			omV = om.MVector(all_vectors[0])
			for ov in all_vectors:
				if ov == all_vectors[0]:
					continue
				if omV.isParallel(om.MVector(ov)):
					parallel_vectors[all_vectors[0]] += 1
					del parallel_vectors[ov]
			del all_vectors[0]
		v = max(parallel_vectors, key=parallel_vectors.get)
		if parallel_vectors[v] > 1:
			tangent, vector_count = v, parallel_vectors[v]
	
	# if no parallel vector is found, use first two points
	if vector_count < 2:
		# get face-relative vertices positions
		vertices_position = face_iter.getPoints(space=space)
		vertices_dict = {}
		# convert face-relative indices to object-relative indices
		for i in range(face_iter.polygonVertexCount()):
			vertices_dict[int(face_iter.vertexIndex(i))] = vertices_position[i]
		vertices_dict = OrderedDict(sorted(vertices_dict.items()))
		vertices_position = []
		for pos in six.itervalues(vertices_dict):
			vertices_position.append(pos)
			if len(vertices_position) == 2:
				break
		tangent = vectorBetweenPoints(list(vertices_position[0]), list(vertices_position[1]))
	else:
		# Get back the original vector since we needed to round the values for comparing the vectors
		edge_id = list(edges_dict.keys())[list(edges_dict.values()).index(tangent)]
		cedge_iter.setIndex(edge_id)
		tangent = vectorBetweenPoints(list(cedge_iter.point(0, space)), list(cedge_iter.point(1, space)))
		
	return list(normal), tangent

def  GetOrientationFromVectors(normal, tangent):	
	binormal = normalizeVector(crossProduct(normal, tangent))
	
	position = [0, 0, 0]
	
	tMatrix = normal + [0] + tangent + [0] + binormal + [0] + position + [1]
	mMatrix = om.MMatrix(tMatrix)
	tmMatrix = om.MTransformationMatrix(mMatrix)
	rotation = tmMatrix.rotation(False).reorder(om.MEulerRotation.kXYZ)
	rotation = [math.degrees(x + 0) for x in list(rotation)[:3]]
	
	return rotation

def  SignedVolumeOfTriangle(p1, p2, p3):
	volume = (p1 * (p2 ^ p3)) / 6
	return volume

def GetObjectVolume(object):
	# Create face list
	faces = object + ".f[*]"
	faceList = om.MSelectionList().add(faces)
	dagPath, component = faceList.getComponent(0)
	
	# Get ids list
	compFn = om.MFnSingleIndexedComponent(component)
	ids = compFn.getElements()
	
	# Get all triangle volumes
	volumes = []
	border = False
	
	# Looping through each face
	face_iter = om.MItMeshPolygon(dagPath, component)
	for id in ids:
		face_iter.setIndex(id)
		numTriangles = face_iter.numTriangles()
		# Loop each face triangle
		for num in range(numTriangles):
			triangle = face_iter.getTriangle(num, space=om.MSpace.kWorld)[0]
			volume =  SignedVolumeOfTriangle(om.MVector(triangle[0]), om.MVector(triangle[1]), om.MVector(triangle[2]))
			volumes.append(volume)
		
		# Check if face is on open border
		if border is False:
			border = face_iter.onBoundary()
	
	# Calcule sum of every triangle volumes
	volume = abs(sum(volumes))

	# Print warning if object has open borders
	if border is True:
		Print.Print("{} has open borders, which could result in unexpected scale values.".format(object), mode='WARNING', deferred=True)
	
	# Return volume cubic root
	return cubicRoot(volume)

def GetEdgeScale(edge):
	id = int(edge.split("[")[-1][:-1])
	
	edgeList = om.MSelectionList().add(edge)
	dagPath = edgeList.getDagPath(0)
	
	edge_iter = om.MItMeshEdge(dagPath)
	edge_iter.setIndex(id)
	
	# Get edge position
	scale = edge_iter.length(space=om.MSpace.kWorld)
	
	return scale

def GetFaceScale(face):
	id = int(face.split("[")[-1][:-1])
	
	faceList = om.MSelectionList().add(face)
	dagPath = faceList.getDagPath(0)
	
	face_iter = om.MItMeshPolygon(dagPath)
	face_iter.setIndex(id)
	
	# Get edge position
	scale = face_iter.getArea(space=om.MSpace.kWorld)
	
	return math.sqrt(scale)

# Create empty MEL function for proper undo/redo operations
mel.eval('proc BakeTransformations(){}')

# Main function
def PerformBakeTransformations(bakeMode=1, setObjSpc=1, clearSel=1, bakePos=1, bakeRot=1, bakeScale=1):
	# Open undo chunk
	cmds.undoInfo(ock=True, cn="BakeTransformations")
	
	# Call empty MEL function for proper undo/redo operations
	mel.eval('BakeTransformations')

	# Get selection
	selection = GetSelection(highlight=False, flatten=True)[0]

	# Check that something is selected
	if not len(selection):
		Print("Nothing selected!", mode='ERROR')
		cmds.undoInfo(cck=True)
	
	# Get object from selection
	component = selection[-1]
	selectType = GetComponentType([component])
	object = GetSelection([component], type="mesh")[2][-1] if selectType else component
	
	# Check that a component is selected
	if bakeMode == 1 and not selectType:
			Print("No component selected!", mode='ERROR')
			cmds.undoInfo(cck=True)
			return
		
	# Check that object is not an instance
	if IsInstanced(object):
		Print("Selected object is an instance and cannot be baked.", mode='ERROR')
		cmds.undoInfo(cck=True)
		return
	
	# Get object parent and outliner position
	parent = cmds.listRelatives(object, f=True, p=True)
	currentPosition = getOutlinerPosition(object)
	
	# Get pivot manipulator context and mode
	if bakeMode == 2:
		currentCtx = cmds.currentCtx()
		if currentCtx == "moveSuperContext":
			manipMode = cmds.manipMoveContext("Move", q=True, m=True)	
		elif currentCtx == "RotateSuperContext":
			manipMode = cmds.manipRotateContext("Rotate", q=True, m=True)
			if manipMode == 1:
				manipMode = 2
			elif manipMode == 2:
				manipMode = 0
			elif manipMode == 3:
				manipMode = 6	
		elif currentCtx == "scaleSuperContext":
			manipMode = cmds.manipScaleContext("Scale", q=True, m=True)
	
	# Store current units and temporarily change for centimeters
	units = cmds.currentUnit(q=True, l=True)
	cmds.currentUnit(l="cm")
	
	# Get translation
	if bakePos or not clearSel:
		# From Component
		if bakeMode == 1:
			if selectType == "v": 
				# Get vertex position
				position = GetVertexPosition(component)
			if selectType == "eg":
				# Get edge position
				position = GetEdgePosition(component)
			if selectType == "fc":
				# Get face position
				position = GetFacePosition(component)
		# From Pivot
		elif bakeMode == 2:
			# Case 1: Get move tool position
			if currentCtx == "moveSuperContext" and cmds.manipMoveContext("Move", q=True, vis=True):
				position = cmds.manipMoveContext("Move", q=True, p=True)
			elif currentCtx == "moveSuperContext" and cmds.manipMoveContext("Move", q=True, epm=True):
				position = cmds.manipMoveContext("Move", q=True, epp=True)
			# Case 2: Get rotate tool position
			elif currentCtx == "RotateSuperContext" and cmds.manipRotateContext("Rotate", q=True, vis=True):
				position = cmds.manipRotateContext("Rotate", q=True, p=True)
			elif currentCtx == "RotateSuperContext" and cmds.manipRotateContext("Rotate", q=True, epm=True):
				position = cmds.manipRotateContext("Rotate", q=True, epp=True)
			# Case 3: Get scale tool position
			elif currentCtx == "scaleSuperContext" and cmds.manipScaleContext("Scale", q=True, vis=True):
				position = cmds.manipScaleContext("Scale", q=True, p=True)
			elif currentCtx == "scaleSuperContext" and cmds.manipScaleContext("Scale", q=True, epm=True):
				position = cmds.manipScaleContext("Scale", q=True, epp=True)
			# Case 4: Get object pivot position
			else:
				rotatePivot = om.MVector(cmds.xform(object, q=True, a=True, ws=True, rp=True))
				scalePivot = om.MVector(cmds.xform(object, q=True, a=True, ws=True, sp=True))
				position = vectorAvg([rotatePivot, scalePivot])
	
	# Get rotation
	if bakeRot or not clearSel:
		# From Component
		if bakeMode == 1:
			if selectType == "v":
				# Get vertex normal and tangent
				normal, tangent = GetVertexVectors(component)
			elif selectType == "eg":
				# Get edge normal and tangent
				normal, tangent = GetEdgeVectors(component)	
			elif selectType == "fc":
				# Get face normal and tangent
				normal, tangent = GetFaceVectors(component)
		
			# Get rotation from the component normal and corresponding edge vector
			rotation =  GetOrientationFromVectors(normal, tangent)
		# From Pivot
		elif bakeMode == 2:
			rotation = cmds.manipPivot(q=True, o=True)[0]
			
			if any([currentCtx == "moveSuperContext", currentCtx == "RotateSuperContext", currentCtx == "scaleSuperContext"]):
				if any([manipMode == 0, manipMode == 4, manipMode == 10]):
					rotation = cmds.xform(object, q=True, a=True, eu=True, ro=True)
				elif manipMode == 1:
					if parent is not None:
						rotation = cmds.xform(parent[0], q=True, a=True, eu=True, ro=True)
				elif manipMode == 5:
					live = cmds.ls(l=True, lv=True)
					if len(live):
						live = cmds.listRelatives(live, f=True, p=True, ni=True, typ="transform")[0]
						rotation = cmds.xform(live, q=True, a=True, eu=True, ro=True)
	
	# Get scale
	if bakeScale:
		# From Component
		if bakeMode == 1:
			if selectType == "v":
				# Get vertex scale
				scale = GetObjectVolume(object)
			elif selectType == "eg":
				# Get edge scale
				scale = GetEdgeScale(component)	
			elif selectType == "fc":
				# Get face scale
				scale = GetFaceScale(component)
		# From Pivot
		elif bakeMode == 2:
			# Get pivot scale
			scale = GetObjectVolume(object)
	
	# Store components selection
	cmds.selectMode(co=True)
	cmds.selectType(pv=True)
	vertices = cmds.ls(sl=True, l=True)
	cmds.selectType(pe=True)
	edges = cmds.ls(sl=True, l=True)
	cmds.selectType(pf=True)
	faces = cmds.ls(sl=True, l=True)

	# Create null and apply transformations
	null = cmds.ls(cmds.group(em=True), l=True)[0]
	cmds.matchTransform(null, object)
	
	# Set translation
	if bakePos:
		# Move null
		cmds.xform(null, a=True, ws=True, t=position)
		# Move pivot
		cmds.xform(object, a=True, ws=True, piv=position)
	
	# Set rotation
	if bakeRot:
		# Rotate null
		cmds.xform(null, a=True, eu=True, roo="xyz", ro=rotation)
	
	# Set scale
	if bakeScale:
		# Scale null
		cmds.xform(null, a=True, ws=True, s=[scale, scale, scale])
	
	# Freeze null transformations
	cmds.makeIdentity(null, a=True, t=1-bakePos, r=1-bakeRot, s=1-bakeScale, n=False, pn=True)
	
	# Parent object to null
	if parent is not None:
		null = cmds.ls(cmds.parent(null, parent), l=True)[0]
	
	object = cmds.ls(cmds.parent(object, null), l=True)[0]
	
	# Freeze object transformations
	cmds.makeIdentity(object, a=True, t=bakePos, r=bakeRot, s=bakeScale, n=False, pn=True)
	
	# Unparent object from null
	if parent is not None:
		object = cmds.ls(cmds.parent(object, parent), l=True)[0]
	else:
		object = cmds.ls(cmds.parent(object, w=True), l=True)[0]
	
	# Delete null
	cmds.delete(null)
	
	# Restore outliner position
	cmds.reorder(object, relative=currentPosition)
	
	# Restore components selection
	cmds.selectMode(co=True)
	cmds.selectType(pv=True)
	cmds.select(vertices, r=True)
	cmds.selectType(pe=True)
	cmds.select(edges, r=True)
	cmds.selectType(pf=True)
	cmds.select(faces, r=True)

	# Select object
	if clearSel:
		cmds.selectMode(o=True)
		cmds.select(object, r=True)
	elif selectType is not None:
		mel.eval("selectType -"+selectType+" 1;")
		cmds.select(selection, r=True)
	
	# Set tools axis to object space
	if setObjSpc:
		cmds.manipMoveContext("Move", e=True, m=0)
		cmds.manipRotateContext("Rotate", e=True, m=0)
		cmds.manipScaleContext("Scale", e=True, m=0)
	elif bakeMode == 2:
		cmds.manipPivot(p=position, o=rotation)
	
	# Recover units
	cmds.currentUnit(l=units)
	
	# Close undo chunk
	cmds.undoInfo(cck=True)

# Create a new partial class to print the correct command name when undoing
class rpartial(partial):
	def __repr__(self):
		return __name__.split(".")[-1]

# Create window
class BakeTransformations(object):
	def __init__(self, optionBox=False, *args, **kwargs):
		# Create default variables
		self.pfx = "BT_"
		self.windowName = self.pfx + "Window"
		self.windowSizeMenuItem = self.pfx + "SaveWindowSize_menuItem"

		self.windowTitle = "Bake Transformations"
		self.runLabel = "Bake"
		self.windowSize = [546, 350]

		# Create option variables
		self.saveWindowSize = self.pfx + "SaveWindowSize"
		self.bakeMode = self.pfx + "BakeMode"
		self.setObjSpc = self.pfx + "SetObjSpc"
		self.clearSel = self.pfx + "ClearSel"
		self.bakePos = self.pfx + "BakePos"
		self.bakeRot = self.pfx + "BakeRot"
		self.bakeScale = self.pfx + "BakeScale"

		# Create window or run command
		if optionBox is True:
			self.createWindow()
		else:
			self.runCmd(closeWindow=False, **kwargs)
	
	# Help command
	def helpCmd(self, *args):
		open_new_tab("https://gabrielnadeau.com/pages/gn-baketransformations")
	
	# Run command
	def runCmd(self, closeWindow, **kwargs):
		# Get option variables
		self.defaultSettings(reset=False)
		
		if "bakeMode" in kwargs:
			bakeMode = kwargs["bakeMode"]
		else:
			bakeMode = cmds.optionVar(q=self.bakeMode)
		
		if "setObjSpc" in kwargs:
			setObjSpc = kwargs["setObjSpc"]
		else:
			setObjSpc = cmds.optionVar(q=self.setObjSpc)
		
		if "clearSel" in kwargs:
			clearSel = kwargs["clearSel"]
		else:
			clearSel = cmds.optionVar(q=self.clearSel)
		
		if "bakePos" in kwargs:
			bakePos = kwargs["bakePos"]
		else:
			bakePos = cmds.optionVar(q=self.bakePos)
		
		if "bakeRot" in kwargs:
			bakeRot = kwargs["bakeRot"]
		else:
			bakeRot = cmds.optionVar(q=self.bakeRot)
		
		if "bakeScale" in kwargs:
			bakeScale = kwargs["bakeScale"]
		else:
			bakeScale = cmds.optionVar(q=self.bakeScale)
		
		# Bake Transformations
		PerformBakeTransformations(bakeMode, setObjSpc, clearSel, bakePos, bakeRot, bakeScale)
		
		# Close window if specified
		if closeWindow is True:
			self.closeWindow()
	
	# Close window
	def closeWindow(self):
		if cmds.window(self.windowName, ex=True) is True:
			cmds.evalDeferred('import maya.cmds as cmds; cmds.deleteUI("'+self.windowName+'", wnd=True)')
			
	# Window size
	def resizeWindow(self):
		if cmds.optionVar(q=self.saveWindowSize) == 0:
			cmds.window(self.windowName, e=True, wh=self.windowSize)
	
	# Default settings
	def defaultSettings(self, reset=False):
		if cmds.optionVar(ex=self.saveWindowSize) == 0:
			cmds.optionVar(iv=(self.saveWindowSize, 1))
		if reset is True or cmds.optionVar(ex=self.bakeMode) == 0:
			cmds.optionVar(iv=(self.bakeMode, 1))
		if reset is True or cmds.optionVar(ex=self.setObjSpc) == 0:
			cmds.optionVar(iv=(self.setObjSpc, 1))
		if reset is True or cmds.optionVar(ex=self.clearSel) == 0:
			cmds.optionVar(iv=(self.clearSel, 1))
		if reset is True or cmds.optionVar(ex=self.bakePos) == 0:
			cmds.optionVar(iv=(self.bakePos, 1))
		if reset is True or cmds.optionVar(ex=self.bakeRot) == 0:
			cmds.optionVar(iv=(self.bakeRot, 1))
		if reset is True or cmds.optionVar(ex=self.bakeScale) == 0:
			cmds.optionVar(iv=(self.bakeScale, 1))
	
	# Reset settings
	def resetSettings(self, *args):
		self.defaultSettings(reset=True)
		self.windowSetup()
	
	# Save settings
	def saveSettings(self, *args):
		cmds.optionVar(iv=(self.saveWindowSize, cmds.menuItem(self.windowSizeMenuItem, q=True, cb=True)))
		cmds.optionVar(iv=(self.bakeMode, cmds.radioButtonGrp(self.bakeMode, q=True, sl=True)))
		cmds.optionVar(iv=(self.setObjSpc, cmds.checkBoxGrp(self.setObjSpc, q=True, v1=True)))
		cmds.optionVar(iv=(self.clearSel, cmds.checkBoxGrp(self.clearSel, q=True, v1=True)))
		cmds.optionVar(iv=(self.bakePos, cmds.checkBoxGrp(self.bakePos, q=True, v1=True)))
		cmds.optionVar(iv=(self.bakeRot, cmds.checkBoxGrp(self.bakeRot, q=True, v1=True)))
		cmds.optionVar(iv=(self.bakeScale, cmds.checkBoxGrp(self.bakeScale, q=True, v1=True)))
	
	# Setup window
	def windowSetup(self):
		cmds.menuItem(self.windowSizeMenuItem, e=True, cb=cmds.optionVar(q=self.saveWindowSize))
		cmds.radioButtonGrp(self.bakeMode, e=True, sl=cmds.optionVar(q=self.bakeMode))
		cmds.checkBoxGrp(self.setObjSpc, e=True, v1=cmds.optionVar(q=self.setObjSpc))
		cmds.checkBoxGrp(self.clearSel, e=True, v1=cmds.optionVar(q=self.clearSel))
		cmds.checkBoxGrp(self.bakePos, e=True, v1=cmds.optionVar(q=self.bakePos))
		cmds.checkBoxGrp(self.bakeRot, e=True, v1=cmds.optionVar(q=self.bakeRot))
		cmds.checkBoxGrp(self.bakeScale, e=True, v1=cmds.optionVar(q=self.bakeScale))
		self.saveSettings()
	
	def initializeWindow(self):
		cmds.showWindow(self.windowName)
		self.resizeWindow()
		cmds.setFocus(self.windowName)
		
	# Create window
	def createWindow(self):
		# If window already opened, set focus on it
		if cmds.window(self.windowName, ex=True) is True:
			self.initializeWindow()
			return
		
		# Window
		cmds.window(self.windowName, t=self.windowTitle, mb=True, wh=self.windowSize)
		
		# Edit Menu
		cmds.menu(l="Edit")
		cmds.menuItem(l="Save Settings", c=partial(self.saveSettings), ecr=False)
		cmds.menuItem(l="Reset Settings", c=partial(self.resetSettings), ecr=False)
		cmds.menuItem(d=True)
		cmds.menuItem(self.windowSizeMenuItem, l="Save Window Size", c=partial(self.saveSettings), cb=False, ecr=False)
		cmds.setParent("..")
		
		# Help Menu
		cmds.menu(l="Help", helpMenu=True)
		cmds.menuItem(l="Help on "+self.windowTitle, i="help.png", c=partial(self.helpCmd), ecr=False)
		cmds.setParent("..")
		
		# Window Form (START)
		cmds.formLayout(self.pfx+"windowForm")
		
		# Tab Layout (START)
		cmds.tabLayout(self.pfx+"tabLayout", tv=False)
		cmds.formLayout(self.pfx+"tabForm")
		
		# Scroll Layout (START)
		cmds.scrollLayout(self.pfx+"scrollLayout", cr=True)
		cmds.formLayout(self.pfx+"scrollForm")
		
		# Description Frame (START)
		cmds.frameLayout(self.pfx+"Description_frameLayout", cll=True, l="Description", li=5, bgs=True, mh=4, mw=0)
		
		# Description Column (START)
		cmds.columnLayout(cat=("left", 20), adj=1)
		
		# Description
		cmds.text(l="Bakes selected component or current tool pivot transformations on object.", al="left")
		cmds.setParent("..")
		
		# Description Column (END)
		cmds.setParent("..")
		
		# Settings Frame (START)
		cmds.frameLayout(self.pfx+"Settings_frameLayout", cll=True, l="Settings", li=5, bgs=True, mh=4, mw=0)
		
		# Settings Column (START)
		cmds.columnLayout(cat=("left", 0), adj=1)
		
		# Space
		cmds.checkBoxGrp(self.setObjSpc, l1="Set tools axis to object space", cat=(1, "left", 143), cc=partial(self.saveSettings))
		
		# Clear
		cmds.checkBoxGrp(self.clearSel, l1="Set selection type to object", cat=(1, "left", 143), cc=partial(self.saveSettings))
		
		# Separation
		cmds.rowLayout(h=3)
		cmds.setParent("..")
		cmds.rowLayout(h=2, bgc=[0.266, 0.266, 0.266])
		cmds.setParent("..")
		cmds.rowLayout(h=3)
		cmds.setParent("..")
		
		# Bake
		cmds.rowLayout(nc=2, cw=(1, 134), cat=(1, "right", 0), ct2=("left", "left"))
		cmds.text(l="Bake:")
		cmds.radioButtonGrp(self.bakeMode, nrb=2, l="", la2=("Component", "Pivot"), cw3=(4, 110, 110), cc=partial(self.saveSettings))
		cmds.setParent("..")
		
		# Transformations
		cmds.rowLayout(nc=2, cw=(1, 134), cat=(1, "right", 0), ct2=("left", "left"))
		cmds.text(l="Transformations:")
		cmds.checkBoxGrp(self.bakePos, l1="Translation", cat=(1, "left", 6), cc=partial(self.saveSettings))
		cmds.setParent("..")
		
		cmds.checkBoxGrp(self.bakeRot, l1="Rotation", cat=(1, "left", 143), cc=partial(self.saveSettings))
		cmds.checkBoxGrp(self.bakeScale, l1="Scale", cat=(1, "left", 143), cc=partial(self.saveSettings))
		
		# Settings Column (END)
		cmds.setParent("..")
		
		# Settings Frame (END)
		cmds.setParent("..")
		
		# Scroll Layout (END)
		cmds.setParent("..")
		cmds.setParent("..")
		
		# Tab Layout (END)
		cmds.setParent("..")
		cmds.setParent("..")
		
		# Buttons
		cmds.formLayout(self.pfx+"Buttons_formLayout", nd=150)
		if int(cmds.about(mjv=True)) < 2020:
			cmds.iconTextButton(self.pfx+"ApplyAndClose_button", st="textOnly", l=self.runLabel, c=rpartial(self.runCmd, closeWindow=True), fla=False, h=26, rpt=True)
			cmds.iconTextButton(self.pfx+"Apply_button", st="textOnly", l="Apply", c=rpartial(self.runCmd, closeWindow=False), fla=False, h=26, rpt=True)
		else:
			cmds.iconTextButton(self.pfx+"ApplyAndClose_button", st="textOnly", l=self.runLabel, c=partial(self.runCmd, closeWindow=True), fla=False, h=26, rpt=True)
			cmds.iconTextButton(self.pfx+"Apply_button", st="textOnly", l="Apply", c=partial(self.runCmd, closeWindow=False), fla=False, h=26, rpt=True)
		cmds.iconTextButton(self.pfx+"Close_button", st="textOnly", l="Close", c=partial(self.closeWindow), fla=False, h=26, rpt=True)
		cmds.setParent("..")
		
		# Window Form (END)
		cmds.setParent("..")
		
		# Window Form Layout
		cmds.formLayout(self.pfx+"windowForm", e=True,
			af=[(self.pfx+"tabLayout", "top", 0), (self.pfx+"tabLayout", "left", 0), (self.pfx+"tabLayout", "right", 0), (self.pfx+"tabLayout", "bottom", 36)])
		
		cmds.formLayout(self.pfx+"windowForm", e=True,
			ac=(self.pfx+"Buttons_formLayout", "top", 5, self.pfx+"tabLayout"),
			af=[(self.pfx+"Buttons_formLayout", "left", 5), (self.pfx+"Buttons_formLayout", "right", 5)],
			an=(self.pfx+"Buttons_formLayout", "bottom"))
		
		# Tabs Form Layout
		cmds.formLayout(self.pfx+"tabForm", e=True,
			af=[(self.pfx+"scrollLayout", "top", 2), (self.pfx+"scrollLayout", "left", 2), (self.pfx+"scrollLayout", "right", 2), (self.pfx+"scrollLayout", "bottom", 2)])
		
		# Scroll Form Layout
		cmds.formLayout(self.pfx+"scrollForm", e=True,
			af=[(self.pfx+"Description_frameLayout", "top", 0), (self.pfx+"Description_frameLayout", "left", 0), (self.pfx+"Description_frameLayout", "right", 0)],
			an=(self.pfx+"Description_frameLayout", "bottom"))
		
		cmds.formLayout(self.pfx+"scrollForm", e=True,
			ac=(self.pfx+"Settings_frameLayout", "top", 0, self.pfx+"Description_frameLayout"),
			af=[(self.pfx+"Settings_frameLayout", "left", 0), (self.pfx+"Settings_frameLayout", "right", 0)],
			an=(self.pfx+"Settings_frameLayout", "bottom"))
		
		# Buttons Form Layout
		cmds.formLayout(self.pfx+"Buttons_formLayout", e=True,
			af=[(self.pfx+"ApplyAndClose_button", "top", 0), (self.pfx+"ApplyAndClose_button", "left", 0)],
			ap=(self.pfx+"ApplyAndClose_button", "right", 2, 50),
			an=(self.pfx+"ApplyAndClose_button", "bottom"))
		
		cmds.formLayout(self.pfx+"Buttons_formLayout", e=True,
			af=(self.pfx+"Apply_button", "top", 0),
			ap=[(self.pfx+"Apply_button", "left", 2, 50), (self.pfx+"Apply_button", "right", 2, 100)],
			an=(self.pfx+"Apply_button", "bottom"))
			
		cmds.formLayout(self.pfx+"Buttons_formLayout", e=True,
			af=[(self.pfx+"Close_button", "top", 0), (self.pfx+"Close_button", "right", 0)],
			ap=(self.pfx+"Close_button", "left", 2, 100),
			an=(self.pfx+"Close_button", "bottom"))
		
		# Window Setup
		self.defaultSettings(reset=False)
		self.windowSetup()
		self.initializeWindow()
