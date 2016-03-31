from game import *
import interactive_game

KEYS = "wsad"

def human_compute_func(board, lm):
    while True:
        response = input("> ")
        if len(response)!=1 or response not in KEYS:
            print("Illegal move.")
        else:
            break

    # assumes that MOVE_UP=0, MOVE_DOWN=1...
    return KEYS.index(response)

print("Use WSAD")
interactive_game.start(human_compute_func)
