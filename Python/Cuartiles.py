#Cuartiles (Se toma a partir del intervalo que contiene las frecuencias absolutas)
k = 0
j = 0
controlador = 0
Vmin = 0
Vmax = 0
xmax = 0
frecI = []
limInf = []
FreAc = []
const = []
longitud = 0
conCuart = []
fi = []
Fi = []
cuartil = []
Val = 0
Amplitud = 0
contador = 0

count = int(input("Escribe el número de cuartiles: "))
longitud = int(input("¿Cuántos números son? "))
Categorias = int(input("¿Cuántas cateorias son? "))
print("Introduce las frecuencias obtenidas anteriormente:")
for i in range(Categorias):
    Val = int(input("> "))
    frecI.append(Val)
    contador = contador + Val
    FreAc.append(contador)

for i in range(count):
    Val = float(input("Escribe el límite inferior: "))
    limInf.append(Val)
    j = j + 1
    k = ((j*longitud)/4)
    const.append(k)
Amplitud = int(input("Introduce la amplitud: "))
for i in range(count):
    for i in range(Categorias):
        if frecI[i] > controlador:
            controlador = frecI[i]
            if frecI[i] > frecI[0]:
                Val = FreAc[i-1]
                contador = frecI[i]
            elif frecI[i] == frecI[0]:
                Val = 0
                contador = frecI[i]            
    fi.append(contador)
    Fi.append(Val)


for i in range(count):
    contador = (limInf[i]+(Amplitud*(const[i]-Fi[i])/fi[i]))
    cuartil.append(contador)
print(cuartil)
cout()