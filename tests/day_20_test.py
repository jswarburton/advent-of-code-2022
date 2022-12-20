from main.day_20 import solve_1, solve_2

input = [1, 2, -3, 3, -2, 0, 4]


def test_solve_1():
    assert solve_1(input) == 3


def test_solve_2():
    assert solve_2(input) == 1623178306
