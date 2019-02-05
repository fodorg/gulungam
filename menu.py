#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1024, 768), RESIZABLE)

def window_init(): # Menu initialization
	fenetre.fill((255, 204, 0)) # BACKGROUND
	font = pygame.font.SysFont(None, 50) # FONT

	# NEW GAME
	pygame.draw.rect(fenetre, (204, 255, 204), [425, 300, 200, 50])
	txt_newGame = font.render("New Game", True, (0, 0, 0))
	fenetre.blit(txt_newGame, (435,310))

	#HIGH SCORE
	pygame.draw.rect(fenetre, (204, 255, 204), [425, 370, 200, 50])
	txt_highScores = font.render("High Scores", True, (0, 0, 0))
	fenetre.blit(txt_highScores, (435,390))

	pygame.display.flip()

window_init()

continuer = 1

while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		if event.type == MOUSEBUTTONDOWN and event.button == 1 and 425 < event.pos[0] < 625 and 370 < event.pos[1] < 420: # CLIC ON HIGH SCORES
			print("clic on high scores")