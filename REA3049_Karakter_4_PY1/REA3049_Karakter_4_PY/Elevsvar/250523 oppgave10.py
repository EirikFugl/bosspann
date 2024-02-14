import random

import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

pg.init()

font = pg.font.SysFont("Arial", 24)

VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

k = 1
#haddr brukt dette om jeg fikk til implemtenteringen av hindringer
xBox = 0
yBox = 0

poeng = 0

class Troll:
    """Klasse for å representere trollet"""

    def __init__(self, x, y, xfart, yfart , lengde, farge, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.xfart = xfart
        self.yfart = yfart
        self.lengde = lengde
        self.farge = farge
        self.vindusobjekt = vindusobjekt


    def tegn(self):
        """Metode for å tegne trollet"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y, self.lengde, self.lengde))

    def flytt(self, taster):
        """Metode for å flytte trollet"""
        if taster[K_UP]:
            self.yfart = -0.1 * k
            self.xfart = 0
        if taster[K_DOWN]:
            self.yfart = 0.1 * k
            self.xfart = 0
        if taster[K_LEFT]:
            self.xfart = -0.1 * k
            self.yfart = 0
        if taster[K_RIGHT]:
            self.xfart = 0.1 * k
            self.yfart = 0

        if self.xfart !=0:
            self.x += self.xfart
        if self.yfart !=0:
            self.y += self.yfart

        if self.x > 490 or self.x < 0:
            print(f"Du fikk {poeng} poeng!")
            pygame.quit()
        if self.y > 490 or self.y < 0:
            print(f"Du fikk {poeng} poeng!")
            pygame.quit()

class Box:
    def __init__(self, x, y, lengde, farge, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.lengde = lengde
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne boksen"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y, self.lengde, self.lengde))



class HindringBox():
    def __init__(self, x, y, lengde, farge, vindusobjekt):
        """Konstruktør"""
        super().__init__()
        self.x = x
        self.y = y
        self.lengde = lengde
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne boksen"""
        pg.draw.rect(self.vindusobjekt, self.farge, (self.x, self.y, self.lengde, self.lengde))

    def kollisjon(self):
        if m.sqrt((troll.x - box.x)**2) + m.sqrt((troll.y - box.y)**2) <= 10:
            print(f"Du fikk {poeng} poeng!")
            pygame.quit()


#Definerer objektene som tas inn i klassene
troll = Troll(200, 200, 0.1, 0, 20, (255, 69, 0), vindu)
box = Box(random.randint(0,490), random.randint(0,490), 20, (255,255,255), vindu)
box2 = Box(random.randint(0,490), random.randint(0,490), 20, (255,255,255), vindu)
box3 = Box(random.randint(0,490), random.randint(0,490), 20, (255,255,255), vindu)
hindring = HindringBox(xBox, yBox, 20, (255, 255, 255), vindu)

fortsett = True
while fortsett:
#spillloop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    trykkede_taster = pg.key.get_pressed()

    vindu.fill((0, 0, 0))
#tegner masse foraskjellige ting
    bilde = font.render(f"Poeng: {poeng}", True, (255, 255, 255))
    vindu.blit(bilde, (400, 20))
    troll.tegn()
    troll.flytt(trykkede_taster)
    box.tegn()
    box2.tegn()
    box3.tegn()
# sjekker avstanden fra boksene
    avstandBox1 = m.sqrt((troll.x - box.x)**2) + m.sqrt((troll.y - box.y)**2)
    avstandBox2 = m.sqrt((troll.x - box2.x) ** 2) + m.sqrt((troll.y - box2.y) ** 2)
    avstandBox3 = m.sqrt((troll.x - box3.x) ** 2) + m.sqrt((troll.y - box3.y) ** 2)

    if avstandBox1 <= 10:
        box.x = random.randint(0,490)
        box.y = random.randint(0,490)
        poeng = poeng + 1
        k = k * 1.1
    if avstandBox2 <= 10:
        box2.x = random.randint(0,490)
        box2.y = random.randint(0,490)
        poeng = poeng + 1
        k = k * 1.1
    if avstandBox3 <= 10:
        box3.x = random.randint(0,490)
        box3.y = random.randint(0,490)
        poeng = poeng + 1
        k = k * 1.1


    pg.display.flip()

pg.quit()