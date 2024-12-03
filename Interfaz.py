import pygame
import sudoku


def reiniciar_juego():
    pass

def mostrar_popup(screen, fuente):
    popup_rect = pygame.Rect(150, 200, 300, 200)
    pygame.draw.rect(screen, (200, 200, 200), popup_rect)
    pygame.draw.rect(screen, (0, 0, 0), popup_rect, 3)

    # Renderizar el texto
    texto = fuente.render("¿Reiniciar?", True, (0, 0, 0))
    texto_rect = texto.get_rect(center=popup_rect.center)

    # Dibujar el texto en el pop-up
    screen.blit(texto, texto_rect)
    pygame.display.flip()

def mostrar_pantalla_inicio(screen, fuente):
    screen.fill((255, 255, 255))
    texto = fuente.render("Pulsa Enter para Jugar", True, (0, 0, 0))
    screen.blit(texto, (50, 250))

def dibujar_grid(screen, width, height, fuente, tamañoBloque,tablero_juego):
    # Dibujar líneas horizontales y verticales para la cuadrícula
    for i in range(0, width, tamañoBloque):
        for j in range(0, height, tamañoBloque):
            rect = pygame.Rect(i, j, tamañoBloque, tamañoBloque)
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), rect, 1)
            if i % (3 * tamañoBloque) == 0 and i != 0:
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (i, 0), (i, height), 5)
            if j % (3 * tamañoBloque) == 0 and j != 0:
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, j), (width, j), 5)

    # Dibujar los números en el tablero
    for i in range(len(tablero_juego)):
        for j in range(len(tablero_juego[0])):
            texto = str(tablero_juego[i][j])
            if texto != "0":
                rect = pygame.Rect(j * tamañoBloque, i * tamañoBloque, tamañoBloque, tamañoBloque)
                rellenar_grid(texto, rect, fuente, screen)

def rellenar_grid(texto, rect, fuente, screen, color=(0, 0, 0)):
    text_surf = fuente.render(texto, True, color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def resaltar_celda(celda, screen, seleccion, tamañoBloque):
    if celda:
        x, y = celda
        rect = pygame.Rect(y * tamañoBloque, x * tamañoBloque, tamañoBloque, tamañoBloque)
        pygame.draw.rect(screen, seleccion, rect, 3)

def modificar_celda(celda, valor, screen, fuente, tamañoBloque,tablero_juego):
    if celda:
        x, y = celda
        tablero_juego[x][y] = valor
        texto = str(tablero_juego[x][y])
        rect = pygame.Rect(y * tamañoBloque, x * tamañoBloque, tamañoBloque, tamañoBloque)
        rellenar_grid(texto, rect, fuente, screen)






