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






###   KONTROLLER   ###
# Pil venstre/høyre for svinge venstre/høyre
# Pil opp/ned for akselere/bremse/rygge
# LShift + 1,2,3,4,5,R for å skifte gir
# Girene må opp cirka hver 40. km/h
# Altså 1. gir opp til 40 km/h, 3. gir mellom 80 og 120 km/h
# Esc for å avslutte
#
#
# I tillegg får du opp framepacing og litt sånn
# Det er mest for å se om spillet hakker, eller om noe er uoptimalisert
# Lager en graf etter avsluttet spill som viser tid brukt på hver frame
# Lykke til!






# Fjerner "Hello from pygame" teksten
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'alhamdillulah fjern teksten'

 # importerer ting
import pygame as p
from pygame.locals import *
import random as r
import math as m
import matplotlib.pyplot as plt
import time as t
import os

# lager talliste for å hente tilfeldige tall raskere
langTall = []
for i in range(10000):
    langTall.append(i)


# importerer bildefiler

def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse # fra linus
    return os.path.join(os.path.dirname(__file__), relRef)

bilBilde = absRef("Sjølinje-bilder/bilBilde.png")
bakgrunnBilde = absRef("Sjølinje-bilder/bakgrunnBilde.jpg")
treBilde = absRef("Sjølinje-bilder/treBilde.png")
eksplosjonBilde = absRef("Sjølinje-bilder/eksplosjonBilde.png")

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


eksplosjon = p.image.load(eksplosjonBilde).convert_alpha()
eksplosjon = p.transform.scale(eksplosjon,(300,300))
# ekrect = eksplosjon.get_rect()
# ekrect.center = eksplosjon.get_rect().center


klokke = p.time.Clock()

font = p.freetype.SysFont("Arial Black", 30)
stor_font = p.freetype.SysFont("Arial Black", 42)
fontGul = p.freetype.SysFont("Arial Black", 35)

 # Konstanter

størrelse = 0.35
maksVinkel = 15
ryggeFart = 50
maksFart = 1000


fps = 60
fartsKorrigering = 0.02
spawnsjanse = 4
svingt = False
krasjet = False

globalFart = 0
rette_opp_fart = globalFart
spawnFaktor = 100*globalFart/maksFart+20
korrektFart = True



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
        self.gir = 1


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
        global korrektFart
        global krasjet
        

        match self.gir:
            case 1: 
                if globalFart <= maksFart/5:
                    self.aksel = 4
                    korrektFart = True
                else: 
                    self.aksel = 1.5 
                    korrektFart = False
            case 2: 
                if globalFart > maksFart/5 and globalFart <= maksFart/5*2:
                    self.aksel = 4
                    korrektFart = True
                else: 
                    self.aksel = 1.5
                    korrektFart = False
            case 3: 
                if globalFart > maksFart/5*2 and globalFart <= maksFart/5*3:
                    self.aksel = 4
                    korrektFart = True
                else: 
                    self.aksel = 1.5
                    korrektFart = False
            case 4: 
                if globalFart > maksFart/5*3 and globalFart <= maksFart/5*4:
                    self.aksel = 4
                    korrektFart = True
                else: 
                    self.aksel = 1.5
                    korrektFart = False 
            case 5: 
                if globalFart > maksFart/5*4:
                    self.aksel = 4
                    korrektFart = True
                else: 
                    self.aksel = 1
                    korrektFart = False
            case "R": 
                if globalFart > maksFart/2:
                    krasjet = True
                    korrektFart = False
                elif globalFart > 0:
                    self.aksel = 0
                    korrektFart = False
                else: 
                    self.aksel = -1 
                    korrektFart = True

        self.aksel = self.aksel*(1.3-globalFart/maksFart)
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
        # self.rect.center = (self.x,self.y)

        if self.spiller == False:
            self.y += globalFart * fartsKorrigering
            self.y += self.fart
        self.rect.center = (self.x,self.y)



class Tre(p.sprite.Sprite):
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

spillerBil = Bil(vindubredde/2+20,vinduhøyde-100,0,spiller=True,brems=15,aksel=(5*(1-globalFart/maksFart)),retning="Med",sving=1.1)

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
    if krasjet: vindu.blit(eksplosjon,(spillerBil.x-eksplosjon.get_rect().width/2,spillerBil.y-eksplosjon.get_rect().height/2))

def velg_felt():
    a = r.randint(1,2)
    if a == 1:
        x = 155
    if a == 2:
        x = 270
    return x 


feltvalg = {
    "MotVen": {"X-Verdi": 157,
               "Y-Verdi": -50,
               "Fart": 4
               },
    "MotHøy": {"X-Verdi": 267,
               "Y-Verdi": -50,
               "Fart": 5
               },
    "MedVen": {"X-Verdi": 375,
               "Y-Verdi": -50,
               "Fart": -6
               },
    "MedHøy": {"X-Verdi": 485,
               "Y-Verdi": -50,
               "Fart": -5
               },
    }

