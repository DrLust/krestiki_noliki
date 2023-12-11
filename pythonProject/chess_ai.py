from queue import PriorityQueue

import chess
import chess.polyglot
import chess.engine
import random

class ChessAI:
    def __init__(self, board):
        """
        Initialize the ChessAI class.

        Args:
            board (chess.Board): The current board state.
        """
        self.board = board
        self.stockfish_path = "C:/Users/ekate/PycharmProjects/pythonProject/stockfish/stockfish-windows-x86-64-modern.exe"
        self.initialize_engine()

    def initialize_engine(self):
        """
        Initialize the engine attribute.
        """
        self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)

    def make_move(self):
        """
        Make a move based on the current board state.

        Returns:
            chess.Move: The best move to make.
        """
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        return result.move





