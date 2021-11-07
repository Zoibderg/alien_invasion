class GameStats:
    """trak stats for alien invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """stats that can change during gameplay"""
        self.ships_left = self.settings.ship_limit