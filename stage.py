import sys, random
import pygame, time
import math
import value
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

def set(t):
    direction=0
    x=10
    y=value.lastY
    for j in range(10):
        value.grid[j][y]=1

    if t==0:
        while x<value.maxWidth-10:
            for j in range(2):
                value.grid[x][y]=1
                if direction==0:
                    x+=1
                else:
                    y+=direction
            
            if y<=10:
                if direction==0:
                    direction = random.randint(0, 1)
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-1, 0)
                else:
                    direction = 0
            else:
                
                if random.randint(0, 4)>1:
                    if direction==0:
                        direction = random.randint(-1, 1)
                    else:
                        direction *= random.randint(0, 1)
    if t==1:
        while x<value.maxWidth-10:
            for j in range(2):
                value.grid[x][y]=1
                if direction==0:
                    x+=1
                else:
                    y+=direction
            
            if y<=10:
                if direction==0:
                    direction = random.randint(0, 1)
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-1, 0)
                else:
                    direction = 0
            else:
                
                if direction==0:
                    direction = random.randint(-1, 1)
                else:
                    direction *= random.randint(0, 1)
    if t==2:
        while x<value.maxWidth-10:
            for j in range(2):
                value.grid[x][y]=1
                if direction==0:
                    x+=1
                else:
                    y+=direction
            
            if y<=10:
                if direction==0:
                    direction = random.randint(0, 1)
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-1, 0)
                else:
                    direction = 0
            else:
                direction = random.randint(-1, 1)
    if t==3:
        while x<value.maxWidth-10:
            for j in range(2):
                value.grid[x][y]=1
                if direction==0:
                    x+=1
                else:
                    y+=direction
            
            if y<=10:
                if direction==0:
                    direction = random.randint(0, 1)
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-1, 0)
                else:
                    direction = 0
            else:
                if direction==0:
                    if random.randint(0, 1)==0:
                        direction = random.randint(-1, 1)
                else:
                    direction *= random.randint(0, 10)
                if direction!=0:
                    direction=int(direction/abs(direction))
    if t==4:
        while x<value.maxWidth-10:
            for j in range(2):
                value.grid[x][y]=1
                if direction==0:
                    x+=1
                else:
                    y+=direction
            
            if y<=10:
                if direction==0:
                    direction = random.randint(0, 1)
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-1, 0)
                else:
                    direction = 0
            else:
                if direction==0:
                        direction = random.randint(-4, 4)
                else:
                    direction *= random.randint(-1, 6)
                if direction!=0:
                    direction=int(direction/abs(direction))
    
    for j in range(10):
        value.grid[value.maxWidth-j-1][y]=1
    value.lastY=y

def draw():
    for w in range(value.width-1):
        for h in range(value.height-1):
            if value.grid[w+value.scroll][h]==1:
                pygame.draw.rect(value.screen, (255,255,255), (w*value.size, h*value.size, value.size, value.size))

def isHit(x,y,w,h):
    l=math.floor(x)
    r=math.ceil(x+w/value.size)
    u=math.floor(y)
    d=math.ceil(y+h/value.size)
    if 0<l and r<value.maxWidth:
        found = any(
            value.grid[x][y] == 1
            for x in range(l, r + 1)
            for y in range(u, d + 1)
        )
    else:  found=False
    return found