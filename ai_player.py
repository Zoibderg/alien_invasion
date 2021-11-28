import pygame

from random import random
from alien_invasion import AlienInvasion
from settings import Settings


class AIPlayer:

    def __init__(self, ai_game):
        """AI player for Alien Invasion"""

        # reference to game object
        self.ai_game = ai_game

        self.screen_rect = self.ai_game.screen.get_rect()

    def run_game(self):
        """Replaces OG run_game() so that we can interject our own controls"""

        # start out game in active state
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # speed up game for development
        self._modify_speed(5)

        # get full fleet size
        self.fleet_size = len(self.ai_game.aliens)

        # start main loop for game
        while True:
            # still calling check_events so we can use keyboard
            # to quit
            self.ai_game._check_events()
            self._implement_strats()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._check_bomb_ship_collisions()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strats(self):
        """Implement strat for playing the game"""
        if len(self.ai_game.aliens) >= 0.5 * self.fleet_size:
            self._sweep_right_left()
        else:
            self._get_target_alien()
            self._shoot_target_alien()

        if self.ai_game.powerups.sprites():
            self._target_pows()
            self._grab_pows()

        if self.ai_game.alien_bombs.sprites():
            self._watch_bombs()
            self._dodge_bomb()

        # fire bullets half the time
        self._fire_bullets()

    def _sweep_right_left(self):
        # sweep to the left and right
        ship = self.ai_game.ship

        if not ship.moving_right and not ship.moving_left:
            # ship is not moving, move it to the right
            ship.moving_right = True
        elif ship.moving_right and ship.rect.right > self.screen_rect.right - 10:
            # ship will hit right edge, move left
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            # ship will hit left edge, move right
            ship.moving_left = False
            ship.moving_right = True

    def _fire_bullets(self):
        # fire bullets when possible, based of freq
        firing_freq = 0.5
        if random() < firing_freq:
            self.ai_game._fire_bullet()

    def _modify_speed(self, speed_factor):
        """speed up game for devlopment"""
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor

    def _shoot_target_alien(self):
        """target a single alien"""
        # attempt to shoot our target

        target_alien = self._get_target_alien()

        if self.ai_game.ship.rect.x < target_alien.rect.x + 150:
            self.ai_game.ship.moving_right = True
            self.ai_game.ship.moving_left = False

        elif self.ai_game.ship.rect.x > target_alien.rect.x - 500:
            self.ai_game.ship.moving_right = False
            self.ai_game.ship.moving_left = True

        self._fire_bullets()

    def _get_target_alien(self):
        # find right most alien in bottom row

        target_alien = self.ai_game.aliens.sprites()[0]

        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                target_alien = alien

            elif alien.rect.y < target_alien.rect.y:
                continue

            elif alien.rect.x > target_alien.rect.x:
                target_alien = alien

        return target_alien

    def _target_pows(self):
        target_pow = self.ai_game.powerups.sprites()[0]

        for pow in self.ai_game.powerups.sprites():
            if pow.rect.y > target_pow.rect.y:
                target_pow = pow

            elif pow.rect.y < target_pow.rect.y:
                continue

        return target_pow

    def _grab_pows(self):
        target_pow = self._target_pows()
        still_grabable = self.screen_rect.height - 100

        if target_pow.rect.y > still_grabable:
            pass

        elif self.ai_game.ship.rect.x > target_pow.rect.x:
            self.ai_game.ship.moving_left = True
            self.ai_game.ship.moving_right = False

        elif self.ai_game.ship.rect.x < target_pow.rect.x:
            self.ai_game.ship.moving_left = False
            self.ai_game.ship.moving_right = True

        elif self.ai_game.ship.rect.x == target_pow.rect.x:
            self.ai_game.ship.moving_left = False
            self.ai_game.ship.moving_right = False

    def _watch_bombs(self):
        target_bomb = self.ai_game.alien_bombs.sprites()[0]

        for bomb in self.ai_game.alien_bombs.sprites():
            if bomb.rect.y > target_bomb.rect.y:
                target_bomb = bomb

            elif bomb.rect.y < target_bomb.rect.y:
                continue

            elif bomb.rect.x > target_bomb.rect.x:
                target_bomb = bomb

        return target_bomb

    def _dodge_bomb(self):
        if not self.ai_game.stats.game_active:

            return
        target_bomb = self._watch_bombs()

        if (
            self.ai_game.ship.rect.x <= self.screen_rect.width // 2
            and target_bomb.rect.x <= self.screen_rect.width // 2
        ):
            if target_bomb.rect.x <= self.ai_game.ship.rect.x:
                self.ai_game.ship.moving_left = False
                self.ai_game.ship.moving_right = True
            if target_bomb.rect.x >= self.ai_game.ship.rect.x:
                self.ai_game.ship.moving_left = True
                self.ai_game.ship.moving_right = False
        if (
            self.ai_game.ship.rect.x >= self.screen_rect.width // 2
            and target_bomb.rect.x >= self.screen_rect.width // 2
        ):
            if target_bomb.rect.x <= self.ai_game.ship.rect.x:
                self.ai_game.ship.moving_left = False
                self.ai_game.ship.moving_right = True
            if target_bomb.rect.x >= self.ai_game.ship.rect.x:
                self.ai_game.ship.moving_left = True
                self.ai_game.ship.moving_right = False


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai_game = AlienInvasion()
    settings = Settings()
    ai_player = AIPlayer(ai_game)

    ai_player.run_game()
