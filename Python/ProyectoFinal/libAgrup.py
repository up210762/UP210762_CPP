import numpy as np
import math as ma

##################################################################################################################################################################
#Función que permite al usuario ingresar los datos durante la ejecución del programa
def int_values(longitud):
    Datos = []
    print("introduce los valores:")
    for i in range(longitud):
        Vmin = 0
        numeros = int(input("> "))
        Datos.append(numeros)
        max_value(numeros)
    return Datos
##################################################################################################################################################################
#Definición del valor máximo de la lista de valores ingresada
def max_value(numeros, xmax=0):
    if numeros > xmax:
        xmax = numeros
        return xmax
##################################################################################################################################################################
#Definición del valor mínimo de la lista de valores ingresada
def min_value(Datos):
    Acomodo = sorted(Datos)
    xmin = Acomodo[0]
    return xmin
##################################################################################################################################################################
#La diferencia entre el valor mínimo y el valor máximo de los valores ingresados
def rango(vmax, vmin):
    rango = vmax - vmin
    return rango
##################################################################################################################################################################
#Función que retorna el valor de las categorias, las cuales son rangos numéricos que determinarán los límites inferiores en la fórmula de los cuartiles y 
#las frecuencias relativas
def Categorias(longitud, xmax, xmin):
    Rango = rango(xmax, xmin)
    logaritmo = round(ma.log10(longitud), 2)
    crudCat = 1 + 3.322*logaritmo
    categorias = round(crudCat)
    return categorias
##################################################################################################################################################################
#La amplitud es la diferencia numérica entre el valor mínimo y máximo de las categorias
def Amplitud(Rango, crudCat):
    crudAmp = Rango/crudCat
    amplitud = round(crudAmp)
    return amplitud
##################################################################################################################################################################
#Función que validará los valores de los límites inferiores y los límites superiores de las categorias
def limits(numeros, Datos, longitud):
    limInf = []
    limSup = []
    xmin = min_value(numeros)
    xmax = max_value(Datos)
    categorias = Categorias(longitud, xmax, xmin)
    for i in range(categorias):
        limInf.append(xmin)
        limSup.append(xmax)
    return limInf, limSup

