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
Acmxi = []
mapa_cantidades={}
VzaAc = 0
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
sup = 0
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

#Obtener categorías
valor = len(limInf)
Val = len(Acomodo)
for i in range(valor):
    fi = 0
    xi = (limSup[i]+limInf[i])/2
    ranCat.append([limInf[i], limSup[i]])
    print(xi)
    Acmxi.append(xi)
    

#Frecuencia absoluta
for i in range(valor):
    fi = 0
    Vmin = limInf[i]
    Vmax = limSup[i]
    for j in range(Val):
        if Acomodo[j] < Vmax and Acomodo[j] >= Vmin:
            fi = fi + 1
    frecI.append(fi)

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
    Val = frecRe[i]*100
    hi.append(Val)

#Varianza
for i in range(valor):
    Val = Val + round((Acmxi[i]*frecI[i]), 4)
x = round(Val/longitud, 4)
for i in range(valor):
    VzaAc = VzaAc + round(((Acmxi[i]-x)*(Acmxi[i]-x))*frecI[i], 4)
    
Vza = round(VzaAc/(longitud-1), 4)

#Desviación estándar
Sd = round((np.sqrt(Vza)), 4)

#Límite inferior
linMax = 0
for i in range(valor):
    if linMax < frecI[i]:
        linMax = limInf[i]
        xmax = frecI[i]
        if (i - 1) < 0:
            valor = 0
            Vmin = 0
        else:
            valor = limInf[i-1]
            Vmin = frecI[i-1]
            Vmax = frecI[i+1]
    

#Media



#Mediana
Val = (((longitud/2)-valor)/sup)
Med = linMax + Amplitud*Val


#Moda
Val = ((xmax-Vmin)/((xmax-Vmin)+(xmax-Vmax)))
Mod = linMax + Amplitud*Val

#Cuartiles

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
    print(f"{hi[i]}%")
print(f"Frecuecia absoluta: {frecI}\nFrecuencia absoluta acumulada: {frecIa}")
print(f"Frecuencia relativa: {frecRe}\nFrecuencia relativa acumulada: {frecReA}")
print(f"Ampitud: {Amplitud}\nCategoría: {ranCat}\nValores: {Acomodo}")
print(f"Varianza: {Vza}\nDesviación estándar: {Sd}")
print(f"Limite inferior: {linMax}")