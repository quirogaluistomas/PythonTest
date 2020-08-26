class Coche():
    #Se denomina estados iniciales y se especifican mediante un constructor
    def __init__(self): #Constructor    
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = True
        #Se ponen 2 guiones bajos para encapsular y no se puede acceder desde afuera salvo desde
        #adentro, es decir desde un metodo o comportamiento

    #Métodos o comportamientos
    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos

        if (self.__enMarcha):            
            return "El coche está en marcha"
        else:
            return "El coche está parado"


    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)


miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print(" ")

print("------A continuación creamos el segundo objeto------")

print(" ")
miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()
