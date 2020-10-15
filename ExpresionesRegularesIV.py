import re

nombre1 = "Sandra López"

nombre2 = "Antonio Gomez"

nombre3 = "Maria López"

#La función match busca siempre al comienzo de la cadena

if re.match("sandra", nombre1, re.IGNORECASE): #Deshabilita el casesensitive

    print("Hemos encontrado el nombre")

else:

    print("No encontré nada capo")



if re.match("...ia", nombre3, re.IGNORECASE): #Cada punto suplanta una letra

    print("Hemos encontrado el nombre")

else:

    print("No encontré nada capo")


#La función search busca en TODA la cadena.

if re.search("López", nombre1, re.IGNORECASE): #Deshabilita el casesensitive

    print("Hemos encontrado el nombre")

else:

    print("No encontré nada capo")
