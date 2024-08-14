import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
WHITE = (255, 255, 255)

# Función principal del juego
def main():
  # Se inicializa el juego
  pygame.init()
  pygame.display.set_caption("Mi juego")
  screen = pygame.display.set_mode((480,360))
  fondo = pygame.image.load('fondo_juego_1.png')
  personaje = pygame.image.load('personaje_sin_fondo_1.png')
  personaje_x = 240
  personaje_y = 180


  # Bucle principal
  while True:

    # 1.- Se dibuja la pantalla
    screen.fill(WHITE)
    screen.blit(fondo, (0, 0))
    screen.blit(personaje, (personaje_x, personaje_y))

    # 2.- Se comprueban los eventos
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit(0)

    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            personaje_x -= 10
        if event.key == K_RIGHT:
            personaje_x += 10
        if event.key == K_UP:
            personaje_y -= 10
        if event.key == K_DOWN:
            personaje_y += 10

    

    # 3.- Se actualiza la pantalla
    pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
  main()