def devuelveCiudades(*ciudades):
#El asterisco significa que el elemento que recibe tiene una dimensión indeterminada y que lo recibe en forma de tupla
#Acceder mediante for anidados a un elemento de la matriz

#La otra forma es con yield from

    for elemento in ciudades:
#        for subElemento in elemento:
            yield from elemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Alicante")

print(next(ciudadesDevueltas))

print(next(ciudadesDevueltas))

