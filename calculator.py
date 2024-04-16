import logging


def add_num(a, b):
    return a + b


def subtract_num(a, b):
    return a - b


def calculator(a, b):
    user_input = input("Write your addition or subtraction here: ")

    # Usuwanie białych znaków przed i po operatorze
    user_input = user_input.replace(" ", "")

    if "+" in user_input:
        operator = "+"
    elif "-" in user_input:
        operator = "-"
    else:
        logging.error("Unknown operator")
        raise ValueError("Unknown operator")

    # Rozdzielenie wejścia na liczby i operator
    numbers = user_input.split(operator)

    # Wyszukanie indeksów, na których występują liczby a i b
    idx_a = user_input.find(numbers[0])
    idx_b = user_input.find(numbers[1])

    # Sprawdzenie, czy liczby a i b są na pozycjach 0 i 1
    if idx_a < idx_b:
        a = float(numbers[0])
        b = float(numbers[1])
    else:
        a = float(numbers[1])
        b = float(numbers[0])

    if operator == "+":
        result = add_num(a, b)
        logging.info(f"{a} + {b} = {result}")
    elif operator == "-":
        result = subtract_num(a, b)
        logging.info(f"{a} - {b} = {result}")

    return result


if __name__ == "__main__":
    try:
        calculator(0, 1)
    except ValueError as e:
        print("Error:", e)
