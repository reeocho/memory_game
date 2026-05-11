# import
from random import *
from turtle import width
from graphics import *

iteration = 0

# create game window
def main():
    settings = GraphWin("Memory Game", 1728, 1080)
    button = Rectangle(Point(250, 100), Point(350, 150)).draw(settings)
    button_text = Text(Point(300, 125), "Start").draw(settings)
    while True:
        if button_text.getText() == "Start":
            settings.close()
            break

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


    
main()
win = create_dot_grid("Dot Grid", 5)

win.getMouse()
win.close()