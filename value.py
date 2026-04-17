import sys, random
import pygame, time
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
pygame.mixer.init()

width = 150
maxWidth=500
height = 100
size =5

screen = pygame.display.set_mode((width*size, height*size))
pygame.display.set_caption("action")


grid = [[0] * height for _ in range(maxWidth)]

scroll=0