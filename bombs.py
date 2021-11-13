import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    """create a bullet that is dropped by aliens"""

    def __init__(self, pos, bullet_speed):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)
        self.speed = bullet_speed

    def update(self):
        self.rect.y += self.speed

    def destroy(self):
        if self.rect.y >= self.settings.screen_height:
            self.kill()
