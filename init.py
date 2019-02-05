import pygame
from pygame.locals import *
from classes import *


all_sprite_list = pygame.sprite.Group()
all_sprite_visible = pygame.sprite.Group()

#platforms
f = open("data/props.txt", "r")
for x in f:
  print(x)


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


#