from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import PhotoImage
from tkinter import filedialog
import pathlib
import sys
from tkinter import messagebox #libreria para los mensajes de alerta
import psycopg2 #importacion del modulo

#CLASE MAIN todo Va dentro de esta CLASS
def INDEX():
    #VENTANA ACTUALIZAR REGISTRO DE ALUMNO
    def act_Alum():
        def Save_Alum():
            MATRICULA = matri2.get()
            ALU = alumno.get()
            PLAN = plantel.get()
            OFED = ofedu.get()
            GRAD = grad.get()
            GRUPO = grad.get()
            PERIODO = perido.get()
            TURNO = turno.get()
            FINSCRIPCION = inscripcion.get()
            ESTATUS = estatus.get()
            FESTATUS = festatus.get()
            print("DATOS ACTUALIZADOS")

        # Crear una ventana secundaria.
        window_alu = tk.Toplevel()
        #color de fondo BG
        window_alu.config(bg="#89BBFF")
        #se le añade un titulo a la app
        window_alu.title("ACTUALIZAR REGISTRO ALUMNOS")
        window_alu.config(width=1080, height=600)

        #MATRICULA
        tk.Label(window_alu, text="MATRICULA", bg="white").place(x=50, y=70, width=80, height=20)
        matri2 = tk.Entry(window_alu, width=10)
        matri2.place(x=135, y=70, width=80, height=20)

        #ALUMNO
        tk.Label(window_alu, text="ALUMNO", bg="white").place(x=250, y=70, width=80, height=20)
        alumno = tk.Entry(window_alu, width=10)
        alumno.place(x=335, y=70, width=80, height=20)

        #OFERTA EDUCATIVA 
        tk.Label(window_alu, text="OFERTA EDUCATIVA", bg="white").place(x=440, y=70, width=120, height=20)
        ofedu = tk.Entry(window_alu, width=10)
        ofedu.place(x=565, y=70, width=200, height=20)

        #PLANTEL
        tk.Label(window_alu, text="PLANTEL", bg="white").place(x=790, y=70, width=75, height=20)
        plantel = tk.Entry(window_alu, width=10)
        plantel.place(x=870, y=70, width=120, height=20)

        #GRADO
        tk.Label(window_alu, text="GRADO", bg="white").place(x=50, y=110, width=40, height=20)
        grad = tk.Entry(window_alu, width=10)
        grad.place(x=100, y=110, width=40, height=20)

        #GRUPO
        tk.Label(window_alu, text="GRUPO", bg="white").place(x=150, y=110, width=40, height=20)
        grup = tk.Entry(window_alu, width=10)
        grup.place(x=200, y=110, width=40, height=20)

        #PERIODO
        tk.Label(window_alu, text="PERIODO", bg="white").place(x=250, y=110, width=50, height=20)
        perido = tk.Entry(window_alu, width=10)
        perido.place(x=310, y=110, width=80, height=20)

        #TURNO
        tk.Label(window_alu, text="TURNO", bg="white").place(x=400, y=110, width=50, height=20)
        turno = tk.Entry(window_alu, width=10)
        turno.place(x=460, y=110, width=80, height=20)

        #FECHA DE INSCRIPCION
        tk.Label(window_alu, text="FECHA DE INSCRIPCION", bg="white").place(x=50, y=150, width=133, height=20)
        inscripcion = tk.Entry(window_alu, width=10)
        inscripcion.place(x=190, y=150, width=100, height=20)

        #ESTATUS
        tk.Label(window_alu, text="ESTATUS", bg="white").place(x=300, y=150, width=80, height=20)
        estatus = tk.Entry(window_alu, width=10)
        estatus.place(x=385, y=150, width=80, height=20)

        #FECHA ESTATUS
        tk.Label(window_alu, text="FECHA ESTATUS", bg="white").place(x=480, y=150, width=90, height=20)
        festatus = tk.Entry(window_alu, width=10)
        festatus.place(x=575, y=150, width=80, height=20)

        #Boton cerrar
        boton_cerrar = ttk.Button(window_alu, text="Cerrar ventana", command=window_alu.destroy)
        boton_cerrar.place(x=50, y=200, width=90, height=40)

        #Boton guardar
        boton_guardar = ttk.Button(window_alu, text="GUARDAR", command= Save_Alum)
        boton_guardar.place(x=150, y=200, width=90, height=40)

        # Cierra la ventana principal
        ventana.withdraw()
        
    #VENTANA ACTUALIZAR REGISTRO CONCEPTO
    def act_Concep():
        def save_Concep():
            CODIGO = codigo.get()
            CONCEP = concepto.get()
            CONTABLE = contable.get()
            COSTO = costo.get()
            CLAS = clasificacion.get()
            print("DATOS ACTUALIZADOS CORRECTAMENTE")

        # Crear una ventana secundaria.
        window_con = tk.Toplevel()
        #color de fondo BG
        window_con.config(bg="#89BBFF")
        #se le añade un titulo a la app
        window_con.title("ACTUALIZAR REGISTRO CONCEPTOS")
        window_con.config(width=1080, height=600)

        #CODIGO
        tk.Label(window_con, text="CODIGO", bg="white").place(x=50, y=70, width=80, height=20)
        codigo = tk.Entry(window_con, width=10)
        codigo.place(x=135, y=70, width=80, height=20)

        #CONCEPTO
        tk.Label(window_con, text="CONCEPTO", bg="white").place(x=250, y=70, width=80, height=20)
        concepto = tk.Entry(window_con, width=10)
        concepto.place(x=335, y=70, width=80, height=20)

        #CUENTA CONTABLE 
        tk.Label(window_con, text="CUENTA CONTABLE", bg="white").place(x=440, y=70, width=120, height=20)
        contable = tk.Entry(window_con, width=10)
        contable.place(x=565, y=70, width=200, height=20)
        #COSTO
        tk.Label(window_con, text="COSTO", bg="white").place(x=790, y=70, width=75, height=20)
        costo = tk.Entry(window_con, width=10)
        costo.place(x=870, y=70, width=120, height=20)

        #CLASIFICACION
        tk.Label(window_con, text="CLASIFICACION", bg="white").place(x=50, y=110, width=100, height=20)
        clasificacion = tk.Entry(window_con, width=10)
        clasificacion.place(x=160, y=110, width=100, height=20)

        #Boton cerrar
        boton_cerrar = ttk.Button( window_con, text="Cerrar ventana", command=window_con.destroy)
        boton_cerrar.place(x=50, y=200, width=90, height=40)
        #Boton Guardar
        boton_guardar = ttk.Button(window_con, text="GUARDAR",command=save_Concep)
        boton_guardar.place(x=150, y=200, width=90, height=40)
        # Cierra la ventana principal
        ventana.withdraw()

    #VENTANA ACTUALIZAR
    def actualizar():
        # Crear una ventana secundaria.
        window_act = tk.Toplevel()
        #color de fondo BG
        window_act.config(bg="#89BBFF")
        #se le añade un titulo a la app
        window_act.title("ACTUALIZAR REGISTROS")
        window_act.config(width=500, height=300)
            
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        btn_Alumnos_insert = ttk.Button(
            window_act,
            text="Insertar Nuevo Alumnos", 
            command=act_Alum
        )
        btn_Conceptos_insert = ttk.Button(
            window_act,
            text="Insertar Nuevo Conceptos", 
            command=act_Concep
        )
        btn_cerrar_insert = ttk.Button(
            window_act,
            text="Cerrar ventana", 
            command=window_act.destroy
        )

        btn_cerrar_insert.place(x=50, y=100, width=90, height=40)
        btn_Alumnos_insert.place(x=150, y=100, width=145, height=40)
        btn_Conceptos_insert.place(x=310, y=100, width=150, height=40)

        # Cierra la ventana principal
        ventana.withdraw()
        
    #VENTANA SECUNDARIA REGISTRO ALUMNO
    def Inser_Alum():

        # Crear una ventana secundaria
        ventana_ins = tk.Toplevel()
        #Color de fondo BG
        ventana_ins.config(bg="#89BBFF")
        #Titulo App
        ventana_ins.title("INSERTAR DATOS")
        ventana_ins.config(width=1000, height=300)

        #Boton cerrar
        boton_cerrar = ttk.Button(ventana_ins, text="Cerrar ventana", command=ventana_ins.destroy)
        boton_cerrar.place(x=50, y=200, width=90, height=40)

        #Boton guardar
        boton_guardar = ttk.Button(ventana_ins, text="INSERTAR", command= "Guardar_Alum")
        boton_guardar.place(x=150, y=200, width=90, height=40)

        # Cierra la ventana principal
        ventana.withdraw()


    #VENTANA SECUNDARIA CONCEPTO
    def Inser_Concep():

        # Crear una ventana secundaria
        ventana_concep = tk.Toplevel()
        #Color de fondo BG
        ventana_concep.config(bg="#89BBFF")
        #Titulo App
        ventana_concep.title("INSERTAR NUEVO CONCEPTO")
        ventana_concep.config(width=1000, height=300)

        #Boton cerrar
        boton_cerrar = ttk.Button( ventana_concep, text="Cerrar ventana", command=ventana_concep.destroy)
        boton_cerrar.place(x=50, y=200, width=90, height=40)
        #Boton Guardar
        boton_guardar = ttk.Button(ventana_concep, text="INSERTAR",command="Guardar_Concep")
        boton_guardar.place(x=150, y=200, width=90, height=40)
        # Cierra la ventana principal
        ventana.withdraw()

    #VENTANA PARA CONSULTAR
    def Consultar():
        def Consu_Alum():
            class TreeviewFrame(ttk.Frame):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    
                    # Crear barras de desplazamiento horizontal y vertical
                    self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
                    self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
                    
                    # Crear un Treeview con barras de desplazamiento asociadas
                    self.treeview = ttk.Treeview(
                        self,
                        xscrollcommand=self.hscrollbar.set,
                        yscrollcommand=self.vscrollbar.set
                    )
                    
                    # Configurar las barras de desplazamiento para controlar el Treeview
                    self.hscrollbar.config(command=self.treeview.xview)
                    self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
                    self.vscrollbar.config(command=self.treeview.yview)
                    self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                    
                    # Empaquetar el Treeview
                    self.treeview.pack()

                def mostrar_info_archivos(self):
                    # Iterar sobre los archivos en el directorio del ejecutable de Python
                    for file in pathlib.Path(sys.executable).parent.iterdir():
                        # Insertar información sobre cada archivo en el Treeview
                        self.treeview.insert(
                            "", tk.END, values=(file.name, file.stat().st_size))

                def mostrar_info_alumnos(self):
                    def obtener_datosBD():
                        # conexión a la BD
                        conexion = psycopg2.connect(user='user1',
                                                    password='1234',
                                                    host='localhost',
                                                    port='5432',
                                                    database='sistema')

                        # Crear un cursor para ejecutar consultas SQL
                        cursor = conexion.cursor()

                        # Ejecutar una consulta para obtener datos (reemplaza con tu propia consulta)
                        cursor.execute("SELECT * FROM alumnos")
                        datos = cursor.fetchall()

                        # Cerrar la conexión y el cursor
                        cursor.close()
                        conexion.close()

                        return datos

                    # Limpiar las filas existentes en el Treeview
                    for fila in self.treeview.get_children():
                        self.treeview.delete(fila)

                    # Configurar el Treeview con columnas y encabezados
                    self.treeview.config(columns=("matricula", "alumno", "plantel", "oferta_edu", "grado", "grupo", "periodo", "turno", "fecha_ins", "estatus", "fecha_est"), show="headings")
                    self.treeview.heading("matricula", text="Matricula")
                    self.treeview.heading("alumno", text="Alumno")
                    self.treeview.heading("plantel", text="Plantel")
                    self.treeview.heading("oferta_edu", text="Oferta Educativa")
                    self.treeview.heading("grado", text="Grado")
                    self.treeview.heading("grupo", text="Grupo")
                    self.treeview.heading("periodo", text="Periodo")
                    self.treeview.heading("turno", text="Turno")
                    self.treeview.heading("fecha_ins", text="Fecha de Inscripcion")
                    self.treeview.heading("estatus", text="Estatus")
                    self.treeview.heading("fecha_est", text="Fecha del Estatus")
                    

                    # Obtener datos de la base de datos y mostrarlos en el Treeview
                    datos = obtener_datosBD()
                    for dato in datos:
                        self.treeview.insert("", "end", values=dato)    
            # Crear una instancia de la clase TreeviewFrame
            treeview_frame = TreeviewFrame(ventana_consul)

            # Empaquetar el TreeviewFrame en la ventana principal
            treeview_frame.pack()

            # Mostrar información de archivos
            treeview_frame.mostrar_info_archivos()

            # Mostrar información de alumnos
            treeview_frame.mostrar_info_alumnos()      

        def Consu_Concep():
            class TreeviewFrame(ttk.Frame):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    # Crear barras de desplazamiento horizontal y vertical
                    self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
                    self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)

                    # Crear un Treeview con barras de desplazamiento asociadas
                    self.treeview = ttk.Treeview(
                        self,
                        xscrollcommand=self.hscrollbar.set,
                        yscrollcommand=self.vscrollbar.set
                    )

                    # Configurar las barras de desplazamiento para controlar el Treeview
                    self.hscrollbar.config(command=self.treeview.xview)
                    self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
                    self.vscrollbar.config(command=self.treeview.yview)
                    self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                    # Empaquetar el Treeview
                    self.treeview.pack()

                def mostrar_info_conceptos(self):
                    def obtener_datos_conceptos():
                        # conexión a la BD
                        conexion = psycopg2.connect(
                            user='user1',
                            password='1234',
                            host='localhost',
                            port='5432',
                            database='sistema'
                        )

                        # Crear un cursor para ejecutar consultas SQL
                        cursor = conexion.cursor()

                        # Ejecutar una consulta para obtener datos de conceptos
                        cursor.execute("SELECT * FROM conceptos")
                        datos = cursor.fetchall()

                        # Cerrar la conexión y el cursor
                        cursor.close()
                        conexion.close()

                        return datos

                    # Limpiar las filas existentes en el Treeview para conceptos
                    for fila in self.treeview.get_children():
                        self.treeview.delete(fila)

                    # Configurar el Treeview con columnas y encabezados para conceptos
                    self.treeview.config(columns=("codigo", "concepto", "cuenta_cont", "costo", "clasif"), show="headings")
                    self.treeview.heading("codigo", text="Código")
                    self.treeview.heading("concepto", text="Concepto")
                    self.treeview.heading("cuenta_cont", text="Cuenta Contable")
                    self.treeview.heading("costo", text="Costo")
                    self.treeview.heading("clasif", text="Clasificación")

                    # Obtener datos de la base de datos y mostrarlos en el Treeview para conceptos
                    datos = obtener_datos_conceptos()
                    for dato in datos:
                        self.treeview.insert("", "end", values=dato)

            # Crear una instancia de la clase TreeviewFrame
            treeview_frame = TreeviewFrame(ventana_consul)

            # Empaquetar el TreeviewFrame en la ventana principal
            treeview_frame.pack()

            # Mostrar información de conceptos
            treeview_frame.mostrar_info_conceptos()

        ventana_consul=tk.Tk()
    
        #color de fondo BG
        ventana_consul.config(bg="#89BBFF")
        #se le añade un titulo a la app
        ventana_consul.title("CONSULTA DE REGISTROS")
        ventana_consul.geometry("1366x700")        

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
            WIND.withdraw()
            window.destroy()
            WIND.deiconify()

    def Insertar():
        # Crear una ventana secundaria.
        ventana_INSERTAR = tk.Toplevel()
        #color de fondo BG
        ventana_INSERTAR.config(bg="#89BBFF")
        #se le añade un titulo a la app
        ventana_INSERTAR.title("INSERTAR REGISTROS")
        ventana_INSERTAR.config(width=500, height=300)
            
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        btn_Alumnos_insert = ttk.Button(
            ventana_INSERTAR,
            text="Insertar Nuevo Alumnos", 
            command=Inser_Alum
        )
        btn_Conceptos_insert = ttk.Button(
            ventana_INSERTAR,
            text="Insertar Nuevo Conceptos", 
            command=Inser_Concep
        )
        btn_cerrar_insert = ttk.Button(
            ventana_INSERTAR,
            text="Cerrar ventana", 
            command=ventana_INSERTAR.destroy
        )

        btn_cerrar_insert.place(x=50, y=100, width=90, height=40)
        btn_Alumnos_insert.place(x=150, y=100, width=145, height=40)
        btn_Conceptos_insert.place(x=310, y=100, width=150, height=40)

        # Cierra la ventana principal
        ventana.withdraw()

    # Definir la función que se ejecutará cuando se haga clic en el botón
    def enviar_datos():
        #conexion a la BD
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
            messagebox.showinfo("CONEXION BD", "CONEXION ESTABLECIDA")
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
        except:
            messagebox.askretrycancel("ERROR", "CONEXION A LA BD FALLIDA.")
        
        FOL = folio.get()
        MATRI = mat.get()
        NOMA = nom.get()
        GRUP = gru.get()
        LIC = lice.get()
        FE = date1
        PLA = plan.get()
        USU = user1
        #Conceptos
        CON1 = conc1.get()
        CON2 = conc2.get()
        CON3 = conc3.get()
        CON4 = conc4.get()
        CON5 = conc5.get()
        CON6 = conc6.get()
        CON7 = conc7.get()
        CONCEPTOF=CON1+CON2+CON3+CON4+CON5+CON6+CON7
        #impotes datos
        IMP1 = impo1.get()
        IMP2 = impo2.get()
        IMP3 = impo3.get()
        IMP4 = impo4.get()
        IMP5 = impo5.get()
        IMP6 = impo6.get()
        IMP7 = impo7.get()
        #% datos
        POR1 = combo1.get()
        POR2 = combo2.get()
        POR3 = combo3.get()
        POR4 = combo4.get()
        POR5 = combo5.get()
        POR6 = combo6.get()
        POR7 = combo7.get()
        #Recargos
        RE1 = rec1.get()
        RE2 = rec2.get()
        RE3 = rec3.get()
        RE4 = rec4.get()
        RE5 = rec5.get()
        RE6 = rec6.get()
        RE7 = rec7.get()
        #Subtotal
        SUB1 = subt1.get()
        SUB2 = subt2.get()
        SUB3 = subt3.get()
        SUB4 = subt4.get()
        SUB5 = subt5.get()
        SUB6 = subt6.get()
        SUB7 = subt7.get()
        TOTAL=SUB1+SUB2+SUB3+SUB4+SUB5+SUB6+SUB7
        #Cantidad que recibe
        CANTR = cant_res.get()
        #Cambio
        CAMBIO = int(CANTR) - int(TOTAL)
        CAM =  cambio.get()
        #forma de pago
        FP = formP.get()
        #Aprovacion
        APRO = aprov.get()
        #cuenta reseptora
        CUR = cuenta_res.get()
        #Observaciones
        OBSERVA = observ.get()
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            # Ejecutar la consulta de inserción (adaptar según tu tabla)
            consulta = "INSERT INTO ventas (folio, plantel, matri, nombre, grupo, licenciatura, fecha, cant_recibe, forma_p, aprov, cuenta_rec, concep, observaciones, subtotal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # Imprimir la consulta y los valores antes de ejecutarla
            print("Consulta:", consulta)
            print("Valores:", (FOL, PLA, MATRI, NOMA, GRUP, LIC, FE, CANTR, FP, APRO, CUR,CONCEPTOF, OBSERVA, TOTAL ))
            cursor.execute(consulta, (FOL, PLA, MATRI,NOMA, GRUP, LIC, FE, CANTR, FP, APRO, CUR, CONCEPTOF, OBSERVA, TOTAL))

            # Confirmar la transacción
            conexion.commit()

            # Limpiar campos de entrada después de la inserción
            folio.delete(0, tk.END)
            plan.delete(0, tk.END)
            mat.delete(0, tk.END)
            nom.delete(0, tk.END)
            gru.delete(0, tk.END)
            lice.delete(0, tk.END)
            conc1.delete(0, tk.END)
            conc2.delete(0, tk.END)
            conc3.delete(0, tk.END)
            conc4.delete(0, tk.END)
            conc5.delete(0, tk.END)
            conc6.delete(0, tk.END)
            conc7.delete(0, tk.END)
            impo1.delete(0, tk.END)
            impo1.delete(0, tk.END)
            impo2.delete(0, tk.END)
            impo3.delete(0, tk.END)
            impo4.delete(0, tk.END)
            impo5.delete(0, tk.END)
            impo6.delete(0, tk.END)
            impo7.delete(0, tk.END)
            combo1.delete(0,tk.END)
            combo2.delete(0,tk.END)
            combo3.delete(0,tk.END)
            combo4.delete(0,tk.END)
            combo5.delete(0,tk.END)
            combo6.delete(0,tk.END)
            combo7.delete(0,tk.END)
            rec1.delete(0,tk.END)
            rec2.delete(0,tk.END)
            rec3.delete(0,tk.END)
            rec4.delete(0,tk.END)
            rec5.delete(0,tk.END)
            rec6.delete(0,tk.END)
            rec7.delete(0,tk.END)
            subt1.delete(0,tk.END)
            subt2.delete(0,tk.END)
            subt3.delete(0,tk.END)
            subt4.delete(0,tk.END)
            subt5.delete(0,tk.END)
            subt6.delete(0,tk.END)
            subt7.delete(0,tk.END)
            cant_res.delete(0,tk.END)
            cambio.delete(0,tk.END)
            formP.delete(0,tk.END)
            aprov.delete(0,tk.END)
            cuenta_res.delete(0,tk.END)
            observ.delete(0,tk.END)
            print("Datos ingresados correctamente.")
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante la inserción
            print(f"Error al ingresar datos: {e}")
            conexion.rollback()

        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()
        
    #VENTANA PRINCIPAL
    WIND = tk.Toplevel(ventana)
    #tamaño de la ventana
    WIND.geometry("1366x768")
    #color de fondo BG
    WIND.config(bg="#89BBFF")
    #se le añade un titulo a la app
    WIND.title("SISTEMA DE COBROS")

    #LOGO
    WIND.iconbitmap("img/LG.ico")
    #la metemos dentro de un label para poder mostrarla
    eti= Label(WIND, image = img1, bg='#89BBFF')
    #eti = tk.Label(WIND, image=imagen_sub)
    eti.place(x=20, y=10)

    #Formulario Crear los widgets del formulario

    #espacio en blanco de la tabla
    tk.Label(WIND, text="SISTEMA DE COBROS", font="Candara 30 bold", bg='#89BBFF', fg="#4169e1", width=0, height=3).grid(row=0, column=6, pady=5)
        
    #FOLIO
    tk.Label(WIND, text="FOLIO:", bg="#89BBFF").grid(row=3, column=2, padx=5, pady=5, sticky = E)
    folio = tk.Entry(WIND, relief=tk.SUNKEN, bd=3, width=10)
    folio.grid(row=3, column=3, sticky=W)

    #PLANTEL
    tk.Label(WIND, text="PLANTEL", bg="#89BBFF").grid(row=3, column=4, padx=5, pady=5)
    plan = tk.Entry(WIND,relief=tk.SUNKEN, bd=3)
    plan.grid(row=3, column=5, sticky=W)

    #MATRICULA
    tk.Label(WIND,text="MATRICULA:", bg="#89BBFF").grid(row=4, column=0, padx=5, pady=5, sticky=E)
    mat = tk.Entry(WIND,relief=tk.SUNKEN, bd=3)
    mat.grid(row=4, column=1, sticky=W)
    
    #NOMBRE DEL ALUMNO
    tk.Label(WIND,text="NOMBRE DEL ALUMNO:", bg="#89BBFF").grid(row=4, column=2, sticky=E, padx=5)
    nom = tk.Entry(WIND,relief=tk.SUNKEN, bd=3)
    nom.grid(row=4, column=3, sticky=W)
    
    #USUARIO
    user1 = e1.get()
    tk.Label(WIND, text="USUARIO:", bg="#89BBFF").grid(row=4, column=4, padx=5)
    user = tk.Label(WIND, text= user1, bg="#89BBFF")
    user.grid(row=4, column=5)

    #GRUPO
    tk.Label(WIND, text="GRUPO:", bg="#89BBFF").grid(row=5, column=0, sticky=E, pady=5, padx=5)
    gru = tk.Entry(WIND,relief=tk.SUNKEN, bd=3)
    gru.grid(row=5, column=1, sticky=W)

    #LICENCIATURA
    tk.Label(WIND, text="LICENCIATURA:", bg="#89BBFF").grid(row=5, column=2, padx=5, sticky=E)
    lice = tk.Entry(WIND,relief=tk.SUNKEN, bd=3)
    lice.grid(row=5, column=3, sticky=W)

    #FECHA
    tk.Label(WIND, text="FECHA:", bg="#89BBFF").grid(row=5, column=4, padx=5)
    dateUno = tk.Label(WIND, text=date.today(), bg="#89BBFF",relief=tk.GROOVE, bd=3)
    date1 = date.today()
    dateUno.grid(row=5, column=5)

    tk.Label(WIND, text="CONCEPTOS", bg="#89BBFF",relief=tk.GROOVE, bd=3).grid(row=6, column=1)
    #INICIAN LOS CONCEPTOS

    conc1 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc1.grid(row=7, column=1)

    conc2 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc2.grid(row=8, column=1)

    conc3 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc3.grid(row=9, column=1)

    conc4 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc4.grid(row=10, column=1)

    conc5 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc5.grid(row=11, column=1)

    conc6 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc6.grid(row=12, column=1)

    conc7 = tk.Entry(WIND, width=30,relief=tk.SUNKEN, bd=3)
    conc7.grid(row=13, column=1)

    #IMPORTE
    tk.Label(WIND, text="IMPORTE:", bg="#89BBFF",relief=tk.GROOVE).grid(row=6, column=2)

    impo1 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo1.grid(row=7, column=2)

    impo2 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo2.grid(row=8, column=2)

    impo3 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo3.grid(row=9, column=2)

    impo4 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo4.grid(row=10, column=2)

    impo5 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo5.grid(row=11, column=2)

    impo6 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo6.grid(row=12, column=2)

    impo7 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    impo7.grid(row=13, column=2)

    #%
    tk.Label(WIND, text="%", bg="#89BBFF",relief=tk.GROOVE, bd=3).grid(row=6, column=3)

    combo1 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
    )
    combo1.config(width=10, height=10)
    combo1.grid(row=7, column=3, pady=3)

    combo2 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo2.config(width=10, height=10)
    combo2.grid(row=8, column=3, pady=3)

    combo3 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo3.config(width=10, height=10)
    combo3.grid(row=9, column=3, pady=3)


    combo4 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo4.config(width=10, height=10)
    combo4.grid(row=10, column=3, pady=3)

    combo5 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo5.config(width=10, height=10)
    combo5.grid(row=11, column=3, pady=3)


    combo6 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo6.config(width=10, height=10)
    combo6.grid(row=12, column=3, pady=3)

    combo7 = ttk.Combobox(
        WIND,
        state="readonly",
        values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    combo7.config(width=10, height=10)
    combo7.grid(row=13, column=3, pady=3)

    #RECARGOS
    tk.Label(WIND, text="RECARGOS:", bg="#89BBFF",relief=tk.GROOVE).grid(row=6, column=4, padx=10)

    rec1 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec1.grid(row=7, column=4, padx=10)

    rec2 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec2.grid(row=8, column=4)

    rec3 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec3.grid(row=9, column=4)

    rec4 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec4.grid(row=10, column=4)

    rec5 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec5.grid(row=11, column=4)

    rec6 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec6.grid(row=12, column=4)

    rec7 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3)
    rec7.grid(row=13, column=4)

    #SUBTOTAL
    tk.Label(WIND, text="SUBTOTAL:", bg="#89BBFF",relief=tk.GROOVE).grid(row=6, column=5, padx=1)

    subt1 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt1.grid(row=7, column=5, padx=1)

    subt2 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt2.grid(row=8, column=5)

    subt3 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt3.grid(row=9, column=5)

    subt4 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt4.grid(row=10, column=5)

    subt5 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt5.grid(row=11, column=5)

    subt6 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt6.grid(row=12, column=5)

    subt7 = tk.Entry(WIND, width=10,relief=tk.SUNKEN, bd=3)
    subt7.grid(row=13, column=5)

    #CANTIDAD QUE RECIBE
    cant_res = tk.Label(WIND, text="CANTIDAD QUE RECIBE", bg="#89BBFF").place(x=755, y=172, width=140, height=19)
    cant_res = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    cant_res.place(x=775, y=203, width=105, height=19)

    #CAMBIO
    cambio = tk.Label(WIND, text="CAMBIO", bg="#89BBFF").place(x=795, y=235, width=60, height=19)
    cambio = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    cambio.place(x=775, y=260, width=105, height=19)

    #FORMA DE PAGO
    tk.Label(WIND, text="FORMA DE PAGO", bg="#89BBFF").place(x=777, y=295, width=100, height=19)
    formP = ttk.Combobox(
        WIND,
        state="readonly",
        values=["Efectivo", "Tarjeta de Credito", "Tarjeta de Debito", "Cheque", "Deposito Bancario"]
    )
    formP.config(width=22, height=10)
    formP.place(x=775, y=325, width=105, height=19)

    #APROVACION
    aprov = tk.Label(WIND, text="APROVACIÓN", bg="#89BBFF").place(x=783, y=357, width=90, height=19)
    aprov = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    aprov.place(x=775, y=385, width=105, height=19)

    #CUENTA RECEPTORA
    cuenta_res = tk.Label(WIND, text="CUENTA RECEPTORA", bg="#89BBFF").place(x=765, y=420, width=120, height=19)
    cuenta_res = ttk.Combobox(
        WIND,
        state="readonly",
        values=["Santander", "No aplica"]
    )
    cuenta_res.config(width=22, height=10)
    cuenta_res.place(x=775, y=455, width=105, height=19)


    #OBSERVACIONES
    observ = tk.Label(WIND, text="OBSERVACIONES:", bg="#89BBFF").place(x=85, y=480, width=110, height=20)
    observ = tk.Entry(WIND, width=30,relief=tk.SUNKEN)
    observ.place(x=210, y=480, width=500, height=20)

    #BOTONES
    boton_enviar = tk.Button(WIND, text="REGISTRAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=enviar_datos)
    boton_enviar.place(x=85, y=520, width=100, height=30)

    btn_Consultar = tk.Button(WIND, text="CONSULTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=Consultar)
    btn_Consultar.place(x=210, y=520, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="INSERTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5,command=Insertar)
    btn_Insert.place(x=330, y=520, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="ACTUALIZAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=actualizar)
    btn_Insert.place(x=460, y=520, width=100, height=30)

    #pruebas
    #pru = tk.Label(ventana, text="PRUEBA:", bg="white").place(x=100, y=500, width=90, height=40)
    #prueba = tk.Entry(ventana, width=30).place(x=200, y=500, width=90, height=40)

    # Cierra la ventana principal
    ventana.withdraw()

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

ventana = tk.Tk()
#tamaño de la ventana
ventana.geometry("700x400")
#color de fondo BG
ventana.config(bg="#89BBFF")
#se le añade un titulo a la app
ventana.title("SISTEMA DE COBROS")

# Centrar la ventana en la pantalla
ventana.update_idletasks()
width = ventana.winfo_width()
height = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (width // 2)
y = (ventana.winfo_screenheight() // 2) - (height // 2)
ventana.geometry(f'{width}x{height}+{x}+{y}')
#LOGO
ventana.iconbitmap("img/LG.ico")

# Configurar columnas y filas para el sistema grid
for i in range(6):
    ventana.grid_columnconfigure(i, weight=1)
    ventana.grid_rowconfigure(i, weight=1)

# USUARIO ENTRADA 
l1=Label(ventana, text="USER",font=("Candara", 20, "bold"), bg='#89BBFF').grid(row=2, column=1, pady=5,columnspan=4)
e1 = Entry(ventana, font=30, relief=SOLID)
e1.grid(row=3, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar

#CONTRASEÑA ENTRADA 
l2 = Label(ventana, text="PASSWORD", font=("Candara", 20, "bold"), bg='#89BBFF').grid(row=4, column=1, pady=5, columnspan=4)
e2 = Entry(ventana, font=30, show='*', relief=SOLID)
e2.grid(row=5, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar

# IMAGEN adding image (remember image should be PNG and not JPG)
img = PhotoImage(file='img/LOGO_TRANSPARENTE.png')
img1 = img.subsample(2, 2)
Label(ventana,image=img1, bg="#89BBFF").grid(row=1, column=1, pady=10, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar


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
eye_button.grid(row=5, column=2, padx=(100, 10),columnspan=2) # Ajusta las coordenadas según sea necesario
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
