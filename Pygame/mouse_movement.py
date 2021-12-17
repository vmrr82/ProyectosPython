import pygame,sys
import random
pygame.init()
pygame.font.init()

#Colours 
white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)
green = (  0,255,  0)
blue  = (  0,  0,255)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


pygame.mouse.set_visible(False)# Mouse visibility
while True:
    #Close window loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_position = pygame.mouse.get_pos()
    x= mouse_position[0]
    y= mouse_position[1]
    text_font = pygame.font.SysFont('Ubuntu',15)
    textsurface = text_font.render(str(mouse_position), False, black)

    screen.fill(white) #Window colour
    screen.blit(textsurface,(350,0))
    #-----------------------------------------#
    pygame.draw.circle(screen,red,(x,y),radius=50)
    
    
    #-----------------------------------------#
    pygame.display.flip()
    clock.tick(80)