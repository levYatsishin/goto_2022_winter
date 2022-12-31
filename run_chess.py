from functions import start_game, draw_board, make_a_move, check_input

game_board = [[f"rook_b", f"knight_b", f"bishop_b", f"queen_b", f"king_b", f"bishop_b", f"knight_b", f"rook_b"],
              [f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b"],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              ["pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w"],
              ["rook_w", "knight_w", "bishop_w", "queen_w", "king_w", "bishop_w", "knight_w", "rook_w"]]

# TODO: move restrictions


def play_chess():
    current_color = 0

    board = start_game(game_board)
    print(draw_board(board))
    print("White's turn!")
    while True:
        move = input(f"Make your move(eg. e2 e4): ")

        if check_input(move):
            board, message, current_color = make_a_move(*move.split(), board, current_color)
        else:
            message = "Invalid input!"

        print(draw_board(board))
        print(message)


play_chess()
