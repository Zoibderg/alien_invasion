import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a sinlge alien in the fleet"""

    def __init__(self, x, y):
        """initlize alien and set its starting position"""
        super().__init__()

        # load alien image at set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, direction):
        self.rect.x += direction