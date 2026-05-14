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
    e = Entry(Point(250, 150), 30)
    e.setText("Username")
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

def colourchangeplayer(dotprev, dotnew, player):
    if player == True:
        colour = "green"
    else:
        colour = "red"
    dotprev.undraw()
    dotprev.setFill("white")
    dotprev.draw(win)
    dotnew.undraw()
    dotnew.setFill(colour)
    dotnew.draw(win)
    return

def error(errormessage):
    error = Text(Point(150, 150), errormessage)
    error.setTextColor("red")
    error.draw(win)
    sleep(1)
    error.undraw()

def nextdot(dot, key):
    index = dots.index(dot)
    if key == "Right":
        if index < len(dots) - 5:
            return dots[index + 5]
        else:
            error("You can't move right!")
            return dot
    elif key == "Left":
        if index >= 5:
            return dots[index - 5]
        else:
            error("You can't move left!")
            return dot
    elif key == "Up":
        if index % 5 != 0:
            return dots[index - 1]
        else:
            error("You can't move up!")
            return dot
    elif key == "Down":
        if index % 5 != 4:
            return dots[index + 1]
        else:
            error("You can't move down!")
            return dot
main()


win, dots = create_dot_grid("Dot Grid", 5)
dots[0].undraw()
dots[0].setFill("green")
dots[0].draw(win)
print(dots)
dot = dots[0]
while True:
    key = win.checkKey()
    if key == "q":
        break
    elif key in ["Right", "Left", "Up", "Down"]:
        dotnew = nextdot(dot, key)
        colourchangeplayer(dot, dotnew, True)
        dot = dotnew
win.getMouse()
win.close()