from main import file_reader
from main.day_13 import solve_1, solve_2

input = file_reader.read(file_name="day13.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input) == 13


def test_solve_2():
    assert solve_2(input) == 140
