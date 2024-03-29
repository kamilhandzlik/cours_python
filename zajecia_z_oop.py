from lista_biurek_do_CoWork import desks_instances


def show_desks():
    desk_index = 0
    for desk in desks_instances:
        print(desk + " [" + str(desk_index) + "]")
        desk_index += 1


def add_desk():
    desk = input("Dodaj biurko: ")
    desks_instances.append(desk)
    print("Dodano biurko!")


def delete_desk():
    desk_index = int(input("Podaj indeks biurka do usunięcia: "))

    if desk_index < 0 or desk_index > len(desks_instances) - 1:
        print("Biurko o tym indeksie nie istnieje")
        return

    desks_instances.pop(desk_index)
    print("Usunięto biurko!")


def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for desk in desks_instances:
        file.write(desk + "/n")
    file.close()


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
            print("7. REGULAMIN USŁUGI I OPCJE PŁATNOŚCI")
        elif user_choice != "8":
            print(f"Przepraszam, wybrałeś {user_choice}, nie jest to poprawny wybór")


def admin_board():
    user_choice = ""

    while user_choice != "8":
        print_menu_admin()
        user_choice = input("Wybierz opcję wybierając odpowiednią cyfrę:")

        if user_choice == "1":
            print(desks_instances)
        elif user_choice == "2":
            add_desk()
        elif user_choice == "3":
            print("3. USUWANIE BIURKA/STANOWISKA")
        elif user_choice == "4":
            print("4. ANULOWANIE REZERWACJI")
        elif user_choice == "5":
            print("5. EDYCJA REGULAMINU USŁUG")
        elif user_choice == "6":
            print("6. EDYCJA DANYCH KONTAKTOWYCH")
        elif user_choice == "7":
            save_tasks_to_file()
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
    print("7. WYJŚCIE Z APLIKACJI/WYLOGOWANIE")
    print("8. WYJŚCIE Z APLIKACJI")


def main_menu():
    user_input = -1

    while user_input != "3":
        if user_input == "1":
            print("Panel Klienta")
            print("Zalogowałeś się do panelu klienta")

            customer_board()

        elif user_input == "2":
            print("PANEL ADMINISTRATORA ")
            print("Zalogowałeś się do panelu administratora")

            admin_board()

        else:
            print(f"Przepraszam, wybrałeś {user_input}, nie jest to poprawny wybór")

        print("1. Zaloguj się jako klienta")
        print("2. Zaloguj się jako administratora ")
        print("3. WYJŚCIE Z APLIKACJI")

        user_input = input("Wybierz panel do którego chcesz się zalogować: ")


if __name__ == "__main__":
    main_menu()
