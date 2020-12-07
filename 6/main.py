#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


SAMPLE = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()


def parse_people(group):
    return [set(person) for person in group.split("\n")]


def solve1(input):

    count = 0
    for group in double_split(input, parse_people):
        qs = set()
        for person in group:
            qs = qs.union(person)
        count += len(qs)
    return count


def solve2(input):
    count = 0
    for group in double_split(input, parse_people):
        qs = None
        for person in group:
            if qs is None:
                qs = person
            qs = qs.intersection(person)
        count += len(qs)
    return count


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 11
    assert solve2(SAMPLE) == 6

    # Part 1
    part1 = solve1(input)
    assert part1 == 6612
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 3268
    print(part2)
