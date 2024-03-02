from src.functions import *
import pytest
from math import sqrt


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_word_count():
    assert word_counter("Hello World") == 2
    assert word_counter("This is a sentence with seven words.") == 7
    assert word_counter("") == 0
    assert word_counter("Wonder if " + "it will" + " work") == 5
    assert word_counter("This is a sentence , with\n seven words.") == 7


def test_fibonacci():
    assert fibonacci_classic(0) == 0
    assert fibonacci_classic(1) == 1
    assert fibonacci_classic(2) == 1
    assert fibonacci_classic(3) == 2
    assert fibonacci_classic(5) == 5
    assert fib(6) == 8
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5


def test_math_domain():
    with pytest.raises(ValueError) as E:
        factorial(sqrt(-1))
        fibonacci_classic(sqrt(-1))
        fib(sqrt(-1))
        factorial("A")
        fibonacci_classic("A")
        fib("A")
    assert "domain" in str(E.value)


@pytest.mark.parametrize(
    "grades, expected",
    [
        ((5, 10), 7.5),
        ((4, 6), 5),
        ((8, 8), 8),
        ((0, 0, 0), 0),
        ((8, 42), 25),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10), 4.090909090909091),
    ],
)
def test_avg_grades(grades, expected):
    student = Student("John", "Doe", grades)
    result = student.get_avg_grade()
    assert result == expected


@pytest.mark.parametrize(
    "first, last, grades",
    [
        ("John", "Doe", [90, 85, 92]),
        ("Jane", "Smith", [80, 88, 95]),
        ("Alice", "Johnson", [75, 79, 82]),
    ],
)
def test_set_active(first, last, grades):
    student = Student(first, last, grades)
    assert not student.active
    student.set_active()
    assert student.active


@pytest.mark.parametrize(
    "first, last, grades, expected_str",
    [
        ("John", "Doe", [90, 85, 92], "John Doe [str(False)]"),
        ("Jane", "Smith", [80, 88, 95], "Jane Smith [str(False)]"),
        ("Alice", "Johnson", [75, 79, 82], "Alice Johnson [str(False)]"),
    ],
)
def test_str_representation(first, last, grades, expected_str, capsys):
    student = Student(first, last, grades)
    print(student)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_str
