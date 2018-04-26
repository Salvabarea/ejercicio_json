#3. Crea un programa que filtre los pokemons por su peso, debe pedir un peso máximo y un peso mínimo
#y deberá mostar su nombre y peso.

import json

from pprint import pprint

with open('PGO.json') as data_file:    
    data = json.load(data_file)

pesoMin = float(input ("Dime el peso mínimo: "))
pesoMax = float(input ("Dime el peso máximo: "))

for dato in data["pokemon"]:
	if float(dato["weight"]) < pesoMax and float(dato["weight"]) > pesoMin:
		pprint (dato["name"])
