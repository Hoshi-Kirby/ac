import sys, random
import pygame, time
import math
import value
import func
import stage
import arrow
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

m=8
n=4
k=2
image = [[[0] * k for _ in range(n)] for _ in range(m+1)]
for j in range(m):
    for i in range(n):
        image[j+1][i][0]=func.imageLoad(2,f"enemyImage/enemy{j+1}-{i}.png",255)[0]
        image[j+1][i][1]=pygame.transform.flip(image[j+1][i][0], True, False)

imageGhost = [[0] * k for _ in range(n)]
for i in range(n):
    imageGhost[i][0]=func.imageLoad(2,f"enemyImage/enemy{6}-{i}.png",120)[0]
    imageGhost[i][1]=pygame.transform.flip(imageGhost[i][0], True, False)

def search(x):
    for h in range(value.height):
        for w in range(int(value.playerWidth/value.size)+2):
            if value.grid[x+w][h]==1:
                return h-value.playerHeight/value.size-2

def set(l,r):
    value.enemyActive=[False]*value.nE
    value.enemyAlive=[1]*value.nE
    value.enemyHP=[5]*value.nE
    value.ghostTime=[0]*value.nE
    value.enemyVX=[0]*value.nE
    value.enemyVY=[0]*value.nE
    for i in range(value.nE):
        x=random.randint(l,r)
        value.enemyX[i]=x
        value.enemyY[i]=search(x)
        value.enemyType[i]=random.randint(1,8)

def draw():
    for i in range(value.nE):
        drawImage(i,value.enemyWalkPause[i]*value.enemyAlive[i])

def drawImage(a,b):
    c=int(-(func.sign(value.playerX-value.enemyX[a])-1)/2)
    if value.enemyAlive[a]==1:
        value.enemyDirect[a]=c
    else:
        c=value.enemyDirect[a]
    if value.ghostTime[a]>0:
        func.ImageDraw(imageGhost[b][c],(value.enemyX[a]-value.scroll)*value.size,value.enemyY[a]*value.size)
    else:
        func.ImageDraw(image[value.enemyType[a]][b][c],(value.enemyX[a]-value.scroll)*value.size,value.enemyY[a]*value.size)

def calc():
    for i in range(value.nE):
        if value.enemyVX[i]==0 and value.enemyType[i]!=8 and value.enemyType[i]!=6:
            value.enemyWalkTime[i]=0
            value.enemyWalkPause[i]=1
        else:
            value.enemyWalkTime[i]+=1
            if value.enemyWalkTime[i]>20:
                value.enemyWalkTime[i]=0
            if value.enemyWalkTime[i]==1:
                value.enemyWalkPause[i]=2
            if value.enemyWalkTime[i]==6:
                value.enemyWalkPause[i]=1
            if value.enemyWalkTime[i]==11:
                value.enemyWalkPause[i]=3
            if value.enemyWalkTime[i]==16:
                value.enemyWalkPause[i]=1
    
    for i in range(value.nE):
        if value.enemyAlive[i]==1:
            if value.playerX+50>value.enemyX[i] and value.enemyVX[i]==0:
                value.enemyActive[i]=True
            match value.enemyType[i]:
                case 8:
                    if random.randint(0,20)==0 and value.enemyActive[i]:
                        value.enemyVX[i]=random.randint(-1,1)
                    else:
                        value.enemyVX[i]=0
                case 4:
                    if random.randint(0,30)==0 and value.enemyActive[i]:
                        value.enemyVX[i]=func.sign(value.playerX-value.enemyX[i])
                    else:
                        if random.randint(0,2)==0:
                            value.enemyVX[i]=0
                case 5:
                    if value.enemyActive[i]:
                        if 0<value.enemyX[i]-value.playerX<20:
                            value.enemyVX[i]=1
                        elif 25<value.enemyX[i]-value.playerX:
                            value.enemyVX[i]=-1
                        elif 0>value.enemyX[i]-value.playerX>-20:
                            value.enemyVX[i]=-1
                        elif -25>value.enemyX[i]-value.playerX:
                            value.enemyVX[i]=1
                        else:
                            value.enemyVX[i]=0
                        if random.randint(0,30)==0:
                            arrow.enemyAdd(i)
                case 6:
                    if value.enemyActive[i]:
                        if value.ghostTime[i]==0 and random.randint(0,60)==0:
                            if (value.playerX-value.enemyX[i])**2+(value.playerY-value.enemyY[i])**2<1600:
                                value.ghostTime[i]=60
                        if value.ghostTime[i]<10:
                            if random.randint(0,20)==0:
                                value.enemyVX[i]=random.randint(-1,1)
                            else:
                                value.enemyVX[i]=0
                            if random.randint(0,20)==0:
                                value.enemyVY[i]=random.randint(-1,1)
                            else:
                                value.enemyVY[i]=0
                        else:
                            ghostDx=(value.playerX-value.enemyX[i])
                            ghostDy=(value.playerY-value.enemyY[i])
                            if abs(ghostDx)>abs(ghostDy):
                                value.enemyVX[i]=func.sign(ghostDx)
                            else:
                                value.enemyVY[i]=func.sign(ghostDy)
                    
                case 2:
                    if value.enemyActive[i]:
                        if abs(value.playerX-value.enemyX[i])<70:
                            if random.randint(0,20)==0:
                                value.enemyVX[i]=func.sign(value.playerX-value.enemyX[i])
                            else:
                                if random.randint(0,2)==0:
                                    value.enemyVX[i]=0
                            if stage.isHit(value.enemyX[i]+func.sign(value.playerX-value.enemyX[i]),value.enemyY[i],value.playerWidth,value.playerHeight-1):
                                if random.randint(0,10)==0:
                                    value.enemyVY[i]=-1


def alive():
    for i in range(value.nE):
        if value.enemyHP[i]<=0:
            value.enemyHP[i]=0
            value.enemyAlive[i]=0