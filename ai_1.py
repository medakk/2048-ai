# This AI lives in the moment.
# Chooses the move that maximizes the
# number of "big" numbers in the board
# in a given moment

from game import *
import interactive_game

def compute_score(board):
    score = 0
    for elem in board:
        score += elem*elem
    return score

def ai_1_compute_func(board, lm):
    possible_moves = []
    for move in lm:
        new_board, res = perform_turn(board.copy(), move, ins_random=False)
        score = compute_score(new_board)

        possible_moves.append((score,move))

    possible_moves.sort()
    return possible_moves[-1][1]

interactive_game.start(ai_1_compute_func)
