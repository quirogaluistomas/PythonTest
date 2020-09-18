from tkinter import *

root = Tk()

miFrame = Frame(root, width = 500, height = 400)

miFrame.pack() #Lo empaqueto a la raiz

miImagen = PhotoImage(file = "fiuba.png")

#miLabel = Label(miFrame, text = "Aguante Python, vieja!", fg = "red", font = ("Comic Sans MS", 18)) #Pongo un label
miLabel = Label(miFrame, image = miImagen)

miLabel.place(x = 100, y = 100) #Ponemos el label donde epecifico

root.mainloop()