import chess
import chess.svg
import random

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
            print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 100
    }

    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            evaluation += value if piece.color == chess.WHITE else -value

    return evaluation

def test_evaluate_board():

    # Testovacia pozícia
    test_position = "r1b1kbnr/pp1p1p1p/n1p5/4p3/3PP2B/8/PPP2PPP/RN1QKBNR b KQkq - 2 5"
    board = chess.Board(fen=test_position)

    # Vypísanie danej pozície
    print("Pôvodná pozícia:")
    print(board)

    # Hodnotenie pozíce
    score = evaluate_board(board)
    print(f"\nEval pozície: {score}")

def get_best_move(board):
    legal_moves = list(board.legal_moves)
    
    if not legal_moves:
        return chess.Move.null()  # Defaultný ťah pre situáciu, keď neni žiadny legálny ťah
    
    best_move = None
    best_eval = float('-inf')

    for move in legal_moves:
        board.push(move)
        eval = evaluate_board(board)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move

def test_get_best_move():

    # Testovacia pozícia
    test_position = "r1b1kbnr/pp1p1p1p/n1p5/4p3/3PP2B/8/PPP2PPP/RN1QKBNR b KQkq - 2 5"
    board = chess.Board(fen=test_position)

    print("Pôvodná pozícia:")
    print(board)

    # Získanie najlepšieho ťahu a zahranie
    best_move = get_best_move(board)
    print(f"\nNajlepší ťah: {best_move.uci()}")
    board.push(best_move)

    # Vypísanie pozície po najlepšom ťahu
    print("\nŠachovnica po najlepšom ťahu:")
    print(board)

def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            move = get_best_move(board)
            print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

#if __name__ == "__main__":
    #play_chess()

#play_chess_random_bot()
#test_evaluate_board()
#test_get_best_move()
    
play_chess()
