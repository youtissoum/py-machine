import math
from re import M
from PIL import Image, ImageDraw
import os

TEXTURE_PATH = 'cmmmPreviewer/textures/'
TEXTURE_SIZE = 16
FINAL_SIZE = 500

def parse_v1(codeStr: str) -> tuple[tuple[int, int], list[tuple[int, int, int, int]], list[tuple[int, int]], str]:
    code: list[str] = codeStr.split(";")

    width = int(code[1])
    height = int(code[2])

    # print(width, height)

    cells: list[str] = code[4].split(',')
    
    parsedCells: list[tuple[int, int, int, int]] = []

    if cells:
        for cell_str in cells:
            # id, rot, x, y
            cell: tuple[int, int, int, int] = tuple(map(int, cell_str.split(".")))
            parsedCells.append(cell)

    placeables: list[str] = code[3].split(',')

    parsedPlaceables: list[tuple[int, int]] = []

    if placeables[0] != '':
        for placeable_str in placeables:
            # x, y
            placeable: tuple[int, int] = tuple(map(int, placeable_str.split('.')))
            parsedPlaceables.append(placeable)

    return(((width, height), parsedCells, parsedPlaceables, code[5]))

def preview(code: tuple[tuple[int, int], list[tuple[int, int, int, int]], list[tuple[int, int]], str]) -> Image:
    bg = Image.open(f'{TEXTURE_PATH}background.png')
    generator = Image.open(f"{TEXTURE_PATH}generator.png").transpose(Image.FLIP_TOP_BOTTOM)
    C_spinner = Image.open(f"{TEXTURE_PATH}C_spinner.png").transpose(Image.FLIP_TOP_BOTTOM)
    CC_spinner = Image.open(f"{TEXTURE_PATH}CC_spinner.png").transpose(Image.FLIP_TOP_BOTTOM)
    mover = Image.open(f"{TEXTURE_PATH}mover.png").transpose(Image.FLIP_TOP_BOTTOM)
    slide = Image.open(f"{TEXTURE_PATH}slide.png").transpose(Image.FLIP_TOP_BOTTOM)
    push = Image.open(f"{TEXTURE_PATH}push.png").transpose(Image.FLIP_TOP_BOTTOM)
    immobile = Image.open(f"{TEXTURE_PATH}immobile.png").transpose(Image.FLIP_TOP_BOTTOM)
    enemy = Image.open(f"{TEXTURE_PATH}enemy.png").transpose(Image.FLIP_TOP_BOTTOM)
    trash = Image.open(f"{TEXTURE_PATH}trash.png").transpose(Image.FLIP_TOP_BOTTOM)
    placeable = Image.open(f"{TEXTURE_PATH}placeable.png").transpose(Image.FLIP_TOP_BOTTOM)
    all_cells = [generator, C_spinner, CC_spinner, mover, slide, push, immobile, enemy, trash]

    width, height = code[0]

    width  *= TEXTURE_SIZE
    height *= TEXTURE_SIZE

    img = Image.new(mode="RGB", size=(int(width), int(height)))

    for i in range(0, width, TEXTURE_SIZE):
        for j in range(0, height, TEXTURE_SIZE):
            img.paste(bg, (i, j))

    for placeable_data in code[2]:
        img.paste(placeable, (placeable_data[0] * TEXTURE_SIZE, placeable_data[1] * TEXTURE_SIZE))

    for cell in code[1]:
        cell_to_paste = all_cells[cell[0]]

        img.paste(cell_to_paste.rotate(cell[1] * 90), (cell[2] * TEXTURE_SIZE, cell[3] * TEXTURE_SIZE))

    bg.close()
    generator.close()
    C_spinner.close()
    CC_spinner.close()
    mover.close()
    slide.close()
    push.close()
    immobile.close()
    enemy.close()
    trash.close()
    placeable.close()

    nextHeight = math.floor(height * (500 / width))
    scaledImg: Image = img.resize(size=(500, nextHeight), resample=Image.NEAREST)
    return(scaledImg.transpose(1))