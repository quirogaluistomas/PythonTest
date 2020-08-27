def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):

#Lo que sigue es para que cuando quiera dividir por cero me saltee el error, tire un mensaje y siga ejecutando el resto del código.
	try:
		return num1/num2
	except ZeroDivisionError:
		#El except captura solo el tipo de error que le especifique
		print("No se puede dividir por 0")
		return "Operacion erronea"
	
	

op1=(int(input("Introduce el primer numero: ")))

op2=(int(input("Introduce el segundo numero: ")))		
	
operacion=input("Introduce la operaciun a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")