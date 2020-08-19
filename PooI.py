class Coche():
    #Ponemos las propiedades o atributos
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    #Métodos o comportamientos
    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if(self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

miCoche = Coche()

print("El largo del coche es: " ,miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche.arrancar()

#Verificación
print(miCoche.estado())

#Este programa tiene 4 propiedades y 2 comportamientos
