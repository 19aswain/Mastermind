import pygame
from settings import *

class Board:
    def __init__(self):
        pass

    def draw(self,screen):
        for x in range (0,WIDTH,TILESIZE):
            for y in range (0,HEIGHT,TILESIZE):
                pygame.draw.line(screen,LIGHTGREY, (x,0),(x,HEIGHT))
                pygame.draw.line(screen,LIGHTGREY, (0,y),(WIDTH,y))