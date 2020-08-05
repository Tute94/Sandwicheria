import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Estructura import *
import json
import datetime
nombre_DDBB = "Sandwicheria"
hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql=""

Sandwicheria = {"Sandwich": #Diccionario con la base predefinida de productos y precios por la empresa.
							[{"TipoDePan":
											[{"Blanco": 10.25},
											 {"Negro": 5.15},
											 {"De Salvado": 14.30},
											 {"Arabe": 9.11}]},
							{"TipoDeQueso":
											[{"Cheddar": 6.15},
											 {"Mozzarella": 4.12}]},
							{"Relleno":
											[{"Carne": 25.30},
											 {"Cerdo": 16.45},
											 {"Pollo": 12.50},
											 {"Jamon": 15.20},
											 {"Tofu": 45.20}]},
							{"TipoDeSalsa":
											[{"Mayonesa": 8.50},
											 {"Ketchup": 7.20},
											 {"Mostaza": 6.15}]},
							{"TipoDeVerdura":
											[{"Lechuga": 5.50},
											 {"Tomate": 4.30},
											 {"Zanahoria": 7.40}]}
					]}

def crear_base(nombre_base_MySQL): #Crea base de datos a partir del nombre de arriba
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql)
	cursor = connection.cursor()
	cursor.execute(f"CREATE DATABASE {nombre_base_MySQL}")
	print (f"Creamos la base de datos {nombre_base_MySQL}")
	cursor.close

def crear_tablas (nombre_base_MySQL,nombre_tabla): #Funcion para crear las tablas con id, producto y precio (Deberiamos agregar Stock))
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql, database= nombre_base_MySQL )
	cursor = connection.cursor()
	cursor.execute(f"CREATE TABLE {nombre_tabla} (id INT AUTO_INCREMENT PRIMARY KEY, PRODUCTO VARCHAR(255) NOT NULL, PRECIO FLOAT NOT NULL)")
	print (f"Creamos la tabla {nombre_tabla}")
	cursor.close
	
def borrar_base(nombre_base_MySQL): #Elimina la base con el nombre de la variable de arriba
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql )
		cursor = connection.cursor()
		print(f"DROP DATABASE {nombre_DDBB}")
		cursor.execute(f"DROP DATABASE {nombre_DDBB}")
		cursor.close
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		print (f"La base de datos {nombre_DDBB} fue eliminada correctamente.")
		cursor.close

def cargar_tabla (nombre_DDBB,tabla,producto,precio): #Funcion para cargar tabla por defecto. (Modificar funcion cuando se agregue el stock)
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql, database= nombre_DDBB )
	cursor = connection.cursor()
	columna_mySQL = f"INSERT INTO {tabla} (PRODUCTO, PRECIO) VALUES (%s, %s)"
	cursor.execute(columna_mySQL, (producto, precio) )
	connection.commit()
	cursor.close
	
def crear_base_predefinida (): #Funcion que crea la base de datos con el menu predefinido de la empresa. (A partir de diccionario)
	


	crear_base(nombre_DDBB)	

	#Con esto se crean las tablas y una lista con los "tipos de":
	listaDeTipos = []
	for tiposde_dic in Sandwicheria ["Sandwich"]:
		for tipoDe_llave in tiposde_dic:
			crear_tablas(nombre_DDBB,tipoDe_llave)
			listaDeTipos.append (tipoDe_llave)


	#Con esto se cargan los productos en la tabla a partir del diccionario:
	for idTipoDe, elTipoDe in enumerate (listaDeTipos):
		print (f"Se cargo en {elTipoDe}")
		
		for id1, productoYPrecio in enumerate (Sandwicheria ["Sandwich"] [idTipoDe][elTipoDe]):
			#print (id1)
			#print (productoYPrecio)
			print (f"Cargamos la tabla {elTipoDe}")
			for producto, precio in productoYPrecio.items():
				print (f"El producto: {producto} al precio de ${precio}")
				cargar_tabla (nombre_DDBB, elTipoDe, producto, precio)
        
        
#Funciones especificas de usuario        
               
def carga_manual (): #Funcion encadenada, depende de cargar tabla. Permite al usuario la carga manual de productos.
	for tiposde_dic in Sandwicheria ["Sandwich"]:
			for tipoDe_llave in tiposde_dic:
				decision = "S"
				while decision.upper () == "S" :
					decision = input(f"\nDesea agregar un {tipoDe_llave}? S/N: ") 
					if decision.upper ()== "S":
					
						print(f"\tCargue el {tipoDe_llave}:")
						producto= input ("\t\tIngrese el nombre del producto ")
						debug= True
						while debug:
							try: 
								precio=float (input ("\t\tngrese el precio del producto "))
								debug= False
							except: 
								print ("\nError, no ha ingresado un numero correcto, vuelva a ingresar precio: ")
														
						cargar_tabla(nombre_DDBB,tipoDe_llave,producto,precio)
						print (f"Usted cargo el producto '{producto}' al precio de ${precio} \n")
						
					elif decision.upper () == "N":
						break 
						
					else:
						print ("Error, vuelva a ingresar el valor S/N")
						decision = "S"
	debug = False

def mostrar_menu (): #Función que te muestra el menú de los ingredientes.
	print ("\nEste es su menu actual: ");
	connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
	cursor = connection.cursor()
	
	for tiposde_dic in Sandwicheria ["Sandwich"]: #Como se listan los tipos de de una base de datos
		for nombre_tabla in tiposde_dic:
			cursor.execute(f"select id, PRODUCTO, PRECIO from {nombre_tabla}")
			print (f"\n\nLos {nombre_tabla} son: \n")
			print("ID |PRODUCTO       |PRECIO")
			
			for fila in cursor:
				print ("{:<3}|{:<15}|{:<6}".format(fila [0], fila [1], fila [2]))
		
	
	cursor.close
	


def modificar_productos ():
	print("holi")
def eliminar_productos ():
	print("holi")
def chequeo_ventas ():
	print ("holi")



#A partir de aca corre el programa:

#borrar_base(nombre_DDBB)












