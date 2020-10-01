'''def area_triangulo(base, altura):

    return(base*altura/2)'''

#La funcion lambda simplifica las funciones sencillas
#y se agregan sobre una sola línea. Para funciones complejas no sirve

area_triangulo = lambda base,altura:(base*altura/2)
al_cubo = lambda numero:pow(numero,3)
#al_cubo = lambda numero:numero**3

triangulo1 = area_triangulo(7,5)

triangulo2 = area_triangulo(9,6)

print(triangulo1)

print(triangulo2)

print(al_cubo(5))

destacar_valor = lambda comision:"¡{}! €".format(comision)

comision_Ana = 15585

print(destacar_valor(comision_Ana))