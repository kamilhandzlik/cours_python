
#################################################
#############  Zadanie 4 ########################
#################################################
"""Napisz program, który obliczy pierwiastek 10 losowych liczb z zakresu 4-100. Następnie utworzy z nich słownik w postaci 

{ 
	1: pierwiastek pierwszej liczby,
	2: pierwiastek drugiej liczby,
	...
}

Następnie zapisz dane do pliku values.json z wcięciem równym 6. Sam plik ma zostać umieszczony w katalogu stats. Upewnij się, plik oraz katalog istnieje przed wykonaniem zapisu JSONa.

*Plik można nadpisywać."""

from math import sqrt
import json
import os.path
from random import randint


num_of_elements = [randint(4, 100) for _ in range(10)]
num_sqrt = [sqrt(num) for num in num_of_elements]
num_dict = {i + 1: sqrt(num) for i, num in enumerate(num_of_elements)}

file_path = 'stats/values.json'

os.makedirs(os.path.dirname(file_path), exist_ok=True)


with open(file_path, 'w') as json_file:
    json.dump(num_dict, json_file, indent=6)

print("Data has been written to 'values.json' in the 'stats' directory.")