import pygame 
import sys
import random as r

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.y = 200
        self.speed = 5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 15)

    def move(self, key):
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed

pygame.init()
screen = pygame.display.set_mode((600, 400))

class Fiende(p.sprite.Sprite): # fuck arv jeg


fiende_gruppe = pygame.sprite.Group

def main():
    
    clock = pygame.time.Clock()

    player = Player()
    fiende = Fiende()

    fiende_teller = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        player.move(pygame.key.get_pressed())
        player.draw(screen)
        if fiende_teller >= 60:
            fiende_gruppe.add(Fiende())
            fiende_teller = 0



        pygame.display.flip()

        fiende_teller += 1
        clock.tick(60)

if __name__ == "__main__":
    main()