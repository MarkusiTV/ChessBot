import chess
import chess.svg
import random

docs = "https://python-chess.readthedocs.io/en/latest/"
other_links = ["https://www.youtube.com/watch?v=Gm1ekmknalw","https://www.youtube.com/watch?v=Hdr64lKQ3e4", "https://www.youtube.com/watch?v=w4FFX_otR-4"]

print("Pre pomoc si prečítaj: ", docs)

def play_chess_random_bot():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves)
            print(f"Bot zahral: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

if __name__ == "__main__":
    play_chess_random_bot()
