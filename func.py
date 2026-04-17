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
    return image
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