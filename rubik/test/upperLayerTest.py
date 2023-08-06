from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.constants import *

class UpperLayerTest(TestCase):

#Analysis of solveUpperLayer
#    A Module
#    Method: solveUpperLayer, given a cube object that has bottom layer and middle layer and up face surface solved and upper corners solved performs rotations on the cube object such that the cube is solved.
#
#    Analysis: uppperLayer.solveUpperLayer
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
#                -a String containing the rotation performed to solve the upper layer of the input cube: 
#            abnormal:
#                -raise a ValueError Exception when pass in a input that is not a cube  


    def test_solveUpperCorners_010_ShouldSolveUpperCornersOnCubeWithSolvedFaceInTheBack(self):
        encodedCube = 'owoooooooyoyyyyyyyrrrrrrrrrwywwwwwwwgggggggggbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpperLayerSolved())
        
    def test_solveUpperCorners_020_ShouldSolveUpperCornersOnCubeWithSolvedFaceInTheRight(self):
        encodedCube = 'rwrrrrrrryyyyyyyyyorooooooowowwwwwwwbbbbbbbbbggggggggg'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpperLayerSolved())
        
    def test_solveUpperCorners_030_ShouldSolveUpperCornersOnCubeWithNoFaceSolved(self):
        encodedCube = 'ybyyyyyyygwgggggggwgwwwwwwwbybbbbbbbooooooooorrrrrrrrr'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpperLayerSolved())
        
    def test_solveUpperCorners_040_ShouldSolveUpperCornersOnCubeWithFrontFaceSolved(self):
        encodedCube = 'wwwwwwwwwbgbbbbbbbybyyyyyyygygggggggooooooooorrrrrrrrr'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpperLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpperLayerSolved())
    
    def test_solveUpFaceCross_910_ShouldRaiseValueErrorExceptionOnCubeWithFlippedEdges(self):
        encodedCube = 'yyyyyyyyybgbbbbbbbwwwwwwwwwgbgggggggrrrrrrrrrooooooooo'
        theCube = cube.Cube(encodedCube)
        with self.assertRaisesRegex(ValueError, CUBE_HAS_FLIPPED_EDGE_EXCEPTION_MSG):
            solveUpperLayer(theCube)
        
        

    
