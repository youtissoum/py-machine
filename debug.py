import math
from cellmachine.CellMachine import CellMachine
from PIL import Image
import time

before = time.time()
cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;1q;1q;{(0(&B)SA(1p(1o)0i2(++(&C)(0(2R);;;0")

# timed
before = time.time()
cellmachine.tick(10)
print(round(time.time() - before, 3))

# almost 4 minutes for nuke in 100x100 map

cellmachine.view().save("out.png")

input()

# while True:
#     cellmachine.tick(1)
#     # cellmachine.tick(int(input("Please enter the amount of ticks : ")))

#     img: Image = cellmachine.view()

#     img.save("out.png")

#     input()