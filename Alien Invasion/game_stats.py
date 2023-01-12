class GameStats():
    """Trach stats for alien invasion"""

    def __init__(self, ai_settings):
        """Initialise statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
