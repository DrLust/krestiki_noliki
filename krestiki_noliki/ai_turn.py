from common import *


class ai_turn:
    def __init__(self):
        pass

    def make_computer_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == empty_cell:
                    board[i][j] = player_o
                    score = self._minimax(board, 0, False)
                    board[i][j] = empty_cell
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        row, col = best_move
        board[row][col] = player_o
        return board

    # Функция для рекурсивного применения алгоритма минимакса
    def _minimax(self, board, depth, is_maximizing):
        score = evaluate(board)
        if score == 1 or score == -1:
            return score
        if all(board[i][j] != empty_cell for i in range(board_size) for j in range(board_size)):
            return 0
        if is_maximizing:
            best_score = float('-inf')
            for i in range(board_size):
                for j in range(board_size):
                    if board[i][j] == empty_cell:
                        board[i][j] = player_o
                        score = self._minimax(board, depth + 1, False)
                        board[i][j] = empty_cell
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(board_size):
                for j in range(board_size):
                    if board[i][j] == empty_cell:
                        board[i][j] = player_x
                        score = self._minimax(board, depth + 1, True)
                        board[i][j] = empty_cell
                        best_score = min(score, best_score)
            return best_score



