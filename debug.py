from cellmachine.CellMachine import CellMachine
from PIL import Image

cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;1q;1q;{(0(13O)SA(1p(1o)0i2(Vw(U4);;;0")

cellmachine.tick(int(input("Please enter the amount of ticks : ")))

img: Image = cellmachine.view()

img.save("out.png")