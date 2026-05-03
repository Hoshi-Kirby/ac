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

m=3
n=4
image=[[0] * n for _ in range(m+1)]
for j in range(m):
    for i in range(n):
        image[j+1][i]=func.imageLoad(2,f"enemyImage/enemy{j+1}-{i}.png",255)[0]
        image[j+1][i]=pygame.transform.flip(image[j+1][i], True, False)

def search(x):
    for h in range(value.height):
        for w in range(int(value.playerWidth/value.size)+1):
            if value.grid[x+w][h]==1:
                return h-value.playerHeight/value.size-1

def set(l,r):
    for i in range(value.nE):
        x=random.randint(l,r)
        value.enemyX[i]=x
        value.enemyY[i]=search(x)
        value.enemyType[i]=random.randint(1,3)

def draw():
    for i in range(value.nE):
        drawImage(i,value.enemyWalkPause[i])

def drawImage(a,b):
    func.ImageDraw(image[value.enemyType[a]][b],(value.enemyX[a]-value.scroll)*value.size,value.enemyY[a]*value.size)

def calc():
    for i in range(value.nE):
        if value.enemyVX[i]==0:
            value.enemyWalkTime[i]=0
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
            value.enemyVX[i]=random.randint(-1,1)
        if random.randint(0,10)==0:
            value.enemyVX[i]*=-1