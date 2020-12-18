#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return line


def solve1(input):
    pass


def solve2(input):
    pass


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE)

    # Part 1
    part1 = solve1(input)
    # assert part1 ==
    print(part1)

    # Part 2
    # part2 = solve2(input)
    # assert part2 ==
    # print(part2)
