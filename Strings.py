nombreUser = input("Ingresa tu nombre: ")

#print("El nombre es: ", nombreUser.upper())
#print("El nombre es: ", nombreUser.lower())
print("El nombre es: ", nombreUser.capitalize())

edad = input("Introduce la edad: ")

while(edad.isdigit() == False):
    edad = input("Introduce la edad: ")

if (int(edad)<18):
    print("Sos menor de edad, no podes acceder a xvideos")
else:
    print("Metete nomá")    