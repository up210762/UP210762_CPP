import random
contador = 4
contador2 = contador
matriz = []

"""
valor2 = random.randint(1, 30)

for i in range(contador):
    matriz.append([])
    for j in range(contador2):
        valor = random.randint(1, 30)
        matriz[i].append(valor)
"""

count = 0
filas = 0
columnas = 0
for i in range(contador):
    matriz.append([])
    for j in range(contador2):
        valor = random.randint(1, 30)
        for k in range(contador):
            if valor == matriz:
                valor = random.randint(1,30)
                matriz[i].append(valor)
            else:
                matriz[i].append(valor)
    columnas = columnas + 1
filas = filas + 1

for i in matriz:
    print("|\t", end=' ')
    for j in i:
        print("{}\t|".format(j), end=' ')
print()

"""
#Imprimir matriz
for  i in matriz:
    print("|\t", end=' ')
    for j in i:
        print("{}\t".format(j), end=' ')
    print("|")
    print()
"""