import itertools


class ChessPiece:

    def __init__(self, type, color, place, first_move=True):
        # possible places to move to (all_x, all_y) in a relative coordinate system; 0 – current place
        possible_moves = {"king": [[p[0] for p in itertools.product([-1, 0, 1], repeat=2)],
                                   [p[1] for p in itertools.product([-1, 0, 1], repeat=2)]],
                          "queen": ([x for x in range(-7, 8)] + [x for x in range(-7, 8)] + [0 for _ in range(15)],
                                    [x for x in range(-7, 8)] + [0 for _ in range(15)] + [x for x in range(-7, 8)]),
                          "rook": ([0 for _ in range(15)] + [x for x in range(-7, 8)],
                                   [x for x in range(-7, 8)] + [0 for _ in range(15)]),
                          "bishop": ([x for x in range(-7, 8)]+[x for x in range(8, -7, -1)]+[x for x in range(-8, 7)],
                                     [x for x in range(-7, 8)]+[x for x in range(-8, 7)]+[x for x in range(8, -7, -1)]),
                          "knight": (list(itertools.chain.from_iterable([[x, x] for x in range(-2, 3)])),
                                     list(itertools.chain.from_iterable(
                                         [[x, -x] for x in [1, 2, 0]] + [[x, -x] for x in [2, 1]]))),
                          "pawn": ([0], [1])}

        self.color = color
        self.type = type
        self.place = place
        self.movements = possible_moves[type]
        self.first_move = first_move

    def check_valid_move(self, board, new_place):
        valid, message = False, "This piece cant move this way!"
        c = 0
        print(self.place, new_place)
        change = (new_place[0] - self.place[0], new_place[1] - self.place[1])

        if self.type == "pawn":
            change = (abs(change[0]), abs(change[1]))
            if change == (0, 2) and self.first_move:
                self.first_move = False
                valid, message = True, ""
            if change == (1, 1) and get_square(board, new_place) != 0:
                if get_square(board, new_place).color != self.color:
                    valid, message = True, ""

        for possible_move in zip(self.movements[0], self.movements[1]):
            if change == possible_move:
                valid, message = True, ""
                c += 1
        if c == 0:
            return valid, message

        if get_square(board, new_place) != 0:
            if get_square(board, new_place).color == self.color:
                valid, message = False, "You can't eat your own pieces, you cruel dictator! :("

        if self.type != "knight":
            # blocks on x axis
            if change[1] == 0:
                step = 1 if change[0] < 0 else -1
                for x in range(change[0]+step, 0, step):
                    checking_place = [self.place[0]+x, self.place[1]]
                    print(change, checking_place)

                    if get_square(board, checking_place):
                        valid, message = False, "You can't move this way, the passage is blocked."

            # blocks on y axis
            elif change[0] == 0:
                step = 1 if change[1] < 0 else -1
                for x in range(change[1]+step, 0, step):
                    checking_place = [self.place[0], self.place[1]+x]
                    print(change, checking_place)

                    if get_square(board, checking_place):
                        valid, message = False, "You can't move this way, the passage is blocked."

            # blocks on diagonals
            # TODO: implement
            else:
                step_x = 1 if change[0] < 0 else -1
                step_y = 1 if change[1] < 0 else -1
                for x in range(change[0]+step_x, 0, step_x):
                    for y in range(change[1] + step_y, 0, step_y):
                        checking_place = [self.place[0]+x, self.place[1]+y]
                        print(change, checking_place)

                        if get_square(board, checking_place):
                            valid, message = False, "You can't move this way, the passage is blocked."

        return valid, message

    def move(self, board, new_place):
        new_board = board[:]

        new_board[7-self.place[1]][self.place[0]] = 0
        new_board[7-new_place[1]][new_place[0]] = ChessPiece(self.type, self.color, new_place, False)

        return new_board

    def draw(self):
        type2string = {"king_0": "♔",
                       "queen_0": "♕",
                       "rook_0": "♖",
                       "bishop_0": "♗",
                       "knight_0": "♘",
                       "pawn_0": "♙",
                       "king_1": "♚",
                       "queen_1": "♛",
                       "rook_1": "♜",
                       "bishop_1": "♝",
                       "knight_1": "♞",
                       "pawn_1": "♟",
                       }
        return type2string[f"{self.type}_{self.color}"]


def get_square(board, loc):
    return board[7-loc[1]][loc[0]]