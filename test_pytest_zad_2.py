from pytest_zad_2 import *

def test_time_shift():
    assert time_shift(2, (10, 10)) == 5
    assert time_shift(3, (12, 3, 30)) == 4

def test_time_travel():
    assert time_travel(datetime(2024, 2, 10, 12, 0), 10) == datetime(2024, 2, 10, 12, 10)
    assert time_travel(datetime(2024, 2, 10, 12, 30), -15) == datetime(2024, 2, 10, 12, 15)

def test_intergration():
    assert time_travel(datetime(2024, 2, 10, 12, 30), time_shift(2, (10, 10))) \
           == datetime(2024, 2, 10, 12, 35)

