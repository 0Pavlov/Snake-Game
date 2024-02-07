import pygame
import random
from pygame.math import Vector2
pygame.init()


class Snake:
    def __init__(self):
        self.head = Vector2(random.randint(0, GRID_DIMENSIONS[0] - 1), random.randint(0, GRID_DIMENSIONS[1] - 1))
        self.body = [self.head]
        self.length = len(self.body)
        self.eat = False

        # Possible directions
        self.up, self.down = Vector2(0, -1), Vector2(0, 1)
        self.left, self.right = Vector2(-1, 0), Vector2(1, 0)

        # Current direction
        self.direction = Vector2(0, 0)

    def draw_snake(self):
        for x, y in enumerate(self.body):
            snake_rect = pygame.Rect(int(y[0] * CELL_SIZE), int(y[1] * CELL_SIZE), CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(screen, pygame.Color((39, 27, 107)), snake_rect)

    def move_snake(self):
        if self.eat:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.eat = False
        elif len(self.body) == 1:
            body_copy = [self.body[0] + self.direction]
            self.body = body_copy
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def grow(self):
        self.eat = True


class Food:
    def __init__(self):
        self.x = random.randint(0, GRID_DIMENSIONS[0] - 1)
        self.y = random.randint(0, GRID_DIMENSIONS[1] - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE - 1, CELL_SIZE - 1)
        pygame.draw.rect(screen, pygame.Color((113, 84, 255)), food_rect)

    def respawn(self):
        self.x = random.randint(0, GRID_DIMENSIONS[0] - 1)
        self.y = random.randint(0, GRID_DIMENSIONS[1] - 1)
        self.pos = Vector2(self.x, self.y)


class Score:
    def __init__(self):
        pygame.font.init()
        self.value = 0
        self.font = pygame.font.Font(None, 30)

    def draw_score(self):
        score_rect = pygame.Rect(0, (GRID_DIMENSIONS[1]) * CELL_SIZE,
                                 (GRID_DIMENSIONS[0]) * CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (69, 50, 182), score_rect)
        score_text = self.font.render(f"Score: {self.value}", True, (19, 12, 56))
        screen.blit(score_text, (3, CELL_SIZE * (GRID_DIMENSIONS[0] - 1) + 4))


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = Score()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.border()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()
        self.score.draw_score()

    def collision(self):
        if self.food.pos == self.snake.body[0]:
            self.score.value += 15
            self.food.respawn()
            self.snake.grow()
        if self.food.pos in self.snake.body:
            self.food.respawn()
        if self.snake.body[0] in self.snake.body[1:]:
            self.snake.body = [self.snake.head]
            self.snake.direction = Vector2(0, 0)
            self.score.value = 0
            self.food.respawn()

    def border(self):
        if self.snake.body[0].x > GRID_DIMENSIONS[0] - 1:
            self.snake.body[0].x = 0
        if self.snake.body[0].x < 0:
            self.snake.body[0].x = GRID_DIMENSIONS[0]
        if self.snake.body[0].y > GRID_DIMENSIONS[1] - 1:
            self.snake.body[0].y = 0
        if self.snake.body[0].y < 0:
            self.snake.body[0].y = GRID_DIMENSIONS[1]


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

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        # Input handling
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w and  # Check if opposite direction and having a body
                    main_game.snake.direction != main_game.snake.down and len(main_game.snake.body) > 1):
                main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_w and len(main_game.snake.body) == 1:
                main_game.snake.direction = Vector2(0, -1)

            if (event.key == pygame.K_a and  # Check if opposite direction and having a body
                    main_game.snake.direction != main_game.snake.right and len(main_game.snake.body) > 1):
                main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_a and len(main_game.snake.body) == 1:
                main_game.snake.direction = Vector2(-1, 0)

            if (event.key == pygame.K_s and  # Check if opposite direction and having a body
                    main_game.snake.direction != main_game.snake.up and len(main_game.snake.body) > 1):
                main_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_s and len(main_game.snake.body) == 1:
                main_game.snake.direction = Vector2(0, 1)

            if (event.key == pygame.K_d and  # Check if opposite direction and having a body
                    main_game.snake.direction != main_game.snake.left and len(main_game.snake.body) > 1):
                main_game.snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_d and len(main_game.snake.body) == 1:
                main_game.snake.direction = Vector2(1, 0)

    screen.fill((7, 4, 24))

    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)
