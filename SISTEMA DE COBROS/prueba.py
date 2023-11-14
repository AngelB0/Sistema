from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import date
import psycopg2 #importacion del modulo
#conexion a la BD
conexion=psycopg2.connect(user='postgres',
                            password='Resendiz03',
                            host='localhost',
                            port='5432',
                            database='sistema')
#utilizar cursor
cursor=conexion.cursor()
#crear sentencia SQL

sql='SELECT * FROM conceptos'

#ejecutar utilar metodo execute
cursor.execute(sql)
#mostrar el resultado
registro=cursor.fetchall()

print(registro)

#VENTANA SECUNDARIA REGISTRO ALUMNO
def Inser_Alum():
    def Guardar_Alum():
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
        print("DATOS GUARDADOS")

    # Crear una ventana secundaria
    ventana_ins = tk.Toplevel()
    #Color de fondo BG
    ventana_ins.config(bg="#89BBFF")
    #Titulo App
    ventana_ins.title("INSERTAR DATOS")
    ventana_ins.config(width=1000, height=300)

    #MATRICULA
    tk.Label(ventana_ins, text="MATRICULA", bg="white").place(x=50, y=70, width=80, height=20)
    matri2 = tk.Entry(ventana_ins, width=10)
    matri2.place(x=135, y=70, width=80, height=20)

    #ALUMNO
    tk.Label(ventana_ins, text="ALUMNO", bg="white").place(x=250, y=70, width=80, height=20)
    alumno = tk.Entry(ventana_ins, width=10)
    alumno.place(x=335, y=70, width=80, height=20)

    #OFERTA EDUCATIVA 
    tk.Label(ventana_ins, text="OFERTA EDUCATIVA", bg="white").place(x=440, y=70, width=120, height=20)
    ofedu = tk.Entry(ventana_ins, width=10)
    ofedu.place(x=565, y=70, width=200, height=20)

    #PLANTEL
    tk.Label(ventana_ins, text="PLANTEL", bg="white").place(x=790, y=70, width=75, height=20)
    plantel = tk.Entry(ventana_ins, width=10)
    plantel.place(x=870, y=70, width=120, height=20)

    #GRADO
    tk.Label(ventana_ins, text="GRADO", bg="white").place(x=50, y=110, width=40, height=20)
    grad = tk.Entry(ventana_ins, width=10)
    grad.place(x=100, y=110, width=40, height=20)

    #GRUPO
    tk.Label(ventana_ins, text="GRUPO", bg="white").place(x=150, y=110, width=40, height=20)
    grup = tk.Entry(ventana_ins, width=10)
    grup.place(x=200, y=110, width=40, height=20)

    #PERIODO
    tk.Label(ventana_ins, text="PERIODO", bg="white").place(x=250, y=110, width=50, height=20)
    perido = tk.Entry(ventana_ins, width=10)
    perido.place(x=310, y=110, width=80, height=20)

    #TURNO
    tk.Label(ventana_ins, text="TURNO", bg="white").place(x=400, y=110, width=50, height=20)
    turno = tk.Entry(ventana_ins, width=10)
    turno.place(x=460, y=110, width=80, height=20)

    #FECHA DE INSCRIPCION
    tk.Label(ventana_ins, text="FECHA DE INSCRIPCION", bg="white").place(x=50, y=150, width=133, height=20)
    inscripcion = tk.Entry(ventana_ins, width=10)
    inscripcion.place(x=190, y=150, width=100, height=20)

    #ESTATUS
    tk.Label(ventana_ins, text="ESTATUS", bg="white").place(x=300, y=150, width=80, height=20)
    estatus = tk.Entry(ventana_ins, width=10)
    estatus.place(x=385, y=150, width=80, height=20)

    #FECHA ESTATUS
    tk.Label(ventana_ins, text="FECHA ESTATUS", bg="white").place(x=480, y=150, width=90, height=20)
    festatus = tk.Entry(ventana_ins, width=10)
    festatus.place(x=575, y=150, width=80, height=20)



    #Boton cerrar
    boton_cerrar = ttk.Button(ventana_ins, text="Cerrar ventana", command=ventana_ins.destroy)
    boton_cerrar.place(x=50, y=200, width=90, height=40)

    #Boton guardar
    boton_guardar = ttk.Button(ventana_ins, text="GUARDAR", command= Guardar_Alum)
    boton_guardar.place(x=150, y=200, width=90, height=40)


