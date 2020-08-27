def evaluarEdad(edad):

#raise lo que hace es levantar una excepción cuando yo quiera y que diga lo que yo quiera. No lo envía el programa sino yo mismo!
    if edad<0:
        raise TypeError("No se permiten edades negativas")

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate.."

print(evaluarEdad(-15))

#Si acá hubiesen mas líneas de código no se ejecutarían porque la excepción que hacemos saltar no es capturada por el try except