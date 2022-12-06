from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> str:
    stacks = _parse_stacks(input)
    longest_stack = max([len(s) for s in stacks])

    return _solve(input[longest_stack + 2 :], stacks, reverse=True)


def solve_2(input: list) -> str:
    stacks = _parse_stacks(input)
    longest_stack = max([len(s) for s in stacks])

    return _solve(input[longest_stack + 2 :], stacks, reverse=False)


def _parse_stacks(input: list) -> list:
    stacks = defaultdict(list)
    for line in input:
        if not line.lstrip().startswith("["):
            break
        for n, i in enumerate(range(0, len(line) - 2, 4)):
            content = line[i : i + 3].strip()
            if content:
                stacks[n].append(content[1])
    return [stacks[i] for i in range(len(stacks))]


def _solve(remaining_input, stacks, reverse: bool):
    for i in remaining_input:
        left, to = i.split(" to ")
        left, fr = left.split(" from ")
        _, num = left.split("move ")

        froms = stacks[int(fr) - 1][: int(num)]
        if reverse:
            froms.reverse()

        stacks[int(to) - 1] = froms + stacks[int(to) - 1]

        stacks[int(fr) - 1] = stacks[int(fr) - 1][int(num) :]
    return "".join([i[0] for i in stacks])


if __name__ == "__main__":
    input = read("day05-01.txt")
    print(solve_1(input))  # RTGWZTHLD
    print(solve_2(input))  # STHGRZZFR
