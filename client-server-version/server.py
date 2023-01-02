from flask import Flask, request, jsonify
from random import shuffle
from chess_functions import start_game, make_a_move, draw_board

app = Flask(__name__)

game_board = [[f"rook_b", f"knight_b", f"bishop_b", f"queen_b", f"king_b", f"bishop_b", f"knight_b", f"rook_b"],
              [f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b", f"pawn_b"],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 0, 0, 0, ],
              ["pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w", "pawn_w"],
              ["rook_w", "knight_w", "bishop_w", "queen_w", "king_w", "bishop_w", "knight_w", "rook_w"]]
rooms = {'default': {"board": start_game(game_board), "players": ["black", "white"]}}


@app.route('/chess', methods=['POST'])
def server():
    if request.method == 'POST':
        answer = {}
        client_input = request.get_json(force=True)

        if client_input["action"] == "join":
            room_id = "default"
            shuffle(rooms[room_id]['players'])
            color = rooms[room_id]['players'].pop(0)

            answer = {"board": draw_board(rooms[room_id]["board"]),
                      "color": color,
                      "message": f"You successfully joined the game!\nYour color is {color}"}

        elif client_input["action"] == 'move':
            move = client_input["move"]
            color = 0 if client_input["color"] == "white" else 1

            board, message, current_color, win = make_a_move(*move.split(), rooms['default']["board"], color)
            answer = {"board": draw_board(board), "message": message, "win": win}

        return jsonify(answer)


if __name__ == '__main__':
    app.run(debug=True)
