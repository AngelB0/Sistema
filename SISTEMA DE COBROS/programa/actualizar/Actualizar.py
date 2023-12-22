import tkinter as tk
from tkinter import ttk

from def_globales import ventana

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
