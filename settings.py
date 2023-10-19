class Settings:
    # A class to store all settings for Alien Invasion
    
    def __init__(self):
        # Initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.max_bullets = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1