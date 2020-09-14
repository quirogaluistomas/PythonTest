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

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"



##La sintaxis para heredar es simplemente pasando a la clase el nombre de la clase de la que se hereda
class Moto(Vehiculos):
    hCaballito = ""

    #Creamos el método propio de la moto
    def caballito(self):
        self.hCaballito = "Voy haciendo willy"

    #Acá se sobreescribe el método agregando el método propio, cuando se llama a estado se llama a este y no al del metodo padre
    def estado(self):
        print("Marca ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha,
         "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n" + self.hCaballito)


class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True



miMoto = Moto("Yamaha", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

#Herencia múltiple. Toma siempre como prioridad la herencia del primer argumento, utiliza ese init
class BicicletaElectrica(VElectricos, Vehiculos):
    pass


miBici = BicicletaElectrica("Orbea", "hp1500")

#Como accedemos a las propiedades de la clase de la que hereda? Se ve en el script HerenciaSuper