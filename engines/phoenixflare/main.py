import chess
from .minimax import minimax_root

def get_move(board, depth):
    """
    Returns the best move for the board given the search depth.
    If board.turn is True (white) then the bot maximizes; 
    if False (black), it minimizes.
    """
    # Maximizing if white, minimizing if black.
    is_maximising = board.turn
    move = minimax_root(depth, board, is_maximising)
    return move