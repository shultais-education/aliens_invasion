class Settings:
    """
    Класс для хранения всех настроек игры.
    """

    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 928
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5

        # Снаряд
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
