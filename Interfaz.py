import pygame
import sudoku
from sudoku import board_nueva, board



def dibujar_grid(screen, width, height,fuente,tamañoBloque):
    for i in range(0, width, tamañoBloque):
        for j in range(0, height, tamañoBloque):
            rect = pygame.Rect(i, j, tamañoBloque, tamañoBloque)
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), rect, 1)
            if i % (3 * tamañoBloque) == 0 and i != 0:
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (i, 0), (i, height), 5)
            if j % (3 * tamañoBloque) == 0 and j!=0:
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, j), (width, j), 5)

    for i in range(len(board_nueva)):
        for j in range(len(board_nueva[0])):
            texto = str(board_nueva[i][j])
            if texto != "0":
                rect = pygame.Rect(j * tamañoBloque, i * tamañoBloque, tamañoBloque, tamañoBloque)
                rellenar_grid(texto, rect, fuente, screen)

def rellenar_grid(texto, rect, fuente,screen,color=(0,0,0)):
    text_surf = fuente.render(texto, True, color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def resaltar_celda(celda,screen,seleccion,tamañoBloque):
    if celda:
        x, y = celda
        rect = pygame.Rect(y * tamañoBloque, x * tamañoBloque, tamañoBloque, tamañoBloque)
        pygame.draw.rect(screen, seleccion, rect, 3)

def modificar_celda(celda,valor,screen,fuente,tamañoBloque):
    if celda:
        x , y = celda
        board_nueva[x][y] = valor
        texto = str(board_nueva[x][y])
        rect = pygame.Rect(y * tamañoBloque, x * tamañoBloque, tamañoBloque, tamañoBloque)
        rellenar_grid(texto,rect,fuente,screen)






