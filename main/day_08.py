from main.file_reader import read


def solve_1(input: list) -> int:
    visible = set()

    for i, line in enumerate(input):
        max_so_far = -1
        for j, num in enumerate(line):
            if int(num) > max_so_far:
                visible.add((i, j))
                max_so_far = int(num)

    for i, line in enumerate(input):
        max_so_far = -1
        for j, num in enumerate(reversed(line)):
            if int(num) > max_so_far:
                visible.add((i, len(line) - 1 - j))
                max_so_far = int(num)

    for j in range(len(input[0])):
        max_so_far = -1
        for i in range(len(input)):
            if int(input[i][j]) > max_so_far:
                visible.add((i, j))
                max_so_far = int(input[i][j])

    for j in range(len(input[0])):
        max_so_far = -1
        for i in reversed(range(len(input))):
            if int(input[i][j]) > max_so_far:
                visible.add((i, j))
                max_so_far = int(input[i][j])

    return len(visible)


def solve_2(input: list) -> int:
    max_score = 0

    for i, line in enumerate(input):
        for j, num in enumerate(line):
            height = int(num)

            max_down = 0
            for i2 in range(i + 1, len(input)):
                max_down = abs(i2 - i)
                if int(input[i2][j]) >= height:
                    break

            max_up = 0
            for i2 in reversed(range(i)):
                max_up = abs(i2 - i)
                if int(input[i2][j]) >= height:
                    break

            max_left = 0
            for j2 in reversed(range(j)):
                max_left = abs(j2 - j)
                if int(input[i][j2]) >= height:
                    break

            max_right = 0
            for j2 in range(j + 1, len(input[0])):
                max_right = abs(j2 - j)
                if int(input[i][j2]) >= height:
                    break

            score = max_down * max_right * max_left * max_up
            if score > max_score:
                max_score = score

    return max_score


if __name__ == "__main__":
    input = read("day08-01.txt")
    print(solve_1(input))  # 1533
    print(solve_2(input))  # 345744
