from functions import start_game, draw_board, make_a_move, check_input
import os

game_board = [["rook_b", "knight_b", "bishop_b", "queen_b", "king_b", "bishop_b", "knight_b", "rook_b"],
              ["pawn_b", "pawn_b", "pawn_b", "pawn_b", "pawn_b", "pawn_b", "pawn_b", "pawn_b"],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              ["pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w"],
              ["rook_w", "knight_w", "bishop_w", "queen_w", "king_w", "bishop_w", "knight_w", "rook_w"]]


def play_chess():
    board = start_game(game_board)
    print(draw_board(board))
    while True:
        move = input("Your move(eg. d2 d4): ")
        if check_input(move):
            board, message = make_a_move(*move.split(), board)
        else:
            message = "Invalid input!"
        print(draw_board(board))
        print(message)


play_chess()
