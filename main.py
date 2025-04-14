from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(100, 200, 5, 2, 15, 15, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
