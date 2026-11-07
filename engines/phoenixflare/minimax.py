import chess
import math
from .eval import evaluate_board

def minimax(board, depth, alpha, beta, maximizing):
    """
    Implements the minimax algorithm with alpha-beta pruning.
    Returns the evaluation score of the board for the given depth.
    """
    # Terminal condition: maximum depth reached or game over.
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

def minimax_root(depth, board, maximizing):
    """
    Determines and returns the best move from the current board position using minimax.
    """
    best_move = None
    if maximizing:
        best_eval = -math.inf
        alpha = -math.inf
        beta = math.inf
        for move in board.legal_moves:
            board.push(move)
            current_eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if current_eval > best_eval:
                best_eval = current_eval
                best_move = move
            alpha = max(alpha, best_eval)
    else:
        best_eval = math.inf
        alpha = -math.inf
        beta = math.inf
        for move in board.legal_moves:
            board.push(move)
            current_eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if current_eval < best_eval:
                best_eval = current_eval
                best_move = move
            beta = min(beta, best_eval)
    return best_move