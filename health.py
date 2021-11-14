import pygame
from pygame.sprite import Sprite

class Health(Sprite):
    """A class for managing our ship."""

    def __init__(self, ai_game):
        """Initlize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/health.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
