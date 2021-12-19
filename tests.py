import unittest.mock

import pygame

from Hungry_snake import border
from Hungry_snake import get_food
from Hungry_snake import higher_level
from Hungry_snake import moving
from Hungry_snake import menu

class TestSnake(unittest.TestCase):

    def test_moving(self):
        snake_size = 10
        dirct = pygame.K_RIGHT
        self.assertEqual(moving(dirct, snake_size), (10, 0))
        snake_size = 10
        dirct = pygame.K_RIGHT
        self.assertEqual(moving(pygame.K_LEFT, snake_size), (-10, 0))
        snake_size = 15
        dirct = pygame.K_RIGHT
        self.assertEqual(moving(pygame.K_DOWN, snake_size), (0, 15))
        snake_size = 20
        dirct = pygame.K_RIGHT
        self.assertEqual(moving(pygame.K_UP, snake_size), (0, -20))

    def test_getfood(self):
        snake_size = 10
        snake_len = 10
        x = 150
        y = 150
        x_food = 120
        y_food = 115
        self.assertEqual(get_food(x, y, x_food, y_food, snake_len, snake_size), (10, x_food, y_food))
        snake_len = 20
        snake_size = 10
        x = 100
        y = 155
        x_food = 100
        y_food = 155
        self.assertNotEqual(get_food(x, y, x_food, y_food, snake_len, snake_size), (20, 100, 155))

    def test_boreder(self):
        x = 520
        y = 500
        self.assertEqual(border(x, y), False)
        x = 530
        y = 290
        self.assertEqual(border(x, y), True)
        x = 500
        y = 60
        self.assertEqual(border(x, y), True)
        x = 20
        y = 570
        self.assertEqual(border(x, y), True)

    def test_level(self):
        snake_len = 12
        level = 1
        snake_speed = 10
        self.assertEqual(higher_level(snake_len, level, snake_speed), (2, 11))
        snake_len = 19
        level = 2
        snake_speed = 10
        self.assertEqual(higher_level(snake_len, level, snake_speed), (2, 10))

    def test_menu(self):
        choice = pygame.K_q
        self.assertEqual(menu(choice), (True, False))