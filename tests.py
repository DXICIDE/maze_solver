import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_cells_visited_false(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[9][9].visited, False)
        self.assertEqual(m1._cells[0][0].visited, False)

        m1._cells[5][5].visited = True
        m1._cells[0][0].visited = True
        self.assertEqual(m1._cells[5][5].visited, True)
        self.assertEqual(m1._cells[0][0].visited, True)
        m1._reset_cells_visited()
        self.assertEqual(m1._cells[5][5].visited, False)
        self.assertEqual(m1._cells[0][0].visited, False)

if __name__ == "__main__":
    unittest.main()