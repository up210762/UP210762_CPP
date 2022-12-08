#Aquí irá el programa de cuartiles y agrupados en un sólo código
import numpy as np
import math as ma
from matplotlib import pylab, mlab, pyplot as plt
from collections import Counter

######## Funciones ########
#1) Diagrama de caja y bigote
def Boxplot(Cuartil):
    np.random.seed(10)
    data = np.random.normal(Cuartil)
    fig = plt.figure(figsize=(10, 7))
    plt.boxplot(data)
    plt.show()

#2) Gráfica de puntos
def GrafPoint(Valx, Valy):
    plt.plot(Valx,Valy, "o", color='b')
    plt.xlabel("X-axis")
    plt.xlabel("Y-axis")
    plt.title("Gráfica de puntos")
    plt.show()

#3) Gráfica lineal
def LinealGraf(Valx, Valy):
    plt.plot(Valx,Valy, color='b')
    plt.xlabel("X-axis")
    plt.xlabel("Y-axis")
    plt.title("Gráfica lineal")
    plt.show()

#4) Histograma
def Hist(Acomodo):
    intervalos = range(min(Acomodo), max(Acomodo) + 2)
    plt.hist(x=Acomodo, bins=intervalos, color='#F2AB6D', rwidth=0.85)
    plt.title('Histograma')
    plt.xlabel('label-X')
    plt.ylabel('label-Y')
    plt.xticks(intervalos)
    plt.show()

def sumatoria(r,x,y):
    r += x
    if r <= y:
        sumatoria(r,x,y)
    else:
        return r


# Variables estáticas

#longitud = int(input("¿Cuántos números introduces? "))
frecRe = []
Datos = [40, 37, 60, 10, 30, 45, 55, 27, \
    40, 70, 30, 50, 35, 40, 60, 80, 50, 60, \
    65, 50, 55, 40, 35, 48, 50]
limInf = []
limSup = []
ranCat = []
conCuart = []
frecI = []
FreAc = []
hi = []
MC = []
cuartil = []
Cuartil = []
const = []
Fi = []
fi = []
Valx = []
Valy = []
mapa_cantidades={}
VzaAc = 0
media = 0
frecIa = 0
xi = 0
xifi = 0
Rango = 0
frecReA = 0
count = 3

# Variables dinámicas
valor = 0
Val = 0
Vmin = 0
vmin = 0
Vmax = 0
vmax = 0
parentesis = 0
contador = 0
controlador = 0
xmax = 0
xmin = 0

"""
# Escritura de los valores
print("Introduce los valores: ")
for i in range(longitud):
    Vmin = 0
    números = int(input("> "))
"""
longitud = len(Datos)

print("Introduce los valores: ")
for i in range(longitud):
    Vmin = 0
    números = Datos[i]
    """numeros = int(input("> "))
    Datos.append(números)"""

#Selección del número máximo
    if números > xmax:
        xmax = números

#Acomodo de datos
Acomodo = sorted(Datos)

#Selección del número menor
xmin = Acomodo[0]

#Rango
Rango = xmax - xmin

#Regla de Sturges
Logaritmo = round(ma.log10(longitud), 2)
crudCat = 1 + 3.322*Logaritmo
Categorias = round(crudCat)
crudAmp = Rango/crudCat
Amplitud = round(crudAmp)
valor = Categorias-1

for i in range(Categorias):
    if i == 0:
        limInf.append(xmin)
        limSup.append(xmin+Amplitud)
    elif i != 0:
        limInf.append(limSup[i-1])
        limSup.append(limInf[i]+Amplitud)

if limSup[valor] <= xmax:
    Vmax = limSup[valor]
    limInf.append(Vmax)
    limSup.append(Vmax+Amplitud)

#Obtener categorías
valor = len(limInf)
Val = len(Acomodo)
for i in range(valor):
    xi = (limSup[i]+limInf[i])/2
    MC.append(xi)
    ranCat.append([limInf[i], limSup[i]])

#Frecuencia absoluta
for i in range(valor):
    contenedor = 0
    Vmin = limInf[i]
    Vmax = limSup[i]
    for j in range(Val):
        if Acomodo[j] < Vmax and Acomodo[j] >= Vmin:
            contenedor = contenedor + 1
    frecI.append(contenedor)

#Frecuencia absoluta acumulada
valor = len(frecI)
for i in range(valor):
    frecIa = frecIa + frecI[i]
    FreAc.append(frecIa)

