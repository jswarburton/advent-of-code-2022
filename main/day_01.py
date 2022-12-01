from main.file_reader import read


def solve_1(input: list) -> int:
    groups = _parse_groups(input)
    return max(sum(group) for group in groups)


def solve_2(input: list) -> int:
    groups = _parse_groups(input)

    sums = [sum(group) for group in groups]
    sums.sort()

    return sum(sums[-3:])


def _parse_groups(input):
    groups = []
    elems = []
    for i in input:
        if not i:
            groups.append(elems)
            elems = []
        else:
            elems.append(int(i))
    groups.append(elems)
    return groups


if __name__ == "__main__":
    input = read("day01-01.txt")
    print(solve_1(input))  # 69177
    print(solve_2(input))  # 207456
