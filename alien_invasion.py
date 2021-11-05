import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initlize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #this creates a display window for our game
        #our arguments (1200, 800) is display in pixels
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Set our background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main loop for our game."""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            # draw the ship to the screen
            self.ship.update()
            #call to update images on the screen
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
                #if that key press is right arrow
                if event.key == pygame.K_RIGHT:
                    # set movement flag to True
                    self.ship.moving_right = True
            # if event is releasing a key
            elif event.type == pygame.KEYUP:
                # if that released key is right arrow key
                if event.key == pygame.K_RIGHT:
                    # set the movement flag to False
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images on screen and flip to the new screen."""
        #fill our background with our bg_color
        self.screen.fill(self.settings.bg_color)
        #draw ship to screen
        self.ship.blitme()

        #Make the most recently drawn screen visible.
        #this clears our previous screen and updates it to a new one
        #this gives our programe smooth movemnt
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

