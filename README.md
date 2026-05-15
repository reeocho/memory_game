# Memory Game
In this project I wanted to make a memory game (originally began as trying to make a wordle/hangman-esque logic game and wordle reverse solver in one - using the correct letter/placements predetermined "guesses" given to the player to solve - but progressed to a more visual memory game) that has a similar format and play style to snake. To achieve this I used the graphics py library to more efficiently create a game window.

## Process
- Experimented using a webpage for the game in the beginning, but ultimately decided on using python (and the graphics.py library)
- Originally https://github.com/reeocho/wordle-solver

## Challenges/problems
Some challenges or problems I faced when creating the game:
- Randomly generating the maze (this was pretty difficult ;-;), ultimately managed to work out limitations at each point in the maze even with varying number of dots by using divisibility of each point's index.
- Getting the dots to move, which I managed to do by manipulating the index (same way as maze generation)

## How to play
- Select settings on the main page. Currently changeable settings include:
    - 
- When the game starts, the correct path is shown on the screen, one dot at a time.