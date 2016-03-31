# this ai just does a random legal move every time

from game import *
import random
import interactive_game

def ai_stochastic_compute_func(board, lm):
    return random.choice(lm)

interactive_game.start(ai_stochastic_compute_func)
