import pygame
from pygame.locals import *
from classes import *
from const import *
from functions import *
from init import *

pygame.init();

fenetre = pygame.display.set_mode((width,height))
font = pygame.font.SysFont(None, 72)


fonds = []
fondsx = []
for i in range(len(backgrounds)):
    fondsx.append(0)
    fonds.append(pygame.image.load(backgrounds[i]).convert_alpha())
    #fonds[i] = pygame.transform.scale(fonds[i], (width*2, height))



perso = Perso()
all_sprite_list.add(perso)

getSpritesVisible(all_sprite_visible,0,all_sprite_list, perso)


score = 0
ctrldir = 0
dir = 0 #dir = 1 > droite dir = -1 > gauche
vis = 0

#BOUCLE INFINIE
start_ticks=pygame.time.get_ticks() #starter tick
continuer = 1
while continuer:
    # Limitation de vitesse de la boucle
    pygame.time.Clock().tick(fps)
    oldprect = perso.rect

    #pour gerer la colision
    oldpbottom = perso.rect.bottom
    oldpy = perso.rect.y
    oldpx = perso.rect.x
    oldpright = perso.rect.right

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            print(score);

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ctrldir = perso.vh
            elif event.key == K_LEFT:
                ctrldir = -perso.vh
            elif event.key == K_ESCAPE:
                continuer = 0
                print(score)

        if event.type == KEYUP:
            if event.key == K_RIGHT and ctrldir == perso.vh or event.key == K_LEFT and ctrldir == -perso.vh:
                ctrldir = 0;

    dir = ctrldir
    perso.bondir()


    #update des pos du fond et des elems
    for i in range(len(fonds)):
        fondsx[i] = fondsx[i]-(dir*i/4);

    score = score +dir
    for platform in platforms_list:
        platform.rect.x = platform.rect.x-dir
    for w in walls_list:
        w.rect.x = w.rect.x-dir

    #collision platform
    block_hit_list = pygame.sprite.spritecollide(perso, platforms_list, False)
    for block in block_hit_list:
        if oldpbottom < block.rect.y:
            perso.v = -vitesse
            perso.rect.bottom = block.rect.y
        elif oldpy > block.rect.bottom:
            perso.v = -perso.v
            perso.rect.top=block.rect.bottom
        else:
            if perso.rect.centerx < block.rect.centerx:
                dir = -(perso.rect.right-block.rect.x)
            else:
                dir = block.rect.right-perso.rect.x
        perso.changeimg()
    if len(block_hit_list)>0:
        # update des pos du fond et des elems
        for i in range(len(fonds)):
            fondsx[i] = fondsx[i] - (dir * i / 4);

        score = score + dir
        for platform in platforms_list:
            platform.rect.x = platform.rect.x - dir
        for w in walls_list:
            w.rect.x = w.rect.x - dir



    #collision wall
    block_hit_list = pygame.sprite.spritecollide(perso, walls_list, False)
    for block in block_hit_list:
        print("")
        # if hitbefore == 0:
        #     #perso.vh = -perso.vh
        # hitbefore = 1



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

    #affichage des sprites

    all_sprite_visible.draw(fenetre)

    #affichage du sol
    pygame.draw.rect(fenetre, (153, 70, 0), pygame.Rect(0, height-150, width, 150))







    #affichege du score
    text = font.render(str(score), True, (0, 128, 0))
    text_rect = text.get_rect()
    text_rect.right = width-10  # align to right to 150px
    text_rect.y = 10
    fenetre.blit(text,text_rect)

    #affichage du timer
    seconds = 180-(pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    min = int(seconds/60)
    seconds = int(seconds%60)
    if seconds <= 0 and min == 0:
        continuer = 0
    if seconds >= 10:
        seconds = str(seconds)
    else:
        seconds = "0"+str(seconds)
    text = font.render(str(min)+":"+seconds, True, (0, 128, 0))
    fenetre.blit(text, (10,10))


    pygame.display.flip()

    if dir != 0:
        getSpritesVisible(all_sprite_visible, score, all_sprite_list,perso)



