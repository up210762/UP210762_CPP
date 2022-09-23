w = 1
while w == 1:

    N = int(input("Escribe la edad de la persona: "))

    if N >= 1 and N <= 30:
        print("Persona de la primera edad.")

    elif N >= 31 and N <= 60:
        print("Persona de la segunda edad.")

    elif N >= 61 and N <= 90:
        print("Persona de la tercera edad.")

    elif N >= 91 and N <= 150:
        print('Persona con edad mayor al promedio.')

    else:
        print("La persona está muerta o no existió.")
        w = 2
