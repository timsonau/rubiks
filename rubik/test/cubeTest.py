import unittest
import rubik.model.cube as cube
from rubik.model.constants import *

class CubeTest(unittest.TestCase):
    
#Analysis of Cube
#
#    Cube: class, instance of a state machine, maintain internal state
#    Method: __init__ constructs a logical cube from a serialized string
#            get      yields serialized string of internal representation
#            rotate   performs rotations on the cube per 'dir' key
#    
#    Analysis: Cube.rotate
#         inputs:
#            directions: string, 0 <= length, [FfRrBbLlUu]; optional, defaults to F is missing; unvalidated
#         output:
#            side-effects: no external side effects internal state change
#            nominal:
#                return serialized rotated cube
#            abnormal:
#                raise ValueError Exception (invalid dir)
#                raise TypeError Exception (non-string dir)
#    Analysis: Cube._init__
#        inputs: 
#            cube:
#              - 54 characters
#              - 6 unique characters from [a-zA-Z0-9]
#              - 5th, 14th, 23rd, 32nd, 41st, and 50th
#                  characters must be unique
#              participation: mandatory
#              understanding: arrives unvalidated
#
#
#    happy path:
#        test 010: F rotation
#        test 020: f rotation
#        test 030: R rotation
#        test 040: r rotation
#        test 050: B rotation
#        test 060: b rotation
#        test 070: L rotation
#        test 080: l rotation
#        test 090: U rotation
#        test 100: u rotation
#        test 110: missing direction
#        test 120: empty direction, ""
#        test 130: multi-string direction
#        test 140: Nominal cube initialization
#    sad path:
#        test 910: invalid direction 
#        test 920: non-string direction
#        test 930: invalid cube, missing cube input
#        test 940: invalid cube, cube does not have 54 chars
#        test 950: invalid cube, cube does not have 6 unique chars
#        test 960: invalid cube, cube has char out of bounds [a-zA-Z0-9]
#        test 970: invalid cube, cube does not have unique char in center positions (5th, 14th, 23rd, 32nd 41st, 50th)
#        test 980: invalid cube, cube has unequal distribution of char
#        test 990" invalid cube, cube passed in is not a string.
#
#    evil path:
#        none

    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'wgrboybbogwyrgbwgobygwrbygwowrobyowwyorrwggryrrgoyybob'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        expectedCube = 'bbwbogoyrgwyrgbygobygwrbygwowrobrowgyorrwgwyrwrgoyybob'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'ybgggorgrorbwroggbybrbbbwgogrrroowobyyoywwbwywrwyywgyo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        expectedCube = 'gorbggygrwrbrrowgbybrbbbwgogryrowwobyyoywwowgrobyywgyo'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_030_ShouldRotateCubeInRDirection(self):
        cubeToRotate = '0oyggw00royorryg0oyoy00r0gwroyyorgowgwg0wgry0rrwgywoww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        expectedCube = '0owggw00wgro0ryoyo0oyg0rggwroyyorgowgwy0wwryrrr0gy0owy'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_040_ShouldRotateCubeInrDirection(self):
        cubeToRotate = 'GOYWGGGRGBWWWRYOYBBRWGBWOBRRBRROOGOOBYORWBYYRYGWGYBWOY'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        expectedCube = 'GOOWGBGRRWYBWRYBWOYRWBBWWBRRBRROOGOOBYORWGYYBYGYGYGWOG'
        self.assertEqual(rotatedCube, expectedCube)
    
    def test_rotate_050_ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'ooorbwrbrbbrbrywgggyogggwoywowrowooybrybyyggybrbwwwgyr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        expectedCube = 'ooorbwrbrbbrbrywggwggogyygoyowrowboyrygbyyggybrbwwwwro'
        self.assertEqual(rotatedCube, expectedCube)
    
    def test_rotate_060_ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'Za0A0aaaA9ZZZ9000zAz9za009aaA0ZAzZaAz9aZz99zzz9ZAZA90A'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        expectedCube = 'Za0A0aaaA9ZzZ9900a90aza9Az09A00AzAaAZZaZz99zzz9ZAZAz0Z'
        self.assertEqual(rotatedCube, expectedCube)
    
    def test_rotate_070_ShouldRotateCubeInLDirection(self):
        cubeToRotate = 'a09A0azZzzaZA99aaAAAazaZ0aZ90z0A009AZza9z9Az00A9ZZz9ZZ'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        expectedCube = 'Z0990aAZzzaZA99aaAAA9zaZ0a00099A0A0zZzaZz9az0aA9AZzzZZ'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_080_ShouldRotateCubeInlDirection(self):
        cubeToRotate = 'AaAZ0ZA0909Za9Az0aaAZZazAa09aa9A0zzZ0099zZzAz0zaAZ99zZ'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        expectedCube = '0aAA0Z90909Za9Az0aaAzZa9Aa0a0ZaAz99zA09ZzZAAz0zazZ9ZzZ'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_090_ShouldRotateCubeInUDirection(self):
        cubeToRotate = 'aa0z0zzaAZAz0990ZzA09za99A9ZAA0AazZaaZ00zaZZ9A9Z9ZAaz0'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        expectedCube = 'ZAzz0zzaAA090990ZzZAAza99A9aa00AazZaZ0aZzZ9a0A9Z9ZAaz0'
        self.assertEqual(rotatedCube, expectedCube)
    
    def test_rotate_100_ShouldRotateCubeInuDirection(self):
        cubeToRotate = '9aAa00ZAaz9aA9zZzaZ000aA990zZ0zAzZ09AZAAzazZa0a99Z9AZz'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        expectedCube = 'zZ0a00ZAa9aAA9zZzaz9a0aA990Z00zAzZ09AaaZzZAAz0a99Z9AZz'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_110_ShouldRotateCubeInFDirection_MissingDirection(self):
        cubeToRotate = '9Zzz0009aAAZA9Az0aa90aa0A99A90zAazAZZZ9azzza090AZZZazZ'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate()
        expectedCube = '0z990Za0zzAZa9A00aa90aa0A99A99zA0zAAZZ9azzZa0zAAZZZazZ'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_120_ShouldRotateCubeInFDirection_EmptyDirection(self):
        cubeToRotate = '00z000Az00ZzZ9AAAaaZ90aAZaZazZaA90zazaAAz9Az9Z9zaZZ999'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate("")
        expectedCube = 'A00z0000zAZzz9A9AaaZ90aAZaZazZaA90zzzaAAz9a9ZAZ0aZZ999'
        self.assertEqual(rotatedCube, expectedCube)
        
    def test_rotate_130_ShouldRotateCubeInMultiDirection(self):
        cubeToRotate = 'Zaaz0ZaaazZ9a99AZzZZzza09zAA00AAA0zA00a9zA9A9z9Z0Z9Za0'
        theCube = cube.Cube(cubeToRotate)
        rotationSequence = 'LRlllRuUlRBBbbLbbLlRllU'
        rotatedCube = theCube.rotate(rotationSequence)
        expectedCube = 'zZ990ZZazZzza99AA0A0zza09ZA0aaAAZ0zA990Aza9Aaa9a0ZzZ0Z'
        self.assertEqual(rotatedCube, expectedCube)
    
    def test_init_140_ShouldIntializeNominalCube(self):
        cubeInput = 'Zaaz0ZaaazZ9a99AZzZZzza09zAA00AAA0zA00a9zA9A9z9Z0Z9Za0'
        theCube = cube.Cube(cubeInput)
        self.assertEqual(cubeInput, theCube.get())
        
    def test_rotate_910_ShouldRaiseValueErrorExceptionOnInvalidDir(self):
        cubeToRotate = 'Zaaz0ZaaazZ9a99AZzZZzza09zAA00AAA0zA00a9zA9A9z9Z0Z9Za0'
        rotationSequence = 'LRlllRuUbbLbbLlRldlUDDD!@#$^%^&%*('
        theCube = cube.Cube(cubeToRotate)
        with self.assertRaises(ValueError):
            theCube.rotate(rotationSequence)
    
    def test_rotate_920_ShouldRaiseTypeErrorExceptionOnInvalidDirType(self):
        cubeToRotate = 'Zaaz0ZaaazZ9a99AZzZZzza09zAA00AAA0zA00a9zA9A9z9Z0Z9Za0'
        rotationSequence = 48
        theCube = cube.Cube(cubeToRotate)
        with self.assertRaises(TypeError):
            theCube.rotate(rotationSequence)
    
    def test_rotate_930_ShouldRaiseValueErrorExceptionOnMissingCubeInput(self):
        with self.assertRaisesRegex(ValueError, MISSING_CUBE_INPUT_EXCEPTION_MSG):
            cube.Cube()
            
    def test_rotate_940_ShouldRaiseValueErrorExceptionOnIncorrectCubeLength(self):
        cubeInput = 'rogwbbygywoorrwgyrwrbrorbgwwgyygbrwgrogoywoybbyogwbobyy'
        with self.assertRaisesRegex(ValueError, INVALID_CUBE_LENGTH_EXCEPTION_MSG):
            cube.Cube(cubeInput)
            
    def test_rotate_950_ShouldRaiseValueErrorExceptionOnCubeWithoutExactly6UniqueChars(self):
        cubeInput = 'bbbbbbbbbrrrrrrrrroooxooooogggggggggyyyyyyyyywwwwwwwww'
        with self.assertRaisesRegex(ValueError, INVALID_NUM_OF_UNIQ_CUBE_CHARS_EXCEPTION_MSG):
            cube.Cube(cubeInput)
            
    def test_rotate_960_ShouldRaiseValueErrorExceptionOnCubeWithCharNotInBound(self):
        cubeInput = 'bbbbbbbbb&&&&&&&&&!!!!!!!!!ggggggggg*********wwwwwwwww'
        with self.assertRaisesRegex(ValueError, CUBE_CHAR_OUT_OF_BOUND_EXCEPTION_MSG):
            cube.Cube(cubeInput)
    
    def test_rotate_970_ShouldRaiseValueErrorExceptionOnCubeWithNonUniqueCharInMiddlePositions(self):
        cubeInput = 'gbybbbgorroywrroroggryowybrbowggrbowwybywgogobywrwwyyg'
        with self.assertRaisesRegex(ValueError, CUBE_MIDDLE_POSITION_CHAR_NOT_UNIQUE_EXCEPTION_MSG):
            cube.Cube(cubeInput)
    
    def test_rotate_980_ShouldRaiseValueErrorExceptionOnCubeWithUnequalCharDistribution(self):
        cubeInput = 'bbbbbbbborrrrrrrroooooooooogggggggggyyyyyyyygwwwwwwwwg'
        with self.assertRaisesRegex(ValueError, UNEQUAL_CUBE_CHAR_DISTRIBUTION_EXCEPTION_MSG):
            cube.Cube(cubeInput)
            
    def test_rotate_980_ShouldRaiseTypeErrorExceptionInvalidCubeType(self):
        with self.assertRaisesRegex(ValueError, INVALID_TYPE_FOR_CUBE_EXCEPTION_MSG):
            cube.Cube(77)
    
            
        
    
        