from .base74 import b74_encode, b74_key
from .Cell import Cell
from level_save_gen_str import *

cpdef str _save_v3(int topLeft, int bottomRight, int width, int height, list cells, list placeables, str start_point):
        cdef str output = start_point

        cdef list cellData = [0] * (((bottomRight + 1) - 0) * ((topLeft + 1) - 0))
        dataIndex = 0

        cdef int y = 0
        cdef int x = 0

        for y in range(0, topLeft+1):
            for x in range(0, bottomRight+1):
                if (x, y) in placeables:
                    cellData[(x - 0) + ((y - 0) * (bottomRight + 1 - 0))] = 73
                else:
                    cellData[(x - 0) + ((y - 0) * (bottomRight + 1 - 0))] = 72

        cdef cell

        for cell in cells:
            cellData[(cell.x - 0) + ((cell.y - 0) * ((bottomRight + 1) - 0))] += (2 * cell.CELL_ID) + (18 * cell.direction)
            cellData[(cell.x - 0) + ((cell.y - 0) * ((bottomRight + 1) - 0))] -= 72

        cdef int matchLength = 0
        cdef int matchOffset = 0
        cdef int maxMatchLength = 0
        cdef int maxMatchOffset = 0

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
                            output += case_one(maxMatchOffset, maxMatchLength)
                            dataIndex += maxMatchLength - 1
                        else:
                            output += b74_key[cellData[dataIndex]]

                    else:
                        if maxMatchLength > 3 + len(b74_encode(maxMatchOffset)):
                            output += case_two(maxMatchOffset, maxMatchLength)
                            dataIndex += maxMatchLength - 1
                        else:
                            output += b74_key[cellData[dataIndex]]

                else:
                    output += case_three(maxMatchOffset, maxMatchLength)
                    dataIndex += maxMatchLength - 1

            else:
                output += b74_encode(cellData[dataIndex])

            maxMatchLength = 0
            dataIndex += 1

        return output + ";;"