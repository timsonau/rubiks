from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperCorners(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the having the upper corners solved
        
        input:  an instance of the cube class with the up surface solved
        output: the rotations required to solve the upper corners
    '''
    rotations = ''
    if(theCube.areUpperCornersSolved()):
        return rotations
    else:
        while(not(theCube.areUpperCornersSolved())):
            
            if(_areThereMatchingCorners(theCube)): 
                rotations += _alignMatchingCornersToCorrectFace(theCube)
            
            rotation = ''
            if(theCube.isUpperFrontLeftCornerSolved() and theCube.isUpperFrontRightCornerSolved()):
                rotation = theCube.withRespectToRight(UPPER_CORNER_ROTATION)
            elif(theCube.isUpperFrontRightCornerSolved() and theCube.isUpperBackRightCornerSolved()):
                rotation = theCube.withRespectToBack(UPPER_CORNER_ROTATION)
            elif(theCube.isUpperBackLeftCornerSolved() and theCube.isUpperBackRightCornerSolved()):
                rotation = theCube.withRespectToLeft(UPPER_CORNER_ROTATION)
            else:
                rotation = UPPER_CORNER_ROTATION
            
            theCube.rotate(rotation)
            rotations += rotation
    return rotations


def _areThereMatchingCorners(cube):
    cubeList = cube.get()
    if(cubeList[LTR] == cubeList[LTL]): return True
    elif(cubeList[RTL] == cubeList[RTR]): return True
    elif(cubeList[FTL] == cubeList[FTR]): return True
    elif(cubeList[BTR] == cubeList[BTL]): return True
    else: return False

def _alignMatchingCornersToCorrectFace(cube):
    rotations = ''
    
    MAX_ROTATIONS = 4
    rotation_num = 1
    while(not(_hasSideBeenAligned(cube)) and rotation_num < MAX_ROTATIONS):
        rotations += 'U'
        cube.rotate('U')
        rotation_num += 1
    return rotations

def _hasSideBeenAligned(cube):
    return _hasFrontFaceBeenAligned(cube) or _hasRightFaceBeenAligned(cube) or _hasBackFaceBeenAligned(cube) or _hasLeftFaceBeenAligned(cube)

def _hasFrontFaceBeenAligned(cube):
    return cube.isUpperFrontLeftCornerSolved() and cube.isUpperFrontRightCornerSolved()

def _hasRightFaceBeenAligned(cube):
    return cube.isUpperFrontRightCornerSolved() and cube.isUpperBackRightCornerSolved()

def _hasBackFaceBeenAligned(cube):
    return cube.isUpperBackLeftCornerSolved() and cube.isUpperBackRightCornerSolved()

def _hasLeftFaceBeenAligned(cube):
    return cube.isUpperFrontLeftCornerSolved() and cube.isUpperBackLeftCornerSolved() 
