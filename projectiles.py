import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, source):
        """create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = source

        # store bullets position in decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the sceen"""
        self.y -= self.settings.bullet_speed
        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bomb(Sprite):
    """create a bullet that is dropped by aliens"""

    def __init__(self, pos, bullet_speed):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        self.speed = bullet_speed

    def update(self):
        self.rect.y += self.speed

    def destroy(self):
        if self.rect.y >= self.settings.screen_height:
            self.kill()
