class Coche():
    #Se denomina estados iniciales y se especifican mediante un constructor
    def __init__(self): #Constructor    
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False
        #Se ponen 2 guiones bajos para encapsular y no se puede acceder desde afuera salvo desde
        #adentro de la clase, es decir desde un metodo o comportamiento

    #Métodos o comportamientos
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__cheque_interno()


        if (self.__enMarcha and chequeo):            
            return "El coche está en marcha"
        elif(self.__enMarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podes arrancar"
        else:
            return "El coche está parado"


    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __cheque_interno(self):
        print("Realizando chequeo interno..")
        
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "Closed"

        if (self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "Closed"):
            return True
        else:
            return False


miCoche = Coche()
print(" ")
print(miCoche.arrancar(True))

miCoche.estado()

print(" ")
print("------A continuación creamos el segundo objeto------")
print(" ")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
#print("Pequeñas pruebas de workteam")
#print("Nueva prueba: Cumplí 28")

miCoche2.estado()
print(" ")