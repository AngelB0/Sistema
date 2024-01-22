# @autor: JORGE ANGEL BECERRIL GONZALEZ
from tkinter import *
from customtkinter import CTk, CTkComboBox
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import PhotoImage
from tkinter import filedialog
import pandas as pd
from sqlalchemy import create_engine
import pathlib
import sys
from tkinter import messagebox #libreria para los mensajes de alerta
import psycopg2 #importacion del modulo
import time#para el tiempo

#CLASE MAIN todo Va dentro de esta CLASS
def INDEX():
    #VENTANA PARA ELIMINAR 
    def eliminar():
        def delete_Alum_com():
            try:
                # Establecer la conexión a la base de datos
                user3 = e1.get()
                passw3 = e2.get()
                bd="sistema"
                conn = psycopg2.connect(
                                    user=user3,
                                    password=passw3,
                                    host='localhost',
                                    port='5432',
                                    database= bd
                                )

                # Crear un objeto cursor
                cursor = conn.cursor()

                # Ejecutar la consulta para eliminar todos los registros de la tabla
                cursor.execute("DELETE FROM alumnos;")

                # Confirmar la transacción
                conn.commit()

                # Cerrar el cursor y la conexión
                cursor.close()
                conn.close()

                # Mostrar una alerta de éxito
                messagebox.showinfo("Éxito", "Registros eliminados correctamente.")

            except Exception as e:
                # Mostrar una alerta de error
                messagebox.showerror("Error", f"Error al eliminar registros:\n{str(e)}")

        
        def delete_Concep_com():
            print("hola")

        # Crear una ventana secundaria.
        window_delete = tk.Toplevel()
        #color de fondo BG
        window_delete.config(bg="#1D1212")
        #se le añade un titulo a la app
        window_delete.title("ELIMINAR REGISTROS")
        window_delete.config(width=500, height=300)
        
        tk.Label(window_delete, text="ELIJA UNA OPCION", bg="#1D1212", fg="white").place(x=50, y=50)

        # Crear un botón dentro de la ventana secundaria
         # para cerrar la misma.
        btn_Alumnos_del = tk.Button(
            window_delete,
            text="Eliinar Alumnos (tabla conmpleta)", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=delete_Alum_com
         )
        btn_Conceptos_del = tk.Button(#FUNCION ELIMINAR CONCEPTOS
            window_delete,
            text="Eliminar Conceptos (tabla completa)", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=delete_Concep_com
        )
        btn_cerrar_del = tk.Button(
            window_delete,
            text="Cerrar ventana", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=window_delete.destroy
        )
        
        btn_cerrar_del.place(x=50, y=100, width=90, height=40)
        btn_Alumnos_del.place(x=150, y=100, width=145, height=40)
        btn_Conceptos_del.place(x=310, y=100, width=150, height=40)
        # Cierra la ventana principal
        ventana.withdraw()

    #VENTANA ACTUALIZAR
    def actualizar():
        #VENTANA ACTUALIZAR REGISTRO DE ALUMNO
        def act_Alum():
            def Save_Alum():
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
                cursor = conexion.cursor()

                aux1 = int(matri2.get())
                aux2 = alumno_a.get(1.0, tk.END)
                aux3 = plantel_a.get(1.0, tk.END)
                aux4 = ofedu_a.get(1.0, tk.END)
                aux5= int(grad_a.get(1.0, tk.END))
                aux6 = grup_a.get(1.0, tk.END)
                aux7 = perido_a.get(1.0, tk.END)
                aux8 = turno_al.get(1.0, tk.END)
                aux9 = inscripcion_a.get(1.0, tk.END)
                aux10 = estatus_a.get(1.0, tk.END)
                aux11 = festatus_a.get(1.0, tk.END)
                cursor.execute("UPDATE prueba SET alumno = %s, plantel = %s, oferta_edu = %s, grado = %s, grupo = %s, periodo = %s, turno = %s, fecha_ins = %s , estatus = %s, fecha_est = %s WHERE matricula = %s",
                                (aux2, aux3, aux4, aux5, aux6, aux7, aux8, aux9, aux10, aux11, aux1))
                messagebox.showinfo("VALIDACION", "DATOS ACTUALIZADOS")
                matri2.delete(0, tk.END)
                alumno_a.delete(1.0, tk.END)
                plantel_a.delete(1.0, tk.END)
                ofedu_a.delete(1.0, tk.END)
                grad_a.delete(1.0, tk.END)
                grup_a.delete(1.0, tk.END)
                perido_a.delete(1.0, tk.END)
                turno_al.delete(1.0, tk.END)
                inscripcion_a.delete(1.0, tk.END)
                estatus_a.delete(1.0, tk.END)
                festatus_a.delete(1.0, tk.END)

                conexion.commit()
                cursor.close()
                conexion.close()

            def obtener_registro_completo_act(llave_primaria):
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

                cursor = conexion.cursor()

                cursor.execute("SELECT * FROM prueba WHERE Matricula = %s", (llave_primaria,))
                registro_completo = cursor.fetchone()

                cursor.close()
                conexion.close()

                return registro_completo

            def accion_al_seleccionar_act(event):
            # Añade más vectores según sea necesario para las demás columnas
                opcion_seleccionada = matri2.get()
                # Actualizar el contenido del Label con la opción seleccionada
                #label_resultado.config(text=f"Opción seleccionada: {opcion_seleccionada}")
                if opcion_seleccionada:
                    registro_completo = obtener_registro_completo_act(opcion_seleccionada)
                    if registro_completo:
                        #segun la matricula imprimimos la informacion del alumno
                        entered_text_1 = str(registro_completo[1])#ALUMNO
                        alumno_a.config(state=tk.NORMAL)
                        alumno_a.delete(1.0, tk.END)
                        alumno_a.insert(tk.END, f"{entered_text_1}")

                        entered_text_2 = str(registro_completo[2])#PLANTEL
                        plantel_a.config(state=tk.NORMAL)
                        plantel_a.delete(1.0, tk.END)
                        plantel_a.insert(tk.END, f"{entered_text_2}")

                        entered_text_3 = str(registro_completo[3])#OFERTA EDUCATIVA
                        ofedu_a.config(state=tk.NORMAL)
                        ofedu_a.delete(1.0, tk.END)
                        ofedu_a.insert(tk.END, f"{entered_text_3}")

                        entered_text_4 = str(registro_completo[4])#GRADO
                        grad_a.config(state=tk.NORMAL)
                        grad_a.delete(1.0, tk.END)
                        grad_a.insert(tk.END, f"{entered_text_4}")

                        entered_text_5 = str(registro_completo[5])#GRUPO
                        grup_a.config(state=tk.NORMAL)
                        grup_a.delete(1.0, tk.END)
                        grup_a.insert(tk.END, f"{entered_text_5}")
                        entered_text_6 = str(registro_completo[6])#PERIODO
                        perido_a.config(state=tk.NORMAL)
                        perido_a.delete(1.0, tk.END)
                        perido_a.insert(tk.END, f"{entered_text_6}")
                        entered_text_7 = str(registro_completo[7])#TURNO
                        turno_al.config(state=tk.NORMAL)
                        turno_al.delete(1.0, tk.END)
                        turno_al.insert(tk.END, f"{entered_text_7}")
                        entered_text_8 = str(registro_completo[8])#INSCRIPCION
                        inscripcion_a.config(state=tk.NORMAL)
                        inscripcion_a.delete(1.0, tk.END)
                        inscripcion_a.insert(tk.END, f"{entered_text_8}")
                        entered_text_9 = str(registro_completo[9])#ESTATUS
                        estatus_a.config(state=tk.NORMAL)
                        estatus_a.delete(1.0, tk.END)
                        estatus_a.insert(tk.END, f"{entered_text_9}")
                        entered_text_10 = str(registro_completo[10])#TURNO
                        festatus_a.config(state=tk.NORMAL)
                        festatus_a.delete(1.0, tk.END)
                        festatus_a.insert(tk.END, f"{entered_text_10}")
                    else:
                        print("Registro no encontrado.")

            def obtener_mat_bd_act():
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

            def on_key_release_act(event):
                    number = mostrar_mat_act()
                    try:
                        value = int(combobox_var.get())
                        filtered_values = [item for item in number if str(value) in str(item)]

                    except ValueError:
                        filtered_values = []

                    matri2['values'] = filtered_values

            def mostrar_mat_act():
                # Obtener las opciones de la base de datos
                opciones_bd_mat = obtener_mat_bd_act()
                # Limpiar el ComboBox
                matri2['values'] = ()
                # Configurar las nuevas opciones en el ComboBox
                matri2['values'] = [opcion[0] for opcion in opciones_bd_mat]
                number_list = matri2['values'] = [opcion[0] for opcion in opciones_bd_mat]

                return number_list
            
            # Crear una ventana secundaria.
            window_alu = tk.Toplevel()
            #color de fondo BG
            window_alu.config(bg="#1D1212")
            #se le añade un titulo a la app
            window_alu.title("ACTUALIZAR REGISTRO ALUMNOS")
            window_alu.config(width=1080, height=600)

            #MATRICULA
            tk.Label(window_alu, text="MATRICULA:", bg="#1D1212", fg="white").place(x=44, y=70, width=80, height=20)
            combobox_var = tk.StringVar()
            matri2 = ttk.Combobox(window_alu, width=20, textvariable=combobox_var)
            matri2.place(x=126, y=70, width=92, height=20)
            # Vincular la función al evento <<ComboboxSelected>>
            matri2.bind("<<ComboboxSelected>>", accion_al_seleccionar_act)
            matri2.bind('<KeyRelease>', on_key_release_act)

            #ALUMNO
            tk.Label(window_alu, text="ALUMNO:",bg="#1D1212", fg="white").place(x=36, y=100, width=80, height=20)
            alumno_a = tk.Text(window_alu, height=1, width=35, wrap=tk.NONE, bd=0, padx=2, pady=2)
            alumno_a.place(x=125, y=100)
            alumno_a.insert(tk.END, "")

            #OFERTA EDUCATIVA 
            tk.Label(window_alu, text="OFERTA EDUCATIVA:", bg="#1D1212", fg="white").place(x=420, y=100, width=120, height=20)
            ofedu_a = tk.Text(window_alu, height=1, width=50, wrap=tk.NONE, bd=0, padx=2, pady=2)
            ofedu_a.place(x=545, y=100)
            ofedu_a.insert(tk.END, "")

            #PLANTEL
            tk.Label(window_alu, text="PLANTEL:", bg="#1D1212", fg="white").place(x=690, y=130, width=75, height=20)
            plantel_a = tk.Text(window_alu, height=1, width=22, wrap=tk.NONE, bd=0, padx=2, pady=2)
            plantel_a.insert(tk.END, "")
            plantel_a.place(x=770, y=130)

            #GRADO
            tk.Label(window_alu, text="GRADO:",bg="#1D1212", fg="white").place(x=50, y=130, width=40, height=20)
            grad_a = tk.Text(window_alu, height=1, width=2, wrap=tk.NONE, bd=0, padx=2, pady=2)
            grad_a.insert(tk.END, "")
            grad_a.place(x=100, y=130)

            #GRUPO
            tk.Label(window_alu, text="GRUPO:", bg="#1D1212", fg="white").place(x=135, y=130, width=40, height=20)
            grup_a = tk.Text(window_alu, height=1, width=16, wrap=tk.NONE, bd=0, padx=2, pady=2)
            grup_a.insert(tk.END, "")
            grup_a.place(x=185, y=130)

            #PERIODO
            tk.Label(window_alu, text="PERIODO:",bg="#1D1212", fg="white").place(x=335, y=130, width=50, height=20)
            perido_a = tk.Text(window_alu, height=1, width=15, wrap=tk.NONE, bd=0, padx=2, pady=2)
            perido_a.insert(tk.END, "")
            perido_a.place(x=395, y=130)

            #TURNO
            tk.Label(window_alu, text="TURNO:",bg="#1D1212", fg="white").place(x=530, y=130, width=50, height=20)
            turno_al = tk.Text(window_alu, height=1, width=10, wrap=tk.NONE, bd=0, padx=2, pady=2)
            turno_al.insert(tk.END, "")
            turno_al.place(x=590, y=130)

            #FECHA DE INSCRIPCION
            tk.Label(window_alu, text="FECHA DE INSCRIPCION:", bg="#1D1212", fg="white").place(x=50, y=160, width=133, height=20)
            inscripcion_a = tk.Text(window_alu, height=1, width=10, wrap=tk.NONE, bd=0, padx=2, pady=2)
            inscripcion_a.insert(tk.END, "")
            inscripcion_a.place(x=190, y=160)

            #ESTATUS
            tk.Label(window_alu, text="ESTATUS:", bg="#1D1212", fg="white").place(x=285, y=160, width=80, height=20)
            estatus_a = tk.Text(window_alu, height=1, width=11, wrap=tk.NONE, bd=0, padx=2, pady=2)
            estatus_a.insert(tk.END, "")
            estatus_a.place(x=362, y=160)

            #FECHA ESTATUS
            tk.Label(window_alu, text="FECHA ESTATUS:", bg="#1D1212", fg="white").place(x=475, y=160, width=90, height=20)
            festatus_a = tk.Text(window_alu, height=1, width=10, wrap=tk.NONE, bd=0, padx=2, pady=2)
            festatus_a.insert(tk.END, "")
            festatus_a.place(x=570, y=160)

            #Boton cerrar
            boton_cerrar = tk.Button(window_alu, text="Cerrar ventana",bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=window_alu.destroy)
            boton_cerrar.place(x=50, y=300, width=90, height=40)

            #Boton guardar
            boton_guardar = tk.Button(window_alu, text="GUARDAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command= Save_Alum)
            boton_guardar.place(x=150, y=300, width=90, height=40)

            # Cierra la ventana principal
            mostrar_mat_act()
            ventana.withdraw()
        
        #VENTANA ACTUALIZAR REGISTRO CONCEPTO
        def act_Concep():
            def save_Concep():
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
                cursor = conexion.cursor()

                a1 = int(codigo_a.get())
                a2 = concepto_a.get(1.0, tk.END)
                a3 = contable_a.get(1.0, tk.END)
                a4 = costo_a.get(1.0, tk.END)
                a5 = clasificacion_a.get(1.0, tk.END)
                cursor.execute("UPDATE conceptos SET concepto = %s, cuenta_cont = %s, costo = %s, clasif = %s WHERE codigo = %s",
                                (a2, a3, a4, a5, a1))
                messagebox.showinfo("VALIDACION", "DATOS ACTUALIZADOS")
                codigo_a.delete(0, tk.END)
                concepto_a.delete(1.0, tk.END)
                contable_a.delete(1.0, tk.END)
                costo_a.delete(1.0, tk.END)
                clasificacion_a.delete(1.0, tk.END)
                conexion.commit()
                cursor.close()
                conexion.close()

            def obtener_registro_completo_act(llave_primaria):
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

                cursor = conexion.cursor()

                cursor.execute("SELECT * FROM conceptos WHERE codigo = %s", (llave_primaria,))
                registro_completo = cursor.fetchone()

                cursor.close()
                conexion.close()

                return registro_completo

            def accion_al_seleccionar_con(event):
            # Añade más vectores según sea necesario para las demás columnas
                opcion_seleccionada = codigo_a.get()
                # Actualizar el contenido del Label con la opción seleccionada
                #label_resultado.config(text=f"Opción seleccionada: {opcion_seleccionada}")
                if opcion_seleccionada:
                    registro_completo = obtener_registro_completo_act(opcion_seleccionada)
                    if registro_completo:
                        #segun la matricula imprimimos la informacion del alumno
                        entered_text_1 = str(registro_completo[1])#CONCEPTO
                        concepto_a.config(state=tk.NORMAL)
                        concepto_a.delete(1.0, tk.END)
                        concepto_a.insert(tk.END, f"{entered_text_1}")

                        entered_text_2 = str(registro_completo[2])#CUENTA CONTABLE
                        contable_a.config(state=tk.NORMAL)
                        contable_a.delete(1.0, tk.END)
                        contable_a.insert(tk.END, f"{entered_text_2}")

                        entered_text_3 = str(registro_completo[3])#COSTO
                        costo_a.config(state=tk.NORMAL)
                        costo_a.delete(1.0, tk.END)
                        costo_a.insert(tk.END, f"{entered_text_3}")

                        entered_text_4 = str(registro_completo[4])#CLASIFICACION
                        clasificacion_a.config(state=tk.NORMAL)
                        clasificacion_a.delete(1.0, tk.END)
                        clasificacion_a.insert(tk.END, f"{entered_text_4}")
                    else:
                        print("Registro no encontrado.")

            def obtener_mat_bd_con():
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
                cursor.execute("SELECT * FROM conceptos")
                matris = cursor.fetchall()

                # Cerrar la conexión y el cursor
                cursor.close()
                conexion.close()

                return matris

            def on_key_release_con(event):
                    number = mostrar_mat_con()
                    try:
                        value = int(combobox_con.get())
                        filtered_values = [item for item in number if str(value) in str(item)]

                    except ValueError:
                        filtered_values = []

                    codigo_a['values'] = filtered_values

            def mostrar_mat_con():
                # Obtener las opciones de la base de datos
                opciones_bd_mat1 = obtener_mat_bd_con()
                # Limpiar el ComboBox
                codigo_a['values'] = ()
                # Configurar las nuevas opciones en el ComboBox
                codigo_a['values'] = [opcion[0] for opcion in opciones_bd_mat1]
                number_list = codigo_a['values'] = [opcion[0] for opcion in opciones_bd_mat1]
                

                return number_list

            # Crear una ventana secundaria.
            window_con = tk.Toplevel()
            #color de fondo BG
            window_con.config(bg="#1D1212")
            #se le añade un titulo a la app
            window_con.title("ACTUALIZAR REGISTRO CONCEPTOS")
            window_con.config(width=1080, height=600)

            #CODIGO
            combobox_con = tk.StringVar()
            tk.Label(window_con, text="CODIGO:", bg="#1D1212", fg="white").place(x=40, y=70, width=80, height=20)
            codigo_a = ttk.Combobox(window_con, width=20, textvariable=combobox_con)
            #codigo_a = ctk.ComboBox(window_con, width=50)
            codigo_a.place(x=135, y=70)
            # Vincular la función al evento <<ComboboxSelected>>
            codigo_a.bind("<<ComboboxSelected>>", accion_al_seleccionar_con)
            codigo_a.bind('<KeyRelease>', on_key_release_con)

            #CONCEPTO
            tk.Label(window_con, text="CONCEPTO:", bg="#1D1212", fg="white").place(x=50, y=100, width=80, height=20)
            concepto_a = tk.Text(window_con, height=1, width=25, wrap=tk.NONE, bd=0, padx=2, pady=2)
            concepto_a.place(x=135, y=100)
            concepto_a.insert(tk.END, "")

            #CUENTA CONTABLE 
            tk.Label(window_con, text="CUENTA CONTABLE:", bg="#1D1212", fg="white").place(x=350, y=100, width=120, height=20)
            contable_a = tk.Text(window_con, height=1, width=3, wrap=tk.NONE, bd=0, padx=2, pady=2)
            contable_a.place(x=475, y=100)
            contable_a.insert(tk.END,"")

            #COSTO
            tk.Label(window_con, text="COSTO:", bg="#1D1212", fg="white").place(x=520, y=100, width=75, height=20)
            costo_a = tk.Text(window_con, height=1, width=8, wrap=tk.NONE, bd=0, padx=2, pady=2)
            costo_a.place(x=585, y=100)
            costo_a.insert(tk.END, "")

            #CLASIFICACION
            tk.Label(window_con, text="CLASIFICACION:", bg="#1D1212", fg="white").place(x=50, y=130, width=100, height=20)
            clasificacion_a = tk.Text(window_con, height=1, width=15, wrap=tk.NONE, bd=0, padx=2, pady=2)
            clasificacion_a.place(x=160, y=130)
            clasificacion_a.insert(tk.END, "")

            #Boton cerrar
            boton_cerrar = tk.Button( window_con, text="Cerrar ventana",bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=window_con.destroy)
            boton_cerrar.place(x=50, y=200, width=90, height=40)
            #Boton Guardar
            boton_guardar = tk.Button(window_con, text="GUARDAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=save_Concep)
            boton_guardar.place(x=150, y=200, width=90, height=40)
            # Cierra la ventana principal
            mostrar_mat_con()
            ventana.withdraw()
            
        # Crear una ventana secundaria.
        window_act = tk.Toplevel()
        #color de fondo BG
        window_act.config(bg="#1D1212")
        #se le añade un titulo a la app
        window_act.title("ACTUALIZAR REGISTROS")
        window_act.config(width=500, height=300)
                
        # Crear un botón dentro de la ventana secundaria
         # para cerrar la misma.
        btn_Alumnos_act = tk.Button(
            window_act,
            text="Actualizar Alumnos", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=act_Alum
         )
        btn_Conceptos_act = tk.Button(
            window_act,
            text="Actualizar Conceptos", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=act_Concep
        )
        btn_venta_act = tk.Button(
            window_act,
            text="Actualizar Venta", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=act_Concep
        )
        btn_cerrar_act = tk.Button(
            window_act,
            text="Cerrar ventana", 
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=window_act.destroy
        )
        
        btn_cerrar_act.place(x=50, y=100, width=90, height=40)
        btn_Alumnos_act.place(x=150, y=100, width=145, height=40)
        btn_Conceptos_act.place(x=310, y=100, width=150, height=40)
        btn_venta_act.place(x=50, y=150, width=150, height=40)
        # Cierra la ventana principal
        ventana.withdraw()

   #VENTANA PARA CONSULTAR
    def Consultar():
        ventana_consul=tk.Tk()
        #color de fondo BG
        ventana_consul.config(bg="#1D1212")
        #se le añade un titulo a la app
        ventana_consul.title("CONSULTA DE REGISTROS")
        ventana_consul.geometry("1200x600")

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
                    #conexion a la BD
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
                    #conexion a la BD
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
        btn_Alumnos = tk.Button(ventana_consul, text="Consultar Alumnos", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=Consu_Alum)
        btn_Conceptos = tk.Button(ventana_consul,text="Consultar Conceptos",bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=Consu_Concep)
        boton_regresar = tk.Button(ventana_consul,text="REGRESAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=lambda:close_window(ventana_consul))

        boton_regresar.place(x=50, y=400, width=90, height=40)
        btn_Alumnos.place(x=150, y=400, width=120, height=40)
        btn_Conceptos.place(x=280, y=400, width=125, height=40)

    def close_window(window):
        # Cierra la ventana principal
        WIND.withdraw()
        window.destroy()
        WIND.deiconify()
        
    def Insertar():
        def import_data_con():
            user4= e1.get()
            passw4 = e2.get()
            table_n1='conceptos'
            try:
                # Abrir el cuadro de diálogo para seleccionar el archivo Excel o CSV
                file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls"), ("Archivos CSV", "*.csv")])

                # Leer el archivo con pandas
                if file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)

                # Establecer la conexión a la base de datos PostgreSQL
                engine = create_engine(f"postgresql://{user4}:{passw4}@localhost:5432/sistema")

                # Insertar los datos en la tabla existente (reemplaza "mi_tabla" con el nombre de tu tabla)
                df.to_sql(table_n1, con=engine, if_exists="append", index=False)

                # Mostrar una alerta de éxito
                messagebox.showinfo("Éxito", "Datos importados correctamente.")

            except Exception as e:
                # Mostrar una alerta de error
                messagebox.showerror("Error", f"Error al importar datos:\n{str(e)}")

        # Función para importar datos a PostgreSQL
        def import_data_to_postgres():
            user4= e1.get()
            passw4 = e2.get()
            table_n1='alumnos'
            try:
                # Abrir el cuadro de diálogo para seleccionar el archivo Excel o CSV
                file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls"), ("Archivos CSV", "*.csv")])

                # Leer el archivo con pandas
                if file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)

                # Establecer la conexión a la base de datos PostgreSQL
                engine = create_engine(f"postgresql://{user4}:{passw4}@localhost:5432/sistema")

                # Insertar los datos en la tabla existente (reemplaza "mi_tabla" con el nombre de tu tabla)
                df.to_sql(table_n1, con=engine, if_exists="append", index=False)

                # Mostrar una alerta de éxito
                messagebox.showinfo("Éxito", "Datos importados correctamente.")

            except Exception as e:
                # Mostrar una alerta de error
                messagebox.showerror("Error", f"Error al importar datos:\n{str(e)}")

        # Crear una ventana secundaria.
        ventana_INSERTAR = tk.Toplevel()
        #color de fondo BG
        ventana_INSERTAR.config(bg="#1D1212")
        #se le añade un titulo a la app
        ventana_INSERTAR.title("INSERTAR REGISTROS")
        ventana_INSERTAR.config(width=500, height=300)
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        btn_Alumnos_insert = tk.Button(
            ventana_INSERTAR,
            text="Insertar Nuevos Alumnos",
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=lambda: import_data_to_postgres()
        )
        btn_Conceptos_insert = tk.Button(
            ventana_INSERTAR,
            text="Insertar Nuevo Conceptos",
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5,
            command=lambda: import_data_con()
        )
        btn_cerrar_insert = tk.Button(
            ventana_INSERTAR,
            text="Cerrar ventana",
            bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, 
            command=ventana_INSERTAR.destroy
        )

        btn_cerrar_insert.place(x=50, y=150, width=90, height=40)
        btn_Alumnos_insert.place(x=150, y=150, width=145, height=40)
        btn_Conceptos_insert.place(x=310, y=150, width=150, height=40)

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
        GRUP = grup.get()
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
            grup.delete(0, tk.END)
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

        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alumnos WHERE Matricula = %s", (llave_primaria,))
        registro_completo = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro_completo
    
    def obtener_registro_completo_concep(OPCC):
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

            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM conceptos WHERE concepto = %s", (OPCC,))
            RC = cursor.fetchone()

            cursor.close()
            conexion.close()

            return RC
    
    def accion_al_seleccionar_matInicial(event):
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
                grup.config(text=str(registro_completo[5]))
                lice.config(text=str(registro_completo[3]))
            else:
                print("Registro no encontrado.")

    def opc_con1(event):
         # Vectores para almacenar los valores
        cod = []
        conce = []
        cuen_con = []
        pressc =[]
        clasi =[]
    # Añade más vectores según sea necesario para las demás columnas
        opcion_seleccionada = str(conc1.get())
        # Actualizar el contenido del Label con la opción seleccionada
        #label_resultado.config(text=f"Opción seleccionada: {opcion_seleccionada}")
        if opcion_seleccionada:
            registro_completo = obtener_registro_completo_concep(opcion_seleccionada)
            registro_formateado = ', '.join(map(str, registro_completo))
            if registro_completo:
                # Almacena cada valor del registro en vectores
                Codigo, concepto, cuenta_con,precio, clasificac = registro_completo
                cod.append(Codigo)
                conce.append(concepto)
                cuen_con.append(cuenta_con)
                pressc.append(precio) 
                clasi.append(clasificac)
                # Formatea la cadena antes de imprimir
                registro_formateado = ', '.join(map(str, registro_completo))
                #segun la matricula imprimimos la informacion del alumno
                impo1.config(text=str(registro_completo[3]))
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
        
        vector1=[]
        vector1=[opcion[0] for opcion in opciones_bd_mat] 
        
        #mat.configure(values=[opcion[0] for opcion in opciones_bd_mat])

    #FUNCION PARA ACTUALIZAR LA HORA
    def times():
        current_time=time.strftime("%H:%M:%S") 
        clock.config(text=current_time, bg='#1D1212' ,fg="white",font="Candara 40 bold")
        clock.after(200,times)

    #VENTANA PRINCIPAL
    WIND = tk.Toplevel(ventana)
    #tamaño de la ventana
    WIND.geometry("1300x768")
    #color de fondo BG
    WIND.config(bg="#1D1212")
    #se le añade un titulo a la app
    WIND.title("SISTEMA DE COBROS")

    #LOGO
    WIND.iconbitmap("img/LG.ico")
    #la metemos dentro de un label para poder mostrarla
    eti= Label(WIND, image = img1, bg='#1D1212')
    #eti = tk.Label(WIND, image=imagen_sub)
    eti.place(x=20, y=10)

    #Formulario Crear los widgets del formulario
    tk.Label(WIND, text="PAQUETES DE GRADUACION", font="Candara 24 bold", bg='#1D1212', fg="#4169e1", width=0, height=3).place(x=800, y=0)

    #HORA EN TIEMPO REAL
    clock=Label(WIND,font=("Candara",50,"bold"))
    clock.place(x=950, y=80)
    times()

    #USUARIO
    user1 = e1.get()
    user = tk.Label(WIND, text= user1, bg="#1D1212", bd=3, fg="white", font="Candara 20 bold" )
    user.place(x=850, y=185, width=150)
        
    #FOLIO
    tk.Label(WIND, text="FOLIO:", bg="#565151", fg="white", relief=tk.GROOVE, bd=3, font="Candara 16 bold").place(x=500, y=60, width=70, height=30)
    folio = tk.Entry(WIND, relief=tk.SUNKEN, bd=3, font="Candara 14 bold")
    folio.place(x=600, y=60, width=100, height=30)

    #MATRICULA
    opciones_bd_mat = obtener_mat_bd()
    tk.Label(WIND,text="MATRICULA:", bg="#565151", fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold").place(x=50, y=150, width=100, height=25)
    mat = ttk.Combobox(WIND, width=30, font="Candara 12 bold")
    vector1=[]
    vector1=[opcion[0] for opcion in opciones_bd_mat] 
    #mat = CTkComboBox(WIND, values=[""])
    mat.place(x=160, y=150, width=110, height=25)
    # Vincular la función al evento <<ComboboxSelected>>
    mat.bind("<<ComboboxSelected>>", accion_al_seleccionar_matInicial)
    
    #NOMBRE DEL ALUMNO
    tk.Label(WIND,text="NOMBRE DEL ALUMNO:", bg="#565151", fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold").place(x=280, y=150, width=185, height=25)
    nom = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=30, bg="white", font="Candara 11 bold")
    nom.place(x=475, y=150, width=350, height=25)

    #LICENCIATURA
    tk.Label(WIND, text="LICENCIATURA:", bg="#565151", fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold").place(x=50, y=185, width=125, height=25)
    lice = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=42, bg="white", font="Candara 11 bold")
    lice.place(x=185, y=185, width=395, height=25)

    #GRUPO
    tk.Label(WIND, text="GRUPO:", bg="#565151", fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold").place(x=590, y=185, width=70, height=25)
    grup = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=18, bg="white", font="Candara 11 bold")
    grup.place(x=675, y=185, width=150, height=25)

    #PLANTEL
    tk.Label(WIND, text="PLANTEL:", bg="#565151",fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold" ).place(x=50, y=225, width=80, height=25)
    plan = tk.Label(WIND,relief=tk.SUNKEN, bd=3, width=19, bg="white", font="Candara 11 bold")
    plan.place(x=140, y=225, width=160, height=25)

    #FECHA
    tk.Label(WIND, text="FECHA:", bg="#565151",fg="white", relief=tk.GROOVE, bd=3, font="Candara 12 bold").place(x=320, y=225, width=70, height=25)
    dateUno = tk.Label(WIND, text=date.today(), bg="#1D1212", bd=3,fg="white", font="Candara 11 bold")
    date1 = date.today()
    dateUno.place(x=400, y=225, width=70, height=25)

    tk.Label(WIND, text="CONCEPTOS", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=100, y=265, width=95, height=25)
    #INICIAN LOS CONCEPTOS
    conc1 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc1.place(x=50, y=305, width=200, height=25)
    # Vincular la función al evento <<ComboboxSelected>>
    conc1.bind("<<ComboboxSelected>>", opc_con1)
    conc2 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc2.place(x=50, y=335, width=200, height=25)
    conc3 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc3.place(x=50, y=365, width=200, height=25)
    conc4 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc4.place(x=50, y=395, width=200, height=25)
    conc5 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc5.place(x=50, y=425, width=200, height=25)
    conc6 = ttk.Combobox(WIND, width=27, font="Candara 11 bold")
    conc6.place(x=50, y=455, width=200, height=25)
    conc7 = ttk.Combobox(WIND, width=27,font="Candara 11 bold")
    conc7.place(x=50, y=485, width=200, height=25)
    #IMPORTE
    tk.Label(WIND, text="IMPORTE", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=270, y=265, width=79, height=25)
    impo1 = tk.Label(WIND, text="", relief=tk.SUNKEN, width=10,bg="white", bd=3)
    impo1.place(x=270, y=305, width=79, height=25)
    impo2 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white", font="Candara 11 bold")
    impo2.place(x=270, y=335, width=79, height=25)
    impo3 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    impo3.place(x=270, y=365, width=79, height=25)
    impo4 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white", font="Candara 11 bold")
    impo4.place(x=270, y=395, width=79, height=25)
    impo5 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3,bg="white", font="Candara 11 bold")
    impo5.place(x=270, y=425, width=79, height=25)
    impo6 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white",font="Candara 11 bold")
    impo6.place(x=270, y=455, width=79, height=25)
    impo7 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    impo7.place(x=270, y=485, width=79, height=25)
    #%
    tk.Label(WIND, text="%",  bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=380, y=265, width=30, height=25)
    combo1 = ttk.Combobox(WIND,state="normal",font="Candara 11 bold",values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo1.place(x=370, y=305, width=50, height=23)

    combo2 = ttk.Combobox(WIND,state="normal",font="Candara 11 bold",values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo2.place(x=370, y=335, width=50, height=23)

    combo3 = ttk.Combobox(WIND,state="normal",font="Candara 11 bold",values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo3.place(x=370, y=365, width=50, height=23)

    combo4 = ttk.Combobox(WIND,state="normal",font="Candara 11 bold",values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo4.place(x=370, y=395, width=50, height=23)

    combo5 = ttk.Combobox(WIND,state="normal",font="Candara 11 bold",values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo5.place(x=370, y=425, width=50, height=20)

    combo6 = ttk.Combobox(WIND, state="normal", font="Candara 11 bold", values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo6.place(x=370, y=455, width=50, height=23)

    combo7 = ttk.Combobox(WIND, state="normal", font="Candara 11 bold", values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    combo7.place(x=370, y=485, width=50, height=23)
    #RECARGOS
    tk.Label(WIND, text="RECARGOS:", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=445, y=265, width=85, height=25)

    rec1 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec1.place(x=465, y=305, width=50, height=24)

    rec2 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec2.place(x=465, y=335, width=50, height=24)

    rec3 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec3.place(x=465, y=365, width=50, height=24)

    rec4 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec4.place(x=465, y=395, width=50, height=24)

    rec5 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec5.place(x=465, y=425, width=50, height=24)

    rec6 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec6.place(x=465, y=455, width=50, height=24)

    rec7 = tk.Entry(WIND, width=10, relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    rec7.place(x=465, y=485, width=50, height=24)

    #SUBTOTAL
    tk.Label(WIND, text="SUBTOTAL:", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=560, y=265, width=90, height=25)
    subt1 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt1.place(x=575, y=305,width=60, height=25)

    subt2 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt2.place(x=575, y=335, width=60, height=25)

    subt3 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt3.place(x=575, y=365, width=60, height=25)

    subt4 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt4.place(x=575, y=395, width=60, height=25)

    subt5 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white",font="Candara 11 bold")
    subt5.place(x=575, y=425, width=60, height=25)

    subt6 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt6.place(x=575, y=455, width=60, height=25)

    subt7 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold")
    subt7.place(x=575, y=485, width=60, height=25)

    #TOTAL A PAGAR
    tk.Label(WIND, text="TOTAL:", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=720, y=265, width=70, height=25)
    total1 = tk.Label(WIND, width=10,relief=tk.SUNKEN, bd=3, bg="white", font="Candara 11 bold").place(x=715, y=295, width=79, height=25)

    #CANTIDAD QUE RECIBE
    cant_res = tk.Label(WIND, text="CANTIDAD QUE RECIBE", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=675, y=340, width=165, height=25)
    cant_res = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3,font="Candara 11 bold" )
    cant_res.place(x=705, y=370, width=105, height=25)

    #CAMBIO
    cambio = tk.Label(WIND, text="CAMBIO", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=720, y=410, width=70, height=25)
    cambio = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    cambio.place(x=700, y=440, width=105, height=25)

    #FORMA DE PAGO
    tk.Label(WIND, text="FORMA DE PAGO", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=865, y=265, width=140, height=25)
    formP = ttk.Combobox( WIND, state="normal",font="Candara 11 bold", values=["Efectivo", "Tarjeta de Credito", "Tarjeta de Debito", "Cheque", "Deposito Bancario"])
    formP.place(x=880, y=295, width=105, height=25)

    #APROVACION
    aprov = tk.Label(WIND, text="APROVACIÓN", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=875, y=340, width=120, height=25)
    aprov = tk.Entry(WIND, width=25,relief=tk.SUNKEN, bd=3, font="Candara 11 bold")
    aprov.place(x=885, y=370, width=105, height=25)

    #CUENTA RECEPTORA
    cuenta_res = tk.Label(WIND, text="CUENTA RECEPTORA", bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=865, y=410, width=152, height=25)
    cuenta_res = ttk.Combobox(WIND,state="readonly",values=["Santander", "No aplica"], font="Candara 11 bold")
    cuenta_res.place(x=883, y=440, width=105, height=25)

    #OBSERVACIONES
    tk.Label(WIND, text="OBSERVACIONES:",  bg="#565151", relief=tk.GROOVE, bd=3, fg="white", font="Candara 12 bold").place(x=50, y=525, width=137, height=25)
    observ = tk.Entry(WIND, width=30,relief=tk.SUNKEN,font="Candara 11 bold")
    observ.place(x=200, y=525, width=620, height=25)

    #BOTONES
    boton_enviar = tk.Button(WIND, text="REGISTRAR", bg="#00D903", fg="white", relief=tk.RAISED, bd=5, command=enviar_datos)
    boton_enviar.place(x=875, y=525, width=100, height=30)

    btn_Consultar = tk.Button(WIND, text="CONSULTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5, command=Consultar)
    btn_Consultar.place(x=210, y=600, width=100, height=30)

    btn_Insert = tk.Button(WIND, text="INSERTAR", bg="#0020BE", fg="white", relief=tk.RAISED, bd=5,command=Insertar)
    btn_Insert.place(x=330, y=600, width=100, height=30)

    btn_Actualizar = tk.Button(WIND, text="ACTUALIZAR", bg="#FF8F00", fg="white", relief=tk.RAISED, bd=5, command=actualizar)
    btn_Actualizar.place(x=460, y=600, width=100, height=30)

    btn_eliminar = tk.Button(WIND, text="ELIMINAR", bg="#FF0000", fg="white", relief=tk.RAISED, bd=5, command=eliminar)
    btn_eliminar.place(x=580, y=600, width=100, height=30)

    # Llamar a las funciones al inicio
    mostrar_opciones_combo()
    mostrar_mat()
    # Cierra la ventana principal
    ventana.withdraw()
#LOGIN
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
ventana.config(bg="#1D1212")
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
l1=Label(ventana, text="USER",font=("Candara", 20, "bold"), bg="#1D1212", fg="white").grid(row=2, column=1, pady=5,columnspan=4)
e1 = Entry(ventana, font=30, relief=SOLID)
e1.grid(row=3, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar

#CONTRASEÑA ENTRADA 
l2 = Label(ventana, text="PASSWORD", font=("Candara", 20, "bold"), bg="#1D1212", fg="white").grid(row=4, column=1, pady=5, columnspan=4)
e2 = Entry(ventana, font=30, show='*', relief=SOLID)
e2.grid(row=5, column=1, pady=5, columnspan=4)
ventana.grid_columnconfigure(1, weight=2)  # Ajusta el peso de la columna para centrar
# Asocia la tecla Enter a la función Evalue
e2.bind("<Return>", lambda event: Evalue())

# IMAGEN adding image (remember image should be PNG and not JPG)
img = PhotoImage(file='img/LOGO_TRANSPARENTE.png')
img1 = img.subsample(2, 2)
Label(ventana,image=img1, bg="#1D1212").grid(row=1, column=1, pady=10, columnspan=4)
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
eye_button.config(image=close_eye, bd=0, bg="white")
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
