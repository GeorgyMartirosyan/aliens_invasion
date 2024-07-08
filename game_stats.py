class GameStats:
    """ Класс для игровой статистики. """

    def __init__(self, ai_settings):
        """ Инициализирует статистику. """
        self.ai_settings = ai_settings
        self.game_active = False  # Игра запускается в неактивном состоянии
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """ Иницилазирует статистику, изменяющуюся в ходе игры. """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1