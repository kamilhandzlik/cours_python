from datetime import datetime

class Human:
    def __init__(self, name, surname, birthdate, gender, living_location, name_of_mother, name_of_father):
        self.name = name
        self.surname = surname
        self.birthdate = self.validate_birthdate(birthdate)
        self.gender = gender
        self.living_location = living_location
        self.name_of_mother = name_of_mother
        self.name_of_father = name_of_father

    

class User(Human):
    def __init__(cls, name, surname, birthdate, gender, living_location, name_of_mother, name_of_father):
        super().__init__(name, surname, birthdate, gender, living_location, name_of_mother, name_of_father)

    def validate_birthdate(self, birthdate):
        try:
            birthdate_obj = datetime.strptime(birthdate, "%d/%m/%Y").date()
            return birthdate_obj
        except ValueError:
            raise ValueError("Invalid date format. Use dd/mm/YYYY.")

    @property
    def age(self):
        today = datetime.now().date()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age


if __name__ == "__main__":
    # Przykład użycia
    user1 = User("John", "Doe", "01/01/1990", "Male", "Portland", "Mary Doe", "John Doe Senior")
    user2 = User("Garry", "Sue", "12/12/1999", "Male", "Maine", "Mary Sue", "James Sue")
    print(f"{user1.name} {user1.surname} is {user1.age} years old. Lives in {user1.living_location}."
          , f"Son of {user1.name_of_mother} and {user1.name_of_father}.")
    print(f"{user2.name} {user2.surname} is {user2.age} years old. Lives in {user2.living_location}.",
          f"Son of {user2.name_of_mother} and {user2.name_of_father}.")