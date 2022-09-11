from unittest import TestCase

from Python_Machine.CellMachine import CellMachine

manticore_import_result = [(4, 0, (44, 46)), (4, 1, (45, 46)), (4, 0, (46, 46)), (4, 0, (47, 46)), (4, 2, (48, 46)), (4, 0, (49, 46)), (4, 1, (43, 47)), (4, 2, (44, 47)), (1, 3, (45, 47)), (4, 2, (46, 47)), (5, 1, (47, 47)), (4, 2, (48, 47)), (4, 2, (49, 47)), (4, 3, (50, 47)), (4, 1, (51, 47)), (4, 1, (44, 48)), (4, 3, (45, 48)), (4, 1, (46, 48)), (4, 0, (47, 48)), (4, 0, (48, 48)), (5, 1, (49, 48)), (4, 0, (50, 48)), (4, 3, (51, 48)), (6, 1, (44, 49)), (0, 0, (45, 49)), (0, 0, (47, 49)), (4, 3, (49, 49)), (4, 1, (50, 49)), (4, 3, (45, 50)), (6, 0, (47, 50)), (7, 0, (48, 50)), (6, 0, (49, 50)), (6, 0, (48, 51))]
def test_import_manticore_v1():
    cellmachine = CellMachine()
    cellmachine.parse_code("V1;100;100;44.46,45.46,46.46,47.46,48.46,49.46,43.47,44.47,45.47,46.47,47.47,48.47,49.47,50.47,51.47,44.48,45.48,46.48,47.48,48.48,49.48,50.48,51.48,44.49,45.49,46.49,47.49,48.49,49.49,50.49,45.50,47.50,48.50,49.50,48.51;4.0.44.46,4.1.45.46,4.0.46.46,4.0.47.46,4.2.48.46,4.0.49.46,4.1.43.47,4.2.44.47,1.3.45.47,4.2.46.47,5.1.47.47,4.2.48.47,4.2.49.47,4.3.50.47,4.1.51.47,4.1.44.48,4.3.45.48,4.1.46.48,4.0.47.48,4.0.48.48,5.1.49.48,4.0.50.48,4.3.51.48,6.1.44.49,0.0.45.49,0.0.47.49,4.3.49.49,4.1.50.49,4.3.45.50,6.0.47.50,7.0.48.50,6.0.49.50,6.0.48.51;;")

    result = []
    for cell in cellmachine.cells.cells:
        result.append((cell.CELL_ID, cell.direction, (cell.x, cell.y)))

    assert result == manticore_import_result, "Importing manticore with v3 encoding did not work"

def test_import_manticore_v3():
    cellmachine = CellMachine()
    cellmachine.parse_code("V3;1q;1q;{(0(!T)9r99J9(1o(1j)rJVJtJJ$r(1q(1j)$r99t9$(1p(1i)v1}1}(2O(1k){{${dfd(6X(1o)(1o(1p)(0(%h);Manticore V1;;0")

    result = []
    for cell in cellmachine.cells.cells:
        result.append((cell.CELL_ID, cell.direction, (cell.x, cell.y)))

    assert result == manticore_import_result, "Importing manticore with v3 encoding did not work"