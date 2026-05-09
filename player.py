import sys, random
import pygame, time
import value
import func
import stage
import enemy
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

player=[]
player.append(func.imageLoad(2,"image/player_0.png",255)[0])
player.append(func.imageLoad(2,"image/player_1.png",255)[0])
player.append(func.imageLoad(2,"image/player_2.png",255)[0])
player.append(func.imageLoad(2,"image/player_3.png",255)[0])
player.append(pygame.transform.flip(player[0], True, False))
player.append(pygame.transform.flip(player[1], True, False))
player.append(pygame.transform.flip(player[2], True, False))
player.append(pygame.transform.flip(player[3], True, False))
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
slash_u=pygame.transform.rotate(slash, 90)
slash_u_f=pygame.transform.rotate(slash_f, -90)
slash_d=pygame.transform.rotate(slash, -90)
slash_d_f=pygame.transform.rotate(slash_f, 90)

def draw(i,a,t,d,x,y):
    if d>0:
        value.screen.blit(player[value.playerIsLeft*4],(x,y))
    elif a==0 and t==0:
        value.screen.blit(player[i],(x,y))
    elif a>0:
        direct=0
        if value.isW:
            direct=90
        if value.isS:
            direct=-90
        if i<3:
            value.screen.blit(playerA,(x,y))
            rotated_image = pygame.transform.rotate(sword, 180*a/6-135+direct)
            if value.isW:
                value.screen.blit(rotated_image,(x,y-value.playerHeight/3))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash_u,(x,y-value.playerHeight))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash_u_f,(x,y-value.playerHeight))
                value.dameX=0
                value.dameY=-value.playerHeight
            elif value.isS:
                value.screen.blit(rotated_image,(x,y+value.playerHeight/3))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash_d,(x,y+value.playerHeight))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash_d_f,(x,y+value.playerHeight))
                value.dameX=0
                value.dameY=value.playerHeight
            else:
                value.screen.blit(rotated_image,(x+value.playerWidth/3,y))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash,(x+value.playerWidth,y))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash2,(x+value.playerWidth,y))
                value.dameX=value.playerWidth
                value.dameY=0
        else:
            value.screen.blit(playerA_f,(x,y))
            rotated_image = pygame.transform.rotate(sword_f, -180*a/6+135-direct)
            value.screen.blit(rotated_image,(x-value.playerWidth/2,y))
            if value.isW:
                value.screen.blit(rotated_image,(x,y-value.playerHeight/3))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash_u_f,(x,y-value.playerHeight))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash_u,(x,y-value.playerHeight))
                value.dameX=0
                value.dameY=-value.playerHeight
            elif value.isS:
                value.screen.blit(rotated_image,(x,y+value.playerHeight/3))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash_d_f,(x,y+value.playerHeight))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash_d,(x,y+value.playerHeight))
                value.dameX=0
                value.dameY=value.playerHeight
            else:
                value.screen.blit(rotated_image,(x-value.playerWidth/3,y))
                if 0<a<5 and not value.slash:
                    value.screen.blit(slash_f,(x-value.playerWidth,y))
                if 1<a<=6 and value.slash:
                    value.screen.blit(slash2_f,(x-value.playerWidth,y))
                value.dameX=-value.playerWidth
                value.dameY=0
        for j in range(value.nE):
            if not value.enemyIsSlash[j]:
                if func.spHitSp(value.playerX+value.dameX/value.size,value.playerY+value.dameY/value.size,value.playerWidth/value.size,value.playerHeight/value.size,value.enemyX[j],value.enemyY[j],value.playerWidth/value.size,value.playerHeight/value.size):    
                    if value.ghostTime[j]<20 and value.moguMoguTime[j]==0:
                        value.enemyHP[j]-=3
                        value.enemyIsSlash[j]=True
                        enemy.nockBack(j)
    elif t>0:
        if i<3:
            value.screen.blit(playerA,(x,y))
        else:
            value.screen.blit(playerA_f,(x,y))

max_width=100
height=20
x=10
y=10
frame_pad = 2 

bg = pygame.Surface((max_width, height), pygame.SRCALPHA)
pygame.draw.rect(bg, (0, 0, 0, 120), (0, 0, max_width, height))

frame_surf = pygame.Surface((max_width + frame_pad*2, height + frame_pad*2), pygame.SRCALPHA)
frame_color = (255, 255, 255, 180)
pygame.draw.rect(frame_surf, frame_color, (0, 0, max_width + frame_pad*2, height + frame_pad*2), 2)

def drawHP():
    value.screen.blit(bg, (x, y))

    value.screen.blit(frame_surf, (x - frame_pad, y - frame_pad))

    current_width = int(max_width * (value.playerHP / 10))
    if value.playerDamageTime==0:
        color1=(138,199,90)
        color2=(102,144,62)
    else:
        color1=(255,0,0)
        color2=(150,0,0)
    pygame.draw.rect(value.screen, color1, (x, y, current_width, height/2))
    pygame.draw.rect(value.screen, color2, (x, y + height/2, current_width, height/2))
