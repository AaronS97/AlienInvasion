from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        # Initialize the class with global game settings and inherit from Sprite
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # Initialize the alien's image, color and position
        self.image_path = 'C:/Users/aaron/OneDrive/Documents/GitHub/AlienInvasion/images/alien.bmp'
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        self.x = self.x + self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        # Check if alien has reached the edge of the screen
        # Return true if it has
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    