class Settings():
    """Класс для хранения всех настроек игры The Bowl catches"""

    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 1.5
        # Промежуток времени в игре
        self.time = 0
        # Промежуток времени в течении которого флешка стоит на месте
        self.fleshka_time_stop = 0.15

        # Параметр пули
        self.bullet_speed_factor = 1
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Настройка флешки
        self.fleshka_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1

