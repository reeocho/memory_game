# import
from random import *
from graphics import *

# create game window
# win = GraphWin("Memory Game", 1728, 1080)


def create_dot_grid(game_code, number):
    spacing = 50
    width = 50 * number
    win = GraphWin(game_code, width, width)

    dot_radius = 1

    for x in range(spacing, width, spacing):
        for y in range(spacing, width, spacing):
            dot = Circle(Point(x, y), dot_radius)
            dot.setFill("black")
            dot.draw(win)
    return win


win = create_dot_grid("Dot Grid", 4)
win.getMouse()
win.close()