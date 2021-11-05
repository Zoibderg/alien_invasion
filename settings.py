class Settings:
    """A class to store our settings for Alien Invasion game."""

    def __init__(self):
        """Initlize the games settings."""
        #All screen settings
        self.screen_width = 1600
        self.screen_height = 900
        #this is our background color, which is a light gray
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
