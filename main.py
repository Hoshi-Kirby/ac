import sys, random
import pygame, time
import stage 
import value
import player
import key
import sword
import timer
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
while True:
    if value.step==0:
        value.reset()
    if value.step==1:
        stage.set(0)
    while value.step==1:
        value.screen.fill((0,0,0))
        stage.draw()
        player.draw(value.playerPause+value.playerIsLeft,value.atackTime,value.throwTime,(value.playerX-value.scroll)*value.size,value.playerY*value.size)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key.event1(event.key)
        key.pressed1()

        sword.calc()
        sword.draw()

        timer.dec1()
        clock.tick(60)
        
        pygame.display.update()