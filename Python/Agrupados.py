import cmath
import math as ma
import tkinter as tk

# Medidas de tendencia central

longitud = int(input("¿Cuántos números introduces? "))
Sumatoria = 0
Datos = []
xmax = 0
Vmax = 0
xmin = 0
Vmin = 0
Val = 0
limInf = []
limSup = []
sup = 0
Rango = 0
ranCat = []

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

for i in range(Categorias):
    if i == 0:
        limInf.append(xmin)
        limSup.append(xmin+Amplitud)
        ranCat.append(f"{limInf},{limSup}")
    elif i != 0:
        limInf.append(limSup[i-1])
        limSup.append(limInf[i]+Amplitud)
    elif limSup[Categorias] <= xmax:
        limInf.append(limSup)
        limSup.append(limSup+Amplitud)
    
print(f"Ampitud: {Amplitud}\nLímite inferior: {limInf}\nLímite superior: {limSup}\nCategoría: {ranCat}")



'''
Media = Sumatoria/longitud



if Categorias != int:


Categorias
Amplitud = longitud/Categorias


Varianza = 
'''