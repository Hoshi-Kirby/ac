import sys, random
import pygame, time
import math
import value
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

ground = pygame.Surface((value.size, value.size), pygame.SRCALPHA)
pygame.draw.rect(ground, (200, 250, 60, 120), (0, 0, value.size, value.size))
face=(0,100,0)

def set(t):
    global face
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
            
            if y<=40:
                if direction==0:
                    direction = random.randint(0, 5)
                    if direction!=1:
                        direction=0
                else:
                    direction = 0
            elif y>=value.height-10:
                if direction==0:
                    direction = random.randint(-5, 0)
                    if direction!=-1:
                        direction=0
                else:
                    direction = 0
            else:
                if direction==0:
                    direction = random.randint(-5, 5)
                else:
                    direction *= random.randint(0, 5)
                if direction!=-1 and direction!=1:
                    direction=0

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
                
                if random.randint(0, 3)>2:
                    if direction==0:
                        direction = random.randint(-1, 1)
                    else:
                        direction *= random.randint(0, 1)
    
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
                direction = random.randint(-1, 1)
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
                    if random.randint(0, 1)==0:
                        direction = random.randint(-1, 1)
                else:
                    direction *= random.randint(0, 10)
                if direction!=0:
                    direction=int(direction/abs(direction))
    if t==5:
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

    if t==0:
        pygame.draw.rect(ground, (200, 250, 60, 120), (0, 0, value.size, value.size))
        face=(0,100,0)
    elif t==1:
        pygame.draw.rect(ground, (100, 80, 50, 180), (0, 0, value.size, value.size))
        face=(50,100,0)
    elif t==2:
        pygame.draw.rect(ground, (150, 200, 170, 120), (0, 0, value.size, value.size))
        face=(50,100,80)
    elif t==3:
        pygame.draw.rect(ground, (200, 200, 100, 120), (0, 0, value.size, value.size))
        face=(140,55,0)
    elif t==4:
        pygame.draw.rect(ground, (40, 60, 100, 180), (0, 0, value.size, value.size))
        face=(10,30,50)
    elif t==5:
        pygame.draw.rect(ground, (50, 70, 120, 120), (0, 0, value.size, value.size))
        face=(200,220,250)

def draw():
    for w in range(value.width):
        isg=False
        for h in range(value.height-1):
            if isg:
                value.screen.blit(ground, (w * value.size, h * value.size))
            if value.grid[w+value.scroll][h]==1:
                isg=True
                pygame.draw.rect(value.screen, face, (w*value.size, h*value.size, value.size, value.size))

def isHit(x,y,w,h):
    l=math.floor(x)
    r=math.ceil(x+w/value.size)
    u=math.floor(y)
    d=math.ceil(y+h/value.size)
    if 0<l and r<value.maxWidth and 0<u and d<value.height:
        found = any(
            value.grid[x][y] == 1
            for x in range(l, r + 1)
            for y in range(u, d + 1)
        )
    else:  found=False
    return found

def isFloor(d,x,y,w):
    if x-1+int(value.playerWidth/value.size)+2<value.maxWidth and d==-1:
        for i in range(int(value.playerWidth/value.size)+2):
            if value.grid[x-1+i][y]==1 and d==-1:
                return True
            if value.grid[x+2+int(w)+1-i][y]==1 and d==1:
                return True
    return False