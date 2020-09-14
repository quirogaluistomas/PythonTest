#Ejemplo de herencia super.

class Persona():
    #Constructor
    def __init__(self, nombre, edad, lugar_residencia): #Características de una persona

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)


#La idea es que un empleado es una persona y queremos que herede de esta clase
class Empleado(Persona):
    #Constructor
    def __init__(self, salario, antiguedad, nombre_emplead, edad_empleado, residencia_empleado): #Características como salario y antiguedad de clase empleado

        super().__init__(nombre_emplead, edad_empleado, residencia_empleado) #Le decimos que ejecute primero al parte padre

        self.salario = salario
        
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()

        print("Salario: ", self.salario, "\n" "Antiguedad: ", self.antiguedad)

#Construimos objeto de tipo persona (instancia de clase persona)
Antonio = Empleado(1500, 10, "Luis", 55, "España")

Antonio.descripcion()

#Chequeamos si una instancia es de tal clase

print(isinstance(Antonio,Persona)) #Si pusiera empleado sería lo mismo pero si lo crease empleado me daría false.