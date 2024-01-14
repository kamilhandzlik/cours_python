#################################################
#############  Zadanie 1 ########################
#################################################
"""Napisz program, który poprosi od użytkownika datę początkową i
 końcową w formacie YYYY-MM-DD. Następnie wylosuje 10 dat z podanego zakresu.
 Zakładamy, że wprowadzone są prawidłowe.

Do losowania daty możemy wykorzystać poniższy kod. Na produkcji jest dostępna
wersja 21.0.0 i jest ona zalecona do tego zadania.

fake = Faker()
fake.date_between(start_date=<data_startowa_jako_datetime>, end_date=<data_koncowa_jako_datetime>)"""
from dis import dis

def is_even(n: int) -> bool:
    if n % 2 != 0:
        return False
    else:
        return True
    
print(is_even(55))

dis(is_even)


#################################################
#############  Zadanie 2 ########################
#################################################
"""  Stwórz listę z 20 losowymi liczbami z przedziału
 <0,1>, następnie  wypisz losową ilość losowych
 elementów z listy."""
from random import uniform, randint


num_of_elements = randint(1, 20)  
num_of_numbers = [uniform(0, 1) for _ in range(20)]


for i in range(num_of_elements):
    print(num_of_numbers[i])

#################################################
#############  Zadanie 3 ########################
#################################################
"""Napisz program który przyjmuje datę w formacie YYYY/MM/DD i
  zwraca datę jaka będzie za X dni."""


from datetime import datetime, timedelta

def user_choice():
    current_date_str = input("Enter date (remember it must be in format YYYY/MM/DD): ")

    try:
        current_date = datetime.strptime(current_date_str, "%Y/%m/%d")
    except ValueError:
        print("Invalid date format. Please use YYYY/MM/DD.")
        return

    try:
        user_days = int(input("Enter number of days: "))
    except ValueError:
        print("Invalid input for days. Please enter a valid integer.")
        return

    find_date(current_date, user_days)

def find_date(current_date, user_days):
    future_date = current_date + timedelta(days=user_days)
    print(f"The date {user_days} days from {current_date.strftime('%Y/%m/%d')} will be: {future_date.strftime('%Y/%m/%d')}")

user_choice()


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