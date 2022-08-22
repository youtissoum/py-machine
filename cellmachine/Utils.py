from cellmachine.Enums import Direction

def do_nothing():
    pass

def get_opposite_direction(direction: Direction):
    direction_to_opposite = {
        Direction.RIGHT: Direction.LEFT,
        Direction.LEFT: Direction.RIGHT,
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP
    }

    return direction_to_opposite[direction]