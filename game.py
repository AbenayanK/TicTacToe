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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BG_COLOR = (255, 255, 255)
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

# Fonts
FONT = pygame.font.SysFont('arial', 50)

# Set the X and O colors
color1 = RED
color2 = BLUE

X = "X"
O = "O"

def get_center(row, col):
    x = (col + 0.5) * cell_size
    y = (row + 0.5) * cell_size
    return x, y


def draw_board():
    # Draw the grid
    for row in range(3):
        for col in range(3):
            # Get the center coordinates of the cell
            x, y = get_center(row, col)
            if board[row][col] == X:
                # Draw X
                pygame.draw.line(screen, color1, (x - radius, y - radius), (x + radius, y + radius), line_width)
                pygame.draw.line(screen, color1, (x - radius, y + radius), (x + radius, y - radius), line_width)
            elif board[row][col] == O:
                # Draw O
                pygame.draw.circle(screen, color2, (int(x), int(y)), radius, line_width)

def draw_grid():
    for row in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, row * cell_size), (3 * cell_size, row * cell_size), 2)
    for col in range(1, 3):
        pygame.draw.line(screen, BLACK, (col * cell_size, 0), (col * cell_size, 3 * cell_size), 2)


def draw():
    screen.fill(BG_COLOR)
    draw_grid()
    draw_board()
    pygame.display.flip()


def mouse_clicked(pos):
    # Convert the mouse position to a row and column index
    row, col = pos[1] // cell_size, pos[0] // cell_size
    # Place the X or O on the board
    place_marker(row, col, current_player)

def place_marker(row, col, player):
    # Check if the cell is empty
    if board[row][col] is None:
        # Update the board
        board[row][col] = player
        # draw_marker(player, color1, color2, (row, col))
        # Switch to the other player
        global current_player
        current_player = O if player == X else X
        draw()
        check_win()
    else:
        print("This cell is already occupied")

def check_win_and_draw_line(board, marker):
    for row in range(3):
        if all(board[row][col] == marker for col in range(3)):
            pygame.draw.line(screen, BLACK, (margin, (row + 1) * cell_size - margin), ((3 * cell_size) - margin, (row + 1) * cell_size - margin), line_width)
            return True
    for col in range(3):
        if all(board[row][col] == marker for row in range(3)):
            pygame.draw.line(screen, BLACK, ((col + 1) * cell_size - margin, margin), ((col + 1) * cell_size - margin, (3 * cell_size) - margin), line_width)
            return True
    if all(board[i][i] == marker for i in range(3)):
        pygame.draw.line(screen, BLACK, (margin, margin), ((3 * cell_size) - margin, (3 * cell_size) - margin), line_width)
        return True
    if all(board[i][2 - i] == marker for i in range(3)):
        pygame.draw.line(screen, BLACK, ((3 * cell_size) - margin, margin), (margin, (3 * cell_size) - margin), line_width)
        return True
    return False

def check_win():
    if check_win_and_draw_line(board, X) or check_win_and_draw_line(board, O):
        print("Player", current_player, "wins")
        pygame.display.flip()

def create_play_again_button():
    button_text = "Play Again"
    font = pygame.font.SysFont('arial', 30)
    button_surface = font.render(button_text, True, (0, 0, 0))
    button_rect = button_surface.get_rect()
    button_rect.center = (window_size[0]/2, window_size[1]/2)
    screen.blit(button_surface, button_rect)
    pygame.display.flip()
    return button_rect

def play():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked(event.pos)
    pygame.quit()

play()
