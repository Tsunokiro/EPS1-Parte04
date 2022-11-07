import sqlite3
conexion = sqlite3.connect("Cabezasalmacen.db")
cursor=conexion.cursor()
print("    Menú de opciones")
print("1. Registrar")
print("2. Eliminar")
print("3. Editar")
print("4. Listar")
print("5. Salir")




opcion=int(input("Seleccione una opcion: "))
if opcion==1:
    consulta_producto1="""SELECT *FROM PRODUCTOS
    ORDER BY NOMBRE"""
    cursor.execute(consulta_producto1)
    producto1=cursor.fetchall()
    for productos in producto1:
        print(productos)
        conexion.close()
elif opcion == 2:
     print("\tAGREGAR PRODUCTO")
     print("Ingrese código")
     codigo = input()
     print("Ingrese nombre:")
     nombre = input()
     print("Ingrese precio")
     precio = input()
   
    
     agregar_producto = [(codigo,nombre,precio)]
     consulta_agregarproducto = """INSERT INTO 
                              PRODUCTOS (CODIGO, NOMBRE, PRECIO)
                              VALUES (?,?,?)
                            """
     cursor.executemany(consulta_agregarproducto,agregar_producto)
     conexion.commit()
     conexion.close()
    
