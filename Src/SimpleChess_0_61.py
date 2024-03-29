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

    evaluation = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            value += get_piece_square_value(piece, square)
            evaluation += value if piece.color == chess.WHITE else -value

    return evaluation

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
            eval = minimax(board, depth - 1, alpha, beta, False)  # Invert maximizing_player for the next level
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
            eval = minimax(board, depth - 1, alpha, beta, True)  # Invert maximizing_player for the next level
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, is_maximizing_player):
    legal_moves = list(board.legal_moves)
    best_move = None
    alpha = float('inf')  # Zmena na kladnú nekonečno pre minimalizáciu

    for move in legal_moves:
        board.push(move)
        f = open("best-move-selection-d2.txt", "a")
        f.write(str(move))
        f.write("\n")
        f.close()
        eval = minimax(board, 4, alpha, float('-inf'), is_maximizing_player)  # Nastavte beta na negatívnu nekonečno pre maximalizáciu
        f = open("best-move-selection-d2.txt", "a")
        f.write(str(eval))
        f.write("\n\n")
        f.close()
        board.pop()

        if eval < alpha:  # Zmena na "<" pre minimalizáciu
            alpha = eval
            best_move = move

    print(f"Botov pohyb minimax-ABP-piecetables: {best_move.uci()}")
    f = open("best-move-selection-d2.txt", "a")
    f.write("Best move: ", best_move)
    f.write("\n------------------------\n")
    f.close()
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
        print("Hodnotenie pozície: ",evaluate_board(board)/100)
        if board.turn == color:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            is_maximizing_player = board.turn != color # True pre Bielych, False pre Čiernych
            move = get_best_move(board, is_maximizing_player)
            # print(f"Botov pohyb: {move.uci()}")

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())


play_chess()
#get_best_move(board=chess.Board())