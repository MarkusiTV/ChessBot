import chess

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

#Funkcia na vybranie pohybu => Proti botom 
def get_best_move(board):
    legal_moves = list(board.legal_moves)
    
    if not legal_moves:
        return chess.Move.null()  # Defaultný ťah, ak ešte nebol žiadny v legalmoves
    
    best_move = None
    best_eval = float('-inf')

    for move in legal_moves:
        board.push(move)
        eval = evaluate_board(board)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_move = move
    
    print(f"Botov pohyb - eval: {best_move.uci()}")
    return best_move

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
