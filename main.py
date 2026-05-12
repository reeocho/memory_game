# import
from random import *
from graphics import *
from time import *

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
    width = 50 * (number+1)
    win = GraphWin(game_code, width, width)
    
    # Dictionary to store dots
    dots = []
    dot_id = 0

    for i, x in enumerate(range(spacing, width, spacing)):
        for j, y in enumerate(range(spacing, width, spacing)):
            grid_id = f"{i}-{j}"
            globals()['var%s' % grid_id] = Circle(Point(x, y), 2)
            globals()['var%s' % grid_id].draw(win)
            
            dots.append(grid_id)
            
    return win, dots


    
main()
win, dots = create_dot_grid("Dot Grid", 5)
print(dots)
win.getMouse()
win.close()