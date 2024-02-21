import chess
import random

board = chess.Board()
#print(board)

legal_moves = list(board.legal_moves)
#print(legal_moves)
#print(len(legal_moves))

move = random.choice(legal_moves)

print(move.uci())
