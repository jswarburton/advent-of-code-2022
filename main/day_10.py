from main.file_reader import read


def solve_1(input: list) -> int:
    cycle = 0

    total = 0
    num = 1

    for line in input:
        if line == "noop":
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                total += cycle * num
        else:
            cycle += 1

            if cycle in {20, 60, 100, 140, 180, 220}:
                total += cycle * num
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                total += cycle * num
            num += int(line[5:])

    return total


def solve_2(input: list) -> int:
    cycle = 0

    sprite_positions = {0, 1, 2}
    image = [[] for _ in range(6)]

    for line in input:
        if line == "noop":
            draw_pos = cycle % 40
            if draw_pos in sprite_positions:
                image[cycle // 40].append("#")
            else:
                image[cycle // 40].append(".")
            cycle += 1
        else:
            draw_pos = cycle % 40
            if draw_pos in sprite_positions:
                image[cycle // 40].append("#")
            else:
                image[cycle // 40].append(".")
            cycle += 1
            draw_pos = cycle % 40
            if draw_pos in sprite_positions:
                image[cycle // 40].append("#")
            else:
                image[cycle // 40].append(".")
            cycle += 1
            sprite_positions = {pos + int(line[5:]) for pos in sprite_positions}
    return ["".join(row) for row in image]


if __name__ == "__main__":
    input = read("day10-01.txt")
    print(solve_1(input))  # 14540
    print("\n".join(solve_2(input)))  # EHZFZHCZ
