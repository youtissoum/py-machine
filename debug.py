import math
from cellmachine.CellMachine import CellMachine
from PIL import Image
import time

before = time.time()
cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;2P;2P;{(0(35h)a(2O(2O)S(5r(tG)6c(2N(2M)dbdddhd(2O(2I)h9JJJ$${{CaA)17(5r(2B)b(5r(2J)d$d}d$(2O(2L)hdd9(2O(2K)bbfh}26GG(aM(2y)(2O)8hjdB3(iZ(2L)}B}(83(2J){{d)04(3ZV(35i)(0(o9);;;0")

tick_amount = int(input("Enter the amount of ticks : "))
# timed
before = time.time()
cellmachine.tick(tick_amount)
print(round(time.time() - before, 3))

# almost 4 minutes for nuke in 100x100 map

before = time.time()
cellmachine.view().save("out.png")
print(round(time.time() - before, 3))

# while True:
#     cellmachine.tick(1)
#     # cellmachine.tick(int(input("Please enter the amount of ticks : ")))

#     img: Image = cellmachine.view()

#     img.save("out.png")

#     input()