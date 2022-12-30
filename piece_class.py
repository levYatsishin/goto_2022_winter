import itertools


class ChessPiece:

    def __init__(self, type, color):
        # possible places to move to (all_x, all_y) in a relative coordinate system; 0 – current place
        possible_moves = {"king": [[p[0] for p in itertools.product([-1, 0, 1], repeat=2)],
                                   [p[1] for p in itertools.product([-1, 0, 1], repeat=2)]],
                          "queen": ([x for x in range(-7, 8)] + [x for x in range(-7, 8)] + [0 for _ in range(15)],
                                    [x for x in range(-7, 8)] + [0 for _ in range(15)] + [x for x in range(-7, 8)]),
                          "rook": ([0 for _ in range(15)] + [x for x in range(-7, 8)],
                                   [x for x in range(-7, 8)] + [0 for _ in range(15)]),
                          "bishop": ([x for x in range(-7, 8)],
                                     [x for x in range(-7, 8)]),
                          "knight": (list(itertools.chain.from_iterable([[x, x] for x in range(-2, 3)])),
                                     list(itertools.chain.from_iterable(
                                         [[x, -x] for x in [1, 2, 0]] + [[x, -x] for x in [2, 1]]))),
                          "pawn": ([0], [1])}

        self.color = color
        self.type = type
        self.movements = possible_moves[type]

    def move(self, board, move):
        pass
        # return new_board

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
