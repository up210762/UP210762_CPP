"""
from Funciones import ecuacion, sumatoria

n = int(input("Escribe un número: "))
sumatoria()

x = int(input("Escribe el valor de la incógnita: "))
ecuacion()

def Mayor(x):
    for i in x:
        menor = x[0]
        if i < menor:
            menor = i
    print(menor)

Lista = [10,9,8,7,6]
Mayor(Lista)

#Obtener el cambio justo para cantidades de monedas
def Cambio(x):
    k = 0
    Monedas = []
    Monedas1=Monedas2=Monedas3=Monedas4=Monedas5=Monedas6=Monedas7=Monedas8=Monedas9=0
    Monedas = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
    for i in Monedas:
        if i > Monedas[k] and i < Monedas[k-1]:
                if i == 1:
                    Monedas1 = Monedas1 + 1
                elif i == 5:
                    Monedas2 = Monedas2 + 1
                elif i == 10:
                    Monedas3 = Monedas3 + 1
                elif i == 20:
                    Monedas4 = Monedas4 + 1
        k = k + 1
Monedas = []
Monedas = [Moneda1 = 1, Moneda2 = 5, Moneda3 = 10, Moneda4 = 20, Moneda5 = 50, Moneda6 = 100, Moneda7 = 200, Moneda8 = 500, Moneda9 = 1000]
"""
matriz = []
contador = 0
for i in range(2):
    for j in range(3):
        contador = contador + 1
        matriz.append(contador)
    print("\n")