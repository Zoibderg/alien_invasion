import sys, pygame

from settings import Settings
from bombs import Bomb
from alien import Alien
from button import Button
from random import choice

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initlize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                            self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.aliens = pygame.sprite.Group()
        self.create_fleet(rows = 5, cols = 8)
        self.alien_direction = 1
        self.alien_bombs = pygame.sprite.Group()

        #Set our background color
        self.bg_color = (230, 230, 230)
        

    def run_game(self):
        """Start main loop for our game."""
        while True:
            self._check_events()
            self.aliens.update(self.alien_direction)
            self.alien_position_check()
            self._update_screen()

    def _check_events(self):
        """Respond to kepresses and mouse events."""

        #for each event in game capture that event
        for event in pygame.event.get():
            #if player preses close, quit game
            if event.type == ALIENBOMB:
                self.alien_shoot()

            elif event.type == pygame.QUIT:
                sys.exit()



    def create_fleet(self, rows, cols, x_distance = 160, y_distance = 120, 
            x_offset = 160, y_offset = 120):

        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                alien_sprite = Alien(x, y)
                self.aliens.add(alien_sprite)

    def alien_position_check(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= self.settings.screen_width:
                self.alien_direction = -1
                self.alien_move_down(10)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(10)
            elif alien.rect.bottom >= self.settings.screen_height:
                print ("bottom hit")

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            bomb_sprite = Bomb(random_alien.rect.center, self.settings.bullet_speed)
            self.alien_bombs.add(bomb_sprite)

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

            self.create_fleet(rows = 5, cols = 8)
            
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Update images on screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        self.alien_bombs.update()

        self.aliens.draw(self.screen)
        self.alien_bombs.draw(self.screen)


        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    
    ALIENBOMB = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENBOMB, 800)

    ai.run_game()

