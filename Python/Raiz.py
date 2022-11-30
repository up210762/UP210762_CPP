'''
from cmath import sqrt
import numpy as np
import math


print(np.sqrt(4))
print(math.sqrt(4))
print(round(1.4,0))


i = 46
k = round(i, -1)
print(f"{i}, {k}")

e = i - 5

if e <= k:
    i = k + 10
else:
    i = k

print(f"{i}")

count = [1, 2, 3]
contenedor = []
for i in range(count):
    k = (count[i] * 10)/4
    contenedor.append(k)

controlador = 0

while controlador < 

from statistics import variance
datos_crudos = input('Dime los numeros: ')
lista_datos = [float(d) for d in datos_crudos.split()]
print(variance(lista_datos))

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)
'''
def contador(num, x):
    num += 1
    if num <= x:
        contador(num, x)
    else:
        print(num)

contador(4, 4)