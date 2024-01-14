"""
Moduł: random
    randint(a,b) - losowa wartość <a,b>
    choice(lista) - wybór przyadkowego elementu z listy
    uniform(a,b) - losowa wartość <a, b> (dostępne wartości zmienno przecinkowe)

Moduł: datetime
    %Y - rok; %m - miesiąc; %d - dzień 
    %B - konwertuje słownie zapisane miesiące ,,january''
    %H - godzina; %M - minuta; %S - sekunda
    
    now() - zwraca aktualną datę i czas
    strptim(data) - konwersja do datetime łańcucha znakowego
    timedleta - dodaje/odejmuje podany zakres czasowy   


"""

from random import randint, uniform
from datetime import datetime, timedelta
from Faker import *

run = True
if run:
    print("-- -- random -- --")
    print(f"Losowy int: {randint(0, 10)}")
    print(f"Losowy float: {uniform(1.0, 2.0)}")

    print("-- -- datetime -- --")
    print(f"Dzisiaj: {datetime.now()}")
    print(f"dzisiaj to str: {datetime.now().strftime('%d.%m.%Y')}")

    date_str = "01-01-2024, 10:45"
    print(datetime.strptime(date_str, "%d-%m-%Y, %H:%M"))
    print(datetime.now() + timedelta(hours=2)) #Do czasu obecnego dodaje n godzin
    print(datetime.now() + timedelta(hours=2, days=7)) #działa też z dniami
    print(datetime.now() + timedelta(days=30)) #działa też z dniami powyżej miesiąc od teraz poprostu zmienia miesiąc powyżej długości danego miesiąca


"""
    Moduł: json
        load() - czytanie pliku w formacie JSON
        dumps() - zapis + formatowanie pliku JSON
    Moduł: math
        Większośc funkcji matematycznych oraz zmiennych (jak np. PI)
    Moduł: os
        path.exists(ścieżka) - sprawdza, czy plik/katalog istnieje
        path.isdir(ścieżka) - sprawdza, czy ścieżka to katalog
        path.isfile(ścieżka) - sprawdza, czy ścieżka to plik
"""
import json
import os.path

if __name__ == '__main__':
    # Odczyt pliku JSON
    data = json.load(open("metadata.json"))
    print(data)
    print(data['title'])

    example_dict = {
        "first": "Adam",
        "last": "Kowalski",
        "phone": "123567345",
        "age": 34,
        "is_employed": True
    }

    # Zapis do pliku JSON
    json.dump(example_dict,
              open("person.json", "w"),
              indent=2
              )

    print(f'Istnieje: {os.path.exists("data")}')
    print(f'Plik: {os.path.isfile("data")}')
    print(f'Katalog: {os.path.isdir("data")}')

    print(f'Istnieje json: {os.path.isfile("person.json")}')