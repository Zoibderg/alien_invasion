import sys, pygame, json

from time import sleep
from random import choice

from buttons import PlayButton, ContinueButton, EndButton
from projectiles import Bullet, Bomb

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from walls import Wall


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initlize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)

        self.walls = Wall(self)
        self.wall_direction = 0.5

        self._create_groups()
        self._create_fleet()
        self._create_buttons()

    def run_game(self):
        """Start main loop for our game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._check_bomb_ship_collisions()
                self._update_aliens()
                
            self._update_screen()


    def _create_buttons(self):
        self.play_button = PlayButton(self, "Play")
        self.game_over_button = EndButton(self, "Game Over, Click here to continue.")
        self.continue_button = ContinueButton(self, "Ship hit! Press SPACE to continue")

    def _create_groups(self):
        self.bullets = pygame.sprite.Group()
        self.alien_bombs = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


    def _check_events(self):
        """Respond to kepresses and mouse events."""
        #for each event in game capture that event
        for event in pygame.event.get():
            #if player preses close, quit game
            if event.type == pygame.QUIT:
                high_score = 'high_score.json'
                with open(high_score, 'w') as hs:
                    json.dump(self.stats.high_score, hs)
                sys.exit()

            elif event.type == ALIENBOMB and self.stats.game_active and self.stats.level >= 5:
                self._alien_shoot()

            # if event is a key press
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """start new game if player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            high_score = 'high_score.json'
            with open(high_score, 'w') as hs:
                json.dump(self.stats.high_score, hs)
            sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active == True:
            self._fire_bullet()
        elif event.key == pygame.K_SPACE and self.stats.game_active == False and self.stats.ships_left > 0:
                self.stats.game_active = True
                pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            # add is simpler than append, but is only avaliable in pygame
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """update bullets position and get rid of old bullets"""
        #update bullets position
        self.bullets.update()
        # get rid of bullets that leave the window
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respond to bullet-alien collisions"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _check_bomb_ship_collisions(self):
        """respond to the ship being hit by bombs"""
        collisions = pygame.sprite.spritecollideany(
            self.ship, self.alien_bombs
        )

        if collisions:
            self._ship_hit()


    def _update_aliens(self):
        """update the position of the aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """respond to the ship being hit by alien"""
        if self.stats.ships_left > 0:
            self._cycle_level()
        else:
            self.stats.game_active = False
            self.stats.reset_stats()
            pygame.mouse.set_visible(True)

    def _cycle_level(self):
        # decrese ships left
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        # get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet and recenter ship
        self._create_fleet()
        self.ship.center_ship()

        # small pause for reset
        sleep(0.5)

        self.stats.game_active = False
        self.continue_button.draw_button()

    def _create_fleet(self):
        """create our fleet of aliens"""
        # creat an alien and fine the number that fits in a row
        # spacing between each alien is equal to one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (5 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create a full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = 2 * alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond if any aliens reach the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """drop entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on screen and flip to the new screen."""
        #fill our background with our bg_color
        self.screen.fill(self.settings.bg_color)

        # draw scoreboard to screen
        self.sb.show_score()

        #draw ship to screen
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.alien_bombs.update()
        self.alien_bombs.draw(self.screen)

        self.aliens.draw(self.screen)

        if self.stats.game_active and self.stats.level >= 10:
            self.walls.draw_wall()
            self.walls.update(self.wall_direction)
            self.check_wall_edges()

        # draw play button if game is inactive
        if not self.stats.game_active:
            if self.stats.level == 1:
                self.play_button.draw_button()

            elif not self.stats.ships_left:
                self.game_over_button.draw_button()
                pygame.mouse.set_visible(True)

            elif self.stats.ships_left != 0:
                self.continue_button.draw_button()

        #Make the most recently drawn screen visible.
        #this clears our previous screen and updates it to a new one
        #this gives our programe smooth movemnt
        pygame.display.flip()

    def check_wall_edges(self):
        if self.walls.rect.right >= self.settings.screen_width:
            self.wall_direction = -0.5
        elif self.walls.rect.left <= 0:
            self.wall_direction = 0.5


    def _alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            bomb_sprite = Bomb(random_alien.rect.center, self.settings.bullet_speed)
            self.alien_bombs.add(bomb_sprite)

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()

    ALIENBOMB = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENBOMB, 800)

    ai.run_game()

