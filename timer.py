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

    for i in range(value.nE):
        if not stage.isHit(value.enemyX[i],value.enemyY[i],value.playerWidth,value.playerHeight) or value.enemyVY[i]<=0:
            value.enemyVY[i]+=0.1
        else:
            value.enemyVY[i]=0
        if not stage.isHit(value.enemyX[i],value.enemyY[i],value.playerWidth,value.playerHeight) and value.enemyVY[i]>0 and value.enemyY[i]<value.height-value.playerHeight/value.size*2:
            for j in range(int(value.enemyVY[i]*10)):
                if stage.isHit(value.enemyX[i],value.enemyY[i],value.playerWidth,value.playerHeight):
                    break
                value.enemyY[i]+=0.1
        d = 1 if value.enemyVX[i] >= 0 else -1
        for j in range(abs(value.enemyVX[i])):
            if stage.isHit(value.enemyX[i]+d,value.enemyY[i],value.playerWidth,value.playerHeight-1):
                break
            if value.enemyX[i]>value.maxWidth-math.ceil(value.playerWidth/value.size)-2 and d==1:
                break
            if value.enemyX[i]<2 and d==-1:
                break
            value.enemyX[i]+=d