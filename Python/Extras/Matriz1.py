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
def sumaDeMatriz(x, y):
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
    for i in diagonal:
        print("|\t{}\t".format(j),end = ' ')
        print()

    for i in suma:
        print("|\t{}\t|".format(j), end = ' ')
        print()

def llenarMatriz(x, y):
    valor = 0
    for i in range(x):
        matriz.append([])
        for j in range(y):
            valor = valor + 1
            matriz[i].append(valor)
    return matriz

def printMatriz(x):
    print("\tImpresión de la matriz")
    for i in x:
        print("|\t", end=' ')
        for j in i:
            print("{}\t".format(j), end=' ')
        print("|\n")
    print("\n\n\n")

def Traspose(matrix):
    if matrix == None or len(matrix) == 0:
        return []
    
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    print("\tImpresión de la traspuesta")
    for i in range(len(matrix[0])):
        print("|\t", end=' ')
        for j in range(len(matrix)):
            print(f"{result[i][j]}\t",end=' ')
        print("|")
        print("\n")
    print("\n\n\n")

def diagonal(x,y):
    print("\tImpredión de la diagonal")
    for i in range(x):
        print("|\t", end=' ')
        for j in range(y):
            if i == j:
                print(f"{matriz[i][j]}\t", end=' ')
            else:
                print("\t", end=' ')
        print("|\n")
    print("\n\n\n")

filas = 4
columnas = filas
llenarMatriz(filas,columnas)
printMatriz(matriz)
Traspose(matriz)
diagonal(filas,columnas)