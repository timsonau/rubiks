from unittest import TestCase
import rubik.model.cube as cube
from rubik.controller.middleLayer import solveMiddleLayer
class MiddleLayerTest(TestCase):
#Analysis of middleLayer
#    A Module
#    Method: solveMiddleLayer, given a cube object solveMiddleLayer performs rotations on the cube with bottom layers solved such that the middle layers is solved.
#
#    Analysis: middleLayer.solveMiddleLayerTest
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
#                    

    def test_solveBottomLayer_010_ShouldReturnEmptyStringsForSolvedBottomLayer(self):
        encodedCube = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        expectedRotations = ""
        self.assertEqual(actualRotations, expectedRotations)
        
    def test_solveBottomCross_020_ShouldSolveMiddleLayerOnCubeWithCorrectFrontLeftEdgePieceInUpFrontEdgeInCorrectOrientation(self):
        encodedCube = "ogyrggggggyyoooooorybbbbbbbrbyrryrrryggyyobrowwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_030_ShouldSolveMiddleLayerOnCubeWithCorrectFrontLeftEdgePieceInUpLeftEdgeInCorrectOrientation(self):
        encodedCube = "yggygggggyyooooooobyobbbbbbyrrrrrrrrgoygybbyrwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_040_ShouldSolveMiddleLayerOnCubeWithCorrectFrontLeftEdgePieceNotInUpperLayerButInFrontLeftEdgeInWrongOrientation(self):
        encodedCube = "byrrggggggyoooooooyyybbbbbbbrorrgrrrrbgyyoygywwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
        
    def test_solveBottomCross_050_ShouldSolveMiddleLayerOnCubeWithCorrectFrontRightEdgePieceInUpFrontEdgeInCorrectOrientation(self):
        encodedCube = "ygyggrgggryoyooooobybbbbbbbrborrrrrrygyyyogogwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
        
    def test_solveBottomCross_060_ShouldSolveMiddleLayerOnCubeWithCorrectFrontRightEdgePieceInRightFrontEdgeInCorrectOrientation(self):
        encodedCube = "yybggbgggrooyooooobyybbbbbbryorrrrrrgrygyggoywwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_070_ShouldSolveMiddleLayerOnCubeWithCorrectFrontRightEdgePieceNotInUpperLayerButInFrontRightEdgeInWrongOrientation(self):
        encodedCube = "goyggogggryygooooobyobbbbbbbyyrrrrrrygrryboygwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
        
    def test_solveBottomCross_080_ShouldSolveMiddleLayerOnCubeWithCorrectBackLeftEdgePieceInUpBackEdgeInCorrectOrientation(self):
        encodedCube = "gbyggggggrorooooooybbbbgbbbyryyrrrrrorbyyyoygwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_090_ShouldSolveMiddleLayerOnCubeWithCorrectBackLeftEdgePieceInUpLeftEdgeInCorrectOrientation(self):
        encodedCube = "bbgggggggoorooooooggbbbybbbyryrrrrrroyybyyryywwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_011_ShouldSolveMiddleLayerOnCubeWithCorrectBackLeftEdgePieceNotInUpperLayerButInBackLeftEdgeInWrongOrientation(self):
        encodedCube = "boyggggggbbgooooooyygbbrbbborobrrrrrygryyyyyrwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_012_ShouldSolveMiddleLayerOnCubeWithCorrectBackRightEdgePieceInUpBackEdgeInCorrectOrientation(self):
        encodedCube = "ryyggggggoygooyoooobggbbbbbyobrrrrrrroyyybyrbwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())\
    
    def test_solveBottomCross_013_ShouldSolveMiddleLayerOnCubeWithCorrectBackRightEdgePieceInUpRightEdgeInCorrectOrientation(self):
        encodedCube = "oyyggggggoobooyooorygobbbbbyygrrrrrrrbyrybygbwwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    def test_solveBottomCross_014_ShouldSolveMiddleLayerOnCubeWithCorrectBackRightEdgePieceNotInUpperLayerButInBackRightEdgeInWrongOrientation(self):
        encodedCube = "yooggggggbbboobooorgyobbbbbgygrrrrrroyyryyryywwwwwwwww"
        theCube = cube.Cube(encodedCube)
        actualRotations = solveMiddleLayer(theCube)
        cubeToTestRotations = cube.Cube(encodedCube)
        cubeToTestRotations.rotate(actualRotations)
        self.assertTrue(cubeToTestRotations.isMiddleLayerSolved())
    
    