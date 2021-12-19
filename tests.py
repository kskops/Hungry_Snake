import Hungry_snake
from Hungry_snake import moving
import unittest
import pygame
import unittest.mock
"""
class Screen(pygame.Surface):
    blit = unittest.mock.MagicMock()

screen = Screen((600,600))
"""
class TestSnake(unittest.TestCase):

    def MovingTest(self):
        snake_size = 10
        dirct = pygame.K_RIGHT
        self.assertEquals(Hungry_snake.moving(dirct, snake_size), 10, 0)
        snake_size = 10
        dirct = pygame.K_RIGHT
        self.assertEquals(Hungry_snake.moving(pygame.K_LEFT, snake_size), (-10, 0))
        snake_size = 15
        dirct = pygame.K_RIGHT
        self.assertEquals(Hungry_snake.moving(pygame.K_DOWN, snake_size), (0, 15))
        snake_size = 20
        dirct = pygame.K_RIGHT
        self.assertEquals(Hungry_snake.moving(pygame.K_UP, snake_size), (0, -20))

    def ScoreTest(self):
        snake_len = 10
        self.assertEquals(Hungry_snake.score_change(snake_len - 1), 9)

