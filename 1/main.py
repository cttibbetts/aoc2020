#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.readlines()


def find_sum(x, input, sum):
    for y in input:
        y = int(y)
        if y == x:
            continue

        if (x + y) == sum:
            return y
    return None


def solve1(input):
    for val in input:
        val = int(val)
        second = find_sum(val, input, 2020)
        if second is not None:
            return int(val) * int(second)


def solve2(input):
    for val in input:
        val = int(val)
        new_sum = 2020 - val

        for x in input:
            x = int(x)
            y = find_sum(x, input, new_sum)
            if y is not None:
                return val * x * y


if __name__ == "__main__":
    # Tests
    assert solve1([1721, 979, 366, 299, 675, 1456]) == 514579
    assert solve2([1721, 979, 366, 299, 675, 1456]) == 241861950

    # Part 1
    part1 = solve1(input)
    # print(part1)
    assert part1 == 63616

    # Part 2
    part2 = solve2(input)
    print(part2)
    assert part2 == 67877784
