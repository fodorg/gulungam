import pygame
from const import *



class Sprit(pygame.sprite.Sprite):

    def __init__(self):#ajouter image
        super().__init__()


    def deplacer(self, dir = 0):
        self.rect.x = self.rect.x-dir


class Perso(Sprit):

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
        self.rect.y = 500
        self.rect.x = 400
        self.son = pygame.mixer.Sound("sound/ressort1.wav")


        self.hitb = hitb(self);

    def bondir(self, ctrlnuage = 0):
        if self.a == 0:
            self.v = -ctrlnuage*vitesse/2
        self.rect.y = self.rect.y+self.v
        self.hitb.updt(self)
        if self.hitb.rect.bottom > (height-148):
            self.v = -vitesse
            self.rect.y = height-148-100
            self.changeimg()
        else:
            self.v = self.v + self.a
            self.v = min(self.v, 25)
        if self.v == 0 or self.v > -vitesse+(self.a*2):
            self.changeimg()
        self.hitb.updt(self)

    def changeimg(self):
        if self.a == 0:
            if(self.v > 0):
                self.image = pygame.image.load(persoImgDescNuage).convert_alpha()
            else:
                self.image = pygame.image.load(persoImgMontNuage).convert_alpha()
        elif self.v <= -vitesse+(self.a*2):
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

        #self.hitbox = pygame.Rect(440, self.rect.y, self.rect.w-40, self.rect.h)

    def addBuff(self, buff):
        if self.buff != buff:
            self.buff = buff
            self.a = acceleration
            if buff == "r":
                self.vh = vitesseDir/4
            elif buff == "a":
                self.vh = vitesseDir*2
            elif buff == "g":
                self.vh = vitesseDir
                self.a = 0
                self.v = 0
            self.startBuff = pygame.time.get_ticks()
            return 1
        else:
            return 0

    def deBuff(self):
        if self.buff == "r" or self.buff == "a":
            self.vh = vitesseDir
        elif self.buff == "g":
            self.a = acceleration
        self.buff=""

    def nuage(self, v):
        self.v = v;

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

    def __init__(self,typeBuff, x, y, w, h,dest = 0):
        super().__init__()
        img = "images/buff"+typeBuff+".png"
        self.dest = dest
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
        self.rect.y = perso.rect.y+30
        self.rect.h = 80
        self.rect.w = 60

