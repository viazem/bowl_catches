import sys

import pygame


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("The bowl catches the flash drive")

    # Запуск основного цикла игры
    while True:
        # Отслеживани е событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()

