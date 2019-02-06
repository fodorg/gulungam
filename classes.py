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
        self.son = pygame.mixer.Sound("sound/ressort1.wav")

        self.hitbox = self.rect
        self.hitbox.x = self.rect.x+20
        self.hitbox.width = self.rect.width-40


        self.hitb = hitb(self);

    def bondir(self, dir = 0):
        self.rect.x=self.rect.x+dir
        self.hitbox.x = self.hitbox.x+dir
        self.rect.y = self.rect.y+self.v
        if self.rect.bottom > (height-148):
            self.v = -vitesse
            self.changeimg();
        else:
            self.v = self.v + self.a
            self.v = min(self.v, 25)
        if self.v == 0 or self.v > -vitesse+(self.a*2):
            self.changeimg()
        self.hitb.updt(self);

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

        self.hitbox = pygame.Rect(440, self.rect.y, self.rect.w-40, self.rect.h)

    def addBuff(self, buff):
        if self.buff != buff:
            self.buff = buff
            if buff == "r":
                self.vh = vitesseDir/4
            elif buff == "a":
                self.vh = vitesseDir*2
            self.startBuff = pygame.time.get_ticks()
            return 1
        else:
            return 0

    def deBuff(self):
        if self.buff == "r" or self.buff == "a":
            self.vh = vitesseDir
        self.buff=""


    def deplacer(self, dir = 0):
        return 0

    def collided(sprite, other):
        """Check if the hitboxes of the two sprites collide."""
        return sprite.hitbox.colliderect(other.hitbox)


class Platform(Sprit):

    def __init__(self,img, x, y, w, h):
        super().__init__()
        img = "images/"+img
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class BlockBuff(Sprit):

    def __init__(self,typeBuff,img, x, y, w, h):
        super().__init__()
        if typeBuff == "r":
            img = "images/"+img
        else:
            img = "images/"+img
        self.typeBuff = typeBuff
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class hitb(pygame.sprite.Sprite):

    def __init__(self,perso):
        super().__init__()
        self.rect = perso.image.get_rect()
        self.updt(perso)

    def updt(self, perso):
        self.rect.x = perso.rect.x+20
        self.rect.y = perso.rect.y
        self.rect.h = perso.rect.h
        self.rect.w = perso.rect.w-42

