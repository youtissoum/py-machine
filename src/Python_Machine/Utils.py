from .Enums import Direction


def do_nothing():
    pass


def get_opposite_direction(direction: Direction):
    """
    Gets the opposite direction of a Direction object
    """
    direction_to_opposite = {
        Direction.RIGHT: Direction.LEFT,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.UP: Direction.DOWN
    }

    return direction_to_opposite[direction]


def get_loc_from_direction(x, y, direction: Direction, *, movement_amount: int = 1):
    """
    Gets a location in the direction going
    """
    new_x, new_y = x, y

    if direction == Direction.RIGHT:
        new_x += movement_amount
    elif direction == Direction.LEFT:
        new_x -= movement_amount
    elif direction == Direction.UP:
        new_y += movement_amount
    elif direction == Direction.DOWN:
        new_y -= movement_amount

    return new_x, new_y
