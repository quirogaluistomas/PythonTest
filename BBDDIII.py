import sqlite3

miConexion = sqlite3.connect("GestionProductos") #Se abre/conecta la conexión

miCursor = miConexion.cursor() #Se crea un cursor porque es asi

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion'")
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")
#productos = miCursor.fetchall()

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")
#print(productos)




miConexion.commit()

miConexion.close() 