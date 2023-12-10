import math
from dataclasses import dataclass
from typing import List

from main.file_reader import read


@dataclass
class Monkey:
    items: List[int]
    op: str
    divisor_test: int
    true_monkey: int
    false_monkey: int


def solve_1(input: list) -> int:
    return _solve(input, num_iterations=20, divisor=3)


def solve_2(input: list) -> int:
    return _solve(input, num_iterations=10000)


def _solve(input, num_iterations, divisor=1):
    monkeys = []
    for line in input:
        if line.startswith("  Starting items: "):
            items = list(map(int, line[len("  Starting items: ") :].split(",")))
        elif line.startswith("  Operation: new = "):
            op = line[len("  Operation: new = ") :]
        elif line.startswith("  Test: divisible by "):
            divisor_test = int(line[len("  Test: divisible by ") :])
        elif line.startswith("    If true: throw to monkey "):
            true_monkey = int(line[len("    If true: throw to monkey ") :])
        elif line.startswith("    If false: throw to monkey "):
            false_monkey = int(line[len("    If false: throw to monkey ") :])
        elif not line:
            monkeys.append(Monkey(items, op, divisor_test, true_monkey, false_monkey))
    monkeys.append(Monkey(items, op, divisor_test, true_monkey, false_monkey))

    divisor_product = math.prod([monkey.divisor_test for monkey in monkeys])

    counts = [0] * len(monkeys)
    for i in range(num_iterations):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                counts[i] += 1

                old = item
                current_worry_level = eval(monkey.op)
                current_worry_level //= divisor
                if current_worry_level % monkey.divisor_test == 0:
                    monkeys[monkey.true_monkey].items.append(
                        current_worry_level % divisor_product
                    )
                else:
                    monkeys[monkey.false_monkey].items.append(
                        current_worry_level % divisor_product
                    )
            monkey.items = []
    counts.sort()
    return counts[-1] * counts[-2]


if __name__ == "__main__":
    input = read("day11-01.txt")
    print(solve_1(input))  # 101436
    print(solve_2(input))  # 19754471646
