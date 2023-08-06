from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.controller.upperCorners import solveUpperCorners
from rubik.model.constants import *
from rubik.model.cube import Cube
import random
import hashlib

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    allowedKeys = {'cube'}
    if (not (parms.keys() <= allowedKeys)):
        result['status'] = INVALID_KEY_STATUS_MSG
        return result
    
    encodedCube = parms.get('cube')
    try:
        theCube = Cube(encodedCube)
        rotations = ""
        rotations += solveBottomCross(theCube)      #iteration 2
        rotations += solveBottomLayer(theCube)      #iteration 3
        rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
        rotations += solveUpSurface(theCube)        #iteration 5
        rotations += solveUpperCorners(theCube)
        rotations += solveUpperLayer(theCube)       #iteration 6
    except Exception as e:
        result['status'] = INVALID_CUBE_STATUS_MSG + e.args[0]
        return result

    result['solution'] = _optimizeRotations(rotations)
    result['status'] = 'ok'
    username = 'hzs0093'
    result['integrity'] = _createIntegrityToken(encodedCube, result['solution'], username)
                     
    return result

def _optimizeRotations(rotations):
    prevRotation = ""
    consectuiveRotations = 1
    newRotations = ""
    for currentRotation in rotations:
        newRotations += currentRotation
        if currentRotation == prevRotation:
            consectuiveRotations += 1
        else:
            consectuiveRotations = 1
        if(consectuiveRotations == 3):
            newRotations = newRotations[:-3]
            eqivRotation = currentRotation.lower() if currentRotation.isupper() else currentRotation.upper() 
            newRotations += eqivRotation
            consectuiveRotations = 1
            currentRotation = eqivRotation
        prevRotation = currentRotation
    return newRotations

def _createIntegrityToken(cube, solution, username):
    itemToTokenize = cube + solution + username
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    return _getRandSubstringOf(fullToken, 8)
    
def _getRandSubstringOf(word, length):
    startIndex = random.randint(0, len(word) - length)
    endIndex = startIndex + length
    randSubstring =word[startIndex:endIndex]
    return randSubstring
    