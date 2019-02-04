#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1366, 768), RESIZABLE)


continuer = 1

while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0