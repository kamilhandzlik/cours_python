import sys  # Dodano import sys, aby użyć sys.getrefcount

class Example:
    def __init__(self):
        self.value = 5

x = 5
y = 5
z = {'a': 1, 'b': 2, 'c': 3}
obj = Example()  # Poprawiono tworzenie obiektu Example

# Przy poniższym zapisie wypisana zostanie nazwa referencji oraz obiekt, do którego się odnosi
# Dalej pokazane jest miejsce w pamięci
print(f"{x=}", id(x))
print(f"{y=}", id(y))

x += 5

print(f"{x=}", id(x))
print(f"{y=}", id(y))

# To jest to samo, co id(x) == id(y)
print(x is y)

print(vars(obj))  # Wywołanie funkcji vars - musi odnosić się do obiektu, a ta musi mieć __init__()
                  # Ponadto vars przyjmuje tylko jeden argument

print(sys.getrefcount(5))  # Dodano import sys i poprawiono argument funkcji getrefcount

#Lista jest klasą i typem ale niekompletnym
# list[str] nie jest klasą jest to generic alias

print(type(list[str]))  # Działa na wersji 3.10 wzwyż

#dla starszych wersji
from typing import List

print(List[str])


# Tworzenie obiektów mutable i immutable
class Object_0:
    def __init__(self, x):
        self.x = x

class Object_1:
    def __init__(self, y):
        self.y = y

obiekt_mutable = Object_0(10)
obiekt_immutable = Object_1(10)

print(obiekt_mutable, obiekt_mutable.x, id(obiekt_mutable))
print(obiekt_immutable, obiekt_immutable.y, id(obiekt_immutable))

# Wprowadzenie zmiany do obiektu mutable
obiekt_mutable.__init__(5)

# Zmiana wartości atrybutu y dla obiektu immutable nie jest możliwa po utworzeniu obiektu
# obiekt_immutable.__init__(5)  # To spowoduje błąd AttributeError

print(obiekt_mutable, obiekt_mutable.x, id(obiekt_mutable))
print(obiekt_immutable, obiekt_immutable.y, id(obiekt_immutable))

