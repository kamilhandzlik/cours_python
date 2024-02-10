"""
    Mamy poniższe funkcje:

    def time_shift(x: int, elements: tuple) -> list:
    	return sum(elements) / x

    def time_travel(start: datetime, duration: int) -> datetime:
    	# duration to wynik powyższej funkcji
    	from datetime import datetime, timedelta
    	return start += timedelta(minutes=duration)

    Przygotuj testy
"""
from datetime import datetime, timedelta


def time_shift(x: int, elements: tuple) -> list:
    return elements[0] / x


def time_travel(start: datetime, duration: int) -> datetime:
    start += timedelta(minutes=duration)
    return start


if __name__ == '__main__':
    assert time_shift(2, (10, 10)) == 5
    assert time_shift(3, (12, 3, 30)) == 4
    assert time_travel(datetime(2024, 2, 10, 12, 0), 10) == datetime(2024, 2, 10, 12, 10)
    assert time_travel(datetime(2024, 2, 10, 12, 30), -15) == datetime(2024, 2, 10, 12, 15)
    assert time_travel(datetime(2024, 2, 10, 12, 30), time_shift(2, (10, 10))) \
           == datetime(2024, 2, 10, 12, 40)
