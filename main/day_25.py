from main.file_reader import read


def solve_1(input: list) -> str:
    return intToSnafu(sum(snafuToInt(snafu) for snafu in input))


def snafuToInt(snafu: str) -> int:
    total = 0
    for i, c in enumerate(snafu):
        b = 5 ** (len(snafu) - i - 1)

        if c.isnumeric():
            total += int(c) * b
        elif c == "-":
            total += -1 * b
        elif c == "=":
            total += -2 * b
    return total


def intToSnafu(i: int) -> str:
    if i == 0:
        return ""
    a, b = divmod(i + 2, 5)
    return intToSnafu(a) + "=-012"[b]


if __name__ == "__main__":
    input = read("day25-01.txt")
    print(solve_1(input))  # 2-212-2---=00-1--102
