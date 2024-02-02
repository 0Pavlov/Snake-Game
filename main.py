import pygame
from pygame.math import Vector2
import random
pygame.init()


class Food:
    def __init__(self):
        self.x = 26
        self.y = 0
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food = pygame.Rect(self.pos.x, self.pos.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, pygame.Color('red'), food)


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

# Food
food = Food()

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

    # Draw a snake
    pygame.draw.rect(screen, pygame.Color('green'), snake_head)

    # Draw food
    food.draw_food()

    pygame.display.update()
    clock.tick(60)
