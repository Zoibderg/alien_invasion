class Settings:
    """A class to store our settings for Alien Invasion game."""

    def __init__(self):
        """Initlize the games settings."""
        # screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 50

        # fleet_direction of 1 represents right; -1 left
        self.fleet_direction = 1