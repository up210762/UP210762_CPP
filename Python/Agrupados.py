import cmath
import math as ma

# Medidas de tendencia central

longitud = int(input("¿Cuántos números introduces? "))
Sumatoria = 0
Datos = []
xmax = 0
Vmax = 0
xmin = 0
Vmin = 0
Val = 0
limInf = 0
Rango = 0

for i in range(longitud):
    Vmin = 0
    números = int(input("Introduce los números: "))
    Datos.append(números)

#Acomodo de datos
for i in Datos:
    Acomodo = sorted(Datos)

#Selección del número máximo
    Vmax = 0
    Vmax = Vmax + números
    if Vmax > xmax:
        xmax = 0
        xmax = xmax + Vmax

#Selección del número menor
xmin = Acomodo[0]

#Rango
Rango = xmax - xmin
#Regla de Sturges
Logaritmo = ma.log10(longitud)
Categorias = 1 + 3.322*Logaritmo

limInf = xmin


'''
Media = Sumatoria/longitud



if Categorias != int:


Categorias
Amplitud = longitud/Categorias


Varianza = 
'''