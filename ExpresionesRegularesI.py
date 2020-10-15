import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es sencillo de comprender"

textoBuscar = "aprender"

textoBuscar = "Python"
#textoEncontrado = re.search(textoBuscar, cadena)

#print(textoEncontrado.start()) #Tira el índice de caracter dónde comienza el texto encontrado
#print(textoEncontrado.end()) #Lo mismo pero con el final
#print(textoEncontrado.span()) #Imprime inicio y final

print(re.findall(textoBuscar,cadena)) #Me trae todas las coincidencias.
print(len(re.findall(textoBuscar,cadena)))