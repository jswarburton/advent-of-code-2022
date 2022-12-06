from main.day_06 import solve_1, solve_2


def test_solve_1():
    assert solve_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert solve_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert solve_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert solve_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert solve_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_solve_2():
    assert solve_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert solve_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert solve_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert solve_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert solve_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
