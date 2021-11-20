import pygame

class Settings:
    """A class to store our settings for Alien Invasion game."""

    def __init__(self):
        """Initlize the games settings."""
        # screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_limit = 3
        self.ship_power = 1
        self.ship_power_max = 5
        self.POWERUP_TIME_ALLOWED = 10000

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 51, 51)
        self.bullets_allowed = 3
        self.upgraded_bullets_allowed = 6


        # alien settings
        self.fleet_drop_speed = 10
        self.increse_bomb_rate = 75

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how muct alien poits value increses
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """settings that change through the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5

        self.alien_speed = 0.5

        self.alien_bomb_speed = 999
        self.wall_speed = 0.5

        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

        self.powerup_time = 0

    def increse_speed(self):
        """increse speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.wall_speed *= self.speedup_scale
        self.alien_bomb_speed -= self.increse_bomb_rate

        self.alien_points = int(self.alien_points * self.score_scale)