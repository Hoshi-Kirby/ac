import sys, random
import pygame, time
import value
import func
import stage
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

sword=func.imageLoad(2,"image/sword.png",255)[0]
sword_f=pygame.transform.flip(sword, True, False)
sword = pygame.transform.rotate(sword, -45)
sword_f = pygame.transform.rotate(sword_f, 45)
ss=2

def calc():
    if value.throwTime>0:
        if not value.swordIsLeft:
            if not stage.isHit(value.swordX+ss-value.playerWidth/value.size/2+1,value.swordY-1,value.playerWidth,value.playerHeight):
                value.swordX+=ss
            else:
                value.throwTime=0
                value.fallTime=5
        else:
            if not stage.isHit(value.swordX-ss,value.swordY-1,value.playerWidth,value.playerHeight):
                value.swordX-=ss
            else:
                value.throwTime=0
                value.fallTime=5

def draw():
    if value.throwTime>0:
        if not value.swordIsLeft:
            value.screen.blit(sword,((value.swordX-value.scroll)*value.size-value.playerWidth,value.swordY*value.size))
        else:
            value.screen.blit(sword_f,((value.swordX-value.scroll)*value.size,value.swordY*value.size))
    if value.fallTime>0:
        if not value.swordIsLeft:
            value.screen.blit(sword,((value.swordX-value.scroll)*value.size-value.playerWidth,(value.swordY+(5-value.fallTime))*value.size))
        else:
            value.screen.blit(sword_f,((value.swordX-value.scroll)*value.size,(value.swordY+(5-value.fallTime))*value.size))
