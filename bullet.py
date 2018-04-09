import pygame
import sys
from pygame.sprite import  Sprite
import time
from time import sleep

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen=screen
#子弹属性
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_hight)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_settings.bullt_color
        self.speed=ai_settings.bullet_speed

    def update(self):
        self.y+=-self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

