"""attempt to make aliens drop powerups when killed"""
import random
import pygame
from pygame.sprite import Sprite
from settings import Settings


class Pow(Sprite):
    def __init__(self, center):
        super().__init__()

        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        # increased for testing
        self.speedy = 5

    def update(self):
        self.settings = Settings()
        self.rect.y += self.speedy
        if self.rect.top >= self.settings.screen_height + 200:
            self.kill()


powerup_images = {'shield': pygame.image.load('images/shield.bmp')}
powerup_images['gun'] = pygame.image.load('images/gun.bmp')