#VENTANA SECUNDARIA CONCEPTO
def Inser_Concep():
     # Crear una ventana secundaria
     ventana_ins = tk.Toplevel()
     #Color de fondo BG
     ventana_ins.config(bg="#89BBFF")
     #Titulo App
     ventana_ins.title("INSERTAR NUEVO CONCEPTO")
     ventana_ins.config(width=1000, height=300)

     #CODIGO
     tk.Label(ventana_ins, text="CODIGO", bg="white").place(x=50, y=70, width=80, height=20)
     codigo = tk.Entry(ventana_ins, width=10)
     codigo.place(x=135, y=70, width=80, height=20)

     #CONCEPTO
     tk.Label(ventana_ins, text="CONCEPTO", bg="white").place(x=250, y=70, width=80, height=20)
     alumno = tk.Entry(ventana_ins, width=10)
     alumno.place(x=335, y=70, width=80, height=20)

     #CUENTA CONTABLE 
     tk.Label(ventana_ins, text="CUENTA CONTABLE", bg="white").place(x=440, y=70, width=120, height=20)
     ofedu = tk.Entry(ventana_ins, width=10)
     ofedu.place(x=565, y=70, width=200, height=20)
     #COSTO
     tk.Label(ventana_ins, text="COSTO", bg="white").place(x=790, y=70, width=75, height=20)
     plantel = tk.Entry(ventana_ins, width=10)
     plantel.place(x=870, y=70, width=120, height=20)

     #CLASIFICACION
     tk.Label(ventana_ins, text="CLASIFICACION", bg="white").place(x=50, y=110, width=100, height=20)
     concepto = tk.Entry(ventana_ins, width=10)
     concepto.place(x=160, y=110, width=100, height=20)

     #Boton cerrar
     boton_cerrar = ttk.Button(
         ventana_ins,
         text="Cerrar ventana", 
         command=ventana_ins.destroy
     )
     #Boton Guardar
     boton_guardar = ttk.Button(
         ventana_ins,
         text="GUARDAR",
     )
     boton_guardar.place(x=150, y=200, width=90, height=40)
     boton_cerrar.place(x=50, y=200, width=90, height=40)

#VENTANA SECUNDARIA DE CONSULTAR SEGUNDA
def Consu_Alu():
        # Crear una ventana secundaria.
        ventana_consul = tk.Toplevel()
        #color de fondo BG
        ventana_consul.config(bg="#89BBFF")
        #se le añade un titulo a la app
        ventana_consul.title("CONSULTA DE REGISTROS")
        ventana_consul.config(width=500, height=300)
        boton_cerrar = ttk.Button(
        ventana_consul,
        text="Cerrar ventana", 
        command=ventana_consul.destroy
        )
        boton_cerrar.place(x=50, y=100, width=90, height=40)

#VENTANA SECUNDARIA DE CONSULTAR PRIMERA
def Consultar():
    # Crear una ventana secundaria.
    ventana_consul = tk.Toplevel()
    #color de fondo BG
    ventana_consul.config(bg="#89BBFF")
    #se le añade un titulo a la app
    ventana_consul.title("CONSULTA DE REGISTROS")
    ventana_consul.config(width=500, height=300)
        
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    btn_Alumnos = ttk.Button(
        ventana_consul,
        text="Consultar Alumnos", 
        command=Consu_Alu
    )
    btn_Conceptos = ttk.Button(
        ventana_consul,
        text="Consultar Conceptos", 
        command=Consu_Alu
    )
    boton_cerrar = ttk.Button(
        ventana_consul,
        text="Cerrar ventana", 
        command=ventana_consul.destroy
    )

    boton_cerrar.place(x=50, y=100, width=90, height=40)
    btn_Alumnos.place(x=150, y=100, width=120, height=40)
    btn_Conceptos.place(x=280, y=100, width=125, height=40)

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
    
# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos():
    FOL = folio.get()
    MATRI = mat.get()
    NOMA = nom.get()
    GRUP = gru.get()
    LIC = lice.get()
    FE = date1
    PLA = plan.get()
    USU = user.get()
    #Conceptos
    CON1 = conc1.get()
    CON2 = conc2.get()
    CON3 = conc3.get()
    CON4 = conc4.get()
    CON5 = conc5.get()
    CON6 = conc6.get()
    CON7 = conc7.get()
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
    #Cantidad que recibe
    CANTR = cant_res.get()
    #Cambio
    CAM =  cambio.get()
    #forma de pago
    FP = formP.get()
    #Aprovacion
    APRO = aprov.get()
    #cuenta reseptora
    CUR = cuenta_res.get()
    #Observaciones
    OBSERVA = observ.get()

    print("DATOS GUARDADOS")

def INDEX():
     print('holaaaaaa')

#VENTANA PRINCIPAL
ventana = tk.Tk()
#tamaño de la ventana
ventana.geometry("1366x768")
#color de fondo BG
ventana.config(bg="#89BBFF")
#se le añade un titulo a la app
ventana.title("SISTEMA DE COBROS")

