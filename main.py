from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(100, 200, 10, 10, 25, 25, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
