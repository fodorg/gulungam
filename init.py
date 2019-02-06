import pygame
from pygame.locals import *
from classes import *


all_sprite_list = pygame.sprite.Group()
all_sprite_visible = pygame.sprite.Group()

#platforms
platforms_list = pygame.sprite.Group()
walls_list = pygame.sprite.Group()

f = open("data/props.txt", "r")

for line in f:
  if line[0] != '#':
    params = line.split(",")
    if params[0] == "p":
      plat = Platform(int(params[1]),int(params[2]),int(params[3]),int(params[4]))
      platforms_list.add(plat)
      all_sprite_list.add(plat)
    elif params[0] == "w":
      wall = Wall(int(params[1]),int(params[2]),int(params[3]),int(params[4]))
      walls_list.add(wall)
      all_sprite_list.add(wall)
#