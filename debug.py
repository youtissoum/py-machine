from cellmachine.CellMachine import CellMachine
from PIL import Image

cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;1q;1q;{(0(Zy)hhh(1p(1o)f(1p(1p)$}46GG(43(1m)c(&G(Zz)(0(86);;")

cellmachine.tick(int(input("Please enter the amount of ticks : ")))

img: Image = cellmachine.view()

img.save("out.png")