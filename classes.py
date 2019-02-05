import pygame
from const import *

class Perso(pygame.sprite.Sprite):
    """Classe permettant de créer un personnage"""

    def __init__(self):
        super().__init__()
        # Sprites du personnage
        # Position du personnage en cases et en pixels
        self.image = pygame.image.load("images/mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.a = acceleration
        self.v = -vitesse
        self.rect = self.image.get_rect()
        self.rect.y = 600
        self.rect.x = 400
        self.hitbox = (self.rect.x+20, self.rect.y, 60, 100)

    def bondir(self, dir = 0):
        self.rect.x=self.rect.x+dir
        self.rect.y = self.rect.y+self.v
        self.hitbox = (self.rect.x+20, self.rect.y, 60, 100)
        if self.rect.y > 500:
            self.v = -vitesse
        else:
            self.v = self.v + self.a


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((153, 51, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    # def collide(self, hitbox):
    #     #return hitbox[0] + hitbox[2] > self.x and hitbox[0] < self.x + self.w and hitbox[1]+hitbox[3] > self.y and hitbox[1] < self.y + self.h
    #     if hitbox[0] + hitbox[2] > self.x and hitbox[0] < self.x + self.w :
    #         if hitbox[1]+hitbox[3] > self.y and hitbox[1]+hitbox[3] < self.y+(self.h/2):
    #             return 1;
    #         elif hitbox[1] < self.y+self.h and hitbox[1] > self.y+(self.h/2):
    #             return -1;
    #     return 0



    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, (153, 51, 0), pygame.Rect(self.x, self.y, self.w, self.h))

    def deplacer(self, dir = 0):
        self.x = self.x+dir

