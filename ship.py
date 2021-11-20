import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class for managing our ship."""

    def __init__(self, ai_game):
        """Initlize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flags
        # we start our flag at false so the ship doesnt move by itself
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships position based on our movement flags"""
        # update ship's x value, not its rectange
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object for self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
