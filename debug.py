import math
from cellmachine.CellMachine import CellMachine
from PIL import Image
import time

before = time.time()
cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;27;27;{(0(2eq)ddd(26(25)}B}B(29(15)}(26)^Tdf(4f(23)d}1bhh(28(21)dhh$dJ}2AA(23(1.)6a2{$rJ9r}{(27(1^){{{h9b$r(8t(22)d9d20c(aA(22)2{Y2(25(22)ca{{6(25(21)6o(n2(25)6i(pb(27)a(4d(iY)(0(1In);;;0")

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