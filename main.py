import pygame
import Interfaz
from pygame import Color

import sudoku

from sudoku import print_board, board_nueva

pygame.init()
width = 540  # ancho pantalla
height = 540  # alto pantalla

tamañoBloque = 60

pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((width, height))
fuente = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
seleccion = (255, 0, 0)

def main():
    celda_seleccionada = None
    valor = ""
    running = True
    sudoku.crear_board_aleatoria()
    while running:
        screen.fill("white")
        Interfaz.dibujar_grid(screen,width,height,fuente,tamañoBloque)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                y, x = event.pos #Vienen inveritos, col y filas
                fila = x // tamañoBloque
                print("X:")
                print(fila)
                print("Y:")
                col = y // tamañoBloque
                print(col)
                celda_seleccionada = (fila, col)
                valor = ""
            if event.type == pygame.KEYDOWN:
                valor = int(chr(event.key))
                print(f"Tecla presionada: {valor}")


           

        Interfaz.resaltar_celda(celda_seleccionada,screen,seleccion,tamañoBloque)
        Interfaz.modificar_celda(celda_seleccionada,valor,screen,fuente,tamañoBloque)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sudoku.solve(board_nueva)
    print_board(board_nueva)

main()