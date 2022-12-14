from main.file_reader import read


def solve_1(input: list) -> int:
    start = [
        (row, col) for row, line in enumerate(input) for col, e in enumerate(line) if e == "S"
    ][0]
    end = [(row, col) for row, line in enumerate(input) for col, e in enumerate(line) if e == "E"][
        0
    ]

    return _fewest_steps(input, start, end)


def solve_2(input: list) -> int:
    starts = [
        (row, col)
        for row, line in enumerate(input)
        for col, e in enumerate(line)
        if e == "S" or e == "a"
    ]
    end = [(row, col) for row, line in enumerate(input) for col, e in enumerate(line) if e == "E"][
        0
    ]

    return min(_fewest_steps(input, start, end) for start in starts)


def _fewest_steps(input, start, end) -> int:
    start_row, start_col = start
    end_row, end_col = end

    def height(r, c):
        if input[r][c] == "S":
            return ord("a")
        if input[r][c] == "E":
            return ord("z")
        return ord(input[r][c])

    rows, cols = len(input), len(input[0])
    steps = [[9999999999] * cols for _ in range(rows)]
    steps[start_row][start_col] = 0

    queue = [(start_row, start_col)]
    while queue:
        row, col = queue[0]
        queue = queue[1:]
        for dir_row, dir_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dir_row, col + dir_col
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and steps[new_row][new_col] == 9999999999
                and height(new_row, new_col) <= height(row, col) + 1
            ):
                steps[new_row][new_col] = steps[row][col] + 1
                queue.append((new_row, new_col))

    return steps[end_row][end_col]


if __name__ == "__main__":
    input = read("day12-01.txt")
    print(solve_1(input))  # 449
    print(solve_2(input))  # 443
