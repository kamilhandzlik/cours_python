# Wzorzec projektowy builder
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
