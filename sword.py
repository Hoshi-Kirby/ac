import sys, random
import pygame, time
import value
import func
import stage
import enemy
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

sword=func.imageLoad(2,"image/sword.png",255)[0]
sword_f=pygame.transform.flip(sword, True, False)
sword = pygame.transform.rotate(sword, -45)
sword_f = pygame.transform.rotate(sword_f, 45)
sword_d = pygame.transform.rotate(sword, 90)
sword_u = pygame.transform.rotate(sword, -90)

def calc():
    if value.throwTime>0:
        if not value.swordIsLeft:
            if not stage.isHit(value.swordX+value.swordVX-value.playerWidth/value.size/2+1,value.swordY-1+value.swordVY,value.playerWidth,value.playerHeight):
                value.swordX+=value.swordVX
                value.swordY+=value.swordVY
            else:
                value.throwTime=0
                value.fallTime=5
        else:
            if not stage.isHit(value.swordX-value.swordVX,value.swordY-1+value.swordVY,value.playerWidth,value.playerHeight):
                value.swordX-=value.swordVX
                value.swordY+=value.swordVY
            else:
                value.throwTime=0
                value.fallTime=5

        for i in range(value.nE):
            if func.spHitSp(value.swordX,value.swordY,value.playerWidth/value.size,value.playerHeight/value.size,value.enemyX[i],value.enemyY[i],value.playerWidth/value.size,value.playerHeight/value.size):    
                if value.ghostTime[i]<20 and value.moguMoguTime[i]==0:
                    value.enemyHP[i]-=1
                    value.throwTime=0
                    enemy.nockBack(i)

def draw():
    if value.throwTime>0:
        if value.swordVY>0:
            image=sword_u
            image_f=sword_u
        elif value.swordVY<0:
            image=sword_d
            image_f=sword_d
        else:
            image=sword
            image_f=sword_f
        if not value.swordIsLeft:
            value.screen.blit(image,((value.swordX-value.scroll)*value.size-value.playerWidth/3,value.swordY*value.size))
        else:
            value.screen.blit(image_f,((value.swordX-value.scroll)*value.size,value.swordY*value.size))
    if value.fallTime>0:
        if value.swordVY==0:
            if not value.swordIsLeft:
                value.screen.blit(sword,((value.swordX-value.scroll)*value.size-value.playerWidth,(value.swordY+(5-value.fallTime))*value.size))
            else:
                value.screen.blit(sword_f,((value.swordX-value.scroll)*value.size,(value.swordY+(5-value.fallTime))*value.size))
