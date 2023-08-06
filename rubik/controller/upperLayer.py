from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''
    rotations = ''
    MAX_ROTATIONS = 4
    rotation_num = 1
    while(not(theCube.isUpperLayerSolved()) and rotation_num < MAX_ROTATIONS):
        rotation = ''
        if(_isRightSideCompleted(theCube)):
            rotation = theCube.withRespectToLeft(UPPER_LAYER_ROTATION)
        elif(_isLeftSideCompleted(theCube)):
            rotation = theCube.withRespectToRight(UPPER_LAYER_ROTATION)
        elif(_isFrontSideCompleted(theCube)):
            rotation = theCube.withRespectToBack(UPPER_LAYER_ROTATION)
        else:
            rotation = UPPER_LAYER_ROTATION
        theCube.rotate(rotation)
        rotations += rotation
        rotation_num += 1
    
    if(not(theCube.isUpperLayerSolved())):
        raise ValueError(CUBE_HAS_FLIPPED_EDGE_EXCEPTION_MSG)
    
    return rotations


def _isLeftSideCompleted(cube):
    cubeList = cube.get()
    leftFaceColors = {cubeList[LTL], cubeList[LTM], cubeList[LTR], cubeList[LML], cubeList[LMM], cubeList[LMR], cubeList[LBL], cubeList[LBM], cubeList[LBR]} 
    return len(leftFaceColors) == 1

def _isRightSideCompleted(cube):
    cubeList = cube.get()
    rightFaceColors = {cubeList[RTL], cubeList[RTM], cubeList[RTR], cubeList[RML], cubeList[RMM], cubeList[RMR], cubeList[RBL], cubeList[RBM], cubeList[RBR]} 
    return len(rightFaceColors) == 1

def _isFrontSideCompleted(cube):
    cubeList = cube.get()
    frontFaceColors = {cubeList[FTL], cubeList[FTM], cubeList[FTR], cubeList[FML], cubeList[FMM], cubeList[FMR], cubeList[FBL], cubeList[FBM], cubeList[FBR]} 
    return len(frontFaceColors) == 1
    