#insertamos la img
my_ima = PhotoImage(file='LOGO_TRANSPARENTE.png')
imagen_sub=my_ima.subsample(2)
#la metemos dentro de un label para poder mostrarla
Etiqueta = Label(ventana, image=imagen_sub).place(x=20, y=10)


#Formulario Crear los widgets del formulario

#espacio en blanco de la tabla
tk.Label(ventana, bg='#89BBFF', width=0, height=10).grid(row=0, column=3, pady=5)
    
#FOLIO
tk.Label(ventana, text="FOLIO:", bg="white").grid(row=3, column=2, padx=5, pady=5, sticky = E)
folio = tk.Entry(ventana, width=10)
folio.grid(row=3, column=3, sticky=W)

#PLANTEL
tk.Label(ventana, text="PLANTEL", bg="white").grid(row=3, column=4, padx=5, pady=5)
plan = tk.Entry(ventana)
plan.grid(row=3, column=5, sticky=W)

#MATRICULA
tk.Label(ventana, text="MATRICULA:", bg="white").grid(row=4, column=0, padx=5, pady=5, sticky=E)
mat = tk.Entry(ventana)
mat.grid(row=4, column=1, sticky=W)
 
#NOMBRE DEL ALUMNO
tk.Label(ventana, text="NOMBRE DEL ALUMNO:", bg="white").grid(row=4, column=2, sticky=E, padx=5)
nom = tk.Entry(ventana)
nom.grid(row=4, column=3, sticky=W)
 
#USUARIO
tk.Label(ventana, text="USUARIO:", bg="white").grid(row=4, column=4, padx=5)
user = tk.Entry(ventana)
user.grid(row=4, column=5, sticky=W)

#GRUPO
tk.Label(ventana, text="GRUPO:", bg="white").grid(row=5, column=0, sticky=E, pady=5, padx=5)
gru = tk.Entry(ventana)
gru.grid(row=5, column=1, sticky=W)

#LICENCIATURA
tk.Label(ventana, text="LICENCIATURA:", bg="white").grid(row=5, column=2, padx=5, sticky=E)
lice = tk.Entry(ventana)
lice.grid(row=5, column=3, sticky=W)

#FECHA
tk.Label(ventana, text="FECHA:", bg="white").grid(row=5, column=4, padx=5)
dateUno = tk.Label(ventana, text=date.today(), bg="white")
date1 = date.today()
dateUno.grid(row=5, column=5)

tk.Label(ventana, text="CONCEPTOS", bg="white").grid(row=6, column=1)
#INICIAN LOS CONCEPTOS

conc1 = tk.Entry(ventana, width=30)
conc1.grid(row=7, column=1)

conc2 = tk.Entry(ventana, width=30)
conc2.grid(row=8, column=1)

conc3 = tk.Entry(ventana, width=30)
conc3.grid(row=9, column=1)

conc4 = tk.Entry(ventana, width=30)
conc4.grid(row=10, column=1)

conc5 = tk.Entry(ventana, width=30)
conc5.grid(row=11, column=1)

conc6 = tk.Entry(ventana, width=30)
conc6.grid(row=12, column=1)

conc7 = tk.Entry(ventana, width=30)
conc7.grid(row=13, column=1)

#IMPORTE
tk.Label(ventana, text="IMPORTE:", bg="white").grid(row=6, column=2)

impo1 = tk.Entry(ventana, width=10)
impo1.grid(row=7, column=2)

impo2 = tk.Entry(ventana, width=10)
impo2.grid(row=8, column=2)

impo3 = tk.Entry(ventana, width=10)
impo3.grid(row=9, column=2)

impo4 = tk.Entry(ventana, width=10)
impo4.grid(row=10, column=2)

impo5 = tk.Entry(ventana, width=10)
impo5.grid(row=11, column=2)

impo6 = tk.Entry(ventana, width=10)
impo6.grid(row=12, column=2)

impo7 = tk.Entry(ventana, width=10)
impo7.grid(row=13, column=2)

#%
tk.Label(ventana, text="%", bg="white").grid(row=6, column=3)

combo1 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo1.config(width=10, height=10)
combo1.grid(row=7, column=3, pady=3)

combo2 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo2.config(width=10, height=10)
combo2.grid(row=8, column=3, pady=3)

combo3 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo3.config(width=10, height=10)
combo3.grid(row=9, column=3, pady=3)


combo4 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo4.config(width=10, height=10)
combo4.grid(row=10, column=3, pady=3)

combo5 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo5.config(width=10, height=10)
combo5.grid(row=11, column=3, pady=3)


