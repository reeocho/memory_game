# import
from random import *
from graphics import *
from time import *

iteration = 0

def text_create(text, settings):
    texttodraw = Text(Point(200, 50), text)
    texttodraw.setTextColor("red")
    texttodraw.draw(settings)
    sleep(5)
    texttodraw.undraw()


def main():
    settings = GraphWin("Memory Game", 500, 300)
    e = Entry(Point(250, 150), 50)
    e.draw(settings)
    button = Rectangle(Point(200, 200), Point(300, 250))
    button.label = Text(Point(250, 225), "Start")
    button.label.draw(settings)
    button.draw(settings)
    while True:
        text = e.getText()
        if button.getP1().getX() < settings.getMouse().getX() < button.getP2().getX() and \
           button.getP1().getY() < settings.getMouse().getY() < button.getP2().getY():
            settings.close()
            break
        else:
            text_create("Type 'start' to begin the game!", settings)

def create_dot_grid(game_code, number):
    spacing = 50
    width = 50 * (number+1)
    win = GraphWin(game_code, width, width)
    
    # Dictionary to store dots
    dots = []
    dot_id = 0

    for i, x in enumerate(range(spacing, width, spacing)):
        for j, y in enumerate(range(spacing, width, spacing)):
            circle = Circle(Point(x, y), 5)
            circle.draw(win)
            dots.append(circle)
            
    return win, dots



main()



win, dots = create_dot_grid("Dot Grid", 5)
win.getMouse()
win.close()