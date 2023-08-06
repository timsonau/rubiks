from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.model.constants import *
class BottomLayerTest(TestCase):
    
#Analysis of bottomLayer
#    A Module
#    Method: solveBottomLayer, given a cube object solveBottomLayer performs rotations on the cube with bottom cross solved such that the corner of bottom layer are correctly solved
#
#    Analysis: bottomLayer.solveBottomLayerTest
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
#                -a String containing the rotation performed to solve the bottom layer of the input cube: 
#            abnormal:
#                -raise a ValueError Exception when pass in a input that is not a cube  
    def test_solveBottomCross_010_ShouldReturnEmptyStringsForSolvedBottomLayer(self):
        encodedCube = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)
    
    def test_solveBottomCross_020_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceInTopFrontLeftCornerWithBottomColorFacingLeft(self):
        encodedCube = "oryoobyooogyybbbbbgrgorgrrrygwogyggbrboyyrgybrwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_030_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceInTopFrontLeftCornerWithBottomColorFacingFront(self):
        encodedCube = "wryyobroooggybbbbboyyorgrrrrrgoggggygoybyroybbwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_040_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceInTopFrontLeftCornerWithBottomColorFacingUp(self):
        encodedCube = "grybobbooogoybbbbbygrorgrrrgyoogrggryygoyrwybywwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_050_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceInTopFrontRightCornerWithBottomColorFacingRight(self):
        encodedCube = "oyoboyooywggrbbrbbyyoorgrrrbggogrgggybryyryobwwbwwwwww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_060_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceInTopFrontRightCornerWithBottomColorFacingFront(self):
        encodedCube = "oywboroobbyrgbbybbgryorgrrroggogrgggbyyyybyoowwrwwwwww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_070_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceInTopFrontRightCornerWithBottomColorFacingUp(self):
        encodedCube = "oybboboororyybbbbbrgborgrrryggogrgggorgyyyyowwwywwwwww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_080_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceInTopBackLeftCornerWithBottomColorFacingLeft(self):
        encodedCube = "oyyboboooogrybbbbbygrorrrrrwggygrygggobyyryobwwwwwwgww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
        
    def test_solveBottomCross_090_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceInTopBackLeftCornerWithBottomColorFacingBack(self):
        encodedCube = "oybboboooygbybbbbbrrworgrrggggrgrrggryyyyoyoowwwwwwyww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_011_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceInTopBackLeftCornerWithBottomColorFacingUp(self):
        encodedCube = "ygobobooobgrybbbbbyggororryryoygrgggwobryrgyywwwwwwrww"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_012_ShouldSolveBottomLayerOnCubeWithBottomBackRightCornerPieceInTopBackRightCornerWithBottomColorFacingRight(self):
        encodedCube = "yybbobooorrwybybbyroygrgbrrgggogrgggobbryyroywwwwwwwwo"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_013_ShouldSolveBottomLayerOnCubeWithBottomBackRightCornerPieceInTopBackRightCornerWithBottomColorFacingBack(self):
        encodedCube = "rybbobooorrbybrbbbwgggrgorrooyogrgggyyrbyygoywwwwwwwwy"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_014_ShouldSolveBottomLayerOnCubeWithBottomBackRightCornerPieceInTopBackRightCornerWithBottomColorFacingUp(self):
        encodedCube = "gybbobooorrrybbbbobgoorgyrrygrogrggggrwyyyyoywwwwwwwwb"
        theCube = cube.Cube(encodedCube) 
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_015_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftButTopFrontRightCorner(self):
        encodedCube = "ygwoobyoooryybbbbbogyorgrrrgrgogyggborbbyyrygrwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_016_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftCornerButSomewhereInUpperLayer(self):
        encodedCube = "ogyoobyoogrgybbbbbygworgrrroryogyggbgyryybbrorwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_017_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceNotInTopBackLeftCornerButSomewhereInTopLayer(self):
        encodedCube = 'yroboroooygrgbbbbbwrgoryrroygrogyyggrbgyyobygwwwwwwbww'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
        
    def test_solveBottomCross_018_ShouldSolveBottomLayerOnCubeWithBottomBackRightCornerPieceNotInTopBackRightCornerButSomewhereInTopLayer(self):
        encodedCube = 'ygwborooorrggbobbbyroyryyrrbboggygggyyroybgobwwwwwwwwr'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
        
    def test_solveBottomCross_019_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftCornerButBottomFrontLeftCornerInWrongOrientation(self):
        encodedCube = "ogybobgoobroybbbbbbyrorgrrrgggogrggwyoyryyyyrowwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_021_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftCornerButBottomFrontRightCorner(self):
        encodedCube = "byyooyoowrgyrbbgbbbgborgrrryrwogyggyorrbyyobggwowwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_022_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftCornerButBottomBackLeftCorner(self):
        encodedCube = "rooyobboobrwybrbbbgoyyrorrggryyggogrogrgybgbyywwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_023_ShouldSolveBottomLayerOnCubeWithBottomFrontLeftCornerPieceNotInTopFrontLeftCornerButBottomBackRightCorner(self):
        encodedCube = "rryooboooogwybrbbgroybrgorrbryogyggyrbbgyygybgwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_024_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceNotInTopFrontRightCornerButBottomFrontRightCornerInWrongOrientation(self):
        encodedCube = "ygrboroowyoogbbobbyryorgrrrobgogrgggbygyyyrybwwbwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_025_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceNotInTopFrontRightCornerButBottomBackRightCorner(self):
        encodedCube = "yygboyoogygrrbgyboybbrrgbrrwybogrgggrobbyyoorwwowwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
        
    def test_solveBottomCross_026_ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceNotInTopFrontRightCornerButBottomBackLeftCorner(self):
        encodedCube = "wybbogooyrrorbbobbbbyorgrrbrgrygrwgggyyoyygoywwgwwwoww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
        
    #need not test ShouldSolveBottomLayerOnCubeWithBottomFrontRightCornerPieceNotInTopFrontRightCornerButBottomFrontLeftCorner as left corner is already solved before right corner so bottom front right corner cannot be located there.
    
    def test_solveBottomCross_027_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceNotInTopBackLeftCornerButInBottomBackLeftCornerInWrongOrientation(self):
        encodedCube = "gybbobooorrgybbbbbyyborgrrgyoyrgrwggoorgyyogywwwwwwrww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_028_ShouldSolveBottomLayerOnCubeWithBottomBackLeftCornerPieceNotInTopBackLeftCornerButInBottomBackRightCorner(self):
        encodedCube = "gyrboboooygyybybbwrbborrrrowoyygryggroggyrogbwwwwwwbwg"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_029_ShouldSolveBottomLayerOnCubeWithBottomBackRightCornerPieceNotInTopBackRightCornerButInBottomBackRightCornerInWrongOreintation(self):
        encodedCube = "ogybobooorboybybbrygyorgwrrbryogrgggrygyyobrgwwwwwwwwb"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveBottomLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isBottomLayerSolved)
    
    def test_solveBottomCross_910_ShouldRaiseTypeErrorExceptionOnSolvingBottomLayerOnNotACube(self):
        self.assertRaises(TypeError, solveBottomLayer, 88)
        
    
        

    