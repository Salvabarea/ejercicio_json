#1. Enumera todos los pokemons y sus tipos.

import json

from pprint import pprint

with open('PGO.json') as data_file:    
    data = json.load(data_file)

for dato in data["pokemon"]:
	pprint ("Nombre:")
	pprint (dato["name"])
	pprint ("Nombre:")
	pprint (dato["type"])
