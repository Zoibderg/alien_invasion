import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initlize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #Set our background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main loop for our game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to kepresses and mouse events."""
        #for each event in game capture that event
        for event in pygame.event.get():
            #if player preses close, quit game
            if event.type == pygame.QUIT:
                sys.exit()
            # if event is a key press
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # add is simpler than append, but is only avaliable in pygame
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """update bullets position and get rid of old bullets"""
        #update bullets position
        self.bullets.update()

        # get rid of bullets that leave the window
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on screen and flip to the new screen."""
        #fill our background with our bg_color
        self.screen.fill(self.settings.bg_color)
        #draw ship to screen
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Make the most recently drawn screen visible.
        #this clears our previous screen and updates it to a new one
        #this gives our programe smooth movemnt
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

