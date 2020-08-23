import sys
import pygame
from random import randint


def check_keydown_events(event, bowl):
    """Реагирует на нажатие клавишь."""
    if event.key == pygame.K_RIGHT:
        # переместить корабль вправо
        bowl.moving_right = True
    elif event.key == pygame.K_LEFT:
        bowl.moving_left = True


def check_keyup_events(event, bowl):
    """Реагирует на отпускание клавишь."""
    if event.key == pygame.K_RIGHT:
        bowl.moving_right = False
    elif event.key == pygame.K_LEFT:
        bowl.moving_left = False


def check_events(bowl):
    """Обработка нажатий клавиш и событий мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, bowl)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, bowl)


def check_bottom_edges(ai_settings, fleshka):
    """Реагирует на достжении флешки края экрана внизу."""
    if fleshka.check_edges():
        True


def update_fleshka(ai_settings, bowl, fleshka):
    """
    Проверяет закончилось ли время перед следующим
    обновлением позиции
    """
    fleshka.time_move += ai_settings.delta_time
    if fleshka.time_move >= ai_settings.fleshka_time_stop:
        fleshka.time_move = 0
        fleshka.update()
    # Проверка попадания в корзину
    # Определим попала флешка в корзину
    if fleshka.rect.bottom >= bowl.rect.y:
        print(f'fleshka.rect.x={fleshka.rect.x}, bowl.rect.x={bowl.rect.x}, fleshka.rect.right={fleshka.rect.right}')
        if (fleshka.rect.x <= bowl.rect.x <= fleshka.rect.right) or \
                (fleshka.rect.x <= bowl.rect.right <= fleshka.rect.right):
            fleshka.rect.x = (fleshka.rect.width +
                              randint(0,
                                      (
                                          fleshka.ai_settings.screen_width - fleshka.rect.width * 2
                                      )
                                      )
                              )
            fleshka.rect.y = (fleshka.rect.height +
                              randint(0,
                                      int(
                                          (
                                              fleshka.ai_settings.screen_height - fleshka.rect.height * 2
                                          )
                                          / 2
                                          )
                                      )
                              )
            fleshka.x = float(fleshka.rect.x)
            fleshka.y = float(fleshka.rect.y)


def update_screen(ai_settings, screen, bowl, fleshka):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    bowl.blitme()
    fleshka.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
