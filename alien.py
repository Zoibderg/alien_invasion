import random
import pygame
from pygame.sprite import Sprite
from random import choice


class Alien(Sprite):
    """A class to represent a sinlge alien in the fleet"""

    def __init__(self, ai_game):
        """initlize alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        alien_one = pygame.image.load('images/alien.png').convert_alpha()
        alien_two = pygame.image.load('images/alien2.png').convert_alpha()
        alien_three = pygame.image.load('images/alien3.png').convert_alpha()
        alien_four = pygame.image.load('images/alien4.png').convert_alpha()

        alien_list = [alien_one, alien_two, alien_three, alien_four]

        # load alien image at set its rect
        self.image = random.choice(alien_list)
        self.rect = self.image.get_rect()

        # start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store aliens exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move the alien to the right or left"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
