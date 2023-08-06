from rubik.model.constants import *
import string
class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube=None):
        #validate the cube here
        self._cube = self._validateCube(encodedCube) 

    def rotate(self, directions='F'):
        directions = self._validateDirections(directions)
        
        if(len(directions) == 0):
            directions = 'F'
            
        for d in directions:
            match d:
                case 'F':
                    self._rotate_F()
                case 'f':
                    self._rotate_f()
                case 'R':
                    self._rotate_R()
                case 'r':
                    self._rotate_r()
                case 'B':
                    self._rotate_B()
                case 'b':
                    self._rotate_b()
                case 'L':
                    self._rotate_L()
                case 'l':
                    self._rotate_l()
                case 'U':
                    self._rotate_U()
                case 'u':
                    self._rotate_u()
        return self._cube
        
    def get(self):
        return self._cube
    
    def withRespectToLeft(self, rotations):
        translation = {'F': 'L', 'f': 'l', 'L': 'B', 'l': 'b', 'R': 'F', 'r': 'f', 'B': 'R', 'b': 'r'}
        translatedRotations = ''
        for r in rotations:
            translatedRotations += translation.get(r, r)
        return translatedRotations
    
    def withRespectToRight(self, rotations):
        translation = {'F': 'R', 'f': 'r', 'L': 'F', 'l': 'f', 'R': 'B', 'r': 'b', 'B': 'L', 'b': 'l'}
        translatedRotations = ''
        for r in rotations:
            translatedRotations += translation.get(r, r)
        return translatedRotations
    
    def withRespectToBack(self, rotations):
        translation = {'F': 'B', 'f': 'b', 'L': 'R', 'l': 'r', 'R': 'L', 'r': 'l', 'B': 'F', 'b': 'f'}
        translatedRotations = ''
        for r in rotations:
            translatedRotations += translation.get(r, r)
        return translatedRotations

    def isBottomLayerSolved(self):
        return self.areBottomEdgesSolved() and self.areBottomCornersSolved()
    
    def isMiddleLayerSolved(self):
        return self.isBottomLayerSolved() and self.areMiddleEdgesSolved()
    
    def isUpperLayerSolved(self):
        return self.areUpperEdgesSolved() and self.areUpperCornersSolved()
    
    def isCubeSolved(self):
        return self.isBottomLayerSolved() and self.isMiddleLayerSolved() and self.isUpperLayerSolved()
    
    def areUpperEdgesSolved(self):
        frontFace = self._cube[FMM]
        leftFace = self._cube[LMM]
        rightFace = self._cube[RMM]
        backFace = self._cube[BMM]
        return self.isUpCrossSolved() and self._cube[FTM] == frontFace and self._cube[LTM] == leftFace and self._cube[RTM] == rightFace and self._cube[BTM] == backFace
        
    def isUpCrossSolved(self):
        upFace = self._cube[UMM]
        return (self._cube[UTM] == upFace) and (self._cube[UML] == upFace) and (self._cube[UBM] == upFace) and (self._cube[UMR] == upFace)
    
    def isUpLTrominoSolved(self):
        upFace = self._cube[UMM]
        return (self._cube[UTM] == upFace) and (self._cube[UML] == upFace)
    
    def isUpITrominoSolved(self):
        upFace = self._cube[UMM]
        return (self._cube[UML] == upFace) and (self._cube[UMR] == upFace)
    
    def isUpSurfaceSolved(self):
        return self.isUpCrossSolved() and self.areUpSurfaceCornersSolved()
    
    def areUpSurfaceCornersSolved(self):
        upFace = self._cube[UMM]
        return (self._cube[UTL] == upFace) and (self._cube[UTR] == upFace) and (self._cube[UBL] == upFace) and (self._cube[UBR] == upFace)
    
    def areBottomEdgesSolved(self):
        cubeList = self._cube
        frontFace = cubeList[FMM]
        rightFace = cubeList[RMM]
        backFace = cubeList[BMM]
        leftFace = cubeList[LMM]
    
        downFace = cubeList[DMM]
        isFrontEdgeCorrect = (cubeList[FBM] == frontFace) and (cubeList[DTM] == downFace)
        isRightEdgeCorrect = (cubeList[RBM] == rightFace) and (cubeList[DMR] == downFace)
        isBackEdgeCorrect = (cubeList[BBM] == backFace) and (cubeList[DBM] == downFace) 
        isLeftEdgeCorrect = (cubeList[LBM] == leftFace) and (cubeList[DML] == downFace)
        
        return isFrontEdgeCorrect and isRightEdgeCorrect and isBackEdgeCorrect and isLeftEdgeCorrect
    
    def isBottomFrontLeftCornerSolved(self):
        cubeList = self._cube
        frontFace = cubeList[FMM]
        leftFace = cubeList[LMM]
        downFace = cubeList[DMM]
        return (cubeList[DTL] == downFace) and (cubeList[LBR] == leftFace) and (cubeList[FBL] == frontFace)
    
    def isBottomFrontRightCornerSolved(self):
        cubeList = self._cube
        frontFace = cubeList[FMM]
        rightFace = cubeList[RMM]
        downFace = cubeList[DMM]
        return (cubeList[DTR] == downFace) and (cubeList[RBL] == rightFace) and (cubeList[FBR] == frontFace)
    
    def isBottomBackLeftCornerSolved(self):
        cubeList = self._cube
        downFace = cubeList[DMM]
        backFace = cubeList[BMM]
        leftFace = cubeList[LMM]
        return (cubeList[DBL] == downFace) and (cubeList[LBL] == leftFace) and (cubeList[BBR] == backFace)
    
    def isBottomBackRightCornerSolved(self):
        cubeList = self._cube
        downFace = cubeList[DMM]
        backFace = cubeList[BMM]
        rightFace = cubeList[RMM]
        return (cubeList[DBR] == downFace) and (cubeList[RBR] == rightFace) and (cubeList[BBL] == backFace)
    
    def areBottomCornersSolved(self):
        return self.isBottomFrontLeftCornerSolved() and self.isBottomFrontRightCornerSolved() and self.isBottomBackLeftCornerSolved() and self.isBottomBackRightCornerSolved()
    
    def areMiddleEdgesSolved(self):
        return self.isMiddleFrontLeftEdgeSolved() and self.isMiddleFrontRightEdgeSolved() and self.isMiddleBackLeftEdgeSolved() and self.isMiddleBackRightEdgeSolved()
    
    def areUpperCornersSolved(self):
        return self.isUpperFrontLeftCornerSolved() and self.isUpperFrontRightCornerSolved() and self.isUpperBackLeftCornerSolved() and self.isUpperBackRightCornerSolved()
    
    def isUpperFrontLeftCornerSolved(self):
        cubeList = self._cube
        upFace = cubeList[UMM]
        frontFace = cubeList[FMM]
        leftFace = cubeList[LMM]
        return (cubeList[UBL] == upFace) and (cubeList[FTL] == frontFace) and (cubeList[LTR] == leftFace)
 
    def isUpperFrontRightCornerSolved(self):
        cubeList = self._cube
        upFace = cubeList[UMM]
        frontFace = cubeList[FMM]
        rightFace = cubeList[RMM]
        return (cubeList[UBR] == upFace) and (cubeList[FTR] == frontFace) and (cubeList[RTL] == rightFace)
    
    def isUpperBackLeftCornerSolved(self):
        cubeList = self._cube
        upFace = cubeList[UMM]
        backFace = cubeList[BMM]
        leftFace = cubeList[LMM]
        return (cubeList[UTL] == upFace) and (cubeList[BTR] == backFace) and (cubeList[LTL] == leftFace)
    
    def isUpperBackRightCornerSolved(self):
        cubeList = self._cube
        upFace = cubeList[UMM]
        backFace = cubeList[BMM]
        rightFace = cubeList[RMM]
        return (cubeList[UTR] == upFace) and (cubeList[BTL] == backFace) and (cubeList[RTR] == rightFace)

    def isMiddleFrontLeftEdgeSolved(self):
        cubeList = self._cube
        frontFace = cubeList[FMM]
        leftFace = cubeList[LMM]
        return (cubeList[FML] == frontFace) and (cubeList[LMR] == leftFace)
    
    def isMiddleFrontRightEdgeSolved(self):
        cubeList = self._cube
        frontFace = cubeList[FMM]
        rightFace = cubeList[RMM]
        return (cubeList[FMR] == frontFace) and (cubeList[RML] == rightFace)
    
    def isMiddleBackLeftEdgeSolved(self):
        cubeList = self._cube
        backFace = cubeList[BMM]
        leftFace = cubeList[LMM]
        return (cubeList[BMR] == backFace) and (cubeList[LML] == leftFace)
    
    def isMiddleBackRightEdgeSolved(self):
        cubeList = self._cube
        backFace = cubeList[BMM]
        rightFace = cubeList[RMM]
        return (cubeList[BML] == backFace) and (cubeList[RMR] == rightFace)

    def _validateDirections(self, directions):
        if (directions == None):
            return 'F'
        self._validateDirectionsType(directions)
        self._validateDirectionsRotationValues(directions)
        return directions
    
    def _validateDirectionsType(self, directions):
        if (not (isinstance(directions, str))):
            raise TypeError(INVALID_TYPE_FOR_DIRECTIONS_EXCEPTION_MSG)
    
    def _validateDirectionsRotationValues(self, directions):
        validDirections = set("FfRrBbLlUu")
        if (not (set(directions).issubset(validDirections))):
            raise ValueError(INVALID_ROTATION_IN_DIRECTION_EXCEPTION_MSG)
        
    def _rotate_F(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the front face
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
        # rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
        # rotate right to down
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
        # rotate bottom to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
        # rotate left to up
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_f(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the front face
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FBR] = cubeList[FBL]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FTR] = cubeList[FBR]
        # rotate up to left
        rotatedCubeList[LBR] = cubeList[UBL]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LTR] = cubeList[UBR]
        # rotate right to up
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
        # rotate bottom to right
        rotatedCubeList[RBL] = cubeList[DTL]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RTL] = cubeList[DTR]
        # rotate left to down
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        self._cube = "".join(rotatedCubeList)
    
    def _rotate_R(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the right face
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
        # rotate up to back
        rotatedCubeList[BBL] = cubeList[UTR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BTL] = cubeList[UBR]
        # rotate back to down
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
        # rotate down to front
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
        # rotate front to up
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_r(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the right face
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RBR] = cubeList[RBL]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RTR] = cubeList[RBR]
        # rotate up to front
        rotatedCubeList[FTR] = cubeList[UTR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FBR] = cubeList[UBR]
        # rotate front to down
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
        # rotate down to back
        rotatedCubeList[BBL] = cubeList[DTR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BTL] = cubeList[DBR]
        # rotate back to up
        rotatedCubeList[UBR] = cubeList[BTL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UTR] = cubeList[BBL]
        self._cube = "".join(rotatedCubeList)
        
    def _rotate_B(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the back face
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
        # rotate up to left
        rotatedCubeList[LBL] = cubeList[UTL]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LTL] = cubeList[UTR]
        # rotate right to up
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
        # rotate bottom to right
        rotatedCubeList[RBR] = cubeList[DBL]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RTR] = cubeList[DBR]
        # rotate left to down
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]
        self._cube = "".join(rotatedCubeList)
    
    def _rotate_b(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the back face
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BBL]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BTR] = cubeList[BBR]
        # rotate up to right
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
        # rotate right to down
        rotatedCubeList[DBR] = cubeList[RTR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBL] = cubeList[RBR]
        # rotate down to right
        rotatedCubeList[LTL] = cubeList[DBL]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LBL] = cubeList[DBR]
        # rotate left to up
        rotatedCubeList[UTR] = cubeList[LTL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTL] = cubeList[LBL]
        self._cube = "".join(rotatedCubeList)
    
    def _rotate_L(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the left face
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
        # rotate up to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
        # rotate front to down
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
        # rotate down to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
        # rotate back to up
        rotatedCubeList[UBL] = cubeList[BTR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UTL] = cubeList[BBR]
        self._cube = "".join(rotatedCubeList)
        
    def _rotate_l(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the left face
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LBR] = cubeList[LBL]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LTR] = cubeList[LBR]
        # rotate up to back
        rotatedCubeList[BBR] = cubeList[UTL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BTR] = cubeList[UBL]
        # rotate back to down
        rotatedCubeList[DBL] = cubeList[BTR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DTL] = cubeList[BBR]
        # rotate down to front
        rotatedCubeList[FTL] = cubeList[DTL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FBL] = cubeList[DBL]
        # rotate front to up
        rotatedCubeList[UTL] = cubeList[FTL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UBL] = cubeList[FBL]
        self._cube = "".join(rotatedCubeList)   
    
    def _rotate_U(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the up face
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
        # rotate front to left
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
        # rotate left to back
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
        # rotate back to right
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
        # rotate right to front
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
        self._cube = "".join(rotatedCubeList)
    
    def _rotate_u(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        # rotate the up face
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UBR] = cubeList[UBL]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UTR] = cubeList[UBR]
        # rotate front to right
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
        # rotate right to back
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
        # rotate back to left
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
        # rotate left to front
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
        self._cube = "".join(rotatedCubeList)

    def _validateCube(self, cube=None):
        self._validateCubeExistence(cube)
        self._validateCubeType(cube)
        self._validateCubeLength(cube)
        self._validateCubeCharValue(cube)
        self._validateCubeUniqueChars(cube)
        self._validateCubeCenterPieces(cube)
        self._validateCubeCharDistribution(cube)
        return cube
    
    def _validateCubeExistence(self, cube=None):
        if (cube == None):
            raise ValueError(MISSING_CUBE_INPUT_EXCEPTION_MSG)
        
    def _validateCubeType(self, cube):
        if (not (isinstance(cube, str))):
            raise ValueError(INVALID_TYPE_FOR_CUBE_EXCEPTION_MSG)
            
    def _validateCubeLength(self, cube):
        if (len(cube) != NUM_PIXELS_CUBE):
            raise ValueError(INVALID_CUBE_LENGTH_EXCEPTION_MSG)
    
    def _validateCubeUniqueChars(self, cube):
        cubeUniqChars = set(cube)
        if (len(cubeUniqChars) != NUM_SIDES_CUBE):
            raise ValueError(INVALID_NUM_OF_UNIQ_CUBE_CHARS_EXCEPTION_MSG)
        
    def _validateCubeCharValue(self, cube):
        cubeUniqChars = set(cube)
        validChars = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        if (not(cubeUniqChars <= validChars)):
            raise ValueError(CUBE_CHAR_OUT_OF_BOUND_EXCEPTION_MSG)
    
    def _validateCubeCenterPieces(self, cube):
        if(len(set(cube[OFFSET_CENTER_PIECE_CUBE::NUM_PIXELS_PER_SIDE_CUBE])) < NUM_SIDES_CUBE):
            raise ValueError(CUBE_MIDDLE_POSITION_CHAR_NOT_UNIQUE_EXCEPTION_MSG)
        
    def _validateCubeCharDistribution(self, cube):
        cubeUniqChars = set(cube)
        for c in cubeUniqChars:
            if (cube.count(c) != NUM_PIXELS_PER_SIDE_CUBE):
                raise ValueError(UNEQUAL_CUBE_CHAR_DISTRIBUTION_EXCEPTION_MSG)
        