from tkinter import *
import subprocess
from tkinter import messagebox

def accion_del_boton():
    subprocess.run(["python", "clan_del_cuervo.pyw"])

def mostrar_version():
    messagebox.showinfo("Versión", "Versión de la aplicación: 0.1")

root = Tk()
root.config(background="#0D1332")
root.resizable(0, 0)
root.title("CLAN DEL CUERVO")
root.geometry("240x200")

menu_bar = Menu(root)
root.iconbitmap("img/clan.ico")
root.config(menu=menu_bar)

archivo_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Versión", command=mostrar_version)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

labeltext = Label(root, text="CLAN DEL CUERVO")
labeltext.config(background="#0D1332", foreground="white")
labeltext.grid(row=0, column=0, padx=70, pady=20)

boton_abrir = Button(root, text="Empezar", command=accion_del_boton)
boton_abrir.grid(row=1, column=0, padx=10, pady=20)

root.mainloop()
