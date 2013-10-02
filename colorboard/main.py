# This is just a little fun color program I made in a few hours one night.
# Neat though isn't it! 
# Chris Laverdiere 2013
# <3 pygame

import pygame
from colorboard import *
from math import *
from random import *

def main():
    # Program constants
    fps = 10

    # Colors for convenience
    red   = (255, 0, 0)
    green = (0, 255, 0)
    blue  = (0, 0, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Board constants
    side_len  = 25           # Pixel length of each square
    squares_x = 15           # Number of squares on x-axis 
    squares_y = 15           # Number of squares on y-axis 
    dir_map   = ["up", "down", "left", "right",
                 "upright", "upleft", "downright", "downleft"]

    # Board initial setup
    board = ColorBoard(squares_x, squares_y)
    board.set_board_color(blue)
    board.set_random_shade()
    board.set_random_tint()

    # Screen constants
    screen_width  = (side_len + int(.1 * side_len)) * squares_x 
    screen_height = (side_len + int(.1 * side_len)) * squares_y 

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    clock = pygame.time.Clock()
    total_frames = 0

    # Game loop
    while True:

        # Draw board nodes
        draw_board(board, screen, side_len)

        # Every second, update colors and direction
        if total_frames % fps == 0:

            # New colors
            new_color = (randint(0,255), randint(0,255), randint(0,255))
            board.set_board_color(new_color)
            board.set_random_shade()
            board.set_random_tint()

            # New direction
            dir_seed = randint(0,7)
            new_dir = dir_map[dir_seed]

        # Shift board every frame
        board.shift_colors(new_dir)

        # fps woop woop
        clock.tick(fps)
        total_frames += 1

        # update the display
        pygame.display.update()

# Method that draws all nodes from the board in nice organized layout.
def draw_board(board, screen, side_len):
    for y, row in enumerate(board.nodes):
        for x, node in enumerate(row):
            rect = pygame.Rect(x * side_len * 1.1, y * side_len * 1.1, side_len, side_len)
            pygame.draw.rect(screen, node.color, rect)

if __name__ == "__main__":
    main()
