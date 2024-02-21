import chess
import random

def play_chess_random_bot():
    color = input("Zadaj farbu: white/black")
    board = chess.Board()
    if color.lower() == "white":
        color = chess.WHITE
    elif color.lower() == "black":
        color = chess.BLACK
    else:
        print("Neplatná farba!")
        return 1

    while not board.is_game_over() and (color == chess.WHITE or color == chess.BLACK):
        print(board)
        if board.turn == color:
            move = input("Tvoj ťah (vo formáte a2a4 alebo K pre ukončenie): ")
            move = chess.Move.from_uci(move.lower())
        else:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves)
            print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

def play_chess_opponent_bot(board):
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    print(f"Botov pohyb - random: {move.uci()}")
    return move

#play_chess_random_bot()
#play_chess_opponent_bot(board=chess.Board())
