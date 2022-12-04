from main.file_reader import read


def solve_1(input: list) -> int:
    count = 0
    for i in input:
        left, right = i.split(",")

        l1, l2 = left.split("-")
        r1, r2 = right.split("-")

        all_left = {i for i in range(int(l1), int(l2) + 1)}
        all_right = {i for i in range(int(r1), int(r2) + 1)}

        if all_left.issubset(all_right) or all_right.issubset(all_left):
            count += 1

    return count


def solve_2(input: list) -> int:
    count = 0
    for i in input:
        left, right = i.split(",")

        l1, l2 = left.split("-")
        r1, r2 = right.split("-")

        allleft = {i for i in range(int(l1), int(l2) + 1)}
        allright = {i for i in range(int(r1), int(r2) + 1)}

        if len(allleft.intersection(allright)) > 0:
            count += 1

    return count


if __name__ == "__main__":
    input = read("day04-01.txt")
    print(solve_1(input))  # 471
    print(solve_2(input))  # 888
