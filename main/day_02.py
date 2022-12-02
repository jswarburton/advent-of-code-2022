from main.file_reader import read


def solve_1(input: list) -> int:
    score = 0
    for i in input:
        a, b = i.split(" ")

        if a == "A":
            if b == "X":
                score += 1 + 3
            elif b == "Y":
                score += 2 + 6
            else:
                score += 3 + 0
        elif a == "B":
            if b == "X":
                score += 1 + 0
            elif b == "Y":
                score += 2 + 3
            else:
                score += 3 + 6
        else:
            if b == "X":
                score += 1 + 6
            elif b == "Y":
                score += 2 + 0
            else:
                score += 3 + 3

    return score


def solve_2(input: list) -> int:
    score = 0
    for i in input:
        a, b = i.split(" ")

        if a == "A":
            if b == "X":
                score += 3 + 0
            elif b == "Y":
                score += 1 + 3
            else:
                score += 2 + 6
        elif a == "B":
            if b == "X":
                score += 1 + 0
            elif b == "Y":
                score += 2 + 3
            else:
                score += 3 + 6
        else:
            if b == "X":
                score += 2 + 0
            elif b == "Y":
                score += 3 + 3
            else:
                score += 1 + 6

    return score


if __name__ == "__main__":
    input = read("day02-01.txt")
    print(solve_1(input))  # 11906
    print(solve_2(input))  # 11186
