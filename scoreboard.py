import pygame

from pygame.sprite import Group
from ui_sprites import UIlaser, UIship, UInumeralX, UInumeral1, UInumeral2, UInumeral3
from ship import Ship


class Scoreboard:
    """a class to report score information"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoreboard
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('fonts/font.ttf', 20)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_remaining_pow_time()
        self.prep_ships()

    def prep_score(self):
        """turn score into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turn high score into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        # center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_remaining_pow_time(self):
        """turn remainging pow time into an image"""
        self.UIlasers = Group()
        if self.settings.ship_power == 1:
            for laser_number in range(self.settings.ship_power):
                laser = UIlaser(self.ai_game)
                laser.rect.x = 110 + laser_number * laser.rect.width * 2
                laser.rect.y = 5
                self.UIlasers.add(laser)
        else:
            for laser_number in range(3):
                laser = UIlaser(self.ai_game)
                laser.rect.x = 110 + laser_number * laser.rect.width * 2
                laser.rect.y = 5
                self.UIlasers.add(laser)



    def prep_level(self):
        """turn level into image"""
        game_level = str(self.stats.level)
        level_str = (f"Level: {game_level}")
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """show how many ships are left"""
        self.UIships = Group()
        for ship in range(1):
            ship = UIship(self.ai_game)
            ship.rect.x = 10
            ship.rect.y = 10
            self.UIships.add(ship)

        self.numx = Group()
        numx = UInumeralX(self.ai_game)
        numx.rect.x = 10 * 5
        numx.rect.y = 15
        self.numx.add(numx)

        self.shipnums = Group()

        if self.stats.ships_left == 3:
            three = UInumeral3(self.ai_game)
            three.rect.x = 75
            three.rect.y = 13
            self.shipnums.add(three)

        elif self.stats.ships_left == 2:
            two = UInumeral2(self.ai_game)
            two.rect.x = 75
            two.rect.y = 13
            self.shipnums.add(two)

        else:
            one = UInumeral1(self.ai_game)
            one.rect.x = 75
            one.rect.y = 13
            self.shipnums.add(one)

    def check_high_score(self):
        """check for a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.UIships.draw(self.screen)
        self.numx.draw(self.screen)
        self.shipnums.draw(self.screen)
        self.UIlasers.draw(self.screen)
