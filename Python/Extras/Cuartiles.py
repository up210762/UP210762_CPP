import matplotlib.pyplot as plt
import numpy as np

#Cuartiles (Se toma a partir del intervalo que contiene las frecuencias absolutas)
k = 0
j = 0
controlador = 0
Vmin = 0
Vmax = 0
xmax = 0
frecI = []
limInf = []
FreAc = []
const = []
longitud = 0
conCuart = []
fi = []
Fi = []
cuartil = []
Val = 0
Amplitud = 0
contador = 0

count = int(input("Escribe el número de cuartiles: "))
longitud = int(input("¿Cuántos números son? "))
Categorias = int(input("¿Cuántas cateorias son? "))
print("Introduce las frecuencias obtenidas anteriormente:")
for i in range(Categorias):
    Val = int(input("> "))
    frecI.append(Val)
    contador = contador + Val
    FreAc.append(contador)

for i in range(count):
    Val = float(input("Escribe el límite inferior: "))
    limInf.append(Val)
    j = j + 1
    k = ((j*longitud)/4)
    const.append(k)
Amplitud = int(input("Introduce la amplitud: "))
for i in range(count):
    for j in range(Categorias):
        if const[i] <= FreAc[0]:
            controlador = 0
            contador = frecI[0]
        elif const[i] > FreAc[0] and const[i] > FreAc[j-1]:
            controlador = FreAc[j-1]
            contador = frecI[j]
    Fi.append(controlador)
    fi.append(contador)

for i in range(count):
    contador = round(limInf[i]+(Amplitud*((const[i]-Fi[i])/fi[i])), 3)
    cuartil.append(contador)
print(cuartil)

#Gráficas
np.random.seed(10)
data = np.random.normal(cuartil)

fig = plt.figure(figsize=(10, 7))
plt.boxplot(data)
plt.show()