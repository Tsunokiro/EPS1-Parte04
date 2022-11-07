import sqlite3
conexion = sqlite3.connect("Cabezasalmacen.db")
cursor=conexion.cursor()
lista_productos=[('1001','aceite',10.50),
                 ('1002','atun',5.0),
                 ('1003','sal',1.5),
                 ('1004','arroz',3.4),
                 ('1005','huevo',10),
                 ('1006','fideos',9.5),
                 ('1007','azucar',8),
                 ('1008','leche',3.3),
                 ('1009','detergente',8.5),
                 ('1010','mayonesa',4.2)
]
consulta_producto="""insert into
productos(codigo,nombre,precio)
values(?,?,?)"""
cursor.executemany(consulta_producto, lista_productos) 
conexion.commit()
conexion.close()