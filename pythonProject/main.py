import chess
import pygame
import logging
import sys
import chess.svg
import chess_ai

# Initialize pygame
pygame.init()

# Constants
BOARD_SIZE = (400, 400)
LOG_SIZE = (400, 200)
SQUARE_SIZE = 50

# Colors
WHITE = (220, 208, 194)
BLACK = (53, 53, 53)
HIGHLIGHT_COLOR = (255, 0, 0)

# Title
GAME_TITLE = "Шахматишки"

# Initialize logging
logging.basicConfig(filename='chess.log', level=logging.DEBUG)

# Load images
pieces = {}
for piece in chess.PIECE_TYPES:
    for color in chess.COLORS:
        # Load image
        image = pygame.image.load(f"{chess.COLOR_NAMES[color]}_{chess.piece_name(piece).upper()}.png")
        # Scale image
        pieces[chess.Piece(piece, color)] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))


# Draw the chessboard
def draw_board(screen, board, legal_moves):
    for rank in range(8):
        for file in range(8):
            # Get square color
            square_color = WHITE if (rank + file) % 2 == 0 else BLACK
            # Draw square
            rect = pygame.Rect(file * SQUARE_SIZE, (7 - rank) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            # Draw square outline
            pygame.draw.rect(screen, square_color, rect)
            # Draw piece
            piece = board.piece_at(chess.square(file, rank))
            if piece:
                # Draw square outline
                screen.blit(pieces[piece], rect)
            if legal_moves and chess.square(file, rank) in legal_moves:
                # Draw square outline
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, rect, 3)


def handle_events(board, legal_moves, selected_piece, is_player_turn):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            file, rank = x // SQUARE_SIZE, (y // SQUARE_SIZE)
            square = chess.square(file, 7 - rank)
            piece = board.piece_at(square)
            if piece and not selected_piece:
                legal_moves = [move.to_square for move in board.legal_moves if move.from_square == square]
                selected_piece = (piece, square)
            elif selected_piece and square in legal_moves:
                make_move(board, selected_piece[1], square)
                legal_moves = None
                selected_piece = None
                is_player_turn = not is_player_turn
            else:
                legal_moves = None
                selected_piece = None
    return legal_moves, selected_piece, is_player_turn


def make_move(board, from_square, to_square):
    move = chess.Move(from_square, to_square)
    board.push(move)


def main():
    if pygame.init() == (False, False):
        print("Error initializing pygame")
        return
    # Initialize pygame screen
    screen = pygame.display.set_mode(BOARD_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    # Initialize board
    board = chess.Board()
    svg_board = chess.svg.board(board=board, width=400, height=400)
    # Initialize legal moves
    legal_moves = None
    # Initialize selected piece
    selected_piece = None
    # Is game over
    game_over = False
    # Is my turn
    is_player_turn = True
    # Main loop
    while not game_over:
        try:
            # Handle user events
            legal_moves, selected_piece, is_player_turn = handle_events(board, legal_moves, selected_piece,
                                                                        is_player_turn)
            # Redraw the board
            draw_board(screen, board, legal_moves)
            # Update screen
            pygame.display.flip()
            # Calculate AI turn
            if not is_player_turn:
                ai_turns = chess_ai.ChessAI(board)
                ai_move = ai_turns.make_move()
                board.push(ai_move)
                draw_board(screen, board, legal_moves)
                is_player_turn = not is_player_turn
            logging.debug("f'Legal moves: {legal_moves}, selected piece: {selected_piece}")
            board.outcome()
            if board.is_game_over():
                game_over = True
        except Exception as e:
            logging.error(f'An error occurred: {e}')


def main_svg():
    pass


if __name__ == "__main__":
    main()
    # main_svg()
