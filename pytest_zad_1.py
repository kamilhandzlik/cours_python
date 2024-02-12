from random import randint

def function(i):
    if not isinstance(i, int):
        raise ValueError("Input must be an integer")

    if i % 5 == 0 and i % 3 == 0:
        return "Pif Paf"
    elif i % 5 == 0:
        return "Pif"
    elif i % 3 == 0:
        return "Paf"
    else:
        return ""

def run_tests():
    # Funkcja do porównywania wyników
    def assert_equals(actual, expected):
        assert actual == expected, f"Expected {expected}, but got {actual}"

    # Testy dla funkcji `function`
    print("Testing function:")

    # Test 1
    result = function(15)
    expected_result = "Pif Paf"
    assert_equals(result, expected_result)
    print("Test 1 passed")

    # Test 2
    result = function(10)
    expected_result = "Pif"
    assert_equals(result, expected_result)
    print("Test 2 passed")

    # Test 3
    result = function(9)
    expected_result = "Paf"
    assert_equals(result, expected_result)
    print("Test 3 passed")

    # Test 4
    result = function(7)
    expected_result = ""
    assert_equals(result, expected_result)
    print("Test 4 passed")



    # Test 6 - przypadkowe liczby
    for _ in range(40):
        random_number = randint(-1000, 1000)
        result = function(random_number)
        print(f"Testing with {random_number}: {result}")

    # Test 7 - sprawdzenie czy wprowadzona zmienna jest integerem
    try:
        result = function("abc")
    except ValueError as e:
        assert str(e) == "Input must be an integer"
        print("Test 7 passed")

# Uruchomienie testów
if "__main__" == __name__:
    run_tests()
