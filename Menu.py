from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional(): #Creamos la funcion que crea la ventana
    messagebox.showinfo("Procesador de Lucho", "Procesador de texto 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencua GNU")

def salirAplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la app?")
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la app?")
    #if valor == "yes":
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar")
    if valor == False:
        root.destroy()

barraMenu = Menu(root) #Se crea el tipo "Menu"
root.config(menu = barraMenu, width = 300, height = 300) #Se le indica en la raiz que es un menu

archivoMenu = Menu(barraMenu, tearoff = 0) #Le digo a qué menu pertenece
archivoMenu.add_command(label = "Nuevo archivo")
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar como..")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label = "Salir", command = salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas = Menu(barraMenu, tearoff = 0)

archivoAyuda = Menu(barraMenu, tearoff = 0)
archivoAyuda.add_command(label = "Licencia", command = avisoLicencia)
archivoAyuda.add_command(label = "Acerca de..", command = infoAdicional)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)

barraMenu.add_cascade(label = "Edición", menu = archivoEdicion)

barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)

barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)

root.mainloop()