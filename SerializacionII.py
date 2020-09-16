import pickle 

class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha,
         "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1 = Vehiculos("Mazda", "MX5")

coche2 = Vehiculos("Seat", "Leon")

coche3 = Vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    #print(c)
    print(c.estado()) #Serializacion de objetos

#Si esta ultima parte donde se levanta lo que hay en losCoches
#se pone en otro archivo .py va a tirar error porque no sabe quien
#coño es Vehiculo! Hay que sí o sí definir la clase nuevamente.