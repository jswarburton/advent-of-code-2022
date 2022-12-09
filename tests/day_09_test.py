from main import file_reader
from main.day_09 import solve_1, solve_2

input_01 = file_reader.read(file_name="day09_01.txt", path="tests/resources")
input_02 = file_reader.read(file_name="day09_02.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input_01) == 13


def test_solve_2():
    assert solve_2(input_02) == 36
