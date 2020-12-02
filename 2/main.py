#!/usr/bin/env python3

SAMPLE = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip().split(
    "\n"
)

with open("input.txt") as file:
    input = file.readlines()


def parse(line):
    vals = line.split(" ")
    r = vals[0].split("-")
    return int(r[0]), int(r[1]), vals[1][0], vals[2]


def valid(low, high, letter, word):
    count = 0
    for c in word:
        if c == letter:
            count += 1
    return low <= count <= high


def valid2(pos1, pos2, letter, word):
    is1 = word[pos1 - 1] == letter
    is2 = word[pos2 - 1] == letter

    return is1 != is2


def solve1(input):
    count_valid = 0
    for line in input:
        low, high, letter, word = parse(line)
        if valid(low, high, letter, word):
            count_valid += 1
    return count_valid


def solve2(input):
    count_valid = 0
    for line in input:
        low, high, letter, word = parse(line)
        if valid2(low, high, letter, word):
            count_valid += 1
    return count_valid


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 2
    assert solve2(SAMPLE) == 1

    # Part 1
    part1 = solve1(input)
    assert part1 == 620
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 727
    print(part2)
