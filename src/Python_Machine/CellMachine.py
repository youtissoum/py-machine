from copy import deepcopy
import math
import operator
import random
from .base74 import b74_decode, b74_encode, b74_key  # noqa: F401
from PIL import Image
from .Enums import Direction
from .Cell import Cell, TickedCell, Generator, C_Spinner, CC_Spinner, Mover, Slide, Push, Immobile, Enemy, Trash
from .Grid import Grid

SUBTICKING_ORDER: list[type[TickedCell]] = [Generator, C_Spinner, CC_Spinner, Mover]
SUBTICKING_DIRECTION = (Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN)
CELLS: list[type[Cell]] = [Generator, C_Spinner, CC_Spinner, Mover, Slide, Push, Immobile, Enemy, Trash]

DEFAULT_TEXTURE_PATH = __file__.removesuffix("CellMachine.py").replace("\\", "/") + "textures/"


class CellMachine():
    """
    A class that can be used like a cell machine level
    """
    cells: Grid = Grid(1, 1)

    tickAmount = 0

    TEXTURE_PATH = __file__.removesuffix("CellMachine.py").replace("\\", "/") + "textures/"
    TEXTURE_SIZE = 16

    bg = Image.open(f'{TEXTURE_PATH}background.png')
    generator = Image.open(f"{TEXTURE_PATH}generator.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    C_spinner = Image.open(f"{TEXTURE_PATH}C_spinner.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    CC_spinner = Image.open(f"{TEXTURE_PATH}CC_spinner.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    mover = Image.open(f"{TEXTURE_PATH}mover.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    slide = Image.open(f"{TEXTURE_PATH}slide.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    push = Image.open(f"{TEXTURE_PATH}push.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    immobile = Image.open(f"{TEXTURE_PATH}immobile.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    enemy = Image.open(f"{TEXTURE_PATH}enemy.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    trash = Image.open(f"{TEXTURE_PATH}trash.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    placeable = Image.open(f"{TEXTURE_PATH}placeable.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    # SETUP
    def __init__(self, preview_scale=2) -> None:
        self.width = 1
        self.height = 1
        self.cells = Grid(1, 1)
        self.placeables: list[tuple[int, int]] = []
        self.name = ""
        self.tickAmount = 0

        self.SCALE = preview_scale

        self.resetCells = Grid(1, 1)

        self.change_textures()

    def change_textures(self, TEXTURE_PATH=DEFAULT_TEXTURE_PATH):
        """
        Changes the path of the textures to a custom one (include '/' at the end)
        """
        self.TEXTURE_PATH = TEXTURE_PATH

        self.bg = Image.open(f'{TEXTURE_PATH}background.png')
        self.generator = Image.open(f"{TEXTURE_PATH}generator.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.C_spinner = Image.open(f"{TEXTURE_PATH}C_spinner.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.CC_spinner = Image.open(f"{TEXTURE_PATH}CC_spinner.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.mover = Image.open(f"{TEXTURE_PATH}mover.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.slide = Image.open(f"{TEXTURE_PATH}slide.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.push = Image.open(f"{TEXTURE_PATH}push.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.immobile = Image.open(f"{TEXTURE_PATH}immobile.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.enemy = Image.open(f"{TEXTURE_PATH}enemy.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.trash = Image.open(f"{TEXTURE_PATH}trash.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.placeable = Image.open(f"{TEXTURE_PATH}placeable.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        self.change_size((self.width, self.height))

    def do_nothing(self):
        pass

    def parse_v1(self, code_str: str) -> tuple[Grid, list[tuple[int, int]], str]:
        """
        Parses a v1 code and turns it into a tuple containing all the data
        """
        code: list[str] = code_str.split(";")

        width = int(code[1])
        height = int(code[2])

        # print(width, height)

        cells: list[str] = code[4].split(',')

        parsedCells: Grid = Grid(width, height)

        if cells:
            for cell_str in cells:
                # id, rot, x, y
                cell = list(map(int, cell_str.split(".")))

                parsedCells.cells.append(CELLS[cell[0]](cell[2], cell[3], cell[1]))

        placeables: list[str] = code[3].split(',')

        parsedPlaceables: list[tuple[int, int]] = []

        if placeables[0] != '':
            for placeable_str in placeables:
                # x, y
                placeable: tuple[int, int] = tuple(map(int, placeable_str.split('.')))  # type: ignore
                parsedPlaceables.append(tuple(placeable))  # type: ignore

        return ((parsedCells, parsedPlaceables, code[5]))

    def parse_v3(self, code_str: str) -> tuple[Grid, list[tuple[int, int]], str]:
        """
        Parses a v3 code and turns it into a tuple containing all the data
        """
        arguments = code_str.split(';')

        rawCells: list[tuple[int, int]] = []

        gridWidth = b74_decode(arguments[1])
        gridHeight = b74_decode(arguments[2])

        length = 0
        dataIndex = 0
        gridIndex = 0
        temp = ""

        cellDataHistory = [0] * (gridWidth * gridHeight)
        offset = 0

        while dataIndex < len(arguments[3]):
            if arguments[3][dataIndex] == ')' or arguments[3][dataIndex] == '(':
                if arguments[3][dataIndex] == ')':
                    dataIndex += 2
                    offset = b74_decode(arguments[3][dataIndex - 1])
                    length = b74_decode(arguments[3][dataIndex])
                else:
                    dataIndex += 1
                    temp = ""
                    while arguments[3][dataIndex] != ')' and arguments[3][dataIndex] != '(':
                        temp += arguments[3][dataIndex]
                        dataIndex += 1
                    offset = b74_decode(temp)
                    if arguments[3][dataIndex] == ')':
                        dataIndex += 1
                        length = b74_decode(arguments[3][dataIndex])
                    else:
                        dataIndex += 1
                        temp = ""
                        while arguments[3][dataIndex] != ')':
                            temp += arguments[3][dataIndex]
                            dataIndex += 1
                        length = b74_decode(temp)
                for i in range(length):
                    rawCells.append((cellDataHistory[gridIndex - offset - 1], gridIndex))
                    cellDataHistory[gridIndex] = cellDataHistory[gridIndex - offset - 1]
                    gridIndex += 1
            else:
                rawCells.append((b74_decode(arguments[3][dataIndex]), gridIndex))
                cellDataHistory[gridIndex] = b74_decode(arguments[3][dataIndex])
                gridIndex += 1
            dataIndex += 1

        newCells: Grid = Grid(gridWidth, gridHeight)
        placeables: list[tuple[int, int]] = []

        for rawCell in rawCells:
            cellX = math.floor(rawCell[1] % gridWidth)
            cellY = math.floor(rawCell[1] / gridWidth)
            if rawCell[0] % 2 == 1:
                placeables.append((cellX, cellY))
            if rawCell[0] >= 72:
                continue
            cellType = math.floor((rawCell[0] / 2) % 9)
            cellDirection = math.floor(rawCell[0] / 18)
            newCells.cells.append(CELLS[cellType](cellX, cellY, cellDirection))

        return ((newCells, placeables, arguments[4]))

    def parse_code(self, code: str):
        """
        Parse a code in any format
        """
        if code.startswith("V1"):
            level = self.parse_v1(code)
        elif code.startswith("V2"):
            raise NotImplementedError("V2 codes have not been implemented yet")
        elif code.startswith("V3"):
            level = self.parse_v3(code)
        else:
            return

        self.cells = Grid(1, 1)
        self.width = 1
        self.height = 1
        self.placeables = []
        self.name = ""

        self.cells = level[0]
        self.width = self.cells.width
        self.height = self.cells.height
        self.placeables = level[1]
        self.name = level[2]

        self.change_size((self.width, self.height))

        self.resetCells = level[0]

    def save_v3(self) -> str:
        """
        Saves the level as a v3 code\n
        slow
        """
        topLeft = self.height - 1
        bottomRight = self.width - 1

        output = f"V3;{b74_encode(self.width)};{b74_encode(self.height)};"

        cellData = [0] * (((bottomRight + 1) - 0) * ((topLeft + 1) - 0))
        dataIndex = 0

        y = 0
        x = 0

        for y in range(0, topLeft+1):
            for x in range(0, bottomRight+1):
                if (x, y) in self.placeables:
                    cellData[(x - 0) + ((y - 0) * (bottomRight + 1 - 0))] = 73
                else:
                    cellData[(x - 0) + ((y - 0) * (bottomRight + 1 - 0))] = 72

        for cell in self.cells.cells:
            cellData[(cell.x - 0) + ((cell.y - 0) * ((bottomRight + 1) - 0))] += (2 * cell.CELL_ID) + (18 * cell.direction)
            cellData[(cell.x - 0) + ((cell.y - 0) * ((bottomRight + 1) - 0))] -= 72

        maxMatchLength = 0
        maxMatchOffset = 0

        while dataIndex < len(cellData):
            maxMatchLength = 0

            matchOffset = 1
            for matchOffset in range(1, dataIndex+1):
                matchLength = 0
                while dataIndex + matchLength < len(cellData) \
                        and cellData[dataIndex + matchLength] == cellData[dataIndex + matchLength - matchOffset]:
                    matchLength += 1
                    if matchLength > maxMatchLength:
                        maxMatchLength = matchLength
                        maxMatchOffset = matchOffset - 1

            if maxMatchLength > 3:
                if len(b74_encode(maxMatchLength)) == 1:
                    if len(b74_encode(maxMatchOffset)) == 1:
                        if maxMatchLength > 3:
                            output += f"){b74_encode(maxMatchOffset)}{b74_encode(maxMatchLength)}"
                            dataIndex += maxMatchLength - 1
                        else:
                            output += b74_key[cellData[dataIndex]]

                    else:
                        if maxMatchLength > 3 + len(b74_encode(maxMatchOffset)):
                            output += f"({b74_encode(maxMatchOffset)}){b74_encode(maxMatchLength)}"
                            dataIndex += maxMatchLength - 1
                        else:
                            output += b74_key[cellData[dataIndex]]

                else:
                    output += f"({b74_encode(maxMatchOffset)}({b74_encode(maxMatchLength)})"
                    dataIndex += maxMatchLength - 1

            else:
                output += b74_encode(cellData[dataIndex])

            maxMatchLength = 0
            dataIndex += 1

        return output + ";;"

    def change_size(self, size: tuple[int, int]):
        """
        This is an internal function and should not be used
        """

        width = self.width * self.TEXTURE_SIZE
        height = self.height * self.TEXTURE_SIZE

        img = Image.new(mode="RGB", size=(int(width), int(height)))

        for i in range(0, width, self.TEXTURE_SIZE):
            for j in range(0, height, self.TEXTURE_SIZE):
                img.paste(self.bg, (i, j))

        self.prerendered_bg = img

    def view(self):
        """
        Turns the level into a PIL image
        """
        all_cells = [self.generator, self.C_spinner, self.CC_spinner, self.mover, self.slide, self.push, self.immobile, self.enemy, self.trash]

        width = self.width
        height = self.height

        width *= self.TEXTURE_SIZE
        height *= self.TEXTURE_SIZE

        img = deepcopy(self.prerendered_bg)

        for placeable_data in self.placeables:
            img.paste(self.placeable, (placeable_data[0] * self.TEXTURE_SIZE, placeable_data[1] * self.TEXTURE_SIZE))

        for cell in self.cells.cells:
            cell_to_paste = all_cells[cell.CELL_ID]

            img.paste(cell_to_paste.rotate(cell.direction * 90), (cell.x * self.TEXTURE_SIZE, cell.y * self.TEXTURE_SIZE))

        if self.SCALE == 0:
            return (img)
        else:
            nextWidth = math.floor(width * self.SCALE)
            nextHeight = math.floor(height * self.SCALE)
            scaledImg = img.resize(size=(nextWidth, nextHeight), resample=Image.Resampling.NEAREST)
            return (scaledImg.transpose(1))

    # TICKING

    def get_cell_at_location(self, x, y):
        """
        Gets a cell at a location
        """
        return self.cells.get(x, y)

    def tick(self, amount=1):
        for i in range(amount):
            tickNum = random.randint(1, 1000)
            for cell_type_to_tick in SUBTICKING_ORDER:
                # if cell_type_to_tick == C_Spinner or cell_type_to_tick == CC_Spinner:
                #     self.view().show()
                for cell_direction_to_tick in SUBTICKING_DIRECTION:
                    # GET CELLS OF DIRECTION
                    cells_to_tick: list[TickedCell] = []
                    for cell in self.cells.cells:
                        if cell_type_to_tick == Generator or cell_type_to_tick == Mover:
                            if cell.direction == cell_direction_to_tick and cell.CELL_ID == cell_type_to_tick.CELL_ID:
                                cells_to_tick.append(cell)  # type: ignore
                        else:
                            cells_to_tick.append(cell) if cell.CELL_ID == cell_type_to_tick.CELL_ID else self.do_nothing()  # type: ignore

                    if cells_to_tick == []:
                        continue

                    if cell_direction_to_tick == Direction.RIGHT:
                        cells_to_tick = sorted(cells_to_tick, key=operator.attrgetter('x'), reverse=True)
                    elif cell_direction_to_tick == Direction.LEFT:
                        cells_to_tick = sorted(cells_to_tick, key=operator.attrgetter('x'), reverse=False)
                    elif cell_direction_to_tick == Direction.UP:
                        cells_to_tick = sorted(cells_to_tick, key=operator.attrgetter('y'), reverse=True)
                    else:
                        cells_to_tick = sorted(cells_to_tick, key=operator.attrgetter('y'), reverse=False)

                    for cell in cells_to_tick:
                        tickedver: TickedCell = cell  # type: ignore
                        if tickedver.tickNum != tickNum:
                            self.cells = tickedver.step(self.cells)
                            tickedver.tickNum = tickNum
            self.tickAmount += 1

    def reset(self):
        self.cells = self.resetCells

    def unload(self):
        """
        Unloads all the images
        """
        self.bg.close()
        self.generator.close()
        self.C_spinner.close()
        self.CC_spinner.close()
        self.mover.close()
        self.slide.close()
        self.push.close()
        self.immobile.close()
        self.enemy.close()
        self.trash.close()
        self.placeable.close()
