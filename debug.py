from cellmachine.CellMachine import CellMachine
from PIL import Image

cellmachine = CellMachine()

# cellmachine.parse_code(input("Please enter your code : "))
cellmachine.parse_code("V3;1q;1q;{(0(WT)Y(1m(1m)S{{a(1p(1p)2(1n(1k)C9r9999CC(1o(1g)6rJVJtJJ$r(2Q(1i)r$r99t9$G(1p(1h)v1}1}$rU(5v(1j)${dfd(aX(1o)(1o(1p)(0(%h);Manticore V1;")

cellmachine.tick(int(input("Please enter the amount of ticks : ")))

img: Image = cellmachine.view()

img.save("out.png")