import random

lista = [1,2,3,4,5,6,7,8,9]

for i in range(9):
    valor = random.choice(lista)
    lista.remove(valor)
    print(valor)

print(lista)