import pygame
import sys
from time import sleep
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    # Overall class to manage the game
    def __init__(self):
        # Initialize game and create resources
        self.settings = Settings()

    def initialize_game(self):
        # Initialize Pygame and create resources
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # Create instance of stats class
        self.stats = GameStats(self)

        # Set active attribute to true
        self.game_active = True

        # Create ship
        self.ship = Ship(self)
       
        # Create sprite groups for bullets and aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # Create fleet of aliens
        self.create_fleet()
        
        # Set game window caption
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
        self.ship.draw_ship()
        self.aliens.draw(self.screen)
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

    def update_fleet(self):
        # Delete any bullets and aliens which have collided         
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Repopulate fleet if it has been destroyed
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
        
    def create_fleet(self):
        # Create the fleet of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        # While loop to create fleet while there is space
        while current_y < (self.settings.screen_height - 3 * alien_height):
                while current_x < (self.settings.screen_width - 2 * alien_width):
                    self.create_alien(current_x, current_y)
                    current_x += 2 * alien_width
        # Finish a row, reset X value and increment Y value
                current_x = alien_width
                current_y += alien_height * 2

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            # Increment Y value after hitting edge, dropping down
            alien.rect.y += self.settings.fleet_drop_speed
        # Reverse direction of travel
        self.settings.fleet_direction *= -1

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            # Check is alien is at an edge
            if alien.check_edges():
                # If alien is at an edge, change direction
                self.change_fleet_direction()
                break

    def create_alien(self, x_position, y_position):
        # Instantiate new alien
        new_alien = Alien(self)
        # Initialize new alien's X position
        new_alien.x = x_position
        new_alien.rect.x = x_position
        # Initialize new alien's Y position
        new_alien.rect.y = y_position
        # Add new alien to sprites group
        self.aliens.add(new_alien)

    def update_aliens(self):
        # Check if fleet of aliens is at an edge
        self.check_fleet_edges()
        # Update the alien fleet
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        # Check if an alien has hit the bottom of the screen
        self.check_aliens_bottom()

    def ship_hit(self):
        # Respond to ship being hit by decrementing number of remaining ships and resetting game
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Get rid of remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self.create_fleet()
            self.ship.center_ship()
            # Sleep for one second
            sleep(1)
        else:
            self.game_active = False

    def check_aliens_bottom(self):
        # Check if any aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.screen_height:
                # Treat this the same as the ship being hit by an alien
                self.ship_hit()
                break

    def run_game(self):
        # Start the main loop for the game
        while True:
            self.check_events()
            
            if self.game_active:
                self.check_events()
                self.ship.update()
                self.update_bullets()
                self.update_fleet()
                self.update_aliens()
                self.update_screen()

if __name__ == '__main__':
    # Make a game instance and run the game
    game = AlienInvasion()
    game.initialize_game()
    game.run_game()