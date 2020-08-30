class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ship_left = self.ai_settings.ship_limit
        # Игра Alien Invasion запускается в активном состоянии
        self.game_active = True
