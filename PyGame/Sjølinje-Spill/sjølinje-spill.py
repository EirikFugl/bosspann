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
import os
\

# importerer bildefiler
# bilBilde = r"C:\Users\eirik\Downloads\KxSI1Mx.png"
# bakgrunnBilde = r"C:\Users\eirik\Downloads\360_F_271939209_fjpuoikPWbsvipp0R6XNzzlFohw76Mwb.jpg"
# treBilde = r"C:\Users\eirik\Downloads\tumblr_df214276172b6f4c6eac99ebec69c734_e0846910_500.png"


def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse # fra linus
    return os.path.join(os.path.dirname(__file__), relRef)

bilBilde = absRef("Sjølinje-bilder/bilBilde.png")
bakgrunnBilde = absRef("Sjølinje-bilder/bakgrunnBilde.jpg")
treBilde = absRef("Sjølinje-bilder/treBilde.png")

 # farger
farge = {"Rød":(255,0,0),"Grønn":(0,255,0),"Blå":(0,0,255),"Svart":(0,0,0),"Grå":(50,50,50),"Gul":(255,255,0)}


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
stor_font = p.freetype.SysFont("Arial Black", 42)
fontGul = p.freetype.SysFont("Arial Black", 35)

 # Konstanter

størrelse = 0.4
maksVinkel = 15
ryggeFart = 20
maksFart = 1000

fps = 100
fartsKorrigering = 0.02
spawnsjanse = 4
svingt = False
krasjet = False

globalFart = 0
rette_opp_fart = globalFart


# Klasser

class Bil(p.sprite.Sprite):
    def __init__(self,x,y,fart,bilde=bilBilde,aksel=0.5,brems=0.5,sving=1,spiller=False,retning=0):
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
        if retning=="Mot":
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

spillerBil = Bil(vindubredde/2+20,vinduhøyde-100,0,spiller=True,brems=5,aksel=5,retning="Med")

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

def velg_felt():
    a = r.randint(1,2)
    if a == 1:
        x = 155
    if a == 2:
        x = 270
    return x 

def spawnTrær(spawnSjanse):
    a = r.randint(0,100)
    if a >= 0 and a<= spawnSjanse/10:
        kollisjonsgruppe.add(Krasj(r.randint(0,80),0))
        kollisjonsgruppe.add(Krasj(r.randint(vindubredde-60,vindubredde),0))
        # kollisjonsgruppe.add(Bil(velg_felt(),0,5))

feltvalg = {
    "MotVen": {"X-Verdi": 157,
               "Y-Verdi": 0,
               "Fart": 4
               },
    "MotHøy": {"X-Verdi": 267,
               "Y-Verdi": 0,
               "Fart": 3
               },
    "MedVen": {"X-Verdi": 375,
               "Y-Verdi": 0,
               "Fart": -5
               },
    "MedHøy": {"X-Verdi": 485,
               "Y-Verdi": 0,
               "Fart": -4
               },
    }

def spawnBiler(spawnSjanse):
    a= r.randint(0,1000)
    if a >=0 and a<= spawnSjanse/50:
        kollisjonsgruppe.add(Bil(feltvalg["MotVen"]["X-Verdi"],feltvalg["MotVen"]["Y-Verdi"],feltvalg["MotVen"]["Fart"],retning="Mot"))
    a= r.randint(0,1000)
    if a >=0 and a<= spawnSjanse/50:
        kollisjonsgruppe.add(Bil(feltvalg["MotHøy"]["X-Verdi"],feltvalg["MotHøy"]["Y-Verdi"],feltvalg["MotHøy"]["Fart"],retning="Mot"))
    a= r.randint(0,1000)
    if a >=0 and a<= spawnSjanse/50:
        kollisjonsgruppe.add(Bil(feltvalg["MedVen"]["X-Verdi"],feltvalg["MedVen"]["Y-Verdi"],feltvalg["MedVen"]["Fart"],retning="Med"))
    a= r.randint(0,1000)
    if a >=0 and a<= spawnSjanse/50:
        kollisjonsgruppe.add(Bil(feltvalg["MedHøy"]["X-Verdi"],feltvalg["MedHøy"]["Y-Verdi"],feltvalg["MedHøy"]["Fart"],retning="Med"))




totale_krasj = 0
krasjet = False

def sjekKollisjon(gruppe):
    global globalFart
    global totale_krasj
    global krasjet

    kolliderer=p.sprite.spritecollide(spillerBil,gruppe,True)
    if str(kolliderer) != "[]":
        globalFart = 0
        spillerBil.aksel=0
        spillerBil.brems=0
        totale_krasj+=1
        
        krasjet = True

def tegnUI():
    if krasjet: stor_font.render_to(vindu,(0,400),f"SUPER GAME OVER BIG L",(0, 0, 0))
    font.render_to(vindu,(30,30),f"{str(int(round(globalFart/6,0)))} km/t",(0, 0, 0))
    # font.render_to(vindu,(30,60),f"Mus: {str(p.mouse.get_pos())}",(0, 0, 0))
    # font.render_to(vindu,(30,90),f"Krasj: {str(totale_krasj)}",(0, 0, 0))

    if dobbel == True: fontGul.render_to(vindu,(30,60),f"{str(int(round(total_lengde,0)))} m",farge["Gul"])
    else:              font.render_to(vindu,(30,60),f"{str(int(round(total_lengde,0)))} m")

# Main Loop
kjører = True
total_lengde = 0


while kjører:
    klokke.tick(fps)


    abab,baba = spillerBil.rect.center
    if abab<= vindubredde/2: 
        total_lengde+=globalFart/12/fps*2
        dobbel = True
    else: 
        total_lengde+=globalFart/12/fps
        dobbel = False


    svingt = False

    for event in p.event.get():
        if event.type == QUIT:
            kjører = False
            p.quit()
            exit()

    rettelse = 1
    retning = ""
    rette_opp_fart = globalFart/100

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

    if trykkedeTaster[K_LEFT] and trykkedeTaster[K_RIGHT]:
        spillerBil.vinkel = pre_sving
        spillerBil.x, spillerBil.y = pre_sving_kord


    if svingt == False:
        if spillerBil.vinkel <0: spillerBil.vinkel += 2
        if spillerBil.vinkel >0: spillerBil.vinkel -= 2


    spawnTrær(3*globalFart/maksFart*1.1)
    spawnBiler(3*globalFart/maksFart*1.1)

    sjekKollisjon(kollisjonsgruppe)

    

    oppdaterAlt()
    tegnAlt()

    tegnUI()

    p.display.flip()