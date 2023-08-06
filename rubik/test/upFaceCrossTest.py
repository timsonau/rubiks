from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.upFaceCross import solveUpCross
from rubik.model.constants import *

class UpFaceCrossTest(TestCase):

#Analysis of
#    A Module upFraceCross
#    Method: solveUpFaceCross, given a cube object that has bottom layer and middle layer solved solveUpFaceCross performs rotations on the cube object such that the upFaceCross is solved.
#
#    Analysis: bottomCross.solveUpFaceCross
#        inputs: 
#            theCube
#            type: Cube Object
#                - rubiks cube represented as a string of 54 characters
#                - has method to rotate the cube faces in the front, right, back, left, and up, in clockwise or counter clockwise direction based on input direction
#                participation: mandatory
#            understanding: 
#                -arrives validated. If what is passed in is a cube we know it is a valid cube since cube is validated upon initialization.
#                -cube arrives with bottom cross solved
#
#         output:
#            side-effects: none
#            nominal:
#                -a String containing the rotation performed to solve the middle layer of the input cube: 
#            abnormal:
#                -raise a ValueError Exception when pass in a input that is not a cube  

    def test_solveUpFaceCross_010_ShouldReturnEmptyStringForSolvedUpFaceCross(self):
        encodedCube = 'gwgrrrrrroogwwwwwwrrooooooogyryyyyyywgwgggygybbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)

    def test_solveUpFaceCross_020_ShouldSolveUpCrossOnCubeWithLTrominoInUpperLeftPosition(self):
        encodedCube = 'rgyrrrrrrggrwwwwwwwogoooooowyyyyyyyyoggggwgrobbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpCrossSolved())
    
    def test_solveUpFaceCross_030_ShouldSolveUpCrossOnCubeWithLTrominoNotInUpperLeftPosition(self):
        encodedCube = 'ggrrrrrrrwogwwwwwwwyyoooooorgyyyyyyyggorggowgbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpCrossSolved())
        
    def test_solveUpFaceCross_040_ShouldSolveUpCrossOnCubeWithITrominoHorizontallyAlgined(self):
        encodedCube = 'wggrrrrrryoywwwwwwggwoooooogrgyyyyyyryogggowrbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpCrossSolved())
        
    def test_solveUpFaceCross_050_ShouldSolveUpCrossOnCubeWithITrominoNotHorizontallyAlgined(self):
        encodedCube = 'gogrrrrrrrgowwwwwwyryoooooorgoyyyyyygggwgywgwbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpCrossSolved())
    
    def test_solveUpFaceCross_060_ShouldSolveUpCrossOnCubeWithNoUsablePattern(self):
        encodedCube = 'ogrrrrrrrwgowwwwwwggyoooooorggyyyyyygwwogryygbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpCross(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpCrossSolved())
    
    def test_solveUpFaceCross_910_ShouldRaiseValueErrorExceptionOnCubeWithFlippedEdge(self):
        encodedCube = 'yryggggggryryyyyyywbwbbbbbbrgrwwwwwwbrgrrrbwgooooooooo'
        theCube = cube.Cube(encodedCube)
        with self.assertRaisesRegex(ValueError, CUBE_HAS_FLIPPED_EDGE_EXCEPTION_MSG):
            solveUpCross(theCube)
        
        
        
