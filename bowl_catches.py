import sys

import pygame

from settings import Settings
from game_stats import GameStats
from bowl import Bowl
from fleshka import Fleshka
import game_function as gf


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("The bowl catches the flash drive")

    stats = GameStats(ai_settings)

    # Создание миски
    bowl = Bowl(ai_settings, screen)

    # Назначаем цвета фона
    bg_color = (230, 230, 230)

    # Создаем флешку
    fleshka = Fleshka(ai_settings, screen)

    # Запуск таймера
    clock = pygame.time.Clock()
    ai_settings.delta_time = 0

    # Запуск основного цикла игры
    while True:
        # Отслеживани и событий клавиатуры и мыши
        gf.check_events(bowl)
        if stats.game_active:
            bowl.update()
            gf.update_fleshka(ai_settings, stats, screen, bowl, fleshka)
            # При каждом проходе цикла перерисовывается экран
            # Отображение последнего прорисованного экрана.

        gf.update_screen(ai_settings, screen, bowl, fleshka)
        # Запоминаем время
        ai_settings.delta_time = clock.tick() / 1000  # / 1000 to convert to seconds.


run_game()
