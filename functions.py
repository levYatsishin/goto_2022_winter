from piece_class import ChessPiece


def start_game(board):
    mapped_board = []
    for idx_row, row in enumerate(board):
        mapped_row = []
        for idx_column, square in enumerate(row):
            if square != 0:
                type = square.split("_")[0]
                color = 0 if square.split("_")[1] == "w" else 1
                mapped_row.append(ChessPiece(type, color, (idx_row, idx_column)))
            else:
                mapped_row.append(0)
        mapped_board.append(mapped_row)

    return mapped_board


def draw_board(board):
    board_str = " " + "_" * 31 + "\n"
    for row_idx, row in enumerate(board):
        row_str = "|"
        for square in row:
            if square != 0:
                row_str += "_" + square.draw()
            else:
                row_str += "__"
            row_str += "_|"

        board_str += row_str + f" {8 - row_idx}\n"

    for letter_ord in range(97, 97 + 8):
        board_str += f"  {chr(letter_ord)} "
    return board_str


def check_input(input_):
    if len(input_.split()) != 2:
        return False

    origin, move = input_.split()[0], input_.split()[1]

    if not (origin[0] in [chr(x) for x in range(97, 97 + 8)]) or not (origin[1] not in [x for x in range(1, 9)]):
        return False
    if not (move[0] in [chr(x) for x in range(97, 97 + 8)]) or not (move[1] not in [x for x in range(1, 9)]):
        return False

    return True


def make_a_move(origin, move, board):
    origin_place = (8 - int(origin[1]), abs(97 - ord(origin[0])))
    new_place = (8 - int(move[1]), abs(97 - ord(move[0])))

    if board[origin_place[0]][origin_place[1]] == 0:
        return board, "Blank square selected!"

    board = board[origin_place[0]][origin_place[1]].move(board, new_place)
    return board, f"You moved your {origin} {board[new_place[0]][new_place[1]].type} to {move}"