#Frecuencia relativa
for i in range(valor):
    Val = round(frecI[i]/longitud, 2)
    frecRe.append(Val)
#Frecuemcia relativa acumulada
    frecReA = frecReA + Val

#Porcentaje
for i in range(valor):
    Val = round(frecRe[i]*100, 0)
    hi.append(Val)
print(f"Porcentajes: {Val}%")

#Varianza
for i in range(valor):
    x = (MC[i]*frecI[i])
    Val = sumatoria(Val, x, valor)


#Media
x = Val/longitud

for i in range(valor):
    VzaAc = VzaAc + ((MC[i]-x)*(MC[i]-x))*frecI[i]
Vza = round(VzaAc/(longitud-1), 4)

#Desviación estándar
Sd = round((np.sqrt(Vza)), 4)

#Límite inferior
linMax = 0
contador = len(frecI)

for i in range(contador):
    if frecI[i] > controlador:
        controlador = frecI[i]
        linMax = limInf[i]
        if linMax == limInf[0]:
            Vmin = 0
            vmin = frecI[i]
            Vmax = frecI[i+1]
            xmax = frecI[i]
        if linMax < limInf[i]:
            Vmin = FreAc[i-1]
            vmin = frecI[i-1]
            Vmax = frecI[i+1]
            xmax = frecI[i]

#Fórmula    
parentesis = (((longitud/2)-Vmin)/xmax)
Med = linMax + (Amplitud*parentesis)

#Moda
controlador = 0
for i in range(Categorias):
    if frecI[i] > controlador:
        controlador = frecI[i]
for i in range(Categorias):
    if controlador != frecI[0] and controlador == frecI[i]:
        vmin = frecI[i-1]
        vmax = frecI[i+1]
    elif controlador == frecI[0] and controlador == frecI[i]:
        vmin = frecI[i]
        vmax = frecI[i+1]
xmax = controlador
Vmin = vmin
Vmax = vmax
Val = ((xmax-Vmin)/((xmax-Vmin)+(xmax-Vmax)))
Mod = linMax + (Amplitud*Val)

#Mediana
controlador = longitud / 2
for i in range(Categorias):
    if controlador <= FreAc[i] and controlador > FreAc[i-1]:
        vmin = FreAc[i-1]
        vmax = frecI[i]
        linMax = limInf[i]
Val = round(((controlador-vmin)/vmax), 3)
Med = linMax + (Amplitud*Val)

#Coeficiente de variación
cV = 0
cV = round((Sd/(x))*100,2)

#Límites inferiores para los cuartiles
controlador = 0
contador = 0
for i in range(count):
    contador = contador + 1
    controlador = ((contador*longitud)/4)
    conCuart.append(controlador)

for i in range(count):
    for j in range(Categorias):
        if conCuart[i] < FreAc[j] and conCuart[i] >= FreAc[j-1]:
            linMax = limInf[j]
    cuartil.append(linMax)

#Cuartiles

for i in range(count):
    for j in range(Categorias):
        if conCuart[i] <= FreAc[0]:
            controlador = 0
            contador = frecI[0]
        elif conCuart[i] > FreAc[0] and conCuart[i] > FreAc[j-1]:
            controlador = FreAc[j-1]
            contador = frecI[j]
    Fi.append(controlador)
    fi.append(contador)

for i in range(count):
    contador = round(cuartil[i]+(Amplitud*((conCuart[i]-Fi[i])/fi[i])), 3)
    Cuartil.append(contador)
print(Cuartil)

#Impresiones de pantalla
for i in range(valor):
    print(f"{hi[i]}%\n")
print(f"Marca de clase: {MC}\n")
print(f"Frecuecia absoluta: {frecI}\n")
print(f"Frecuencia absoluta acumulada: {frecIa}\n")
print(f"Frecuencia relativa: {frecRe}\n")
print(f"Frecuencia relativa acumulada: {frecReA}\n")
print(f"Valores: {Acomodo}\n")
print(f"Varianza: {Vza}\n")
print(f"Desviación estándar: {Sd}\n")
print(f"Media: {x}\n")
print(f"Mediana: {Med}\n")
print(f"Moda: {Mod}\n")
print(f"Coeficiente de variación: {cV}%\n")
print(f"Los valores de los cuartiles son: {Cuartil}")

##### Gráficas #####

Boxplot(Cuartil)
#GrafPoint()
#LinealGraf()
Hist(Acomodo)
