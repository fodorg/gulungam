import pygame
from pygame.locals import *
from classes import *
from const import *
from functions import *

pygame.init();

fenetre = pygame.display.set_mode((width,height))
font = pygame.font.SysFont(None, 72)


fonds = []
fondsx = []
for i in range(len(backgrounds)):
    fondsx.append(0)
    fonds.append(pygame.image.load(backgrounds[i]).convert_alpha())
    #fonds[i] = pygame.transform.scale(fonds[i], (width*2, height))



all_sprite_list = pygame.sprite.Group()
all_sprite_visible = pygame.sprite.Group()

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

getSpritesVisible(all_sprite_visible,0,all_sprite_list, perso)


hitbefore = 0
score = 0;
dir = 0; #dir = 1 > droite dir = -1 > gauche
vis = 0

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
            elif event.key == K_ESCAPE:
                continuer = 0
                print(score)

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
            elif perso.v < 0 :
                perso.v = -perso.v
            perso.changeimg()
        hitbefore = 1

    if len(block_hit_list) == 0:
        hitbefore = 0;

    #update des pos du fond et des elems
    for i in range(len(fonds)):
        fondsx[i] = fondsx[i]-(dir*i/4);

    score = score +dir;
    for platform in platforms_list:
        platform.rect.x = platform.rect.x-dir


    #affichage des fonds
    for i in range (len(fonds)):
        fondxi = fondsx[i]
        if fondxi <= -2*width or fondxi >= 2*width:
            fondxi = 0
            fondsx[i] = 0
        if fondxi < -width:
            fenetre.blit(fonds[i], ((fondxi)+(2*width), 0))
        elif fondxi > 0:
            fenetre.blit(fonds[i], ((fondxi)-(2*width), 0))
        fenetre.blit(fonds[i], (fondxi, 0))

    #hitbox
    #pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(perso.hitbox[0], perso.hitbox[1], perso.hitbox[2], perso.hitbox[3]))

    #affichage des sprites
    all_sprite_visible.draw(fenetre)

    #affichege du score
    text = font.render(str(score), True, (0, 128, 0))
    text_rect = text.get_rect()
    text_rect.right = width-10  # align to right to 150px
    text_rect.y = 10
    fenetre.blit(text,text_rect)


    pygame.display.flip()

    if dir != 0:
        getSpritesVisible(all_sprite_visible, score, all_sprite_list,perso)



