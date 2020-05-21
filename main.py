import pygame
import random


pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

X = Y = 240
WIDTH = HEIGHT = 20

class Grid:
    @staticmethod
    def draw(screen):
        x = 0
        y = 0
        for i in range(int(SCREEN_WIDTH/WIDTH)):
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + SCREEN_HEIGHT), 1)
            x += WIDTH

        x = 0
        y = 0
        for i in range(int(SCREEN_HEIGHT/HEIGHT)):
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x + SCREEN_WIDTH, y), 1)
            y += WIDTH

class Snake:
    def __init__(self, x, y, dirx, diry, width, height, body_length):
        self.x = x
        self.y = y
        self.dirx = dirx
        self.diry = diry
        self.width = width
        self.height = height
        self.body_length = body_length
        self.foodpos = self.food()

    def draw(self):
        pygame.draw.rect(SCREEN, (0, 255, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(SCREEN, (255, 0, 0), (self.foodpos[0], self.foodpos[1], self.width, self.height))
        self.eat()

    def food(self):
        x = random.randrange(0, 500, WIDTH)
        y = random.randrange(0, 500, HEIGHT)
        return x, y

    def eat(self):
        if self.x == self.foodpos[0] and self.y == self.foodpos[1]:
            self.foodpos = self.food()

run = True
snake = Snake(X, Y, 0, -1, WIDTH, HEIGHT, 1)


while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    # screen continuum
    if snake.x <= 0 - WIDTH :
        snake.x = 500
    elif snake.x >= 500 :
        snake.x = 0 - WIDTH
    elif snake.y <= 0:
        snake.y = 500 - HEIGHT
    elif snake.y >= 500:
        snake.y = 0


    # controls
    if keys[pygame.K_DOWN]:
        snake.diry = 1
        snake.dirx = 0
    if keys[pygame.K_UP]:
        snake.diry = -1
        snake.dirx = 0
    if keys[pygame.K_RIGHT]:
        snake.dirx = 1
        snake.diry = 0
    if keys[pygame.K_LEFT]:
        snake.dirx = -1
        snake.diry = 0


    snake.x += snake.dirx * snake.width
    snake.y += snake.diry * snake.width

    SCREEN.fill((0,0,0))
    Grid.draw(SCREEN)
    snake.draw()
    pygame.display.update()





pygame.quit()
