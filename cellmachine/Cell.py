from cellmachine.Enums import Direction
from copy import deepcopy

from cellmachine.Utils import get_opposite_direction

class Grid():
    width = 0
    height = 0
    cells = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell

        return None

class Cell():
    CELL_ID = -1
    CELL_NAME = "EMPTY"

    x = 0
    y = 0
    direction = Direction.RIGHT
    tickNum = 0

    def move_in_direction(self, direction, grid: Grid, bias=-1):
        new_x = self.x
        new_y = self.y

        if self.CELL_NAME == "mover":
            if direction == self.direction:
                bias += 1
            elif direction == get_opposite_direction(self.direction):
                bias -= 1

        if direction == Direction.RIGHT:
            new_x += 1
        elif direction == Direction.LEFT:
            new_x -= 1
        elif direction == Direction.UP:
            new_y += 1
        elif direction == Direction.DOWN:
            new_y -= 1

        if new_x >= grid.width or new_y >= grid.height or new_x < 0 or new_y < 0:
            return ((False, grid, 0))

        cell_at_location: Cell = grid.get(new_x, new_y)
        if cell_at_location:
            if cell_at_location == self:
                exit()
            if cell_at_location.CELL_NAME == "immobile":
                return ((False, grid, bias))
            elif cell_at_location.CELL_NAME == "trash":
                grid.cells.remove(self)
                return ((True, grid, bias))
            elif cell_at_location.CELL_NAME == "enemy":
                grid.cells.remove(cell_at_location)
                grid.cells.remove(self)
                return ((True, grid, bias))
            elif cell_at_location.CELL_NAME == "slide":
                if cell_at_location.direction != direction and \
                    cell_at_location.direction != get_opposite_direction(direction):
                    return ((False, grid, bias))
            move_result, grid, bias = cell_at_location.move_in_direction(direction, grid, bias=bias)
            if not move_result:
                return ((False, grid, bias))

        if bias < 0:
            return ((False, grid, bias))

        self.x = new_x
        self.y = new_y

        return ((True, grid, bias))

    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction

class TickedCell(Cell):
    def step(self, grid: Grid):
        raise NotImplementedError("The stepping function has not been implemented")

class Generator(TickedCell):
    CELL_ID = 0
    CELL_NAME = "generator"

    def step(self, grid: Grid):
        cell_to_copy = None
        if self.direction == Direction.RIGHT:
            cell_to_copy = deepcopy(grid.get(self.x - 1, self.y))
            cell_position = (self.x + 1, self.y)
        elif self.direction == Direction.LEFT:
            cell_to_copy = deepcopy(grid.get(self.x + 1, self.y))
            cell_position = (self.x - 1, self.y)
        elif self.direction == Direction.DOWN:
            cell_to_copy = deepcopy(grid.get(self.x, self.y + 1))
            cell_position = (self.x, self.y - 1)
        elif self.direction == Direction.UP:
            cell_to_copy = deepcopy(grid.get(self.x, self.y - 1))
            cell_position = (self.x, self.y + 1)

        if not cell_to_copy:
            return grid

        if cell_position[0] > grid.width or cell_position[1] > grid.height:
            return grid

        cell_at_position: Cell = grid.get(cell_position[0], cell_position[1])
        if cell_at_position:
            if cell_at_position.CELL_NAME == "trash":
                return grid
            elif cell_at_position.CELL_NAME == "enemy":
                grid.cells.remove(cell_at_position)
                return grid
            elif cell_at_position.CELL_NAME == "slide":
                if cell_at_position.direction != self.direction and \
                    cell_at_position.direction != get_opposite_direction(self.direction):
                    return grid
            move_result, grid, bias = cell_at_position.move_in_direction(self.direction, grid, 0)
            if not move_result or bias < 0:
                return grid
        
        cell_to_copy.x = cell_position[0]
        cell_to_copy.y = cell_position[1]
        grid.cells.append(cell_to_copy)

        return grid

class C_Spinner(TickedCell):
    CELL_ID = 1
    CELL_NAME = "c_spinner"

    def step(self, grid: Grid):
        to_new_rotation = {
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.UP: Direction.RIGHT
        }

        left_cell: Cell = grid.get(self.x - 1, self.y)
        if left_cell:
            left_cell.direction = to_new_rotation[left_cell.direction]

        right_cell: Cell = grid.get(self.x + 1, self.y)
        if right_cell:
            right_cell.direction = to_new_rotation[right_cell.direction]

        down_cell: Cell = grid.get(self.x, self.y - 1)
        if down_cell:
            down_cell.direction = to_new_rotation[down_cell.direction]

        up_cell: Cell = grid.get(self.x, self.y + 1)
        if up_cell:
            up_cell.direction = to_new_rotation[up_cell.direction]

        return grid

class CC_Spinner(TickedCell):
    CELL_ID = 2
    CELL_NAME = "cc_spinner"

    def step(self, grid: Grid):
        to_new_rotation = {
            Direction.RIGHT: Direction.UP,
            Direction.DOWN: Direction.RIGHT,
            Direction.LEFT: Direction.DOWN,
            Direction.UP: Direction.LEFT
        }

        left_cell: Cell = grid.get(self.x - 1, self.y)
        if left_cell:
            left_cell.direction = to_new_rotation[left_cell.direction]

        right_cell: Cell = grid.get(self.x + 1, self.y)
        if right_cell:
            right_cell.direction = to_new_rotation[right_cell.direction]

        down_cell: Cell = grid.get(self.x, self.y - 1)
        if down_cell:
            down_cell.direction = to_new_rotation[down_cell.direction]

        up_cell: Cell = grid.get(self.x, self.y + 1)
        if up_cell:
            up_cell.direction = to_new_rotation[up_cell.direction]

        return grid

class Mover(TickedCell):
    CELL_ID = 3
    CELL_NAME = "mover"

    def step(self, grid: Grid):
        result, grid, bias = self.move_in_direction(self.direction, grid)
        return grid

class Slide(Cell):
    CELL_ID = 4
    CELL_NAME = "slide"

class Push(Cell):
    CELL_ID = 5
    CELL_NAME = "push"

class Immobile(Cell):
    CELL_ID = 6
    CELL_NAME = "immobile"

class Enemy(Cell):
    CELL_ID = 7
    CELL_NAME = "enemy"

class Trash(Cell):
    CELL_ID = 8
    CELL_NAME = "trash"