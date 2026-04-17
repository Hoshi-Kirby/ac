import sys, random
import pygame, time
import value
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

def set():
    direction=0
    x=10
    y=50
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
            
            if random.randint(0, 3)>0:
                if direction==0:
                    direction = random.randint(-1, 1)
                else:
                    direction *= random.randint(0, 1)

def draw():
    for w in range(value.width-1):
        for h in range(value.height-1):
            if value.grid[w+value.scroll][h]==1:
                pygame.draw.rect(value.screen, (255,255,255), (w*value.size, h*value.size, value.size, value.size))
