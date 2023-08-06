from rubik.model.constants import *
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''
    rotations = ''
    if(theCube.isMiddleLayerSolved()):
        return rotations
    else:
        if(not theCube.isMiddleFrontLeftEdgeSolved()):
            rotations += _solveFrontLeftEdge(theCube)
        if(not theCube.isMiddleFrontRightEdgeSolved()):
            rotations += _solveFrontRightEdge(theCube)
        if(not theCube.isMiddleBackLeftEdgeSolved()):
            rotations += _solveBackLeftEdge(theCube)
        if(not theCube.isMiddleBackRightEdgeSolved()):
            rotations += _solveBackRightEdge(theCube)
    return rotations      

def _solveFrontLeftEdge(cube):
    rotations = ''
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    leftFace = cubeList[LMM]
    
    correctFrontLeftEdgeColors = {frontFace, leftFace}
    rotations += _positionCorrectMiddleEdgeInTopLayer(cube, correctFrontLeftEdgeColors)
    
    if(_canSolveFrontLeftEdgeFromTheFront(cube)):
        rotations += _solveFrontLeftEdgeFromTheFront(cube)
    else:
        rotations += _solveFrontLeftEdgeFromTheLeft(cube)
    
    return rotations

def _solveFrontRightEdge(cube):
    rotations = ''
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    
    correctFrontRightEdgeColors = {frontFace, rightFace}
    rotations += _positionCorrectMiddleEdgeInTopLayer(cube, correctFrontRightEdgeColors)
    
    if(_canSolveFrontRightEdgeFromTheFront(cube)):
        rotations += _solveFrontRightEdgeFromTheFront(cube)
    else:
        rotations += _solveFrontRightEdgeFromTheRight(cube)

    return rotations

def _solveBackLeftEdge(cube):
    rotations = ''
    cubeList = cube.get()
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    
    correctBackLeftEdgeColors = {backFace, leftFace}
    rotations += _positionCorrectMiddleEdgeInTopLayer(cube, correctBackLeftEdgeColors)
    
    if(_canSolveBackLeftEdgeFromTheBack(cube)):
        rotations += _solveBackLeftEdgeFromTheBack(cube)
    else:
        rotations += _solveBackLeftEdgeFromTheLeft(cube)
    return rotations

def _solveBackRightEdge(cube):
    rotations = ''
    cubeList = cube.get()
    backFace = cubeList[BMM]
    rightFace = cubeList[RMM]
    
    correctBackRightEdgeColors = {backFace, rightFace}
    rotations += _positionCorrectMiddleEdgeInTopLayer(cube, correctBackRightEdgeColors)
    
    if(_canSolveBackRightEdgeFromTheBack(cube)):
        rotations += _solveBackRightEdgeFromTheBack(cube)
    else:
        rotations += _solveBackRightEdgeFromTheRight(cube)
    return rotations

def _positionCorrectMiddleEdgeInTopLayer(cube, correctEdgeColors):
    rotations = ''
    cubeList = cube.get()
    
    frontLeftEdgePieceColors = {cubeList[FML], cubeList[LMR]}
    frontRightEdgePieceColors = {cubeList[FMR], cubeList[RML]}
    backLeftEdgePieceColors = {cubeList[BMR], cubeList[LML]}
    backRightEdgePieceColors = {cubeList[BML], cubeList[RMR]}
    
    if (frontLeftEdgePieceColors == correctEdgeColors):
        rotations = _sendUpFrontEdgeToFrontLeftEdge(cube)
    elif (frontRightEdgePieceColors == correctEdgeColors):
        rotations = _sendUpFrontEdgeToFrontRightEdge(cube)
    elif (backLeftEdgePieceColors == correctEdgeColors):
        rotations = _sendUpBackEdgeToBackLeftEdge(cube)
    elif(backRightEdgePieceColors == correctEdgeColors):
        rotations = _sendUpBackEdgeToBackRightEdge(cube)
    else:
        return rotations
    
    return rotations

