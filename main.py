# import
from random import *
from graphics import *
from time import *

competitive = True

def text_create(text, settings):
    texttodraw = Text(Point(200, 50), text)
    texttodraw.setTextColor("red")
    texttodraw.draw(settings)
    sleep(5)
    texttodraw.undraw()

def check_location():
    # if it is next in the maze return true otherwise return false
    pass

def first_animation(maze):
    dots[maze[0]].undraw()
    dots[maze[0]].setFill("green")
    dots[maze[0]].draw(win)
    for x in range(1, len(maze)):
        sleep(0.5)
        dot = dots[maze[x-1]]
        dotnew = dots[maze[x]]
        dot.undraw()
        dot.setFill("white")
        dot.draw(win)
        dotnew.undraw()
        dotnew.setFill("green")
        dotnew.draw(win)
    sleep(0.5)
    dotnew.undraw()
    dotnew.setFill("white")
    dotnew.draw(win)
    return

def main():
    settings = GraphWin("Memory Game", 500, 300)
    e = Entry(Point(250, 150), 30)
    e.setText("Username")
    e.draw(settings)
    button = Rectangle(Point(200, 200), Point(300, 250))
    button.label = Text(Point(250, 225), "Start")
    button.label.draw(settings)
    button.draw(settings)
    name = e.getText()
    while True:
        if button.getP1().getX() < settings.getMouse().getX() < button.getP2().getX() and \
           button.getP1().getY() < settings.getMouse().getY() < button.getP2().getY():
            settings.close()
            break
        else:
            text_create("Press button to begin", settings)
    return name

def create_dot_grid(game_code, number):
    spacing = 50
    width = 50 * (number+1)
    win = GraphWin(game_code, width, width)
    
    # Dictionary to store dots
    dots = []

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

def createmaze(n):
    current = randint(0, n-1)
    maze = [current]
    endpoint = randint(n*n - n, n*n - 1)
    print(current, endpoint)
    while True:
        current = maze[-1]
        possible = []
        if current > n*n - n:
            if current == endpoint:
                print(maze)
                break
            if current < endpoint:
                maze.append(current + 1)
            if current > endpoint:
                maze.append(current - 1)
        else:
            if current % n != n-1:
                possible.append(1)
            if current % n != 0:
                possible.append(-1)
            if current + n <= n * n -1:
                possible.append(n)
            if not possible:
                raise IndexError("Oops something went wrong :(")
            added = maze[-1] + possible[randint(0, len(possible) - 1)]
            if added in maze:
                pass
            else:
                maze.append(added)
    return maze

def nextdot(dot, key, n):
    index = dots.index(dot)
    if key == "Right":
        if index < len(dots) - n:
            return dots[index + n]
        else:
            error("You can't move right")
            return dot
    elif key == "Left":
        if index >= n:
            return dots[index - n]
        else:
            error("You can't move left")
            return dot
    elif key == "Up":
        if index % n != 0:
            return dots[index - 1]
        else:
            error("You can't move up")
            return dot
    elif key == "Down":
        if index % n != n - 1:
            return dots[index + 1]
        else:
            error("You can't move down")
            return dot

def success_screen():
    Rectangle(Point(0,0), Point(win.getWidth(), win.getHeight())).draw(win)
    pass

number = 5
name = main()
maze = createmaze(number)

win, dots = create_dot_grid("Dot Grid", number)
first_animation(maze)
dots[0].undraw()
dots[0].setFill("green")
dots[0].draw(win)
dot = dots[0]
while True:
    key = win.checkKey()
    if key == "q":
        break
    if key == "h":
        if not competitive:
            hint_screen()
    if key == "m":
        # check location correct?
        pass
    elif key in ["Right", "Left", "Up", "Down"]:
        dotnew = nextdot(dot, key, number)
        colourchangeplayer(dot, dotnew, True)
        dot = dotnew
win.getMouse()
win.close()