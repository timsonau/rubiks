from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''
    rotations = '' 
    
    if(theCube.areBottomEdgesSolved()):
        if(_doesBottomEdgeMatchMiddle(theCube)):
            return rotations
        theCube.rotate(ALL_SIDE_180_ROTATION)
        rotations += ALL_SIDE_180_ROTATION
        
    
    if (not (_isTopDaisyComplete(theCube))):
        rotations += _buildDaisyPatternTop(theCube)
        
    rotations += _buildBottomCrossWithTopDaisy(theCube)
    return rotations

def _buildDaisyPatternTop(cube):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    rotations = ''
    MAX_POSSIBLE_ROTATIONS = 4
    rotation_num = 0
    while(rotation_num <= MAX_POSSIBLE_ROTATIONS and not(_isTopDaisyComplete(cube))): 
        if (cube.get()[UBM] != downFace):
            rotations += _solveBottomPetal(cube)
        if(cube.get()[UMR] != downFace):
            rotations += _solveRightPetal(cube)
        if(cube.get()[UTM] != downFace):
            rotations += _solveTopPetal(cube)
        if(cube.get()[UML] != downFace):
            rotations += _solveLeftPetal(cube)
        rotation_num += 1
    return rotations

def _solveBottomPetal(cube):
    rotations = ''
    posOfPetal = _findPositionOfNearestAvaliablePetalInFrontFace(cube)
    if(posOfPetal == RML):
        rotations = 'f'
    elif(posOfPetal == LMR):
        rotations = 'F'
    elif(posOfPetal == DTM):
        rotations = FRONT_180_ROTATION
    elif(posOfPetal == FMR):
        rotations = 'uR'
    elif(posOfPetal == FML):
        rotations = 'Ul'
    elif(posOfPetal == FBM):
        rotations = 'fuR'
    elif(posOfPetal == FTM):
        rotations = 'FuR'
    else:
        rotations = 'U'
    cube.rotate(rotations)
    return rotations

def _solveRightPetal(cube):
    rotations = ''
    posOfPetal = _findPositionOfNearestAvaliablePetalInRightFace(cube)
    if(posOfPetal == BML):
        rotations = 'r' 
    elif(posOfPetal == FMR):
        rotations = 'R'
    elif(posOfPetal == DMR):
        rotations = cube.withRespectToRight(FRONT_180_ROTATION)
    elif(posOfPetal == RMR):
        rotations = 'uB'
    elif(posOfPetal == RML):
        rotations = 'Uf'
    elif(posOfPetal == RBM):
        rotations = 'RUf'
    elif(posOfPetal == RTM):
        rotations = 'rUf'
    else:
        rotations = 'U'
        
    cube.rotate(rotations)
    return rotations

def _solveTopPetal(cube):
    rotations = ''
    posOfPetal = _findPositionOfNearestAvalaiblePetalInBackFace(cube)
    if(posOfPetal == LML):
        rotations = 'b'
    elif(posOfPetal == RMR):
        rotations = 'B'
    elif(posOfPetal == DBM):
        rotations = cube.withRespectToBack(FRONT_180_ROTATION)
    elif(posOfPetal == BMR):
        rotations = 'uL'
    elif(posOfPetal == BML):
        rotations = 'Ur'
    elif(posOfPetal == BBM):
        rotations = 'buL'
    elif(posOfPetal == BTM):
        rotations = 'BuL'
    else:
        rotations = 'U'
    cube.rotate(rotations)
    return rotations

def _solveLeftPetal(cube):
    rotations = ''
    posOfPetal = _findPositionOfNearestAvalaiblePetalInLeftFace(cube)
    if(posOfPetal == BMR):
        rotations = 'L'
    elif(posOfPetal == FML):
        rotations = 'l'
    elif(posOfPetal == DML):
        rotations += cube.withRespectToLeft(FRONT_180_ROTATION)
    elif(posOfPetal == LML):
        rotations = 'Ub'
    elif(posOfPetal == LMR):
        rotations = 'uF'
    elif(posOfPetal == LTM):
        rotations = 'LuF'
    elif(posOfPetal == LBM):
        rotations = 'luF'
    else:
        rotations = 'U'
    cube.rotate(rotations)
    return rotations

