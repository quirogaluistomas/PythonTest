import re

lista_nombres = ["Ana", "Pedro", "María", "Rosa", "Sandra", "Celia"]

for elemento in lista_nombres:
    if re.findall("^[O-T]", elemento): #Acá muestra todos los nombres que comienzan con letras entre O y T

        print (elemento)



lista_nombres = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4"]

for elemento in lista_nombres:

    if re.findall("Ma[0-3]", elemento): 
    #if re.findall("Ma[^0-3]", elemento): #Si onemos ese símbolo niega el rango
    #if re.findall("Ma[0-3A-B], elemento): # Trae tambiién si hubiese MaA y MaB    
    #if re.findall("Ma[.:], elemento): #Trae los que tengan punto o dos puntos luego de Ma     
        print (elemento)
