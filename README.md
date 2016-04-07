# 2048_ai

## Play it yourself
To play the game yourself, run:
```
python3 human.py
```

## Watch an AI play the game
To run any of the different AIs, run any of the provided AI scripts
```
python3 ai_2.py
python3 ai_stochastic.py
```

## Write your own AI
The basic steps to write an AI for the game are

* Create a script with the following imports
```
from game import *
import interactive_game
```
* Write a function to compute the next move. This is a function that takes the current board and a list of legal moves as arguments, and returns a move. The current board is a 1D numpy array with 16 elements. The legals moves are a list of enums defined in game.py

* Run the game with
```
interactive_game.start(your_compute_function)
```

For an example, look at ai_1.py, which chooses the move that maximizes the sum of the square of the elements.

