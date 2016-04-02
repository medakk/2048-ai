# uses minimax to look ahead

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

def insert_worst_random(board):
    worst_i = -1
    worst_score = 2**16
    replace_with = 0
    for i in range(16):
        if board[i]!=0:
            continue

        board[i] = 4
        score,move = get_best_move(board)

        if score<worst_score:
            worst_score = score
            worst_i = i
            replace_with = 4

        board[i] = 2
        score,move = get_best_move(board)

        if score<worst_score:
            worst_score = score
            worst_i = i
            replace_with = 2

        board[i] = 0

    if worst_i==-1:
        return board
    else:
        board[i] = replace_with
        return board

def get_best_move(board):
    lm = legal_moves(board)
    if lm == []:
        return (compute_score(board,TURN_ILLEGAL), -1)

    best_move = None
    for move in lm:
        new_board, res = perform_turn(board.copy(), move, ins_random=False)
        score = compute_score(new_board, res)

        score_move = (score,move)
        if best_move==None:
            best_move = score_move
        elif best_move<score_move:
            best_move = score_move

    return best_move

def minimax(board, lm=None, depth=5):
    if depth==1:
        return get_best_move(board)

    if not lm:
        lm = legal_moves(board)

    if lm == []:
        return (compute_score(board,TURN_ILLEGAL), -1)

    best_move = None
    for move in lm:
        new_board, res = perform_turn(board.copy(), move, ins_random=False, skip_check=True)
        score = compute_score(new_board)

        new_board = insert_random(new_board)
        next_score, next_move = minimax(new_board.copy(), depth=depth-1)
        score += next_score

        score_move = (score,move)
        if best_move==None:
            best_move = score_move
        elif best_move<score_move:
            best_move = score_move

    return best_move
               
turn = 0
depth = 3
def ai_2_compute_func(board, lm):
    global turn
    global depth
    turn += 1
    depth = 3
            
    next_score, next_move = minimax(board, lm=lm, depth=depth) 
    return next_move

interactive_game.start(ai_2_compute_func)
