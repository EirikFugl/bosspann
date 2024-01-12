from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'alhamdillulah fjern teksten'
import pygame as p
from pygame.locals import *
from pygame.sprite import Sprite, Group
import random as r
import time


p.init()

# Du kjører på sjølinjen, fire felt, dobbel poeng for feil retning, fart øker mye, 
# svinging minker med fart, biler kommer imot, plusspoeng for near miss, poeng for antall meter, 
# ulike biler med ulik akselerasjon, fart, svinging, etc. 

# Vanskelighetsgrad basert på tid på dag: 
# lett (tirsdag - halv tolv), middels (torsdag - klokken tre), vanskelg (fredag klokken halv fem)
# modifiers:
# sol, regn, snø, slapsehelvete, klink is

# klasser:
# Bil - Fart, størrelse/hitbox, farge, type, felt (pikselverdi for kjørefeltet), retning
# Spiller - Akselerasjon, bremsing, svinging

# Gire
# Hold shift for å clutche, velg gir med 1,2,3,4,5,R

# ------------ FAKTISK GJENNOMFØRING --------------

# bruke sprites til objektene
# sprites til alt egentlig


skjermInfo = p.display.Info()
vinduBredde = 600#skjermInfo.current_w * 1/3
vinduHøyde = skjermInfo.current_h -80

vindu = p.display.set_mode(((vinduBredde,vinduHøyde)))
p.display.set_caption("Sjølinje-spill")

fargeListe = {"Rød":(255,0,0),"Grønn":(0,255,0),"Blå":(0,0,255)}

class Bil(p.sprite.Sprite):
    def __init__(self,image,x,y,bilde=r"C:\Users\eirik\Downloads\KxSI1Mx.png"):
        p.sprite.Sprite.__init__(self)
        self.image = image
        self.image = p.image.load(r"C:\Users\eirik\Downloads\KxSI1Mx.png")
        self.x = x
        self.y = y
        self.bilde = bilde

        self.image = p.transform.scale(self.image, (self.image.get_rect().width*0.05,self.image.get_rect().height*0.05)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def roter(self,vinkel):
        print(self.image.get_rect().center)
        midt = self.image.get_rect().center
        self.image = p.transform.rotate(vindu,vinkel)
        print(self.image.get_rect().center)
        self.rect = self.image.get_rect(center=midt)

vinkling = 20
bilGruppe = p.sprite.Group()

bil1 = Bil(0,300,300)
bilGruppe.add(bil1)

farger=[]
for i in range(100):
    farger.append(p.Color(r.randint(0,255),r.randint(0,255),r.randint(0,255)))


kjører = True
clock = p.time.Clock()

while kjører:

    clock.tick(10)
    for event in p.event.get():


        if event.type == QUIT:
            kjører = False
        
        # if event.type == KEYDOWN:
        #     if event.key == p.K_5:
        #         vindu.fill(farger[r.randint(0,99)])
        #     if event.key == p.K_ESCAPE:
        #         kjører == False
        #     if event.key == p.K_h:
        #         p.draw.rect(vindu, farger[r.randint(0,99)],(xPos,yPos,50,50))
        #     if event.key==p.K_g:
        #         ball.endreFart(1.1)
        #         ball2.endreFart(1.1)
    

    trykkedeTaster = p.key.get_pressed()
    if trykkedeTaster[K_UP]:
        pass
    if trykkedeTaster[K_DOWN]:
        pass
    if trykkedeTaster[K_LEFT]:
        bil1.roter(vinkling)
    if trykkedeTaster[K_RIGHT]:
        # vindu.fill(farger[r.randint(0,99)])
        bil1.roter(-vinkling)
    vindu.fill(fargeListe["Rød"])


    bilGruppe.draw(vindu)




    

    

    p.display.update()




p.quit()
exit()