from unittest import TestCase
from rubik.view.rotate import rotate
from rubik.model.constants import *
class RotateTest(TestCase):

#Analysis of Rotate
#    A Module
#    Method: rotate performs rotations on the cube per 'dir' key
#    
#    Analysis: Cube.rotate
#        inputs: python dictionary containing
#        1) key: ‘cube’
#            value: string
#                - 54 characters
#                - 6 unique characters from [a-zA-Z0-9]
#                - 5th, 14th, 23rd, 32nd, 41st, and 50th
#                characters must be unique
#                participation: mandatory
#                understanding: arrived unvalidated
#
#        2) key: 'dir'
#            value: string 
#                - .GE. 0 characters
#                - taken from [FfRrBbLlUu]
#                participation: optional, defaults to "F" is missing
#                understanding: arrived unvalidated
#
#         output:
#            side-effects: no external side effects internal state change
#            nominal:
#                return Python dictionary containing: 
#                        1) 'cube': 'www.....bbb' (encoded cube sequence after the rotation has been applied)
#                        2) 'status': 'ok'
#            abnormal:
#                a) Invalid Rotation Input  
#                    return Python dictionary containing: 
#                        1) {‘status’: ‘error: invalid rotation’}
#                b)Invalid Cube Input
#                    return Python dictionary containing: 
#                        1) {‘status’: ‘error: invalid cube’}
#                c)Invalid Key Input
#                    return Python dictionary containing: 
#                        1) {‘status’: ‘error: invalid key input’}
#     Happy path (actual rotation is already tested in cubeTest.py)
#        test 010: Test nominal dir rotation on nominal cube
#        test 020: Test no dir key on nominal cube
#     Sad Path:
#        test 910: Test invalid dir on nominal cube
#        test 920: Test invalid cube, too many (>56) in cube sequence: 55 chars(above bound)
#        test 930: Test invalid cube, too little (<56) characters in cube sequence: 53 chars(below bound)
#        test 940: Test invalid cube, too much unique characters (>6) in cube sequence: 7 (above bound)
#        test 950: Test invalid cube, too little unique characters (<6) in cube sequence: 5 (below bound)
#        test 960: Test invalid cube, middle positions not unique (5th, 14th, 23rd, 32nd, 41st, and 50th)
#        test 970: Test invalid cube, cube with non-equal # of characters for each unique character
#        test 980: Test invalid cube, no cube in param
#        test 990: Test invalid cube, in cube
#        test 911: Test invalid key, detect a key in param that is not 'cube' or 'dir'
#
    def test_rotate_010_ShouldRotateNominalCubeWithNominalRotation(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfFLluUBRrUf'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        expectedCube = 'wbbrbbybbroorrwrrwygwoooooobbrygyygggyrgyroyybwwwwwggg'
        self.assertEqual(expectedCube, result.get('cube'))
    
    def test_rotate_020_ShouldRotateFNominalCubeNoDirKey(self):
        encodedCube = 'ywwrbboyboyowrgyowyryoorgorobbbgywowgwrgygggrgbrwwrbyb'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        expectedCube = 'oryybwbbwgyogrgrowyryoorgorobgbgbworgwrgygwybywowwrbyb'
        self.assertEqual(expectedCube, result.get('cube'))
    
    def test_rotate_910_ShouldReturnInvalidRotationStatus(self):
        encodedCube = 'rogwbbygywoorrwgyrwrbrorbgwwgyygbrwgrogoywoybbyogwboby'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfFLluUBDddDRrUf'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_DIRECTION_STATUS_MSG))
    
    def test_rotate_920_ShouldReturnInvalidCubeStatus55Chars(self):
        encodedCube = 'rogwbbygywoorrwgyrwrbrorbgwwgyygbrwgrogoywoybbyogwbobyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfFLluUBRrUf'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
    
    def test_rotate_930_ShouldReturnInvalidCubeStatus53chars(self):
        encodedCube = 'rogwbbygywoorrwgyrwrbrorbgwwgyygbrwgrogoywoybbyogwbob'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'Ff'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
    
    def test_rotate_940_ShouldReturnInvalidCubeStatusTooManyUniqueChars(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooxooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
        
    def test_rotate_950_ShouldReturnInvalidCubeStatusTooLittleUniqueChars(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyyooooooooo'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
        
    def test_rotate_960_ShouldReturnInvalidCubeStatusMiddlePostionCharsNonUnique(self):
        encodedCube = 'gbybbbgorroywrroroggryowybrbowggrbowwybywgogobywrwwyyg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
        
    def test_rotate_970_ShouldReturnInvalidCubeStatusNonEqualDistributionOfUniqueCharacters(self):
        encodedCube = 'bbbbbbbborrrrrrrroooooooooogggggggggyyyyyyyygwwwwwwwwg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
    
    def test_rotate_980_ShouldReturnInvalidCubeStatusNoCube(self):
        parms = {}
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
        
    def test_rotate_990_ShouldReturnInvalidCubeInvalidChar(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrr!!!!!!!!!ggggggggg*********wwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLlu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
        
    def test_rotate_911_ShouldReturnInvalidKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfLllBlu'
        parms['java'] = 'is_java_and_javascript_related?'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid key', result['status'])
        
    
    
    
    
