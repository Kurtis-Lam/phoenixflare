from engines.phoenixflare.main import get_move

import chess
from chess.engine import PlayResult, Limit
import random
from lib.engine_wrapper import MinimalEngine
from lib.lichess_types import MOVE, HOMEMADE_ARGS_TYPE
import logging

logger = logging.getLogger(__name__)

class ExampleEngine(MinimalEngine):
    """An basic engine that all engines inherit"""

class PhoenixFlare(ExampleEngine):
    def search(self, board: chess.Board, time_limit: Limit, ponder: bool, draw_offered: bool, root_moves: MOVE) -> PlayResult:
        print("PhoenixFlare thinking...")
        
        move = get_move(board, 4)

        return PlayResult(move, None)