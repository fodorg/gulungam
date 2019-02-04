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

    def bondir(self, fenetre, fond):
        a = -10;

        while a <= 10:
            self.y = self.y+a;
            a = a+1
            fenetre.blit(fond, (0, 0))
            pygame.transform.scale(fond, (600,800));

            fenetre.blit(self.image, (self.x, self.y))  # dk.direction = l'image dans la bonne direction
            pygame.display.flip()
    def deplacer(self, a, dir):
        self.x=self.x+dir
        self.y = self.y+a