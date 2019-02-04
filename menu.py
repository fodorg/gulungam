#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1024, 768), RESIZABLE)

fenetre.fill((255, 204, 0))
pygame.draw.rect(fenetre, (204, 255, 204), [425, 300, 200, 50])

pygame.display.flip()

continuer = 1

while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0