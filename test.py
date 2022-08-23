import unittest

from cellmachine.CellMachine import CellMachine

assertion = ""

def get_cell_data(cells):
    cell_data = []
    for cell in cells:
        cell_data.append((cell.CELL_ID, cell.CELL_NAME, (cell.x, cell.y), cell.direction))
    return cell_data

class ManticoreV1Test(unittest.TestCase):
    def test_v1_import(self):
        cellmachine = CellMachine()
        cellmachine.parse_code("V1;100;100;44.46,45.46,46.46,47.46,48.46,49.46,43.47,44.47,45.47,46.47,47.47,48.47,49.47,50.47,51.47,44.48,45.48,46.48,47.48,48.48,49.48,50.48,51.48,44.49,45.49,46.49,47.49,48.49,49.49,50.49,45.50,47.50,48.50,49.50,48.51;4.0.44.46,4.1.45.46,4.0.46.46,4.0.47.46,4.2.48.46,4.0.49.46,4.1.43.47,4.2.44.47,1.3.45.47,4.2.46.47,5.1.47.47,4.2.48.47,4.2.49.47,4.3.50.47,4.1.51.47,4.1.44.48,4.3.45.48,4.1.46.48,4.0.47.48,4.0.48.48,5.1.49.48,4.0.50.48,4.3.51.48,6.1.44.49,0.0.45.49,0.0.47.49,4.3.49.49,4.1.50.49,4.3.45.50,6.0.47.50,7.0.48.50,6.0.49.50,6.0.48.51;Manticore V1;")
        cells = get_cell_data(cellmachine.cells.cells)
        self.assertEqual(cells, [(4, 'slide', (44, 46), 0), (4, 'slide', (45, 46), 1), (4, 'slide', (46, 46), 0), (4, 'slide', (47, 46), 0), (4, 'slide', (48, 46), 2), (4, 'slide', (49, 46), 0), (4, 'slide', (43, 47), 1), (4, 'slide', (44, 47), 2), (1, 'c_spinner', (45, 47), 3), (4, 'slide', (46, 47), 2), (5, 'push', (47, 47), 1), (4, 'slide', (48, 47), 2), (4, 'slide', (49, 47), 2), (4, 'slide', (50, 47), 3), (4, 'slide', (51, 47), 1), (4, 'slide', (44, 48), 1), (4, 'slide', (45, 48), 3), (4, 'slide', (46, 48), 1), (4, 'slide', (47, 48), 0), (4, 'slide', (48, 48), 0), (5, 'push', (49, 48), 1), (4, 'slide', (50, 48), 0), (4, 'slide', (51, 48), 3), (6, 'immobile', (44, 49), 1), (0, 'generator', (45, 49), 0), (0, 'generator', (47, 49), 0), (4, 'slide', (49, 49), 3), (4, 'slide', (50, 49), 1), (4, 'slide', (45, 50), 3), (6, 'immobile', (47, 50), 0), (7, 'enemy', (48, 50), 0), (6, 'immobile', (49, 50), 0), (6, 'immobile', (48, 51), 0)], "V1 import did not give correct cells")
        self.assertEqual(cellmachine.name, "Manticore V1", "V1 import did not give correct name")
        self.assertEqual((cellmachine.width, cellmachine.height), (100, 100), "V1 import did not give correct size")

    def test_v3_import(self):
        cellmachine = CellMachine()
        cellmachine.parse_code("V3;1q;1q;{(0(!T)9r99J9(1o(1j)rJVJtJJ$r(1q(1j)$r99t9$(1p(1i)v1}1}(2O(1k){{${dfd(6X(1o)(1o(1p)(0(%h);Manticore V1;")
        cells = get_cell_data(cellmachine.cells.cells)
        self.assertEqual(cells, [(4, 'slide', (44, 46), 0), (4, 'slide', (45, 46), 1), (4, 'slide', (46, 46), 0), (4, 'slide', (47, 46), 0), (4, 'slide', (48, 46), 2), (4, 'slide', (49, 46), 0), (4, 'slide', (43, 47), 1), (4, 'slide', (44, 47), 2), (1, 'c_spinner', (45, 47), 3), (4, 'slide', (46, 47), 2), (5, 'push', (47, 47), 1), (4, 'slide', (48, 47), 2), (4, 'slide', (49, 47), 2), (4, 'slide', (50, 47), 3), (4, 'slide', (51, 47), 1), (4, 'slide', (44, 48), 1), (4, 'slide', (45, 48), 3), (4, 'slide', (46, 48), 1), (4, 'slide', (47, 48), 0), (4, 'slide', (48, 48), 0), (5, 'push', (49, 48), 1), (4, 'slide', (50, 48), 0), (4, 'slide', (51, 48), 3), (6, 'immobile', (44, 49), 1), (0, 'generator', (45, 49), 0), (0, 'generator', (47, 49), 0), (4, 'slide', (49, 49), 3), (4, 'slide', (50, 49), 1), (4, 'slide', (45, 50), 3), (6, 'immobile', (47, 50), 0), (7, 'enemy', (48, 50), 0), (6, 'immobile', (49, 50), 0), (6, 'immobile', (48, 51), 0)], "V3 import did not give correct cells")
        self.assertEqual(cellmachine.name, "Manticore V1", "V1 import did not give correct name")
        self.assertEqual((cellmachine.width, cellmachine.height), (100, 100), "V1 import did not give correct size")

    def test_ticking(self):
        cellmachine = CellMachine()
        cellmachine.parse_code("V3;1q;1q;{(0(!T)9r99J9(1o(1j)rJVJtJJ$r(1q(1j)$r99t9$(1p(1i)v1}1}(2O(1k){{${dfd(6X(1o)(1o(1p)(0(%h);Manticore V1;")
        cellmachine.tick(2)
        self.assertEqual(get_cell_data(cellmachine.cells.cells), [(4, 'slide', (44, 46), 0), (4, 'slide', (45, 46), 3), (4, 'slide', (46, 46), 0), (4, 'slide', (47, 46), 0), (4, 'slide', (48, 46), 2), (4, 'slide', (49, 46), 0), (4, 'slide', (43, 47), 1), (4, 'slide', (44, 47), 0), (1, 'c_spinner', (45, 47), 3), (4, 'slide', (46, 47), 0), (5, 'push', (47, 47), 1), (4, 'slide', (48, 47), 2), (4, 'slide', (49, 47), 2), (4, 'slide', (50, 47), 3), (4, 'slide', (51, 47), 1), (4, 'slide', (44, 48), 1), (4, 'slide', (45, 48), 1), (4, 'slide', (46, 48), 1), (4, 'slide', (47, 48), 0), (4, 'slide', (48, 48), 0), (5, 'push', (49, 48), 1), (4, 'slide', (50, 48), 0), (4, 'slide', (51, 48), 3), (6, 'immobile', (44, 49), 1), (0, 'generator', (45, 49), 0), (0, 'generator', (47, 49), 0), (4, 'slide', (49, 49), 3), (4, 'slide', (50, 49), 1), (4, 'slide', (45, 50), 3), (6, 'immobile', (47, 50), 0), (7, 'enemy', (48, 50), 0), (6, 'immobile', (49, 50), 0), (6, 'immobile', (48, 51), 0), (6, 'immobile', (46, 49), 1), (6, 'immobile', (48, 49), 1)], "ticking did not work")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ManticoreV1Test('test_v1_import'))
    suite.addTest(ManticoreV1Test('test_v3_import'))
    suite.addTest(ManticoreV1Test('test_ticking'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())