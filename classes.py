import pygame
from const import *

class Perso:
    """Classe permettant de créer un personnage"""

    def __init__(self):
        # Sprites du personnage
        # Position du personnage en cases et en pixels
        self.x = width/2
        self.y = height*(3/4)
        self.image = pygame.image.load("images/mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.a = acceleration
        self.v = -vitesse
        self.hitbox = (self.x, self.y, 100, 100)

    def bondir(self, dir = 0):
        self.x=self.x+dir
        self.y = self.y+self.v
        self.hitbox = (self.x, self.y, 100, 100)
        if self.v > vitesse:
            self.v = -self.v
        else:
            self.v = self.v + self.a


class platform:

    def __init__(self, x, y, w, h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;

    def collide(self, hitbox):
        if self.x < hitbox[0] and self. self.x > hitbox[0]+1