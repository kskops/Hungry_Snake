import pygame
import time
import random

def menu(choice):
    """Функция используется для изменения статуса игры
    Принимает на  вход choice - выбор, введенный игроком с клавиатуры
    Возвращает game_over - статус игры, game_close - статус открытия игры"""
    if choice == pygame.K_q:
        game_over = True
        game_close = False
    if choice == pygame.K_n:
        game_process()
    return game_over, game_close

def border(x, y):
    """Функция используется для определения, находится ли змея в границах игры
    Принимает на вход значения x - текущая координата змейки по оси X
    y - текущая координаат змейки по оси Y
    Возвращает game_close - статус игры (активен / неактивен)"""
    if x >= 525 or x < 65 or y >= 525 or y < 65:
        game_close = True
    else:
        game_close = False

    return game_close

def moving(dirct, snake_size):
    """Функция используется для передвижения змеи.
    Принимает на вход переменные - dirict, отвечающую за направление движения,
    и snake_size, отвечающую за размер одного блока змеи.
    Возвращает значения, в каком напралении сдвинулась змея по оси X (dx) и Y (dy)"""
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

def get_food(x, y, x_food, y_food, snake_len, snake_size):
    """Функция используется для определения попала ли змейка на еду
    Принимает на вход: x - координата головы зммеи по X, y - координата головы змеи по Y,
     x_food - координата еды по X, y_food - координата еды по Y, snake_len - длина змеи
     snake_size - размер одного блока змейки
     Возвращает snake_len - длину змеи после определения попала ли змея на еду,
     x_food - координата еды по X после определения попала ли змея на еду,
     y_food - координата еды по Y после определения попала ли змея на еду"""
    if x == x_food and y == y_food:
        x_food = round(random.randrange(65, width - snake_size - 75) / 10.0) * 10.0
        y_food = round(random.randrange(65, height - snake_size - 75) / 10.0) * 10.0
        snake_len += 1
    return snake_len, x_food, y_food

def score_change(score):
    """Функция испоьзуется для вывода количества очков.
    Принимает на вход кол-во очков"""
    score_font = pygame.font.SysFont("comicsans", 35)
    value = score_font.render("Score: " + str(score), True, score_color)
    screen.blit(value, [0, 0])


def print_level(level):
    """Функция для вывода уровня игры
    Принимает на вход level - значение текущего уровня"""
    level_font = pygame.font.SysFont("comicsans", 35)
    value = level_font.render("Level: " + str(level), True, white)
    screen.blit(value, [420, 0])

def snake_change(snake_size, snake_list):
    """Функция используется для вывода змеи.
    Принимает на вход размер одного блока змейки и ее длинну"""
    for a in snake_list:
        pygame.draw.rect(screen, snake_color, [a[0], a[1], snake_size, snake_size])

def message(msg, color, size_x, size_y):
    """Функция предназначена для вывода сообщений в игре.
    На вход принимает само сообщение, его цвет, координаат по X и Y"""
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [size_x, size_y])

def higher_level(snake_len, level, snake_speed):
    """Функция предназначена для повышения уровня игры/скорости змейки
    Принимает на вход snake_len - длину змеи, level - текущий уровень игры,
    snake_speed - скорсть змейки
    Возвращает level - уровень, snake_speed - скорость змейки"""
    if snake_len > level * 10 + 1:
        snake_speed += 1
        level += 1
    return level, snake_speed


def game_process():
    """Функция отвечает за процесс игры"""
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Hungry snake')

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
                    choice = event.key
                    game_over, game_close = menu(choice)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                x_change, y_change = moving(event.key, snake_size)

        game_close = border(x, y)

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
        score_change(snake_len - 1)
        print_level(level)

        pygame.display.update()

        snake_len, x_food, y_food = get_food(x, y, x_food, y_food, snake_len, snake_size)

        timing.tick(snake_speed)

        level, snake_speed = higher_level(snake_len, level, snake_speed)



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

if __name__ == "__main__":
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Hungry snake')

    timing = pygame.time.Clock()

    snake_size = 10
    snake_speed = 10

    game_process()