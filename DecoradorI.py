#Decorador suma funcionalidades a las funciones
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        #Acciones adicionales

        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado")
    
    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):

    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):

    print(num1-num2)
    
@funcion_decoradora
def potencia(base, exponente):

    print(pow(base, exponente))

suma(7,5,8)

resta(12,10)

potencia(base = 5, exponente = 3) #Se pone kwargs porque lleva "clave valor"