from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''
    rotations = ''
    if(theCube.isUpCrossSolved()):
        return rotations
    else:
        rotations += _solveUpLTromino(theCube)
        rotations += _upGradeUpPattern(theCube)
        
    if(not theCube.isUpCrossSolved()): 
        raise ValueError(CUBE_HAS_FLIPPED_EDGE_EXCEPTION_MSG)
    
    return rotations

def _solveUpLTromino(cube):
    rotations = ''
    if(cube.isUpLTrominoSolved()):
        return rotations
    else:
        if(not _isThereUpLTromino(cube)):
            rotations += _solveUpITromino(cube)
            rotations += _upGradeUpPattern(cube)
        rotations += _upperLeftAlignUpLTromino(cube)
    
    return rotations
    
def _isThereUpLTromino(cube):
    cubeList = cube.get()
    upFace = cubeList[UMM]
    upperRightAligned = cubeList[UTM] == upFace and cubeList[UMR] == upFace
    lowerRightAligned = cubeList[UBM] == upFace and cubeList[UMR] == upFace
    lowerLeftAligned = cubeList[UBM] == upFace and cubeList[UML] == upFace
    return upperRightAligned or lowerRightAligned or lowerLeftAligned

def _upperLeftAlignUpLTromino(cube):
    rotations = ''
    MAX_ROTATIONS = 4
    rotation_num = 1
    while(not(cube.isUpLTrominoSolved()) and rotation_num < MAX_ROTATIONS):
        rotations += 'U'
        cube.rotate('U')
        rotation_num += 1
    return rotations

def _solveUpITromino(cube):
    rotations = ''
    if(cube.isUpITrominoSolved()):
        return rotations
    else:
        if(not _isThereUpITromino(cube)):
            rotations += _upGradeUpPattern(cube)
        rotations += _horizontalAlignUpITromino(cube)

    return rotations

def _isThereUpITromino(cube):
    cubeList = cube.get()
    upFace = cubeList[UMM]
    return cubeList[UTM] == upFace and cubeList[UBM] == upFace

def _horizontalAlignUpITromino(cube):
    rotations = ''
    if(not cube.isUpITrominoSolved()):
        cube.rotate('U')
        rotations += 'U'
    return rotations

def _upGradeUpPattern(cube):
    rotations = UP_FACE_CROSS_ROTATION
    cube.rotate(rotations)
    return rotations