combo6 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo6.config(width=10, height=10)
combo6.grid(row=12, column=3, pady=3)

combo7 = ttk.Combobox(
    state="readonly",
    values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
)
combo7.config(width=10, height=10)
combo7.grid(row=13, column=3, pady=3)

#RECARGOS
tk.Label(ventana, text="RECARGOS:", bg="white").grid(row=6, column=4, padx=10)

rec1 = tk.Entry(ventana, width=10)
rec1.grid(row=7, column=4, padx=10)

rec2 = tk.Entry(ventana, width=10)
rec2.grid(row=8, column=4)

rec3 = tk.Entry(ventana, width=10)
rec3.grid(row=9, column=4)

rec4 = tk.Entry(ventana, width=10)
rec4.grid(row=10, column=4)

rec5 = tk.Entry(ventana, width=10)
rec5.grid(row=11, column=4)

rec6 = tk.Entry(ventana, width=10)
rec6.grid(row=12, column=4)

rec7 = tk.Entry(ventana, width=10)
rec7.grid(row=13, column=4)

#SUBTOTAL
tk.Label(ventana, text="SUBTOTAL:", bg="white").grid(row=6, column=5, padx=1)

subt1 = tk.Entry(ventana, width=10)
subt1.grid(row=7, column=5, padx=1)

subt2 = tk.Entry(ventana, width=10)
subt2.grid(row=8, column=5)

subt3 = tk.Entry(ventana, width=10)
subt3.grid(row=9, column=5)

subt4 = tk.Entry(ventana, width=10)
subt4.grid(row=10, column=5)

subt5 = tk.Entry(ventana, width=10)
subt5.grid(row=11, column=5)

subt6 = tk.Entry(ventana, width=10)
subt6.grid(row=12, column=5)

subt7 = tk.Entry(ventana, width=10)
subt7.grid(row=13, column=5)

#CANTIDAD QUE RECIBE
cant_res = tk.Label(ventana, text="CANTIDAD QUE RECIBE", bg="white").place(x=755, y=172, width=140, height=19)
cant_res = tk.Entry(ventana, width=25)
cant_res.place(x=775, y=203, width=105, height=19)

#CAMBIO
cambio = tk.Label(ventana, text="CAMBIO", bg="white").place(x=795, y=235, width=60, height=19)
cambio = tk.Entry(ventana, width=25)
cambio.place(x=775, y=260, width=105, height=19)

#FORMA DE PAGO
tk.Label(ventana, text="FORMA DE PAGO", bg="white").place(x=777, y=295, width=100, height=19)
formP = ttk.Combobox(
    state="readonly",
    values=["Efectivo", "Tarjeta de Credito", "Tarjeta de Debito", "Cheque", "Deposito Bancario"]
)
formP.config(width=22, height=10)
formP.place(x=775, y=325, width=105, height=19)

#APROVACION
aprov = tk.Label(ventana, text="APROVACIÓN", bg="white").place(x=783, y=357, width=90, height=19)
aprov = tk.Entry(ventana, width=25)
aprov.place(x=775, y=385, width=105, height=19)

#CUENTA RECEPTORA
cuenta_res = tk.Label(ventana, text="CUENTA RECEPTORA", bg="white").place(x=765, y=420, width=120, height=19)
cuenta_res = ttk.Combobox(
    state="readonly",
    values=["Santander", "No aplica"]
)
cuenta_res.config(width=22, height=10)
cuenta_res.place(x=775, y=455, width=105, height=19)


#OBSERVACIONES
observ = tk.Label(ventana, text="OBSERVACIONES:", bg="white").place(x=85, y=480, width=110, height=20)
observ = tk.Entry(ventana, width=30)
observ.place(x=210, y=480, width=500, height=20)

#BOTONES
boton_enviar = tk.Button(ventana, text="REGISTRAR", bg="white", command=enviar_datos)
boton_enviar.place(x=85, y=520, width=100, height=30)

btn_Consultar = tk.Button(ventana, text="CONSULTAR", bg="white", command=Consultar)
btn_Consultar.place(x=210, y=520, width=100, height=30)

btn_Insert = tk.Button(ventana, text="INSERTAR", bg="white", command=Insertar)
btn_Insert.place(x=330, y=520, width=100, height=30)

#pruebas
#pru = tk.Label(ventana, text="PRUEBA:", bg="white").place(x=100, y=500, width=90, height=40)
#prueba = tk.Entry(ventana, width=30).place(x=200, y=500, width=90, height=40)


#el bucle que hace que se repita todo hasta que se cierre la ventana
ventana.mainloop()
cursor.close()
conexion.close()
