import tkinter as tk

from tkinter import ttk

from tkinter import messagebox

from tkinter import *
import subprocess
# ============================================DEFINIR LA FINCION DE salirAplicacion=======================================================================



def salirAplicacion():

    valor = messagebox.askquestion('Clan del Cuervo - Salir', '¿Deseas salir de la aplicación?')

    if valor == 'yes':

        root.destroy()

# ===================================================================================================================


# ============================================DEFINIR LA FINCION DE abrirVentanaProyectos=======================================================================
def abrirVentanaProyectos():

    ventana_proyectos = tk.Toplevel(root)

    ventana_proyectos.title("CDC - Proyectos")
    ventana_proyectos.iconbitmap("img/clan.ico")

    ventana_proyectos.geometry("300x200")

    ventana_proyectos.configure(background="#0D1332")

    ventana_proyectos.resizable(0, 0)
    
    label_proyectos = tk.Label(ventana_proyectos, text="Lista de Proyectos", bg="#0D1332", fg='white')

    label_proyectos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    proyecto1 = tk.Label(ventana_proyectos, text="1. Hacer una página web del C.D.C", bg="#0D1332", fg='white')

    proyecto1.grid(row=1, column=0, sticky='w', padx=10)
    
    proyecto2 = tk.Label(ventana_proyectos, text="2. Llegar a 50 suscriptores en YouTube", bg="#0D1332", fg='white')

    proyecto2.grid(row=2, column=0, sticky='w', padx=10)
# ===================================================================================================================

# ============================================DEFINIR LA FINCION DE acerca_de======================================================================
def acerca_de():

    mensaje = """
    
    Versión: 0.1

    Autor: Vicepresidente del Clan

    Fecha: Viernes 22 de Septiembre de 2023 22:28

    """
    messagebox.showinfo('Clan del Cuervo - Acerca de', mensaje)
# ===================================================================================================================

# ============================================DEFINIR LA FINCION DE contacto=======================================================================

def contacto():

    messagebox.showinfo("Contacto del Clan del Cuervo", "clandelcuervolgn@gmail.com")

root = tk.Tk()

root.title("Clan Del Cuervo - 2023")

root.resizable(0,0)

root.iconbitmap("img\clan.ico")


root.geometry("1008x469")

root.config(bg="#0D1332")
# ===================================================================================================================














barraMenu = tk.Menu(root)

root.config(menu=barraMenu)

# ============================================MENU-SALIR====================================================================
archivoMenu = tk.Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label='Salir', command=salirAplicacion)
# ================================================================================================================

# ===========================================MENU-PROYECTOS=====================================================================
archivoMas = tk.Menu(barraMenu, tearoff=0)

archivoMas.add_command(label="Proyectos", command=abrirVentanaProyectos)
# ================================================================================================================

# ============================================MENU DE ACRCA DE.. Y CONTACTO====================================================================
archivoAyuda = tk.Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label='Acerca de..', command=acerca_de)

archivoAyuda.add_command(label='Contacto', command=contacto)
# ================================================================================================================

# ============================================MENU DE APLICACION, MAS, AYUDA====================================================================
barraMenu.add_cascade(label="Aplicación", menu=archivoMenu)

