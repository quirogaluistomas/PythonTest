from tkinter import * #Biblioteca para gui

raiz = Tk()

raiz.title("Ventana de pruebas") #Titulo de la ventana

#raiz.resizable(True,False) #Height and Width

raiz.iconbitmap("LogoDamez.ico")

#raiz.geometry("650x350")

raiz.config(bg = "black") #color de background

miFrame = Frame() #Construyo Frame

miFrame.pack()
#miFrame.pack(fill = "both", expand = "True")#Lo meto en la raiz con alguna característica

miFrame.config(bg = "red")

miFrame.config(width = "650", height = "350")

miFrame.config(cursor = "pirate")

raiz.mainloop() #Loop infinito que queda a la espera de eventos

