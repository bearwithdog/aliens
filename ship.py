import pygame
class Ship():
    def __init__(self,screen,ai_setting):
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False

        self.center=float(self.rect.centerx)

    #显示图片
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=1.5
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center+=-1.5
        self.rect.centerx=self.center


