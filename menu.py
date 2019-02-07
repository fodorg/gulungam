#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from save import *
from hello import *

def loadBackground():
	background = pygame.image.load("images/background1.png").convert_alpha()
	plan1 = pygame.image.load("images/plan11.png").convert_alpha()
	plan2 = pygame.image.load("images/plan12.png").convert_alpha()
	plan3 = pygame.image.load("images/plan13.png").convert_alpha()
	plan4 = pygame.image.load("images/plan14.png").convert_alpha()
	fenetre.blit(background, (0, 0))
	fenetre.blit(plan4, (0, 0))
	fenetre.blit(plan3, (0, 0))
	fenetre.blit(plan2, (0, 0))
	fenetre.blit(plan1, (0, 0))
	pygame.display.flip()

def window_menu(): # Menu display
	buttons = pygame.image.load("images/menu.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))


def window_menuStart(): # Menu mouseover START display
	buttons = pygame.image.load("images/menu_start.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))


def window_menuHighScore(): # Menu mouseover HIGHSCORE display
	buttons = pygame.image.load("images/menu_highscores.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))


def window_menuQuit(): # Menu mouseover QUITTER display
	buttons = pygame.image.load("images/menu_quitter.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))


def window_menuCred(): # Menu mouseover CREDITS display
	buttons = pygame.image.load("images/menu_credits.png").convert_alpha()
	fenetre.blit(buttons, (0, 0))


def window_highScores(): # High score display
	back = pygame.image.load("images/highscores.png").convert()
	fenetre.blit(back, (0, 0))
	bigFont = pygame.font.Font("fonts/pixelart.ttf", 40) # FONT
	smallFont = pygame.font.Font("fonts/vcr.ttf", 30)

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

	# BACK
	back = pygame.image.load("images/back.png")
	back = pygame.transform.scale(back, (150, 75))
	fenetre.blit(back, (10, 10))


def window_end():
	loadBackground()

	color = (255, 252, 244)
	smallFont = pygame.font.Font("fonts/pixelart.ttf", 50) # FONT
	bigFont = pygame.font.Font("fonts/pixelart.ttf", 70) # FONT

	txt_sentence = smallFont.render("YOU SCORED", True, color)
	fenetre.blit(txt_sentence, (350, 200))

	score = getAllScores()[-1]
	txt_score = bigFont.render(str(score), True, color)
	fenetre.blit(txt_score, (400, 300))

	back = pygame.image.load("images/back.png")
	start = pygame.image.load("images/start.png")

	back = pygame.transform.scale(back, (300, 150))
	start = pygame.transform.scale(start, (300, 150))

	fenetre.blit(back, (190, 600))
	fenetre.blit(start, (500, 600))

def window_credits():
	back = pygame.image.load("images/credits.png")
	fenetre.blit(back, (0, 0))

	back = pygame.image.load("images/back.png")
	back = pygame.transform.scale(back, (150, 75))
	fenetre.blit(back, (10, 10))

def window_nameSelect():
	pseudo = pygame.image.load("images/pseudo.png")
	fenetre.blit(pseudo,(0, 0))

	pygame.draw.rect(fenetre, (255, 255, 255), [210, 200, 602, 58])  # Text input DIMENSION IMPORTANT
	font = pygame.font.Font("fonts/pixelart.ttf", 60) # TEXT FONT
	name = ""
	txt_Name = font.render(name, True, (0, 0, 0))
	fenetre.blit(txt_Name, (215, 200))

	back = pygame.image.load("images/back.png")
	back = pygame.transform.scale(back, (150, 75))
	fenetre.blit(back, (10, 10))

	pygame.display.flip()

	alphakeys = [K_a, K_z, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_q, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_m,
				 K_w, K_x, K_c, K_v, K_b, K_n]

	buttonPseudoStatus = "main"
	nameDone = False
	while not nameDone:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key in alphakeys and len(name) < 8:  # press on letter
					name = name + (event.unicode).upper()
					txt_Name = font.render(name, True, (0, 0, 0))
					fenetre.blit(txt_Name, (215, 200))
					pygame.display.flip()

				if event.key == K_BACKSPACE:                   # press on backspace
					name = name[:-1]
					pygame.draw.rect(fenetre, (255, 255, 255), [210, 200, 602, 58])
					txt_Name = font.render(name, True, (0, 0, 0))
					fenetre.blit(txt_Name, (215, 200))
					pygame.display.flip()

				if event.key == K_RETURN and len(name) > 0:    # press on enter
					pygame.mixer.music.load("sound/musique_game.wav")
					pygame.mixer.music.play(-1)
					game(name)  # ACTUAL GAME
					pygame.mixer.music.load("sound/musique_menu.wav")
					pygame.mixer.music.play(-1)
					raise Exception("END")

			if event.type == MOUSEMOTION:
				if 383 < event.pos[0] < 650 and 287 < event.pos[1] < 451:  # MOTION ON START
					if buttonPseudoStatus != "start":
						pseudo = pygame.image.load("images/pseudo start.png")
						fenetre.blit(pseudo, (0, 0))

						back = pygame.image.load("images/back.png")
						back = pygame.transform.scale(back, (150, 75))
						fenetre.blit(back, (10, 10))

						pygame.draw.rect(fenetre, (255, 255, 255), [210, 200, 602, 58])
						txt_Name = font.render(name, True, (0, 0, 0))
						fenetre.blit(txt_Name, (215, 200))

						pygame.display.flip()
						buttonPseudoStatus = "start"

				elif 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # MOTION ON BACK
					if buttonPseudoStatus != "back":
						backOnClick = pygame.image.load("images/back_onclick.png")
						backOnClick = pygame.transform.scale(backOnClick, (150, 75))
						fenetre.blit(backOnClick, (10, 10))

						pygame.draw.rect(fenetre, (255, 255, 255), [210, 200, 602, 58])
						txt_Name = font.render(name, True, (0, 0, 0))
						fenetre.blit(txt_Name, (215, 200))

						pygame.display.flip()
						buttonPseudoStatus = "back"

				else:
					if buttonPseudoStatus != "main":
						pseudo = pygame.image.load("images/pseudo.png")
						fenetre.blit(pseudo, (0, 0))

						back = pygame.image.load("images/back.png")
						back = pygame.transform.scale(back, (150, 75))
						fenetre.blit(back, (10, 10))

						pygame.draw.rect(fenetre, (255, 255, 255), [210, 200, 602, 58])
						txt_Name = font.render(name, True, (0, 0, 0))
						fenetre.blit(txt_Name, (215, 200))

						pygame.display.flip()
						buttonPseudoStatus = "main"

			if event.type == MOUSEBUTTONDOWN and event.button == 1: # CLIC
				if 383 < event.pos[0] < 650 and 287 < event.pos[1] < 451 and len(name) > 0:  # CLIC ON START
					pygame.mixer.music.load("sound/musique_game.wav")
					pygame.mixer.music.play(-1)
					game(name)  # ACTUAL GAME
					pygame.mixer.music.load("sound/musique_menu.wav")
					pygame.mixer.music.play(-1)
					raise Exception("END")

				if 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # CLIC ON BACK
					raise Exception("BACK")

			if event.type == QUIT:
				raise Exception("QUIT")



#########################             MAIN               ###############################################################
pygame.init()
fenetre = pygame.display.set_mode((1024, 768))
window_menu()
pygame.display.set_caption("the soul of Gulungan")
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
					try:                           # EXCEPTION
						window_nameSelect()
					except Exception as exep:
						if exep.args[0] == "QUIT":
							continuer = 0
						if exep.args[0] == "BACK":
							pygame.mixer.music.load("sound/musique_menu.wav")
							pygame.mixer.music.play(-1)
							window_menu()
							status = "main"
							buttonStatus = "main"
						if exep.args[0] == "END":
							pygame.mixer.music.load("sound/musique_menu.wav")
							pygame.mixer.music.play(-1)
							status = "end"
							buttonStatus = "end"
							window_end()

				if 818 < event.pos[0] < 1014 and 660 < event.pos[1] < 758:  # CLIC ON QUITTER
					continuer = 0

				if 10 < event.pos[0] < 206 and 661 < event.pos[1] < 758:  # CLIC ON CREDITS
					status = "credits"
					window_credits()

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
							buttonStatus = "back"

					else:
						if buttonStatus != "main":
							back = pygame.image.load("images/back.png")
							back = pygame.transform.scale(back, (150, 75))
							fenetre.blit(back, (10, 10))
							buttonStatus = "main"

		elif status == "end":  # END
			if event.type == MOUSEBUTTONDOWN and event.button == 1:   # CLIC
				if 190 < event.pos[0] < 490 and 600 < event.pos[1] < 750:  # CLIC ON BACK
					status = "main"
					window_menu()

				if 500 < event.pos[0] < 800 and 600 < event.pos[1] < 750:  # CLIC ON START
					name = getAllScores()[len(getAllScores()) -2]
					# pygame.mixer.music.load("sound/musique_game.wav")
					# pygame.mixer.music.play(-1)
					# saveNew(name, game())  # ACTUAL GAME
					# pygame.mixer.music.load("sound/musique_menu.wav")
					# pygame.mixer.music.play(-1)
					# raise Exception("END")
					try:                           # EXCEPTION
						pygame.mixer.music.load("sound/musique_game.wav")
						pygame.mixer.music.play(-1)
						game(name)   # ACTUAL GAME
					except Exception as exep:
						if exep.args[0] == "QUIT":
							continuer = 0
						if exep.args[0] == "BACK":
							pygame.mixer.music.load("sound/musique_menu.wav")
							pygame.mixer.music.play(-1)
							window_menu()
							status = "main"
							buttonStatus = "main"
						if exep.args[0] == "END":
							pygame.mixer.music.load("sound/musique_menu.wav")
							pygame.mixer.music.play(-1)
							status = "end"
							buttonStatus = "end"
							window_end()

			if event.type == MOUSEMOTION:
				if 190 < event.pos[0] < 490 and 600 < event.pos[1] < 750:  # MOTION ON BACK
					if buttonStatus != "back":
						print("BACK should RED")
						backOnClick = pygame.image.load("images/back_onclick.png")
						backOnClick = pygame.transform.scale(backOnClick, (300, 150))
						fenetre.blit(backOnClick, (190, 600))
						buttonStatus = "back"

				elif 500 < event.pos[0] < 800 and 600 < event.pos[1] < 750:  # MOTION ON START
					if buttonStatus != "start":
						startOnClick = pygame.image.load("images/start_onclic.png")
						startOnClick = pygame.transform.scale(startOnClick, (300, 150))
						fenetre.blit(startOnClick, (500, 600))
						buttonStatus = "start"

				else:
					if buttonStatus != "end":
						back = pygame.image.load("images/back.png")
						start = pygame.image.load("images/start.png")

						back = pygame.transform.scale(back, (300, 150))
						start = pygame.transform.scale(start, (300, 150))

						fenetre.blit(back, (190, 600))
						fenetre.blit(start, (500, 600))
						buttonStatus = "end"

		elif status == "credits":
			if event.type == MOUSEBUTTONDOWN and event.button == 1:   # CLIC
				if 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # CLIC ON BACK
					status = "main"
					window_menu()

			if event.type == MOUSEMOTION:   # MOTION
				if 10 < event.pos[0] < 160 and 10 < event.pos[1] < 85:  # MOTION ON BACK
					if buttonStatus != "back":
						backOnClick = pygame.image.load("images/back_onclick.png")
						backOnClick = pygame.transform.scale(backOnClick, (150, 75))
						fenetre.blit(backOnClick, (10, 10))
						buttonStatus != "back"

				else:
					if buttonStatus != "main":
						back = pygame.image.load("images/back.png")
						back = pygame.transform.scale(back, (150, 75))
						fenetre.blit(back, (10, 10))
						buttonStatus != "main"

	pygame.display.flip()