import pygame
from pygame.locals import *
from classes import *
from const import *

pygame.init();

fenetre = pygame.display.set_mode((width,height))
fond = pygame.image.load(background).convert()
fond = pygame.transform.scale(fond, (width, height))



all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
platforms_list = pygame.sprite.Group()
plat = Platform(400,400,50,50)
platforms_list.add(plat)
all_sprite_list.add(plat)
plat = Platform(300,300,20,20)
platforms_list.add(plat)
all_sprite_list.add(plat)
plat = Platform(800,500,50,50)
platforms_list.add(plat)
all_sprite_list.add(plat)
plat = Platform(900,400,50,10)
platforms_list.add(plat)
all_sprite_list.add(plat)
plat = Platform(1100,400,100,50)
platforms_list.add(plat)
all_sprite_list.add(plat)
plat = Platform(1600,300,50,50)
platforms_list.add(plat)
all_sprite_list.add(plat)

perso = Perso();
all_sprite_list.add(perso)




score = 0;



#Rafraîchissement de l'écran
pygame.display.flip()


#BOUCLE INFINIE

continuer = 1
dir = 0; #dir = 1 > droite dir = -1 > gauche

# BOUCLE D'ACCUEIL



while continuer:
    # Limitation de vitesse de la boucle
    pygame.time.Clock().tick(fps)
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

    block_hit_list = pygame.sprite.spritecollide(perso, platforms_list, False)
    for block in block_hit_list:
        if dir != 0:
            dir = 0
        # si le perso descend
        elif perso.v > 0:
            perso.v = -vitesse
        elif perso.v < 0:
            perso.v = vitesse

    fondx = fondx-dir;
    score = score +dir;
    for platform in platforms_list:
        platform.rect.x = platform.rect.x-dir

    fenetre.blit(fond, (fondx, 0))
    if fondx <= -width or fondx >= width:
        fondx = 0
    if fondx < 0:
        fenetre.blit(fond, (fondx+width, 0))
    elif fondx > 0:
        fenetre.blit(fond, (fondx-width, 0))





    #hitbox
    #pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(perso.hitbox[0], perso.hitbox[1], perso.hitbox[2], perso.hitbox[3]))

    all_sprite_list.update()

    all_sprite_list.draw(fenetre)
#    fenetre.blit(perso.image,(perso.x, perso.y))




    pygame.display.flip()
