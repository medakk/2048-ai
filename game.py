#!/usr/bin/python3

import numpy as np

# Legal Moves
MOVE_UP    = 0
MOVE_DOWN  = 1
MOVE_LEFT  = 2
MOVE_RIGHT = 3

# Turn results
TURN_OK        = 0
TURN_ILLEGAL   = 1
TURN_GAME_OVER = 2

def print_board(board):
    """
    takes an unrolled (1*16) 2048 game board
    and prints it
    """
    unrolled_board = board.reshape([4,4])
    for row in unrolled_board:
        print("|" + "------|"*4)
        row_str="| {:>4d} | {:>4d} | {:>4d} | {:>4d} |".format(*row).replace("   0", "    ")
        print(row_str)
    print("|" + "------|"*4)

def gen_board():
    """
    generates a game board (np array with 16 elements)
    all squares are empty(0) except two squares
    """
    board = np.zeros(16, dtype=int)

    # randomly add two random stuff
    board = insert_random(insert_random(board))

    return board

def is_board_valid(board):
    """
    returns False if the board contains an element that is
    neither a power of 2 nor 0

    returns False if the board doesn't conform to required
    sized
    """

    if board.shape != (16,):
        return False

    for elem in board:
        if elem==0:
            continue
        if 2**np.int(np.log2(elem)) != elem:
            return False
    return True

def can_collapse(row):
    """
    returns true if the given row
    can be collapsed to the left

    can also be a column
    """

    for a,b in zip(row[1:], row):
        if a==0:
            continue
        if b==0 or a==b:
            return True
    return False

def can_collapse_r(row):
    """
    similar to can_collapse, but
    in the reversed direction
    """
    row_r = row[::-1]
    return can_collapse(row_r)

lm_cache_board_id = None
lm_cache_result = None
def legal_moves(board):
    """
    returns a list of legal moves
    for the given board
    """
    global lm_cache_board_id, lm_cache_result
    
    if lm_cache_board_id==id(board):
        return lm_cache_result

    lm_cache_board_id = id(board)

    lm = []
    board_unrolled = board.reshape([4,4])

    if np.any(np.apply_along_axis(can_collapse, 0, board_unrolled)):
        lm.append(MOVE_UP)

    if np.any(np.apply_along_axis(can_collapse_r, 0, board_unrolled)):
        lm.append(MOVE_DOWN)

    if np.any(np.apply_along_axis(can_collapse, 1, board_unrolled)):
        lm.append(MOVE_LEFT)

    if np.any(np.apply_along_axis(can_collapse_r, 1, board_unrolled)):
        lm.append(MOVE_RIGHT)

    lm_cache_result = lm

    return lm

def collapse(board_u):
    """
    takes a row/column of the board
    and collapses it to the left
    """
    i = 1
    limit = 0
    while i < 4:
        if board_u[i]==0:
            i += 1
            continue

        up_index = i-1
        curr_index = i
        while up_index>=0 and board_u[up_index]==0:
            board_u[up_index] = board_u[curr_index]
            board_u[curr_index] = 0
            up_index -= 1
            curr_index -= 1

        if up_index >= limit and board_u[up_index]==board_u[curr_index]:
            board_u[up_index] *= 2
            board_u[curr_index] = 0
            limit = curr_index

        i += 1

    return board_u

def collapse_r(board_u):
    """
    like collapse, but in the opposite direction
    ie: folds to the right
    """
    rev_board_u = board_u[::-1]
    return collapse(rev_board_u)[::-1]

def perform_turn(board_u, move, ins_random=True, skip_check=False):
    """
    perform the move and return a new board
    if ins_random==False, a new random cell
    is not added.
    """

    if not skip_check:
        if move not in legal_moves(board_u):
            return board_u, TURN_ILLEGAL

    board = board_u.reshape([4,4])

    if move==MOVE_UP:
        np.apply_along_axis(collapse, 0, board)
    elif move==MOVE_DOWN:
        np.apply_along_axis(collapse_r, 0, board)
    elif move==MOVE_LEFT:
        np.apply_along_axis(collapse, 1, board)
    elif move==MOVE_RIGHT:
        np.apply_along_axis(collapse_r, 1, board)

    board_u = board.reshape((16,))
    if ins_random:
        board_u = insert_random(board_u)

    if skip_check:
        return (board_u, TURN_OK)
    if not legal_moves(board_u):
        return (board_u, TURN_GAME_OVER)
    else:
        return (board_u, TURN_OK)

def insert_random(board):
    not_zero = board!=0
    if np.all(not_zero):
        return board

    r_ind = np.random.randint(16)
    while board[r_ind]!=0:
        r_ind = (r_ind + 1)%16

    # 90% chance of 2
    if np.random.randint(10)==0:
        r_val = 4
    else:
        r_val = 2

    board[r_ind] = r_val
    return board
