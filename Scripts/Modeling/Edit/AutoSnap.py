import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma
import collections

util = om.MScriptUtil()
util.createFromInt(0)

dummy = {}
dummy['mob'] = om.MObject()
dummy['intPtr'] = util.asIntPtr()
dummy['omp'] = om.MPoint()

class MDagPath(om.MDagPath):
    def __init__(self, node=None):
        super(MDagPath, self).__init__()
        if node is not None:
            sel = om.MSelectionList()
            sel.add(node)
            sel.getDagPath(0, self, dummy['mob'])

    def __str__(self):
        return self.fullPathName()

class MeshData(object):
    def __init__(self, mfnMesh):
        self.mesh = mfnMesh
        self.regist()

    def minmax(self, minA, maxA, pos):
        for i in range(3):
            if minA[i] > pos[i]:
                minA[i] = pos[i]
            if maxA[i] <= pos[i]:
                maxA[i] = pos[i]

    def createBlock(self, minA, maxA):
        functions = []
        split = 8
        for i in range(3):
            reach = (maxA[i] - minA[i]) / split
            code = "lambda x: "
            for j in range(split - 1):
                characters = {'min': minA[i], 'reach': reach, 'i': j}
                if j == 0:
                    code += "(((%(min)s - 10000000  <= x <  (%(min)s + %(reach)s * (%(i)s+2)))) * (%(i)s+2) or " % characters
                elif j == split - 2:
                    code += "(((%(min)s + %(reach)s * (%(i)s+1)) <= x <  (%(min)s  + 100000000))) * (%(i)s+2) or 0) - 1" % characters
                else:
                    code += "(((%(min)s + %(reach)s * (%(i)s+1)) <= x <  (%(min)s + %(reach)s * (%(i)s+2)))) * (%(i)s+2) or " % characters
            functions.append(eval(code))
        getBlockKeyFunc = lambda x, y, z: (functions[0](x), functions[1](y), functions[2](z))

        indexDict = collections.defaultdict(list)
        for x in range(1, split):
            reachX = (maxA[0] - minA[0]) / split
            for y in range(1, split):
                reachY = (maxA[1] - minA[1]) / split
                for z in range(1, split):
                    reachZ = (maxA[2] - minA[2]) / split
                    # Use a tuple of coordinates instead of MPoint
                    p = (reachX * x + minA[0], reachY * y + minA[1], reachZ * z + minA[2])
                    a = indexDict[p]
                    for xx in range(2):
                        for yy in range(2):
                            for zz in range(2):
                                a.append((x - xx, y - yy, z - zz))
        return getBlockKeyFunc, indexDict

    def getPoints(self):
        posA = om.MPointArray()
        self.mesh.getPoints(posA, om.MSpace.kWorld)
        return posA

    def regist(self):
        posA = self.getPoints()
        length = posA.length()
        self.posA = posA

        minXYZ = [100000, 100000, 100000]
        maxXYZ = [-100000, -100000, -100000]
        for i in range(length):
            pos = posA[i]
            self.minmax(minXYZ, maxXYZ, pos)

        getBlockKeyFunc, indexDict = self.createBlock(minXYZ, maxXYZ)
        pointsDict = collections.defaultdict(list)
        for i in range(length):
            pos = posA[i]
            key = getBlockKeyFunc(pos[0], pos[1], pos[2])
            pointsDict[key].append((pos, i))

        for points, keys in indexDict.items():
            if not any(pointsDict[k] for k in keys):
                indexDict[points] = False

        self.point_boxIndex = indexDict
        self.boxIndex_points = pointsDict

    def getColosetVertexId(self, point):
        minLength = 10000000000
        colosetBox = None

        # Convert back to MPoint for distance calculation
        for k, v in self.point_boxIndex.items():
            if v:
                k_point = om.MPoint(k[0], k[1], k[2])  # Convert tuple back to MPoint
                length = k_point.distanceTo(point)
                if length < minLength:
                    minLength = length
                    colosetBox = k

        if colosetBox is None:
            return -1

        minLength = 10000000000
        result = -1

        for k in self.point_boxIndex[colosetBox]:
            points = self.boxIndex_points[k]

            for _point, idx in points:
                length = _point.distanceTo(point)
                if length < minLength:
                    minLength = length
                    result = idx

        return result

