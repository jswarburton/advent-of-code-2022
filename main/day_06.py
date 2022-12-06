from main.file_reader import read


def solve_1(input: str) -> int:
    return _solve(input, 4)


def solve_2(input: str) -> int:
    return _solve(input, 14)


def _solve(line: str, num: int) -> int:
    for i in range(num, len(line)):
        if len(set(line[i - num : i])) == num:
            return i


if __name__ == "__main__":
    input = read("day06-01.txt")[0]
    print(solve_1(input))  # 1816
    print(solve_2(input))  # 2625
