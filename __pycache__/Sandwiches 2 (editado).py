import datetime

pedidoNuevo = []

Sandwicheria = {"Sandwich": 
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

listadeprecio=[]
listaDeLlaves = []
altaPedido = {}

for llaves in Sandwicheria ["Sandwich"]:
	for diccionarios in llaves:
		listaDeLlaves.append (diccionarios)

#print (listaDeLlaves)
sumavalor=0
for id1, elige in enumerate(listaDeLlaves):
    print (f"Elija el {elige}")
    for id, producto in enumerate (Sandwicheria ["Sandwich"][id1] [elige]):
        id += 1
        print (str (id), str(producto))
        print(elige)

    producto = int(input ("Elija número "))#tratar el error de ingreso
    producto -= 1
    altaPedido [elige] = Sandwicheria ["Sandwich"][id1] [elige] [producto]

precioAPagar=0
for tipoDe,productoYSuPrecio in altaPedido.items():
	for suProducto, suPrecio in productoYSuPrecio.items():
		precioAPagar = precioAPagar + suPrecio
print (f"Su pedido consta de: \n{altaPedido}")
print(f"\n\nEl precio total a pagar es ${precioAPagar}.")
#
#print (elige)
#print (producto)
#print (precio)
	#sumavalor = sumavalor + int(Sandwicheria ["Sandwich"][id1] [elige] [producto][precio])



