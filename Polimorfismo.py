class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

#Utilizamos polimorfismo

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
#La pregunta sería a qué método desplazamiento llamará ya que no sabemos qué objeto es "vehiculo"..La respuesta es
#que es un parámetro y va a ir cambiando su forma según lo que le pasen y sabrá a que desplazamiento llamar.

#miVehiculo = Camion()
miVehiculo = Coche()

desplazamientoVehiculo(miVehiculo)