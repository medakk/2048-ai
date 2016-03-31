from game import *

KEYS = "wsad"

board = gen_board()
while True:
    print_board(board)

    lm = [KEYS[i] for i in legal_moves(board)]
    print("LEGAL: {}".format(lm))

    response = input()
    board,res = perform_turn(board, KEYS.index(response))

    if res==TURN_ILLEGAL:
        print("ILLEGAL MOVE! Press enter.")
        input()
    elif res==TURN_GAME_OVER:
        print("Whoops. Dead :)")
        break
