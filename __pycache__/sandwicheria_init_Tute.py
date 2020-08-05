import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
import datetime
from Estructura import *
debug = True
nombre_DDBB = "Sandwicheria"

hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql=""

Sandwicheria = {"Sandwich": 
							[{"TipoDePan":
											[{"Blanco": 10.25},
											 {"Negro": 5.15},
											 {"De Salvado": 14.30},
											 {"Arabe": 9.11}]
								},
							 {"TipoDeQueso":
											[{"Cheddar": 6.15},
											 {"Mozzarella": 4.12}]
								 },
							 {"Relleno":
											[{"Carne": 25.30},
											 {"Cerdo": 16.45},
											 {"Pollo": 12.50},
											 {"Jamon": 15.20},
											 {"Tofu": 45.20}]
								 },
							 {"TipoDeSalsa":
											[{"Mayonesa": 8.50},
											 {"Ketchup": 7.20},
											 {"Mostaza": 6.15}]
								 },
							 {"TipoDeVerdura":
											[{"Lechuga": 5.50},
											 {"Tomate": 4.30},
											 {"Zanahoria": 7.40}]
								 }
							]
				}


def crear_base(nombre_base_MySQL):
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql )
	#connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")#database='AGT',
	cursor = connection.cursor()
	cursor.execute(f"CREATE DATABASE {nombre_base_MySQL}")
	if debug: print (f"Creamos la base de datos {nombre_base_MySQL}")
	print ("cerramos conexión")
	cursor.close


def crear_tablas (nombre_base_MySQL, nombre_tabla):
	Nombre_columna_1 = "Producto"
	Nombre_columna_2 = "Precio"

	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql, database = nombre_base_MySQL)
	cursor = connection.cursor()
	cursor.execute(f"CREATE TABLE {nombre_tabla} (id INT AUTO_INCREMENT PRIMARY KEY, {Nombre_columna_1} VARCHAR(255) NOT NULL, {Nombre_columna_2} FLOAT NOT NULL) ")
	if debug: print (f"Creamos la tabla {nombre_tabla}")
	cursor.close
	#Columnas = ["Productos","Precio"] 
	
def borrar_base(nombre_base_MySQL_input):
	connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql  )
	cursor = connection.cursor()
	cursor.execute(f"DROP DATABASE {nombre_base_MySQL_input}")
	cursor.close

def cargar_tabla (nombre_DDBB,tabla,producto,precio):
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql, database= nombre_DDBB )
	cursor = connection.cursor()
	columna_mySQL = f"INSERT INTO {tabla} (PRODUCTO, PRECIO) VALUES (%s, %s)"
	cursor.execute(columna_mySQL, (producto, precio) )
	connection.commit()
	print (f"Cargamos la tabla {tabla}")
	cursor.close
borrar_base (nombre_DDBB)

crear_base(nombre_DDBB)	
listaDeTipos = []
for tiposDe_dic in Sandwicheria ["Sandwich"]:
	for tipoDe in tiposDe_dic:
		crear_tablas(nombre_DDBB, tipoDe)
		listaDeTipos.append(tipoDe)

for idTipoDe, elTipoDe in enumerate (listaDeTipos):
	print (f"Se cargo en {elTipoDe}")
	
	for id1, productoYPrecio in enumerate (Sandwicheria ["Sandwich"] [idTipoDe][elTipoDe]):
		#print (id1)
		#print (productoYPrecio)
		for producto, precio in productoYPrecio.items():
			print (f"El producto: {producto} al precio de ${precio}")
			cargar_tabla (nombre_DDBB, elTipoDe, producto, precio)
	
	
