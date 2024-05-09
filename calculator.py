import logging

user_input = 0


def add_num(a, b):
    return a + b


def subtract_num(a, b):
    return a - b


def calculator(a, b):
    user_input = input("Write your addition or subtraction here:")

    if not isinstance(a, (int or float)) or not isinstance(b, (int or float)):
        if not isinstance(a, (int or float)):
            logging.error(f"{a} is not a number")
            raise ValueError(f"{a} is not a number")
        elif not isinstance(b, (int or float)):
            logging.error(f"{b} is not a number")
            raise ValueError(f"{b} is not a number")

    inputs = user_input.split()
    a = None
    b = None

    for element in inputs:
        try:
            num = float(element)
        except ValueError:
            print(f"'{element}' nie jest liczbą. Pomijam.")
            continue

        if a is None:
            a = num
        else:
            b = num
            break

    if "+" in user_input:
        result = add_num(a, b)
        logging.info(f"{a} + {b} = {result}")

    elif "-" in user_input:
        result = subtract_num(a, b)
        logging.info(f"{a} - {b} = {result}")

    else:
        logging.error("Unknown operator")
        raise ValueError("Unknown operator")

    return result


if __name__ == "__main__":
    calculator(1, 2)
