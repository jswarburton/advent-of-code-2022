from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    sizes = _parse_dir_sizes(input)
    return sum(size for size in sizes.values() if size <= 100000)


def solve_2(input: list) -> int:
    sizes = _parse_dir_sizes(input)
    free_space = 70000000 - sizes["/"]
    return min(size for size in sizes.values() if size >= 30000000 - free_space)


def _parse_dir_sizes(input: list) -> dict:
    sizes = defaultdict(int)
    current_location = []
    for line in input:
        if line.startswith("$ cd "):
            to = line[5:]
            if to == "..":
                current_location.pop()
            elif to == "/":
                current_location = [to]
            elif current_location[-1] == "/":
                current_location.append(current_location[-1] + to)
            else:
                current_location.append(current_location[-1] + "/" + to)
        elif line[0].isdigit():
            size = int(line.split(" ")[0])
            for dir in current_location:
                sizes[dir] = size + sizes[dir]
    return sizes


if __name__ == "__main__":
    input = read("day07-01.txt")
    print(solve_1(input))  # 1513699
    print(solve_2(input))  # 7991939
