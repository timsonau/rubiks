'''
Constants used across the microservice 
'''

#-----------------------------------
#  Mapping of cube element positions to mnemonic names
#  Each mnemonic is a three-character pattern, frc, where
#       f indicates the face and is one of F, R, B, L, U, D
#       r indicates the row and is one of T, M, B (for top, middle, bottom, respectively)
#       c indicates the column and is one of L, M, R (for left, middle, right, repectively)
#  The regex for the pattern is r'[FRBLUD][TMB][LMR]'
#
# Front face
FTL = 0
FTM = 1
FTR = 2
FML = 3
FMM = 4
FMR = 5
FBL = 6
FBM = 7
FBR = 8

# Right face
RTL = 9
RTM = 10
RTR = 11
RML = 12
RMM = 13
RMR = 14
RBL = 15
RBM = 16
RBR = 17

# Back face
BTL = 18
BTM = 19
BTR = 20
BML = 21
BMM = 22
BMR = 23
BBL = 24
BBM = 25
BBR = 26

# Left face
LTL = 27
LTM = 28
LTR = 29
LML = 30
LMM = 31
LMR = 32
LBL = 33
LBM = 34
LBR = 35

# Up face
UTL = 36
UTM = 37
UTR = 38
UML = 39
UMM = 40
UMR = 41
UBL = 42
UBM = 43
UBR = 44

#Down face
DTL = 45
DTM = 46
DTR = 47
DML = 48
DMM = 49
DMR = 50
DBL = 51
DBM = 52
DBR = 53


UP_FACE_SURFACE_ROTATION = 'RUrURUUr'
UP_FACE_CROSS_ROTATION = 'FURurf'
LEFT_TRIGGER_ROTATION = 'luLU'
RIGHT_TRIGGER_ROTATION = 'RUru'
FRONT_180_ROTATION = 'FF'
ALL_SIDE_180_ROTATION = 'FFRRBBLL'
UPPER_CORNER_ROTATION = 'lURuLUr' + UP_FACE_SURFACE_ROTATION
UPPER_LAYER_ROTATION = 'FFUrLFFlRUFF'

NUM_PIXELS_CUBE = 54
NUM_SIDES_CUBE = 6
NUM_PIXELS_PER_SIDE_CUBE = 9
OFFSET_CENTER_PIECE_CUBE = 4

MISSING_CUBE_INPUT_EXCEPTION_MSG = 'missing cube'
INVALID_CUBE_LENGTH_EXCEPTION_MSG = 'cube length must be 54 character'
INVALID_NUM_OF_UNIQ_CUBE_CHARS_EXCEPTION_MSG = 'number of unique characters not equal to 6'
CUBE_CHAR_OUT_OF_BOUND_EXCEPTION_MSG = 'out of bound character in sequence'
CUBE_MIDDLE_POSITION_CHAR_NOT_UNIQUE_EXCEPTION_MSG = 'center characters - 5th, 14th, 23rd, 32nd, 41st, 50th - not unique'
UNEQUAL_CUBE_CHAR_DISTRIBUTION_EXCEPTION_MSG = 'unequal distribution of characters. Each unique character must have count of 9'
CUBE_HAS_FLIPPED_EDGE_EXCEPTION_MSG = 'cube has flipped edge piece, invalid scramble'
CUBE_HAS_FLIPPED_CORNER_EXCEPTION_MSG = 'cube has flipped corner piece, invalid scramble'

INVALID_TYPE_FOR_CUBE_EXCEPTION_MSG = 'Cube is not a string'
INVALID_TYPE_FOR_DIRECTIONS_EXCEPTION_MSG = 'Directions is not a string'
INVALID_ROTATION_IN_DIRECTION_EXCEPTION_MSG = 'Directions contain invalid rotation value. Rotation value can only be from this set [F,f,R,r,B,b,L,l,U,u]'
INVALID_TYPE_NOT_A_CUBE_EXCEPTION_MSG = 'Input is not a cube'

INVALID_KEY_STATUS_MSG = 'error: invalid key'
INVALID_CUBE_STATUS_MSG = 'error: invalid cube, '
INVALID_DIRECTION_STATUS_MSG = 'error: invalid direction, '

