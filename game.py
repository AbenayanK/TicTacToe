import sys
import pygame

# Set up the Pygame window
pygame.init()
window_size = (300, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tic Tac Toe')

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game board
board = [['-' for _ in range(3)] for _ in range(3)]

# Set the size of each cell on the game board
cell_size = 100

# Set the current player to 'X'
current_player = 'X'

def draw_board(board):
  """Draw the Tic Tac Toe game board"""
  for row in range(3):
    for col in range(3):
      x, y = col * cell_size, row * cell_size
      pygame.draw.rect(window, WHITE, (x, y, cell_size, cell_size), 1)
      if board[row][col] != '-':
        font = pygame.font.Font(None, 72)
        text_surface = font.render(board[row][col], True, BLACK)
        text_rect = text_surface.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
        window.blit(text_surface, text_rect)

def place_marker(row, col, player):
  """Place a marker for the current player on the game board"""
  board[row][col] = player

# Run the game loop
while True:
  # Handle player input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Get the mouse coordinates
      mouse_x, mouse_y = pygame.mouse.get_pos()
      # Calculate the row and column that was clicked
      row, col = mouse_y // cell_size, mouse_x // cell_size
      # Place the X or O on the board
      place_marker(row, col, current_player)
      # Switch to the other player
      current_player = 'O' if current_player == 'X' else 'X'
    # Draw the game board
    window.fill(BLACK)
    draw_board(board)
    # Update the display
    pygame.display.update()
