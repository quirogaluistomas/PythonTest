from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack() #Meto el frame en el root. No respeta dimensiones que le indicamos

miNombre = StringVar() #indico que es un tipo string

cuadroNombre = Entry(miFrame, textvariable = miNombre) #Indico donde irá el cuatro de texto (en el frame)
cuadroNombre.grid(row = 0, column = 1, padx = 10, pady = 10) #Ubico el entry en una grilla, mejor que coordenadas
cuadroNombre.config(fg = "red", justify = "center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 3, column = 1, padx = 10, pady = 10)

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 4, column = 1, padx = 10, pady = 10)

scrollVert = Scrollbar(miFrame, command = textoComentario.yview)
scrollVert.grid(row = 4, column = 2, sticky = "nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 10)

PassLabel = Label(miFrame, text = "Password: ")
PassLabel.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)

ApellidoLabel = Label(miFrame, text = "Apellido: ")
ApellidoLabel.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)

DireccionLabel = Label(miFrame, text = "Dirección: ")
DireccionLabel.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 10)

ComentariosLabel = Label(miFrame, text = "Comentarios: ")
ComentariosLabel.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10)

def codigoBoton():

    miNombre.set("Juan")

botonEnvio = Button(raiz, text = "Enviar", command = codigoBoton)
botonEnvio.pack()

raiz.mainloop()

