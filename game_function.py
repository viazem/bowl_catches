import sys
import pygame


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


def update_screen(ai_settings, screen, bowl):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    bowl.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
