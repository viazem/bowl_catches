import pygame
from pygame.sprite import Sprite
from random import randint


class Fleshka(Sprite):
    """Класс представляющий одну флешку."""

    def __init__(self, ai_settings, screen):
        """Инициализирует флешку и задает ее начальную позицию."""
        super(Fleshka, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/fleshka.png')
        self.rect = self.image.get_rect()

        # Каждая флешка появляется в случайной позиции экрана
        self.reset_pos()

        # Промежуток времени до перемещения флешки
        self.time_move = 0.0

    def reset_pos(self):
        # Каждая флешка появляется в левом верхнем углу экрана
        self.rect.x = (
                self.rect.width +
                randint(0,
                        (self.ai_settings.screen_width - self.rect.width * 2)))
        self.rect.y = (
                self.rect.height +
                randint(0,
                        int((self.ai_settings.screen_height - self.rect.height * 2) / 2)))
        # Сохранение вещественных координат центра флешки
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Выводит флешку в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещение флешки вниз"""
        self.y += self.ai_settings.fleet_drop_speed
        self.rect.y = self.y

    def check_edges(self):
        """Возвращает True если флешка находится у края экрана"""
        if self.rect.bottom >= self.ai_settings.screen_height:
            return True
