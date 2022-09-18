from .Enums import Direction

def do_nothing():
    pass

def get_opposite_direction(direction: Direction):
    direction_to_opposite = {
        Direction.RIGHT: Direction.LEFT,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.UP: Direction.DOWN
    }

    return direction_to_opposite[direction]

def get_loc_from_direction(x, y, direction: Direction):
    new_x, new_y = x, y

    if direction == Direction.RIGHT:
        new_x += 1
    elif direction == Direction.LEFT:
        new_x -= 1
    elif direction == Direction.UP:
        new_y += 1
    elif direction == Direction.DOWN:
        new_y -= 1

    return new_x, new_y