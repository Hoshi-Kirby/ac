import sys, random
import pygame, time
import value
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

width = 150
maxWidth=1000
height = 100
size =5

screen = pygame.display.set_mode((width*size, height*size))
pygame.display.set_caption("action")

step=1

lastY=50

grid = [[0] * height for _ in range(maxWidth)]

scroll=0

playerX=6
playerY=43
playerVY=0
playerWidth=0
playerHeight=0
playerPauseTime=0
playerPause=0
playerIsLeft=0

jumpTime=0

dashTimeA=0
dashTimeD=0
dashLeftTime=0
dashRightTime=0
dashCoolTime=0

atackTime=0
slash=False
slashTime=0
throwTime=0
fallTime=0
swordX=0
swordY=0
swordIsLeft=False


def reset():
    value.step=1
    value.grid = [[0] * value.height for _ in range(value.maxWidth)]
    
    value.scroll=0

    value.playerX=6
    value.playerY=value.lastY-7
    value.playerVY=0
    value.playerPauseTime=0
    value.playerPause=0
    value.playerIsLeft=0

    value.dashTimeA=0
    value.dashTimeD=0
    value.dashLeftTime=0
    value.dashRightTime=0
    value.dashCoolTime=0

    value.atackTime=0
    value.slash=False
    value.slashTime=0
