# uses minimax to look ahead

import sys
from functools import partial
from game import *
import interactive_game

def compute_score(board, res=TURN_OK):
    score = 0

    zero_count = 0
    for i,elem in enumerate(board):
        if elem==0:
            zero_count += 1
        elif i==0:
            score += elem**5
        elif i==1 or i==4:
            score += elem**4
        elif i==2 or i==5 or i==8:
            score += elem**2
        elif i==3 or i==6 or i==9 or i==12:
            score += elem**1

    #score = score * zero_count * 0.3

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
