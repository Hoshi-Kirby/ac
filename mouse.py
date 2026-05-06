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

def event1(button):
    if button==1:
        if value.throwTime==0 and value.fallTime==0:
            value.enemyIsSlash=[False]*value.nE
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
    if button==3:
        if value.throwTime==0 and value.fallTime==0:
            value.player2C[119]=True
            value.throwTime=12
            value.swordX=value.playerX
            value.swordY=value.playerY
            if value.isW ^ value.isS:
                if value.isW:
                    value.swordVX=0
                    value.swordVY=-2
                else:
                    value.swordVX=0
                    value.swordVY=2
            else:
                value.swordVX=2
                value.swordVY=0
            value.swordIsLeft=value.playerIsLeft==3