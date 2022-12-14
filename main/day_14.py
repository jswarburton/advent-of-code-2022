from main.file_reader import read


def solve_1(input: list) -> int:
    blocked_positions = _parse_blocked_positions(input)
    lowest_point = max(pos[1] for pos in blocked_positions)

    sand_positions = set()
    while True:
        pos = _find_final_pos(blocked_positions.union(sand_positions), lowest_point)
        if pos is None:
            break
        else:
            sand_positions.add(pos)

    return len(sand_positions)


def solve_2(input: list) -> int:
    blocked_positions = _parse_blocked_positions(input)
    lowest_point = max(pos[1] for pos in blocked_positions) + 2

    sand_positions = set()
    while True:
        pos = _find_final_pos(blocked_positions.union(sand_positions), lowest_point, floor=True)
        if pos == (500, 0):
            return len(sand_positions) + 1
        else:
            sand_positions.add(pos)


def _find_final_pos(all_blocked, max_y: int, floor=False):
    pos = (500, 0)

    while True:
        if (pos[0], pos[1] + 1) not in all_blocked:
            pos = (pos[0], pos[1] + 1)
        elif (pos[0] - 1, pos[1] + 1) not in all_blocked:
            pos = pos[0] - 1, pos[1] + 1
        elif (pos[0] + 1, pos[1] + 1) not in all_blocked:
            pos = pos[0] + 1, pos[1] + 1
        else:
            return pos

        if floor and pos[1] == max_y - 1:
            return pos

        if pos[1] >= max_y:
            # Falling off edge
            return None


def _parse_blocked_positions(input):
    blocked = set()
    for line in input:
        parts = line.split(" -> ")
        coords = [(int(part.split(",")[0]), int(part.split(",")[1])) for part in parts]

        for i in range(len(coords) - 1):
            start_x, start_y = coords[i]
            end_x, end_y = coords[i + 1]

            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    blocked.add((x, y))
    return blocked


if __name__ == "__main__":
    input = read("day14-01.txt")
    print(solve_1(input))  # 1003
    print(solve_2(input))  # 25771
