from ai_turn import *
import tkinter as tk
from tkinter import messagebox
from common import *

class game_processing:
    def __init__(self):
        self.ai_turn = ai_turn()
        # Создаем игровое поле
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.root = None

    def start_game(self):
        # Создаем главное окно
        self.root = tk.Tk()
        self.root.title("Крестики-Нолики")
        self._show_board()
        self.root.mainloop()

    def _show_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=self.board[i][j], font=('Arial', 20), width=8, height=4,
                                   command=lambda row=i, col=j: self._make_move(row, col))
                button.grid(row=i, column=j)

    def _make_move(self, row, col):
        if self.board[row][col] == empty_cell:
            self.board[row][col] = player_x
            if check_winner(self.board, player_x):
                self._handle_game_end(win_message_head, win_message_body)
            elif all(self.board[i][j] != empty_cell for i in range(board_size) for j in range(board_size)):
                self._handle_game_end(draw_message_head, draw_message_body)
            else:
                self._make_ai_move()

    def _make_ai_move(self):
        self.board = self.ai_turn.make_computer_move(self.board)
        self._show_board()
        if check_winner(self.board, player_o):
            self._handle_game_end(lose_message_head, lose_message_body)
        elif all(self.board[i][j] != empty_cell for i in range(board_size) for j in range(board_size)):
            self._handle_game_end(draw_message_head, draw_message_body)

    def _handle_game_end(self, title, message):
        self._show_board()
        messagebox.showinfo(title, message)
        self.root.quit()




