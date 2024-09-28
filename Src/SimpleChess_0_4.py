import chess
import random

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3.5,
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

def get_best_move(board):
    legal_moves = list(board.legal_moves)
    best_move = None
    best_eval = float('-inf') if board.turn == chess.WHITE else float('inf')

    for move in legal_moves:
        board.push(move)
        eval = minimax(board, 3, False) #if board.turn == chess.WHITE else True)  # Hĺbka (napr 2) - v minimaxe je chyba, opraviť
        eval += random.randint(1,50)/500
        board.pop()

        '''
        if eval < best_eval:
                best_eval = eval
                best_move = move
        '''

        if board.turn == chess.BLACK:
            if eval < best_eval:
                best_eval = eval
                best_move = move
        elif board.turn == chess.WHITE:
            if eval > best_eval:
                best_eval = eval
                best_move = move

    print("Eval: ", best_eval)
    return best_move

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)
    f = open("fajl.txt", "a")

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            print(move)
            f.write(str(move))
            f.write("\n")
            board.push(move)
            eval = minimax(board, depth - 1, False)
            f.write(str(eval))
            f.write("\n")
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            print(move)
            f.write(str(move))
            f.write("\n")
            board.push(move)
            eval = minimax(board, depth - 1, True)
            f.write(str(eval))
            f.write("\n")
            print(eval, "\n")
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

def play_chess():
    color = input("Zadaj farbu: white/black")
    board = chess.Board()
    if color.lower() == "white":
        color = chess.WHITE
    elif color.lower() == "black":
        color = chess.BLACK
    else:
        print("Neplatná farba!")
        return 1

    while not board.is_game_over():
        print(board)
        if board.turn == color:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            move = get_best_move(board)
            print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

play_chess()