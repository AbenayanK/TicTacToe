# ICS3U
# CPT
# Luciano
# Tic Tac Toe Game



import pygame

# Initialize pygame
pygame.init()

# Set the window dimensions
window_width = 400
window_height = 400

# creating windowb 
window = pygame.display.set_mode((window_width, window_height))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set  background color
bg_color = WHITE

# Drawing horizontal line across the middle of the window
pygame.draw.line(window, BLACK, (0, window_height / 2), (window_width, window_height / 2), 5)
