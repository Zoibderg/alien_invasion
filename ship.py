import pygame

class Ship:
    """A class for managing our ship."""

    def __init__(self, ai_game):
        """Initlize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flags
        # we start our flag at false so the ship doesnt move by itself
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships position based on our movement flags"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

