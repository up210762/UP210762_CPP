import numpy as np
import math as ma

#El valor de x debe ser la cantidad total de datos introducidos
def int_values(longitud):
    Datos = []
    print("introduce los valores:")
    for i in range(longitud):
        Vmin = 0
        numeros = int(input("> "))
        Datos.append(numeros)
        max_value(numeros)
    return Datos

#Funciones de seleccion de los valores mínimo y máximo
def max_value(numeros, xmax=0):
    if numeros > xmax:
        xmax = numeros
        return xmax

def min_value(Datos):
    Acomodo = sorted(Datos)
    xmin = Acomodo[0]
    return xmin

def rango(vmax, vmin):
    rango = vmax - vmin
    return rango

def Categorias(longitud, xmax, xmin):
    Rango = rango(xmax, xmin)
    logaritmo = round(ma.log10(longitud), 2)
    crudCat = 1 + 3.322*logaritmo
    categorias = round(crudCat)
    return categorias

def Amplitud(Rango, crudCat):
    crudAmp = Rango/crudCat
    amplitud = round(crudAmp)
    return amplitud

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

