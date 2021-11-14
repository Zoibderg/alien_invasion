import pygame

"""attempt to make walls that will appear during gameplay"""

class Wall:
    """a wall to get in the players way"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #demensions of wall
        self.width, self.height = 500, 20
        self.wall_color = (255, 255, 255)

        #build and place wall
        self.rect = pygame.Rect(0, 900, self.width, self.height)
        #self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def draw_wall(self):
        self.screen.fill(self.wall_color, self.rect)

    def update(self, direction):
        """move wall to left or right"""
        self.x += direction
        self.rect.x = self.x
