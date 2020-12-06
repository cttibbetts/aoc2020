#!/usr/bin/env python3

with open("input.txt") as file:
    input = [line.strip() for line in file.readlines()]
input.append("")

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
""".split(
    "\n"
)


def solve1(input):
    answers = {}
    count = 0
    for line in input:
        for c in line:
            answers[c] = True

        if not line:
            count += len(answers.keys())
            answers = {}

    return count


def solve2(input):
    answers = {}
    count = 0
    people = 0
    for line in input:
        if not line:
            for q, a in answers.items():
                if a == people:
                    count += 1
            answers = {}
            people = 0
            continue

        people += 1
        for c in line:
            answers[c] = answers.get(c, 0) + 1

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
