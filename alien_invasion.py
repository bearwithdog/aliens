import  sys
import  pygame
from settings import  Setting
from ship import Ship
import game_function as gf
from alien import Ailec
from bullet import Bullet
from pygame.sprite import Group
from game_stats import GameStats
import threading
import time
from button import Button
def run_game():
    pygame.init()
    ai_seting=Setting()
    screen=pygame.display.set_mode((ai_seting.screen_width,ai_seting.screen_hight))
    pygame.display.set_caption("躲避外星人")
    bg_color=(230,230,230)
    ship=Ship(screen,ai_seting)
    stats=GameStats(ai_seting)
    bullet=Group()
    alien=Group()
    play_button=Button(ai_seting, screen, 'PLAY')
    ali=Ailec(ai_seting,screen)
    alien.add(ali)
    t1=threading.Thread(target=gf.move_update,args=(ai_seting,alien,))
    #守护线程
    t1.setDaemon(True)
    t1.start()
    start_time=time.time()
    end_time=time.time()
    while True:
        gf.chenck_event(ship,bullet,stats,play_button,ai_seting,screen,t1)
        end_time=time.time()
        if(stats.game_active):
            ship.update()
            bullet.update()
            gf.collision(alien, bullet,ai_seting,screen)
            gf.update_aliens(ai_seting,stats,screen,ship,alien,bullet)
            gf.remove_bullet(bullet)
            if(end_time-start_time>=0.2):
                new_bullet=Bullet(ai_seting,screen,ship)
                bullet.add(new_bullet)
                start_time=end_time

        gf.update_screen(ai_seting,stats,screen,ship,bullet,alien,play_button)
try:
    run_game()
except:
    print("Unexpected error:", sys.exc_info())