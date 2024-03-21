# skriver alt på nytt fordi fuck det som ikke er sprites ærlig talt

import pygame as p
import random as r
import sys
from os import environ
environ['p_HIDE_SUPPORT_PROMPT'] = 'fjern teksten'


p.init()
screen = p.display.set_mode((600, 400))

clock = p.time.Clock()

class Spiller(p.sprite.Sprite):
    def __init__(self,x,y,fart):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = fart
        self.killbox = 30

        

    def move(self, key):
        if key[p.K_w]:
            self.y -= self.speed
        if key[p.K_s]:
            self.y += self.speed
        if key[p.K_a]:
            self.x -= self.speed
        if key[p.K_d]:
            self.x += self.speed
    


    def update(self):
        p.draw.circle(screen, (255, 255, 255), (self.x, self.y), 15)

        


class Fiende(p.sprite.Sprite): # fuck arv sprites er freaky på den arv tingen
    def __init__(self,x,y,fart):
        p.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed  = int(fart) * 0.1
        self.rect = p.Rect(1,1,10,10)
        self.rect.center = (self.x,self.y)
    
    def move(self):
        if player.x < self.x:
            self.x -= self.speed
        elif player.x > self.x:
            self.x += self.speed
        if player.y < self.y:
            self.y -= self.speed
        elif player.y > self.y:
            self.y += self.speed
    
    def update(self):
        Fiende.move(self)
        p.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)

        if p.key.get_pressed()[p.K_SPACE]:
            p.draw.circle(screen, (255,0,0), (player.x, player.y),40)

            if self.x >= player.x-40 and self.x <= player.x+40 and self.y >= player.y-40 and self.y <= player.y+40:
                Fiende.kill(self)

        if self.x >= player.x-15 and self.x <= player.x+15 and self.y >= player.y-15 and self.y <= player.y+15:
            print("GAME OVER\n"*100)
            p.quit()
            sys.exit()



player = Spiller(300,200,5)

fiende_gruppe = p.sprite.Group()
fiende_teller = 0



def main():
    global fiende_teller


    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()    

        

        screen.fill((0,0,0))

        player.move(p.key.get_pressed())
        player.update()
        fiende_gruppe.update()

        if fiende_teller >= 60:
            fiende_gruppe.add(Fiende(r.randint(0,600),r.randint(0,400),r.randint(10,20)))
            fiende_teller = 0

        
        p.display.flip()


        fiende_teller += 1
        clock.tick(60)

    






if __name__ == "__main__":
    main()