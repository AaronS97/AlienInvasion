import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # A class to manage bullets fired from the ship
    def __init__(self, game):
        # Initialize the class with global game settings and inherit from Sprite
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # Initialize the bullet's color and position
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        # Move the bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)