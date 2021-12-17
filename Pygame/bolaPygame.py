import pygame,sys
pygame.init()

#Definir colores
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

size = (600,300)

screen = pygame.display.set_mode(size) #ventana
clock = pygame.time.Clock()

#Coordenadas para movimiento

coord_x = 100
coord_y = 100

speed_x = 3
speed_y = 3

while True:
  #-------------Bucle cerrar ventana con libreria sys---------#
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      sys.exit()
  #-----------------------------------------------------------#
  #------------------LÓGICA-----------------------------------#
  if (coord_x > 550 or coord_x < 50):
    speed_x *= -1
  if (coord_y > 250 or coord_y < 50):
    speed_y *= -1

  coord_x += speed_x
  coord_y += speed_y
  #------------------LÓGICA-----------------------------------#
  #----------------Color de fondo
  screen.fill(BLACK) 
  #-------------------------ZONA DE DIBUJO-----------------------------#

  #pygame.draw.line(screen,GREEN,[100,100],[500,100],5)
  pygame.draw.circle(screen,WHITE,(coord_x,coord_y),radius=60,width=0)

  #pygame.draw.circle(screen,RED,(500,200),30,18)
  """for x in range(100,500,50):
    pygame.draw.line(screen,GREEN,(x+10,270),(x+10,130),5)
    pygame.draw.rect(screen,RED,(x,230,20,20))
    pygame.draw.rect(screen,BLUE,(x,190,20,20))
    pygame.draw.rect(screen,BLACK,(x,150,20,20))
    pygame.draw.circle(screen,RED,(x+35,200),10,3)"""
  #-------------------------ZONA DE DIBUJO-----------------------------#
  pygame.display.flip() #Actualizar pantalla
  clock.tick(90)