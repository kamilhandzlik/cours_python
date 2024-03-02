from src.main import *
import pytest
from math import sqrt


@pytest.fixture
def example_user():
    return {"first": "Piotr", "phone": "900800100"}


@pytest.mark.parametrize(
    "arg1, arg2, result", [(5, 10, 15), (4, 6, 10), (-1, -10, -11), (0, 0, 0)]
)
def test_add_with_params(arg1, arg2, result):
    r = add_two_numbers(arg1, arg2)
    assert r == result


@pytest.mark.parametrize("in_number, expected", [(8, 4), (10, 5), (12, 6)])
def test_divide_by_two(in_number, expected):
    result = divide_two_numbers(in_number, 2)
    assert result == expected


def test_add():
    assert add_two_numbers(5, 10) == 15
    assert add_two_numbers(-12, 2) == -10


def test_divide():
    assert divide_two_numbers(4, 2) == 2
    assert divide_two_numbers(7, 2) == 3.5


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as E:
        divide_two_numbers(10, 0)
    assert str(E.value) == "division by zero"


def test_math_domain():
    with pytest.raises(ValueError) as E:
        add_two_numbers(sqrt(-1), 0)
    assert "domain" in str(E.value)


def test_select_first(example_user):
    assert select_info(example_user["first"]) == "PIOTR"


def test_select_phone(example_user):
    assert select_info(example_user["phone"]) == "+48" + example_user["phone"]
