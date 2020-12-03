#!/usr/bin/env python3

with open("input.txt") as file:
    # input = file.readlines()
    input = [line.strip() for line in file.readlines()]

SAMPLE = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().split(
    "\n"
)


def traverse(input, dx, dy):
    x = 0
    y = 0
    tree = 0

    while y < len(input):
        line = input[y]
        if line[x] == "#":
            tree += 1
        x += dx
        y += dy

        if x >= len(line):
            x = x - len(line)
    return tree


def solve1(input):
    return traverse(input, 3, 1)


def solve2(input):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    out = 1
    for slope in slopes:
        trees = traverse(input, slope[0], slope[1])
        out = out * trees

    return out


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 7
    assert solve2(SAMPLE) == 336

    # Part 1
    part1 = solve1(input)
    # print(part1)
    assert part1 == 278

    # Part 2
    part2 = solve2(input)
    print(part2)
    assert part2 == 9709761600
