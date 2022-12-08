#Programa de funciones


def sumatoria(r):
    n = int()
    for i in range(n):
        r = i + 1
    print(f"El resultado de la sumatoria es: {r}")

def ecuacion(x):
    r = x**2 - 8 * x + 15
    print(f"El resultado de la sumatoria es: {r}")


n = int(input("Escribe un número: "))
sumatoria(n)

x = int(input("Escribe el valor de la incógnita: "))
ecuacion(x)
