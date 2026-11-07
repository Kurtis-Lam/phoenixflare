from .material import eval_material
from .positions import eval_positions

def evaluate_board(board):
    """
    Returns the board evaluation computed as the sum of
    material evaluation and positional evaluation.
    """
    return eval_material(board) + eval_positions(board)