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

# Tablero vacío para juego
tablero_juego = [[0 for _ in range(9)] for _ in range(9)]

# Inicializa las restricciones globales
def inicializar_restricciones(tablero):
    global filas, columnas, subcuadros
    filas = [set() for _ in range(9)]
    columnas = [set() for _ in range(9)]
    subcuadros = [set() for _ in range(9)]

    for fila in range(9):
        for columna in range(9):
            num = tablero[fila][columna]
            if num != 0:
                subcuadro = (fila // 3) * 3 + (columna // 3)
                filas[fila].add(num)
                columnas[columna].add(num)
                subcuadros[subcuadro].add(num)

# Añade un número a las restricciones
def añadir_numero(num, fila, columna):
    subcuadro = (fila // 3) * 3 + (columna // 3)
    filas[fila].add(num)
    columnas[columna].add(num)
    subcuadros[subcuadro].add(num)

# Elimina un número de las restricciones
def eliminar_numero(num, fila, columna):
    subcuadro = (fila // 3) * 3 + (columna // 3)
    filas[fila].remove(num)
    columnas[columna].remove(num)
    subcuadros[subcuadro].remove(num)

# Comprueba si un número es válido en una posición dada
def es_valido(num, fila, columna):
    subcuadro = (fila // 3) * 3 + (columna // 3)
    if num in filas[fila] or num in columnas[columna] or num in subcuadros[subcuadro]:
        return False
    return True

# Encuentra una celda vacía
def encontrar_vacio(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return None

# Resuelve un Sudoku con backtracking
def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    fila, columna = vacio

    for num in range(1, 10):
        if es_valido(num, fila, columna):
            tablero[fila][columna] = num
            añadir_numero(num, fila, columna)

            if resolver_sudoku(tablero):
                return True

            tablero[fila][columna] = 0
            eliminar_numero(num, fila, columna)

    return False

# Cuenta las soluciones posibles
def resolver_con_contador(tablero, contador):
    if contador[0] > 1:
        return

    vacio = encontrar_vacio(tablero)
    if not vacio:
        contador[0] += 1
        return

    fila, columna = vacio
    for num in range(1, 10):
        if es_valido(num, fila, columna):
            tablero[fila][columna] = num
            añadir_numero(num, fila, columna)
            resolver_con_contador(tablero, contador)
            tablero[fila][columna] = 0
            eliminar_numero(num, fila, columna)


# Verifica si un Sudoku tiene una única solución
def tiene_unica_solucion(tablero):
    contador = [0]
    resolver_con_contador(tablero, contador)
    return contador[0] == 1

def eliminar_celdas(tablero):
    celdas_a_borrar = 55
    celdas_validas = [(fila, columna) for fila in range(9) for columna in range(9)]
    random.shuffle(celdas_validas)
    celdas_eliminadas = 0
    intentos_fallidos = 0
    max_intentos_fallidos = 10  # Número máximo de intentos fallidos antes de parar
    celdas_descartadas = []  # Lista para guardar celdas descartadas temporalmente
    celdas_restauradas = set()  # Usamos un conjunto para evitar restaurar celdas repetidas

    while celdas_a_borrar > 0 and celdas_validas:
        # Seleccionamos una celda aleatoria
        fila, columna = random.choice(celdas_validas)
        valor_original = tablero[fila][columna]

        if valor_original != 0:
            tablero[fila][columna] = 0
            eliminar_numero(valor_original, fila, columna)

            if tiene_unica_solucion(tablero):
                celdas_a_borrar -= 1
                celdas_eliminadas += 1
                print(f"Celda eliminada. Celdas restantes a eliminar: {celdas_a_borrar}")

                # Eliminar la celda de celdas_validas y agregarla a celdas_descartadas
                celdas_validas.remove((fila, columna))
                celdas_descartadas.append((fila, columna))  # Guardamos la celda descartada

                # Resetear los intentos fallidos
                intentos_fallidos = 0
            else:
                print(f"No se puede eliminar la celda ({fila}, {columna}). Se vuelve a agregar el valor.")
                tablero[fila][columna] = valor_original
                añadir_numero(valor_original, fila, columna)

                # Mover la celda a la lista de descartadas
                celdas_validas.remove((fila, columna))  # Eliminar de celdas_validas
                celdas_descartadas.append((fila, columna))  # Añadir a celdas_descartadas
                intentos_fallidos += 1  # Incrementar el contador de intentos fallidos

        # Si se han alcanzado demasiados intentos fallidos, rompemos el bucle
        if intentos_fallidos >= max_intentos_fallidos:
            print("Se han intentado todas las combinaciones posibles, no se pueden eliminar más celdas.")
            break

        # Si ya no hay más celdas válidas para eliminar, restauramos las celdas descartadas en orden inverso
        if not celdas_validas and celdas_descartadas:
            print("Restaurando celdas descartadas para intentar de nuevo...")

            while celdas_descartadas:
                celda_restaurada = celdas_descartadas.pop()  # Sacamos la última celda descartada
                fila, columna = celda_restaurada

                # Si esta celda ya fue restaurada antes, no la volvemos a restaurar
                if (fila, columna) in celdas_restauradas:
                    continue

                # Restauramos la celda en el tablero
                tablero[fila][columna] = valor_original
                añadir_numero(valor_original, fila, columna)

                # La agregamos a celdas_validas solo si no ha sido restaurada antes
                celdas_validas.append(celda_restaurada)

                # Marcamos la celda como restaurada para no intentar restaurarla nuevamente
                celdas_restauradas.add((fila, columna))

                # Reiniciamos los intentos fallidos
                intentos_fallidos = 0
                break  # Salimos del bucle de restauración para continuar con el siguiente intento

        # Si ya no quedan celdas para intentar, terminamos el proceso
        if not celdas_validas and not celdas_descartadas:
            print("Ya no hay más celdas para eliminar, se detiene el proceso.")
            break

    print(f"El número final de celdas eliminadas es: {celdas_eliminadas}")



# Imprime el tablero
def imprimir_tablero(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()


# Función para crear un tablero aleatorio con al menos 17 pistas
def crear_tablero_aleatorio(tablero):
    elecciones = list(range(1, 10))
    contador = 0

    while contador < 17:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        num = random.choice(elecciones)

        if tablero[fila][columna] == 0 and es_valido(num, fila, columna):
            tablero[fila][columna] = num
            añadir_numero(num, fila, columna)
            contador += 1

    return tablero

def verificar_consistencia(tablero):
    for fila in range(9):
        for columna in range(9):
            num = tablero[fila][columna]
            if num != 0:
                subcuadro = (fila // 3) * 3 + (columna // 3)
                if num not in filas[fila] or num not in columnas[columna] or num not in subcuadros[subcuadro]:
                    print(f"Inconsistencia detectada en ({fila}, {columna}): {num}")
                    return False
    return True


# Función principal para crear el tablero y resolverlo
def tablero():
    inicializar_restricciones(tablero_juego)
    crear_tablero_aleatorio(tablero_juego)
    print("Tablero generado aleatoriamente:")
    imprimir_tablero(tablero_juego)

    resolver_sudoku(tablero_juego)
    print("\nTablero resuelto:")
    imprimir_tablero(tablero_juego)

    eliminar_celdas(tablero_juego)
    print("\nTablero generado como puzzle:")
    imprimir_tablero(tablero_juego)
    verificar_consistencia(tablero_juego)
    print(filas)
    print(columnas)
    print(subcuadros)


