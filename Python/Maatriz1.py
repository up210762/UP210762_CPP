'''
for i in range(4):
    for j in range(4):
        if i == j:
            print((i+1)*(j+1), end="")
        else:
            print(" ", end=" ")
    print("\n")
'''
matriz = []
def funcionMatriz(x, y):
    matriz = []
    diagonal = []
    suma = []
    contador = 0
    for i in range(x):
        sumador = 0
        for j in range(y):
            contador = contador + 1
            sumador = sumador + contador
            if i == j:
                diagonal.append(contador)
        suma.append(sumador)
    print(diagonal)
    print(suma)

    return matriz

"""
def printMatriz(x, y):
    matriz.
    for i in range(x):
        for j in range(y):
            print(matriz[i][j], end=" ")
    print("\n")

def diagonal(matriz, x, y):
    for i in range(x):
        for j in range(y):
            if i == j:
                print(matriz[i])
"""

filas = 4
columnas = filas
funcionMatriz(filas,columnas)
#diagonal(matriz, filas, columnas)
   