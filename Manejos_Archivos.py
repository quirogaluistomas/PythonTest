from io import open

#Si existe lo abre y sino lo crea
#archivo_text = open("archivo.txt", "w")

#frase = "Estupendo dia para estudiar Python \n el miércoles"

#archivo_text.write(frase)

#archivo_text.close()

#Ahora ponemos en modo lectura como si el archivo ya existiera
archivo_text = open("archivo.txt", "r")

#texto = archivo_text.read()

#archivo_text.close()

#print(texto)


#Ahora guardamos en lista linea a linea
lineas_texto = archivo_text.readlines()

archivo_text.close()

print(lineas_texto)

print(lineas_texto[0])
print(lineas_texto[1])


#Ahora supongamos que quiero hacer un agregado de línea

archivo_text = open("archivo.txt", "a")

archivo_text.write("\nSiempre es buen momento para estudiar Python")

archivo_text.close()