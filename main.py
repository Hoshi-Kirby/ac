import sys, random
import pygame, time
import stage 
import value
import func
import player
import enemy
import key
import mouse
import sword
import arrow
import fire
import timer
import p2
import title
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

bgData = []

bgData.append(func.imageLoad(2, "image/sougen.png", 255))
bgData.append(func.imageLoad(2, "image/sinrin.png", 255))
bgData.append(func.imageLoad(2, "image/kaitei.png", 255))
bgData.append(func.imageLoad(2, "image/sabaku.png", 255))
bgData.append(func.imageLoad(2, "image/toshi.png", 255))
bgData.append(func.imageLoad(2, "image/dokutu.png", 255))
bgData.append(func.imageLoad(2, "image/oshiro.png", 255))
titleImage=func.imageLoad(2, "image/titleImage.png", 255)

value.enemyWidth=[value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth,value.playerWidth*4+10]
value.enemyHeight=[value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight,value.playerHeight*4+10]

value.level=0
while True:
    if value.step==0:
        value.reset()
        if not value.isTitle:
            value.step=1
        else:
            value.isTitle=False
    while value.step==0:
        title.draw_bg(titleImage[0],titleImage[1],titleImage[2])
        title.draw_logo(value.width*value.size/2,150,0)
        for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        key.event0(event.key)
                    if event.type == MOUSEBUTTONDOWN:
                        mouse.event0(event.button)
        clock.tick(60)
        
        pygame.display.update()
    if value.step==1:
        value.level+=1
        match(value.level):
            case 1|2|3:
                sb=0
                value.nE=20
            case 4|5|6:
                sb=1
                value.nE=20
            case 7|8|9:
                sb=2
                value.nE=15
            case 10|11|12:
                sb=3
                value.nE=10
            case 13|14|15:
                sb=4
                value.nE=9
            case 16|17|18:
                sb=5
                value.nE=8
            case 19:
                sb=6
                value.nE=1
            case _:
                sb=random.randint(0,5)
                value.nE=10
        stage.set(sb)
        enemy.set(10,value.maxWidth-10)
    while value.step==1:
        func.draw_bg(bgData[sb][0], value.scroll, 4800,bgData[sb][1],bgData[sb][2])
        stage.draw()
        arrow.add0()
        p2t=59-int(value.pressShiftTime/2)
        p2.draw(value.player2Pause[p2t]+value.player2IsLeft[p2t]*4,value.player2AtackTime[p2t],value.player2ThrowTime[p2t],(value.player2X[p2t]-value.scroll)*value.size,value.player2Y[p2t]*value.size)
        player.draw(value.playerPause+value.playerIsLeft*4,value.atackTime,value.throwTime,value.playerDamageTime,(value.playerX-value.scroll)*value.size,value.playerY*value.size)              
        enemy.draw()
        fire.draw()

        player.drawHP()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key.event1(event.key)
            if event.type == MOUSEBUTTONDOWN:
                mouse.event1(event.button)

        key.pressed1()
        value.playerMaxHP=max(value.playerMaxHP,value.playerHP)

        sword.calc()
        sword.draw()
        arrow.addCheck(p2t)
        arrow.calc()
        arrow.draw()
        enemy.calc()
        enemy.alive()
        fire.calc()
        enemy.isHit()
        enemy.heart()

        p2.memo()

        timer.dec1()
        clock.tick(60)
        
        pygame.display.update()