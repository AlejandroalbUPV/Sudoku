import random
import copy
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board_nueva = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,6,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False



def valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #check columnas
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    #Comprobar 3x3
    box_x = pos[0] // 3
    box_y =  pos[1] // 3

    for i in range(box_x * 3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(len(board)):
        if i % 3 ==0  and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end ="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]== 0:
                return i,j #fila y columna
    return None



def crear_board_aleatoria():
    eleciones = list(range(1,10))
    contador = 0
    while contador <= 17:

        fila = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.choice(eleciones)

        if board_nueva[fila][col] == 0 and valid(board_nueva, num, (fila, col)):
            board_nueva[fila][col] = num
            contador += 1


crear_board_aleatoria()
print_board(board_nueva)


# Crear una copia de board_nueva
board_a_resolver = copy.deepcopy(board_nueva)
solve(board_a_resolver)
print("_______________")
print_board(board_a_resolver)