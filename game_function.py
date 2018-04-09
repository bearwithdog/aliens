import sys
import random
import time
import pygame
from alien import Ailec
from bullet import  Bullet
from time import sleep
from button import Button
from alien import Ailec
def chenck_event(ship,bullet,stats,play_button,ai_settings,screen,t1):
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            sys.exit()
        elif eve.type == pygame.KEYDOWN:
            if eve.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif eve.key==pygame.K_LEFT:
                ship.moving_left=True
            elif eve.key==pygame.K_SPACE:
                new_bullet=Bullet(ai_settings,screen,ship)
                bullet.add(new_bullet)

        elif eve.type==pygame.KEYUP:
            if eve.key==pygame.K_RIGHT:
                ship.moving_right=False
            if eve.key==pygame.K_LEFT:
                ship.moving_left=False
        elif eve.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)

def check_play_button(stats,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active=True


def update_screen(ai_settings,stats,screen,ship,bullet,alien,play_button):
    screen.fill(ai_settings.bg_color)
    for bt in bullet.sprites():
        bt.draw_bullet()
    ship.blitme()
    if  not stats.game_active:
        play_button.draw_button()
    for ai in alien:
        ai.bitme()
    pygame.display.flip()

def remove_bullet(bullet):
    for bt in bullet.sprites():
        if bt.rect.bottom<=0:
            bullet.remove(bt)
    print(len(bullet))

def move_update(ai_settings,alien):
    while True:
        for ai in  alien:
            ai.rect.centerx=random.randint(0,ai_settings.screen_width)
            ai.rect.centery=random.randint(0,ai_settings.screen_hight)
        time.sleep(1)

def collision(aliens,bullets,ai_seting,screen):
    collision=pygame.sprite.groupcollide(aliens,bullets,False,True)
    new_num_alien=len(collision)
    for i in range(0,new_num_alien):
        ai=Ailec(ai_seting,screen)
        aliens.add(ai)
    collision.clear()

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        sleep(2)
    else:
        aliens.empty()
        bullets.empty()
        ali=Ailec(ai_settings,screen)
        aliens.add(ali)
        stats.game_active=False
        sleep(2)
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

