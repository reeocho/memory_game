# import
from random import *
from graphics import *
from time import *


def text_create(text, settings):
    texttodraw = Text(Point(200, 50), text)
    texttodraw.setTextColor("red")
    texttodraw.draw(settings)
    sleep(5)
    texttodraw.undraw()

def check_location(maze, dot, iteration):
    if dots.index(dot) == maze[iteration]:
        return True
    else:
        return False

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
    difficulty1 = Rectangle(Point(110, 50), Point(185, 100))
    difficulty1.label = Text(Point(150, 75), "Easy")
    difficulty1.label.draw(settings)
    difficulty1.draw(settings)
    difficulty2 = Rectangle(Point(210, 50), Point(285, 100))
    difficulty2.label = Text(Point(250, 75), "Medium")
    difficulty2.label.draw(settings)
    difficulty2.draw(settings)
    difficulty3 = Rectangle(Point(310, 50), Point(385, 100))
    difficulty3.label = Text(Point(350, 75), "Hard")
    difficulty3.label.draw(settings)
    difficulty3.draw(settings)

    e = Entry(Point(250, 150), 30)
    e.setText("Username")
    e.draw(settings)
    name = e.getText()
    while True:
        if difficulty1.getP1().getX() < settings.getMouse().getX() < difficulty1.getP2().getX() and \
           difficulty1.getP1().getY() < settings.getMouse().getY() < difficulty1.getP2().getY():
            number = 3
            settings.close()
            break
        if difficulty2.getP1().getX() < settings.getMouse().getX() < difficulty2.getP2().getX() and \
           difficulty2.getP1().getY() < settings.getMouse().getY() < difficulty2.getP2().getY():
            number = 5
            settings.close()
            break
        if difficulty3.getP1().getX() < settings.getMouse().getX() < difficulty3.getP2().getX() and \
           difficulty3.getP1().getY() < settings.getMouse().getY() < difficulty3.getP2().getY():
            number = 7
            settings.close()
            break
        else:
            text_create("Choose Difficulty", settings)
    return name, number

def create_dot_grid(game_code, number):
    spacing = 50
    width = 50 * (number+1)
    win = GraphWin(game_code, width, width)
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

def success_screen(time):
    background = Rectangle(Point(0,0), Point(win.getWidth(), win.getHeight())).draw(win)
    background.setFill("white")
    text = Text(Point(win.getWidth()/2, win.getHeight()/2), "Win!")
    text.draw(win)
    text_time = Text(Point(win.getWidth()/2, win.getHeight()/2 + 30), f"Time: {time:.2f} seconds")
    text_time.draw(win)
    pass

def failscreen():
    background = Rectangle(Point(0,0), Point(win.getWidth(), win.getHeight())).draw(win)
    background.setFill("white")
    text = Text(Point(win.getWidth()/2, win.getHeight()/2), "Fail!")
    text.draw(win)
    pass

iteration = 0
name, number = main()
maze = createmaze(number)

win, dots = create_dot_grid("Dot Grid", number)
first_animation(maze)
dots[0].undraw()
dots[0].setFill("green")
dots[0].draw(win)
dot = dots[0]
starttime = time()
while True:
    key = win.checkKey()
    if iteration == len(maze):
        success_screen(time()-starttime)
        break
    if key == "q":
        win.getMouse()
        win.close()
        break
    if key == "m":
        if check_location(maze, dot, iteration):
            iteration += 1
            print(iteration)
        else:
            failscreen()
        print(dot)
    elif key in ["Right", "Left", "Up", "Down"]:
        dotnew = nextdot(dot, key, number)
        colourchangeplayer(dot, dotnew, True)
        dot = dotnew

win.getMouse()
win.close()