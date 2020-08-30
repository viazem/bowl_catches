import sys
import pygame
from time import sleep


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


def check_bottom_edges(stats, bowl, fleshka):
    """Реагирует на достжении флешки края экрана внизу."""
    # print(f'stats.ship_left = {stats.ship_left}')
    if fleshka.check_edges():
        if stats.ship_left > 0:
            stats.ship_left -= 1
            fleshka.reset_pos()
            ship_hit(stats, bowl, fleshka)
        else:
            stats.game_active = False


def catch_fleshka(ai_settings, bowl, fleshka):
    """Определить попадание флешки в корзину."""
    catch = False
    # Проверка попадания в корзину
    # Определим попала флешка в корзину
    if fleshka.rect.bottom >= bowl.rect.y and (
            (fleshka.rect.x <= bowl.rect.x <= fleshka.rect.right) or (
             fleshka.rect.x <= bowl.rect.right <= fleshka.rect.right)):
        # print(f'fleshka.rect.x={fleshka.rect.x}, bowl.rect.x={bowl.rect.x}, fleshka.rect.right={fleshka.rect.right}')
        fleshka.reset_pos()
        catch = True

    return catch


def ship_hit(stats, bowl, fleshka):
    """Обрабатывает столкновение коризины и флешки"""

    # Создание новой флешки и размещение корзины в центре
    fleshka.reset_pos()
    bowl.center_bowl()

    # Пауза
    sleep(0.5)


def update_fleshka(ai_settings, stats, screen, bowl, fleshka):
    """
    Проверяет закончилось ли время перед следующим
    обновлением позиции
    """
    fleshka.time_move += ai_settings.delta_time
    if fleshka.time_move >= ai_settings.fleshka_time_stop:
        fleshka.time_move = 0
        fleshka.update()
    # Проверка попадания в корзину
    if catch_fleshka(ai_settings, bowl, fleshka):
        print("Fleshka hit!!")
        ship_hit(stats, bowl, fleshka)

    check_bottom_edges(stats, bowl, fleshka)



def update_screen(ai_settings, screen, bowl, fleshka):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    bowl.blitme()
    fleshka.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
