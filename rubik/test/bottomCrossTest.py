from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.model.constants import *
class BottomCrossTest(TestCase):
#Analysis of bottomCross
#    A Module
#    Method: solveBottomCross, given a cube object solveBottomCrossTest performs rotations on the cube object resulting in the bottom face has a cross
#
#    Analysis: bottomCross.solveBottomCrossTest
#        inputs: 
#            theCube
#            type: Cube Object
#                - rubiks cube represented as a string of 54 characters
#                - has method to rotate the cube faces in the front, right, back, left, and up, in clockwise or counter clockwise direction based on input direction
#                participation: mandatory
#            understanding: arrives unvalidated. If what is passed in is a cube we know it is a valid cube since cube is validated upon initialization. 
#
#         output:
#            side-effects: changes the state of the cube that is passed in.
#            nominal:
#                -a String containing the rotation performed to solve the bottom cross of the input cube: 
#            abnormal:
#                -raise a ValueError Exception when pass in a input that is not a cube  
    def test_solveBottomCross_010_ShouldReturnEmptyStringsForSolvedBottomCross(self):
        encodedCube = 'worybogboygrbrbyrogyorgoggwwrgyobborbrygyyogbwwbwwwrwy'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)
        
    def test_solveBottomCross_020_ShouldSolveBottomCrossOnCubeWithCompletedDaisyWithMatchedCenters(self):
        encodedCube = 'wbgybrgogorbbryrgwwgrogooyoyogbobyrrbwrwywowywgygwybrb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_030_ShouldSolveBottomCrossOnCubeWithCompleteCrossWithNonMatchingEdgesFixableByURotation(self):
        encodedCube = 'woryboborygrbrbgbogyorgoyrowrgyobggwbrygyyogbrwwwwwywb'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_040_ShouldSolveBottomCrossOnCubeWithCompletedDaisyWithMisMatchedCenters(self):
        encodedCube = 'orybbybgroogrrbwrwybgrgyrbgogbooyogrywrwywwwbyybowgwog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_050_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInRightMiddleLeft(self):
        encodedCube = 'bbogbrryywogwrbbrwybgrgyrbgogyooyogbywrwywrybwroowgwog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_060_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInDownTopMiddle(self):
        encodedCube = 'rgbybbyrorogyrbbrwybgrgyrbgogwoorogoywrwywbyybwwowgwog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_070_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInLeftMiddleRight(self):
        encodedCube = 'yyrrbgobbbogyrbyrwybgrgyrbgogboowogwywrwyworwbyrowgwog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_080_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInFrontTopMiddle(self):
        encodedCube = 'rwwobgwbbbogyrbyrwybgrgrrboogwyogyooywrwywbrogyrywgbog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_090_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInFrontMiddleRight(self):
        encodedCube = 'worbbwbgwbogrrborwybgrgrrbooggyoyyorywrwywogwyybywgbog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_011_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInFrontBottomMiddle(self):
        encodedCube = 'bygobbrwwybgrrrrygogyggyobbbrogogwybrwywywyorwogrwboow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_012_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheBottomMissingPetalInFrontMiddleLeft(self):
        encodedCube = 'wgbwbbrowrogyrbgrwybgrgrrboogoyoryobywrwywbyywgoywgbog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_013_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInBackMiddleLeft(self):
        encodedCube = 'broybgboggywrrowbgrbgwgyrbbogygoowyyywbwybrwwogrrwrooy'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_014_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInFrontMiddleRight(self):
        encodedCube = 'brrybwborgbworrwyggbgggyobbogygoowyyywrwyrrwyogbrwboow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_015_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInDownMiddleRight(self):
        encodedCube = 'brrybrboywrgbrygowwbgbgybbbogygoowyyywowygrwgogrrwwoor'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_016_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInRightMiddleRight(self):
        encodedCube = 'brybbbgywogwyrwgrrgbgogywbbogygorwyyywrwyorwbroorwgoob'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_017_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInRightBottomMiddle(self):
        encodedCube = 'brobbggybgyorrgrwwbbgogyrbbogygorwyyywywybrwwrowrwooog'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_018_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheRightMissingPetalInRightTopMiddle(self):
        encodedCube = 'brrbbogybwwrgrroygbbgggyobbogygorwyyywwwyorwgroyrwboow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_019_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInLeftMiddleLeft(self):
        encodedCube = 'bogrbyobgrbwororywogobggbgyyrowoyrgwgrgwywywwbryywbbor'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_021_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInRightMiddleRight(self):
        encodedCube = 'bogrbyobgrbrorwryyygbggbogowroooywgwrobwywywwbryywbgrg'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_022_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInDownBottomMiddle(self):
        encodedCube = 'bogrbyobgrbrororybbbogggygogroroyggwwowwywywwbryywbywr'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_023_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInBackTopMiddle(self):
        encodedCube = 'bogrbygbgrbbororywrwobgybgbgrogogwyowgywywywwyryrwboor'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_024_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInBackMiddleRight(self):
        encodedCube = 'bogrbygbgrbrororyobbrggwbyoyrogogwyobowwywywwyryrwbggw'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_025_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInBackMiddleLeft(self):
        encodedCube = 'bogrbygbgrbworgryyoybwggrbborooogryowggwywywwyryrwbwob'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_026_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheTopMissingPetalInBackBottomMiddle(self):
        encodedCube = 'bogrbygbgrbworgrygbgbygbowrwrooogbyoroowywywwyryrwbygw'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_027_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalInBackMiddleRight(self):
        encodedCube = 'broybywbgbogorrrygrbrggwobyyywgogoorbwwrywowybrygwbgow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_028_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalInFrontMiddleLeft(self):
        encodedCube = 'yrowbyrbgbogorrrygrbwggyobbroogogwyybwwgywgwybryrwboow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_029_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalDownMiddleLeft(self):
        encodedCube = 'brogbygbgbogorrrygrboggrobbwgryooygobwwyywwwyyrywwbrow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_031_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalLeftMiddleLeft(self):
        encodedCube = 'rrorbooyoboggrrgygrbwgggobyrrywoyrgwbwwbywgwyboyywbbow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_032_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalLeftMiddleRight(self):
        encodedCube = 'yrogbowyoboggrrgygrboggrobrwgryowyrrbwwyywbwyboybwbgow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_033_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalLeftTopMiddle(self):
        encodedCube = 'brobbogyoboggrrgygrbbggyobbrwrgorwyyywwgywwwyroyrwboow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
        
    def test_solveBottomCross_034_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithTheLeftMissingPetalLeftBottomMiddle(self):
        encodedCube = 'broybobyoboggrrgygrbgggbobbyywrogrwrrwwrywowyyoygwbwow'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    
    def test_solveBottomCross_035_ShouldSolveBottomCrossOnCubeWithIncompleteDaisyWithMultipleMissingPetals(self):
        encodedCube = 'oywybyywwrogrrgororoyrgwybybwwoogobrrgwgyygbbgbbrwwgob'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomCross(theCube)
        cubeToTestRotation = cube.Cube(encodedCube)
        cubeToTestRotation.rotate(actualRotations)
        self.assertTrue(cubeToTestRotation.areBottomEdgesSolved())
    