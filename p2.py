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

playerC=func.imageLoad(2,"image/player_C.png",255)[0]
playerC_f=pygame.transform.flip(playerC, True, False)
sword=func.imageLoad(2,"image/sword.png",255)[0]
sword_f=pygame.transform.flip(sword, True, False)
slash=func.imageLoad(2,"image/slash.png",255)[0]
slash_f=pygame.transform.flip(slash, True, False)
slash2=pygame.transform.flip(slash, False, True)
slash2_f=pygame.transform.flip(slash_f, False, True)

for i in range(6):
    dark_surface = pygame.Surface(player[i].get_size(), pygame.SRCALPHA)
    dark_surface.fill((100, 100, 100, 255))
    player[i].blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
dark_surface = pygame.Surface(playerC.get_size(), pygame.SRCALPHA)
dark_surface.fill((100, 100, 100, 255))
playerC.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
dark_surface = pygame.Surface(playerC_f.get_size(), pygame.SRCALPHA)
dark_surface.fill((100, 100, 100, 255))
playerC_f.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def memo():
    for i in range(119):
        value.player2X[i]=value.player2X[i+1]
        value.player2Y[i]=value.player2Y[i+1]
        value.player2Pause[i]=value.player2Pause[i+1]
        value.player2IsLeft[i]=value.player2IsLeft[i+1]
        value.player2AtackTime[i]=value.player2AtackTime[i+1]
        value.player2ThrowTime[i]=value.player2ThrowTime[i+1]
        value.player2A[i]=value.player2A[i+1]
        value.player2C[i]=value.player2C[i+1]
        value.is2W[i]=value.is2W[i+1]
        value.is2S[i]=value.is2S[i+1]
    value.player2X[119]=value.playerX
    value.player2Y[119]=value.playerY
    value.player2Pause[119]=value.playerPause
    value.player2IsLeft[119]=value.playerIsLeft
    value.player2AtackTime[119]=value.atackTime
    value.player2ThrowTime[119]=value.throwTime
    value.is2W[119]=value.isW
    value.is2S[119]=value.isS

def draw(i,a,t,x,y):
    if a==0 and t==0:
        value.screen.blit(player[i],(x,y))
    elif a>0:
        if i<3:
            value.screen.blit(playerC,(x,y))
        else:
            value.screen.blit(playerC_f,(x,y))
    elif t>0:
        if i<3:
            value.screen.blit(playerC,(x,y))
        else:
            value.screen.blit(playerC_f,(x,y))
