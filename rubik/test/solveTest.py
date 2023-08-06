from unittest import TestCase
from rubik.view.solve import solve
from rubik.model.constants import *
import rubik.model.cube as cube
import hashlib

class SolveTest(TestCase):
        
#Analysis of Solve
#    A Module
#    Method: solves the inputed cube and outputs the rotations performed on the cube
#    
#    Analysis: Cube.solve
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
#         output:
#            side-effects: no external side effects internal state change
#            nominal:
#                return Python dictionary containing: 
#                        1) 'solution': 'fLll.....uBbb' (rotations used to solve the rubik's cube)
#                        2) 'status': 'ok'
#                        3) 'integrity:': ''
#            abnormal:
#                b)Invalid Cube Input
#                    return Python dictionary containing: 
#                        1) {‘status’: ‘error: invalid cube’}
#                c)Invalid Key Input
#                    return Python dictionary containing: 
#                        1) {‘status’: ‘error: invalid key input’}
#
#     Happy path (actual bottom cross solving is done in bottomCross.Test)
#        test 010: Test solve on a nominal cube and check to see if the bottom cross is solved
#        test 020: Failing Acceptance Test 
#        test 030: Test solve on a nominal cube and check to see if the bottom layer is solved
#     Sad Path: (full BVA coverage of invalid cube tests are done in cubeTest, in this file we just need to make sure an invalid cube is handled)
#        test 910: Test invalid key, detect a key in param that is not 'cube'
#        test 920: Test invalid cube, too many chars
#        
    
    def test_solve_010_ShouldSolveNominalCubeAndCheckIfBottomCrossSolved(self):
        parms = {}
        parms['cube'] = 'byorbyrrywgbrrwrwgyogogoowroyryobygwybogywwbbggbowbgrw'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.areBottomEdgesSolved())
    
    def test_solve_020_FailedAcceptanceShouldSolveNominalCubeAndCheckIfBottomCrossSolved(self):
        parms = {}
        parms['cube'] = 'rwogbrggbwobwrgyyywgbwgogrgyrgwooyyworryybwbboyrbwoobr'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        expectedRotations = 'frbluFFRRBBLL'
        self.assertTrue(result['solution'].startswith(expectedRotations))
        
    def test_solve_030_ShouldSolveNominalCubeAndCheckIfBottomLayerSolved(self):
        parms = {}
        parms['cube'] = 'yorborgbbwgbgbgoywooworwgwrrroggybrybbwyyygwgrrywwoybo'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isBottomLayerSolved())
        
    def test_solve_040_ShouldSolveNominalCubeAndCheckIfMiddleLayerSolved(self):
        parms = {}
        parms['cube'] = 'rbgwbrgororrwrogywbyrygbobyyoyrogbrwbgwgyggoyowwywbowb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isMiddleLayerSolved())
        
    def test_solve_050_FailedAcceptanceShouldSolveNominalCubeMiddleLayerWithBottomLayerAlreadySolved(self):
        parms = {}
        parms['cube'] = 'orbogogggryryoyooogbogbobbbbrggrbrrryryyybygywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isMiddleLayerSolved())
    
    def test_solve_060_ShouldSolveNominalCubeAndCheckIfUpCrossSolved(self):
        parms = {}
        parms['cube'] = 'gobyrrggrwbbwwggoorgwrorygworybybooygoyygwowrrywybbbwb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isUpCrossSolved())
    
    def test_solve_070_ShouldSolveNominalCubeAndCheckIfUpSurfaceIsSolved(self):
        parms = {}
        parms['cube'] = 'bogwwgboborbrowworyyggyrgwrwwrbrbyyrogoogywyyybobbggrw'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isUpSurfaceSolved())
        
    def test_solve_080_ShouldCheckIntegrityKeyOfResult(self):
        parms = {}
        parms['cube'] = 'ogowyooyyybryryrbobgwbwrygggbwgorrwwrywogrgogbrbobwywb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        
        sha256Hash = '34ea5c671e766dd4152c32168a8a1dc7adc350cb37b473b804694a056d536389'
        self.assertEqual(len(result['integrity']), 8)
        self.assertTrue(result['integrity'] in sha256Hash)
        
    def test_solve_090_ShouldSolveNominalCubeAndCheckIfUpSurfaceIsSolved(self):
        parms = {}
        parms['cube'] = 'grgybbrorobwworbrobwrygowryworbrgbgbggowwyywywyyoybogg'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.areUpperCornersSolved())
        
    def test_solve_110_ShouldSolveNominalCubeAndCheckIfCubeIsSolved(self):
        parms = {}
        parms['cube'] = 'ogbwowyygrrbgbbwgbwbborywyrywwogryogorrbyggyyorrwwogbo'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertIn('solution', result)
        cubeToTestSolution = cube.Cube(parms['cube'])
        cubeToTestSolution.rotate(result['solution']) 
        self.assertTrue(cubeToTestSolution.isCubeSolved())
        
    def test_solve_910_ShouldReturnInvalidKeyStatus(self):
        parms = {}
        parms['cube'] = 'obygbywobgywgrwobrgoyggbyobbowrorrrbrbryyrgwoowywwywgg'
        parms['billevanstrio'] = 'someday_my_prince_will_come'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid key', result['status'])
    
    def test_solve_920_ShouldReturnInvalidCubeStatus(self):
        parms = {}
        parms['cube'] = 'obygbywobgywgrwobrgoyggbyobbowrorrrbrbryyrgwoowywwywggg'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertTrue(result['status'].startswith(INVALID_CUBE_STATUS_MSG))
    