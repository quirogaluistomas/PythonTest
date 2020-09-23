import sqlite3

miConexion = sqlite3.connect("GestionProductos") #Se abre/conecta la conexión

miCursor = miConexion.cursor() #Se crea un cursor porque es asi
#Se agrega la palabra UNIQUE cuando no quiero que se repita el campo
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20)
    )
''')

productos = [

    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica"),
    ("muñeco", 30, "jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()