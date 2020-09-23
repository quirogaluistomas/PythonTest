from tkinter import *

root = Tk()

varOpcion = IntVar()

def imprimir():

    #print(varOpcion.get())

    if varOpcion.get() == 1:
        Etiqueta.config(text = "Has elegido masculino")
    elif varOpcion.get() == 2:
        Etiqueta.config(text = "Has elegido femenino")
    else:
        Etiqueta.config(text = "Has elegido otras opciones")
    

Label(root, text= "Género: ").pack()

#Creo que si en vez de no poner () al llamado imprimir le ponemos
#lambda funca igual.

Radiobutton(root, text = "Masculino", variable = varOpcion, value = 1, command = imprimir).pack()
Radiobutton(root, text = "Femenino", variable = varOpcion, value = 2, command = imprimir).pack()
Radiobutton(root, text = "Otras opciones", variable = varOpcion, value = 3, command = imprimir).pack()
Etiqueta = Label(root)
Etiqueta.pack()

root.mainloop()