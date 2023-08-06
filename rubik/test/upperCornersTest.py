from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.upperCorners import solveUpperCorners
from rubik.model.constants import *

class UpperCornerTest(TestCase):

#Analysis of upperCorners
#    A Module
#    Method: solveUpperCorners, given a cube object that has bottom layer and middle layer and up face surface solved solveUpperCorners performs rotations on the cube object such that the upper corners are solved.
#
#    Analysis: uppperCorners.solveUpperCorners
#        inputs: 
#            theCube
#            type: Cube Object
#                - rubiks cube represented as a string of 54 characters
#                - has method to rotate the cube faces in the front, right, back, left, and up, in clockwise or counter clockwise direction based on input direction
#                participation: mandatory
#            understanding: 
#                -arrives validated. If what is passed in is a cube we know it is a valid cube since cube is validated upon initialization.
#                -cube arrives with bottom layer and middle layer and up face surface solved
#
#         output:
#            side-effects: none
#            nominal:
#                -a String containing the rotation performed to solve the upper corners of the input cube: 
#            abnormal:
#                -raise a ValueError Exception when pass in a input that is not a cube  

#
    def test_solveUpFaceSurface_010_ShouldReturnEmptyStringForSolvedUpperCorners(self):
        encodedCube = 'gygggggggybyyyyyyybgbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)
        
    def test_solveUpperCorners_020_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersOnLeftSide(self):
        encodedCube = 'gbyggggggbygyyyyyyygbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
        
    def test_solveUpperCorners_030_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersOnFrontSide(self):
        encodedCube = 'ooooooooobbrbbbbbbggbrrrrrrrrgggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
        
    def test_solveUpperCorners_040_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersOnRightSide(self):
        encodedCube = 'rrgggggggooooooooobbrbbbbbbggbrrrrrryyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
    
    def test_solveUpperCorners_050_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersOnBackSide(self):
        encodedCube = 'bygwwwwwwwgbbbbbbbybyyyyyyygwwggggggooooooooorrrrrrrrr'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
        
    def test_solveUpperCorners_060_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersInSameSideButNotInCorrectSide(self):
        encodedCube = 'gbroooooobrgggggggrgbrrrrrrooobbbbbbwwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
        
    def test_solveUpperCorners_070_ShouldSolveUpperCornersOnCubeWithMatchingUpperCornersDiagonally(self):
        encodedCube = 'gobbbbbbbobroooooobggggggggrrorrrrrrwwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperCorners(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.areUpperCornersSolved())
    
    
    