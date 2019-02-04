import pygame
from pygame.locals import *
from classes import *
from const import *

pygame.init();

platforms = []
platforms.append(Platform(400,400,50,50))
platforms.append(Platform(300,300,20,20))
platforms.append(Platform(800,500,50,50))
platforms.append(Platform(900,400,50,10))
platforms.append(Platform(1100,400,100,50))
platforms.append(Platform(1600,300,50,50))


fenetre = pygame.display.set_mode((width,height))

score = 0;


fond = pygame.image.load(background).convert()
fond = pygame.transform.scale(fond, (width, height))
perso = Perso();

#Rafraîchissement de l'écran
pygame.display.flip()


#BOUCLE INFINIE

continuer = 1
dir = 0; #dir = 1 > droite dir = -1 > gauche

# BOUCLE D'ACCUEIL

while continuer:
    # Limitation de vitesse de la boucle

    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            print(score);

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                dir = vitesseDir
            elif event.key == K_LEFT:
                dir = -vitesseDir

        if event.type == KEYUP:
            if event.key == K_RIGHT and dir == vitesseDir or event.key == K_LEFT and dir == -vitesseDir:
                dir = 0;

    perso.bondir()
    fondx = fondx-dir;
    score = score +dir;

    fenetre.blit(fond, (fondx, 0))
    if fondx <= -width or fondx >= width:
        fondx = 0
    if fondx < 0:
        fenetre.blit(fond, (fondx+width, 0))
    elif fondx > 0:
        fenetre.blit(fond, (fondx-width, 0))

    #platforms
    for elem in platforms:
        i = elem.collide(perso.hitbox)
        if(i == 1):
            perso.v = -vitesse
        if(i == -1):
            perso.v = -perso.v
        elem.deplacer(-dir)
        elem.afficher(fenetre)


    #hitbox
    #pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(perso.hitbox[0], perso.hitbox[1], perso.hitbox[2], perso.hitbox[3]))

    fenetre.blit(perso.image,(perso.x, perso.y))




    pygame.display.flip()
