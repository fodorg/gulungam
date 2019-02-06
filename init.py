import pygame
from pygame.locals import *
from classes import *


all_sprite_list = pygame.sprite.Group()
all_sprite_visible = pygame.sprite.Group()

#platforms
platforms_list = pygame.sprite.Group()
speeders_list = pygame.sprite.Group()


f = open("data/props.txt", "r")

for line in f:
  if line[0] != '#':
    params = line.split(",")
    if len(params) >= 5:
      if params[0] == "p":
        plat = Platform(int(params[1]),int(params[2]),int(params[3]),int(params[4]))
        platforms_list.add(plat)
        all_sprite_list.add(plat)
      elif params[0] == "s":
        s = Speeder(int(params[1]),int(params[2]),int(params[3]),int(params[4]))
        speeders_list.add(s)
        all_sprite_list.add(s)
#