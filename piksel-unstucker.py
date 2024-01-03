import pygame as p
import random as r
import time

farger=[]
for i in range(100):
    farger.append(p.Color(r.randint(0,255),r.randint(0,255),r.randint(0,255)))

p.init()
print(farger)

skjermInfo = p.display.Info()
vindu = p.display.set_mode((skjermInfo.current_w,skjermInfo.current_h))
# p.display.toggle_fullscreen()
# p.draw.rect(vindu,farger[r.randint(0,99)],p.Rect(20,20,30,30))
# time.sleep(3)
# p.draw.circle(vindu,(244,255,0),p.Rect(30,30,60,60))
while i<=20*60:
    vindu.fill(farger[r.randint(0,99)])
    p.draw.rect(vindu,farger[r.randint(0,99)],p.Rect(20,20,30,30))

    p.display.flip()
    i+=1
    time.sleep(float(1/60))
    



# for i in range(10):
#     print("FERDIG!!!!!")
# Importing the library
# import pygame
# import time
   
# # Initializing Pygame
# pygame.init()
   
# # Creating the surface
# sample_surface = pygame.display.set_mode((400,300))
   
# # Choosing red color for the rectangle
# color = (255,255,0)
   
# # Drawing Rectangle
# pygame.draw.rect(sample_surface, color, 
#                  pygame.Rect(30, 30, 60, 60))
 
# # The pygame.display.flip() method is used 
# to update content on the display screen
p.display.flip()
