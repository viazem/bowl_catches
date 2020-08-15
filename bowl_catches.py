import sys

import pygame

from settings import Settings
from bowl import Bowl
import game_function as gf


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("The bowl catches the flash drive")

    # Создание миски
    bowl = Bowl(ai_settings, screen)

    # Назначаем цвета фона
    bg_color = (230, 230, 230)

    # Запуск основного цикла игры
    while True:
        # Отслеживани и событий клавиатуры и мыши
        gf.check_events(bowl)
        bowl.update()
        # При каждом проходе цикла перерисовывается экран
        # Отображение последнего прорисованного экрана.
        gf.update_screen(ai_settings, screen, bowl)


run_game()
