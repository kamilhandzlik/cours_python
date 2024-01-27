from zadanie_4_menu_kamil_handzlik import *


def main_menu():
    print("1. Wyświetl listę produktów")
    print("2. Dodaj produkt")
    print("3. Usuń produkt")
    print("4. Zapisz zmiany")
    print("5. Pokaż ile sztuk danego produktu jest w magazynie")
    print(
        "6. Pokaż zestawienia"
    )  
    print("7. Wyjdź")


user_choice = ""


# Pętla dla magazynu
class Magazine:
    # TODO zrobić z tego metodę, dodać dziedziczenie po odpowiedniej klasie
    while user_choice != "7":
        main_menu()

        user_choice = input("Wybierz opcję wpisując odpowiednią cyfrę: ")

        if (
            user_choice == 1
        ):  #TODO Zrobić z tego metodę albo funkcję i spraw żeby działało jak już ogarniesz  to klasę sklepu też przerob albo żeby z oba korzystały z jednego
            print("1. Wyświetl listę produktów")
            print(
                "2. ta lista pokazuje klucze z dict produktów oraz daje nowe opcje wyboru"
            )
            print("3. Wybierz produkt, z którym chcesz się lepiej zapoznać")
            print(
                """4. Przechodzi do podstrony produktu, na której są jego parametry,
                   dane techniczne certyfikaty - w konsoli poprostu printuje wszystkie 
                   wartości z dicta dla danego klucza, na którym zapisane są wszystkie dane produktu """
            )
            print("5. Wróć")

        elif user_choice == "2":  #TODO zrób do tego metodę
            print("2. Dodaj produkt")

        elif user_choice == "3":  #TODO zrób do tego metodę
            print("3. Usuń produkt")

        elif user_choice == "4":  #TODO zrób dp tego metodę
            print("4. Zapisz zmiany")

        elif user_choice == "5":  #TODO zrób do tego metodę
            print("5. Pokaż ile sztuk danego produktu jes w magazynie")

        elif user_choice == "6":  #TODO zrób do tego osobną klasę
            print("1 - Pokaż najtańszy produkt w magazynie")
            print("2  - Pokażnajdroższy produkt w magazynie")
            print("3 - Pokaż, którego produktu jest najwięcej (kg lub sztuki)")
            print("4 - Pokaż, którego produktu jest najmniej (kg lub sztuki)")
            print("5 -  Pokaż, który produkt najlepiej się sprzedaje")
            print("6 - Pokaż, którego na magazynie jest za mało i trzeba go zamówić")

        elif user_choice == "7":
            print("7. Wyjdź")


class InternetShop:
    # Pętla dla sklepu
    while user_choice != "7": # TODO dodaj rozwiązania z magazynu
        main_menu()

        user_choice = input("Wybierz opcję wpisując odpowiednią cyfrę: ")

        if user_choice == 1:
            print("1. Wyświetl listę produktów")
            print(
                "2. ta lista pokazuje klucze z dict produktów oraz daje nowe opcje wyboru"
            )
            print("3. Wybierz produkt, z którym chcesz się lepiej zapoznać")
            print(
                """4. Przechodzi do podstrony produktu, na której są jego parametry,
                   dane techniczne certyfikaty - w konsoli poprostu printuje wszystkie 
                   wartości z dicta dla danego klucza, na którym zapisane są wszystkie dane produktu """
            )
            print("5. Wróć")

        elif user_choice == "6":
            print("1 - Pokaż najtańszy produkt w magazynie")
            print("2  - Pokażnajdroższy produkt w magazynie")
            print("3 - Pokaż, którego produktu jest najwięcej (kg lub sztuki)")
            print("4 - Pokaż, którego produktu jest najmniej (kg lub sztuki)")
            print("5 -  Pokaż, który produkt najlepiej się sprzedaje")
            print("6 - Pokaż, którego na magazynie jest za mało i trzeba go zamówić")

        elif user_choice == "7":
            print("7. Wyjdź")


# Wybierz czy chcesz wejść do sklepu czy do magazynu
while user_choice != "3":
    print("1. Sklep intenetowy")
    print("2. Magazyn")
    print("3. Wyjdź")
    user_choice = input("Wybierz opcję wpisując odpowiednią cyfrę: ")

    if user_choice == "1":
        pass  ##TODO jak już ogarniesz klasę sklepu to ją tutaj dodaj

    elif user_choice == "2":
        pass  #TODO jak już ogarniesz klasę magazynu to ją tutaj dodaj

    elif user_choice == "3":
        print("Wyszedłeś z aplikacji")
