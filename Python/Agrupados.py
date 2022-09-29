import cmath
import math as ma

# Variables estáticas
longitud = int(input("¿Cuántos números introduces? "))
frecRe = 0
frecReA = 0
xmax = 0
xmin = 0
Datos = []
limInf = []
limSup = []
ranCat = []
frecI = []
frecIa = []
sup = 0
xi = 0
Rango = 0

# Variables dinámicas
valor = 0
Val = 0
Vmin = 0
Vmax = 0

# Escritura de los valores
for i in range(longitud):
    Vmin = 0
    números = int(input("Introduce los números: "))
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
Logaritmo = ma.log10(longitud)
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
    frecIa = frecIa + frecI(i)

#Frecuencia relativa
for i in range(valor):
    frecRe = frecI[i]/longitud

print(f"Frecuecia absoluta: {frecI}")
print(f"Ampitud: {Amplitud}\nLímite inferior: {limInf}\nLímite superior: {limSup}\nCategoría: {ranCat}\nValores: {Acomodo}")
