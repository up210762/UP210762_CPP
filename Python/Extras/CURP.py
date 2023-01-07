nombres = input("Nombres: ")
apellidos = input("Apellidos: ")
nacimiento = input("Nacimiento: ")

curp = str()
curp = curp + apellidos[0:1]
curp = curp + nombres[0]
curp = curp + nacimiento
print(curp)