import sys, random
import pygame, time
import stage 
import value
import player
import key
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
while True:
    if value.step==0:
        value.reset()
    if value.step==1:
        stage.set()
    while value.step==1:
        value.screen.fill((0,0,0))
        stage.draw()
        player.draw(value.playerPause+value.playerIsLeft,(value.playerX-value.scroll)*value.size,value.playerY*value.size)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key.event1(event.key)
        key.pressed1()


        if value.dashRightTime>0:
            value.dashRightTime-=1
        if value.dashLeftTime>0:
            value.dashLeftTime-=1
        if not stage.isHit(value.playerX,value.playerY,value.playerWidth,value.playerHeight) or value.playerVY<=0:
            value.playerVY+=0.1
        else:
            value.playerVY=0
        if not stage.isHit(value.playerX,value.playerY,value.playerWidth,value.playerHeight) and value.playerVY>0 and value.playerY<value.height-value.playerHeight/value.size*2:
            for i in range(int(value.playerVY*10)):
                if stage.isHit(value.playerX,value.playerY,value.playerWidth,value.playerHeight):
                    break
                value.playerY+=0.1
        if not stage.isHit(value.playerX,value.playerY-1,value.playerWidth,value.playerHeight) and value.playerVY<0:
            value.playerY+=value.playerVY
        clock.tick(60)
        
        pygame.display.update()