def spawnTing(spawnSjanse):
    a = r.choice(langTall)
    if a <= spawnSjanse/4:
        kollisjonsgruppe.add(Bil(feltvalg["MotVen"]["X-Verdi"],feltvalg["MotVen"]["Y-Verdi"],feltvalg["MotVen"]["Fart"],retning="Mot"))
    
    elif a <= spawnSjanse/2:
        kollisjonsgruppe.add(Bil(feltvalg["MotHøy"]["X-Verdi"],feltvalg["MotHøy"]["Y-Verdi"],feltvalg["MotHøy"]["Fart"],retning="Mot"))

    elif a <= spawnSjanse*0.75:
        kollisjonsgruppe.add(Bil(feltvalg["MedVen"]["X-Verdi"],feltvalg["MedVen"]["Y-Verdi"],feltvalg["MedVen"]["Fart"],retning="Med"))

    elif a <= spawnSjanse:
        kollisjonsgruppe.add(Bil(feltvalg["MedHøy"]["X-Verdi"],feltvalg["MedHøy"]["Y-Verdi"],feltvalg["MedHøy"]["Fart"],retning="Med"))
    
    elif a <= spawnsjanse*1.25:
        kollisjonsgruppe.add(Tre(r.randint(0,80),0))

    elif a <= spawnSjanse*1.5:
        kollisjonsgruppe.add(Tre(r.randint(vindubredde-60,vindubredde),0))


totale_krasj = 0
krasjet = False
frameListe = []

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
    if krasjet: stor_font.render_to(vindu,(30,400),f"SUPER GAME OVER BIG L",farge["Blå"])

    if globalFart >= maksFart/5*4: font.render_to(vindu,(30,30),f"{str(int(round(globalFart/5,0)))} km/t",farge["Rød"])
    else: font.render_to(vindu,(30,30),f"{str(int(round(globalFart/5,0)))} km/t",farge["Svart"])
    # font.render_to(vindu,(30,60),f"Mus: {str(p.mouse.get_pos())}",(0, 0, 0))
    # font.render_to(vindu,(30,90),f"Krasj: {str(totale_krasj)}",(0, 0, 0))

    if dobbel == True: fontGul.render_to(vindu,(30,60),f"{str(int(round(total_lengde,0)))} m",farge["Gul"])
    else:              font.render_to(vindu,(30,60),f"{str(int(round(total_lengde,0)))} m"),farge["Svart"]

    font.render_to(vindu,(30,100),f"Gir: {spillerBil.gir}",farge["Svart"])
    if korrektFart: font.render_to(vindu,(30,130),f"Korrekt gir!",farge["Svart"])




# Main Loop ####################################################
    
kjører = True
total_lengde = 0
xVerdier = []
abna = 0

while kjører:
    klokke.tick(fps)

    starttid = t.time()

    for event in p.event.get():
        if event.type == QUIT:
            kjører = False



       #   fartendringer
    if krasjet: 
        globalFart = 0
        maksVinkel = 0
        spillerBil.sving = 0
        spawnFaktor = 0
        
    
    if spillerBil.x < 90:
        globalFart = globalFart*0.9
    elif spillerBil.x > 560:
        globalFart = globalFart*0.9
    else: globalFart = globalFart*0.9989 


       #   dobbel poeng for motgående felt
    if spillerBil.x <= vindubredde/2:
        total_lengde += globalFart/12/fps*2
        dobbel = True
    else:
        total_lengde+=globalFart/12/fps
        dobbel = False




       #   gjenopretting av bil
    svingt = False

    rettelse = 1
    retning = ""
    rette_opp_fart = globalFart/maksFart*2

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
    
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_1]:
        spillerBil.gir = 1
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_2]:
        spillerBil.gir = 2
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_3]:
        spillerBil.gir = 3
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_4]:
        spillerBil.gir = 4
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_5]:
        spillerBil.gir = 5
    if trykkedeTaster[K_LSHIFT] and trykkedeTaster[K_r]:
        spillerBil.gir = "R"
    


    if svingt == False:
        if spillerBil.vinkel <0: spillerBil.vinkel += 2
        if spillerBil.vinkel >0: spillerBil.vinkel -= 2



       #   gjøre / tegne ting
    
    spawnTing(spawnFaktor*2)

    sjekKollisjon(kollisjonsgruppe)

    oppdaterAlt()

    tegnAlt()

    tegnUI()

    frametime = round((t.time()-starttid)*1000,1)
    frameListe.append((t.time()-starttid)*1000)
    abna+=1
 
 
 
    xVerdier.append(abna)




    font.render_to(vindu,(400,30),f"Frametime: {frametime} ms")
    # if frametime > 17: print("hakk",frametime," ms")
    

    p.display.flip()


# POST SPILL TING ############################################

p.quit()


gjennomsnittsFrame = 0
for ting in frameListe:
    gjennomsnittsFrame+=ting
gjennomsnittsFrame = gjennomsnittsFrame / len(frameListe)



plt.plot(xVerdier,frameListe)
plt.show()

print(f"Gjennomsnitts-framepacing = {round(gjennomsnittsFrame,3)} ms\nMaks (før det hakker): {round(1000/fps,1)} ms")
print(f"Total Lengde / poeng: {round(total_lengde,0)} m")
exit()

# Kilder:
# Hoveddelen av scrollefunksjonen er hentet fra:
# https://www.geeksforgeeks.org/creating-a-scrolling-background-in-pygame/
#
# Funksjonen absRef() er hentet fra:
# Linus Gabriel Berg-Høisæter
#
#
