from CoWork_klasy import *
import json


def show_admin_desks_view():
    print("Admin Desks View:")

    try:
        with open("desks.json", "r") as file:
            desks_instances = json.load(file)

            if not desks_instances:
                print("Brak biurek do wyświetlenia.")
                return

            for name, desk_data in desks_instances.items():
                print(f"{name}: {json.dumps(desk_data, indent=2)}")

    except FileNotFoundError:
        print("Plik desks.json nie istnieje. Brak biurek do wyświetlenia.")


def add_desk():
    desks_instances = load_desks_from_file("desks.json")

    idx = len(desks_instances.keys()) + 1
    name = input("Podaj nazwę biurka: ")
    desk_type = input("Podaj typ biurka: ")
    monitor = input("Czy biurko ma monitor? (True/False): ").lower() == "true"
    rozmiar = int(input("Podaj rozmiar biurka: "))
    price = float(input("Podaj cenę biurka PLN/h: "))
    status = input("Podaj status biurka: ")

    new_desk = Desks(idx, name, desk_type, monitor, rozmiar, price, status)
    desks_instances[idx] = new_desk
    print("Dodano biurko!")

    save_desks_to_file(desks_instances)


def delete_desk():
    desks_instances = load_desks_from_file("desks.json")

    print("Aktualne Biurka:")
    for idx, (key, desk) in enumerate(desks_instances.items()):
        print(f"{idx + 1}. {desk['name']}")

    if not desks_instances:
        print("Brak dostępnych biurek do usunięcia.")
        return

    try:
        del_desk_idx = int(input(
            "Podaj numer biurka do usunięcia (lub wpisz -1, aby anulować): "
        )) - 1

        if del_desk_idx == -1:
            print("Anulowano usunięcie.")
            return

        if 0 <= del_desk_idx < len(desks_instances):
            deleted_desk_name = list(desks_instances.keys())[del_desk_idx]
            desks_instances.pop(deleted_desk_name)
            print(f"Usunięto biurko: {deleted_desk_name}")
        else:
            print("Nieprawidłowy numer biurka. Nie usunięto żadnego biurka.")

        save_desks_to_file(desks_instances)

    except ValueError:
        print("Nieprawidłowe dane wejściowe. Podaj prawidłowy numer biurka.")


def save_desks_to_file(desks_instances):
    with open("desks.json", "w") as file:
        data = {}
        for name, desk in desks_instances.items():
            data[name] = desk.to_dict()
        json.dump(data, file, indent=2)
    print("Zapisano biurka do pliku.")


def customer_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_customer()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print("1. NASZA OFERTA")
        elif user_choice == "2":
            print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
        elif user_choice == "3":
            print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
        elif user_choice == "4":
            print("4. REZERWACJA BIURKA")
        elif user_choice == "5":
            print("5. ANULOWANIE REZERWACJI")
        elif user_choice == "6":
            print("6. DANE KONTAKTOWE BIURA")
        elif user_choice == "7":
            print(
                """
            7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI
            nie mamy jeszcze regulaminu i opcji płatności, ale stworzymy tekst i wrzucimy
                  """
            )
        elif user_choice == "8":
            print("8. WYJŚCIE Z APLIKACJI")
        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def admin_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_admin()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
            show_admin_desks_view()

        elif user_choice == "2":
            print("2. DODWANIE BIURKA/STANOWISKA")
            add_desk()

        elif user_choice == "3":
            print("3. USUWANIE BIURKA/STANOWISKA")
            delete_desk()

        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
        elif user_choice == "5":
            print("5. EDYCJA REGULAMINU USŁUG")
        elif user_choice == "6":
            print("6. EDYCJA DANYCH KONTAKTOWYCH")
        elif user_choice == "7":
            print("7. ZAPISZ ZMIANY")
            save_desks_to_file()

        elif user_choice != "8":
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def print_menu_customer():
    print("1. NASZA OFERTA")
    print("2. SZCZEGÓŁOWE SPECYFIKACJE ORAZ CENNIK USŁUG")
    print("3. DOSTĘPNOŚĆ BIUREK/STANOWISK")
    print("4. REZERWACJA BIURKA")
    print("5. ANULOWANIE REZERWACJI")
    print("6. DANE KONTAKTOWE BIURA")
    print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
    print("8. WYJŚCIE Z APLIKACJI")


def print_menu_admin():
    print("1. LISTA REZERWACJI I DANE SUMARYCZNE")
    print("2. DODWANIE BIURKA/STANOWISKA")
    print("3. USUWANIE BIURKA/STANOWISKA")
    print("4. ANULOWANIE REZERWACJI")
    print("5. EDYCJA REGULAMINU USŁUG")
    print("6. EDYCJA DANYCH KONTAKTOWYCH")
    print("7. ZAPISZ ZMIANY")
    print("8. WYJŚCIE Z APLIKACJI")


def main_menu():
    user_choice = ""

    while user_choice != "3":
        print("1. Zaloguj się jako klienta")
        print("2. Zaloguj się jako administratora ")
        print("3. WYJŚCIE Z APLIKACJI")
        user_choice = input("Wybierz panel do którego chcesz się zalogować: ")

        if user_choice == "1":
            print("Panel Klienta")
            print("Zalogowałeś się do panelu klienta")

            customer_board()

        elif user_choice == "2":
            print("PANEL ADMINISTRATORA ")
            print("Zalogowałeś się do panelu administratora")

            admin_board()

        else:
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


if __name__ == "__main__":
    main_menu()
