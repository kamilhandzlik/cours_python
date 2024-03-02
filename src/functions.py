class Student:
    def __init__(self, first, last, grades) -> None:
        self.first = first
        self.last = last
        self.grades = grades
        self.active = False

    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)

    def set_active(self):
        self.active = True

    def __str__(self) -> str:
        return f"{self.first} {self.last} [str({self.active})]"


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def word_counter(sentence):
    from re import findall

    return len(findall(r"\w+", sentence))


def fibonacci_classic(n):
    if n in {0, 1}:
        return n
    return fibonacci_classic(n - 1) + fibonacci_classic(n - 2)


def fib(n):
    return n if n in [0, 1] else fib(n - 1) + fib(n - 2)
