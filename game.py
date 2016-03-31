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
    all squares are empty(0) except two squares, which are filled
    with twos
    """
    board = np.zeros(16, dtype=int)

    # randomly add two random twos.
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
        

def legal_moves(board):
    """
    returns a list of legal moves
    for the given board
    """
    lm = []
    board_unrolled = board.reshape([4,4])
    flag = False

    #check for up
    for i in range(3, 0, -1):
        for a,b in zip(board_unrolled[i], board_unrolled[i-1]):
            if a==0:
                continue
            if b==0 or a==b:
                lm.append(MOVE_UP)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for down
    for i in range(3):
        for a,b in zip(board_unrolled[i], board_unrolled[i+1]):
            if a==0:
                continue
            if b==0 or a==b:
                lm.append(MOVE_DOWN)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for left
    for i in range(3,0,-1):
        for a,b in zip(board_unrolled[:,i], board_unrolled[:,i-1]):
            if a==0:
                continue
            if b==0 or a==b:
                lm.append(MOVE_LEFT)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for right
    for i in range(3):
        for a,b in zip(board_unrolled[:,i], board_unrolled[:,i+1]):
            if a==0:
                continue
            if b==0 or a==b:
                lm.append(MOVE_RIGHT)
                flag = True
                break
        if flag:
            break

    return lm

def collapse(board_u):
    """
    takes a row/column of the board
    and collapses it
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

def perform_turn(board_u, move):
    """
    perform the move and return a new board
    """

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
    board_u = insert_random(board_u)
    
    if not legal_moves(board_u):
        return (board_u, TURN_GAME_OVER)
    else:
        return (board_u, TURN_OK)

def insert_random(board):
    not_zero = board!=0
    if np.all(not_zero):
        return board

    # get the indices of empty squares
    # TODO: beautify this
    empty_indices = list(map(lambda b: b[0], filter(lambda b : not b[1], enumerate(not_zero))))
    
    r_val = np.random.choice([2,4])
    r_ind = np.random.choice(empty_indices)

    board[r_ind] = r_val
    return board
