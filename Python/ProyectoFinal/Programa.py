from tkinter import *
import tkinter as tk
import os

os.system("clear")

ventana = tk.Tk()
ventana.geometry("800x800")

def intLong():
    longitud = entrada1.get()
    etiqueta1['text'] = longitud

entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=0)
entrada1.pack()

etiqueta1 = tk.Label(ventana)
etiqueta1.pack() 

boton1 = tk.Button(ventana, text="Introducir", command=intLong)
boton1.pack()

"""
etiqueta = tk.Label(ventana, text="Hola Mundo")
etiqueta.pack(fill=tk.BOTH, expand=True)

CajaTexto = tk.Entry(ventana)
cajaTexto.pack()

def saludo(nombre):
    print("Hola " + nombre)

boton1 = tk.Button(ventana, text="Aceptar", padx=10, pady=5, command=lambda: saludo("Mundo"))
boton1.pack()
"""
ventana.mainloop()
