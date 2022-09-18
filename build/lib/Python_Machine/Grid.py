class Grid():
    width = 0
    height = 0
    cells = []  # type: ignore

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.cells = []

    def get(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell

        return None
