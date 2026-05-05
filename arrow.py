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

arrow=func.imageLoad(2,"image/arrow.png",255)[0]
arrow_f=pygame.transform.flip(arrow, True, False)
arrow = pygame.transform.rotate(arrow, -45)
arrow_f = pygame.transform.rotate(arrow_f, 45)

def add0():
    value.player2A[119]=0
    value.player2C[119]=0

def addA(p2t):
    if value.player2IsLeft[p2t]==0:
        if value.is2W[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0,-4))
        elif value.is2S[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0,1))
        else:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],3,-0.2))
    else:
        if value.is2W[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0,-4))
        elif value.is2S[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0,2))
        else:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],-3,-0.2))
def addC(p2t):
    if value.player2IsLeft[p2t]==0:
        if value.is2W[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0.2,-3))
        elif value.is2S[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],0.2,1))
        else:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],2,-1))
    else:
        if value.is2W[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],-0.2,-3))
        elif value.is2S[p2t]:
            value.arrows.append(value.Arrow(value.player2X[p2t],value.player2Y[p2t],-0.2,1))
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
        for i in range(value.nE):
            if func.spHitSp(ar.x,ar.y,value.playerWidth/value.size,value.playerHeight/value.size,value.enemyX[i],value.enemyY[i],value.playerWidth/value.size,value.playerHeight/value.size):
                if value.enemyType[i]==2 or value.enemyType[i]==3:
                    ar.vx*=-1
                    ar.vy*=-1
                elif value.ghostTime[i]<20 and value.moguMoguTime[i]==0:
                    ar.alive = False
                    value.enemyHP[i]-=2
                    enemy.nockBack(i)
    value.arrows = [a for a in value.arrows if a.alive]
    for ar in value.enemyArrows:
        ar.vy += 0.02
        ar.update()
        if stage.isHit(ar.x,ar.y,value.playerWidth,value.playerHeight):
            ar.alive = False
        if func.spHitSp(ar.x,ar.y,value.playerWidth/value.size,value.playerHeight/value.size,value.playerX,value.playerY,value.playerWidth/value.size,value.playerHeight/value.size):
            ar.alive = False
    value.enemyArrows = [a for a in value.enemyArrows if a.alive]


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
    for ar in value.enemyArrows:
        angle = math.atan2(ar.vy, ar.vx)
        angle_deg = math.degrees(angle)

        img = arrow if ar.vx > 0 else arrow_f
        rotated = pygame.transform.rotate(img, -angle_deg)

        value.screen.blit(
            rotated,
            ((ar.x - value.scroll) * value.size, ar.y * value.size)
        )


def calc_trajectory(ex, ey, px, py, v):
    g=0.02
    dx = px - ex
    dy = ey-py-value.playerHeight/value.size/2
    D = v**4 - g * (g * dx**2 + 2 * dy * v**2)
    if D < 0 or dx==0:
        return None  # 届かない
    sqrtD = math.sqrt(D)
    tan1 = (v**2 - sqrtD) / (g * dx)
    tan2 = (v**2 + sqrtD) / (g * dx)

    angles = [math.atan(tan1), math.atan(tan2)]

    for theta in angles:
        vx = v * math.cos(theta)
        vy = v * math.sin(theta)

        if dx < 0:
            vx = -vx
        else:
            vy = -vy

        return vx, vy
    return None

def enemyAdd(i):
    s= random.uniform(0, 1)
    ex = value.enemyX[i]
    ey = value.enemyY[i]
    px = value.playerX
    py = value.playerY
    result = calc_trajectory(ex,ey,px,py,s)
    if not(result is None):
        vx, vy = result
        value.enemyArrows.append(
            value.Arrow(ex, ey-int(value.playerHeight/value.size), vx, vy)
        )