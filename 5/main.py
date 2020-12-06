#!/usr/bin/env python3
with open("input.txt") as file:
    input = [line.strip() for line in file.readlines()]


def parse_seat(code):
    code = code.replace("L", "0").replace("R", "1")
    code = code.replace("F", "0").replace("B", "1")

    row = int(code[:7], 2)
    col = int(code[7:], 2)

    return row * 8 + col


def solve1(input):
    high = 0
    for line in input:
        id = parse_seat(line)
        if id > high:
            high = id

    return high


def solve2(input):
    OPEN = "o"
    TAKEN = "x"
    seats = [OPEN] * 128 * 8

    for line in input:
        id = parse_seat(line)
        seats[id] = TAKEN

    first = seats.index(TAKEN)
    return seats.index(OPEN, first)


if __name__ == "__main__":
    # Tests
    assert parse_seat("FBFBBFFRLR") == 357
    assert parse_seat("BFFFBBFRRR") == 567
    assert parse_seat("FFFBBBFRRR") == 119
    assert parse_seat("BBFFBBFRLL") == 820

    # Part 1
    part1 = solve1(input)
    assert part1 == 978
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 727
    print(part2)
