import pygame
from pygame.sprite import Sprite


class Bang(Sprite):
    """
    Класс представляющий взрыв пришельца.
    """

    def __init__(self, ai_game, centerx, centery):
        """
        Инициализирует пришельца и задает его начальную позицию.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения взрыва.
        self.image = pygame.image.load('images/ufo-1.png')
        self.rect = self.image.get_rect()

        # Каждый взрыв появляется на месте пришельца.
        self.rect.centerx = centerx
        self.rect.centery = centery

        # Засекаем время создания взрыва.
        self.time = pygame.time.get_ticks()

    def update(self):
        ...