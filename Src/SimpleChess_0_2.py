import chess
import chess.svg
import random

def play_chess_random_bot():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Tvoj ťah (vo formáte a2a4 alebo K pre ukončenie): ")
            move = chess.Move.from_uci(move.lower())
        else:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves)
            print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

play_chess_random_bot()
