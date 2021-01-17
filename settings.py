class Settings:
    """
    Класс для хранения всех настроек игры.
    """

    def __init__(self):
        # Общие настройки
        self.screen_width = 1920
        self.screen_height = 928
        self.bg_color = (230, 230, 230)

        # Корабль
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Снаряды
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Флот
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Направление флота: 1 вправо, -1 влево.
        self.fleet_direction = 1
