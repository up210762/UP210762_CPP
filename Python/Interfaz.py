import tkinter
from tkinter import *

ventana = Tk()
ventana.title("Datos Agrupados")
ventana.geometry("800x800")

long = tkinter.Entry(ventana, font="Calibri 20")
long.grid(row=0, column=0,columnspan=4,padx=5,pady=5) 

boton1 = tkinter.Button(ventana,text="Enviar datos", command= lambda: entrada_valor)
boton1.grid(row=1, column=0)

l1 = tkinter.Label(ventana, text=long)
l1.grid(row=2, column=0)



def entrada_valor():
    longitud = long.get()
    return longitud

ventana.mainloop()
