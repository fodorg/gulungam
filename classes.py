import pygame
from const import *



class Sprit(pygame.sprite.Sprite):

    def __init__(self):#ajouter image
        super().__init__()


    def deplacer(self, dir = 0):
        self.rect.x = self.rect.x-dir


class Perso(Sprit):
    """Classe permettant de créer un personnage"""

    def __init__(self):
        super().__init__()
        # Sprites du personnage
        # Position du personnage en cases et en pixels
        self.image = pygame.image.load(persoImgDesc).convert_alpha()
        #self.image = pygame.transform.scale(self.image, (100, 133))
        self.vh = vitesseDir
        self.buff = ""
        self.a = acceleration
        self.duraBuff = 0
        self.v = -vitesse
        self.rect = self.image.get_rect()
        self.rect.y = 600
        self.rect.x = 400
        self.hitbox = (self.rect.x+20, self.rect.y, 60, 100)
        self.son = pygame.mixer.Sound("sound/ressort1.wav")

    def bondir(self, dir = 0):
        self.rect.x=self.rect.x+dir
        self.rect.y = self.rect.y+self.v
        self.hitbox = (self.rect.x+20, self.rect.y, 60, 100)
        if self.rect.bottom > (height-150):
            self.v = -vitesse
            self.changeimg();
        else:
            self.v = self.v + self.a
            self.v = min(self.v, 25)
        if self.v == 0 or self.v > -vitesse+(self.a*2):
            self.changeimg()

    def changeimg(self):
        if self.v <= -vitesse:
            self.son.play()
            self.image = pygame.image.load(persoImgBounce).convert_alpha()
        elif self.v < 0:
            self.image = pygame.image.load(persoImgMont).convert_alpha()
            #self.rect.y = self.rect.y+20
        else:
            self.image = pygame.image.load(persoImgDesc).convert_alpha()
            #self.rect.y = self.rect.y-3
        self.rect.width = self.image.get_rect().width
        self.rect.height = self.image.get_rect().height

    def ralenti(self):
        self.vh = vitesseDir/2
        self.buff = "slow"
        self.startBuff = pygame.time.get_ticks()
    def buff(self):
        if self.buff != "":
            self.duraBuff = 5 - (pygame.time.get_ticks() - self.startBuff) / 1000  # calculate how many seconds
            if self.duraBuff < 0:#on enleve le buff
                if self.buff == "slow":
                    self.vh = vitesseDir
            self.buff = ""
    def deplacer(self, dir = 0):
        return 0

class Platform(Sprit):

    def __init__(self, x, y, w, h,img):
        super().__init__()
        img = "images/"+img
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Speeder(Sprit):

    def __init__(self, x, y, w, h,img):
        super().__init__()
        img = "images/"+img
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x





