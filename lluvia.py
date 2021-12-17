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

coord_list = []
for i in range(90): #raindrops quantity
        x = random.randint(0,800)
        y = random.randint(0,500)
        coord_list.append([x,y])

while True:
    #Close window loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(white) #Window colour
    #Points
    for coord in coord_list:
        pygame.draw.circle(screen,blue,coord,2)
        coord[1] += 1
        if coord[1] > 600:
            coord[1] = 0 
             
    pygame.display.flip()
    clock.tick(80)