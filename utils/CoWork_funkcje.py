from CoWork_klasy import Desks, desks_instances

def show_admin_desks_view():
    print("Admin Desks View:")
    for keys, values in desks_instances.items():
        print(keys, values)


def add_desk():
    name = input("Podaj nazwę biurka: ")
    desk_type = input("Podaj typ biurka: ")
    price = float(input("Podaj cenę biurka PLN/h: "))
    status = input("Podaj status biurka: ")

    new_desk = Desks(name, desk_type, price, status)
    desks_instances[name] = new_desk
    print("Dodano biurko!")


def delete_desk():
    desk_index = int(input("Podaj indeks biurka do usunięcia: "))

    if desk_index < 0 or desk_index > len(desks_instances) - 1:
        print("Biurko o tym indeksie nie istnieje")
        return

    desks_instances.pop(desk_index)
    print("Usunięto biurko!")


def save_tasks_to_file():
    with open("desks.json", "w") as file:
        for desk in desks_instances:
            file.write(f"{desk.desk_type}, {desk.price}, {desk.status}\n")
    print("Zapisano biurka do pliku.")
