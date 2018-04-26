# 5. Crear un programa que nos pida el nombre de un pokemon, luego nos mostrará un menú donde
# podremos seleccionar el Tipo, la Altura, el Peso, las Debilidades y Otra información (libre).


import json

from pprint import pprint

with open('PGO.json') as data_file:    
    data = json.load(data_file)

menu = True

print ("¡Hola, bienvenido a la Pokedex, desde aquí puedes consultar cualquier dato.")
pokemon = input ("¿Qué pokemon quieres consultar?: ")

for dato in data["pokemon"]:
	if pokemon == dato["name"]:
		print ("------")
		print ("Has accedido a los datos de",pokemon, "cuyo número es",dato["num"])
		print ("------")
		while menu:
			print ("Menú:")
			print ("1. Tipo de Pokemon.")
			print ("2. Altura.")
			print ("3. Peso.")
			print ("4. Debilidades.")
			print ("5. Otra información.")
			print ("6. Salir.")
			seleccion = int(input("Ingrese un número: "))
			if seleccion == 1:
				print ("Pokemon tipo:",dato["type"])
				continue
			elif seleccion == 2:
				print (pokemon,"mide",dato["height"])
				continue
			elif seleccion == 3:
				print (pokemon,"pesa",dato["weight"],"kilos.")
				continue
			elif seleccion == 4:
				print ("Las debilidades de",pokemon,"son:",dato["weaknesses"])
				continue
			elif seleccion == 5:
				print (pokemon,"tiene una probabilidad de aparecer de:",dato["spawn_chance"])
				print (pokemon,"suele aparecer sobre las:",dato["spawn_time"])
				print ("Si consiguieses un huevo de",pokemon,"tendrías que andar",dato["egg"],"para que eclosionase.")
				continue
			elif seleccion == 6:
				print ("Saliendo.")
				menu = False
			print ("------")
