import pygame
from settings import Settings


class Ship:
    """
    Класс управления кораблем.
    """

    def __init__(self, ai_game):
        """
        Инициализирует корабль и задает его начальную позицию.
        """
        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнегоа края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """
        Ресует корабль в текущей позиции
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Обнвление позиции корабля с учетом флага.
        """
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
