from main.day_25 import solve_1

input = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122",
]


def test_solve_1():
    assert solve_1(input) == "2=-1=0"
