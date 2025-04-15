from cell import Cell
import time as time
import random as random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._win.maze = self
        if seed != None:
            self._seed = random.seed(seed)
        self.create()

    def create(self):
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()
    
    def reset(self):
        if self._win:
            self._win.clear_canvas()
            self.create()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            cols = list()
            for j in range(self._num_rows):
                cols.append(Cell(None, None, None, None, self._win))
            self._cells.append(cols)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j]._x1 = self._x1 + (i) * self._cell_size_x
        self._cells[i][j]._x2 = self._x1 + (i+1) * self._cell_size_x
        self._cells[i][j]._y1 = self._y1 + (j) * self._cell_size_y
        self._cells[i][j]._y2 = self._y1 + (j+1) * self._cell_size_y
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._cells[0][0].draw()
        self._cells[self._num_cols-1][self._num_rows-1].draw()
        self._animate()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_to_visit = []
            if i > 0:
                if self._cells[i-1][j].visited == False:
                    next_to_visit.append([i-1,j])
            if i < self._num_cols-1:
                if self._cells[i+1][j].visited == False:
                    next_to_visit.append([i+1,j])
            if j > 0:
                if self._cells[i][j-1].visited == False:
                    next_to_visit.append([i,j-1])
            if j+1 < self._num_rows:
                if self._cells[i][j+1].visited == False:
                    next_to_visit.append([i,j+1])
            print(next_to_visit)
            if len(next_to_visit) == 0:
                self._cells[i][j].draw()
                return
            else:
                random_direction = random.randrange(len(next_to_visit))
                i1 = next_to_visit[random_direction][0]
                j1 = next_to_visit[random_direction][1]
                if i1 == i+1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i1][j].has_left_wall = False
                    self._cells[i][j].draw()
                    self._break_walls_r(i1, j)
                elif i1 == i-1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i1][j].has_right_wall = False
                    self._cells[i][j].draw()
                    self._break_walls_r(i1, j)
                elif j1 == j+1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j1].has_top_wall = False
                    self._cells[i][j].draw()
                    self._break_walls_r(i, j1)
                elif j1 == j-1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j1].has_bottom_wall = False
                    self._cells[i][j].draw()
                    self._break_walls_r(i, j1)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        
        # Move to the left
        if i > 0:
            if self._cells[i-1][j].visited == False:
                if self._cells[i][j].has_left_wall == False:
                    self._cells[i][j].draw_move(self._cells[i-1][j], undo = False)
                    if self._solve_r(i-1,j):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i-1][j], undo = True)

        # Move to the right
        if i < self._num_cols-1:
            if self._cells[i+1][j].visited == False:
                if self._cells[i][j].has_right_wall == False:
                    self._cells[i][j].draw_move(self._cells[i+1][j], undo = False)
                    if self._solve_r(i+1,j):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i+1][j], undo = True)

        # Move Up
        if j > 0:
            if self._cells[i][j-1].visited == False:
                if self._cells[i][j].has_top_wall == False:
                    self._cells[i][j].draw_move(self._cells[i][j-1], undo = False)
                    if self._solve_r(i,j-1):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j-1], undo = True)

         # Move Down
        if j+1 < self._num_rows:
            if self._cells[i][j+1].visited == False:
                if self._cells[i][j].has_bottom_wall == False:
                    self._cells[i][j].draw_move(self._cells[i][j+1], undo = False)
                    if self._solve_r(i,j+1):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j+1], undo = True)
        return False