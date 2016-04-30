# uses minimax to look ahead

import sys
from functools import partial
from game import *
import interactive_game

def compute_score(board, res=TURN_OK):
    score = board[0]**5 \
          + board[1]**4 + board[4]**4 \
          + board[2]**2 + board[5]**2 + board[8]**2 \
          + board[3]    + board[6]    + board[9]    + board[12]

    if res==TURN_GAME_OVER or res==TURN_ILLEGAL:
        return -score

    return score

def minimax(board, lm=None, depth=5):
    if not lm:
        lm = legal_moves(board)

    if lm == []:
        return (compute_score(board,TURN_ILLEGAL), -1)

    best_move = None
    for move in lm:
        new_board, res = perform_turn(board.copy(), move, ins_random=False, skip_check=True)
        score = compute_score(new_board)

        if depth != 1:
            new_board = insert_random(new_board)
            next_score, next_move = minimax(new_board.copy(), depth=depth-1)
            score += next_score

        score_move = (score,move)
        if best_move==None:
            best_move = score_move
        elif best_move<score_move:
            best_move = score_move

    return best_move
               
def ai_2_compute_func(board, lm, depth):
    next_score, next_move = minimax(board, lm=lm, depth=depth) 
    return next_move

if __name__=="__main__":
    if len(sys.argv)>=2:
        depth = int(sys.argv[1])
    else:
        depth = 3

    interactive_game.start(partial(ai_2_compute_func, depth=depth))
