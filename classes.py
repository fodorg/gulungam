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
        if self.y > 500:
            self.v = -vitesse
        else:
            self.v = self.v + self.a


class Platform:

    def __init__(self, x, y, w, h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;

    def collide(self, hitbox):
        #return hitbox[0] + hitbox[2] > self.x and hitbox[0] < self.x + self.w and hitbox[1]+hitbox[3] > self.y and hitbox[1] < self.y + self.h
        if hitbox[0] + hitbox[2] > self.x and hitbox[0] < self.x + self.w :
            if hitbox[1]+hitbox[3] > self.y and hitbox[1]+hitbox[3] < self.y+(self.h/2):
                return 1;
            elif hitbox[1] < self.y+self.h and hitbox[1] > self.y+(self.h/2):
                return -1;
        return 0
    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, (153, 51, 0), pygame.Rect(self.x, self.y, self.w, self.h))

    def deplacer(self, dir = 0):
        self.x = self.x+dir

