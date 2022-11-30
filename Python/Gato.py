from tkinter import *
from tkinter import messagebox #para la caja de mensajes
from tkinter import simpledialog #para pedir nombre de jugadores

def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disable")

#Inicia el juego
def iniciarJuego():
    for i in range(0,9):
        listaBotones[i].config(state="normal")#Para desbloquear los botones para eso el estado normal
        listaBotones[i].config(bg="light grey")#A c/u de los botones se les da un color
        listaBotones[i].config(text="")#Vaciar c/u de los botones, Limpiar sin necesidad de abrir y cerrar el programa
        t[i] = "N"#Limpia el tablero interno

    global nombreJugador1,nombreJugador2 #indica a que variales globales quiere acceder
    nombreJugador1 = simpledialog.askstring("Jugador","Escribe el nombre del jugador 1: ")
    nombreJugador2 = simpledialog.askstring("Jugador", "Escribe el nombre del jugador 2: ")
    turnoJugador.set("Turno : "+nombreJugador1)

def comenzar(num):
    global turno, nombreJugador1, nombreJugador2
    if t[num] =="N" and turno==0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(bg="white")
        t[num] = "X"
        turno = 1
        turnoJugador.set("Turno: " + nombreJugador2)
    elif t[num] == "N" and turno==1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(bg="light blue")
        t[num] = "O"
        turno = 0
        turnoJugador.set("Turno: " + nombreJugador1)

    listaBotones[num].config(state="disable")
    verificar()

def verificar():
    if (t[0]=="X" and t[1]=="X" and t[2]=="X") or (t[3]=="X" and t[4]=="X" and t[5]=="X") or (t[6]=="X" and t[7]=="X" and t[8]=="X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador1)
    elif (t[0]=="X" and t[3]=="X" and t[6]=="X") or (t[1]=="X" and t[4]=="X" and t[7]=="X") or (t[2]=="X" and t[5]=="X" and t[8]=="X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador1)
    elif (t[0]=="X" and t[4]=="X" and t[8]=="X") or (t[2]=="X" and t[4]=="X" and t[6]=="X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador1)
    elif (t[0]=="O" and t[1]=="O" and t[2]=="O") or (t[3]=="O" and t[4]=="O" and t[5]=="O") or (t[6]=="O" and t[7]=="O" and t[8]=="O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador2)
    elif (t[0]=="O" and t[3]=="O" and t[6]=="O") or (t[1]=="O" and t[4]=="O" and t[7]=="O") or (t[2]=="O" and t[5]=="O" and t[8]=="O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador2)
    elif (t[0]=="O" and t[4]=="O" and t[8]=="O") or (t[2]=="O" and t[4]=="O" and t[6]=="O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste "+nombreJugador2)
    elif (t[0]== "O"):
        messagebox.showinfo("Empate")




ventana= Tk()
ventana.title("Juego del gato")
ventana.geometry("400x500")
turno=0
nombreJugador1=" "
nombreJugador2=" "

listaBotones=[] #lista para los objetos de 9 botones
t=[] #lista para escoger que pueda ser X, O (t=Tablero)
turnoJugador=StringVar()#Ver el turno entre jugador y otro asi como lo valla mostrando

#Llenar tablero de vacios con la letra "N"
for i in range(0,9):
    t.append("N")
#print(t) #para ver las N en vacio

#Hacer nuestros 9 botones
boton0=Button(ventana, width=9, height=3,command=lambda: comenzar(0))
boton0.place(x=50,y=50)
listaBotones.append(boton0)

boton1=Button(ventana, width=9, height=3,command=lambda: comenzar(1))
boton1.place(x=150,y=50)
listaBotones.append(boton1)

boton2=Button(ventana, width=9, height=3,command=lambda: comenzar(2))
boton2.place(x=250,y=50)
listaBotones.append(boton2)

boton3=Button(ventana, width=9, height=3,command=lambda: comenzar(3))
boton3.place(x=50,y=150)
listaBotones.append(boton3)

boton4=Button(ventana, width=9, height=3,command=lambda: comenzar(4))
boton4.place(x=150,y=150)
listaBotones.append(boton4)

boton5=Button(ventana, width=9, height=3,command=lambda: comenzar(5))
boton5.place(x=250,y=150)
listaBotones.append(boton5)

boton6=Button(ventana, width=9, height=3,command=lambda: comenzar(6))
boton6.place(x=50,y=250)
listaBotones.append(boton6)

boton7=Button(ventana, width=9, height=3,command=lambda: comenzar(7))
boton7.place(x=150,y=250)
listaBotones.append(boton7)

boton8=Button(ventana, width=9, height=3,command=lambda: comenzar(8))
boton8.place(x=250,y=250)
listaBotones.append(boton8)

#print(listaBotones) ver atraves de las variables por consola

turnoE=Label(ventana, textvariable=turnoJugador)
turnoE.place(x=120,y=20)

iniciar=Button(ventana, bg="#006", fg="white", text="Iniciar juego", width=15, height=3, command= iniciarJuego)
iniciar.place(x=130,y=350)

#bloquea el tablero del juego hasta que el jugador de a iniciar el juego, aqui manda a llamar a la funcion bloquear
bloquear()

ventana.mainloop()