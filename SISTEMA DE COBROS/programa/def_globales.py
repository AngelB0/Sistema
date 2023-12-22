from tkinter import *
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox, PhotoImage
from tkinter import SOLID

ventana = tk.Tk()


#tamaño de la ventana
ventana.geometry("700x400")
#color de fondo BG
ventana.config(bg="#89BBFF")
#se le añade un titulo a la app
ventana.title("SISTEMA DE COBROS")

#LOGO

ventana.iconbitmap("img/LG.ico")




l1=Label(ventana, text="USER",font=("Candara", 20, "bold"), bg='#89BBFF').grid(row=2, column=1, pady=5,columnspan=4)
e1 = Entry(ventana, font=30, relief=SOLID)
e1.grid(row=3, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar

#CONTRASEÑA ENTRADA 

l2 = Label(ventana, text="PASSWORD", font=("Candara", 20, "bold"), bg='#89BBFF').grid(row=4, column=1, pady=5, columnspan=4)
e2 = Entry(ventana, font=30, show='*', relief=SOLID)
e2.grid(row=5, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar


# IMAGEN

img = PhotoImage(file='img/LOGO_TRANSPARENTE.png')
img1 = img.subsample(2, 2)
Label(ventana,image=img1, bg="#89BBFF").grid(row=1, column=1, pady=10, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar