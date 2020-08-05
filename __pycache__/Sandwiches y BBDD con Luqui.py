import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
from Estructura import *


hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql=""


nombre_DDBB = "BasesDeDatos_Sandwicheria"
nombre_tabla_1 = "TipoDePan"
nombre_tabla_2 = "TipoDeQueso"
nombre_tabla_3 =  "TipoDeProteina"
nombre_tabla_4 = "TipoDeSalsa"

nombre_columna_1 = "Producto"
nombre_columna_2 = "Precio"
nombre_columna_3 = "Codigo"


"""
Sandwicheria= {"Sandwich": [
{"TipoDePan":["Blanco","Negro","De Salvado"]},
{"TipoDeQueso":["Cheddar","Mozzarella"]},
{"TipoDeProteina":["Pollo","Jamon","Tofu"]},
{"TipoDeSalsa":["Mayonesa","Ketchup","Mostaza"]}
]}
"""


def borrar_base():
	try:
		print ("Conectamos con MySQL")
		#connection = mysql.connector.connect(host="localhost",user="root", passwd="")
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql )
		cursor = connection.cursor()
		print("DROP DATABASE "+str(nombre_DDBB))
		cursor.execute("DROP DATABASE "+str(nombre_DDBB))
		cursor.close
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close



def crear_base():
	try:
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql )
		cursor = connection.cursor()

		cursor.execute(f"CREATE DATABASE {nombre_DDBB}")
		connection.commit()
		cursor = connection.cursor()
		print(cursor.rowcount, "record inserted.")
		print ("USE DATABASE")
		cursor.execute(f"USE {nombre_DDBB}")
		cursor = connection.cursor()
		
		#Tabla de Pan
		print ("CREATE TABLE")
		print ("CREATE COLUMN")
		cursor.execute("CREATE TABLE "+str(nombre_tabla_1) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor = connection.cursor()
		
		print('columnas_mysql = "INSERT INTO  "'+str(nombre_tabla_1) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla_1) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)"

		
		cursor.execute(columnas_mysql, ("Blanco", 30 , "Bl"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Negro", 35 , "Ne"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Salvado", 30 , "Sa"))
		connection.commit()
		
		##############################################################
		#Tabla de Quesos
		cursor.execute("CREATE TABLE "+str(nombre_tabla_2) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor = connection.cursor()
		
		print('columnas_mysql = "INSERT INTO  "'+str(nombre_tabla_2) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla_2) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)"
	
		
		cursor.execute(columnas_mysql, ("Cheddar", 30 , "Ch"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Muzzarella", 35 , "Mu"))
		connection.commit()

		
		##############################################################
		#Tabla de Proteina
		cursor.execute("CREATE TABLE "+str(nombre_tabla_3) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor = connection.cursor()
		
		print('columnas_mysql = "INSERT INTO  "'+str(nombre_tabla_3) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla_3) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)"
		
		
		cursor.execute(columnas_mysql, ("Pollo", 25 , "Po"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Jamon", 30 , "Ja"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Tofu", 35 , "To"))
		connection.commit()
		
		
		
		##############################################################
		#Tabla de Salsas
		cursor.execute("CREATE TABLE "+str(nombre_tabla_4) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor = connection.cursor()
		
		print('columnas_mysql = "INSERT INTO  "'+str(nombre_tabla_4) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla_4) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)"
		
		
		cursor.execute(columnas_mysql, ("Mayonesa", 30 , "May"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Mostaza", 30 , "Mo"))
		connection.commit()
		cursor.execute(columnas_mysql, ("Ketchup", 30 , "Ke"))
		connection.commit()
		
		
		print(cursor.rowcount, "record inserted.")
		print("cerramos conexión");
		cursor.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
		cursor.close
	finally:
		cursor.close

	print(cursor.rowcount, "record inserted.")
	print("cerramos conexión");
	cursor.close




borrar_base ();
crear_base();
limpiar ();





