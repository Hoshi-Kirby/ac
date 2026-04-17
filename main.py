import sys, random
import pygame, time
import stage 
import value
import player
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()
step=1
clock = pygame.time.Clock()
while True:
    stage.set()
    while step==1:
        value.screen.fill((0,0,0))
        stage.draw()
        player.draw(1,100,100)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_d] and value.scroll<value.maxWidth-value.width:
            value.scroll+=1
        if pressed_keys[K_a] and value.scroll>0:
            value.scroll-=1


        clock.tick(60)
        
        pygame.display.update()