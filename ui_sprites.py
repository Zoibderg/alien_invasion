import pygame
from pygame.sprite import Sprite

class UIlaser(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/ui_laser.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        
class UIship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/ship_lives.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class UInumeralX(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/numeralX.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class UInumeral1(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/numeral1.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class UInumeral2(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/numeral2.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class UInumeral3(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect.(rect stands for rectangle)
        self.image = pygame.image.load('images/numeral3.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)