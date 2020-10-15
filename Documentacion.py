class Areas:

    """ Esta clase calcula áreas """
    
    def areaCuadrado (lado):

        """ Calculo de area de un cuadrado bien sencillo"""

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):

        return "El área del triángulo es: " + str((base*altura)/2)


print(Areas.areaCuadrado(3))

print(Areas.areaTriangulo(5,3))


#help(Areas.areaCuadrado) #Imprime los comentarios
help(Areas)