import sys, random
import pygame, time
import math
import value
import func
import stage
import enemy
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

fire1=func.imageLoad(2,"image/fire1.png",255)[0]
fire2=func.imageLoad(2,"image/fire2.png",255)[0]

def calc():
    for fb in value.fireBalls:
        fb.update()
        if stage.isHit(int(fb.x/value.size),int(fb.y/value.size),value.playerWidth,value.playerHeight):
            fb.alive = False
        if func.spHitSp(int(fb.x/value.size),int(fb.y/value.size),value.playerWidth/value.size,value.playerHeight/value.size,value.playerX,value.playerY,value.playerWidth/value.size,value.playerHeight/value.size):
            fb.alive = False
            value.playerHP-=1
            value.playerDamageTime=10
        if value.throwTime>0 and func.spHitSp(int(fb.x/value.size),int(fb.y/value.size),value.playerWidth/value.size,value.playerHeight/value.size,value.swordX,value.swordY,value.playerWidth/value.size,value.playerHeight/value.size):
            fb.alive = False
        if value.atackTime>0 and func.spHitSp(int(fb.x/value.size),int(fb.y/value.size),value.playerWidth/value.size,value.playerHeight/value.size,value.playerX+value.dameX/value.size,value.playerY+value.dameY/value.size,value.playerWidth/value.size,value.playerHeight/value.size):
            fb.alive = False
        for ar in value.arrows:
            if func.spHitSp(int(fb.x/value.size),int(fb.y/value.size),value.playerWidth/value.size,value.playerHeight/value.size,ar.x,ar.y,value.playerWidth/value.size,value.playerHeight/value.size):
                fb.alive = False
                ar.alive = False
        if fb.y<-value.playerHeight:
            fb.alive = False
    value.fireBalls = [a for a in value.fireBalls if a.alive]


def draw():
    for fb in value.fireBalls:
        if value.fireTime<15:
            value.screen.blit(fire1,(fb.x - value.scroll* value.size, fb.y))
        else:
            value.screen.blit(fire2,(fb.x - value.scroll* value.size, fb.y))


def add(i):
    ex = value.enemyX[i]*value.size
    ey = value.enemyY[i]*value.size
    px = value.playerX*value.size
    py = value.playerY*value.size
    r=1
    vx=(px-ex)/math.sqrt((px-ex)**2+(py-ey)**2)/r
    vy=(py-ey)/math.sqrt((px-ex)**2+(py-ey)**2)/r
    value.fireBalls.append(value.Arrow(ex, ey, vx, vy))