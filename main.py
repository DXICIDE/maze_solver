from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(1600, 800)
    maze = Maze(0, 0, 40, 40, 15, 15, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
