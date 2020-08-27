#edad = input("Introduce una edad: ")

#while edad<0 or (edad>100):
#    print("Has introducido una edad incorrecta")
#    edad = input("Introduce una edad: ")


#Calculo de raiz
import math

numero = float(input("Introduce un numero por favor: "))
intentos = 0

while numero<0:
    print("No se puede introducir un numero negativo")
    
    if intentos==2:
        print("Has consumido los intentos. El programa finalizara")
        break; 


    if numero<0:
        intentos = intentos+1

    numero = float(input("Introduce un numero por favor: "))

if intentos<2:
    solucion = math.sqrt(numero)
    print("El resultado es:" + str(solucion))

#Recordar que para python3 la función input toma enteros y strings, corresponde a mi castearlo o no.