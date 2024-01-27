class Produkt:
    def __init__(
        self,
        type_of_prod,
        name,
        description,
        technical_data,
        num_of_items_in_magazine,
        price,
    ):
        self.type_of_prod = type_of_prod
        self.name = name
        self.description = description
        self.technical_data = technical_data
        self.num_of_items_in_magazine = num_of_items_in_magazine
        self.price = price

    def show_all_info_about_products(self):
        print(
            f"""Nazwa {self.name}, Typ materiału {self.type_of_prod},
               Opis {self.description}, Dane techniczne {self.technical_data} 
               - Cena: {self.price} PLN, Dostępność: {self.num_of_items_in_magazine} sztuk"""
        )


class Magazyn:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def wyswietl_produkty(self):
        print("Produkty w magazynie:")
        for produkt in self.produkty:
            produkt.show_all_info_about_products()


class SklepInternetowy:
    def __init__(self):
        self.magazyn = Magazyn()

    def dodaj_produkt_do_magazynu(self, produkt):
        self.magazyn.dodaj_produkt(produkt)

    def wyswietl_produkty_w_sklepie(self):
        self.magazyn.wyswietl_produkty()

    def internet_shop_main_menu(self):
        print("1. Wyświetl listę produktów")
        print("2. Dodaj produkt")
        print("3. Usuń produkt")
        print("4. Zapisz zmiany")
        print("5. Pokaż ile sztuk danego produktu jest w magazynie")
        print("6. Pokaż zestawienia")
        print("7. Wyjdź")

    def handle_user_choice(self, user_choice):
        if user_choice == "1":
            self.wyswietl_produkty_w_sklepie()
        elif user_choice == "2":
            self.dodaj_produkt_do_magazynu(self.create_produkt())
        # Dodaj obsługę pozostałych opcji

    def create_produkt(self):
        # Funkcja do tworzenia nowego produktu na podstawie danych wprowadzonych przez użytkownika
        # Możesz użyć input() do pobrania danych od użytkownika
        pass


# Przykładowe użycie: TODO - do zmiany sposób użycia i wywołania
sklep = SklepInternetowy()


# Sklep Internetowy
def internet_shop():
    while user_choice != "7":
        sklep.internet_shop_main_menu()
        user_choice = input("Wybierz opcję wpisując odpowiednią cyfrę: ")
        sklep.handle_user_choice(user_choice)


def magazine():
    pass  # TODO Zrób pętlę z magazynem


user_choice = ""
# Wybierz czy chcesz wejść do sklepu czy do magazynu
while user_choice != "3":
    print("1. Sklep intenetowy")
    print("2. Magazyn")
    print("3. Wyjdź")
    user_choice = input("Wybierz opcję wpisując odpowiednią cyfrę: ")

    if user_choice == "1":
        internet_shop()

    elif user_choice == "2":
        magazine()

    elif user_choice == "3":
        print("Wyszedłeś z aplikacji")
