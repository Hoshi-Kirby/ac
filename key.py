import sys, random
import pygame, time
import math
import value
import func
import stage
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

def event1(key):
    if key==K_SPACE:
        if stage.isHit(value.playerX,value.playerY,value.playerWidth,value.playerHeight):
            value.playerVY=-2
            value.jumpTime=0
        elif stage.isHit(value.playerX+1,value.playerY,value.playerWidth,value.playerHeight) and value.playerIsLeft==0:
            value.playerVY=-2
            value.dashLeftTime=4
            value.playerIsLeft=3-value.playerIsLeft
            value.jumpTime=0
        elif stage.isHit(value.playerX-1,value.playerY,value.playerWidth,value.playerHeight) and value.playerIsLeft==3:
            value.playerVY=-2
            value.dashRightTime=4
            value.playerIsLeft=3-value.playerIsLeft
            value.jumpTime=0
    if key==K_r:
        value.step=0
    if key==K_a:
        value.playerIsLeft=3
    if key==K_d:
        value.playerIsLeft=0
    if key==K_RETURN:
        value.player2A[119]=True
        if value.slashTime==0:
            value.atackTime=6
            value.slashTime=12
        else:
            if value.slash:
                value.atackTime=6
                value.slashTime=12
                value.slash=False
            else:
                value.atackTime=0
                value.slash=True
    if key==K_RSHIFT:
        if value.throwTime==0 and value.fallTime==0:
            value.player2C[119]=True
            value.throwTime=12
            value.swordX=value.playerX
            value.swordY=value.playerY
            value.swordIsLeft=value.playerIsLeft==3
    if value.dashCoolTime==0:
        if value.dashTimeA>0:
            if key==K_a:
                value.dashLeftTime=6
                value.dashCoolTime=20
        if value.dashTimeD>0:
            if key==K_d:
                value.dashRightTime=6
                value.dashCoolTime=20
        if key==K_a:
            value.dashTimeA=15
            value.dashTimeD=0
        if key==K_d:
            value.dashTimeA=0
            value.dashTimeD=15

    
def pressed1():
    pressed_keys = pygame.key.get_pressed()

    if value.dashLeftTime>0:
        for i in range(2):
            if value.playerX>0 and not stage.isHit(value.playerX-1,value.playerY-1,value.playerWidth,value.playerHeight):
                value.playerX-=1
    if value.dashRightTime>0:
        for i in range(2):
            if value.playerX<value.maxWidth and not stage.isHit(value.playerX+1,value.playerY-1,value.playerWidth,value.playerHeight):
                value.playerX+=1

    if pressed_keys[K_SPACE]:
        if 0<=value.jumpTime<10:
            value.jumpTime+=1
    else:
        if 0<=value.jumpTime<10:
            value.jumpTime+=1
        if value.jumpTime==6:
            value.playerVY=-0.8

    if pressed_keys[K_LSHIFT]:
        if value.pressShiftTime<118:
            value.pressShiftTime+=1
    else:
        if value.pressShiftTime>0:
            value.pressShiftTime-=2


    if pressed_keys[K_d] ^ pressed_keys[K_a]:
        value.playerPauseTime+=1
        if value.playerPauseTime>20:
            value.playerPauseTime=0
        if value.playerPauseTime==1:
            value.playerPause=1
        if value.playerPauseTime==6:
            value.playerPause=0
        if value.playerPauseTime==11:
            value.playerPause=2
        if value.playerPauseTime==16:
            value.playerPause=0
        
        if pressed_keys[K_d]:
            if not stage.isHit(value.playerX+1,value.playerY-1,value.playerWidth,value.playerHeight):
                if value.playerX<value.maxWidth-math.ceil(value.playerWidth/value.size)-2:
                    value.playerX+=1
                else:
                    value.step=0
                if value.playerX-value.scroll>=value.width/2 and value.scroll<value.maxWidth-value.width:
                    value.scroll+=1
                if value.playerX-value.scroll>value.width/2 and value.scroll<value.maxWidth-value.width:
                        value.scroll+=1
            value.playerIsLeft=0
        if pressed_keys[K_a]:
            if not stage.isHit(value.playerX-1,value.playerY-1,value.playerWidth,value.playerHeight):
                if value.playerX>1:
                    value.playerX-=1
                if value.playerX-value.scroll<=value.width/2 and value.scroll>0:
                    value.scroll-=1
                    if value.playerX-value.scroll<value.width/2 and value.scroll>0:
                        value.scroll-=1
            value.playerIsLeft=3
    else:
        value.playerPause=0
        value.playerPauseTime=0
        if value.dashTimeA>0:
            value.dashTimeA-=1
        if value.dashTimeD>0:
            value.dashTimeD-=1
        if value.dashCoolTime>0:
            value.dashCoolTime-=1
