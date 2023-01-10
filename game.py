from os import wait

import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (450, 450)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Tic Tac Toe")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BG_COLOR = (0, 0, 0)
# Set the font
font = pygame.font.Font(None, 100)

# Create the Tic Tac Toe board
board = [[None, None, None], [None, None, None], [None, None, None]]

# Set the current player
current_player = "X"

# Set the cell size
cell_size = 150

# Set the margin size
margin_size = 50

# Set the radius of the X and O
radius = cell_size // 3

# Set the margin
margin = margin_size // 2

# Set the line width
line_width = 10

# Set the line color
line_color = WHITE

# Set the X and O colors
color1 = RED
color2 = BLUE


X = "X"
O = "O"

def draw_board():
  # Draw the grid
  for row in range(3):
    for col in range(3):
      color = WHITE
      if board[row][col] == X:
        color = RED
      elif board[row][col] == O:
        color = BLUE
      pygame.draw.rect(screen, color, (col*cell_size, row*cell_size, cell_size, cell_size))
      pygame.draw.rect(screen, BLACK, (col*cell_size, row*cell_size, cell_size, cell_size), 2)

def draw():
  row = 0
  col = 0
  screen.fill(BG_COLOR)
  draw_board()

  pygame.display.flip()
  draw_marker(X, RED, BLUE, (row, col))
  draw_marker(O, RED, BLUE, (row, col))

def mouse_clicked(pos):
  # Convert the mouse position to a row and column index
  row, col = pos[1] // cell_size, pos[0] // cell_size
  # Place the X or O on the board
  place_marker(row, col, current_player)

def place_marker(row, col, player):
  # Update the board
  board[row][col] = player
  # Switch to the other player
  global current_player
  current_player = O if player == X else X

def is_winner(board, marker):
      # Check if there is a win horizontally
      for row in range(3):
          if all(board[row][col] == marker for col in range(3)):
              return True
      # Check if there is a win vertically
      for col in range(3):
          if all(board[row][col] == marker for row in range(3)):
              return True
      # Check if there is a win diagonally
      if all(board[i][i] == marker for i in range(3)):
          return True
      if all(board[i][2 - i] == marker for i in range(3)):
          return True
      return False


def draw_marker(marker, color1, color2, pos):
  row, col = pos  # Unpack the tuple into row and col
  # Draw an X
  if marker == X:
    # Get the center coordinates of the cell
    x, y = get_center(row, col)
    # Draw the left diagonal line
    pygame.draw.line(screen, color1, (x - radius, y - radius), (x + radius, y + radius), line_width)
    # Draw the right diagonal line
    pygame.draw.line(screen, color1, (x - radius, y + radius), (x + radius, y - radius), line_width)
  # Draw an O
  elif marker == O:
    # Get the center coordinates of the cell
    x, y = get_center(row, col)
    # Draw the circle
    pygame.draw.circle(screen, color2, (x, y), radius, line_width)


def get_center(row, col):
  x = col * cell_size + cell_size // 2
  y = row * cell_size + cell_size // 2
  return (x, y)  # Return the tuple (x, y)

def update():
  global board, current_player
  # Check if there is a winner
  if is_winner(board, "X"):
    print("X is the winner!")

    running = False
  elif is_winner(board, "O"):
    print("O is the winner!")

    running = False
  # Switch players
  elif current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"




def mouse_clicked(pos):
  # Calculate the row and column that was clicked
  mouse_x, mouse_y = pos
  row, col = mouse_y // cell_size, mouse_x // cell_size

  # Place the X or O on the board
  place_marker(row, col, current_player)

# Main game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_clicked(event.pos)
  # Update and draw the game
  update()
  draw()
  # Update the display
  pygame.display.update()


# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Tic Tac Toe")

# Loop until the user clicks the close button
while running == True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_clicked(event.pos)
  # Update and draw the game
  update()
  draw()

# Quit pygame
pygame.quit()
