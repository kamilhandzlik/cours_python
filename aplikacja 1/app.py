import requests

id_person = input("Podaj id osoby nt, której informacje chcesz uzyskać:")
response = requests.get(f'https://swapi.dev/api/people/{id_person}/')
if response.status_code == 200:
    response_json = response.json()
    print(f"Wybrałeś postać {response_json['name']}, która ma {response_json['height']} cm wzrostu")
else:
    print('Źle wykonane zapytanie')