def _findTheNearestPositionWithPetal(cube, positions):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    for pos in positions:
        if cubeList[pos] == downFace:
            return pos
    return -1

def _findPositionOfNearestAvalaiblePetalInLeftFace(cube):
    postitionsInLeftFace = [BMR, FML, DML, LML, LMR, LTM, LBM]
    return _findTheNearestPositionWithPetal(cube, postitionsInLeftFace)

def _findPositionOfNearestAvalaiblePetalInBackFace(cube):
    postitionsInBackFace = [LML, RMR, DBM, BTM, BMR, BML, BBM]
    return _findTheNearestPositionWithPetal(cube, postitionsInBackFace)

def _findPositionOfNearestAvaliablePetalInRightFace(cube):
    postitionsInRightFace = [BML, FMR, DMR, RMR, RML, RBM, RTM]
    return _findTheNearestPositionWithPetal(cube, postitionsInRightFace)

def _findPositionOfNearestAvaliablePetalInFrontFace(cube):
    positionsInFrontFace = [RML, LMR, DTM, FMR, FML, FTM, FBM]
    return _findTheNearestPositionWithPetal(cube, positionsInFrontFace)
    
def _buildBottomCrossWithTopDaisy(cube):
    rotations = ''
    MAX_POSSIBLE_ROTATIONS = 3
    rotation_num = 0
    while((rotation_num <= MAX_POSSIBLE_ROTATIONS) and not(_isBottomCrossSolved(cube))):
        rotations += _rotateTopEdgesWithMatchingMiddle(cube)
        cube.rotate('U')
        rotations+= 'U'
        rotation_num += 1
    cube.rotate('u')
    rotations = rotations[:-1]
    return rotations

def _isBottomCrossSolved(cube):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    return (cubeList[DTM] == downFace) and (cubeList[DMR] == downFace) and (cubeList[DBM] == downFace) and (cubeList[DML] == downFace)

def _isTopDaisyComplete(cube):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    return (cubeList[UTM] == downFace) and (cubeList[UMR] == downFace) and (cubeList[UBM] == downFace) and (cubeList[UML] == downFace)

def _doesBottomEdgeMatchMiddle(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    return (cubeList[FBM] == frontFace) and (cubeList[RBM] == rightFace) and (cubeList[BBM] == backFace) and (cubeList[LBM] == leftFace)

    
def _rotateTopEdgesWithMatchingMiddle(cube):
    cubeList = cube.get()
    rotations = ""
    downFace = cubeList[DMM]
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    hasBeenSolved = {'f': cubeList[BTM] == downFace, 'r': cubeList[BMR] == downFace, 'b': cubeList[BBM] == downFace, 'l': cubeList[BML] == downFace}
    
    if (not(hasBeenSolved['f'])):
        doesFrontTopEdgeMatchMiddle = (cubeList[FTM] == frontFace) and (cubeList[UBM] == downFace)
        if(doesFrontTopEdgeMatchMiddle):
            rotation = FRONT_180_ROTATION
            cubeList = cube.rotate(rotation)
            rotations += rotation
    
    if (not(hasBeenSolved['r'])):
        doesRightTopEdgeMatchMiddle = (cubeList[RTM] == rightFace) and (cubeList[UMR] == downFace)
        if(doesRightTopEdgeMatchMiddle):
            rotation = cube.withRespectToRight(FRONT_180_ROTATION)
            cubeList = cube.rotate(rotation)
            rotations += rotation
            
    if (not(hasBeenSolved['b'])):
        doesBackTopEdgeMatchMiddle = (cubeList[BTM] == backFace) and (cubeList[UTM] == downFace)
        if(doesBackTopEdgeMatchMiddle):
            rotation = cube.withRespectToBack(FRONT_180_ROTATION)
            cubeList = cube.rotate(rotation)
            rotations += rotation
    
    if (not(hasBeenSolved['l'])):
        doesLeftTopEdgeMatchMiddle = (cubeList[LTM] == leftFace) and (cubeList[UML] == downFace)
        if(doesLeftTopEdgeMatchMiddle):
            rotation = cube.withRespectToLeft(FRONT_180_ROTATION)
            cubeList = cube.rotate(rotation)
            rotations += rotation
           
    return rotations
