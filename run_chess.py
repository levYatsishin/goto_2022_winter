from functions import start_game, draw_board, make_a_move, check_input

game_board = [[f"rook_b", f"knight_b", f"bishop_b", f"queen_b", f"king_b", f"bishop_b", f"knight_b", f"rook_b"],
              [f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b"],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              ["pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w"],
              ["rook_w", "knight_w", "bishop_w", "queen_w", "king_w", "bishop_w", "knight_w", "rook_w"]]


# TODO: win conditions
# TODO: ban moves which threatens the king on the next move


def play_chess():
    # 0 - white; 1 - black
    current_color = 0
    board = start_game(game_board)

    c_c = "White" if current_color == 0 else "Black"
    print(draw_board(board))
    print(f"{c_c}'s turn!")
    while True:
        move = input(f"Make your move(eg. d2 d4): ")
        if check_input(move):
            board, message, current_color = make_a_move(*move.split(), board, current_color)
        else:
            message = "Invalid input!"

        print(draw_board(board))
        print(message)


play_chess()
