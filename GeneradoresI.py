#En el ejemplo de la diapo muestra que un generador va generando de 1 en uno los valoresen la lista y vuelve a la siguiente linea
# de ejecucion con lo cual hay que llamar nuevamente a la función para que genere otro numero y así sucesivamente.

#Sin generador

#def generarPares(cantidad):
    
#    num = 1

#    miLista = []

#    while num<cantidad:

#        miLista.append(num*2)
#        num = num + 1

#    return miLista

#print(generarPares(10))

#Con generador

def generarPares(cantidad):
    
    num = 1

    
    while num<cantidad:

        yield num*2

        num = num + 1

#Este objeto guarda el objeto iterable que devuelve el generador
devuelvePares = generarPares(10)

#for i in devuelvePares:
#    print(i)

#El metodo next toma elemento a elemento lo que tiene el objeto iterable

print(next(devuelvePares))
print("Aqui podria ir mas codigo")

print(next(devuelvePares))
print("Aqui podria ir mas codigo")

print(next(devuelvePares))