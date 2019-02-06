import pygame
from pygame.locals import *
from classes import *


pygame.init();

fenetre = pygame.display.set_mode((width,height))

all_sprite_list = pygame.sprite.Group()
all_sprite_visible = pygame.sprite.Group()

#platforms
platforms_list = pygame.sprite.Group()
blocksBuff_list = pygame.sprite.Group()

listargs = ["p", "a", "g", "+", "-"]

f = open("data/props.txt", "r")

for line in f:
  line1=line.rstrip()
  params = line.split(",")
  if len(params) >= 5:
    if len(params) == 5:
      params.insert(1,"blocNull.png")

    if params[0] == "p":
      plat = Platform(params[1],int(params[2]),int(params[3]),int(params[4]),int(params[5]))
      platforms_list.add(plat)
      all_sprite_list.add(plat)
    elif params[0] in listargs:
      b = BlockBuff(params[0],params[1],int(params[2]),int(params[3]),int(params[4]),int(params[5]))
      blocksBuff_list.add(b)
      all_sprite_list.add(b)
#