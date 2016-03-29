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
    two_1 = np.random.randint(16)
    two_2 = two_1
    while two_2==two_1:
        two_2 = np.random.randint(16)
    board[two_1]=2
    board[two_2]=2

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
            if (b==0 and a!=0) or a==b:
                lm.append(MOVE_UP)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for down
    for i in range(3):
        for a,b in zip(board_unrolled[i], board_unrolled[i+1]):
            if (b==0 and a!=0) or a==b:
                lm.append(MOVE_DOWN)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for left
    for i in range(3,0,-1):
        for a,b in zip(board_unrolled[:,i], board_unrolled[:,i-1]):
            if (b==0 and a!=0) or a==b:
                lm.append(MOVE_LEFT)
                flag = True
                break
        if flag:
            break

    flag = False

    #check for right
    for i in range(3):
        for a,b in zip(board_unrolled[:,i], board_unrolled[:,i+1]):
            if (b==0 and a!=0) or a==b:
                lm.append(MOVE_RIGHT)
                flag = True
                break
        if flag:
            break

    return lm

def perform_turn(board, move):
    """
    perform the move and return a new board
    """

    if move not in legal_moves(board):
        return (board, TURN_ILLEGAL)

    board_unrolled = board.reshape([4,4])

    # TODO: perform move

    if not legal_moves[board]:
        return (board, TURN_GAME_OVER)
    else:
        return (board, TURN_OK)
    

board = gen_board()
print_board(board)
print(legal_moves(board))
