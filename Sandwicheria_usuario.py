
from Sandwicheria_init_Final import*

debug = True

while debug:
	
	try :
		connection = mysql.connector.connect(host= host_local,user= usuario ,passwd= password_de_msql, database= nombre_DDBB )
		cursor = connection.cursor()
		
		print ("\n \nBienvenido a su sangucheria, a continuación cargue sus productos:")
		
		menu = True 
		while menu:	
				
			print ("\n \n¿Que desea hacer?: ")
			
			
			print ("\n \t1-modificar productos y precios")		
			print ("\n \t2-agregar productos ")
			print ("\n \t3-eliminar productos ")
			print ("\n \t4-ver ventas")
			print ("\n \t5-Ver productos ingresados")
			print ("\n \t6-finalizar")
			
			
			
			desicion_menu = input ("\nIngrese el numero de la opcion deseada: ")
			
			if desicion_menu == "1":
				modificar_productos()
			elif desicion_menu == "2":
				carga_manual()	
			elif desicion_menu == "3":
				eliminar_productos()
			elif desicion_menu == "4":
				chequeo_ventas()
			elif desicion_menu == "5":
				mostrar_menu()			
			elif desicion_menu == "6":
				print("\n\tHasta la proxima venta")
				menu = False	 
			else: 
				print("\n\tError vuelva a ingresar una opcion")
			
			
			
		debug = False
		 
			
	
	except:
		crear_base_predefinida ()
		

		

	


