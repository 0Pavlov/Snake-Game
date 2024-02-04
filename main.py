import pygame
import random
from pygame.math import Vector2
pygame.init()

down = Vector2(0, 1)  # TEST
class Snake:
    def __init__(self):
        self.body = [Vector2(4, 2), Vector2(5, 2), Vector2(6, 2)]
        self.direction = down  # TEST

    def draw_snake(self):
        for x, y in enumerate(self.body):
            snake_rect = pygame.Rect(int(y[0] * CELL_SIZE), int(y[1] * CELL_SIZE), CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(screen, pygame.Color('Green'), snake_rect)


    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy


class Food:
    def __init__(self):
        self.x = random.randint(0, GRID_DIMENSIONS[0] - 1)
        self.y = random.randint(0, GRID_DIMENSIONS[1] - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, pygame.Color('red'), food_rect)


class Score:
    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw_score(self):
        score_rect = pygame.Rect(0, (GRID_DIMENSIONS[1]) * CELL_SIZE,
                                 (GRID_DIMENSIONS[0]) * CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (30, 30, 30), score_rect)
        score_text = self.font.render(f"Score: {self.score}", True, (100, 100, 100))
        screen.blit(score_text, (3, CELL_SIZE * (GRID_DIMENSIONS[0] - 1) + 4))


# Snake
snake = Snake()

# Score
score = Score()


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

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Input handling
        if event.type == pygame.KEYDOWN:
            pass

    screen.fill('black')

    # Draw snake
    snake.draw_snake()
    snake.move_snake()  # TEST

    # Draw score
    score.draw_score()

    # Draw food
    food.draw_food()

    pygame.display.update()
    clock.tick(60)
