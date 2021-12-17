import pygame,sys
import random
pygame.init()

#Colours 
white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)
green = (  0,255,  0)
blue  = (  0,  0,255)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    #Close window loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white) #Window colour
    
    
    
    #-----------------------------------------#
    pygame.display.flip()
    clock.tick(80)