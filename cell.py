from window import *

class Cell:
    def __init__(self, x1, y1, x2, y2, win, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
    def draw(self):
        if self._win is None:
            return
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1), Point(self._x2, self._y1)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2), Point(self._x2, self._y2)), "black")
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1), Point(self._x1, self._y2)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1), Point(self._x2, self._y2)), "black")

    def draw_move(self, to_cell, undo = False):
        cell_a = Point((self._x1 + self._x2)/2,(self._y1 + self._y2)/2)
        cell_b = Point((to_cell._x1 + to_cell._x2)/2,(to_cell._y1 + to_cell._y2)/2)
        if undo:
            self._win.draw_line(Line(cell_a, cell_b), "gray")
        else:
            self._win.draw_line(Line(cell_a, cell_b), "red")