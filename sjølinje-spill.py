### SJØLINJE SPILL

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


 # Fjerner "Hello from pygame" teksten
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'alhamdillulah fjern teksten'

 # importerer ting
import pygame as p
from pygame.locals import *
import random as r
import math as m

 # importerer bildefiler
bilBilde = r"C:\Users\eirik\Downloads\KxSI1Mx.png"
bakgrunnBilde = r"C:\Users\eirik\Downloads\360_F_271939209_fjpuoikPWbsvipp0R6XNzzlFohw76Mwb.jpg"
treBilde = r"C:\Users\eirik\Downloads\tumblr_df214276172b6f4c6eac99ebec69c734_e0846910_500.png"

 # farger
farge = {"Rød":(255,0,0),"Grønn":(0,255,0),"Blå":(0,0,255),"Svart":(0,0,0),"Grå":(50,50,50)}


 # skjerm setup
p.init()

vindubredde = 600
vinduhøyde = 800
vindu = p.display.set_mode((vindubredde,vinduhøyde))


# bakgrunn setup
bakgrunn = p.image.load(bakgrunnBilde).convert_alpha()
bakgrunn = p.transform.rotozoom(bakgrunn,90,2)

vindubredde = bakgrunn.get_rect().width-52
vindu = p.display.set_mode((vindubredde,vinduhøyde))
p.display.set_caption("Sjølinje-spill")

scroll = 0
tiles = m.ceil(vinduhøyde / bakgrunn.get_height()) + 1


klokke = p.time.Clock()

font = p.freetype.SysFont("Arial Black", 30)
stor_font = p.freetype.SysFont("Arial Black", 60)

 # Konstanter

størrelse = 0.4
maksVinkel = 15
ryggeFart = 20
maksFart = 600
fps = 100
fartsKorrigering = 0.02
spawnsjanse = 4
svingt = False
krasjet = False

globalFart = 0


# Klasser

class Bil(p.sprite.Sprite):
    def __init__(self,x,y,fart,bilde=bilBilde,aksel=0.5,brems=0.5,sving=1,spiller=False):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.bilde = bilde
        self.fart = fart
        self.aksel = aksel
        self.brems = brems
        self.sving = sving
        self.spiller = spiller

        self.vinkel = 0

        self.image = p.image.load(self.bilde).convert_alpha()
        if spiller == False:
            self.image = p.transform.rotate(self.image,180)
        self.image = p.transform.smoothscale(self.image,(self.image.get_rect().width*størrelse*0.1,self.image.get_rect().height*størrelse*0.1))
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def akselerer(self):
        global globalFart
        global maksFart
        if  globalFart < maksFart: globalFart+=self.aksel
    
    def bremse(self):
        global globalFart
        global ryggeFart
        if globalFart > -ryggeFart: globalFart -=self.brems
    
    def svinge(self,retning):
        global maksVinkel
        global svingt

        if retning == "venstre":
            svingt = True
            if self.vinkel < maksVinkel:
                self.vinkel += self.sving
            self.x -= abs(self.vinkel)*globalFart/maksFart/2

        if retning == "høyre":
            svingt = True
            if self.vinkel > -maksVinkel:
                self.vinkel -= self.sving
            self.x += abs(self.vinkel)*globalFart/maksFart/2
        


    def update(self):

        ## ROTASJON ##
        self.image = p.transform.rotozoom(self.orig_image,self.vinkel,1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = (self.x,self.y)

        if self.spiller == False:
            self.y += globalFart * fartsKorrigering
            self.y += self.fart


class Krasj(p.sprite.Sprite):
    def __init__(self,x,y,bilde=treBilde):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = p.image.load(bilde).convert_alpha()
        self.image = p.transform.smoothscale(self.image,(self.image.get_rect().width*størrelse*0.4,self.image.get_rect().height*størrelse*0.4))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    
    def update(self):
        self.y += globalFart * fartsKorrigering
        self.rect.center = (self.x,self.y)


# sprite setup

spillerBil = Bil(vindubredde/2+20,vinduhøyde-100,0,spiller=True,brems=2,aksel=2)

bilgruppe = p.sprite.Group()
kollisjonsgruppe = p.sprite.Group()

bilgruppe.add(spillerBil)


# vanlige funksjoner
def oppdaterAlt():
    kollisjonsgruppe.update()    
    bilgruppe.update()

def tegnAlt():
    kollisjonsgruppe.draw(vindu)  
    bilgruppe.draw(vindu)  

def spawnTrær(spawnSjanse):
    a = r.randint(0,100)
    if a >= 0 and a<= spawnSjanse/10:
        kollisjonsgruppe.add(Krasj(r.randint(0,vindubredde),0))
        kollisjonsgruppe.add(Bil(200,20,5))
    

def sjekKollisjon(gruppe):
    global globalFart
    kolliderer=p.sprite.spritecollide(spillerBil,gruppe,False)
    if str(kolliderer) != "[]":
        globalFart = 0
        spillerBil.aksel=0
        stor_font.render_to(vindu,(vindubredde/2-100,vinduhøyde/2),f"GAME OVER",(0, 0, 0))

# Main Loop
kjører = True

while kjører:
    klokke.tick(fps)

    svingt = False

    for event in p.event.get():
        if event.type == QUIT:
            kjører = False
            p.quit()
            exit()

    rettelse = 1
    retning = ""

    vindu.fill(farge["Svart"])

    ## Scrolle bakgrunnsbilde ##

    tall1 = 0
    while tall1 < tiles:
        vindu.blit(bakgrunn,(-50,(bakgrunn.get_height()*tall1+scroll)*-1))
        tall1 +=1
    
    scroll -= globalFart*fartsKorrigering

    if abs(scroll) > bakgrunn.get_height():
        scroll = 0

    
    ## INPUTS
    
    trykkedeTaster = p.key.get_pressed()

    if trykkedeTaster[K_ESCAPE]:
        kjører = False
    
    if trykkedeTaster[K_UP]:
        spillerBil.akselerer()
    
    if trykkedeTaster[K_DOWN]:
        spillerBil.bremse()
    
    pre_sving = spillerBil.vinkel
    pre_sving_kord = spillerBil.x, spillerBil.y

    if trykkedeTaster[K_LEFT]:
        spillerBil.svinge("venstre")
    
    if trykkedeTaster[K_RIGHT]:
        spillerBil.svinge("høyre")

    # if trykkedeTaster[K_LEFT] and trykkedeTaster[K_RIGHT]:
    #     spillerBil.vinkel = pre_sving
    #     spillerBil.x, spillerBil.y = pre_sving_kord

    

    if svingt == False:
        if spillerBil.vinkel <0: spillerBil.vinkel += 0.6
        if spillerBil.vinkel >0: spillerBil.vinkel -= 0.6


    if krasjet: sjekKollisjon(kollisjonsgruppe), spawnTrær(spawnsjanse)


    oppdaterAlt()
    tegnAlt()

    font.render_to(vindu,(30,30),f"Fart: {str(int(round(globalFart/6,0)))} km/t",(0, 0, 0))
    p.display.flip()