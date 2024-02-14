import pygame as pg
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
import random
import math

class Rect(pg.sprite.Sprite):
    '''Superclass of a 30*30 square with collision'''
    def __init__(self, x=0, y=0, color=(pg.Color("Red")), group=[]):
        super().__init__(group)
        self.rect=pg.Rect(x, y, 30, 30)
        self.image=pg.Surface([30, 30])
        self.image.fill(color)
        self.color=color
    
    def update(self, *args, **kwargs):
        self.image.fill(self.color)
        return super().update(*args, **kwargs)

class Player(Rect):
    '''Player'''
    def __init__(self, group):
        super().__init__(375, 250, pg.Color("Green"), group)
        self.dir=(0,1)
        self.speed=2.5
        self.group=group
        self.score=0
        self.safeObstacles=[]
        self._x=375.0
        self._y=250.0

    def update(self, *args, **kwargs):
        '''Update player, should be called every tick'''
        # Move Player
        self.x+=self.dir[0]*self.speed
        self.y+=self.dir[1]*self.speed

        # Make list of collisons
        collisions=pg.sprite.spritecollide(self, self.group, False)

        # Check if we have left safe obstacle created from eating food
        for obstacle in self.safeObstacles:
            if obstacle not in collisions:
                self.safeObstacles.remove(obstacle)

        # Detect collisions
        for colliding_sprite in collisions:
            if type(colliding_sprite) == Player:
                # Always collides with itself
                pass
            elif type(colliding_sprite) == Food:
                self.score += 1
                self.speed *= 1.05
                self.safeObstacles.append(colliding_sprite.turnToObstacle()) # Obstacle is safe until we stop colliding
                Food(self.group)
            elif type(colliding_sprite) == Obstacle and colliding_sprite not in self.safeObstacles:
                self.loss()

        # Detect if outside of map
        if (self.x < 0 
         or self.y < 0 
         or self.x > 750-30 
         or self.y > 500-30):
            self.loss()

        return super().update(*args, **kwargs)

    def loss(self):
        '''Lose the game'''
        self.speed=0
        self.color=pg.Color("Red")

    def up(self):
        self.dir=(0,-1)

    def down(self):
        self.dir=(0,1)

    def left(self):
        self.dir=(-1,0)

    def right(self):
        self.dir=(1,0)

    # x and y need to be floats but we need integer pixel values to draw,
    # so we use getters and setters for x and y pos
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x=value
        self.rect.left=math.floor(value)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y=value
        self.rect.top=math.floor(value)
    

class Food(Rect):
    def __init__(self, group):
        self.group=group
        while True:
            # Create sprite at random pos untill it doesn't collide
            self.x=random.randint(0, 750-30)
            self.y=random.randint(0, 500-30)
            super().__init__(self.x, self.y, pg.Color("Yellow"))
            if not pg.sprite.spritecollideany(self, group):
                self.add(group)
                break

    def turnToObstacle(self):
        '''Kill self and create obstacle at position'''
        self.kill()
        return Obstacle(self.x, self.y, self.group)

class Obstacle(Rect):
    def __init__(self, x, y, group):
        super().__init__(x, y, pg.Color("Gray"), group)

class UI():
    '''Game UI showing player score'''
    def __init__(self, player, surface):
        self.player=player
        self.surface=surface
        self.font=pg.font.SysFont("Roboto", 50)
        self.draw()

    def draw(self):
        text=self.font.render(str(self.player.score), True, pg.Color("White"))
        self.surface.blit(text, (375, 10))

# Initiate game objects
pg.init()
screen=pg.display.set_mode([750,500])
clock=pg.time.Clock()
group=pg.sprite.Group()
player=Player(group)
ui=UI(player, screen)
for i in range(3):
    Food(group)

# Game Loop
quitFlag=False
while not quitFlag:
    # Check if player quits
    for event in pg.event.get():
        if event.type==pg.QUIT:
            quitFlag=True

    clock.tick(60) # Set framerate

    # Detect inputt
    pressed_keys = pg.key.get_pressed()
    if pressed_keys[K_UP]:
        player.up()
    elif pressed_keys[K_DOWN]:
        player.down()
    elif pressed_keys[K_LEFT]:
        player.left()
    elif pressed_keys[K_RIGHT]:
        player.right()

    # Update sprites
    group.update()

    # Draw everything
    screen.fill(pg.Color("Black"))
    group.draw(screen)
    ui.draw()
    pg.display.flip()

pg.quit()