from enum import IntEnum

class CellTypes(IntEnum):
    GENERATOR = 1,
    ROTATOR_CW = 2
    ROTATOR_CCW = 3
    MOVER = 4
    SLIDE = 5
    PUSH = 6
    IMMOBILE = 7
    ENEMY = 8
    TRASH = 9

class Direction(IntEnum):
    RIGHT = 0,
    DOWN = 1,
    LEFT = 2,
    UP = 3