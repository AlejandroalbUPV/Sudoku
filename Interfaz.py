import pygame

def dibujar_grid(screen, width, height):
    tamañoBloque = 60
    for i in range(0, width, tamañoBloque):
        for j in range(0, height, tamañoBloque):
            rect = pygame.Rect(i, j, tamañoBloque, tamañoBloque)
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), rect, 1)

