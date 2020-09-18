import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre: ", self.nombre)

    def __str__(self): #Convierte en cadena de texto la informacion del objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

#Creamos la clase lista que tendrá a las personas

class ListaPersonas:

    personas = [] #Defino lista vacía

    def __init__(self):

        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas al fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("Información del fichero: ")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona("Pepe", "Masculino", 28)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
#p = Persona("Sandra", "Femenino", 29)
#miLista.agregarPersonas(p)

#p = Persona("Lucho", "Masculino", 28)
#miLista.agregarPersonas(p)

#p = Persona("Agus", "Femenino", 28)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()
