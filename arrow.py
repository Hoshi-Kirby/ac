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

arrow=func.imageLoad(2,"image/arrow.png",255)[0]
arrow_f=pygame.transform.flip(arrow, True, False)
arrow = pygame.transform.rotate(arrow, -45)
arrow_f = pygame.transform.rotate(arrow_f, 45)

def add0():
    value.player2A[119]=0
    value.player2C[119]=0

def addA(p2t):
    if value.player2IsLeft[p2t]==0:
        value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],2,0))
    else:
        value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],-2,0))
def addC(p2t):
    if value.player2IsLeft[p2t]==0:
        value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],2,-1))
    else:
        value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],-2,-1))

def addCheck(p2t):
    if value.player2A[p2t]:
        value.player2A[p2t]=False
        addA(p2t)
    if p2t!=0 and value.player2A[p2t-1]:
        value.player2A[p2t-1]=False
        addA(p2t)
    if value.player2C[p2t]:
        value.player2C[p2t]=False
        addC(p2t)
    if p2t!=0 and value.player2C[p2t-1]:
        value.player2C[p2t-1]=False
        addC(p2t)

def calc():
    for ar in value.arrows:
        ar.vy += 0.1
        ar.update()
        if stage.isHit(ar.x,ar.y,value.playerWidth,value.playerHeight):
            ar.alive = False
    value.arrows = [a for a in value.arrows if a.alive]

def draw():
    for ar in value.arrows:
        angle = math.atan2(ar.vy, ar.vx)
        angle_deg = math.degrees(angle)

        img = arrow if ar.vx > 0 else arrow_f
        rotated = pygame.transform.rotate(img, -angle_deg)

        value.screen.blit(
            rotated,
            ((ar.x - value.scroll) * value.size, ar.y * value.size)
        )