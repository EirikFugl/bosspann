import pygame as p
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



skjermInfo = p.display.Info()
vinduBredde = skjermInfo.current_w * 1/3
vinduHøyde = skjermInfo.current_h -60

vindu = p.display.set_mode(((vinduBredde,vinduHøyde)))
p.display.set_caption("Sjølinje-spill")


bilFart = 0
bilSvingFart = 0

class Bil():
    def __init__(self,fart,størrelse,modell,posisjon,retning,føre):
        self.fart = fart
        self.størrelse = størrelse
        self.modell = modell
        self.posisjon = posisjon
        self.retning = retning
        self.føre = føre
    
    def getFart(self):
        return self.fart
    
    def getStørrelse(self):
        return self.størrelse
    
    def getModell(self):
        return self.modell

    def getPosisjon(self):
        return self.posisjon
    
    def getRetning(self):
        return self.retning




class SpillerBil(Bil):
    def __init__(self,fart,størrelse,modell,posisjon,føre,akselerasjon,bremse,svinge):
        super().__init__(fart,størrelse,modell,posisjon,føre)
        self.akselerasjon = akselerasjon
        self.bremse = bremse
        self.svinge = svinge
    
    def getAkselerasjon(self):
        return self.akselerasjon
    
    def getBremse(self):
        return self.bremse
    
    def getSvinge(self):
        return self.svinge
    
    def akselerer(self):
        self.fart+=self.akselerasjon

    def brems(self):
        self.fart+=self.bremse

    def svinge(self):
        self.posisjon += self.svinge
    







time.sleep(2)