import pygame
import Interfaz
from pygame import Color

import sudoku

from sudoku import print_board


pygame.init()
width = 540  # ancho pantalla
height = 540  # alto pantalla

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
def main():
    running = True

    while running:
        screen.fill("white")
        Interfaz.dibujar_grid(screen,width,height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


main()