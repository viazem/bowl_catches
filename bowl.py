import pygame


class Bowl():

    def __init__(self, screen):
        """Инициализирует корзину и задаёт её первоночальную позицию"""
        self.screen = screen

        # Загрузка изображения корзинки и получения прямоугольника.
        self.image = pygame.image.load('images/miska.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждая миска появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
