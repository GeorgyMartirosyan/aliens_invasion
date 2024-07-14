import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        """ Инициализирует корабль и задает его начальную позицию. """
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/15100.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Флаги перемещения.
        self.moving_right = False
        self.moving_left = False

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранения вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)


    def update(self):
        """ Обновляет позицию корабля с учётом флага. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """ Устанавливает позицию корабля по центру. """
        self.center = self.screen_rect.centerx

    def blitme(self):
        """ Рисует корабль в текущей позиции. """
        self.screen.blit(self.image, self.rect)
