from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'alhamdillulah fjern teksten'

import pygame as p
from pygame.locals import *
from pygame.sprite import Group, Sprite, Group
import random as r
import math

bilBilde = r"C:\Users\eirik\Downloads\KxSI1Mx.png"
pilBilde = r"C:\Users\eirik\Downloads\pngimg.com - red_arrow_PNG20.png"
treBilde = r"C:\Users\eirik\Downloads\tumblr_df214276172b6f4c6eac99ebec69c734_e0846910_500.png"
bakgrunnBilde = r"C:\Users\eirik\Downloads\360_F_271939209_fjpuoikPWbsvipp0R6XNzzlFohw76Mwb.jpg"

størrelse = 0.3


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

globalFart = 0

skjermInfo = p.display.Info()
vinduBredde = 600#skjermInfo.current_w * 1/3
vinduHøyde = 800#skjermInfo.current_h -80

vindu = p.display.set_mode(((vinduBredde,vinduHøyde)))
p.display.set_caption("Sjølinje-spill")

fargeListe = {"Rød":(255,0,0),"Grønn":(0,255,0),"Blå":(0,0,255)}

font = p.freetype.SysFont('Arial', 30)

class Bil(p.sprite.Sprite):
    def __init__(self,x,y,scale,bilde=bilBilde):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vinkel = 0
        self.fart = 0


        self.image = p.image.load(bilde).convert_alpha()
        self.image = p.transform.smoothscale(self.image,(self.image.get_rect().width*størrelse*0.1,self.image.get_rect().height*størrelse*0.1))
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)


    def update(self):

        ## ROTASJON ##
        self.image = p.transform.rotozoom(self.orig_image,self.vinkel,1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = (self.x,self.y)










class Trær(p.sprite.Sprite):
    def __init__(self,x,y,scale,bilde=treBilde,fart=globalFart):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        
        self.vinkel = 0
        self.fart = fart


        self.image = p.image.load(bilde).convert_alpha()
        self.image = p.transform.smoothscale(self.image,(self.image.get_rect().width*størrelse*0.4,self.image.get_rect().height*størrelse*0.4))
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
                ## ROTASJON ##
        
        # self.image = p.transform.rotozoom(self.orig_image,self.vinkel,1)
        # self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = (self.x,self.y+globalFart*0.2)


        self.y+=globalFart*0.02




tre = Trær(200,200,0.2)
bil = Bil(vindu.get_width()/2,vindu.get_height()-100,0.1)


bilGruppe = p.sprite.Group()
treGruppe = p.sprite.Group()



bilGruppe.add(bil)
treGruppe.add(tre)

farger=[]
for i in range(100):
    farger.append(p.Color(r.randint(0,255),r.randint(0,255),r.randint(0,255)))


kjører = True
clock = p.time.Clock()
maksVinkel = 10
ryggefart = 20
maksfart = 200
fps = 100
ill=0

bg = p.image.load(bakgrunnBilde).convert_alpha()
bg = p.transform.rotozoom(bg,90,2)
scroll = 0
tiles = math.ceil(vinduHøyde / bg.get_height()) + 1


while kjører:

    clock.tick(fps)
    rettelse = 1

    vindu.fill((0,0,0))
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
    
    i = 0
    while(i < tiles): 
        vindu.blit(bg, (-50,(bg.get_height()*i + scroll)*-1)) 
        i += 1

    scroll -= globalFart*0.02

  

    if abs(scroll) > bg.get_height(): 
        scroll = 0
    


        
    trykkedeTaster = p.key.get_pressed()

    if trykkedeTaster[K_ESCAPE]:
        kjører = False


    if trykkedeTaster[K_UP]:
        if globalFart < maksfart: globalFart +=0.5

    if trykkedeTaster[K_DOWN]:
        if globalFart > -ryggefart: globalFart -=0.5
        pass

    if trykkedeTaster[K_LEFT]:
        if bil.vinkel < maksVinkel:
            bil.vinkel +=1
            rettelse = 0
        bil.x-=1
        pass

    if trykkedeTaster[K_RIGHT]:
        if bil.vinkel > -maksVinkel:
            bil.vinkel -= 1
            rettelse = 0
        bil.x+=1
        pass


    if bil.vinkel <0:
        bil.vinkel +=rettelse
    elif bil.vinkel>0:
        bil.vinkel-=rettelse

    bilGruppe.update()
    bilGruppe.draw(vindu)
    treGruppe.update()
    treGruppe.draw(vindu)


    
    ill+=1

    if ill ==r.randint(100,300):
        treGruppe.add(Trær(r.randint(0,vindu.get_width()/2-50),20,0.2))
        # bilGruppe.add(Bil(r.randint(vindu.get_width()/2+20,vindu.get_width()/2+120),vindu.get_width()/2-20,vindu.get_width()/2-120))

        
        ill=0
    elif ill== r.randint(100,200):
        treGruppe.add(Trær(r.randint(vindu.get_width()/2+50,vindu.get_width()),20,0.2))
        # bilGruppe.add(Bil(r.randint(vindu.get_width()/2+20,vindu.get_width()/2+120),vindu.get_width()/2-20,vindu.get_width()/2-120))


        ill=0
    
    if ill > 500:
        ill = 0


    kolliderer=p.sprite.spritecollide(bil,treGruppe,True)
    if str(kolliderer) != "[]":
        print("KOLLISJON")





    
    font.render_to(vindu,(10,10),f"Global Fart: {str(globalFart)} piksel/frame",(0, 0, 0))
    font.render_to(vindu,(vindu.get_width()-200,20),f"Kolliderer: {kolliderer}",(0, 0, 0))
    p.display.flip()




p.quit()
exit()