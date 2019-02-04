import pygame
from pygame.locals import *
from classes import *
from const import *

pygame.init();


fenetre = pygame.display.set_mode((width,height))



fond = pygame.image.load("images/background.jpeg").convert()
fond = pygame.transform.scale(fond, (width, height))
perso = Perso();

#Rafraîchissement de l'écran
pygame.display.flip()


#BOUCLE INFINIE

continuer = 1
v = -20;
a = 3;
dir = 0; #dir = 1 > droite dir = -1 > gauche

# BOUCLE D'ACCUEIL

while continuer:
    # Limitation de vitesse de la boucle

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                dir = 10
            elif event.key == K_LEFT:
                dir = -10

        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                dir = 0;

    perso.deplacer(v,dir)
    if v > 20:
        v = -v
    else :
        v= v+a
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso.image,(perso.x, perso.y))  # dk.direction = l'image dans la bonne direction
    pygame.display.flip()
