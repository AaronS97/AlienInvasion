import pygame
import sys
from ship import Ship
from settings import Settings
from bullet import Bullet

class AlienInvasion:
    # Overall class to manage the game
    def __init__(self):
        # Initialize game and create resources
        self.settings = Settings()

    def initialize_game(self):
        # Initialize Pygame and create resources
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Alien Invasion")

    def check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        # Respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        # Update the screen
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def fire_bullets(self):
        # Check if player has used max allowed bullets
        if len(self.bullets) < self.settings.max_bullets:
        # Create a new bullet and add it to the bullets group
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        # Start the main loop for the game
        while True:
            self.check_events()
            self.update_screen()
            self.ship.update()
            self.update_bullets()

if __name__ == '__main__':
    # Make a game instance and run the game
    game = AlienInvasion()
    game.initialize_game()
    game.run_game()