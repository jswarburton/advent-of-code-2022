from main.file_reader import read


def solve_1(input: list) -> int:
    numbers = [(i, int(num)) for i, num in enumerate(input)]
    orig = [int(num) for num in input]

    numbers = _move(numbers, orig)

    index_zero = [n[1] for n in numbers].index(0)

    return sum(numbers[(index_zero + i) % len(numbers)][1] for i in [1000, 2000, 3000])


def _move(nums, orig):
    for i, num in enumerate(orig):
        next = (i, num)
        index = nums.index(next)

        l, r = nums[:index], nums[index + 1 :]
        temp = l + r

        next_pos = (index + num) % (len(nums) - 1)
        temp.insert(next_pos, next)

        nums = temp

    return nums


def solve_2(input: list) -> int:
    numbers = [(i, int(x) * 811589153) for i, x in enumerate(input)]
    orig = [int(num) * 811589153 for num in input]

    for _ in range(10):
        numbers = _move(numbers, orig)

    index_zero = [n[1] for n in numbers].index(0)

    return sum(numbers[(index_zero + i) % len(numbers)][1] for i in [1000, 2000, 3000])


if __name__ == "__main__":
    input = read("day20-01.txt")
    print(solve_1(input))  # 13883
    print(solve_2(input))  # 19185967576920
