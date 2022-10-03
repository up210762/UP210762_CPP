import numpy as np
import math as ma
import fnmatch
import matplotlib

# Variables estáticas
longitud = int(input("¿Cuántos números introduces? "))
frecRe = []
Datos = []
limInf = []
limSup = []
ranCat = []
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
Vmax = 0
parentesis = 0
contador = 0
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

print(f"Constante sin redondear: {crudCat}\nConstante redondeada: {Categorias}")
print(f"La amplitud sin redondear es: {crudAmp}\nLa amplitud redondeada es: {Amplitud}")

#Obtener categorías
valor = len(limInf)
Val = len(Acomodo)
for i in range(valor):
    fi = 0
    xi = (limSup[i]+limInf[i])/2
    MC.append(xi)
    ranCat.append([limInf[i], limSup[i]])
print(f"Los límites inferiores son: {limInf}\nMarcas de clase: {MC}\nRango de categorías: {ranCat}\n")  

#Frecuencia absoluta
for i in range(valor):
    fi = 0
    Vmin = limInf[i]
    Vmax = limSup[i]
    print(f"Valor máximo de la categoría: {Vmax}\nValor mínimo de la categoría: {Vmin}")
    for j in range(Val):
        if Acomodo[j] < Vmax and Acomodo[j] >= Vmin:
            fi = fi + 1
    frecI.append(fi)
print(f"Las frecuencias absolutas son: {frecI}")

#Frecuencia absoluta acumulada
valor = len(frecI)
for i in range(valor):
    frecIa = frecIa + frecI[i]
    FreAc.append(frecIa)
print(f"Las frecuencias absolutas acumuladas son: {FreAc}")


#Frecuencia relativa
for i in range(valor):
    Val = round(frecI[i]/longitud, 2)
    frecRe.append(Val)
#Frecuemcia relativa acumulada
    frecReA = frecReA + Val
print(f"Frecuencia relativa: {frecRe}\nFrecuencia relativa acumulada: {frecReA}")

#Porcentaje
for i in range(valor):
    Val = round(frecRe[i]*100, 0)
    hi.append(Val)
    print(f"Porcentajes: {Val}%")

#Varianza
for i in range(valor):
    Val = Val + (MC[i]*frecI[i])
    print(f"Sumatoria para el valor de la varianza: {Val}")
#Media
    #media = media + Val,2
x = Val/longitud
print(f"Valor para la varianza: {x}")
for i in range(valor):
    VzaAc = VzaAc + ((MC[i]-x)*(MC[i]-x))*frecI[i]
print(f"Sumatoria para la varianza {VzaAc}")
    
Vza = round(VzaAc/(longitud-1), 4)
print(f"La varianza es: {Vza}")

#Desviación estándar
Sd = round((np.sqrt(Vza)), 4)
print(f"La desviación estándar es: {Sd}")

#Mediana
#Límite inferior
linMax = 0
contador = len(frecI)
print(contador)

for i in frecI:
    while i > 0 and i <= contador:
        if linMax < limInf[i]:
            linMax = limInf[i]
            Vmin = FreAc[i-1]
            Vmax = limInf[i+1]
            xmax = frecI[i]
    if linMax == limInf[0]:
        if linMax < limInf[i]:
            linMax = limInf[i]
            Vmin = 0
            Vmax = limInf[i+1]
            xmax = frecI[i]
print(f"Limite inferior: {linMax}\n{Vmin}\n{Vmax}\nDivisor: {xmax}")
#Fórmula    
parentesis = (((longitud/2)-Vmin)/xmax)
Med = linMax + (Amplitud*parentesis)
print(f"Media: {Med}")
'''
#Moda
Val = ((xmax-Vmin)/((xmax-Vmin)+(xmax-Vmax)))
Mod = linMax + Amplitud*Val

#Coeficiente de variación
cV = 0
cV = (Sd/x)*100


#Cuartiles
k = 0
count = int(input("Escribe el número de cuartiles: "))
for i in range(count):
    k = k + 1
    const = ((k*longitud)/4)
    linMax = linMax + Amplitud
    print(f"Límite inferior: {linMax}")
    div = ((const-valor)/xmax)
    mult = Amplitud * div
    Val = linMax + mult
    cuartil.append(Val)
print(cuartil)

"""
#Impresión de gráficas
print("1) histograma\n2) caja y bigote\n3) de puntos")
enter = input()
while enter < 4 and enter > 0:
    if enter == "1":
        for i in Acomodo:
            if i in mapa_cantidades:
                mapa_cantidades[i] += 1
            else:
                mapa_cantidades[i] = 1
        for j in sorted(mapa_cantidades):
            print(f'{j}: {mapa_cantidades[j]}')



#Impresiones de pantalla
for i in range(valor):
    print(f"{hi[i]}%\n")
print(f"Marca de clase: {MC}\n")
print(f"Frecuecia absoluta: {frecI}\n")
print(f"Frecuencia absoluta acumulada: {frecIa}\n")
print(f"Frecuencia relativa: {frecRe}\n")
print(f"Frecuencia relativa acumulada: {frecReA}\n")
print(f"Ampitud: {Amplitud}\n")
print(f"Categoría: {ranCat}\n")
print(f"Valores: {Acomodo}\n")
print(f"Varianza: {Vza}\n")
print(f"Desviación estándar: {Sd}\n")
print(f"Media: {x}\n")
print(f"Mediana: {Med}\n")
print(f"Moda: {Mod}\n")
print(f"Coeficiente de variación: {cV}")
print(f"Cuartiles: {cuartil}")
"""
'''