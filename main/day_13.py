import functools

from main.file_reader import read


def solve_1(input: list) -> int:
    pairs = []
    pair = []
    for line in input:
        if not line:
            pairs.append(pair)
            pair = []
        else:
            pair.append(eval(line))
    pairs.append(pair)

    return sum(i + 1 for i, (a, b) in enumerate(pairs) if compare(a, b) == -1)


def solve_2(input: list) -> int:
    lines = [eval(line) for line in input if line]
    lines.append([[2]])
    lines.append([[6]])

    sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))

    return (sorted_lines.index([[2]]) + 1) * (sorted_lines.index([[6]]) + 1)


def compare(a, b):
    if type(a) == list and type(b) == list:
        for a1, b1 in zip(a, b):
            comparison = compare(a1, b1)
            if comparison:
                return comparison

        return compare(len(a), len(b))
    elif type(a) == list:
        return compare(a, [b])
    elif type(b) == list:
        return compare([a], b)
    else:
        if a < b:
            return -1
        if b < a:
            return 1
        return 0


if __name__ == "__main__":
    input = read("day13-01.txt")
    print(solve_1(input))  # 5717
    print(solve_2(input))  # 25935
