#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def find_sum(x, input, sum):
    for y in input:
        y = int(y)
        if y == x:
            continue

        if (x + y) == sum:
            return y


def has_sum(value, list):
    for x in list:
        y = find_sum(x, list, value)
        if y is not None:
            return x, y
    return None


def parse(line):
    return int(line)


def solve1(input, preamble_len=25):
    preamble = []
    for value in input_split(input, parse):
        if len(preamble) < preamble_len:
            preamble.append(value)
            continue

        if not has_sum(value, preamble):
            return value

        preamble.append(value)
        preamble = preamble[1:]


def sum_list(list):
    i = 0
    for x in list:
        i += x
    return i


def solve2(input, inv):
    sets = []
    for value in input_split(input, parse):
        sets.append([])

        for i, values in enumerate(sets):
            sets[i].append(value)
            if sum(sets[i]) == inv:
                sums = sorted(sets[i])
                return sums[0] + sums[-1]


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE, 5) == 127
    assert solve2(SAMPLE, 127) == 62

    # Part 1
    part1 = solve1(input)
    assert part1 == 1038347917
    # print(part1)

    # Part 2
    part2 = solve2(input, part1)
    assert part2 == 137394018
    print(part2)
