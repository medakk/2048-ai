# Creates an interactive game, given the
# function used to compute the next move

from game import *

DIRECTIONS = "↑↓←→"

def start(compute_func):
    """
    Simulates the game
    compute_func takes a board and a list
    of legal moves s and returns a move
    """

    board = gen_board()
    turn = 1
    while True:
        print("\nTurn:", turn)
        print_board(board)

        lm = legal_moves(board)
        print("Legal: ", *[DIRECTIONS[i] for i in lm])

        chosen_move = compute_func(board,lm)
        print("Chosen: " + DIRECTIONS[chosen_move])

        board, res = perform_turn(board, chosen_move)

        turn += 1
        if res==TURN_ILLEGAL:
            print("ILLEGAL MOVE! Press enter.")
            turn -= 1
            input()
        elif res==TURN_GAME_OVER:
            print("\nTurn:", turn)
            print_board(board)
            print("Whoops. Dead :)")
            break
