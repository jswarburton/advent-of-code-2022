from main.file_reader import read


def solve_1(input: list) -> int:
    sum = 0
    for i in input:
        first, second = i[: (len(i) // 2)], i[len(i) // 2 :]

        unique1, unique2 = set(first), set(second)
        in_all = unique1.intersection(unique2)

        ch = in_all.pop()

        if ord("a") <= ord(ch) <= ord("z"):
            sum += ord(ch) - ord("a") + 1
        else:
            sum += ord(ch) - ord("A") + 27

    return sum


def solve_2(input: list) -> int:
    groups = []
    group = []
    for i in input:
        if len(group) == 3:
            groups.append(group)
            group = [i]
        else:
            group.append(i)

    groups.append(group)

    sum = 0

    for g in groups:
        unique1, unique2, unique3 = set(g[0]), set(g[1]), set(g[2])
        in_all = unique1.intersection(unique2).intersection(unique3)

        ch = in_all.pop()

        if ord("a") <= ord(ch) <= ord("z"):
            sum += ord(ch) - ord("a") + 1
        else:
            sum += ord(ch) - ord("A") + 27

    return sum


if __name__ == "__main__":
    input = read("day03-01.txt")
    print(solve_1(input))  # 7990
    print(solve_2(input))  # 2602
