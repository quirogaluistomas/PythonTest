from io import open

archivo_texto = open("archivo.txt", "r+") #Lectura mas escritura

#print(archivo_texto.read())

#archivo_texto.seek(0)

#print(archivo_texto.read())

#Ahora hago otra pruebita con el método seek() que posiciona el puntero en donde le especificamos.

#archivo_texto.seek(11)

#print(archivo_texto.read()) #Recordar que al read(x) podés indicarle hasta donde leer x caracter.

#Ejemplo con read(x)

#print(archivo_texto.read(11))

#print(archivo_texto.read())

#Ejemplo mejor con len para tomar la mitad de la lista

#archivo_texto.seek(len(archivo_texto.read())/2)

#print(archivo_texto.read())

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
