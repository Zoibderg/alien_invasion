import pygame
from pygame.sprite import Sprite

"""attempt to make walls that will appear during gameplay"""

class Wall(Sprite):
    """a wall to get in the players way"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #demensions of wall
        self.width, self.height = 200, 20
        self.wall_color = (255, 255, 255)

        #build and place wall
        self.rect = pygame.Rect(0, 900, self.width, self.height)
        #self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def draw_wall(self):
        self.screen.fill(self.wall_color, self.rect)

    def update(self, direction):
        """move wall to left or right"""
        self.x += (direction * self.settings.wall_speed)
        self.rect.x = self.x
