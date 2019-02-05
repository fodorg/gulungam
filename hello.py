import pygame
from pygame.locals import *
from classes import *
from const import *

pygame.init();

fenetre = pygame.display.set_mode((width,height))
fond = pygame.image.load(background).convert()
fond = pygame.transform.scale(fond, (width, height))



all_sprite_list = pygame.sprite.Group()

#platforms
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



hitbefore = 0
score = 0;
dir = 0; #dir = 1 > droite dir = -1 > gauche


#BOUCLE INFINIE

continuer = 1
while continuer:
    # Limitation de vitesse de la boucle
    pygame.time.Clock().tick(fps)

    #events
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

    #collision
    block_hit_list = pygame.sprite.spritecollide(perso, platforms_list, False)
    for block in block_hit_list:
        if hitbefore == 0:
            if perso.rect.y+(perso.rect.height/2) < block.rect.y+(block.rect.height/2):
                perso.v = -vitesse
            else:
                perso.v = -perso.v
        hitbefore = 1

    if len(block_hit_list) == 0:
        hitbefore = 0;

    #update des pos du fond et des elems
    fondx = fondx-dir;
    score = score +dir;
    for platform in platforms_list:
        platform.rect.x = platform.rect.x-dir


    #affichage du fond
    fenetre.blit(fond, (fondx, 0))
    if fondx <= -width or fondx >= width:
        fondx = 0
    if fondx < 0:
        fenetre.blit(fond, (fondx+width, 0))
    elif fondx > 0:
        fenetre.blit(fond, (fondx-width, 0))

    #hitbox
    #pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(perso.hitbox[0], perso.hitbox[1], perso.hitbox[2], perso.hitbox[3]))

    #affichage des sprites
    all_sprite_list.update()
    all_sprite_list.draw(fenetre)

    pygame.display.flip()
