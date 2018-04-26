#2. Crea un programa que al introducir por pantalla un tipo de pokemon cuente la cantidad de pokemons
#que son de dicho tipo.

import json

from pprint import pprint

with open('PGO.json') as data_file:    
    data = json.load(data_file)
contador = 0

tipo2 = input("Dime el tipo (en inglés): ")

for dato in data["pokemon"]:
	for tipo in dato["type"]:
		if tipo == tipo2:
			contador+=1

print("Hay un total de",contador,"pokemons de tipo",tipo2)