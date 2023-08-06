from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.model.constants import *
class UpFaceSurfaceTest(TestCase):

#Analysis of upFaceSurface
#    A Module
#    Method: solveUpFaceSurface, given a cube object that has bottom layer and middle layer and upFaceCross solved solveUpFaceSurface performs rotations on the cube object such that the upFaceSurface is solved.
#
#    Analysis: upFaceSurface.solveUpSurface
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
    
    def test_solveUpFaceSurface_010_ShouldReturnEmptyStringForSolvedUpFace(self):
        encodedCube = 'rwwwwwwwwoyoooooooyoryyyyyywryrrrrrrgggggggggbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)
        
    def test_solveUpFaceSurface_020_ShouldSolveUpSurfaceOnCubeWithOneCornerSolvedWithUnsolvedCornersInRightOrientation(self):
        encodedCube = 'wygwwwwwwyrgoooooowwgyyyyyyoorrrrrrrygogggggrbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
    
    def test_solveUpFaceSurface_030_ShouldSolveUpCrossOnCubeWithOneCornerSolvedWithUnsolvedCornersNotInRightOrientation(self):
        encodedCube = 'ooywwwwwwgrwoooooogyryyyyyygwwrrrrrrygrgggggobbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
        
    def test_solveUpFaceSurface_040_ShouldSolveUpCrossOnCubeWithNoCornersSolved(self):
        encodedCube = 'wogwwwwwwoywoooooogwryyyyyygrgrrrrrrygrgggogybbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
    
    def test_solveUpFaceSurface_050_ShouldSolveUpCrossOnCubeWithNoCornersSolvedWithUnsolvedCornersNotInRightOrientation(self):
        encodedCube = 'gwrwwwwwwgrgoooooowogyyyyyyoywrrrrrrygogggrgybbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
        
    def test_solveUpFaceSurface_060_ShouldSolveUpCrossOnCubeWithTwoCornersSolvedWithUpFaceColorInFrontTopLeft(self):
        encodedCube = 'gwgwwwwwwrryoooooorywyyyyyyooyrrrrrrggggggogwbbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
        
    def test_solveUpFaceSurface_070_ShouldSolveUpCrossOnCubeWithTwoCornersSolvedWithUpFaceColorNotInFrontTopLeft(self):
        encodedCube = 'ooywwwwwwgwgoooooorryyyyyyyrywrrrrrrggwgggggobbbbbbbbb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveUpSurface(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isUpSurfaceSolved())
    
    def test_solveUpFaceCross_910_ShouldRaiseValueErrorExceptionOnCubeWithFlippedCorner(self):
        encodedCube = 'wbowwwwwwbyybbbbbbgwwyyyyyybggggggggooooooooyrrrrrrrrr'
        theCube = cube.Cube(encodedCube)
        with self.assertRaisesRegex(ValueError, CUBE_HAS_FLIPPED_CORNER_EXCEPTION_MSG):
            solveUpSurface(theCube)
    
        
    


