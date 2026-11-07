import chess

weights = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def eval_material(board):
    """
    Returns the total white material minus total black material.
    """
    evaluation = 0
    for square, piece in board.piece_map().items():
        value = weights.get(piece.piece_type, 0)
        if piece.color == chess.WHITE:
            evaluation += value
        else:
            evaluation -= value
    return evaluation