import tkinter as tk
from tkinter import ttk
import pandas as pd
from sqlalchemy import create_engine
from tkinter import messagebox #libreria para los mensajes de alerta
from tkinter import filedialog

from def_globales import ventana

def Insertar():
    def import_data_con(file_path):
        table_name='conceptos'
        try:
            # Leer el archivo CSV o Excel usando pandas
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Formato de archivo no compatible")

            # Establecer conexión a PostgreSQL (actualiza los parámetros según tu configuración)
            engine = create_engine('postgresql://user1:1234@localhost:5432/sistema')
            df.to_sql(table_name, engine, index=False, if_exists='replace')

            # Mostrar mensaje de éxito
            messagebox.showinfo("REGISTROS", "Se añadieron los registros correctamente")

        except Exception as e:
            # Mostrar mensaje de error si algo sale mal
            messagebox.askretrycancel("ERROR REGISTROS", "El archivo no se pudo insertar correctamente.")

    # Función para importar datos a PostgreSQL
    def import_data_to_postgres(file_path):
        table_name='alumnos'
        try:
            # Leer el archivo CSV o Excel usando pandas
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Formato de archivo no compatible")

            # Establecer conexión a PostgreSQL (actualiza los parámetros según tu configuración)
            engine = create_engine('postgresql://user1:1234@localhost:5432/sistema')
            df.to_sql(table_name, engine, index=False, if_exists='replace')

            # Mostrar mensaje de éxito
            messagebox.showinfo("REGISTROS", "Se añadieron los registros correctamente")
        except Exception as e:
            # Mostrar mensaje de error si algo sale mal
                messagebox.askretrycancel("ERROR REGISTROS", "El archivo no se pudo insertar correctamente.")
    # Función para seleccionar el archivo a importar
    def browse_file():
        file_path = filedialog.askopenfilename()
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

    # Crear una ventana secundaria.
    ventana_INSERTAR = tk.Toplevel()
    #color de fondo BG
    ventana_INSERTAR.config(bg="#89BBFF")
    #se le añade un titulo a la app
    ventana_INSERTAR.title("INSERTAR REGISTROS")
    ventana_INSERTAR.config(width=500, height=300)

    # Etiqueta y entrada para el archivo
    label1 = tk.Label(ventana_INSERTAR, text="Seleccione el archivo:")
    label1.place(x=180, y=50, width=150, height=40)
    file_path_entry = tk.Entry(ventana_INSERTAR, width=50)
    file_path_entry.place(x=150, y=100, width=200, height=20)
    browse_button = tk.Button(ventana_INSERTAR, text="Buscar", command=browse_file)
    browse_button.place(x=210, y=150, width=90, height=40)
    
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    btn_Alumnos_insert = ttk.Button(
        ventana_INSERTAR,
        text="Insertar Nuevo Alumnos", 
        command=lambda: import_data_to_postgres(file_path_entry.get())
    )
    btn_Conceptos_insert = ttk.Button(
        ventana_INSERTAR,
        text="Insertar Nuevo Conceptos", 
        command=lambda: import_data_con(file_path_entry.get())
    )
    btn_cerrar_insert = ttk.Button(
        ventana_INSERTAR,
        text="Cerrar ventana", 
        command=ventana_INSERTAR.destroy
    )

    btn_cerrar_insert.place(x=50, y=250, width=90, height=40)
    btn_Alumnos_insert.place(x=150, y=250, width=145, height=40)
    btn_Conceptos_insert.place(x=310, y=250, width=150, height=40)

    # Cierra la ventana principal
    ventana.withdraw()