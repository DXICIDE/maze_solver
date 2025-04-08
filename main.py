from window import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw(Line(Point(200,300), Point(300,300)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
