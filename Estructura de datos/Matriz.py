matriz = []
valor = 0
x = 2
y = 4
for i in range(x):
    matriz.append([])
    for j in range(y):
        valor = valor + 10
        matriz[i].append(valor)

print("\tImpresión de la matriz")
for i in matriz:
    print("|\t", end=' ')
    for j in i:
        print("{}\t".format(j), end=' ')
    print("|\n")
print("\n\n\n")