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

def search(x):
    for h in range(value.height):
        for w in range(int(value.playerWidth/value.size)+1):
            if value.grid[x+w][h]==1:
                return h-value.playerHeight/value.size-1

def set(l,r):
    value.enemyActive=[False]*value.nE
    for i in range(value.nE):
        x=random.randint(l,r)
        value.enemyX[i]=x
        value.enemyY[i]=search(x)
        value.enemyType[i]=random.randint(1,8)

def draw():
    for i in range(value.nE):
        drawImage(i,value.enemyWalkPause[i])

def drawImage(a,b):
    c=int(-(func.sign(value.playerX-value.enemyX[a])-1)/2)
    func.ImageDraw(image[value.enemyType[a]][b][c],(value.enemyX[a]-value.scroll)*value.size,value.enemyY[a]*value.size)

def calc():
    for i in range(value.nE):
        if value.enemyVX[i]==0 and value.enemyType[i]!=8:
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