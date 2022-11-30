import random

vector = []
count = 0

for i in range(9):
    lista = [1,2,3,4,5,6,7,8,9]
    vector.append([])
    for j in range(9):
        valor = random.choice(lista)
        vector[i].append(valor)
        lista.remove(valor)

for i in vector:
    print("|\t", end=' ')
    for j in i:
        print("{}\t".format(j), end=' ')
    print('|\n')