def _canSolveFrontLeftEdgeFromTheFront(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    leftFace = cubeList[LMM]
    
    return _canSolveMiddleEdgeFromASide(cube, targetOutwardFace=frontFace, targetUpwardFace=leftFace)
   
def _canSolveFrontRightEdgeFromTheFront(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
        
    return _canSolveMiddleEdgeFromASide(cube, targetOutwardFace=frontFace, targetUpwardFace=rightFace)

def _canSolveBackLeftEdgeFromTheBack(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
        
    return _canSolveMiddleEdgeFromASide(cube, targetOutwardFace=backFace, targetUpwardFace=leftFace)

def _canSolveBackRightEdgeFromTheBack(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    rightFace = cubeList[RMM]
        
    return _canSolveMiddleEdgeFromASide(cube, targetOutwardFace=backFace, targetUpwardFace=rightFace)

def _canSolveMiddleEdgeFromASide(cube, targetOutwardFace, targetUpwardFace):
    cubeList = cube.get()
    edgePostionInTopLayer = [(FTM, UBM), (LTM, UML), (BTM, UTM), (RTM, UMR)]
    
    for outwardPos, upwardPos in edgePostionInTopLayer:
        if(cubeList[outwardPos] == targetOutwardFace and cubeList[upwardPos] == targetUpwardFace):
            return True
    return False

def _solveFrontLeftEdgeFromTheFront(cube):
    rotations = _rotateTopLayerUntilCorrectFrontLeftEdgeInUpFrontEdge(cube)
    rotations += _sendUpFrontEdgeToFrontLeftEdge(cube)
    return rotations

def _solveFrontLeftEdgeFromTheLeft(cube):
    rotations = _rotateTopLayerUntilCorrectFrontLeftEdgeInUpLeftEdge(cube)
    rotations += _sendUpLeftEdgeToFrontLeftEdge(cube)
    return rotations

def _solveFrontRightEdgeFromTheFront(cube):
    rotations = _rotateTopLayerUntilCorrectFrontRightEdgeInUpFrontEdge(cube)
    rotations += _sendUpFrontEdgeToFrontRightEdge(cube)
    return rotations

def _solveFrontRightEdgeFromTheRight(cube):
    rotations = _rotateTopLayerUntilCorrectFrontRightEdgeInUpRightEdge(cube)
    rotations += _sendUpRightEdgeToFrontRightEdge(cube)
    return rotations

def _solveBackLeftEdgeFromTheBack(cube):
    rotations = _rotateTopLayerUntilCorrectBackLeftEdgeInUpBackEdge(cube)
    rotations += _sendUpBackEdgeToBackLeftEdge(cube)
    return rotations

def _solveBackLeftEdgeFromTheLeft(cube):
    rotations = _rotateTopLayerUntilCorrectBackLeftEdgeInUpLeftEdge(cube)
    rotations += _sendUpLeftEdgeToBackLeftEdge(cube)
    return rotations

def _solveBackRightEdgeFromTheBack(cube):
    rotations = _rotateTopLayerUntilCorrectBackRightEdgeInUpBackEdge(cube)
    rotations += _sendUpBackEdgeToBackRightEdge(cube)
    return rotations

def _solveBackRightEdgeFromTheRight(cube):
    rotations = _rotateTopLayerUntilCorrectBackRightEdgeInUpRightEdge(cube)
    rotations += _sendUpRightEdgeToBackRightEdge(cube)
    return rotations

def _rotateTopLayerUntilCorrectFrontLeftEdgeInUpFrontEdge(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    leftFace = cubeList[LMM]
    
    correctFrontLeftEdgeColors = {frontFace, leftFace}
    upFrontEdgePiecePos = [FTM, UBM]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upFrontEdgePiecePos, correctFrontLeftEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectFrontLeftEdgeInUpLeftEdge(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    leftFace = cubeList[LMM]
    
    correctFrontLeftEdgeColors = {frontFace, leftFace}
    upLeftEdgePiecePos = [LTM, UML]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upLeftEdgePiecePos, correctFrontLeftEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectFrontRightEdgeInUpFrontEdge(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    
    correctFrontRightEdgeColors = {frontFace, rightFace}
    upFrontEdgePiecPos = [FTM, UBM]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upFrontEdgePiecPos, correctFrontRightEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectFrontRightEdgeInUpRightEdge(cube):
    cubeList = cube.get()
    frontFace = cubeList[FMM]
    rightFace = cubeList[RMM]
    
    correctFrontRightEdgeColors = {frontFace, rightFace}
    upRightEdgePiecPos = [RTM, UMR]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upRightEdgePiecPos, correctFrontRightEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectBackLeftEdgeInUpBackEdge(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    
    correctBackLeftEdgeColors = {backFace, leftFace}
    upBackEdgePiecePos = [BTM, UTM]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upBackEdgePiecePos, correctBackLeftEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectBackLeftEdgeInUpLeftEdge(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    leftFace = cubeList[LMM]
    
    correctBackLeftEdgeColors = {backFace, leftFace}
    upLeftEdgePiecePos = [LTM, UML]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upLeftEdgePiecePos, correctBackLeftEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectBackRightEdgeInUpBackEdge(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    rightFace = cubeList[RMM]
    
    correctBackRightEdgeColors = {backFace, rightFace}
    upBackEdgePiecePos = [BTM, UTM]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upBackEdgePiecePos, correctBackRightEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectBackRightEdgeInUpRightEdge(cube):
    cubeList = cube.get()
    backFace = cubeList[BMM]
    rightFace = cubeList[RMM]
    
    correctBackRightEdgeColors = {backFace, rightFace}
    upRightEdgePiecePos = [RTM, UMR]
    rotations = _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, upRightEdgePiecePos, correctBackRightEdgeColors)
    return rotations

def _rotateTopLayerUntilCorrectMiddleEdgeInCorrectTopEdgePosition(cube, targetTopEdgePosition, correctMiddleEdgeColors):
    rotations = ''
    cubeList = cube.get()
    currTargetTopEdgeColors = {cubeList[pos] for pos in targetTopEdgePosition}
    
    MAX_ROTATIONS = 4
    rotation_num = 1
    while(correctMiddleEdgeColors != currTargetTopEdgeColors and rotation_num < MAX_ROTATIONS):
        rotations += 'U'
        cube.rotate('U')
        cubeList = cube.get()
        currTargetTopEdgeColors = {cubeList[pos] for pos in targetTopEdgePosition}
        rotation_num += 1
    return rotations

def _sendUpFrontEdgeToFrontLeftEdge(cube):
    rotations = 'u' + LEFT_TRIGGER_ROTATION + cube.withRespectToLeft(RIGHT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations

def _sendUpFrontEdgeToFrontRightEdge(cube):
    rotations = 'U' + RIGHT_TRIGGER_ROTATION + cube.withRespectToRight(LEFT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations
    
def _sendUpLeftEdgeToFrontLeftEdge(cube):
    rotations = 'U' + cube.withRespectToLeft(RIGHT_TRIGGER_ROTATION) + LEFT_TRIGGER_ROTATION
    cube.rotate(rotations)
    return rotations

def _sendUpRightEdgeToFrontRightEdge(cube): 
    rotations = 'u' + cube.withRespectToRight(LEFT_TRIGGER_ROTATION) + RIGHT_TRIGGER_ROTATION
    cube.rotate(rotations)
    return rotations

def _sendUpBackEdgeToBackLeftEdge(cube):
    rotations = 'U' + cube.withRespectToBack(RIGHT_TRIGGER_ROTATION) + cube.withRespectToLeft(LEFT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations

def _sendUpLeftEdgeToBackLeftEdge(cube):
    rotations = 'u' + cube.withRespectToLeft(LEFT_TRIGGER_ROTATION) + cube.withRespectToBack(RIGHT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations

def _sendUpBackEdgeToBackRightEdge(cube):
    rotations = 'u' + cube.withRespectToBack(LEFT_TRIGGER_ROTATION) + cube.withRespectToRight(RIGHT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations

def _sendUpRightEdgeToBackRightEdge(cube):
    rotations = 'U' + cube.withRespectToRight(RIGHT_TRIGGER_ROTATION) + cube.withRespectToBack(LEFT_TRIGGER_ROTATION)
    cube.rotate(rotations)
    return rotations
