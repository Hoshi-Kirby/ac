import sys, random
import pygame, time
import value
import func
import stage
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

playerA=func.imageLoad(2,"image/player_A.png",255)[0]
playerA_f=pygame.transform.flip(playerA, True, False)
sword=func.imageLoad(2,"image/sword.png",255)[0]
sword_f=pygame.transform.flip(sword, True, False)
slash=func.imageLoad(2,"image/slash.png",255)[0]
slash_f=pygame.transform.flip(slash, True, False)
slash2=pygame.transform.flip(slash, False, True)
slash2_f=pygame.transform.flip(slash_f, False, True)

def draw(i,a,t,x,y):
    if a==0 and t==0:
        value.screen.blit(player[i],(x,y))
    elif a>0:
        if i<3:
            value.screen.blit(playerA,(x,y))
            rotated_image = pygame.transform.rotate(sword, 180*a/6-135)
            value.screen.blit(rotated_image,(x+value.playerWidth/3,y))
            if 0<a<5 and not value.slash:
                value.screen.blit(slash,(x+value.playerWidth,y))
            if 1<a<=6 and value.slash:
                value.screen.blit(slash2,(x+value.playerWidth,y))
        else:
            value.screen.blit(playerA_f,(x,y))
            rotated_image = pygame.transform.rotate(sword_f, -180*a/6+135)
            value.screen.blit(rotated_image,(x-value.playerWidth/2,y))
            if 0<a<5 and not value.slash:
                value.screen.blit(slash_f,(x-value.playerWidth,y))
            if 1<a<=6 and value.slash:
                value.screen.blit(slash2_f,(x-value.playerWidth,y))
    elif t>0:
        if i<3:
            value.screen.blit(playerA,(x,y))
        else:
            value.screen.blit(playerA_f,(x,y))