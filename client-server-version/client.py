from chess_functions import check_input
import requests


def join_game(game_id='default'):
    server_request = {'action': 'join', 'room': game_id}
    server_answer = requests.post('http://localhost:5000/chess', json=server_request).json()
    print(server_answer["board"] + "\n" + server_answer["message"])
    return server_answer["color"]


def play(your_color):
    win = False

    while not win:
        move = input(f"Make your move(eg. d2 d4): ")
        while not check_input(move):
            print("Invalid input!")
            move = input(f"Make your move(eg. d2 d4): ")

        server_request = {'action': 'move', 'color': your_color, 'move': move}
        server_answer = requests.post('http://localhost:5000/chess', json=server_request).json()

        print(server_answer["board"] + "\n" + server_answer["message"])


color = join_game()
play(color)
