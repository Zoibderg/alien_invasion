import pygame

from pygame.sprite import Group
from health import EmptyHealth, Health
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
        self.prep_empty_hearts()
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
        pow_time_left = self.settings.ship_power
        pow_time_str = "{}".format(pow_time_left)
        self.powtime_image = self.font.render(pow_time_str, True, 
        self.text_color, self.settings.bg_color)

        self.powtime_rect = self.powtime_image.get_rect()
        self.powtime_rect.left = self.screen_rect.left + 275
        self.powtime_rect.top = self.screen_rect.top + 30

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
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Health(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_empty_hearts(self):
        self.empty_hearts = Group()
        for ship_number in range(self.settings.ship_limit):
            empty_heart = EmptyHealth(self.ai_game)
            empty_heart.rect.x = 10 + ship_number * empty_heart.rect.width
            empty_heart.rect.y = 10
            self.empty_hearts.add(empty_heart)

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
        self.screen.blit(self.powtime_image, self.powtime_rect)
        self.empty_hearts.draw(self.screen)
        self.ships.draw(self.screen)