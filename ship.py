import pygame

class Ship:
    # A class to manage the ship

    def __init__(self, game):
        # Initialize the ship and set its starting position
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect()

        self.image_path = 'C:/Users/Aaron/OneDrive/Programming/Python/Crash Course/alien_invasion/images/ship.bmp'
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()                                      

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def draw_ship(self):
        # Draw the ship at its current location 
        self.screen.blit(self.image, self.rect)