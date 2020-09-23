import sqlite3

miConexion = sqlite3.connect("PrimeraDBase") #Se abre/conecta la conexión

miCursor = miConexion.cursor() #Se crea un cursor porque es asi

#miCursor.execute("CREATE TABLE PRODUCTOS(Nombre_Artículo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20))")
#Invalidamos la linea para que no tire error y quiera crear nuevamente la tabla

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")
#Invalido esta porque ahora voy a hacer otras cosas

#Acá agrego a la tabla una lista de tuplas en vez de hacer varios insert ino
#variosProductos = [

#    ("Camiseta", 10, "Deportes"),
#    ("Jarrón", 90, "Cerámica"),
#    ("Camión", 20, "Jugueteria")

#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall() #Leo la base de datos

for producto in variosProductos:

    print(producto)

miConexion.commit()

miConexion.close()