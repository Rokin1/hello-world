import sys

from pygame.sprite import Group

import pygame

from settings import Settings

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from ship import Ship

from alien import Alien

import game_functions as gf

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scorebord.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship, a group of bullets, and a group of aliens.
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats,  sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        
        """for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullet))
        gf.update_screen(ai_settings, screen, ship, bullets)"""
        """#Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        screen.fill(bg_color)
        ship.blitme()
                
        #Make the most recently drawn screen visible
        pygame.display.flip()"""
        
run_game()

"""
# set the background color.
bg_color = (230,230,230)

#start the main loop for the game.
while True:

    #Redraw the screen during each pass through the loop.
    screen.fill(big_color)
    # Make thr most drawn screen visible.
    pygame.display.flip()"""    
