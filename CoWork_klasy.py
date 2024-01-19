class Desks:
    def __init__(self, name, desk_type, price, status):
        self.name = name
        self.desk_type = desk_type
        self.price = price
        self.status = status


# Create instances for each entry in the dictionary
desks_instances = {
    "Biurko nr 1": Desks("Biurko pojedyncze bez monitora, trzy gniazdka", 50, "czynne"),
    "Biurko nr 2": Desks("Biurko pojedyncze bez monitora, trzy gniazdka", 50, "czynne"),
    "Biurko nr 3": Desks("Biurko pojedyncze bez monitora, trzy gniazdka", 50, "czynne"),
    "Biurko nr 4": Desks("Biurko pojedyncze bez monitora, trzy gniazdka", 50, "czynne"),
    "Biurko nr 5": Desks("Biurko pojedyncze bez monitora, trzy gniazdka", 50, "czynne"),
    "Biurko nr 6": Desks("Biurko pojedyncze z monitorem, trzy gniazdka", 80, "czynne"),
    "Biurko nr 7": Desks("Biurko pojedyncze z monitorem, trzy gniazdka", 80, "czynne"),
    "Biurko nr 8": Desks("Biurko pojedyncze z monitorem, trzy gniazdka", 80, "czynne"),
    "Biurko nr 9": Desks("Biurko pojedyncze z monitorem, trzy gniazdka", 80, "czynne"),
    "Biurko nr 10": Desks("Biurko pojedyncze z monitorem, trzy gniazdka", 80, "czynne"),
    "Biurko nr 11 -14": Desks(
        "Biurko 4 osobowe bez monitorów, dwanaście gniazdek", 40, "czynne"
    ),
    "Biurko nr 15 -18": Desks(
        "Biurko 4 osobowe bez monitorów, dwanaście gniazdek", 40, "czynne"
    ),
    "Biurko nr 19 -22": Desks(
        "Biurko 4 osobowe bez monitorów, dwanaście gniazdek", 40, "czynne"
    ),
    "Biurko nr 23 -26": Desks(
        "Biurko 4 osobowe bez monitorów, dwanaście gniazdek", 40, "czynne"
    ),
    "Biurko nr 27 -30": Desks(
        "Biurko 4 osobowe bez monitorów, dwanaście gniazdek", 40, "czynne"
    ),
    "Biurko nr 31 -34": Desks(
        "Biurko 4 osobowe z monitorami, dwanaście gniazdek", 65, "czynne"
    ),
    "Biurko nr 35 -38": Desks(
        "Biurko 4 osobowe z monitorami, dwanaście gniazdek", 65, "czynne"
    ),
    "Biurko nr 39 -42": Desks(
        "Biurko 4 osobowe z monitorami, dwanaście gniazdek", 65, "czynne"
    ),
    "Biurko nr 43 -46": Desks(
        "Biurko 4 osobowe z monitorami, dwanaście gniazdek", 65, "czynne"
    ),
    "Biurko nr 47 -50": Desks(
        "Biurko 4 osobowe z monitorami, dwanaście gniazdek", 65, "czynne"
    ),
    "Biurko nr 51 -60": Desks(
        "Biurko 10 osobowe bez monitorów, trzydzieści gniazdek", 25, "czynne"
    ),
    "Biurko nr 61 -70": Desks(
        "Biurko 10 osobowe bez monitorów, trzydzieści gniazdek", 25, "czynne"
    ),
    "Biurko nr 71 -80": Desks(
        "Biurko 10 osobowe z monitorami, trzydzieści gniazdek", 40, "czynne"
    ),
    "Biurko nr 81 -90": Desks(
        "Biurko 10 osobowe z monitorami, trzydzieści gniazdek", 40, "czynne"
    ),
}


# Now, desks_instances is a dictionary where keys are desk names, and values are instances of the Desks class
