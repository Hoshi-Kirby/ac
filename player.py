import sys, random
import pygame, time
import value
import func
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

player=[]
player.append(func.imageLoad(2,"image/player_1.png",255)[0])
player.append(func.imageLoad(2,"image/player_2.png",255)[0])
player.append(func.imageLoad(2,"image/player_3.png",255)[0])
player.append(pygame.transform.flip(player[0], True, False))
player.append(pygame.transform.flip(player[1], True, False))
player.append(pygame.transform.flip(player[2], True, False))
value.playerWidth,value.playerHeight=func.imageLoad(2,"image/player_1.png",255)[1:]
value.playerWidth-=value.size*2
value.playerHeight-=value.size

def draw(i,x,y):
    value.screen.blit(player[i],(x,y))