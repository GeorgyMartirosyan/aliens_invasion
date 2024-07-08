class Settings:
    """ Класс для хранения всех настроек игры Alien Invasion. """

    def __init__(self):
        """ Инициализирует настройки игры. """
        # Параметры программы.
        self.screen_width = 1600
        self.screen_height = 950
        self.bg_color = (230, 230, 230)

        # Параметры корабля.
        self.ship_speed_factor = 1.5

        # Параметры пули.
        self.bullet_speed_factor = 0.7 # 0.7
        self.bullet_width = 3 # 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Параметры пришельцов.
        self.alien_speed_factor = 0.7
        self.fleet_drop_speed = 3
        # fleet_direction = 1, означает передвижение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.ship_limit = 3

        # Темп ускорение игры.
        self.speedup_scale = 1.1

        # Темп роста стомости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры. """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.7
        self.alien_points = 50

    def increase_speed(self):
        """ Увеличивает настройки скорости и стоимости пришельцев. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.score_scale