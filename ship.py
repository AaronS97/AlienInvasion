import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game):
        # Initialize the class with global game settings and inherit from Sprite
        super().__init__()
        # initialize the class, get screen and rect
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # load the ship image
        self.image_path = 'ENTER PATH TO SHIP IMAGE HERE' 
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()         
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # State of the ship's movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = float(self.rect.x)