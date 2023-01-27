import numpy as np, math as ma, os, time

##################################################################################################################################################################
#Función que permite al usuario ingresar los datos durante la ejecución del programa
def int_values(longitud):
    Datos = []
    print("introduce los valores:")
    for i in range(longitud):
        Vmin = 0
        numeros = int(input("> "))
        Datos.append(numeros)
    return Datos
##################################################################################################################################################################
#Sumatoria
##################################################################################################################################################################
#Definición del valor mínimo y máximo de la lista de valores ingresada
def min_max_value(Datos):
    Acomodo = sorted(Datos)
    xmin = Acomodo[0]
    xmax = Acomodo[-1]
    print(xmin, xmax)
    return xmin, xmax
##################################################################################################################################################################
#La diferencia entre el valor mínimo y el valor máximo de los valores ingresados
def rango(vmax, vmin):
    rango = vmax - vmin
    print(rango)
    return rango
##################################################################################################################################################################
#Función que retorna el valor de las categorias, las cuales son rangos numéricos que determinarán los límites inferiores en la fórmula de los cuartiles y 
#las frecuencias relativas
def Categorias(longitud):
    logaritmo = round(ma.log10(longitud), 2)
    crudCat = 1 + 3.322*logaritmo
    categorias = round(crudCat)
    print(categorias, crudCat)
    return categorias, crudCat
##################################################################################################################################################################
#La amplitud es la diferencia numérica entre el valor mínimo y máximo de las categorias
def Amplitud(xmax, xmin, crudCat):
    Rango = rango(xmax, xmin)
    crudAmp = Rango/crudCat
    amplitud = round(crudAmp)
    print(amplitud)
    return amplitud
##################################################################################################################################################################
#Función que validará los valores de los límites inferiores y los límites superiores de las categorias
def limits(Datos, longitud):
    limInf = []
    limSup = []
    xmin, xmax = min_max_value(Datos)
    categorias, crudCat = Categorias(longitud)
    amplitud = Amplitud(xmax, xmin, crudCat)
    for i in range(categorias):
        limInf.append(xmin)
        xmin = xmin + amplitud
        limSup.append(xmin)
    return limInf, limSup
##################################################################################################################################################################
#Obtener la media de aritmética de las categorias
def Media_Aritmetica(categorias, LimInf, LimSup):
    MC = []
    for i in range(categorias):
        xi = int((LimSup[i]+LimInf[i]) / 2)
        MC.append(xi)
    return MC
##################################################################################################################################################################
#Obtener la frecuencia absoluta
def Absoluta(longitud, categorias, LimInf, LimSup, Acomodo):
    frecI = []
    for i in range(categorias):
        contenedor = 0
        Vmin = LimInf[i]
        Vmax = LimSup[i]
        for j in range(longitud):
            if Acomodo[j] < Vmax and Acomodo[j] >= Vmin:
                contenedor = contenedor + 1
        frecI.append(contenedor)
    return frecI
##################################################################################################################################################################
#Frecuencia absoluta acumulada
def Absoluta_acumulada(absoluta):
    count = 0
    acumulada = []
    for i in absoluta:
        count = count + i
        acumulada.append(count)
    return acumulada
##################################################################################################################################################################
#Frecuencia relativa
def Relativa(frecI, longitud, categorias):
    FrecRe = []
    for i in range(categorias):
        val = round(frecI[i]/longitud, 2)
        FrecRe.append(val)
    return FrecRe
##################################################################################################################################################################
#Frecuencia relativa acumulada
def relativa_Acumulada(relativa):
    relAcum = []
    acumulada = 0.0
    for i in relativa:
        acumulada = acumulada + i
        relAcum.append(acumulada)
    return relAcum
##################################################################################################################################################################
#Porcentajes
def Porcentajes(relativa):
    hi = []
    count = 1
    for i in relativa:
        hi.append(int(round(i*100, 0)))
    print("Los porcentajes son: ")
    for i in hi:
        if count != len(relativa):
            print(f"|\t{i}%\t", end=' ')
            time.sleep(1)
        elif count == len(relativa):
            print(f"|\t{i}%\t|\n",end=' ')
            time.sleep(1)
        count = count + 1
    return hi
##################################################################################################################################################################
#Media
def Media(categorias, Media_arit, absoluta, longitud):
    val = 0
    for i in range(categorias):
        x = Media_arit[i] * absoluta[i]
        val = val + x
    media = val / longitud
    return media
##################################################################################################################################################################
#Varianza
def Varianza(categorias ,Media_arit, absoluta, longitud, media):
    vza = 0
    for i in range(categorias):
        vza =  vza + ((Media_arit[i] - media)**2)*absoluta[i]
    varianza = round(vza/(longitud - 1), 4)
    return varianza
##################################################################################################################################################################
#Desviación estándar
def Desviacion_Estandar(varianza):
    sd = round(varianza**.5, 4)
    return sd

##################################################################################################################################################################
#Media de MTC
def Media_MTC(absoluta, limInf, abs_Acum, amplitud, longitud, categorias):
    linMax = 0
    controlador = 0
    for i in range(len(absoluta)):
        if absoluta[i] > controlador:
            controlador = absoluta[i]
            linMax = limInf[i]
            if linMax == limInf[0]:
                Vmin = 0
                vmin = absoluta[i]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
            if linMax < limInf[i]:
                Vmin = abs_Acum[i-1]
                vmin = absoluta[i-1]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
    parentesis = (((longitud/2)-Vmin)/xmax)
    Med = linMax + amplitud*parentesis
    controlador = longitud / 2
    for i in range(categorias):
        if controlador <= abs_Acum[i] and controlador > abs_Acum[i-1]:
            vmin = abs_Acum[i-1]
            vmax = absoluta[i]
            linMax = limInf[i]
    Val = round(((controlador-vmin)/vmax), 3)
    Med = linMax + (amplitud*Val)
    return Med

