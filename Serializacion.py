import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb") #write binary

pickle.dump(lista_nombres, fichero_binario) #Informacion que queremos volcar, nombre del fichero al que va a ir

fichero_binario.close()

del(fichero_binario) #borra de memoria

#Ahora vemos si podemos leer ese archivo binario

fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)