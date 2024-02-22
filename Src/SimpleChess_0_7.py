import chess

#B > N > 3P
#B + N = R + 1.5P
#Q + P = 2R

# Hodnoty figúr
piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 510,
    chess.QUEEN: 880,
    chess.KING: 20000
}

piece_square_tables = {

    chess.PAWN: [
        [0,  0,  0,  0,  0,  0,  0,  0],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [0,  0, 0, 20, 20,  0,  0,  0],
        [5,  5, 10, 25, 25, 10,  5,  5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [0,  0,  0,  0,  0,  0,  0,  0]
        ],

    chess.KNIGHT: [
        [-50,-40,-30,-30,-30,-30,-40,-50],
        [-40,-20,  0,  5,  5,  0,-20,-40],
        [-30,  5, 10, 15, 15, 10,  5,-30],
        [-30,  0, 15, 20, 20, 15,  0,-30],
        [-30,  5, 15, 20, 20, 15,  5,-30],
        [-30,  0, 10, 15, 15, 10,  0,-30],
        [-40,-20,  0,  0,  0,  0,-20,-40],
        [-50,-40,-30,-30,-30,-30,-40,-50]
        ],

    chess.BISHOP: [
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-20,-10,-10,-10,-10,-10,-10,-20]
        ],

    chess.ROOK: [
        [0,  0,  0,  5,  5,  0,  0,  0],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [5, 10, 10, 10, 10, 10, 10,  5],
        [0,  0,  0,  0,  0,  0,  0,  0]
        ],

    chess.QUEEN: [
        [-20,-10,-10, -5, -5,-10,-10,-20],
        [-10,  0,  5,  0,  0,  0,  0,-10],
        [-10,  5,  5,  5,  5,  5,  0,-10],
        [0,  0,  5,  5,  5,  5,  0, -5],
        [-5,  0,  5,  5,  5,  5,  0, -5],
        [-10,  0,  5,  5,  5,  5,  0,-10],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-20,-10,-10, -5, -5,-10,-10,-20]
        ],

    chess.KING: [
        [20, 30, 10,  0,  0, 10, 30, 20],
        [20, 20, -10, -15,-15,-10, 20, 20],
        [-10,-20,-20,-20,-20,-20,-20,-10],
        [-20,-30,-30,-40,-40,-30,-30,-20],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30]
        ],

}

# Invertované tabuľky pre čiernych
#piece_square_tables_black = {piece: [list(reversed(row)) for row in table] for piece, table in piece_square_tables.items()}

piece_square_tables_black = {piece: [list(row) for row in reversed(table)] for piece, table in piece_square_tables.items()} #otočený (1.riadok bude posledný)

#print(piece_square_tables_black)

def evaluate_board(board):
    stand_pat = 0

    if board.is_checkmate():
        return -100000 if board.turn == chess.WHITE else 100000

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            value += get_piece_square_value(piece, square)
            stand_pat += value if piece.color == chess.WHITE else -value

    return quiescence_search(board, stand_pat, -100000, 100000, board.turn == chess.WHITE) / 100

def quiescence_search(board, stand_pat, alpha, beta, maximizing_player):
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    legal_moves = list(board.legal_moves)
    legal_captures = [move for move in legal_moves if board.is_capture(move)]

    for move in legal_captures:
        board.push(move)
        score = -quiescence_search(board, -stand_pat, -beta, -alpha, not maximizing_player)
        board.pop()

        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha

def get_piece_square_value(piece, square):
    table = piece_square_tables[piece.piece_type]
    if piece.color == chess.BLACK:
        table = piece_square_tables_black[piece.piece_type]

    file, rank = chess.square_file(square), chess.square_rank(square)
    return table[rank][file]

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)  
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

''' Nový kód - minimax
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)  
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

'''

def get_best_move(board, is_maximizing_player):
    legal_moves = list(board.legal_moves)
    best_move = None
    alpha = float('inf')  # Zmena na kladnú nekonečno pre minimalizáciu

    for move in legal_moves:
        board.push(move)
        eval = minimax(board, 4, alpha, float('-inf'), is_maximizing_player)  # Nastavte beta na negatívnu nekonečno pre maximalizáciu
        board.pop()

        if eval < alpha:  # Zmena na "<" pre minimalizáciu
            alpha = eval
            best_move = move

    print(f"Botov pohyb minimax-ABP-piecetables: {best_move.uci()}")
    return best_move
 
def play_chess():
    color = input("Zadaj farbu: white/black ")
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
        print("Hodnotenie pozície: ",evaluate_board(board))
        if board.turn == color:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            is_maximizing_player = board.turn != color
            move = get_best_move(board, is_maximizing_player)

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())


play_chess()