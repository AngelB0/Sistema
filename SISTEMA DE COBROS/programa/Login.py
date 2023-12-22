from tkinter import *
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox, PhotoImage
from tkinter import SOLID

import psycopg2
from Index import INDEX
from def_globales import *

def Evalue():
    user3 = e1.get()
    passw3 = e2.get()
    bd="sistema"
    try:
        conexion = psycopg2.connect(
                            user=user3,
                            password=passw3,
                            host='localhost',
                            port='5432',
                            database= bd
                        )
        messagebox.showinfo("INICIO DE SESION", "DATOS CORRECTOS")
        INDEX()
    except:
        messagebox.askretrycancel("ERROR", "Inicio de Sesion fallido, Intentelo de nuevo.")
    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    # Cerrar la conexión y el cursor
    cursor.close()
    conexion.close()

def toggle_visibility():
    if e2.cget("show") == "*":
        eye_button.config(image=open_eye)
        e2.config(show="")
    else:
        eye_button.config(image=close_eye)
        e2.config(show="*")


# Centrar la ventana en la pantalla
ventana.update_idletasks()
width = ventana.winfo_width()
height = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (width // 2)
y = (ventana.winfo_screenheight() // 2) - (height // 2)
ventana.geometry(f'{width}x{height}+{x}+{y}')


# Configurar columnas y filas para el sistema grid
for i in range(6):
    ventana.grid_columnconfigure(i, weight=1)
    ventana.grid_rowconfigure(i, weight=1)

# Asocia la tecla Enter a la función Evalue
e2.bind("<Return>", lambda event: Evalue())

# BOTON LOGIN
b1 = Button(ventana, text = "LOGIN",
    font=("Sitka", 12, "bold"), 
    command=Evalue, relief=RAISED, 
    state="normal",bg="#4169e1", 
    fg="white", cursor="hand2", 
    activebackground="white", 
    activeforeground="black")
b1.grid(row=6, column=1, pady=10, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar

# Ojo para mostrar/ocultar contraseña
eye_button = Button(ventana, command=toggle_visibility)
open_eye = PhotoImage(file='img/visible.png')  # Ajusta la ruta y el nombre de la imagen
close_eye = PhotoImage(file='img/ojo.png')  # Ajusta la ruta y el nombre de la imagen
eye_button.config(image=close_eye, bd=0, bg="#89BBFF")
eye_button.grid(row=5, column=2, padx=(135, 10),columnspan=2) # Ajusta las coordenadas según sea necesario
ventana.grid_columnconfigure(2, weight=1)  # Ajusta el peso de la columna para centrar

#moverse con las flechas para el label y boton 
def abajo(event):
    event.widget.tk_focusNext().focus()
    limite = event.widget.tk_focusNext()
    if isinstance(limite, tk.Entry):
        limite.focus()
    return "break"  # Evita que el evento se propague

def arriba(event):
    limite2 = event.widget.tk_focusPrev()
    if isinstance(limite2, tk.Entry):
        limite2.focus()
    return "break"
# Asocia el evento <Down> a la función para cada Entry
e1.bind("<Down>", abajo)
e1.bind("<Up>", arriba)
e2.bind("<Down>", abajo)
e2.bind("<Up>", arriba)
# Boton a label
b1.bind("<Up>", lambda event: e2.focus())

ventana.mainloop()