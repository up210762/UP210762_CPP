from tkinter import *
import tkinter as tk
import os
import math as ma
import time
import libAgrup as la

os.system("clear")

ventana = tk.Tk()
ventana.geometry("800x800")

"""
def intLong():
    longitud = entrada1.get()
    etiqueta1['text'] = longitud
"""

etiqueta1 = tk.Label(ventana)
etiqueta1.pack()

################################################################################################
#Funciones
################################################################################################
def intDatos():
    datos = entrada1.get()
    Datos.append(datos)
    etiqueta1["text"] = Datos


def EtiquetaDatos(Imprimir):
    etiqueta1['text'] = Imprimir

################################################################################################
#Botones
################################################################################################
Datos = [40, 37, 60, 10, 30, 45, 55, 27, \
    40, 70, 30, 50, 35, 40, 60, 80, 50, 60, \
    65, 50, 55, 40, 35, 48, 50]

longitud = len(Datos)

Min, Max = la.min_max_value(Datos)
EtiquetaDatos(Min)
EtiquetaDatos(Max)

Rango = la.rango(Min, Max)
EtiquetaDatos(Rango)

categorias, crudCat = la.Categorias(longitud)
EtiquetaDatos(categorias)
EtiquetaDatos(crudCat)

amplitud = la.Amplitud(Max, Min, crudCat)
EtiquetaDatos(amplitud)

LimInf, LimSup = la.limits(Datos, longitud)
EtiquetaDatos(LimInf)
EtiquetaDatos(LimSup)

MA = la.Media_Aritmetica(categorias, LimInf, LimSup)
EtiquetaDatos(MA)

absoluta = la.Absoluta(longitud, categorias, LimInf, LimSup, Acomodo=sorted(Datos))
EtiquetaDatos(absoluta)

absAcum = la.Absoluta_acumulada(absoluta)
EtiquetaDatos(absAcum)

rel = la.Relativa(absoluta, longitud, categorias)
EtiquetaDatos(rel)

relAcum = la.relativa_Acumulada(rel)
EtiquetaDatos(relAcum)

Potje = la.Porcentajes(rel)
EtiquetaDatos(Potje)

media = la.Media(categorias, MA, absoluta, longitud)
EtiquetaDatos(media)

varianza = la.Varianza(categorias, MA, absoluta, longitud, media)
EtiquetaDatos(varianza)

DE = la.Desviacion_Estandar(varianza)
EtiquetaDatos(DE)

MMTC = la.Media_MTC(absoluta, LimInf, absAcum, amplitud, longitud, categorias)
EtiquetaDatos(MMTC)

moda = la.Moda_MTC(absoluta, categorias, amplitud, LimInf, absAcum)
EtiquetaDatos(moda)

MedMTC = la.Mediana_MTC(absoluta, categorias, LimInf, absAcum, longitud, amplitud)
EtiquetaDatos(MedMTC)

CV = la.Coefficiente_variacion(DE, MA, absoluta, categorias)
EtiquetaDatos(CV)


"""
entrada1 = tk.Entry(ventana)
entrada1.pack()

boton1 = tk.Button(ventana, text="Introducir Dato", command=intDatos)
boton1.pack()

#entrada2 = tk.Entry(ventana)
#entrada2.pack()

boton2 = tk.Button(ventana, text="Calcular", command=lambda:EtiquetaDatos(Min, Max))
boton2.pack()
"""

ventana.mainloop()