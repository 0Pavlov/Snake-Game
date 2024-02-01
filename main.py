import pygame
import random

pygame.init()


# Game window
class Window:
    def __init__(self, x_dimension, y_dimension):
        self.x = x_dimension
        self.y = y_dimension


Window = Window(500, 500)
screen = pygame.display.set_mode(size=(Window.x, Window.y), vsync=1)
pygame.display.set_caption("Snake")

# Grid
CELL_SIZE = Window.x // 20
GRID_DIMENSIONS = (20, 19)

# Game speed
time, time_step = 0, 200
clock = pygame.time.Clock()

# Snake
snake_head = pygame.Rect(1, 1, CELL_SIZE - 2, CELL_SIZE - 2)
segments = [snake_head.copy()]
length = 1

"""test_surface = pygame.Surface((Window.x // GRID_DIMENSIONS[0], Window.y // GRID_DIMENSIONS[1]))  # TEST"""

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Input handling
        if event.type == pygame.KEYDOWN:
            pass

    screen.fill('black')

    # Draw grid
    for row in range(GRID_DIMENSIONS[1]):
        for col in range(GRID_DIMENSIONS[0]):
            pygame.draw.rect(screen, 'white', (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Draw a snake
    pygame.draw.rect(screen, pygame.Color('green'), snake_head)

    # Draw some things

    pygame.display.update()
    clock.tick(60)
