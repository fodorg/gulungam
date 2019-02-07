import pygame
from pygame.locals import *
from classes import *
from const import *
from functions import *
from init import *

fonds = []
fondsx = []

def loadbackground(lvl):

    for i in range(len(backgrounds[lvl])):
        fondsx.append(0)
        fonds.append(pygame.image.load(backgrounds[lvl][i]).convert_alpha())
        #fonds[i] = pygame.transform.scale(fonds[i], (width*2, height))


def game():
    font = pygame.font.SysFont(None, 72)

    loadbackground(0)


    perso = Perso()
    all_sprite_list.add(perso)

    getSpritesVisible(all_sprite_visible,0,all_sprite_list, perso)
    lvl = 0
    transition = 0
    score = 0
    ctrldir = 0
    ctrlnuage = 0
    dir = 0 #dir = 1 > droite dir = -1 > gauche
    vis = 0

    #BOUCLE INFINIE
    start_ticks=pygame.time.get_ticks() #starter tick
    continuer = 1
    while continuer:


        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(fps)


        #pour gerer la colision
        oldpbottom = perso.hitb.rect.bottom
        oldpy = perso.hitb.rect.y


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
                if event.key == K_UP:
                    ctrlnuage = 1
                elif event.key == K_DOWN:
                    ctrlnuage =-1
                elif event.key == K_ESCAPE:
                    continuer = 0
                    print(score)

            if event.type == KEYUP:
                if event.key == K_RIGHT and ctrldir == perso.vh or event.key == K_LEFT and ctrldir == -perso.vh:
                    ctrldir = 0
                if event.key == K_UP and ctrlnuage == 1 or event.key == K_DOWN and ctrlnuage == -1:
                    ctrlnuage = 0
        dir = ctrldir

        perso.bondir(ctrlnuage)

        #update des pos du fond et des elems
        for i in range(len(fonds)):
            fondsx[i] = fondsx[i]-(dir*vitessebackground[i]);

        score = score +dir
        for e in all_sprite_list:
            e.deplacer(dir)

        #collision platform
        corrdir = 0
        block_hit_list = pygame.sprite.spritecollide(perso.hitb, platforms_list, False)
        for block in block_hit_list:
            if perso.hitb.rect.right <= block.rect.x+dir*2:
                corrdir = (block.rect.x-perso.hitb.rect.right)
            elif perso.hitb.rect.x >= block.rect.right+dir*2:
                corrdir = -(perso.hitb.rect.x-block.rect.right)
            elif oldpbottom <= block.rect.y:
                perso.v = -vitesse
                perso.rect.y = block.rect.y-100
                #print(perso.rect.x)
                perso.hitb.updt(perso)
            elif oldpy >= block.rect.bottom :
                perso.v = -perso.v
                perso.rect.top=block.rect.bottom-20
                perso.hitb.updt(perso)
            perso.changeimg()

        if len(block_hit_list)>0:
            # update des pos du fond et des elems
            for i in range(len(fonds)):
                fondsx[i] = fondsx[i] - (corrdir * vitessebackground[i]);

            score = score + corrdir
            for e in all_sprite_list:
                e.deplacer(corrdir)

        #collision buffs
        block_hit_list = pygame.sprite.spritecollide(perso.hitb, blocksBuff_list, True)
        for block in block_hit_list:
            if block.typeBuff == "r" or block.typeBuff == "a" or block.typeBuff == "g":
                if perso.addBuff(block.typeBuff) == 1: #retourne vrai si le buff est activé
                    if block.typeBuff == "r" or block.typeBuff == "a" or block.typeBuff == "g":
                        if ctrldir > 0:
                            ctrldir = perso.vh
                        elif ctrldir < 0:
                            ctrldir = -perso.vh
            else:
                if block.typeBuff == "-":
                    score = score + malusPoints
                elif block.typeBuff == "+":
                    score = score + bonusPoints
                elif block.typeBuff == "t" : #tp
                    for e in all_sprite_list:
                        e.deplacer(block.dest-block.rect.x)
                    tp(int(block.dest))
                    getSpritesVisible(all_sprite_visible,score,all_sprite_list,perso)
                    transition = 600
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

        pygame.draw.rect(fenetre, (153, 70, 0), perso.hitb.rect)

        all_sprite_visible.draw(fenetre)

        #affichage du sol
        pygame.draw.rect(fenetre, (153, 70, 0), pygame.Rect(0, height-148, width, 148))


        #verif et affichage du buff
        if perso.buff != "":
            duraBuff = 5 - (pygame.time.get_ticks() - perso.startBuff) / 1000  # calculate how many seconds
            if duraBuff < 0:#on enleve le buff
                perso.deBuff()
                if ctrldir > 0:
                    ctrldir = perso.vh
                elif ctrldir < 0:
                    ctrldir = -perso.vh

            buffHud = pygame.Rect(0,0,duraBuff*50,20)
            buffHud.centerx = width/2

            pygame.draw.rect(fenetre, (153, 70, 0), buffHud)


        #affichege du score
        text = font.render(str(int(score)), True, (0, 128, 0))
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


        #transition
        if transition > 0:
            while transition > 0:
                pygame.draw.rect(fenetre, (153, 70, 0), pygame.Rect(0, transition, width, height))
                pygame.display.flip()
                transition -=30
                pygame.time.Clock().tick(fps)
                pygame.display.flip()




        pygame.display.flip()

        if dir != 0:
            getSpritesVisible(all_sprite_visible, score, all_sprite_list,perso)
    return int(score)


