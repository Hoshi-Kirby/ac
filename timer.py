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

def dec1():
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
    if value.atackTime>0 and not value.slash:
        value.atackTime-=1
    if value.atackTime<6 and value.slash:
        value.atackTime+=1
        if value.atackTime==6:
            value.atackTime=0
            value.slash=False
    if value.slashTime>0:
        value.slashTime-=1
    if value.throwTime>0:
        value.throwTime-=1
    if value.fallTime>0:
        value.fallTime-=1