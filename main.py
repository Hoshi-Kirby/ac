import sys, random
import pygame, time
import stage 
import value
import func
import player
import key
import sword
import arrow
import timer
import p2
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

bgData = []

bgData.append(func.imageLoad(2, "image/sougen.png", 255))
bgData.append(func.imageLoad(2, "image/sinrin.png", 255))
bgData.append(func.imageLoad(2, "image/sabaku.png", 255))
bgData.append(func.imageLoad(2, "image/toshi.png", 255))
bgData.append(func.imageLoad(2, "image/dokutu.png", 255))

while True:
    if value.step==0:
        value.reset()
    if value.step==1:
        stage.set(4)
    while value.step==1:
        func.draw_bg(bgData[3][0], value.scroll, 4800,bgData[3][1],bgData[3][2])
        stage.draw()
        arrow.add0()
        p2t=59-int(value.pressShiftTime/2)
        p2.draw(value.player2Pause[p2t]+value.player2IsLeft[p2t],value.player2AtackTime[p2t],value.player2ThrowTime[p2t],(value.player2X[p2t]-value.scroll)*value.size,value.player2Y[p2t]*value.size)
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
        arrow.addCheck(p2t)
        arrow.calc()
        arrow.draw()

        p2.memo()

        timer.dec1()
        clock.tick(60)
        
        pygame.display.update()