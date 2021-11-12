import pygame, random
from pygame.sprite import Sprite

class Bomb(Sprite):
    """create a bullet that is dropped by aliens"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midbottom = self.rect.midbottom

        self.y = float(self.rect.y)

    def update(self):
        """move bullet down screen"""
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bomb(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)