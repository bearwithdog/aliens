import pygame
import random
import time
from pygame.sprite import Sprite
class Ailec(Sprite):
    def __init__(self,ai_setings,screen):
        super(Ailec,self).__init__()
        self.screen=screen
        self.ai_settings=ai_setings
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def bitme(self):
        self.screen.blit(self.image,self.rect)