class LatticeData(MeshData):
    def __init__(self, mfnLattice):
        super(LatticeData, self).__init__(mfnLattice)

    def getPoints(self):
        mfnLattice = self.mesh
        divisions = cmds.lattice(mfnLattice.fullPathName(), q=True, divisions=True)
        points = om.MPointArray()
        for u in range(divisions[2]):
            for t in range(divisions[1]):
                for s in range(divisions[0]):
                    trans = cmds.pointPosition(mfnLattice.fullPathName() + '.pt[%s][%s][%s]' % (s, t, u), world=True)
                    points.append(om.MPoint(trans[0], trans[1], trans[2]))

        return points

def progress(**kwargs):
    if cmds.about(b=True):
        return False
    if kwargs.get('maxValue', False) is not False and kwargs['maxValue'] == 0:
        return False
    cmds.progressWindow(**kwargs)

def isLttice(targetMesh):
    try:
        oma.MFnLattice(MDagPath(targetMesh))
        return True
    except:
        return False

def applySnapOnClosetVertex(targetMesh, moveVertexList):
    if isLttice(targetMesh):
        target = oma.MFnLattice(MDagPath(targetMesh))
        tgtMesh = LatticeData(target)
    else:
        target = om.MFnMesh(MDagPath(targetMesh))
        tgtMesh = MeshData(target)
    tgtPoints = tgtMesh.getPoints()

    moveNode = moveVertexList[0].split('.')[0]
    if isLttice(moveNode):
        compName = 'pt'
        movTarget = oma.MFnLattice(MDagPath(moveNode))
        movMesh = LatticeData(movTarget)
    else:
        compName = 'vtx'
        movTarget = om.MFnMesh(MDagPath(moveNode))
        movMesh = MeshData(movTarget)
    movPoints = movMesh.getPoints()

    length = movPoints.length()

    vtx = cmds.ls(moveVertexList, fl=True)
    if compName == 'pt':
        divisions = cmds.lattice(moveNode, divisions=True, q=True)
        vertexIndex = [
            (int(v.split('[')[-3].split(']')[0]),
             int(v.split('[')[-2].split(']')[0]),
             int(v.split('[')[-1].split(']')[0]))
            for v in vtx
        ]
        vertexIndex = tuple((s + divisions[0] * t + (divisions[0] * divisions[1]) * u) for s, t, u in vertexIndex)
    else:
        vertexIndex = tuple(int(v.split('[')[-1].split(']')[0]) for v in vtx)

    progress(title='rsSnapOnClosestVertex', progress=0, maxValue=length, status='', isInterruptable=True)
    for i in range(length):
        if i in vertexIndex:
            if i % 50 == 0:
                progress(e=True, progress=i, status=f'{i}/{length}')
            num = tgtMesh.getColosetVertexId(movPoints[i])
            point = tgtPoints[num]
            cmds.move(point.x, point.y, point.z, f'{moveNode}.{compName}[{i}]', a=True, ws=True)
    progress(endProgress=1)

def cmd():
    try:
        companyName = cmds.displayString('rsCompany', q=True, value=True)
        if companyName == 'square-enix':
            pass
        else:
            mel.eval('RsDccTpc ("rsSnapOnClosestVertex", "2015/10", "kimutoru@rstool", "cmd", "功能描述","");')
    except Exception as e:
        print(f"Error: {e}")

    cmds.undoInfo(ock=True)
    sel = cmds.ls(sl=True)
    if len(sel) > 1:
        if isLttice(sel[0].split('.')[0]):
            vtx = cmds.ls('*.pt[*][*][*]', sl=True, fl=True)
            if not vtx:
                moveNode = sel[0].split('.')[0]
                vtx = cmds.ls(moveNode + '.pt[*]')
        else:
            vtx = cmds.ls('*.vtx[*]', sl=True, fl=True)
            if not vtx:
                moveNode = sel[0].split('.')[0]
                vtx = cmds.ls(moveNode + '.vtx[*]')

        applySnapOnClosetVertex(sel[-1], vtx)
    else:
        cmds.error('[rsSnapOnClosestVertex] 请至少选择两个对象，一个是目标对象，另一个是要移动的顶点列表。')
    cmds.undoInfo(cck=True)

# if __name__ == "__main__":
#     cmd()
