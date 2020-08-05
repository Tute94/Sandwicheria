import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
import datetime
debug = True
nombre_DDBB = "Sandwicheria"
nombre_tabla = "producto"
hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql=""

{"Sandwich": 
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

def crear_base(nombre_base_MySQL):
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql )
	#connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")#database='AGT',
	cursor = connection.cursor
	cursor.execute(f"CREATE DATABASE {nombre_base_MySQL}")
	if debug: print (f"Creamos la base de datos {nombre_base_MySQL}")
	print ("cerramos conexión")
	cursor.close


def crear_tablas (nombre_base_MySQL):
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql )
	cursor = connection.cursor
	cursor.execute(f"CREATE TABLE {nombre_tabla} (id INT AUTO_INCREMENT PRIMARY KEY, {Nombre_columna_1} VARCHAR(255) NOT NULL,(id INT AUTO_INCREMENT PRIMARY KEY, {Nombre_columna_2} FLOAT NOT NULL, ")
	if debug: print (f"Creamos la tabla {nombre_tabla}")
	
	
crear_base (nombre_DDBB)
	
	

