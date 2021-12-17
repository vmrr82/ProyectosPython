import pygame,sys

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

#----Coordenates-----#
coord_x = 10
coord_y = 10

#--speed---
x_speed = 0
y_speed = 0



while True:
    #Close window loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #----KEYBOARD----------------#
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = +3
            elif event.key == pygame.K_DOWN:
                y_speed = +3
            elif event.key == pygame.K_UP:
                y_speed = -3
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            
        
    screen.fill(white) #Window colour
    coord_x += x_speed
    coord_y += y_speed
    #-----------------------------------------#
    
    pygame.draw.rect(screen, red,(coord_x,coord_y,50,50))
    text_font = pygame.font.SysFont('Ubuntu',15)
    textsurface = text_font.render("x = " + str(coord_x) + " "  + "y = " + str(coord_y), False, black)
    screen.blit(textsurface,(350,0))
      
    #-----------------------------------------#
    pygame.display.flip()
    clock.tick(80)
pygame.quit()