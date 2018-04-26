# 4. Crear un programa que nos pida el nombre del pokemon y nos diga su siguiente evolucion.

import json

from pprint import pprint

with open('PGO.json') as data_file:    
    data = json.load(data_file)

nombre = input("Nombre del pokemon: ")

for dato in data["pokemon"]:
	if nombre == dato["name"]:
		for evolucion in dato["next_evolution"]:
			pprint(evolucion["name"])