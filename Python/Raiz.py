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
'''
count = [1, 2, 3]
contenedor = []
for i in range(count):
    k = (count[i] * 10)/4
    contenedor.append(k)

controlador = 0

while controlador < 