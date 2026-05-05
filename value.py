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
swordVX=0
swordVY=0
swordIsLeft=False
dameX=0
dameY=0

player2X=[6]*120
player2Y=[43]*120
player2Pause=[0]*120
player2IsLeft=[0]*120
player2AtackTime=[0]*120
player2ThrowTime=[0]*120
player2A=[False]*120
player2C=[False]*120
pressShiftTime=0

isW=False
isS=False
is2W=[False]*120
is2S=[False]*120

arrows=[]
class Arrow:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.alive = True

    def update(self):
        self.x +=self.vx
        self.y +=self.vy

nE=10
enemyType=[0]*nE
enemyX=[0]*nE
enemyY=[0]*nE
enemyVX=[0]*nE
enemyVY=[0]*nE
enemyIsAtack=[0]*nE
enemyWalkPause=[1]*nE
enemyWalkTime=[0]*nE
enemyActive=[False]*nE
enemyAlive=[1]*nE
enemyDirect=[0]*nE
enemyHP=[0]*nE
enemyIsSlash=[False]*nE
enemyBackTime=[0]*nE

enemyArrows=[]
class EnemyArrow:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.alive = True

    def update(self):
        self.x +=self.vx
        self.y +=self.vy

ghostTime=[0]*nE
roboWalkTime=[0]*nE
moguMoguTime=[0]*nE
moguNotice=[0]*nE
roboMoveTime=[1]*nE
roboAtackTime=[0]*nE

fireBalls=[]
class FireBall:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.alive = True

    def update(self):
        self.x +=self.vx
        self.y +=self.vy

fireTime=0

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
