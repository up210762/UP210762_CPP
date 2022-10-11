import numpy as np
import math as ma
import fnmatch

# Variables estáticas
longitud = int(input("¿Cuántos números introduces? "))
frecRe = []
Datos = []
limInf = []
limSup = []
ranCat = []
conCuart = []
frecI = []
FreAc = []
hi = []
MC = []
cuartil = []
mapa_cantidades={}
VzaAc = 0
media = 0
frecIa = 0
xi = 0
xifi = 0
Rango = 0
frecReA = 0

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

# Escritura de los valores
print("Introduce los valores: ")
for i in range(longitud):
    Vmin = 0
    números = int(input("> "))
    Datos.append(números)

#Selección del número máximo
    if números > xmax:
        xmax = números

#Acomodo de datos
for i in Datos:
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

###print(f"Constante sin redondear: {crudCat}\nConstante redondeada: {Categorias}")###
###print(f"La amplitud sin redondear es: {crudAmp}\nLa amplitud redondeada es: {Amplitud}")###

#Obtener categorías
valor = len(limInf)
Val = len(Acomodo)
for i in range(valor):
    fi = 0
    xi = (limSup[i]+limInf[i])/2
    MC.append(xi)
    ranCat.append([limInf[i], limSup[i]])
###print(f"Los límites inferiores son: {limInf}\nMarcas de clase: {MC}\nRango de categorías: {ranCat}\n")###

#Frecuencia absoluta
for i in range(valor):
    fi = 0
    Vmin = limInf[i]
    Vmax = limSup[i]
    ###print(f"Valor máximo de la categoría: {Vmax}\nValor mínimo de la categoría: {Vmin}")###
    for j in range(Val):
        if Acomodo[j] < Vmax and Acomodo[j] >= Vmin:
            fi = fi + 1
    frecI.append(fi)
###print(f"Las frecuencias absolutas son: {frecI}")###

#Frecuencia absoluta acumulada
valor = len(frecI)
for i in range(valor):
    frecIa = frecIa + frecI[i]
    FreAc.append(frecIa)
###print(f"Las frecuencias absolutas acumuladas son: {FreAc}")###


#Frecuencia relativa
for i in range(valor):
    Val = round(frecI[i]/longitud, 2)
    frecRe.append(Val)
#Frecuemcia relativa acumulada
    frecReA = frecReA + Val
###print(f"Frecuencia relativa: {frecRe}\nFrecuencia relativa acumulada: {frecReA}")###

#Porcentaje
for i in range(valor):
    Val = round(frecRe[i]*100, 0)
    hi.append(Val)
print(f"Porcentajes: {Val}%")

#Varianza
for i in range(valor):
    Val = Val + (MC[i]*frecI[i])

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
print()

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
        vmin = frecI[i-1]
        vmax = frecI[i+1]
xmax = controlador
Vmin = vmin
Vmax = vmax
Val = ((xmax-Vmin)/((xmax-Vmin)+(xmax-Vmax)))
Mod = linMax + (Amplitud*Val)
###print(f"La moda es: {Mod}")###

#Mediana
controlador = longitud / 2
for i in range(Categorias):
    if controlador <= FreAc[i] and controlador > FreAc[i-1]:
        vmin = FreAc[i-1]
        vmax = frecI[i]
        linMax = limInf[i]
Val = ((controlador-vmin)/vmax)
Med = linMax + (Amplitud*Val)

#Coeficiente de variación
cV = 0
cV = round((Sd/(x))*100,2)
###print(f"El coeficiete de variación es: {cV}%")###

#Límites inferiores para los cuartiles
controlador = 0
contador = 0
xmax = 3
for i in range(xmax):
    contador = contador + 1
    controlador = ((contador*longitud)/4)
    conCuart.append(controlador)

for i in range(xmax):
    for j in range(Categorias):
        if conCuart[i] < FreAc[j] and conCuart[i] >= FreAc[j-1]:
            linMax = limInf[j]
    cuartil.append(linMax)

#Impresiones de pantalla
for i in range(valor):
    print(f"{hi[i]}%\n")
print(f"Marca de clase: {MC}\n")
print(f"Frecuecia absoluta: {frecI}\n")
print(f"Frecuencia absoluta acumulada: {frecIa}\n")
print(f"Frecuencia relativa: {frecRe}\n")
print(f"Frecuencia relativa acumulada: {frecReA}\n")
print(f"Categoría: {ranCat}\n")
print(f"Valores: {Acomodo}\n")
print(f"Varianza: {Vza}\n")
print(f"Desviación estándar: {Sd}\n")
print(f"Media: {x}\n")
print(f"Mediana: {Med}\n")
print(f"Moda: {Mod}\n")
print(f"Coeficiente de variación: {cV}%\n")
print("Para los cuartiles introduce los siguientes valores en el programa Cuartiles")
print("Cantidad de cuartiles: 3")
print(f"Cantidad de valores: {longitud}")
print(f"El total de categorías es: {Categorias}")
print(f"Las frecuencias absolutas son: {frecI}")
print(f"Los límites inferiores a introducir son {cuartil}")
print(f"La amplitud es: {Amplitud}")