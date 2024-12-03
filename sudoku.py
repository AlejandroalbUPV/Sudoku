import random

# Tablero resuelto de Sudoku
tablero_resuelto = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Tablero del juego con espacios vacíos
tablero_juego = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Función principal para resolver el Sudoku
def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True  # No hay más espacios vacíos, puzzle resuelto
    else:
        fila, columna = vacio

    # Intentar números del 1 al 9 en la posición vacía
    for i in range(1, 10):
        if es_valido(tablero, i, (fila, columna)):
            tablero[fila][columna] = i  # Colocar el número

            if resolver_sudoku(tablero):  # Recursivamente resolver
                return True

            tablero[fila][columna] = 0  # Deshacer si no es solución

    return False  # No hay solución

# Función para verificar si un número es válido en una posición dada
def es_valido(tablero, num, pos):
    fila, columna = pos

    # Verificar fila
    for i in range(len(tablero[0])):
        if tablero[fila][i] == num and columna != i:
            return False

    # Verificar columna
    for j in range(len(tablero)):
        if tablero[j][columna] == num and fila != j:
            return False

    # Verificar subcuadro 3x3
    cuadro_x = fila // 3
    cuadro_y = columna // 3
    for i in range(cuadro_x * 3, cuadro_x * 3 + 3):
        for j in range(cuadro_y * 3, cuadro_y * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False

    return True

# Función para imprimir el tablero de Sudoku
def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(tablero[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

# Función para encontrar la siguiente casilla vacía (0)
def encontrar_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return i, j  # Retorna fila y columna
    return None

# Función para crear un tablero aleatorio con al menos 17 pistas
def crear_tablero_aleatorio():
    elecciones = list(range(1, 10))
    contador = 0

    while contador <= 17:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        num = random.choice(elecciones)

        if tablero_juego[fila][columna] == 0 and es_valido(tablero_juego, num, (fila, columna)):
            tablero_juego[fila][columna] = num
            contador += 1

    return tablero_juego

# Función para resolver el tablero y devolverlo
def crear_tablero(tablero):
    if resolver_sudoku(tablero):
        return tablero
    else:
        print("No se pudo resolver el tablero.")
        return None

# Función para eliminar celdas del tablero para crear el rompecabezas
def eliminar_celdas(tablero):
    global valor_original
    celdas_a_borrar = 64
    while celdas_a_borrar > 0:
        fila, columna = random.randint(0, 8), random.randint(0, 8)
        if tablero[fila][columna] != 0:

            valor_original = tablero[fila][columna]
            tablero[fila][columna] = 0

        if not tiene_unica_solucion(tablero):
            tablero[fila][columna] = valor_original
        else:
            celdas_a_borrar -= 1

# Función para verificar si el tablero tiene una única solución
def tiene_unica_solucion(tablero):
    contador = [0]
    resolver_con_contador(tablero, contador)
    return contador[0] == 1

# Función recursiva para resolver el tablero con contador de soluciones
def resolver_con_contador(tablero, contador):
    if contador[0] > 1:  # Detener si ya hay más de una solución
        return

    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, num, (fila, columna)):
                        tablero[fila][columna] = num
                        resolver_con_contador(tablero, contador)
                        tablero[fila][columna] = 0  # Backtracking
                return
    contador[0] += 1

# Función principal para generar el tablero
def tablero():
    crear_tablero_aleatorio()
    print("Tablero principal:")
    crear_tablero(tablero_juego)
    imprimir_tablero(tablero_juego)
    # Eliminar celdas para crear el rompecabezas
    eliminar_celdas(tablero_juego)
    print("Tablero generado: \n")
    imprimir_tablero(tablero_juego)

# Función para mostrar el tablero generado y resuelto
def tablero_solucionado():
    # Imprimir el resultado
    print("Tablero solucionado:")
    resolver_sudoku(tablero_juego)
    imprimir_tablero(tablero_juego)
