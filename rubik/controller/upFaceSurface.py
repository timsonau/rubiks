from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''
    rotations = ''
    if (theCube.isUpSurfaceSolved()):
        rotations += ''
    else:
        MAX_ROTATIONS = 5
        rotation_num = 1
        while((not theCube.isUpSurfaceSolved()) and  rotation_num < MAX_ROTATIONS):
            cornersSolved = _numUpCornersSolved(theCube)
            if (cornersSolved == 0): 
                rotations += _positionUpFaceColorInLeftTopRight(theCube)
            elif (cornersSolved == 1): 
                rotations += _positionUpFaceColorInUpBottomLeft(theCube)
            else: 
                rotations += _positionUpFaceColorInFrontTopLeft(theCube)
            
            theCube.rotate(UP_FACE_SURFACE_ROTATION)
            rotations += UP_FACE_SURFACE_ROTATION
            rotation_num += 1
    
    if(not theCube.isUpSurfaceSolved()):
        raise ValueError(CUBE_HAS_FLIPPED_CORNER_EXCEPTION_MSG)
    
    return rotations

def _positionUpFaceColorInFrontTopLeft(cube):
    return _positionUpFaceColorInPosition(cube, FTL)

def _positionUpFaceColorInUpBottomLeft(cube):
    return _positionUpFaceColorInPosition(cube, UBL)

def _positionUpFaceColorInLeftTopRight(cube):
    return _positionUpFaceColorInPosition(cube, LTR)

def _positionUpFaceColorInPosition(cube, position):
    rotations = ''
    cubeList = cube.get()
    upFace = cubeList[UMM]
    MAX_ROTATIONS = 4
    rotation_num = 1
    
    while(not(cubeList[position] == upFace) and rotation_num < MAX_ROTATIONS):
        rotations += 'U'
        cube.rotate('U')
        cubeList = cube.get()
        rotation_num += 1
    return rotations

def _numUpCornersSolved(cube):
    cubeList = cube.get()
    upFace = cubeList[UMM]
    numSolved = 0
    cornerColors = [cubeList[UTL], cubeList[UTR], cubeList[UBL], cubeList[UBR]]
    for color in cornerColors:
        if(color == upFace):
            numSolved += 1
    return numSolved