#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

def window_main(): # Menu display
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

def window_highScores(): # High score display
	fenetre.fill((104, 194, 226))  # BACKGROUND
	bigFont = pygame.font.SysFont(None, 60) # FONT
	smallFont = pygame.font.SysFont(None, 30)

	# TITLE
	txt_title = bigFont.render("HIGH SCORES", True, (0, 0, 0))
	fenetre.blit(txt_title, (380, 20))

	# TABLE
	color = (255, 252, 244) # color of the line
	pygame.draw.rect(fenetre, (26, 103, 219), [40, 90, 936, 638])
	pygame.draw.line(fenetre, color, [512, 90], [512, 728], 3)
	pygame.draw.line(fenetre, color, [40, 90], [975, 90], 3)
	pygame.draw.line(fenetre, color, [975, 90], [975, 728], 3)
	pygame.draw.line(fenetre, color, [40, 90], [40, 728], 3)
	pygame.draw.line(fenetre, color, [40, 728], [975, 728], 3)

	for i in range(10):
		pygame.draw.line(fenetre, color, [40, (i+1)*58+90], [975, (i+1)*58+90], 3)

	# TEXT IN TABLE
	txt_name = bigFont.render("NAME", True, color)
	fenetre.blit(txt_name, (220, 100))
	txt_score = bigFont.render("SCORE", True, color)
	fenetre.blit(txt_score, (665, 100))



	pygame.display.flip()

######################### MAIN #######################
pygame.init()
fenetre = pygame.display.set_mode((1024, 768))

window_main()

continuer = 1
status = "main"
while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		if status == "main" and event.type == MOUSEBUTTONDOWN and event.button == 1 and 425 < event.pos[0] < 625 and 370 < event.pos[1] < 420: # CLIC ON HIGH SCORES
			status = "highScores"
			window_highScores()