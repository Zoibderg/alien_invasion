class Settings:
    """A class to store our settings for Alien Invasion game."""

    def __init__(self):
        """Initlize the games settings."""
        # screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

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

        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increse_speed(self):
        """increse speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)