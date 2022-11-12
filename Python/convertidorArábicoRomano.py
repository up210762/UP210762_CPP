#Programa de conversión de números árabes a romanos
"""
romano = str()
for i in range(1, 9):
    if i < 4:
        romano = "I" + romano
        print(romano)
    elif i == 4:
        romano = str()
        romano = "IV" + romano
        print(romano)
    elif i == 5:
        romano = str()
        romano = "V"
        print(romano)
    elif i > 5 and i < 9:
        romano = romano + "I"
        print(romano)
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Romanos = [I,V,X,L,C,D,M]
valor = 20
Resultado = str()
for i in range(len(Romanos)):
    if valor < Romanos[i] and valor > Romanos[i-1]:
        controlador = Romanos[i-1]
        if controlador == I:
            Resultado = Resultado