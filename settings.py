class Settings:
    # A class to store all settings for Alien Invasion
    
    def __init__(self):
    # Static settings    
        # Initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 3
        self.bullet_height = 15
        self.max_bullets = 3
        # Alien settings
        self.fleet_drop_speed = 5
        # Ship settings
        self.ship_limit = 3
    # Dynamic settings
        self.speed_increase_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize dynamic settings that change each round
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_increase_scale
        self.bullet_speed *= self.speed_increase_scale
        self.alien_speed *= self.speed_increase_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        