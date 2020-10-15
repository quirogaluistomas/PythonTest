import re

lista_nombres = ["Ana Gomez", "María Martín",
                "Sandra López", "Santiago Martín",
                "niños", "niñas"]


for elemento in lista_nombres:
    if re.findall("^Sandra", elemento): #^Busca en los elementos que comienzan con lo que sigue al simbolo

        print(elemento)


for elemento in lista_nombres:
    if re.findall("Martín$", elemento): #^Busca en los elementos que terminan con lo que sigue al simbolo

        print(elemento)

    

for elemento in lista_nombres:
    if re.findall("[ó]", elemento): #^Busca en los elementos que contienen el simbolo ó

        print(elemento)


for elemento in lista_nombres:
    if re.findall("niñ[oa]s", elemento): #^Busca en los nombres que contengan la "o" o la "a" en dicha posición

        print(elemento)