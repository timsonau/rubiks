from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''
    rotations = ''
    
    if(not isinstance(theCube, Cube)):
        raise TypeError(INVALID_TYPE_NOT_A_CUBE_EXCEPTION_MSG)
    if(theCube.isBottomLayerSolved()):
        return rotations
    else:
        if(not theCube.isBottomFrontLeftCornerSolved()):
            rotations += _solveBottomFrontLeftCorner(theCube)
        if(not theCube.isBottomFrontRightCornerSolved()):
            rotations += _solveBottomFrontRightCorner(theCube)
        if(not theCube.isBottomBackLeftCornerSolved()):
            rotations += _solveBottomBackLeftCorner(theCube)
        if(not theCube.isBottomBackRightCornerSolved()):
            rotations += _solveBottomBackRightCorner(theCube)
            
    return rotations

def _solveBottomFrontLeftCorner(cube):
    rotations = _positionCorrectBottomFrontLeftCornerInTopFrontLeftCorner(cube)
    rotations += _sendTopFrontLeftCornerToBottomFrontLeftCorner(cube)
    return rotations

def _solveBottomFrontRightCorner(cube):
    rotations = _positionCorrectBottomFrontRightCornerInTopFrontRightCorner(cube)
    rotations += _sendTopFrontRightCornerToBottomFrontRightCorner(cube)
    return rotations

def _solveBottomBackLeftCorner(cube):
    rotations = _positionCorrectBottomBackLeftCornerInTopBackLeftCorner(cube)
    rotations += _sendTopBackLeftCornerToBottomBackLeftCorner(cube)
    return rotations

def _solveBottomBackRightCorner(cube):
    rotations = _positionCorrectBottomBackRightCornerInTopBackRightCorner(cube)
    rotations += _sendTopBackRightCornerToBottomBackRightCorner(cube)
    return rotations

def _positionCorrectBottomFrontLeftCornerInTopFrontLeftCorner(cube):
    cubeList = cube.get()
    rotations = ''
    frontFace = cubeList[FMM]
    leftFace = cubeList[LMM]
    downFace = cubeList[DMM]
    
    correctBottomFrontLeftCornerColors = {leftFace, frontFace, downFace}
    topFrontLeftCornerPiecePos = [LTR, FTL, UBL]
    
    rotations += _postionCorrectBottomCornerInCorrectTopCorner(cube, topFrontLeftCornerPiecePos, correctBottomFrontLeftCornerColors)
    return rotations

def _positionCorrectBottomFrontRightCornerInTopFrontRightCorner(cube):
    cubeList = cube.get()
    rotations = ''
    
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    downFace = cubeList[DMM]
    
    correctBottomFrontRightCornerColors = {rightFace, frontFace, downFace}
    topFrontRightCornerPiecePos = [RTL, FTR, UBR]
    
    rotations += _postionCorrectBottomCornerInCorrectTopCorner(cube, topFrontRightCornerPiecePos, correctBottomFrontRightCornerColors)
    return rotations

def _positionCorrectBottomBackLeftCornerInTopBackLeftCorner(cube):
    cubeList = cube.get()
    rotations = ''
    
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    downFace = cubeList[DMM]
    
    correctBottomBackLeftCornerColors = {leftFace, backFace, downFace}
    topBackLeftCornerPiecePos = [LTL, BTR, UTL]

    rotations += _postionCorrectBottomCornerInCorrectTopCorner(cube, topBackLeftCornerPiecePos, correctBottomBackLeftCornerColors)
    return rotations

def _positionCorrectBottomBackRightCornerInTopBackRightCorner(cube):
    cubeList = cube.get()
    rotations = ''
    
    backFace = cubeList[BMM]
    rightFace = cubeList[RMM]
    downFace = cubeList[DMM]
    
    correctBottomBackRightCornerColors = {rightFace, backFace, downFace}
    topBackRightCornerPiecePos = [RTR, BTL, UTR]

    rotations += _postionCorrectBottomCornerInCorrectTopCorner(cube, topBackRightCornerPiecePos, correctBottomBackRightCornerColors)
    return rotations

