import pygame
from pygame.locals import *
from const import *

def getSpritesVisible(allSpriteVisible, x, allSprite, perso):
    allSpriteVisible.empty()
    allSpriteVisible.add(perso)
    print("a")

    for s in allSprite:
        if s.rect.right > 0 and s.rect.x < width:
            allSpriteVisible.add(s)
            print(s)
