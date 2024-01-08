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



##############################
#####   1    #################
##############################
from dataclasses import dataclass       #import metody potrzebnej do wykonania sposobu pierwszego

#Tworzenie klas
@dataclass                                  #Inicjalizowanie sposobu pierwszego
                                            #Inicjowanie atrybutów klasymożna to zrobić na dwa sposoby 
class Person:                             #Tworzenie klasy i jej nazywanie (nawias może być pusty lub nawiązywać do jakiegpś obiektu bądź klasy)
    first_name: str                         #Tworzenie atrybutów klasy sposób 1
    last_name: str                          # Podajesz ich nazwę a następnie typ
    age: int
    weight: int = 0  # Dodanie atrybutu weight z domyślną wartością 0
    
    def __init__(self, first_name, last_name, age):     # sposób 2   #nazywasz atrybuty      
        self.first_name = first_name                    # inicjalizujesz atrybuty
        self.last_name = last_name
        self.age = age                                  #self można tłumaczyć jako "należy do instancji"



    def speak(self):         #to jest metoda klasy- w zasadzie wszystkie ffunkcje w klasie poza  init i new są metodami    #wywoływanie jakiejś akcji z atrybutów  #nie trzeba podawać atrybutów 
        print(f"Hi I am called {self.first_name} {self.last_name}, and my age is {self.age}")
        if hasattr(self, 'weight'):  # Sprawdzenie, czy atrybut weight istnieje
            print(f"I weight {self.weight} kg")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

    def talk(self):
        print("I am talking")


tim = Person('Tim', 'Ferguson', 24)                 #Tworzenie instancji
fred = Person('Fred', 'Porborne', 25)               #Tworzenie drugiej instancji
tim.change_age(5)                                   #zmiana wartości atrynutu instancji
tim.add_weight(70)                                  #dodawanie atrybutu instancji
tim.speak()                                         #Wywoływanie instancji - metody
fred.speak()


##############################
#####   2    #################
##############################

#Dziedziczenie
class Cat(Person):                                  #Dziedziczenie po klasie Person     
    def __init__(self, first_name, age, color):     #inicjalizowanie atrybutów po klasie z której ta klasa dziedziczy i dodawanie nowych atrybutów
        super().__init__(first_name,"" , age)           
        self.color = color                          #inicjowanie nowych atrybutów

    def talk(self):
        print("Meow!")                              #możemy nadpisywać klasy dziedziczone z nad klasy 

tim = Cat('tim', 5, 'blue')
    

##############################
#####   2    #################
##############################

#zadanie z klass - stworzenie podstawowego kalkulatora punktów z zmiennymi poza klasą

class Point:
    def __init__(self, x=0, y=0, coords=(0, 0)):
        self.x = x
        self.y = y
        coords = (self.x, self.y)

    def move(self, x, y):
        self.x +=  x
        self.y += y
                                                            # dodawanie
    def __add__(self, p):                                   # w tej metodzie jeśli poza metodą mamy p1 + p2 to p2 staje się self a p1 p 
        return Point(self.x + p.x, self.y + p.y)             #bierzemy koordynaty p1 i dodajemy je do koordynatów p2
                                                            #odejmowanie
    def __sub__(self, p):                                    
        return Point(self.x - p.x, self.y - p.y) 
                                                            #mnożenie
    def __mul__(self, p):                                   # to mnożenie nie zwraca wektora po kuntach a skalar 
        return self.x * p.x, self.y * p.y
                                                            #porównuję punkty na porstawie ich odległości od  punkty  (0, 0) w osiach x i y
    def lenght(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
                                                            # porównanie zwóci wartości boolowskie
    def __gt__(self, p):                                     #większe
        return self.lenght() > p.lenght()
    
    def __ge__(self, p):                                    #Większe równe
        return self.lenght() >= p.lenght()
 
    def __lt__(self, p):                                    #mniejsze
        return self.lenght() < p.lenght()
 
    def __le__(self, p):                                    #mniejsze równe
        return self.lenght() <= p.lenght()
                                                            #równe
    def __eq__(self, p):
       pass # return self.lenght() == p.lenght() 

    def __str__(self) -> str:                               # tametoda sprawia, że zamiast miejsca w pamięci printuje się obiekt
        return f"({str(self.x)}, {str(self.y)})"            # nie dostajemy wówczas czegoś takiego:
                                                            # <__main__.Point object at 0x0000019A9890BA10> <__main__.Point object at 0x0000019A9890BA9
                                                            # tylko ładny zapis
                                                            # (6 , 6) (-3 , -3) (3, 6)


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7)
print(p1 > p2)
print(p7 == p6)



##############################
#####   3    #################
##############################

################################
# Metody statyczne metody klas##
################################
class Dog:
    dogs = []                           # zmienna lokalna w klasie
                                        # dobrą praktyką jest podawać zmienne lokalne w  klasie właśnie w ten sposób
                                        # pod warunkiem jednak, że taka zmienna ma być statyczna i się nie ędzie zmieniać w kodzie
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)          #referencje do takiej zmiennej możesz robić tak samo jak do atrybutów

    @classmethod                        #to jest dekorator dodajesz go jak chcesz pokazać, że jest to specjalny typ metody
    def num_dogs(cls):
        return len(cls.dogs)
    
    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")

    def __str__(self) -> str:               #nie musisz mieć referencji do czego kolwiek w klasie możemy mieć jakie parametry chcemy nie potrzeba w nich self ani cls
        return "My name is" +  str(self.name)

tim = Dog("Tim")
jim = Dog("Jim")
print(Dog.dogs)                         #wywołanie zmiennej loklnej i jej instancji
print(Dog.num_dogs())                   #wywołanie classmethod - działa praktycznie tak samo jak wszystkie .strip() .join() .count()
Dog.bark(5)                             #wywołanie metody statycznej - używasz jej kiedy chesz użyc funcji jako funkcji chcesz mieć ją zapisaną w klasie
                                        #ale nie chcesz żeby miała interakcję z klasą co więcej nie musisz mieć wypisanych żadnych instancji klasy żeby móc wywołać metodę statyczną

##############################
#####   4    #################
##############################

################################
# Klasy prywatne i publiczne ###
################################
# Klasy prywatne tworzy się prze jeden podkreślnik przed nazwą klasy
# Jako takich i w pythonie nie ma ale _ pozwala określić sobie i innym programistą, że dana klasa faktycznie jest prywatna
# Klasy prywatna może być użyta tylko w jednym pliku lub zakresie a publiczna może być użyta wszędzie

class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("hello")

    def display(self):
        print("Hi")


