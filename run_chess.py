from piece_class import ChessPiece


def start_game(board):
    mapped_board = []
    for row in board:
        mapped_row = []
        for square in row:
            if square != 0:
                type = square.split("_")[0]
                color = 0 if square.split("_")[1] == "w" else 1
                mapped_row.append(ChessPiece(type, color))
            else:
                mapped_row.append(0)
        mapped_board.append(mapped_row)

    return mapped_board


def draw_board(board):
    board_str = " "+"_"*31+"\n"
    for row_idx, row in enumerate(board):
        row_str = "|"
        for square in row:
            if square != 0:
                row_str += "_" + square.draw()
            else:
                row_str += "__"
            row_str += "_|"

        board_str += row_str + f" {row_idx+1}\n"

    for letter_ord in range(97, 97+8):
        board_str += f"  {chr(letter_ord)} "
    return board_str


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


play_chess()
