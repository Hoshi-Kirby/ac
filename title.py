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


titleChar = []
s=5.5
titleChar.append(func.imageLoad(s, "charImage/kyou.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/ryoku.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/kata.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/a.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/ku.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/shi.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/lyo.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/nn.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/ge.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/l.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/mu.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/kome.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/ichi.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/hito.png", 255)[0])
titleChar.append(func.imageLoad(s, "charImage/you.png", 255)[0])
titleCharSize=func.imageLoad(s, "charImage/you.png", 255)[1]

def draw_bg(bg_img, img_w,img_h):
    scale = value.height / img_h
    new_w = int(img_w * scale)*value.size
    new_h = value.height*value.size

    bg_scaled = pygame.transform.scale(bg_img, (new_w, new_h))

    value.screen.blit(bg_scaled, (0, 0))

def draw_logo(x,y,d):
    for i in range(len(titleChar)):
        func.ImageDraw(titleChar[i],x+(d+titleCharSize)*i-((d+titleCharSize)*len(titleChar))/2,y)