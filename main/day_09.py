from main.file_reader import read


def solve_1(input: list) -> int:
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    tail_positions = {(tail_x, tail_y)}

    dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for line in input:
        dir, dist = line.split()
        dist = int(dist)

        for _ in range(dist):
            head_x += dirs[dir][0]
            head_y += dirs[dir][1]
            tail_x, tail_y = _move_tail((head_x, head_y), (tail_x, tail_y))
            tail_positions.add((tail_x, tail_y))

    return len(tail_positions)


def solve_2(input: list) -> int:
    head_x, head_y = 0, 0
    tail = [(0, 0)] * 9

    tail_positions = {tail[8]}

    dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for line in input:
        dir, dist = line.split()
        dist = int(dist)

        for _ in range(dist):
            head_x += dirs[dir][0]
            head_y += dirs[dir][1]
            tail[0] = _move_tail((head_x, head_y), tail[0])
            for i in range(1, 9):
                tail[i] = _move_tail(tail[i - 1], tail[i])
            tail_positions.add(tail[8])

    return len(tail_positions)


def _move_tail(head_pos, tail_pos):
    dist_x = abs(head_pos[0] - tail_pos[0])
    dist_y = abs(head_pos[1] - tail_pos[1])

    if dist_x >= 2 and dist_y >= 2:
        tail_pos = (
            head_pos[0] - 1 if tail_pos[0] < head_pos[0] else head_pos[0] + 1,
            head_pos[1] - 1 if tail_pos[1] < head_pos[1] else head_pos[1] + 1,
        )
    elif dist_x >= 2:
        tail_pos = (head_pos[0] - 1 if tail_pos[0] < head_pos[0] else head_pos[0] + 1, head_pos[1])
    elif dist_y >= 2:
        tail_pos = (head_pos[0], head_pos[1] - 1 if tail_pos[1] < head_pos[1] else head_pos[1] + 1)
    return tail_pos


if __name__ == "__main__":
    input = read("day09-01.txt")
    print(solve_1(input))  # 6081
    print(solve_2(input))  # 2487
