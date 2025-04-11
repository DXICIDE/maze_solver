from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(200,300), Point(300,300)), "black")
    win.draw_line(Line(Point(250,300), Point(400,478)), "red")
    win.draw_line(Line(Point(378,550), Point(520,112)), "green")
    cell = Cell(100, 100, 110, 110, win, True, True, True, True)
    cell.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
