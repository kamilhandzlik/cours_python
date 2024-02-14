#####################################################################################
###############   BUILDER      ###################################################
#####################################################################################


# Wzorzec projektowy Builder
from typing import Optional


# Krok 1
# Z diagramu UML z zajęć jest to odpowiednik Product 1 Builder
# Definiuje Produkt który chcemy budować
class APIEndpoint:
    path: Optional[str]
    method: Optional[str]
    status: Optional[int]
    description: Optional[str]


# Krok 2
# Z diagramu UML z zajęć jest to odpowiednik Product  Builder
# Interfejs, który będzie mówił jakie rzeczy będziemy mogli na tym produkcie ustalić
class APIEndpointBuilder:
    def set_path(self):
        raise NotImplementedError

    def set_method(self):
        raise NotImplementedError

    def set_status(self):
        raise NotImplementedError

    def set_description(self):
        raise NotImplementedError


# Krok 3
# Z diagramu UML z zajęć jest to odpowiednik Product Directory
# Ta klasa zobowiązuje wykonywać się wszystkie metody, które są zdefiniowane w interfejsie
class GetAPIEndpointBuilder(APIEndpointBuilder):
    # To jest konstruktor produktu, który nic w sobie nie będzie miał
    # czyli jest to produkt, który w sobie nie ma żadnych atrybutów
    def __init__(self):
        self.api_endpoint = APIEndpoint()

    def set_path(self, path) -> "GetAPIEndpointBuilder":
        self.api_endpoint.path = path
        return self

    def set_method(self, method):
        self.api_endpoint.method = method
        return self

    def set_status(self, status):
        self.api_endpoint.status = status
        return self

    def set_description(self, description):
        self.api_endpoint.description = description
        return self

    def build(self) -> "APIEndpoint":
        return self.api_endpoint


get_api_endpoint_builder = GetAPIEndpointBuilder()

GET_ENDPOINTS = {}

first_get_endpoint = (
    get_api_endpoint_builder.set_path("/home")
    .set_method("GET")
    .set_status(200)
    .set_description("Zwraca główną stronę internetową")
    .build()
)

second_get_endpoint = (
    get_api_endpoint_builder.set_path("/shop")
    .set_method("GET")
    .set_status(200)
    .set_description("Zwraca stronę zwracającą sklep internetowy")
    .build()
)

# Bez użycia vars()
GET_ENDPOINTS["/home"] = {
    "path": first_get_endpoint.path,
    "method": first_get_endpoint.method,
    "status": first_get_endpoint.status,
    "description": first_get_endpoint.description,
}

GET_ENDPOINTS["/shop"] = {
    "path": second_get_endpoint.path,
    "method": second_get_endpoint.method,
    "status": second_get_endpoint.status,
    "description": second_get_endpoint.description,
}

print(GET_ENDPOINTS["/home"])
print(GET_ENDPOINTS["/shop"])


#####################################################################################
###############   FACTORY      ###################################################
#####################################################################################
# Wzorzec projektowy Fabryka


# Krok 1 Definiujemy interfejs, który chcemy stworzyć
# Interfejs Product z diagramu UML
class Computer:
    ram_size: int = 0

    def power_on(self):
        raise NotImplementedError

    def power_off(self):
        raise NotImplementedError


# Krok 2 - Konkretne klasy o podobnych zachowaniach
# Concrete Product 1
class Laptop(Computer):
    ram_size = 4096

    def power_on(self):
        return "Laptop powered on"

    def power_off(self):
        return "Laptop powered off"


# Concrete Product 2
class PC(Computer):
    ram_size = 8192

    def power_on(self):
        return "PC powered on"

    def power_off(self):
        return "PC powered off"


# Krok 3 - Implementujemy fabryki wersja 1 i 2 "WAŻNE!!" MUSZĄ ZAWIERAĆ METODĘ """create """
# To jest interfejs Product Factory z diagramu UML
class ComputerFactory:
    def create(self) -> "Computer":
        raise NotImplementedError


# To jest Product 1 Factory z diagramu UML
class LaptopFactory(ComputerFactory):
    def create(self) -> Computer:
        print("Tworzy Laptop")
        return Laptop()


# To jest Product 2 Factory z diagramu UML
class PCFactory(ComputerFactory):
    def create(self) -> Computer:
        print("Tworzy PC")
        return PC()


# Krok 4 implementujemy konkretny produkt
# Tworzymy słownik, który będzie przechowywał nam nasze fabryki
COMPUTER_FACTORIES = {"PC": PCFactory, "Laptop": LaptopFactory}

# Jeśli chcemy użyć naszej fabryki tutaj przychodzi nam request
# użytkownik chce stworzyć PC
request = {"create": "PC"}

# Wiedząc, że wszystkie fabryki mają ten sam interfejs odzyskujemy ze słownika
# to co użytkownik przesłał nam w zapytaniu

computer_to_make = request["create"]
# na podstawie requesta tworzymy instancję dla użytkownika za pomocą metody create
COMPUTER_FACTORIES[computer_to_make].create


# WZORCE BEHAWIORALNE
# BEHAVIOURAL DESIGN PATTERNS

#####################################################################################
###############   STRATEGY       ###################################################
#####################################################################################
# Wzorzec projektowy Strategy


# Przykład dla dzielenia rachunków w restauracji na podstawie ilości ludzi


# Krok 1 deinicja interfejsu strategi i konkretnych klas
# Interfejs
class BillingStrategy:
    def calculate(self, amount):
        raise NotImplementedError


# Konkretna klasa 1
class OverTenPeopleBillingStrategy(BillingStrategy):
    def calculate(self, amount):
        # tutaj dolicz 10% do rachunku gdy jest więcej niż 10 ludzi do zapłaty
        return amount * 1.1


# Konkretna klasa 2
class NormaBillingStrategy(BillingStrategy):
    def calculate(self, amount):
        # zwykła płatność bez promocji
        return amount


# Konkretna klasa 3
class OwnerBillingStrategy(BillingStrategy):
    def calculate(self, amount):
        # Właściciel za nic nie płaci
        return 0


# Krok 2
# Definicja kontekstu
class BillingContext:
    def __init__(self):
        self._strategy: BillingContext = NormaBillingStrategy()

    def set_strategy(self, Strategy: BillingStrategy):
        self._strategy = Strategy()

    def calculate(self, amount):
        return self._strategy.calculate(amount)


# Krok 3
# Wymagany jest tylko jeden kontekst
billing_context = BillingContext()

# Zmieniaj w zależności od wymaganej sytuacji
billing_context.set_strategy(NormaBillingStrategy)
billing_context.calculate()

billing_context.set_strategy(OwnerBillingStrategy)
billing_context.calculate()

billing_context.set_strategy(OverTenPeopleBillingStrategy)
billing_context.calculate()
