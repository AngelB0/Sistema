from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import date
import psycopg2 #importacion del modulo

from def_globales import *
from actualizar.Actualizar import actualizar
from consultar.Consultar import Consultar
from insertar.Insertar import Insertar

#CLASE MAIN todo Va dentro de esta CLASS
def INDEX():

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
        SUB1 = int(subt1.get())
        SUB2 = int(subt2.get())
        SUB3 = int(subt3.get())
        SUB4 = int(subt4.get())
        SUB5 = int(subt5.get())
        SUB6 = int(subt6.get())
        SUB7 = int(subt7.get())
        TOTAL= SUB1 + SUB2 + SUB3 + SUB4 + SUB5 + SUB6 + SUB7
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

    def obtener_opciones_bd_combo():
        user3 = e1.get()
        passw3 = e2.get()
        bd="sistema"
        conexion = psycopg2.connect(
                            user=user3,
                            password=passw3,
                            host='localhost',
                            port='5432',
                            database= bd
                        )

            # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Ejecutar una consulta para obtener opciones (reemplaza con tu propia consulta)
        cursor.execute("SELECT concepto FROM conceptos")
        opciones = cursor.fetchall()

        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

        return opciones
    
    def mostrar_opciones_combo():
        # Obtener las opciones de la base de datos
        opciones_bd_con = obtener_opciones_bd_combo()

        # Limpiar el ComboBox
        conc1['values'] = ()
        conc2['values'] = ()
        conc3['values'] = ()
        conc4['values'] = ()
        conc5['values'] = ()
        conc6['values'] = ()
        conc7['values'] = ()

        # Configurar las nuevas opciones en el ComboBox
        conc1['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc2['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc3['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc4['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc5['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc6['values'] = [opcion[0] for opcion in opciones_bd_con]
        conc7['values'] = [opcion[0] for opcion in opciones_bd_con]
    
    def obtener_registro_completo(llave_primaria):
        user3= e1.get()
        passw3 = e2.get()
        bd= "sistema"
        conexion = psycopg2.connect(user=user3,
                                    password=passw3,
                                    host='localhost',
                                    port='5432',
                                    database=bd)

        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alumnos WHERE Matricula = %s", (llave_primaria,))
        registro_completo = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro_completo

    def accion_al_seleccionar(event):
         # Vectores para almacenar los valores
        matriculas = []
        nombres = []
        plantels = []
        oferta_ed =[]
        gra =[]
        gru =[]
        periodo =[]
        turno =[]
        fecha_in =[]
        estatus=[]
        fecha_es=[]
    # Añade más vectores según sea necesario para las demás columnas
        opcion_seleccionada = mat.get()
        # Actualizar el contenido del Label con la opción seleccionada
        #label_resultado.config(text=f"Opción seleccionada: {opcion_seleccionada}")
        if opcion_seleccionada:
            registro_completo = obtener_registro_completo(opcion_seleccionada)
            registro_formateado = ', '.join(map(str, registro_completo))
            if registro_completo:
                # Almacena cada valor del registro en vectores
                Matricula, alumno, plantel,oferta, grado, grupo1, peri, turn, date_in, sta, date_es = registro_completo
                matriculas.append(Matricula)
                nombres.append(alumno)
                plantels.append(plantel)
                oferta_ed.append(oferta) 
                gra.append(grado)
                gru.append(grupo1)
                periodo.append(peri)
                turno.append(turn)
                fecha_in.append(date_in)
                estatus.append(sta)
                fecha_es.append(''.join(map(str, date_es)))
                # Formatea la cadena antes de imprimir
                registro_formateado = ', '.join(map(str, registro_completo))
                #segun la matricula imprimimos la informacion del alumno
                a=nombres
                plan.config(text=str(registro_completo[2]))
                nom.config(text= str(registro_completo[1]))
                # Añade más líneas según sea necesario para las demás columnas
                # Muestra el registro completo
                print("Registro Completo:", registro_formateado)
                # Al finalizar, puedes acceder a los vectores matriculas, nombres, plantels, etc., para obtener los valores almacenados.
                print("Matriculas:", matriculas)
                print("Nombres:", str(registro_completo[1]))
                print("Plantels:", str(registro_completo[2]))
                print("Oferta educativa:", oferta_ed)
                print("Grado:", gra)
                print("GRUPO:", gru)
                print("periodo:", periodo)
                print("turno:", turno)
                print("fecha inscripcion:", fecha_in)
                print("estatus:", estatus)
                print("fecha de estatus:", fecha_es)
            else:
                print("Registro no encontrado.")

    def obtener_mat_bd():
        user3 = e1.get()
        passw3 = e2.get()
        bd="sistema"
        conexion = psycopg2.connect(
                            user=user3,
                            password=passw3,
                            host='localhost',
                            port='5432',
                            database= bd
                        )
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Ejecutar una consulta para obtener opciones (reemplaza con tu propia consulta)
        cursor.execute("SELECT * FROM alumnos")
        matris = cursor.fetchall()

        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

        return matris

    def mostrar_mat():
         # Obtener las opciones de la base de datos
        opciones_bd_mat = obtener_mat_bd()
        # Limpiar el ComboBox
        mat['values'] = ()
        # Configurar las nuevas opciones en el ComboBox
        mat['values'] = [opcion[0] for opcion in opciones_bd_mat]
        
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
    plan = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=30)
    plan.grid(row=3, column=5, sticky=W)

    #MATRICULA
    tk.Label(WIND,text="MATRICULA:", bg="#89BBFF").grid(row=4, column=0, padx=5, pady=5, sticky=E)
    mat = ttk.Combobox(WIND, width=30)
    mat.grid(row=4, column=1, sticky=W)
    # Vincular la función al evento <<ComboboxSelected>>
    mat.bind("<<ComboboxSelected>>", accion_al_seleccionar)

    #NOMBRE DEL ALUMNO
    tk.Label(WIND,text="NOMBRE DEL ALUMNO:", bg="#89BBFF").grid(row=4, column=2, sticky=E, padx=5)
    nom = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=30)
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

    conc1 = ttk.Combobox(WIND, width=27)
    conc1.grid(row=7, column=1)

    conc2 = ttk.Combobox(WIND, width=27)
    conc2.grid(row=8, column=1)

    conc3 = ttk.Combobox(WIND, width=27)
    conc3.grid(row=9, column=1)

    conc4 = ttk.Combobox(WIND, width=27)
    conc4.grid(row=10, column=1)

    conc5 = ttk.Combobox(WIND, width=27)
    conc5.grid(row=11, column=1)

    conc6 = ttk.Combobox(WIND, width=27)
    conc6.grid(row=12, column=1)

    conc7 = ttk.Combobox(WIND, width=27)
    conc7.grid(row=13, column=1)

    #IMPORTE
    tk.Label(WIND, text="IMPORTE:", bg="#89BBFF",relief=tk.GROOVE).grid(row=6, column=2)

    impo1 = tk.Label(WIND, text="", relief=tk.SUNKEN, width=10,bg="white", bd=3)
    impo1.grid(row=7, column=2)

    impo2 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white")
    impo2.grid(row=8, column=2)

    impo3 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    impo3.grid(row=9, column=2)

    impo4 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white")
    impo4.grid(row=10, column=2)

    impo5 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white")
    impo5.grid(row=11, column=2)

    impo6 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    impo6.grid(row=12, column=2)

    impo7 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
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

    subt1 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt1.grid(row=7, column=5, padx=1)

    subt2 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt2.grid(row=8, column=5)

    subt3 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt3.grid(row=9, column=5)

    subt4 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt4.grid(row=10, column=5)

    subt5 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt5.grid(row=11, column=5)

    subt6 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt6.grid(row=12, column=5)

    subt7 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white")
    subt7.grid(row=13, column=5)

    #CANTIDAD QUE RECIBE
    cant_res = tk.Label(WIND, text="CANTIDAD QUE RECIBE", bg="#89BBFF").place(x=770, y=172, width=140, height=19)
    cant_res = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    cant_res.place(x=790, y=203, width=105, height=19)

    #CAMBIO
    cambio = tk.Label(WIND, text="CAMBIO", bg="#89BBFF").place(x=810, y=235, width=60, height=19)
    cambio = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    cambio.place(x=790, y=260, width=105, height=19)

    #FORMA DE PAGO
    tk.Label(WIND, text="FORMA DE PAGO", bg="#89BBFF").place(x=792, y=295, width=100, height=19)
    formP = ttk.Combobox(
        WIND,
        state="readonly",
        values=["Efectivo", "Tarjeta de Credito", "Tarjeta de Debito", "Cheque", "Deposito Bancario"]
    )
    formP.config(width=22, height=10)
    formP.place(x=790, y=325, width=105, height=19)

    #APROVACION
    aprov = tk.Label(WIND, text="APROVACIÓN", bg="#89BBFF").place(x=798, y=357, width=90, height=19)
    aprov = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3)
    aprov.place(x=790, y=385, width=105, height=19)

    #CUENTA RECEPTORA
    cuenta_res = tk.Label(WIND, text="CUENTA RECEPTORA", bg="#89BBFF").place(x=780, y=420, width=120, height=19)
    cuenta_res = ttk.Combobox(
        WIND,
        state="readonly",
        values=["Santander", "No aplica"]
    )
    cuenta_res.config(width=22, height=10)
    cuenta_res.place(x=790, y=455, width=105, height=19)

    #OBSERVACIONES
    observ = tk.Label(WIND, text="OBSERVACIONES:", bg="#89BBFF").place(x=85, y=480, width=110, height=20)
    observ = tk.Entry(WIND, width=30,relief=tk.SUNKEN)
    observ.place(x=210, y=480, width=300, height=20)

    #TOTAL A PAGAR
    total = tk.Label(WIND, text="TOTAL", bg="#89BBFF").place(x=570, y=480, width=40, height=20)
    total1 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white").place(x=655, y=480, width=79, height=20)

    #BOTONES
    boton_enviar = tk.Button(WIND, text="REGISTRAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=enviar_datos)
    boton_enviar.place(x=85, y=520, width=100, height=30)

    btn_Consultar = tk.Button(WIND, text="CONSULTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=Consultar)
    btn_Consultar.place(x=210, y=520, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="INSERTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5,command=Insertar)
    btn_Insert.place(x=330, y=520, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="ACTUALIZAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=actualizar)
    btn_Insert.place(x=460, y=520, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="ELIMINAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command="Eliminar")
    btn_Insert.place(x=580, y=520, width=100, height=30)

    #pruebas
    #pru = tk.Label(ventana, text="PRUEBA:", bg="white").place(x=100, y=500, width=90, height=40)
    #prueba = tk.Entry(ventana, width=30).place(x=200, y=500, width=90, height=40)

    # Llamar a las funciones al inicio
    mostrar_opciones_combo()
    mostrar_mat()
    # Cierra la ventana principal
    ventana.withdraw()