barraMenu.add_cascade(label="Más", menu=archivoMas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
# ================================================================================================================


# ============================================DEFINIR LA FUNCION DE mostrar_niveles====================================================================
def mostrar_niveles():

    ventana_emergente = Toplevel(root)

    ventana_emergente.title("CDC-NIVELES")

    ventana_emergente.iconbitmap("img/clan.ico")

    # Establecer el tamaño de la ventana emergente usando geometry
    ventana_emergente.geometry("400x200")  # Ancho x Alto en píxeles
    texto = """
● Presidente
● Vicepresidente
● Paladín Jefe
● Paladín
● Centinela
● Caballero
● Iniciado
"""

    texto_niveles = Text(ventana_emergente, wrap=tk.WORD)

    texto_niveles.insert(tk.END, texto)

    texto_niveles.config(font=("Arial", 12),background="#0D1332", foreground='white',padx=20,pady=20,state=tk.DISABLED )

    texto_niveles.pack(expand=True, fill=tk.BOTH)
# ================================================================================================================



# ============================================definir la funcion de  donde estamos====================================================================
def donde_estamos():

    donde_estamos= tk.Toplevel(root)

    donde_estamos.title("CDC - DÓNDE ESTAMOS")
    donde_estamos.iconbitmap("img/clan.ico")

    donde_estamos.geometry("400x200")

    donde_estamos.configure(background="#0D1332")

    donde_estamos.resizable(0, 0)
    
    label_DONDE_ESTAMOS = tk.Label(donde_estamos, text="sitios webs donde estamos,España", bg="#0D1332", fg='white')

    label_DONDE_ESTAMOS.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    proyecto1 = tk.Label(donde_estamos, text="1.youtube:https://www.youtube.com/@CLAN_DEL_CUERVO", bg="#0D1332", fg='white')

    proyecto1.grid(row=1, column=0, sticky='w', padx=10)
    
    proyecto2 = tk.Label(donde_estamos, text="2.github:https://github.com/Clan-Del-Cuervo-ESP", bg="#0D1332", fg='white')

    proyecto2.grid(row=2, column=0, sticky='w', padx=10)

    proyecto3 = tk.Label(donde_estamos, text="3.istagram:https://www.instagram.com/clan_del_cuervo_logrono_/", background='#0D1332', fg='white')

    proyecto3.grid(row=3 , column=0,sticky='w', padx=10 ,)



def que_somos_():
    # Crear una ventana secundaria
    ventana_que_somos = tk.Toplevel()
    ventana_que_somos.title("CDC - QUE SOMOS")
    ventana_que_somos.geometry("400x200")
    ventana_que_somos.iconbitmap("img/clan.ico")
    ventana_que_somos.configure(background="#0D1332")
    ventana_que_somos.resizable(0, 0)

    texto = """
    Somos un grupo que ayuda a gente
    No somos muchos por ahora, pero en un futuro seremos más
    Contacto: clandelcuervolgn@gmail.com"""

    somos_frame = tk.Frame(ventana_que_somos, bg="#0D1332")
    somos_frame.pack(fill="both", expand=True)

    mensaje = tk.Label(somos_frame, text=texto, bg="#0D1332", fg='white')
    mensaje.grid(row=0, column=0, sticky='w', padx=10)




def abrir_calculadora():
    subprocess.run(["python", "cdc_calculator_.pyw"])

def como_subir_de_nivel():

    messagebox.showinfo("CDC-cómo-subir-de-nivel", 
 """1-ayuda a gente
    2-habla con el jefe o los vicepresidentes""")



def mas_opciones():
    # Crear una ventana secundaria

    ventana_opciones = Toplevel()

    ventana_opciones.config(background="#0D1332")
    ventana_opciones.iconbitmap("img/clan.ico")

    ventana_opciones.title("CDC-Más Opciones")
    ventana_opciones.geometry('430x240')

    # Crear un menú
    menu = tk.Menu(ventana_opciones)
   
    ventana_opciones.config(menu=menu)

    # Crear elementos de menú

    archivo_menu = Menu(menu,tearoff=0)  # Añadir tearoff aquí
    archivo_menu = tk.Menu(menu)
    menu.add_cascade(label="Archivo", menu=archivo_menu,)
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=ventana_opciones.destroy)

    # Crear botones y usar grid para disposición
    boton1 = tk.Button(ventana_opciones, text="Abrir calculadora del CDC", command=abrir_calculadora)
    boton1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    
    boton2 = tk.Button(ventana_opciones, text="Cómo subir de nivel", command=como_subir_de_nivel)
    boton2.grid(row=1, column=0, padx=10, pady=5, sticky='w')
 


donde_estamos






















# ===========================================CREAR UN BOTON-DE-NIVELES=====================================================================
# Crear un estilo personalizado para el primer botón
estilo_niveles = ttk.Style()
estilo_niveles.configure("Niveles.TButton", foreground="black", background="#0D1332", font=("Arial", 12), padding=10)

# Crear el primer botón con el estilo personalizado
boton_niveles = ttk.Button(root, text="Niveles", style="Niveles.TButton", command=mostrar_niveles)
boton_niveles.grid(row=0, padx=12, pady=30)
# ================================================================================================================



# ============================================CREAR UN BOTON-DE-DONDE ESTAMOS====================================================================
# Crear un estilo personalizado para el segundo botón
estilo_donde_estamos = ttk.Style()
estilo_donde_estamos.configure("DondeEstamos.TButton", foreground="black", background="#0D1332", font=("Arial", 12), padding=10)

# Crear el segundo botón con el estilo personalizado
boton_donde_estamos = ttk.Button(root, text="Dónde estamos", style="DondeEstamos.TButton", command=donde_estamos)
boton_donde_estamos.grid(row=1, padx=10, pady=10)
# ================================================================================================================


# ============================================CREAR UN BOTON-DE-QUE-SOMOS====================================================================
que_somos = ttk.Style()
que_somos.configure("quesomos.TButton", foreground="black", background="#0D1332", font=("Arial", 12), padding=10)

# Crear el segundo botón con el estilo personalizado
que_somos = ttk.Button(root, text="Qué somos", style="quesomos.TButton", command=que_somos_)
que_somos.grid(row=2, padx=10, pady=10)
# ================================================================================================================


# ============================================CREAR UN BOTON-DE-MAS OPCIONES====================================================================
masOPciones = ttk.Style()
masOPciones.configure("masOPciones.TButton", foreground="black", background="#0D1332", font=("Arial", 12), padding=10)


# Crear el segundo botón con el estilo personalizado
masOPciones = ttk.Button(root, text="Más opciones", style="masOPciones.TButton", command=mas_opciones)
masOPciones.grid(row=3, column=0, padx=10, pady=10)
# ================================================================================================================



# # ===========================================PONE UNA IMG=====================================================================
 # Cargar la imagen para el fondo (reemplaza "imagen.png" con la ruta de tu propia imagen)
imagen_fondo = tk.PhotoImage(file="img/icon-1-niveles.png")

# # Crear una etiqueta con la imagen como fondo
fondo = tk.Label(root, image=imagen_fondo)
fondo.grid(row=0,column=2)
# # # ================================================================================================================

# # ============================================2PONE UNA IMG====================================================================
# # Cargar la imagen para el fondo (reemplaza "imagen.png" con la ruta de tu propia imagen)
imagen_fondo_ = tk.PhotoImage(file="img/donde_estamos.png")
imagen_fondo_.config( height=70)

# # Crear una etiqueta con la imagen como fondo
fondo_ = tk.Label(root, image=imagen_fondo_)
fondo_.grid(row=1,column=2)
# # ================================================================================================================
root.mainloop()