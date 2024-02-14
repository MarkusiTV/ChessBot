import SimpleChess_0_2
import SimpleChess_0_3
import SimpleChess_0_4
import SimpleChess_0_5

import chess

hier = input("Koľko chceš aby hrali hier?: ")

ww = 0
d = 0
wb = 0

def play_chess_bot_vs_bot(board, bot1_function, bot2_function):
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = bot1_function(board)
        else:
            move = bot2_function(board)

        board.push(move)

    return board.result()

for i in range(int(hier)):
    board = chess.Board()
    result = play_chess_bot_vs_bot(board, SimpleChess_0_2.play_chess_opponent_bot, SimpleChess_0_5.get_best_move)

    print("Koniec hry")
    print("Výsledok: " + result)

    if result == "1-0":
        ww += 1
        print("Vyhral bot 1\n")
    elif result == "0-1":
        print("Vyhral bot 2\n")
        wb += 1
    else:
        print("Remíza\n")
        d += 1

print("Bot 1 vyhral: " + str(ww))
print("Bot 2 vyhral: " + str(wb))
print("Remíza: " + str(d))
