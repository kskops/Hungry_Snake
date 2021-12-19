import pygame
import time
import random

"""Функция используется для передвижения змеи. Принимает на вход переменные - dirict, отвечающую 
за направление движения, и snake_size, отвечающую за размер одного блока змеи. Возвращает значения, 
в каком напралении сдвинулась змея по оси X и Y"""
def moving(dirct, snake_size):
    dx = 0
    dy = 0
    left = pygame.K_LEFT
    right = pygame.K_RIGHT
    up = pygame.K_UP
    down = pygame.K_DOWN
    if dirct == left:
        dx = -snake_size
        dy = 0
    elif dirct == right:
        dx = snake_size
        dy = 0
    elif dirct == up:
        dy = -snake_size
        dx = 0
    elif dirct == down:
        dy = snake_size
        dx = 0
    return dx, dy

"""Функция испоьзуется для вывода количества очков. 
Принимает на вход кол-во очков"""
def score_change(score):
    score_font = pygame.font.SysFont("comicsans", 35)
    value = score_font.render("Score: " + str(score), True, score_color)
    screen.blit(value, [0, 0])
    return score

"""Функция используется для вывода змеи. 
Принимает на вход размер одного блока змейки и ее длинну"""
def snake_change(snake_size, snake_list):
    for a in snake_list:
        pygame.draw.rect(screen, snake_color, [a[0], a[1], snake_size, snake_size])

"""Функция предназначена для вывода сообщений в игре. 
На вход принимает само сообщение, его цвет, координаат по X и Y"""
def message(msg, color, size_x, size_y):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [size_x, size_y])

"""Функция отвечает за процесс игры"""
def game_process():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Hungry snake')

    score = 0

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_len = 1

    x_food = round(random.randrange(65, width - snake_size - 75) / 10.0) * 10.0
    y_food = round(random.randrange(65, height - snake_size - 75) / 10.0) * 10.0

    level = 1

    snake_speed = 15

    while not game_over:

        while game_close == True:
            screen.fill(screen_color)
            frane = pygame.draw.rect(screen, white, [50, 50, 500, 500])
            screent = pygame.draw.rect(screen, screen_color, [55, 55, 490, 490])
            message("GAME OVER", mesg_color, 230, 200)
            message("q - quit / n - play again", mesg_color, 170, 250)
            score_change(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_n:
                        game_process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                x_change, y_change = moving(event.key, snake_size)

        if x >= 525 or x < 70 or y >= 525 or y < 70:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(screen_color)
        frane = pygame.draw.rect(screen, white, [50, 50, 500, 500])
        screent = pygame.draw.rect(screen, screen_color, [55, 55, 490, 490])
        pygame.draw.rect(screen, food_color, [x_food, y_food, snake_size, snake_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        for a in snake_list[:-1]:
            if a == snake_head:
                game_close = True

        snake_change(snake_size, snake_list)
        score_change(score)

        pygame.display.update()

        if x == x_food and y == y_food:
            x_food = round(random.randrange(65, width - snake_size - 75) / 10.0) * 10.0
            y_food = round(random.randrange(65, height - snake_size - 75) / 10.0) * 10.0
            snake_len += 1
            score = score_change(snake_len - 1)

        timing.tick(snake_speed)

        if snake_len - 1 >= level * 10:
            snake_speed += 1
            level += 1

    screen.fill(screen_color)
    message("GAME OVER", mesg_color, 230, 220)
    pygame.display.update()
    time.sleep(1)

    pygame.quit()
    quit()


white = (255, 255, 255)
score_color = (0, 250, 154)
snake_color = (173, 255, 47)
mesg_color = (255, 0, 255)
food_color = (255, 20, 147)
screen_color = (72, 61, 139)

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hungry snake')

timing = pygame.time.Clock()

snake_size = 10
snake_speed = 10

game_process()