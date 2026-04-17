import sys, random
import pygame, time
import value
import func
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

player=[]
player.append(func.imageLoad(2,"image/player_1.png",255))
player.append(func.imageLoad(2,"image/player_2.png",255))
player.append(func.imageLoad(2,"image/player_3.png",255))

def draw(i,x,y):
    value.screen.blit(player[i],(x,y))