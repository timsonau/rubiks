from rubik.model.cube import Cube
from rubik.model.constants import *
import string

def rotate(parms):    
    """Return rotated cube""" 
    result = {}
    #check keys
    allowedKeys = {'cube', 'dir'}
    if (not (parms.keys() <= allowedKeys)):
        result['status'] = INVALID_KEY_STATUS_MSG
        return result
    
    #check cube
    encodedCube = parms.get('cube')
    try:
        theCube = Cube(encodedCube)
    except Exception as e:
        result['status'] = INVALID_CUBE_STATUS_MSG + e.args[0]
        return result
    
    #check directions
    directions = parms.get('dir')
    try:
        theCube.rotate(directions)
    except Exception as e:
        result['status'] = INVALID_DIRECTION_STATUS_MSG + e.args[0]
        return result
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result