def _postionCorrectBottomCornerInCorrectTopCorner(cube, topCornerPositions, correctCornerColors):
    rotations = ''
    
    rotations += _postionCorrectBottomCornerToTopLayer(cube, correctCornerColors)
    rotations += _rotateTopLayerUntilCorrectBottomCornerInTopLayerIsPositionedDirectlyAboveItsCorrectCorner(cube, topCornerPositions, correctCornerColors)
    return rotations

def _rotateTopLayerUntilCorrectBottomCornerInTopLayerIsPositionedDirectlyAboveItsCorrectCorner(cube, topCornerPositions, correctCornerColors):
    cubeList = cube.get()
    rotations = ''
    currTopCornerColors = {cubeList[pos] for pos in topCornerPositions}
    
    MAX_ROTATIONS = 4
    rotation_num = 1
    while(correctCornerColors != currTopCornerColors and rotation_num < MAX_ROTATIONS):
        rotations += 'U'
        cube.rotate('U')
        cubeList = cube.get()
        currTopCornerColors = {cubeList[pos] for pos in topCornerPositions}
        rotation_num += 1
    return rotations

def _postionCorrectBottomCornerToTopLayer(cube, correctCornerColors):
    cubeList = cube.get()
    rotations = ''
    
    bottomFrontLeftCornerPieceColors = {cubeList[LBR], cubeList[FBL], cubeList[DTL]}
    bottomFrontRightCornerPieceColors = {cubeList[RBL], cubeList[FBR], cubeList[DTR]}
    bottomBackLeftCornerPieceColors = {cubeList[LBL], cubeList[BBR], cubeList[DBL]}
    bottomBackRightCornerPieceColors = {cubeList[RBR], cubeList[BBL], cubeList[DBR]}
    
    if(bottomFrontLeftCornerPieceColors == correctCornerColors):
        rotations += 'luL'
    elif(bottomFrontRightCornerPieceColors == correctCornerColors):
        rotations += 'RUr'
    elif(bottomBackLeftCornerPieceColors == correctCornerColors):
        rotations += 'LUl'
    elif(bottomBackRightCornerPieceColors == correctCornerColors):
        rotations += 'ruR'
    else:
        return rotations
    
    cube.rotate(rotations)
    return rotations

def _sendTopFrontLeftCornerToBottomFrontLeftCorner(cube):
    rotations = ''
    cubeList = cube.get()
    downFace = cubeList[DMM]
    
    if(cubeList[FTL] == downFace):
        rotations = 'ulUL'
    elif(cubeList[LTR] == downFace):
        rotations = 'luL'
    elif(cubeList[UBL] == downFace):
        rotations = 'luuLUluL'
    else:
        rotations = ''
        
    cube.rotate(rotations)
    return rotations

def _sendTopFrontRightCornerToBottomFrontRightCorner(cube):
    rotations = ''
    cubeList = cube.get()
    downFace = cubeList[DMM]
    if(cubeList[RTL] == downFace):
        rotations = 'RUr'
    elif(cubeList[FTR] == downFace):
        rotations = 'URur'
    elif(cubeList[UBR] == downFace):
        rotations = 'RUUruRUr'
    else:
        rotations = ''
    cube.rotate(rotations)
    return rotations

def _sendTopBackLeftCornerToBottomBackLeftCorner(cube):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    if(cubeList[LTL] == downFace):
        rotations = 'LUl'
    elif(cubeList[BTR] == downFace):
        rotations = 'ULul'
    elif(cubeList[UTL] == downFace):
        rotations = 'LUUluLUl'
    else:
        rotations = ''
    cube.rotate(rotations)
    return rotations

def _sendTopBackRightCornerToBottomBackRightCorner(cube):
    cubeList = cube.get()
    downFace = cubeList[DMM]
    rotations = ""
    if(cubeList[RTR] == downFace):
        rotations = 'ruR'
    elif(cubeList[BTL] == downFace):
        rotations = 'urUR'
    elif(cubeList[UTR] == downFace):
        rotations = 'ruuRUruR'
    else: 
        rotations = ''
        
    cube.rotate(rotations)
    return rotations



