import cmath
import math as ma

# Variables estáticas
longitud = int(input("¿Cuántos números introduces? "))
frecRe = []
Datos = []
limInf = []
limSup = []
ranCat = []
frecI = []
hi = []
Acmxi = []
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

#Frecuencia relativa
for i in range(valor):
    Val = frecI[i]/longitud
    frecRe.append(Val)
#Frecuemcia relativa acumulada
    frecReA = frecReA + Val

#Porcentaje
for i in range(valor):
    Val = frecRe[i]*100
    hi.append(Val)

#Varianza
for i in range(valor):
    Val = Val + (Acmxi[i]*frecI[i])
x = Val/longitud
for i in range(valor):
    VzaAc = VzaAc + (((xi[i]-x)^2)*frecI)
Vza = VzaAc/(longitud-1)

#Desviación estándar
Sd = cmath.sqrt(Vza)

#Impresiones de pantalla
for i in range(valor):
    print(f"{hi[i]}%")
print(f"Frecuecia absoluta: {frecI}\nFrecuencia absoluta acumulada: {frecIa}")
print(f"Frecuencia relativa: {frecRe}\nFrecuencia relativa acumulada: {frecReA}")
print(f"Ampitud: {Amplitud}\nCategoría: {ranCat}\nValores: {Acomodo}")
print(f"Varianza: {Vza}\nDesviación estándar: {Sd}")
