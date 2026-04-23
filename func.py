import sys, random
import pygame, time
import value
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

def imageLoad(size,imageText,alpha):
    image = pygame.image.load(imageText).convert_alpha()
    image = pygame.transform.scale_by(image,size)
    image.set_alpha(alpha)
    width, height = image.get_size()
    return image,width,height
def buttonImageLoad(size,imageText,alpha,x,y):
    image = pygame.image.load(imageText).convert_alpha()
    image = pygame.transform.scale_by(image,size)
    image.set_alpha(alpha)
    imageRect=image.get_rect(topleft=(x, y))
    return image,imageRect

def ImageDraw(image,x,y):
    value.screen.blit(image,(x,y))
def butttonImageDraw(image,imageRect,x,y):
    value.screen.blit(image,(x,y))
    if imageRect.collidepoint(pygame.mouse.get_pos()):
        return True
    else:
        return False
def draw_bg(bg_img, scroll, max_scroll,img_w,img_h):
    # 高さに合わせてスケーリング
    scale = value.height / img_h
    new_w = int(img_w * scale)*value.size
    new_h = value.height*value.size

    bg_scaled = pygame.transform.scale(bg_img, (new_w, new_h))

    # スクロール割合
    t = scroll / max_scroll if max_scroll != 0 else 0

    # 動ける範囲
    max_offset = max(0, new_w - value.width)

    # パララックス位置
    offset = int(max_offset * t)

    # 描画
    value.screen.blit(bg_scaled, (-offset, 0))