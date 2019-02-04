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
a = -10;
i = 1
dir = 0; #dir = 1 > droite dir = -1 > gauche

# BOUCLE D'ACCUEIL

while continuer:
    # Limitation de vitesse de la boucle

    pygame.time.Clock().tick(30)
    dir = 0;
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                perso.bondir(fenetre, fond);

    perso.deplacer(a,dir)
    a = a+i
    if a < -10:
        i = 1;
    elif a > 10:
        i = -1
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso.image,(perso.x, perso.y))  # dk.direction = l'image dans la bonne direction
    pygame.display.flip()