##################################################################################################################################################################
#Moda
def Moda_MTC(absoluta, categorias, amplitud, limInf, abs_Acum):
    linMax = 0
    contador = categorias
    controlador = 0
    for i in range(contador):
        if absoluta[i] > controlador:
            controlador = absoluta[i]
            linMax = limInf[i]
            if linMax == limInf[0]:
                Vmin = 0
                vmin = absoluta[i]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
            if linMax < limInf[i]:
                Vmin = abs_Acum[i-1]
                vmin = absoluta[i-1]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
    controlador = 0
    for i in range(categorias):
        if absoluta[i] > controlador:
            controlador = absoluta[i]
    for i in range(categorias):
        if controlador != absoluta[0] and controlador == absoluta[i]:
            vmin = absoluta[i-1]
            vmax = absoluta[i+1]
        elif controlador == absoluta[0] and controlador == absoluta[i]:
            vmin = absoluta[i]
            vmax = absoluta[i+1]
    xmax = controlador
    Vmin = vmin
    Vmax = vmax
    Val = ((xmax-Vmin)/((xmax-Vmin)+(xmax-Vmax)))
    Mod = linMax + (amplitud*Val)
    return Mod

##################################################################################################################################################################
#Mediana
def Mediana_MTC(absoluta, categorias, limInf, abs_Acum, longitud, amplitud):
    linMax = 0
    controlador = 0
    for i in range(categorias):
        if absoluta[i] > controlador:
            controlador = absoluta[i]
            linMax = limInf[i]
            if linMax == limInf[0]:
                Vmin = 0
                vmin = absoluta[i]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
            if linMax < limInf[i]:
                Vmin = abs_Acum[i-1]
                vmin = absoluta[i-1]
                Vmax = absoluta[i+1]
                xmax = absoluta[i]
    controlador = longitud / 2
    for i in range(categorias):
        if controlador <= abs_Acum[i] and controlador > abs_Acum[i-1]:
            vmin = abs_Acum[i-1]
            vmax = absoluta[i]
            linMax = limInf[i]
    Val = round(((controlador-vmin)/vmax), 3)
    Med = linMax + (amplitud*Val)
    return Med
##################################################################################################################################################################
#Coefficiente de variación
def Coefficiente_variacion(Standar_desv, Media_arit, absoluta, categorias):
    for i in range(categorias):
        x = Media_arit[i] * absoluta[i]
    cV = 0
    cV = round((Standar_desv/(x))*100,2)
    return cV
##################################################################################################################################################################
#Cuartiles
def Cuartiles_Datos_Agrupados(rel_Acum, limInf, categorias, amplitud, longitud):
    controlador = 0
    contador = 0
    linMax = 0
    conCuart = []
    cuartil = []
    Cuartil = []
    Fi = []
    fi = []

    for i in range(3):
        contador = contador + 1
        controlador = ((contador*longitud)/4)
        conCuart.append(controlador)
    
    for i in range(3):
        for j in range(categorias):
            if conCuart[i] < abs_acumulada[j] and conCuart[i] >= abs_acumulada[j-1]:
                linMax = limInf[j]
        cuartil.append(linMax)
    
    for i in range(3):
        for j in range(categorias):
            if conCuart[i] <= abs_acumulada[0]:
                controlador = 0
                contador = absoluta[0]
            elif conCuart[i] > abs_acumulada[0] and conCuart[i] > abs_acumulada[j-1]:
                controlador = abs_acumulada[j-1]
                contador = absoluta[j]
            Fi.append(controlador)
            fi.append(contador)
    
    for i in range(3):
        contador = round(cuartil[i] + (amplitud*((conCuart[i]-Fi[i])/fi[i])), 3)
        Cuartil.append(contador)
    return Cuartil
##################################################################################################################################################################
"""
os.system('clear')
Datos = [40, 37, 60, 10, 30, 45, 55, 27, 40, 70, 30, 50, 35, 40, 60, 80, 50, 60, 65, 50, 55, 40, 35, 48, 50]
LimInf, LimSup = limits(Datos, 25)
longitud = 25
categorias, crudCat = Categorias(longitud)
MC = Media_Aritmetica(categorias, LimInf, LimSup)
absoluta = Absoluta(longitud, categorias, LimInf, LimSup, Acomodo=sorted(Datos))
print(absoluta)
xmin, xmax = min_max_value(Datos)
amplitud = Amplitud(xmax, xmin, crudCat)
abs_acumulada = Absoluta_acumulada(absoluta)
print(abs_acumulada)
relativa = Relativa(absoluta, longitud, categorias)
print(relativa)
rel_acumulada = relativa_Acumulada(relativa)
print (rel_acumulada)
porcentajes = Porcentajes(relativa)
media = Media(categorias, MC, absoluta, longitud)
varianza = Varianza(categorias, MC, absoluta, longitud, media)
print(varianza)
sd = Desviacion_Estandar(varianza)
print(sd)
Med = Media_MTC(absoluta, LimInf, abs_acumulada)
print(Med)
mod = Moda_MTC(absoluta, categorias, LimInf, abs_acumulada)
print(mod)
cv = Coefficiente_variacion(sd,MC)
print(cv)
cuartil = Cuartiles_Datos_Agrupados(rel_acumulada, LimInf, categorias, amplitud, longitud)
print(cuartil)
"""