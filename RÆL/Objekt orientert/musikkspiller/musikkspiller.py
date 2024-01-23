import pygame
from time import sleep as s

file = 'some.mp3'
#pygame.init()

file = 'Objekt orientert\musikkspiller\musikk\outro-song_oqu8zAg.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play() 
while pygame.mixer.music.get_busy():
    s(0.1)


class Sang:
    def __init__(self,tittel, filnavn):
        self.tittel = tittel
        self.filnavn = filnavn

    def sangTittel(self):
        return self.tittel
    
    def sangFil(self):
        return self.filnavn



class Spiller:
    def __init__(self,)    






#player
#press space for å pause, unpause
#press r for å rewinde
#s for skip
#o for å repeate
#get_pos for å lage tidslinje el. bar
#q for å queue

