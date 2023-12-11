player_x = 'X'
player_o = 'O'
empty_cell = ' '
board_size = 3
win_message_head = 'Победа!'
win_message_body = 'Вы победили!'
draw_message_head = 'Ничья!'
draw_message_body = 'Ничья!'
lose_message_head = 'Проигрыш!'
lose_message_body = 'Вы проиграли!'

# Функция для проверки выигрышной комбинации
def check_winner(board, player):
    # Проверяем строки и столбцы
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Проверяем диагонали
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Функция для оценки текущего состояния игры
def evaluate(board):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    else:
        return 0
