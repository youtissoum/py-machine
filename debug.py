import math
from cellmachine.CellMachine import CellMachine
from PIL import Image
import time

before = time.time()
cellmachine = CellMachine()

cellmachine.parse_code(input("Please enter your code : "))
# cellmachine.parse_code("V3;1q;1q;{(0(!T)9r99J9(1o(1j)rJVJtJJ$r(1q(1j)$r99t9$(1p(1i)v1}1}(2O(1k){{${dfd(6X(1o)(1o(1p)(0(%h);Manticore V1;;0")

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