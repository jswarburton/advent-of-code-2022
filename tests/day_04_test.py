from main.day_04 import solve_1, solve_2

input = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def test_solve_1():
    assert solve_1(input) == 2


def test_solve_2():
    assert solve_2(input) == 4
