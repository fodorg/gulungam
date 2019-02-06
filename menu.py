#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from save import *

def loadBackground():
	background = pygame.image.load("images/background.jpg").convert_alpha()
	plan1 = pygame.image.load("images/plan1.png").convert_alpha()
	plan2 = pygame.image.load("images/plan2.png").convert_alpha()
	plan3 = pygame.image.load("images/plan3.png").convert_alpha()
	plan4 = pygame.image.load("images/plan4.png").convert_alpha()
	fenetre.blit(background, (0, 0))
	fenetre.blit(plan4, (0, 0))
	fenetre.blit(plan3, (0, 0))
	fenetre.blit(plan2, (0, 0))
	fenetre.blit(plan1, (0, 0))
	print("loadBackground")

def window_menu(): # Menu display
	buttons = pygame.image.load("images/menu.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))

	pygame.display.flip()

def window_menuStart(): # Menu mouseover START display
	buttons = pygame.image.load("images/menu_start.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))

	pygame.display.flip()

def window_menuHighScore(): # Menu mouseover HIGHSCORE display
	buttons = pygame.image.load("images/menu_highscores.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))

	pygame.display.flip()

def window_menuQuit(): # Menu mouseover QUITTER display
	buttons = pygame.image.load("images/menu_quitter.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))

	pygame.display.flip()

def window_menuCred(): # Menu mouseover CREDITS display
	buttons = pygame.image.load("images/menu_credits.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))

	pygame.display.flip()

def window_highScores(): # High score display
	loadBackground()
	bigFont = pygame.font.SysFont(None, 60) # FONT
	smallFont = pygame.font.SysFont(None, 40)

	# TITLE
	txt_title = bigFont.render("HIGH SCORES", True, (0, 0, 0))
	fenetre.blit(txt_title, (380, 20))

	# TABLE
	color = (255, 252, 244) # color of the line
	pygame.draw.rect(fenetre, (26, 103, 219), [40, 90, 936, 638])
	pygame.draw.line(fenetre, color, [512, 90], [512, 728], 3) # middle line
	pygame.draw.line(fenetre, color, [40, 90], [975, 90], 3)
	pygame.draw.line(fenetre, color, [975, 90], [975, 728], 3)
	pygame.draw.line(fenetre, color, [40, 90], [40, 728], 3)
	pygame.draw.line(fenetre, color, [40, 728], [975, 728], 3)

	for i in range(10):
		pygame.draw.line(fenetre, color, [40, (i+1)*58+90], [975, (i+1)*58+90], 3)

	# TEXT IN TABLE
	txt_nameTitle = bigFont.render("NAME", True, color)
	fenetre.blit(txt_nameTitle, (220, 100))
	txt_scoreTitle = bigFont.render("SCORE", True, color)
	fenetre.blit(txt_scoreTitle, (665, 100))

	i = 0
	data = getAllScoresSorted()
	while i < 10 and i < len(data):
		name, score = data[i]            # tuple unpacking
		txt_name = smallFont.render(name, True, color)
		fenetre.blit(txt_name, (50, i*58+165))
		txt_score = smallFont.render(str(score), True, color)
		fenetre.blit(txt_score, (525, i*58+165))
		i += 1

	back = pygame.image.load("images/back.png")
	back = pygame.transform.scale(back, (150, 75))
	fenetre.blit(back, (10, 10))

	pygame.display.flip()

def window_end():
	loadBackground()

def window_nameSelect():
	loadBackground()

	pygame.draw.rect(fenetre, (255, 255, 255), [370, 350, 322, 45])  # Text input DIMENSION IMPORTANT
	font = pygame.font.SysFont(None, 60) # TEXT FONT
	name = ""
	txt_Name = font.render(name, True, (0, 0, 0))
	fenetre.blit(txt_Name, (375, 350))
	pygame.display.flip()

	alphakeys = [K_a, K_z, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_q, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_m,
				 K_w, K_x, K_c, K_v, K_b, K_n]

	nameDone = False
	while not nameDone:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key in alphakeys and len(name) < 8:  # press on letter
					name = name + (event.unicode).upper()
					txt_Name = font.render(name, True, (0, 0, 0))
					fenetre.blit(txt_Name, (375, 350))
					pygame.display.flip()

				if event.key == K_BACKSPACE:                   # press on backspace
					name = name[:-1]
					pygame.draw.rect(fenetre, (255, 255, 255), [370, 350, 322, 45])
					txt_Name = font.render(name, True, (0, 0, 0))
					fenetre.blit(txt_Name, (375, 350))
					pygame.display.flip()

				if event.key == K_RETURN and len(name) > 0:    # press on enter
					print("return")

			if event.type == QUIT:
				print("quit")



#########################             MAIN               ###############################################################
pygame.init()
fenetre = pygame.display.set_mode((1024, 768))
window_menu()

pygame.mixer.music.load("sound/musique_menu.wav")
pygame.mixer.music.play(-1)

window_menu()

continuer = 1
status = "main"
buttonStatus = "main"
while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		if status == "main": # MAIN PAGE
			if event.type == MOUSEBUTTONDOWN and event.button == 1: # CLIC
				if 383 < event.pos[0] < 641 and 601 < event.pos[1] < 730:  # CLIC ON HIGH SCORES
					status = "highScores"
					window_highScores()

				if 383 < event.pos[0] < 641 and 451 < event.pos[1] < 580: # CLIC ON START
					status = "nameSelect"
					window_nameSelect()

				if 818 < event.pos[0] < 1014 and 660 < event.pos[1] < 758:  # CLIC ON QUITTER
					continuer = 0

				if 10 < event.pos[0] < 206 and 661 < event.pos[1] < 758:  # CLIC ON CREDITS
					print("CLIC CREDIT")

			if event.type == MOUSEMOTION: # MOTION
				if 383 < event.pos[0] < 641 and 601 < event.pos[1] < 730:  # MOTION ON HIGH SCORES
					if buttonStatus != "highScore":
						window_menuHighScore()
						buttonStatus = "highScore"

				elif 383 < event.pos[0] < 641 and 451 < event.pos[1] < 580: # MOTION ON START
					if buttonStatus != "start":
						window_menuStart()
						buttonStatus = "start"

				elif 818 < event.pos[0] < 1014 and 660 < event.pos[1] < 758:  # MOTION ON QUITTER
					if buttonStatus != "quit":
						window_menuQuit()
						buttonStatus = "quit"

				elif 10 < event.pos[0] < 206 and 661 < event.pos[1] < 758:  # MOTION ON CREDITS
					if buttonStatus != "cred":
						window_menuCred()
						buttonStatus = "cred"

				else:
					if buttonStatus != "main":
						window_menu()
						buttonStatus = "main"

		elif status == "highScores":            # HIGH SCORES
				if event.type == MOUSEBUTTONDOWN and event.button == 1:    # CLIC
					if 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # CLIC ON BACK
						status = "main"
						window_menu()

				if event.type == MOUSEMOTION:
					if 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # MOTION ON BACK
						if buttonStatus != "back":
							backOnClick = pygame.image.load("images/back_onclick.png")
							backOnClick = pygame.transform.scale(backOnClick, (150, 75))
							fenetre.blit(backOnClick, (10, 10))
							pygame.display.flip()
							buttonStatus = "back"

					else:
						if buttonStatus != "main":
							back = pygame.image.load("images/back.png")
							back = pygame.transform.scale(back, (150, 75))
							fenetre.blit(back, (10, 10))
							pygame.display.flip()
							buttonStatus = "main"

