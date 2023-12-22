import tkinter as tk
from tkinter import ttk
import psycopg2
import sys
import pathlib



#VENTANA PARA CONSULTAR
def Consultar():
    ventana_consul=tk.Tk()
    #color de fondo BG
    ventana_consul.config(bg="#89BBFF")
    #se le añade un titulo a la app
    ventana_consul.title("CONSULTA DE REGISTROS")
    ventana_consul.geometry("1366x700")

    def Consu_Alum():
        # Mostrar información de archivos
        treeview_frame.mostrar_info_archivos()
        # Mostrar información de alumnos
        treeview_frame.mostrar_info_alumnos()


    def Consu_Concep():
        # Mostrar información de conceptos
        treeview_frame.mostrar_info_conceptos()


    class TreeviewFrame(ttk.Frame):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
            self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
            self.treeview = ttk.Treeview(
                self,
                xscrollcommand=self.hscrollbar.set,
                yscrollcommand=self.vscrollbar.set
            )

            self.hscrollbar.config(command=self.treeview.xview)
            self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            self.vscrollbar.config(command=self.treeview.yview)
            self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.treeview.pack()

            # Atributo para rastrear el estado del Treeview (minimizado o no)
            self.minimizado = False

        def mostrar_info_archivos(self):
            for file in pathlib.Path(sys.executable).parent.iterdir():
                self.treeview.insert(
                    "", tk.END, values=(file.name, file.stat().st_size))

        def mostrar_info_alumnos(self):
            def obtener_datosBD():
                conexion = psycopg2.connect(user='user1',
                                            password='1234',
                                            host='localhost',
                                            port='5432',
                                            database='sistema')
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM alumnos")
                datos = cursor.fetchall()
                cursor.close()
                conexion.close()
                return datos

            for fila in self.treeview.get_children():
                self.treeview.delete(fila)

            self.treeview.config(columns=("matricula", "alumno", "plantel", "oferta_edu", "grado", "grupo", "periodo", "turno", "fecha_ins", "estatus", "fecha_est"), show="headings")
            self.treeview.heading("matricula", text="Matricula")
            self.treeview.heading("alumno", text="Alumno")
            self.treeview.heading("plantel", text="Plantel")
            self.treeview.heading("oferta_edu", text="Oferta Educativa")
            self.treeview.heading("grado", text="Grado")
            self.treeview.heading("grupo", text="Grupo")
            self.treeview.heading("periodo", text="Periodo")
            self.treeview.heading("turno", text="Turno")
            self.treeview.heading("fecha_ins", text="Fecha de Inscripción")
            self.treeview.heading("estatus", text="Estatus")
            self.treeview.heading("fecha_est", text="Fecha de Estatus")

            datos = obtener_datosBD()
            for dato in datos:
                self.treeview.insert("", "end", values=dato)

        def mostrar_info_conceptos(self):
            def obtener_datos_conceptos():
                conexion = psycopg2.connect(
                    user='user1',
                    password='1234',
                    host='localhost',
                    port='5432',
                    database='sistema'
                )
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM conceptos")
                datos = cursor.fetchall()
                cursor.close()
                conexion.close()
                return datos

            for fila in self.treeview.get_children():
                self.treeview.delete(fila)

            self.treeview.config(columns=("codigo", "concepto", "cuenta_cont", "costo", "clasif"), show="headings")
            self.treeview.heading("codigo", text="Código")
            self.treeview.heading("concepto", text="Concepto")
            self.treeview.heading("cuenta_cont", text="Cuenta Contable")
            self.treeview.heading("costo", text="Costo")
            self.treeview.heading("clasif", text="Clasificación")

            datos = obtener_datos_conceptos()
            for dato in datos:
                self.treeview.insert("", "end", values=dato)

        def toggle_minimizar(self):
            # Cambiar el estado de minimizado y mostrar u ocultar el Treeview en consecuencia
            self.minimizado = not self.minimizado
            if self.minimizado:
                self.treeview.pack_forget()
            else:
                self.treeview.pack()

    
    # Crear una instancia de la clase TreeviewFrame
    treeview_frame = TreeviewFrame(ventana_consul)
    # Empaquetar el TreeviewFrame en la ventana principal
    treeview_frame.pack()

    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.            
    btn_Alumnos = ttk.Button(
        ventana_consul,
        text="Consultar Alumnos",
        command=Consu_Alum
    )
    btn_Conceptos = ttk.Button(
        ventana_consul,
        text="Consultar Conceptos", 
        command=Consu_Concep
    )
    boton_regresar = ttk.Button(ventana_consul,text="REGRESAR", command=lambda:close_window(ventana_consul))
    boton_regresar.place(x=50, y=600, width=90, height=40)
    btn_Alumnos.place(x=150, y=600, width=120, height=40)
    btn_Conceptos.place(x=280, y=600, width=125, height=40)

def close_window(window):
    # Cierra la ventana principal
    #WIND.withdraw()
    window.destroy()
    #WIND.deiconify()