import sqlite3
conexion = sqlite3.connect("Cabezasalmacen.db")
#idalumno INTEGER PRIMARY KEY AUTOINCREMENT,
tabla_producto="""CREATE TABLE productos(
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE,
                nombre TEXT UNIQUE,
                precio REAL      
                )
               """
cursor = conexion.cursor()
cursor.execute(tabla_producto)
conexion.close()