import pygame
import Interfaz
from pygame import Color
from sudoku import tablero_juego, resolver_sudoku, imprimir_tablero, tablero

pygame.init()

# Configuración de la pantalla
width, height = 540, 540
tamañoBloque = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

# Fuente y reloj
fuente = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Color de selección
seleccion = (255, 0, 0)


def main():
    celda_seleccionada = None
    valor = ""
    running = True
    inicio = True  # Indicador de la pantalla de inicio

    # Inicialización del tablero
    tablero()

    while running:
        if inicio:
            # Pantalla de inicio
            Interfaz.mostrar_pantalla_inicio(screen, fuente)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    inicio = False  # Comienza el juego al presionar Enter
        else:
            # Rellenar la pantalla con el color blanco
            screen.fill("white")

<<<<<<< HEAD
            # Dibujar la cuadrícula y los números del tablero
            Interfaz.dibujar_grid(screen, width, height, fuente, tamañoBloque, tablero_juego)

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    y, x = event.pos  # Las coordenadas se invierten
                    fila = x // tamañoBloque
                    col = y // tamañoBloque
                    celda_seleccionada = (fila, col)
                    valor = ""
                if event.type == pygame.KEYDOWN:
                    # Asegúrate de que el valor presionado es un número entre 1 y 9
                    if event.key in range(pygame.K_1, pygame.K_9 + 1):
                        valor = event.key - pygame.K_0
                        print(f"Tecla presionada: {valor}")
=======
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
>>>>>>> 74c5a5faa78a233ef19ad2b53f65476dbdf3ea9a

                    # Si presionas 'R', puedes mostrar un popup para reiniciar
                    if event.key == pygame.K_r:
                        Interfaz.mostrar_popup(screen, fuente)

<<<<<<< HEAD
            # Resaltar la celda seleccionada y modificarla si es necesario
            Interfaz.resaltar_celda(celda_seleccionada, screen, seleccion, tamañoBloque)
            Interfaz.modificar_celda(celda_seleccionada, valor, screen, fuente, tamañoBloque, tablero_juego)
=======
           

        Interfaz.resaltar_celda(celda_seleccionada,screen,seleccion,tamañoBloque)
        Interfaz.modificar_celda(celda_seleccionada,valor,screen,fuente,tamañoBloque)
>>>>>>> 74c5a5faa78a233ef19ad2b53f65476dbdf3ea9a

            # Actualizar la pantalla
            pygame.display.flip()

        # Limitar la velocidad del juego
        clock.tick(60)

    pygame.quit()

    # Resolver el Sudoku al final del juego
    resolver_sudoku(tablero_juego)
    imprimir_tablero(tablero_juego)


# Ejecutar el juego
if __name__ == "__main__":
    main()


