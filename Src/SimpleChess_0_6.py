import chess

#B > N > 3P
#B + N = R + 1.5P
#Q + P = 2R

mp = False

pawn_table = [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5,  5, 10, 25, 25, 10,  5,  5],
    [0,  0,  0, 20, 20,  0,  0,  0],
    [5, -5,-10,  0,  0,-10, -5,  5],
    [5, 10, 10,-20,-20, 10, 10,  5],
    [0,  0,  0,  0,  0,  0,  0,  0]
    ]

knight_table = [
    [-50,-40,-30,-30,-30,-30,-40,-50],
    [-40,-20,  0,  0,  0,  0,-20,-40],
    [-30,  0, 10, 15, 15, 10,  0,-30],
    [-30,  5, 15, 20, 20, 15,  5,-30],
    [-30,  0, 15, 20, 20, 15,  0,-30],
    [-30,  5, 10, 15, 15, 10,  5,-30],
    [-40,-20,  0,  5,  5,  0,-20,-40],
    [-50,-40,-30,-30,-30,-30,-40,-50]
    ]

bishop_table = [
    [-20,-10,-10,-10,-10,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5, 10, 10,  5,  0,-10],
    [-10,  5,  5, 10, 10,  5,  5,-10],
    [-10,  0, 10, 10, 10, 10,  0,-10],
    [-10, 10, 10, 10, 10, 10, 10,-10],
    [-10,  5,  0,  0,  0,  0,  5,-10],
    [-20,-10,-10,-10,-10,-10,-10,-20]
    ]

rook_table = [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [5, 10, 10, 10, 10, 10, 10,  5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [0,  0,  0,  5,  5,  0,  0,  0]
    ]

queen_table = [
    [-20,-10,-10, -5, -5,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5,  5,  5,  5,  0,-10],
    [-5,  0,  5,  5,  5,  5,  0, -5],
    [0,  0,  5,  5,  5,  5,  0, -5],
    [-10,  5,  5,  5,  5,  5,  0,-10],
    [-10,  0,  5,  0,  0,  0,  0,-10],
    [-20,-10,-10, -5, -5,-10,-10,-20]
    ]

king_midgame_table = [
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-20,-30,-30,-40,-40,-30,-30,-20],
    [-10,-20,-20,-20,-20,-20,-20,-10],
    [20, 20,  0,  0,  0,  0, 20, 20],
    [20, 30, 10,  0,  0, 10, 30, 20]
    ]

king_endgame_table = [
    [-50,-40,-30,-20,-20,-30,-40,-50],
    [-30,-20,-10,  0,  0,-10,-20,-30],
    [-30,-10, 20, 30, 30, 20,-10,-30],
    [-30,-10, 30, 40, 40, 30,-10,-30],
    [-30,-10, 30, 40, 40, 30,-10,-30],
    [-30,-10, 20, 30, 30, 20,-10,-30],
    [-30,-30,  0,  0,  0,  0,-30,-30],
    [-50,-30,-30,-30,-30,-30,-30,-50]
    ]

pawn_table_black = list(reversed(pawn_table))
knight_table_black = list(reversed(knight_table))
bishop_table_black = list(reversed(bishop_table))
rook_table_black = list(reversed(rook_table))
queen_table_black = list(reversed(queen_table))
king_midgame_table_black = list(reversed(king_midgame_table))
king_endgame_table_black = list(reversed(king_endgame_table))

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 510,
        chess.QUEEN: 880,
        chess.KING: 20000
    }


    pawn_table_black = list(reversed(pawn_table))
    knight_table_black = list(reversed(knight_table))
    bishop_table_black = list(reversed(bishop_table))
    rook_table_black = list(reversed(rook_table))
    queen_table_black = list(reversed(queen_table))
    king_midgame_table_black = list(reversed(king_midgame_table))
    king_endgame_table_black = list(reversed(king_endgame_table))

    evaluation = 0

    '''
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            evaluation += value if piece.color == chess.WHITE else -value

    return evaluation
    '''

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            value += get_piece_square_value(piece, square, piece_values)
            evaluation += value if piece.color == chess.WHITE else -value

    return evaluation

def get_piece_square_value(piece, square, piece_values):
    piece_square_tables = {
        chess.PAWN: pawn_table,
        chess.KNIGHT: knight_table,
        chess.BISHOP: bishop_table,
        chess.ROOK: rook_table,
        chess.QUEEN: queen_table,
        chess.KING: king_midgame_table  # Můžete zvolit king_endgame_table pro koncovou hru
    }

    if piece.color == chess.BLACK:
        piece_square_tables = {
            chess.PAWN: pawn_table_black,
            chess.KNIGHT: knight_table_black,
            chess.BISHOP: bishop_table_black,
            chess.ROOK: rook_table_black,
            chess.QUEEN: queen_table_black,
            chess.KING: king_midgame_table_black  # Můžete zvolit king_endgame_table_black pro koncovou hru
        }

    # Získání hodnoty z tabulky podle pozice a typu figury
    file, rank = chess.square_file(square), chess.square_rank(square)
    return piece_square_tables[piece.piece_type][rank][file]

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

def get_best_move(board):
    legal_moves = list(board.legal_moves)
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    for move in legal_moves:
        board.push(move)
        eval = minimax(board, 3, alpha, beta, mp)  #Hĺbka (napr 2)
        board.pop()

        if eval > alpha:
            alpha = eval
            best_move = move

    print(f"Botov pohyb minimax-ABP-piecetables: {best_move.uci()}")
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
        print(evaluate_board(board))
        if board.turn == color:
            move = input("Tvoj ťah (vo formáte a2a4): ")
            move = chess.Move.from_uci(move.lower())
        else:
            move = get_best_move(board)
            #print(f"Botov pohyb: {move.uci()}")
            print(evaluate_board(board))

        board.push(move)

    print("Koniec hry")
    print("Výsledok: " + board.result())

play_chess()
#get_best_move(board=chess.Board())